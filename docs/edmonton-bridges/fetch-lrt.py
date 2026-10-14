"""Download Edmonton light-rail geometry and write a modelling file.

Writes lrt-tracks.json beside this script. Open ways are chained into
polylines. Construction and proposed ways are kept separate. Stations are
the named light-rail nodes. This is the above-ground routing to reuse if
the track is modelled later.
"""

from __future__ import annotations

import json
import math
import urllib.request
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
RAW = Path(r"D:\Code\msfs-airports\_build\osm-lrt.json")
OUT = HERE / "lrt-tracks.json"
QUERY = """
[out:json][timeout:90];
(
  way["railway"="light_rail"]({s},{w},{n},{e});
  way["railway"="construction"]["construction"="light_rail"]({s},{w},{n},{e});
  way["proposed:railway"="light_rail"]({s},{w},{n},{e});
  node["railway"="station"]({s},{w},{n},{e});
  node["railway"="stop"]({s},{w},{n},{e});
  node["public_transport"="stop_position"]["light_rail"="yes"]({s},{w},{n},{e});
);
out geom;
"""


ENDPOINTS = ("https://overpass.openstreetmap.fr/api/interpreter",)

# South, west, north, east. Overlapped so a way on a tile edge is not cut off.
TILES = (
    (53.49, -113.72, 53.57, -113.48),  # Valley Line West, Lewis Farms to downtown
    (53.49, -113.56, 53.60, -113.42),  # downtown, river, Metro to Blatchford
    (53.55, -113.52, 53.66, -113.36),  # Capital Line northeast and Gorman
    (53.42, -113.58, 53.53, -113.46),  # Capital Line south
    (53.44, -113.50, 53.55, -113.34),  # Valley Line Southeast
    (53.38, -113.62, 53.46, -113.46),  # Capital Line South extension
)


def fetch_tile(south, west, north, east) -> dict:
    query = QUERY.format(s=south, w=west, n=north, e=east)
    last = None
    for url in ENDPOINTS:
        req = urllib.request.Request(
            url,
            data=query.encode(),
            headers={"User-Agent": "msfs-airports/0.1 (edmonton lrt)"},
        )
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                return json.loads(resp.read())
        except Exception as exc:
            last = exc
            print(f"  {url} {south},{west} failed: {exc}")
    raise last


def fetch() -> dict:
    elements = []
    seen = set()
    for tile in TILES:
        data = fetch_tile(*tile)
        added = 0
        for element in data["elements"]:
            key = (element["type"], element["id"])
            if key in seen:
                continue
            seen.add(key)
            elements.append(element)
            added += 1
        print(f"  tile {tile}: {added} new")
    document = {"elements": elements}
    RAW.parent.mkdir(parents=True, exist_ok=True)
    RAW.write_text(json.dumps(document), encoding="utf-8")
    return document


def kind(tags: dict) -> str:
    railway = tags.get("railway", "")
    if railway == "construction" or tags.get("construction") == "light_rail":
        return "construction"
    if "proposed:railway" in tags or railway == "proposed":
        return "proposed"
    if tags.get("tunnel") in {"yes", "building_passage"} or tags.get("tunnel:name"):
        return "tunnel"
    if tags.get("bridge") in {"yes", "viaduct", "trestle"}:
        return "bridge"
    if tags.get("cutting") == "yes":
        return "cutting"
    if tags.get("embankment") == "yes":
        return "embankment"
    return "surface"


def round_pt(lat, lon):
    return [round(lat, 6), round(lon, 6)]


def chain(ways: list[dict]) -> list[list[list[float]]]:
    """Join ways that share an endpoint. Each way is used once."""
    unused = []
    for way in ways:
        pts = [round_pt(p["lat"], p["lon"]) for p in way.get("geometry", [])]
        if len(pts) >= 2:
            unused.append(pts)
    lines = []
    while unused:
        line = unused.pop()
        grew = True
        while grew:
            grew = False
            for i, pts in enumerate(unused):
                if pts[0] == line[-1]:
                    line.extend(pts[1:])
                elif pts[-1] == line[-1]:
                    line.extend(reversed(pts[:-1]))
                elif pts[-1] == line[0]:
                    line = pts[:-1] + line
                elif pts[0] == line[0]:
                    line = list(reversed(pts[1:])) + line
                else:
                    continue
                unused.pop(i)
                grew = True
                break
        lines.append(line)
    return lines


def length_m(line) -> float:
    total = 0.0
    for (a_lat, a_lon), (b_lat, b_lon) in zip(line, line[1:]):
        scale = 111_320
        x = (b_lon - a_lon) * math.cos(math.radians((a_lat + b_lat) / 2)) * scale
        y = (b_lat - a_lat) * scale
        total += math.hypot(x, y)
    return total


def main():
    data = fetch()
    ways = [e for e in data["elements"] if e["type"] == "way"]
    nodes = [e for e in data["elements"] if e["type"] == "node"]
    relations = [e for e in data["elements"] if e["type"] == "relation"]

    grouped = defaultdict(list)
    way_notes = []
    for way in ways:
        tags = way.get("tags", {})
        # Road construction shares railway=construction. Keep light rail only.
        if tags.get("railway") == "construction" and tags.get("construction") not in {None, "light_rail", "rail"}:
            continue
        if tags.get("railway") == "construction" and tags.get("construction") == "rail":
            continue
        item_kind = kind(tags)
        way["_kind"] = item_kind
        grouped[(item_kind, tags.get("service") or "")].append(way)
        way_notes.append({
            "osm_way": way["id"],
            "kind": item_kind,
            "name": tags.get("name"),
            "bridge": tags.get("bridge"),
            "tunnel": tags.get("tunnel"),
            "layer": tags.get("layer"),
            "service": tags.get("service"),
            "usage": tags.get("usage"),
            "construction": tags.get("construction"),
        })

    routes = []
    for (item_kind, service), group in sorted(grouped.items()):
        for line in chain(group):
            routes.append({
                "kind": item_kind,
                "service": service or None,
                "length_m": round(length_m(line)),
                "points": line,
            })

    stations = []
    for node in nodes:
        tags = node.get("tags", {})
        name = tags.get("name")
        if not name:
            continue
        light = (
            tags.get("light_rail") == "yes"
            or tags.get("station") == "light_rail"
            or tags.get("subway") == "yes"
            or "lrt" in name.lower()
            or tags.get("operator") in {"ETS", "Edmonton Transit Service"}
        )
        if tags.get("train") == "yes" and tags.get("light_rail") != "yes":
            continue
        stations.append({
            "name": name,
            "lat": round(node["lat"], 6),
            "lon": round(node["lon"], 6),
            "railway": tags.get("railway"),
            "station": tags.get("station"),
            "light_rail": tags.get("light_rail"),
            "subway": tags.get("subway"),
            "layer": tags.get("layer"),
            "level": tags.get("level"),
            "operator": tags.get("operator"),
        })

    track_pts = [pt for route in routes for pt in route["points"]]

    def near_track(lat, lon) -> bool:
        # A station node sits on the platform, not always on the rail.
        for tlat, tlon in track_pts[::3]:
            if abs(tlat - lat) > 0.002 or abs(tlon - lon) > 0.003:
                continue
            scale = 111_320
            x = (tlon - lon) * math.cos(math.radians(lat)) * scale
            y = (tlat - lat) * scale
            if math.hypot(x, y) < 150:
                return True
        return False

    stations = [s for s in stations if near_track(s["lat"], s["lon"]) or "lrt" in s["name"].lower()]
    # One row per name. Platforms are often tagged twice.
    unique = {}
    for station in stations:
        unique.setdefault(station["name"], station)
    stations = sorted(unique.values(), key=lambda s: (s["name"]))

    document = {
        "source": "OpenStreetMap via Overpass, railway=light_rail and construction ways, 2026-10-14",
        "note": "points are [lat, lon] along each chained way. kind is bridge, tunnel, cutting, embankment, surface, construction, or proposed. A bridge kind is the elevated or bridged piece. Construction ways are not in service. This file is the above-ground routing to reuse if the track is modelled later.",
        "routes": routes,
        "stations": stations,
        "way_count": len(way_notes),
    }
    OUT.write_text(json.dumps(document, indent=2), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
    print(f"ways {len(ways)} stations {len(stations)} polylines {len(routes)}")
    for (item_kind, service), group in sorted(grouped.items()):
        metres = sum(length_m([round_pt(p["lat"], p["lon"]) for p in w.get("geometry", [])]) for w in group)
        label = item_kind if not service else f"{item_kind}/{service}"
        print(f"  {label:22} ways {len(group):4}  {metres/1000:.1f} km")
    print("-- bridge polylines --")
    for route in routes:
        if route["kind"] != "bridge":
            continue
        mid = route["points"][len(route["points"]) // 2]
        print(f"  {route['length_m']:6} m  {mid[0]:.5f},{mid[1]:.5f}")
    print("-- stations --")
    for station in stations:
        print(f"  {station['lat']:.5f},{station['lon']:.5f}  {station['name']}")


if __name__ == "__main__":
    main()
