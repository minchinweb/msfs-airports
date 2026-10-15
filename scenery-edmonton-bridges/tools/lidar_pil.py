"""LiDAR clip reader without rasterio/pyproj (Pillow + numpy only), and profiles.csv writer for the sites measure-sites.py has not run on.

The clips in docs/edmonton-bridges/reference/<site>/elevation are EPSG:3979 (NAD83(CSRS) / Canada Atlas Lambert), 1 m, float32.
Run:  python -I scenery-edmonton-bridges/tools/lidar_pil.py <reference folder> [...]   (writes elevation/profiles.csv, same columns
as measure-sites.py: part,osm_way,chainage_m,dtm_m,dsm_m,rise_m; 25 m steps along every mapped line way).
"""
import json, math, sys
from pathlib import Path
import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
A, F = 6378137.0, 1 / 298.257222101
E = math.sqrt(2 * F - F * F)


def lcc(lat, lon, lat1=49.0, lat2=77.0, lat0=49.0, lon0=-95.0):
    """EPSG:3979 forward projection (Lambert conformal conic, 2 standard parallels, GRS80)."""
    def m(p):
        return math.cos(p) / math.sqrt(1 - E * E * math.sin(p) ** 2)

    def t(p):
        return math.tan(math.pi / 4 - p / 2) / ((1 - E * math.sin(p)) / (1 + E * math.sin(p))) ** (E / 2)
    p1, p2, p0, p = map(math.radians, (lat1, lat2, lat0, lat))
    n = (math.log(m(p1)) - math.log(m(p2))) / (math.log(t(p1)) - math.log(t(p2)))
    Fc = m(p1) / (n * t(p1) ** n)
    r0 = A * Fc * t(p0) ** n
    r = A * Fc * t(p) ** n
    th = n * math.radians(lon - lon0)
    return r * math.sin(th), r0 - r * math.cos(th)


class Grid:
    def __init__(self, path):
        im = Image.open(path)
        tag = im.tag_v2
        tp, sc = tag[33922], tag[33550]
        self.x0, self.y0, self.px = tp[3], tp[4], sc[0]
        a = np.array(im, dtype=float)
        a[a < -1000] = np.nan
        self.a = a

    def at(self, lat, lon):
        x, y = lcc(lat, lon)
        c = int((x - self.x0) / self.px)
        r = int((self.y0 - y) / self.px)
        if 0 <= r < self.a.shape[0] and 0 <= c < self.a.shape[1]:
            return float(self.a[r, c])
        return float("nan")


def walk(o, out, grp=""):
    if isinstance(o, dict):
        if "nodes" in o and isinstance(o["nodes"], list):
            out.append((grp, o))
        for k, v in o.items():
            walk(v, out, grp or k)
    elif isinstance(o, list):
        for v in o:
            walk(v, out, grp)


def samples(nodes, step):
    """[(chainage, lat, lon)] every `step` m along a lat/lon polyline."""
    ky = 111320.0
    kx = 111320.0 * math.cos(math.radians(nodes[0][0]))
    pts, cum = [], [0.0]
    for (a, b), (c, d) in zip(nodes[:-1], nodes[1:]):
        cum.append(cum[-1] + math.hypot((d - b) * kx, (c - a) * ky))
    out, s, i = [], 0.0, 0
    while s <= cum[-1] + 1e-6:
        while i < len(nodes) - 2 and s > cum[i + 1]:
            i += 1
        u = (s - cum[i]) / ((cum[i + 1] - cum[i]) or 1)
        out.append((s, nodes[i][0] + (nodes[i + 1][0] - nodes[i][0]) * u, nodes[i][1] + (nodes[i + 1][1] - nodes[i][1]) * u))
        s += step
    return out


def main(folders):
    for f in folders:
        f = Path(f)
        dsm, dtm = Grid(f / "elevation/dsm-2018-1m.tif"), Grid(f / "elevation/dtm-2018-1m.tif")
        ways = []
        walk(json.load(open(f / "geometry.json", encoding="utf-8")), ways)
        rows = ["part,osm_way,chainage_m,dtm_m,dsm_m,rise_m\n"]
        for grp, d in ways:
            nodes = [tuple(p) for p in d["nodes"]]
            if nodes[0] == nodes[-1]:
                continue
            part = d.get("part", "")
            for s, la, lo in samples(nodes, 25.0):
                a, b = dsm.at(la, lo), dtm.at(la, lo)
                rows.append("%s,%s,%.0f,%.2f,%.2f,%.2f\n" % (part, d["osm_way"], s, b, a, a - b))
        (f / "elevation/profiles.csv").write_text("".join(rows), newline="")
        print(f, len(rows) - 1, "rows")


if __name__ == "__main__":
    main(sys.argv[1:])
