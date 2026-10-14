"""Download OpenStreetMap geometry for every bridge on the map.

Writes bridge-geometry.json beside this script. Each entry has the bridge
ways near that catalogue centre, plus the roads and railways that share a
node with those ways: the approaches, the ramps, and the cross road.

The map script is the catalogue. Centres are the plotted points, not a new survey.
"""

from __future__ import annotations

import importlib.util
import json
import math
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "bridge-geometry.json"
CACHE = Path(r"D:\Code\msfs-airports\_build\osm-bridge-cache")
MAP = "https://api.openstreetmap.org/api/0.6/map?bbox={minlon},{minlat},{maxlon},{maxlat}"

KEEP_TAGS = {
    "name", "ref", "highway", "railway", "bridge", "layer", "lanes", "oneway",
    "maxspeed", "destination", "destination:ref", "bridge:structure", "bridge:name",
    "man_made", "service", "junction", "surface", "width", "maxheight", "foot",
    "bicycle", "cycleway", "sidewalk", "note", "alt_name", "official_name",
}


def load_catalogue():
    spec = importlib.util.spec_from_file_location("draw_map", HERE / "draw-map.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rows = []
    for kind, table in (("river", module.RIVER), ("freeway", module.FREEWAY), ("left_off", module.SKIPPED)):
        for code, name, lat, lon, estimated in table:
            rows.append({
                "code": code,
                "name": name,
                "list": kind,
                "lat": lat,
                "lon": lon,
                "estimated": estimated,
            })
    return rows


def metres(lat1, lon1, lat2, lon2) -> float:
    scale = 111_320
    x = (lon2 - lon1) * math.cos(math.radians((lat1 + lat2) / 2)) * scale
    y = (lat2 - lat1) * scale
    return math.hypot(x, y)


def clusters(rows):
    """Groups of nearby centres. A box wider than about 2 km is split."""
    pending = [rows]
    accepted = []
    while pending:
        group = pending.pop()
        lats = [r["lat"] for r in group]
        lons = [r["lon"] for r in group]
        span_lat = max(lats) - min(lats)
        span_lon = max(lons) - min(lons)
        if len(group) > 1 and (span_lat > 0.018 or span_lon > 0.025 or len(group) > 5):
            key = "lat" if span_lat >= span_lon else "lon"
            group.sort(key=lambda r: r[key])
            mid = len(group) // 2
            pending.append(group[:mid])
            pending.append(group[mid:])
        else:
            accepted.append(group)
    return accepted


def fetch(box) -> ET.Element:
    minlat, minlon, maxlat, maxlon = box
    key = f"{minlat:.4f}_{minlon:.4f}_{maxlat:.4f}_{maxlon:.4f}"
    CACHE.mkdir(parents=True, exist_ok=True)
    cached = CACHE / f"{key}.xml"
    if cached.exists() and cached.stat().st_size > 200:
        return ET.fromstring(cached.read_text(encoding="utf-8"))
    url = MAP.format(minlon=minlon, minlat=minlat, maxlon=maxlon, maxlat=maxlat)
    req = urllib.request.Request(url, headers={"User-Agent": "msfs-airports/0.1 (bridge geometry)"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read()
    except urllib.error.HTTPError as exc:
        if exc.code == 400:
            return None
        raise
    cached.write_bytes(raw)
    time.sleep(0.8)
    return ET.fromstring(raw)


def box_for(group, pad=0.004):
    lats = [r["lat"] for r in group]
    lons = [r["lon"] for r in group]
    return (min(lats) - pad, min(lons) - pad, max(lats) + pad, max(lons) + pad)


def parse(root):
    nodes = {}
    for node in root.findall("node"):
        nodes[node.get("id")] = (float(node.get("lat")), float(node.get("lon")))
    ways = []
    for way in root.findall("way"):
        tags = {t.get("k"): t.get("v") for t in way.findall("tag")}
        refs = [n.get("ref") for n in way.findall("nd")]
        pts = [nodes[ref] for ref in refs if ref in nodes]
        if len(pts) < 2:
            continue
        ways.append({"id": int(way.get("id")), "tags": tags, "refs": refs, "pts": pts})
    return ways


def way_record(way) -> dict:
    tags = {k: v for k, v in way["tags"].items() if k in KEEP_TAGS or k.startswith("bridge")}
    return {
        "osm_way": way["id"],
        "tags": tags,
        "nodes": [[round(lat, 6), round(lon, 6)] for lat, lon in way["pts"]],
    }


def nearest(way, lat, lon) -> float:
    return min(metres(lat, lon, p[0], p[1]) for p in way["pts"])


def nearest_segment(way, points) -> float:
    """Metres from any point to the closest segment of the way, not just its nodes."""
    best = float("inf")
    pts = way["pts"]
    for lat, lon in points:
        for (alat, alon), (blat, blon) in zip(pts, pts[1:]):
            # Project in a local metre frame.
            cos = math.cos(math.radians(lat))
            ax, ay = (alon - lon) * 111_320 * cos, (alat - lat) * 111_320
            bx, by = (blon - lon) * 111_320 * cos, (blat - lat) * 111_320
            dx, dy = bx - ax, by - ay
            length = dx * dx + dy * dy
            t = 0 if length == 0 else max(0, min(1, -(ax * dx + ay * dy) / length))
            best = min(best, math.hypot(ax + t * dx, ay + t * dy))
    return best


def role_of(way, bridge_ways) -> str:
    highway = way["tags"].get("highway") or ""
    if highway.endswith("_link"):
        return "ramp"
    names = set()
    refs = set()
    for bridge in bridge_ways:
        if bridge["tags"].get("name"):
            names.add(bridge["tags"]["name"])
        if bridge["tags"].get("ref"):
            refs.add(bridge["tags"]["ref"])
    if way["tags"].get("name") and way["tags"]["name"] in names:
        return "approach"
    if way["tags"].get("ref") and way["tags"]["ref"] in refs:
        return "approach"
    return "cross_road"


def is_bridge(way) -> bool:
    return way["tags"].get("bridge") in {"yes", "viaduct", "trestle"}


def grow_bridges(seeds, ways, lat, lon):
    """Follow bridge ways that continue the same deck, out to 800 m."""
    chosen = list(seeds)
    ids = {w["id"] for w in chosen}
    refs = {ref for w in chosen for ref in w["refs"]}
    changed = True
    while changed:
        changed = False
        for way in ways:
            if way["id"] in ids or not is_bridge(way):
                continue
            if not refs.intersection(way["refs"]):
                continue
            if nearest(way, lat, lon) > 800:
                continue
            chosen.append(way)
            ids.add(way["id"])
            refs.update(way["refs"])
            changed = True
    return chosen


def entry_for(row, ways, centres=None) -> dict:
    lat, lon = row["lat"], row["lon"]
    centres = centres or [(lat, lon)]
    bridges = [w for w in ways if is_bridge(w) and any(nearest(w, c[0], c[1]) <= 180 for c in centres)]
    widened = False
    if not bridges:
        bridges = [w for w in ways if is_bridge(w) and any(nearest(w, c[0], c[1]) <= 400 for c in centres)]
        widened = bool(bridges)
    bridges = grow_bridges(bridges, ways, lat, lon)
    bridge_refs = {ref for w in bridges for ref in w["refs"]}
    bridge_ids = {w["id"] for w in bridges}
    pedestrian = {"footway", "cycleway", "path", "steps"}
    bridge_is_pedestrian = any(b["tags"].get("highway") in pedestrian or not b["tags"].get("highway") for b in bridges)
    connected = []
    for way in ways:
        if way["id"] in bridge_ids:
            continue
        if not (way["tags"].get("highway") or way["tags"].get("railway")):
            continue
        if not bridge_refs.intersection(way["refs"]):
            continue
        highway = way["tags"].get("highway") or ""
        if highway in pedestrian and not bridge_is_pedestrian:
            continue
        record = way_record(way)
        record["role"] = role_of(way, bridges)
        connected.append(record)
    # The road underneath an overpass usually does not share a node with the deck.
    connected_ids = {c["osm_way"] for c in connected}
    bridge_nodes = [p for w in bridges for p in w["pts"]]
    for way in ways:
        if way["id"] in bridge_ids or way["id"] in connected_ids or is_bridge(way):
            continue
        highway = way["tags"].get("highway") or ""
        if highway in {"", "service", "footway", "cycleway", "path", "steps"}:
            continue
        if not bridge_nodes:
            continue
        if nearest_segment(way, bridge_nodes) > 45:
            continue
        record = way_record(way)
        record["role"] = "cross_road"
        connected.append(record)
    match = min((nearest(w, lat, lon) for w in bridges), default=None)
    return {
        "code": row["code"],
        "name": row["name"],
        "list": row["list"],
        "estimated_centre": row["estimated"],
        "centre": [round(lat, 6), round(lon, 6)],
        "match_m": None if match is None else round(match, 1),
        "widened_search": widened,
        "bridge_ways": [way_record(w) for w in bridges],
        "connected": connected,
    }


def main():
    rows = load_catalogue()
    groups = clusters(rows)
    print(f"{len(rows)} bridges in {len(groups)} boxes")
    found = {}
    for index, group in enumerate(groups, 1):
        root = fetch(box_for(group))
        if root is None and len(group) == 1:
            root = fetch(box_for(group, pad=0.002))
        if root is None:
            if len(group) == 1:
                print(f"  {index}/{len(groups)} box rejected for {group[0]['code']}")
                continue
            groups.extend([group[: len(group) // 2], group[len(group) // 2 :]])
            print(f"  {index} split a rejected box")
            continue
        ways = parse(root)
        for row in group:
            found[row["code"]] = entry_for(row, ways)
        print(f"  {index}/{len(groups)} {', '.join(r['code'] for r in group)}")

    # F20 is the midpoint of two decks. The estimated Yellowhead centres sit
    # north of the road, so look again on the road itself.
    extra_centres = {
        "F20": [(53.516, -113.431), (53.517, -113.386)],
    }
    for row in rows:
        if row["estimated"] and row["code"] not in extra_centres:
            extra_centres[row["code"]] = [(row["lat"] - 0.006, row["lon"])]
    for code, centres in extra_centres.items():
        item = found.get(code)
        if item and item["bridge_ways"] and code != "F20":
            continue
        row = next(r for r in rows if r["code"] == code)
        ways = []
        for lat, lon in centres:
            root = fetch(box_for([{"lat": lat, "lon": lon}]))
            if root is not None:
                ways.extend(parse(root))
        if not ways:
            continue
        found[code] = entry_for(row, ways, centres=[(row["lat"], row["lon"]), *centres])
        print(f"  retry {code}: {len(found[code]['bridge_ways'])} bridge ways")

    bridges = []
    missing = []
    for row in rows:
        item = found.get(row["code"])
        if item is None:
            item = entry_for(row, [])
            item["error"] = "map box was rejected"
        if not item["bridge_ways"]:
            missing.append(row["code"])
        bridges.append(item)

    notes = {
        "Y68": "Estimated from the street grid. No tagged bridge within 700 m.",
        "Y69": "Estimated from the street grid. No tagged bridge within 700 m.",
        "Y70": "Estimated from the street grid. No tagged bridge within 700 m.",
        "Y73": "Estimated from the street grid. No tagged bridge within 700 m.",
        "Y74": "Estimated from the street grid. No tagged bridge within 700 m.",
        "H30": "Whitemud Creek arch. OpenStreetMap does not tag a separate bridge on the Henday mainline here.",
    }
    for item in bridges:
        if item["code"] in notes and not item["bridge_ways"]:
            item["note"] = notes[item["code"]]

    document = {
        "source": "OpenStreetMap map API 0.6, bridge and connected highway/railway ways",
        "retrieved": "2026-10-14",
        "centre_note": "centre is the point plotted on edmonton-bridges-map.png. It is a deck centre from OpenStreetMap, or an estimate where estimated_centre is true.",
        "geometry_note": "bridge_ways are the tagged bridge, viaduct, or trestle within 180 m of the centre (400 m if the first pass was empty), plus bridge ways that continue the same deck out to 800 m. connected ways are the approaches and ramps that share a node with the deck, and the cross road passing underneath within 45 m. role is approach when the name or ref matches the bridge, ramp for a link road, otherwise cross_road. Node lists are [lat, lon] in way order and stop at the edge of the downloaded box.",
        "bridges": bridges,
    }
    OUT.write_text(json.dumps(document, indent=2), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes), {len(missing)} without a bridge way: {' '.join(missing)}")


if __name__ == "__main__":
    main()
