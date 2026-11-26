"""Map the airport obstacle limitation surfaces around CYXD and report the areas they cover.

Run from the repo root:  python -I tools/obstacle_surfaces.py [--buildings buildings.csv] [--rules rules.json]
                                                          [--radius 8000] [--cell 50] [--grid-csv out.csv]

Reads the runway thresholds and field elevation from airport-cyxd/PackageSources/Scenery/airport-cyxd/CYXD.xml. All three
runways are used, as if they were all open. It lays out the surfaces around the field and reports:
  - the area each surface covers, and the area covered by any surface;
  - the area where each surface is the lowest limit (the binding one);
  - for each building in --buildings (CSV with columns name,lat,lon,top_amsl_m and optional ground_amsl_m), whether its top
    is above the lowest cutoff at its position, and by how much. Ground elevation enables the 90 m and 150 m height tests.

To use from another script:
    from obstacle_surfaces import ObstacleModel
    model = ObstacleModel()
    model.clearance(53.5444, -113.4909, top_amsl_m=820, ground_amsl_m=670)
    # {'obstacle': True, 'margin_m': ..., 'cutoff_amsl_m': ..., 'cutoff': '...'}  (positive margin = above the cutoff)

The dimensions in RULES are placeholders in the shape of the ICAO Annex 14 / TP 312 surfaces for a non-precision runway. They are
NOT the rules that applied before 1995, and they have not been checked against TP 312E Chapter 4. Replace them with --rules FILE
(JSON, same keys as RULES).

Heights are metres above sea level (AMSL). Positions are local metres east (x) and north (y) of the field reference point.
"""

import argparse
import csv
import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SCENERY_XML = Path(__file__).resolve().parent.parent / "airport-cyxd" / "PackageSources" / "Scenery" / "airport-cyxd" / "CYXD.xml"
M_PER_DEG_LAT = 110574.0

RULES = {
    "approach": {"start_m": 60, "inner_width_m": 150, "divergence": 0.15, "length_m": 3000, "slope": 1 / 20},
    "takeoff": {"start_m": 0, "inner_width_m": 180, "divergence": 0.125, "length_m": 15000, "slope": 0.02},
    "transitional": {"strip_half_width_m": 75, "slope": 1 / 7, "longitudinal_margin_m": 60},
    "inner_horizontal": {"height_above_field_m": 45, "radius_m": 4000},
    "conical": {"slope": 1 / 20, "outer_height_m": 100},
}


def to_xy(lat, lon, lat0, lon0):
    """Local metres east and north of (lat0, lon0)."""
    return (
        (lon - lon0) * M_PER_DEG_LAT * math.cos(math.radians(lat0)),
        (lat - lat0) * M_PER_DEG_LAT,
    )


def read_field(xml_path):
    """Field reference point and runways (name, both thresholds as (x, y, alt), centre, length) from CYXD.xml."""
    root = ET.parse(xml_path).getroot()
    airport = root.find(".//Airport")
    lat0, lon0 = float(airport.get("lat")), float(airport.get("lon"))
    field_alt = float(airport.get("alt"))

    runways = []
    for rw in root.iter("Runway"):
        starts = {s.get("end"): s for s in rw.findall("RunwayStart")}
        if "PRIMARY" not in starts or "SECONDARY" not in starts:
            continue
        number = int(rw.get("number"))
        ends = []
        for key, label in (("PRIMARY", number), ("SECONDARY", (number + 18 - 1) % 36 + 1)):
            s = starts[key]
            x, y = to_xy(float(s.get("lat")), float(s.get("lon")), lat0, lon0)
            ends.append({"label": f"{label:02d}", "x": x, "y": y, "alt": float(s.get("alt"))})
        runways.append({"name": f"{number:02d}/{ends[1]['label']}", "ends": ends})
    return {"lat0": lat0, "lon0": lon0, "field_alt": field_alt, "runways": runways}


def unit(dx, dy):
    d = math.hypot(dx, dy)
    return dx / d, dy / d


def build_surfaces(field, rules):
    """Precompute the per-end and per-runway geometry used by evaluate()."""
    ends, centres = [], []
    for rw in field["runways"]:
        p, q = rw["ends"]
        for here, other in ((p, q), (q, p)):
            d = unit(here["x"] - other["x"], here["y"] - other["y"])  # outward from the runway, past this end
            ends.append({"runway": rw["name"], "label": here["label"], "x": here["x"], "y": here["y"],
                         "alt": here["alt"], "d": d, "n": (-d[1], d[0])})
        ux, uy = unit(q["x"] - p["x"], q["y"] - p["y"])
        centres.append({
            "runway": rw["name"],
            "x": (p["x"] + q["x"]) / 2, "y": (p["y"] + q["y"]) / 2,
            "u": (ux, uy), "n": (-uy, ux),
            "half_length": math.hypot(q["x"] - p["x"], q["y"] - p["y"]) / 2,
            "alt": (p["alt"] + q["alt"]) / 2,
        })
    return ends, centres


def evaluate(x, y, field, ends, centres, rules):
    """Every surface that covers (x, y), as a list of (surface name, limit AMSL in metres)."""
    out = []
    field_alt = field["field_alt"]

    for e in ends:
        dx, dy = x - e["x"], y - e["y"]
        a = dx * e["d"][0] + dy * e["d"][1]  # distance outward from this runway end
        t = abs(dx * e["n"][0] + dy * e["n"][1])  # distance sideways from the extended centreline
        ap = rules["approach"]
        if ap["start_m"] <= a <= ap["start_m"] + ap["length_m"]:
            half = ap["inner_width_m"] / 2 + ap["divergence"] * (a - ap["start_m"])
            if t <= half:
                out.append((f"{e['runway']} {e['label']} approach", e["alt"] + ap["slope"] * (a - ap["start_m"])))
        tk = rules["takeoff"]
        if tk["start_m"] <= a <= tk["start_m"] + tk["length_m"]:
            half = tk["inner_width_m"] / 2 + tk["divergence"] * (a - tk["start_m"])
            if t <= half:
                out.append((f"{e['runway']} {e['label']} take-off", e["alt"] + tk["slope"] * (a - tk["start_m"])))

    ih = rules["inner_horizontal"]
    ih_limit = field_alt + ih["height_above_field_m"]
    r = math.hypot(x, y)
    if r <= ih["radius_m"]:
        out.append(("inner horizontal", ih_limit))

    co = rules["conical"]
    if ih["radius_m"] < r <= ih["radius_m"] + co["outer_height_m"] / co["slope"]:
        out.append(("conical", ih_limit + co["slope"] * (r - ih["radius_m"])))

    tr = rules["transitional"]
    for c in centres:
        dx, dy = x - c["x"], y - c["y"]
        s = abs(dx * c["u"][0] + dy * c["u"][1])
        t = abs(dx * c["n"][0] + dy * c["n"][1])
        if s > c["half_length"] + tr["longitudinal_margin_m"] or t < tr["strip_half_width_m"]:
            continue
        limit = c["alt"] + tr["slope"] * (t - tr["strip_half_width_m"])
        if limit <= ih_limit:  # above this height the inner horizontal surface takes over
            out.append((f"{c['runway']} transitional", limit))
    return out


def lowest(covers):
    """(limit AMSL, binding surface name) for a list from evaluate(), or (None, None) if nothing covers the point."""
    if not covers:
        return None, None
    name, limit = min(covers, key=lambda item: item[1])
    return limit, name


OBSTACLE_HEIGHT_TESTS = {"low_m": 90, "low_radius_m": 6000, "high_m": 150}  # CARs 601.23(1)(b) and (d), heights above ground


class ObstacleModel:
    """CYXD's obstacle cutoffs for import: ObstacleModel().clearance(lat, lon, top_amsl_m, ground_amsl_m).

    clearance() returns a dict:
      obstacle       True if the top is above the lowest cutoff that applies here (lights needed under Standard 621)
      margin_m       top minus that cutoff, in metres: positive = above it (penetrates), negative = below it
      cutoff_amsl_m  the lowest cutoff AMSL that applies at this point (None if no cutoff applies)
      cutoff         which cutoff that is, e.g. "inner horizontal" or "90 m AGL within 6 km"
    Pass ground_amsl_m to include the 90 m and 150 m height tests; without it only the surfaces are checked.
    """

    def __init__(self, rules=None, xml_path=SCENERY_XML):
        self.rules = rules if rules is not None else RULES
        self.field = read_field(xml_path)
        self.ends, self.centres = build_surfaces(self.field, self.rules)

    def clearance(self, lat, lon, top_amsl_m, ground_amsl_m=None):
        x, y = to_xy(lat, lon, self.field["lat0"], self.field["lon0"])
        cutoffs = list(evaluate(x, y, self.field, self.ends, self.centres, self.rules))
        if ground_amsl_m is not None:
            if math.hypot(x, y) <= OBSTACLE_HEIGHT_TESTS["low_radius_m"]:
                low = OBSTACLE_HEIGHT_TESTS["low_m"]
                cutoffs.append((f"{low} m AGL within {OBSTACLE_HEIGHT_TESTS['low_radius_m'] // 1000} km", ground_amsl_m + low))
            high = OBSTACLE_HEIGHT_TESTS["high_m"]
            cutoffs.append((f"{high} m AGL", ground_amsl_m + high))
        if not cutoffs:
            return {"obstacle": False, "margin_m": None, "cutoff_amsl_m": None, "cutoff": None}
        name, limit = min(cutoffs, key=lambda item: item[1])
        return {
            "obstacle": top_amsl_m > limit,
            "margin_m": round(top_amsl_m - limit, 2),
            "cutoff_amsl_m": round(limit, 2),
            "cutoff": name,
        }


def read_buildings(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--buildings", type=Path, help="CSV: name,lat,lon,top_amsl_m")
    parser.add_argument("--rules", type=Path, help="JSON file replacing the placeholder RULES")
    parser.add_argument("--radius", type=float, default=8000, help="grid radius in metres around the field (default 8000)")
    parser.add_argument("--cell", type=float, default=50, help="grid cell size in metres (default 50)")
    parser.add_argument("--grid-csv", type=Path, help="write every covered cell: x_m,y_m,limit_amsl_m,binding_surface")
    args = parser.parse_args(argv)

    rules = json.loads(args.rules.read_text(encoding="utf-8")) if args.rules else RULES
    model = ObstacleModel(rules)
    field, ends, centres = model.field, model.ends, model.centres

    print(f"Field elevation {field['field_alt']:.1f} m AMSL; runways {', '.join(r['name'] for r in field['runways'])}")
    if args.rules is None:
        print("WARNING: placeholder rules (ICAO-style, not the pre-1995 rules). Use --rules FILE for real dimensions.")

    cell_area = args.cell * args.cell
    coverage, binding, union = {}, {}, 0
    grid_rows = []
    steps = int(args.radius // args.cell)
    for i in range(-steps, steps + 1):
        for j in range(-steps, steps + 1):
            x, y = i * args.cell, j * args.cell
            covers = evaluate(x, y, field, ends, centres, rules)
            if not covers:
                continue
            union += 1
            for name, _ in covers:
                coverage[name] = coverage.get(name, 0) + 1
            limit, name = lowest(covers)
            binding[name] = binding.get(name, 0) + 1
            if args.grid_csv:
                grid_rows.append((x, y, limit, name))

    km2 = lambda n: n * cell_area / 1e6  # noqa: E731
    print(f"\nArea under any surface: {km2(union):.2f} km2 (grid {args.cell:g} m, radius {args.radius:g} m)")
    print(f"\n{'surface':<28}{'covers km2':>12}{'lowest limit km2':>18}")
    for name in sorted(coverage, key=lambda k: -coverage[k]):
        print(f"{name:<28}{km2(coverage[name]):>12.2f}{km2(binding.get(name, 0)):>18.2f}")

    if args.grid_csv:
        with open(args.grid_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["x_m", "y_m", "limit_amsl_m", "binding_surface"])
            w.writerows((x, y, round(limit, 2), name) for x, y, limit, name in grid_rows)
        print(f"\nWrote {len(grid_rows)} covered cells to {args.grid_csv}")

    if args.buildings:
        rows = read_buildings(args.buildings)
        print(f"\nBuildings: {len(rows)}")
        penetrating = []
        for row in rows:
            ground = row.get("ground_amsl_m") or None
            c = model.clearance(float(row["lat"]), float(row["lon"]), float(row["top_amsl_m"]),
                                float(ground) if ground else None)
            if c["obstacle"]:
                penetrating.append((c["margin_m"], row.get("name", ""), float(row["top_amsl_m"]), c["cutoff_amsl_m"], c["cutoff"]))
        print(f"Above a cutoff: {len(penetrating)}")
        for margin, bname, top, limit, sname in sorted(penetrating, reverse=True):
            print(f"  {bname:<36} top {top:7.1f}  cutoff {limit:7.1f}  over by {margin:6.1f} m  ({sname})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
