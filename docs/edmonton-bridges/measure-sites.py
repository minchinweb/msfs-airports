"""Measurements from the 2018 LiDAR clips: bridge extent and height above ground along each mapped way, raised width (every deck at that level side by side, rails included),
terrain profiles at 25 m steps, and roof/outline heights for closed ways. Run in the venv with rasterio:  python measure-sites.py [site ...]
Writes data/measurements.json (all sites only), reference/<site>/elevation/profiles.csv, and (via write-measurements.py) the markdown.
Rise = DSM minus DTM at the same point: the height of the top surface (deck, rails, traffic) above bare ground. It is NOT
the clear height under the deck: subtract the deck depth (about 1 to 2.5 m, unknown per bridge). 1 m pixels: widths are +-1 m."""
import glob, json, os, sys
import numpy as np, rasterio
from rasterio.features import geometry_mask
from pyproj import Transformer
HERE = os.path.dirname(os.path.abspath(__file__))
T = Transformer.from_crs(4326, 3979, always_xy=True)
RISE_MIN = 3.0      # DSM above DTM by more than this = on a bridge or structure
STEP, PSTEP = 2.0, 25.0
DECK_PARTS = ("road_deck", "sidewalk", "bike_lane", "lrt", "east_", "west_", "pedestrian", "upper", "lower", "scona", "connors", "avenue", "north_", "south_", "footbridge", "cycleway")


def collect(o, out, path=""):
    if isinstance(o, dict):
        if "nodes" in o and isinstance(o["nodes"], list): out.append((path.strip("/").split("/")[0], o))
        for k, v in o.items(): collect(v, out, path + "/" + k)
    elif isinstance(o, list):
        for v in o: collect(v, out, path)


class Grid:
    def __init__(s, dsm_p, dtm_p):
        s.a = rasterio.open(dsm_p)
        s.dsm = s.a.read(1, masked=True).astype(float).filled(np.nan)
        s.dtm = rasterio.open(dtm_p).read(1, masked=True).astype(float).filled(np.nan)

    def at(s, arr, x, y):
        r, c = s.a.index(x, y)
        if not (1 <= r < arr.shape[0] - 1 and 1 <= c < arr.shape[1] - 1): return np.nan
        w = arr[r - 1:r + 2, c - 1:c + 2]
        return np.nanmedian(w) if np.isfinite(w).any() else np.nan


def line_samples(nodes, step):
    pts = [T.transform(lon, lat) for lat, lon in nodes]; out = []; ch = 0.0
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        L = float(np.hypot(x1 - x0, y1 - y0))
        if L == 0: continue
        n = max(1, int(L / step)); ux, uy = (x1 - x0) / L, (y1 - y0) / L
        for k in range(n):
            out.append((ch + L * k / n, x0 + (x1 - x0) * k / n, y0 + (y1 - y0) * k / n, ux, uy))
        ch += L
    if out: out.append((ch, pts[-1][0], pts[-1][1], out[-1][3], out[-1][4]))
    return out, ch


def width_at(g, x, y, ux, uy, level):
    """Contiguous raised run across the line through (x, y), perpendicular to (ux, uy); metres."""
    px, py = -uy, ux; offs = np.arange(-40, 40.01, 0.5); ok = []
    for o in offs:
        s = g.at(g.dsm, x + px * o, y + py * o); d = g.at(g.dtm, x + px * o, y + py * o)
        ok.append(bool(np.isfinite(s) and np.isfinite(d) and abs(s - level) < 1.5 and s - d > 2.0))
    i0 = int(np.argmin(np.abs(offs)))
    if not ok[i0]:  # the centreline sits on a gap: look 1.5 m either side
        for j in range(1, 4):
            if ok[i0 - j]: i0 -= j; break
            if ok[i0 + j]: i0 += j; break
        else: return None
    lo = i0; gap = 0
    while lo > 0 and (ok[lo - 1] or gap < 2):
        gap = 0 if ok[lo - 1] else gap + 1; lo -= 1
    hi = i0; gap = 0
    while hi < len(ok) - 1 and (ok[hi + 1] or gap < 2):
        gap = 0 if ok[hi + 1] else gap + 1; hi += 1
    while not ok[lo]: lo += 1
    while not ok[hi]: hi -= 1
    return (hi - lo) * 0.5 + 0.5


def polygon_stats(g, nodes, part, wid):
    poly = [T.transform(lon, lat) for lat, lon in nodes]
    m = ~geometry_mask([{"type": "Polygon", "coordinates": [poly]}], out_shape=g.dsm.shape, transform=g.a.transform)
    s = g.dsm[m]; s = s[np.isfinite(s)]
    if len(s) < 5: return None
    edge = [e for e in (g.at(g.dtm, x, y) for x, y in poly) if np.isfinite(e)]
    gr = float(np.median(edge)) if edge else float("nan")
    return {"part": part, "osm_way": wid, "area_m2": int(m.sum()), "dsm_median": round(float(np.median(s)), 2), "dsm_p95": round(float(np.percentile(s, 95)), 2),
            "dsm_max": round(float(s.max()), 2), "ground_edge_median": round(gr, 2), "ground_edge_min": round(min(edge), 2) if edge else None,
            "ground_edge_max": round(max(edge), 2) if edge else None, "p95_above_ground": round(float(np.percentile(s, 95)) - gr, 2), "max_above_ground": round(float(s.max()) - gr, 2)}


def line_stats(g, nodes, part, wid, grp, is_deck):
    smp, L = line_samples(nodes, STEP)
    if not smp: return None
    rows = [(ch, x, y, ux, uy, g.at(g.dsm, x, y), g.at(g.dtm, x, y)) for ch, x, y, ux, uy in smp]
    rise = np.array([r[5] - r[6] for r in rows]); on = np.isfinite(rise) & (rise > RISE_MIN)
    e = {"part": part, "osm_way": wid, "group": grp, "plan_length_m": round(L, 1), "samples": len(rows)}
    if not on.any(): return e
    idx = np.where(on)[0]; runs = np.split(idx, np.where(np.diff(idx) > 3)[0] + 1)  # gaps up to 6 m stay in one run
    run = max(runs, key=len); a, b = run[0], run[-1]; sub = [rows[i] for i in run]
    if rows[b][0] - rows[a][0] < 6: return e  # a single raised sample is noise (a car, a rail, a tree)
    e["structure_run"] = {"from_chainage_m": round(rows[a][0], 1), "to_chainage_m": round(rows[b][0], 1), "length_m": round(rows[b][0] - rows[a][0] + STEP, 1),
                          "rise_min": round(float(np.nanmin([r[5] - r[6] for r in sub])), 2), "rise_median": round(float(np.nanmedian([r[5] - r[6] for r in sub])), 2),
                          "rise_max": round(float(np.nanmax([r[5] - r[6] for r in sub])), 2), "dsm_median": round(float(np.nanmedian([r[5] for r in sub])), 2),
                          "dtm_under_min": round(float(np.nanmin([r[6] for r in sub])), 2), "dtm_under_max": round(float(np.nanmax([r[6] for r in sub])), 2)}
    if is_deck:
        mid = sub[len(sub) // 5: len(sub) - len(sub) // 5] or sub; lvl = float(np.nanmedian([r[5] for r in mid]))
        ws = [w for r in mid[::2] for w in [width_at(g, r[1], r[2], r[3], r[4], lvl)] if w is not None]
        if len(ws) >= 3: e["raised_width_m"] = {"median": round(float(np.median(ws)), 1), "p10": round(float(np.percentile(ws, 10)), 1), "p90": round(float(np.percentile(ws, 90)), 1), "n": len(ws)}
    return e


def main():
    res = {}
    for folder in sorted(set(os.path.dirname(f) for f in glob.glob(os.path.join(HERE, "reference", "**", "geometry.json"), recursive=True))):
        name = os.path.relpath(folder, os.path.join(HERE, "reference")).replace("\\", "/")
        if sys.argv[1:] and not any(s in name for s in sys.argv[1:]): continue
        dsm_p, dtm_p = [os.path.join(folder, "elevation", f"{k}-2018-1m.tif") for k in ("dsm", "dtm")]
        if not os.path.exists(dsm_p): continue
        g = Grid(dsm_p, dtm_p); ways = []; collect(json.load(open(os.path.join(folder, "geometry.json"))), ways)
        out = {"lines": [], "polygons": []}; prof = ["part,osm_way,chainage_m,dtm_m,dsm_m,rise_m\n"]
        for grp, d in ways:
            nodes = d["nodes"]; part = d.get("part") or d.get("which", "")[:30]; wid = d.get("osm_way", "")
            if len(nodes) >= 4 and nodes[0] == nodes[-1]:
                p = polygon_stats(g, nodes, part, wid)
                if p: out["polygons"].append(p)
                continue
            e = line_stats(g, nodes, part, wid, grp, grp == "decks" and part.startswith(DECK_PARTS))
            if e: out["lines"].append(e)
            for ch, x, y, _, _ in line_samples(nodes, PSTEP)[0]:
                s, dt = g.at(g.dsm, x, y), g.at(g.dtm, x, y)
                prof.append(f"{part},{wid},{ch:.0f},{dt:.2f},{s:.2f},{s - dt:.2f}\n")
        res[name] = out
        open(os.path.join(folder, "elevation", "profiles.csv"), "w", newline="").write("".join(prof))
        print(name, len(out["lines"]), "lines", len(out["polygons"]), "polygons", flush=True)
    if not sys.argv[1:]:
        json.dump(res, open(os.path.join(HERE, "data", "measurements.json"), "w"), indent=1)
    return res


if __name__ == "__main__":
    main()
