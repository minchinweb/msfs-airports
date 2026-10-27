"""Print what the sim has for an airport (runways, starts, parking, taxi paths, frequencies, approaches), read from Little Navmap's database.

Run from the repo root:  python -I tools/sim_airport.py H28 [CYXD ...] [--sim msfs] [--json out.json]
Little Navmap fills its database from the sim through SimConnect's facilities API, so the data is only as fresh as its last
"Load Scenery Library"; the date is printed first. Lengths, widths and altitudes are feet as stored, with metres added;
headings are true. The database is opened read-only, so Little Navmap can stay running.
"""
import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

DB_DIR = Path(os.environ.get("APPDATA", "")) / "ABarthel/little_navmap_db"
DB_NAMES = {"msfs24": "little_navmap_msfs24.sqlite", "msfs": "little_navmap_msfs.sqlite"}
FT = 0.3048
BLOBS = {"vertices", "vertices2", "triangles", "geometry"}


def rows(db, sql, *args):
    """Query results as dicts, without binary columns (apron geometry)."""
    cur = db.execute(sql, args)
    names = [d[0] for d in cur.description]
    return [{k: v for k, v in zip(names, r) if k not in BLOBS} for r in cur]


def data_date(db, path):
    """When Little Navmap last loaded the scenery library, and which build did it."""
    meta = rows(db, "select * from metadata")[0]
    loaded = datetime.fromisoformat(meta["last_load_timestamp"])
    return {
        "database": str(path),
        "last_load": loaded.isoformat(timespec="seconds"),
        "age_days": (datetime.now() - loaded).days,
        "data_source": meta["data_source"],
        "airac_cycle": meta["airac_cycle"],
        "compiler": meta["compiler_version"],
    }


def airport(db, ident):
    """Everything the database holds for one airport, or None if the ident is not there."""
    found = rows(db, "select * from airport where ident = ?", ident.upper())
    if not found:
        return None
    a = found[0]
    aid = a["airport_id"]
    ends = {e["runway_end_id"]: e for e in rows(
        db, "select e.* from runway_end e join runway r on e.runway_end_id in (r.primary_end_id, r.secondary_end_id)"
            " where r.airport_id = ?", aid)}
    runways = rows(db, "select * from runway where airport_id = ?", aid)
    for r in runways:
        r["primary_end"] = ends.get(r["primary_end_id"])
        r["secondary_end"] = ends.get(r["secondary_end_id"])
    return {
        "airport": a,
        "com": rows(db, "select * from com where airport_id = ?", aid),
        "runways": runways,
        "starts": rows(db, "select * from start where airport_id = ?", aid),
        "helipads": rows(db, "select * from helipad where airport_id = ?", aid),
        "parking": rows(db, "select * from parking where airport_id = ?", aid),
        "taxi_paths": rows(db, "select * from taxi_path where airport_id = ?", aid),
        "aprons": rows(db, "select * from apron where airport_id = ?", aid),
        "approaches": rows(db, "select * from approach where airport_id = ?", aid),
    }


def ft_m(ft):
    return "-" if ft is None else f"{ft:.0f} ft ({ft * FT:.1f} m)"


def pos(r):
    return f"{r['laty']:.6f}, {r['lonx']:.6f}"


def report(d):
    a = d["airport"]
    print(f"\n{a['ident']}  {a['name']}  (region {a['region']}, add-on: {'yes' if a['is_addon'] else 'no'})")
    print(f"  marker (ARP)  {pos(a)}   elevation {ft_m(a['altitude'])}   magvar {a['mag_var']:.2f}")
    print(f"  bounds        lat {a['bottom_laty']:.6f} to {a['top_laty']:.6f}, lon {a['left_lonx']:.6f} to {a['right_lonx']:.6f}")
    for c in d["com"]:
        print(f"  com           {c['type']} {c['frequency'] / 1e6:.3f} {c['name'] or ''}")
    for r in d["runways"]:
        p, s = r["primary_end"] or {}, r["secondary_end"] or {}
        print(f"  runway        {p.get('name')}/{s.get('name')}  {ft_m(r['length'])} x {ft_m(r['width'])}  surface {r['surface']}"
              f"  true hdg {r['heading']:.2f}  centre {pos(r)}  elev {ft_m(r['altitude'])}")
        for e in (p, s):
            if not e:
                continue
            extras = [f"{k} {e[k]}" for k in ("offset_threshold", "blast_pad", "overrun") if e[k]]
            extras += [f"{side} VASI {e[side + '_vasi_type']} {e[side + '_vasi_pitch']}"
                       for side in ("left", "right") if e[side + "_vasi_type"]]
            if e["app_light_system_type"]:
                extras.append(f"ALS {e['app_light_system_type']}")
            if e["ils_ident"]:
                extras.append(f"ILS {e['ils_ident']}")
            print(f"    end {e['name']:<4}  {pos(e)}  {'  '.join(extras)}")
    for s in d["starts"]:
        print(f"  start         {s['type']} {s['runway_name'] or s['number']}  {pos(s)}  hdg {s['heading']:.2f}  elev {ft_m(s['altitude'])}")
    for h in d["helipads"]:
        print(f"  helipad       {h['type']} {h['surface']}  {pos(h)}  {ft_m(h['length'])} x {ft_m(h['width'])}")
    for p in d["parking"]:
        print(f"  parking       {p['type']} {p['name']} {p['number']}{p['suffix'] or ''}  {pos(p)}  hdg {p['heading']:.1f}  radius {p['radius']} ft")
    named = sorted({t["name"] for t in d["taxi_paths"] if t["name"]})
    print(f"  taxi paths    {len(d['taxi_paths'])}" + (f"  (names: {', '.join(named)})" if named else ""))
    print(f"  aprons        {len(d['aprons'])}")
    for ap in d["approaches"]:
        print(f"  approach      {ap['type']} {ap['runway_name'] or ''}{ap['suffix'] or ''}  FAF {ap['fix_ident']}"
              f"  alt {ap['altitude']}  missed alt {ap['missed_altitude']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("idents", nargs="+", help="airport idents as the sim knows them, e.g. H28 CYXD")
    ap.add_argument("--sim", choices=DB_NAMES, default="msfs24", help="which Little Navmap database (default msfs24)")
    ap.add_argument("--db", type=Path, help="explicit path to a Little Navmap .sqlite file")
    ap.add_argument("--json", type=Path, help="also write everything found to this JSON file")
    args = ap.parse_args()

    path = args.db or DB_DIR / DB_NAMES[args.sim]
    if not path.exists():
        sys.exit(f"No Little Navmap database at {path}")
    db = sqlite3.connect(f"file:{path.as_posix()}?mode=ro", uri=True)

    meta = data_date(db, path)
    print(f"Little Navmap data: loaded {meta['last_load']} ({meta['age_days']} days ago), source {meta['data_source']},"
          f" {meta['compiler']}")
    print(f"  {path}")
    print("  Reload in Little Navmap (Scenery Library > Load Scenery Library) to pick up sim updates or new add-ons.")

    out = {"little_navmap": meta, "airports": {}}
    for ident in args.idents:
        d = airport(db, ident)
        if d is None:
            print(f"\n{ident.upper()}: not in this database")
            continue
        out["airports"][ident.upper()] = d
        report(d)

    if args.json:
        args.json.write_text(json.dumps(out, indent=2), encoding="utf-8")
        print(f"\nWrote {args.json}")


if __name__ == "__main__":
    main()
