"""Sample only this folder's LiDAR clips. Do not write ELEVATION.md."""
import json, os
import numpy as np, rasterio
from pyproj import Transformer

HERE = os.path.dirname(os.path.abspath(__file__))
t = Transformer.from_crs(4326, 3979, always_xy=True)


def densify(nodes, step=3.0):
    pts = [t.transform(lon, lat) for lat, lon in nodes]
    out = []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        n = max(1, int(np.hypot(x1 - x0, y1 - y0) / step))
        out += [(x0 + (x1 - x0) * k / n, y0 + (y1 - y0) * k / n) for k in range(n)]
    return out + [pts[-1]]


g = json.load(open(os.path.join(HERE, "geometry.json"), encoding="utf-8"))
dtm_p = os.path.join(HERE, "elevation", "dtm-2018-1m.tif")
dsm_p = os.path.join(HERE, "elevation", "dsm-2018-1m.tif")
with rasterio.open(dtm_p) as a, rasterio.open(dsm_p) as b:
    dtm = a.read(1, masked=True)
    dsm = b.read(1, masked=True)
    print("dtm nodata frac", float(dtm.mask.mean()) if np.ma.is_masked(dtm) else 0)
    print("dsm nodata frac", float(dsm.mask.mean()) if np.ma.is_masked(dsm) else 0)
    print("dtm min", float(dtm.compressed().min()) if dtm.compressed().size else "empty")
    print("dtm max", float(dtm.compressed().max()) if dtm.compressed().size else "empty")
    cx, cy = t.transform(g["centre"][1], g["centre"][0])
    r, c = a.index(cx, cy)
    print("centre pixel", r, c, "dtm", None if not (0 <= r < dtm.shape[0] and 0 <= c < dtm.shape[1]) else (None if dtm.mask[r, c] else float(dtm[r, c])))
    parts = g["decks"] + g["approaches"]
    for d in parts:
        vals = []
        for x, y in densify(d["nodes"]):
            rr, cc = b.index(x, y)
            if 0 <= rr < dsm.shape[0] and 0 <= cc < dsm.shape[1] and not dsm.mask[rr, cc]:
                vals.append(float(dsm[rr, cc]))
        if len(vals) >= 6:
            p = np.percentile(vals, [10, 50, 90])
            print(f"{d['part']}\t{len(vals)}\t{p[0]:.2f}\t{p[1]:.2f}\t{p[2]:.2f}")
        else:
            print(f"{d['part']}\t{len(vals)}\ttoo few")
