"""Plot CYXD layout / taxi network: this project vs roscohead's alternate."""
import math, os
import xml.etree.ElementTree as ET
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MPoly

HERE = os.path.dirname(os.path.abspath(__file__))
MINE = os.path.join(HERE, "..", "..", "..", "airport-cyxd", "PackageSources", "Scenery", "airport-cyxd", "CYXD.xml")
HIS = os.path.join(HERE, "..", "alt-roscohead", "roscohead-cyxd.xml")
HISCVX = os.path.join(HERE, "..", "alt-roscohead", "roscohead-cyxd.cvx.xml")
LAT0, LON0 = 53.5725, -113.5210
KX = 111195 * math.cos(math.radians(LAT0)); KY = 111195


def xy(lat, lon):
    return ((float(lon) - LON0) * KX, (float(lat) - LAT0) * KY)


def load(path):
    root = ET.parse(path).getroot()
    d = dict(runways=[], aprons=[], points={}, parking={}, paths=[], polys=[], objs=[], ils=None)
    for r in root.iter("Runway"):
        d["runways"].append(r)
    for a in root.iter("Apron"):
        d["aprons"].append([xy(v.get("lat"), v.get("lon")) for v in a.findall("Vertex")])
    for p in root.iter("TaxiwayPoint"):
        d["points"][int(p.get("index"))] = (xy(p.get("lat"), p.get("lon")), p.get("type"))
    for p in root.iter("TaxiwayParking"):
        d["parking"][int(p.get("index"))] = (xy(p.get("lat"), p.get("lon")), p.get("type"), p.get("number"), float(p.get("radius", "10").rstrip("M")))
    for p in root.iter("TaxiwayPath"):
        d["paths"].append((p.get("type"), int(p.get("start")), int(p.get("end"))))
    for p in root.iter("Polygon"):
        pts = [xy(v.get("lat"), v.get("lon")) for v in p.findall("Vertex")]
        if len(pts) > 2:
            d["polys"].append(pts)
    for o in root.iter("SceneryObject"):
        if o.get("lat"):
            d["objs"].append(xy(o.get("lat"), o.get("lon")))
    return d


def cvx(path):
    out = []
    for s in ET.parse(path).getroot().iter("Shape"):
        pts = [xy(p.get("Latitude"), p.get("Longitude")) for p in s.iter("Point")]
        if len(pts) > 2:
            out.append(pts)
    return out


def rwy_poly(r):
    cx, cy = xy(r.get("lat"), r.get("lon"))
    h = math.radians(float(r.get("heading")))
    L = float(r.get("length").rstrip("MF")) * (0.3048 if r.get("length").endswith("F") else 1)
    W = float(r.get("width").rstrip("MF")) * (0.3048 if r.get("width").endswith("F") else 1)
    ux, uy = math.sin(h), math.cos(h); px, py = uy, -ux
    return [(cx + sx * ux * L / 2 + sy * px * W / 2, cy + sx * uy * L / 2 + sy * py * W / 2)
            for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]


def draw_layout(ax, d, extra, title):
    for a in d["aprons"]:
        ax.add_patch(MPoly(a, fc="#c8c8c8", ec="#888", lw=.6))
    for p in extra:
        ax.add_patch(MPoly(p, fc="#f4a6a6", ec="#c33", lw=.6, alpha=.45))
    for r in d["runways"]:
        ax.add_patch(MPoly(rwy_poly(r), fc="#333", ec="k"))
        cx, cy = xy(r.get("lat"), r.get("lon"))
        ax.text(cx, cy, r.get("number") + "/" + r.get("number") if False else r.get("number"), color="w", fontsize=7, ha="center")
    if d["objs"]:
        ax.scatter(*zip(*d["objs"]), s=6, c="#26a", zorder=5)
    ax.set_title(title); ax.set_aspect("equal"); ax.grid(alpha=.3)


def draw_taxi(ax, d, title, color, alpha=1.0, label=None):
    pts, pk = d["points"], d["parking"]
    for t, s, e in d["paths"]:
        a = pts.get(s, pk.get(s)); b = pk.get(e) if t == "PARKING" and e in pk else pts.get(e, pk.get(e))
        if not a or not b:
            continue
        ax.plot([a[0][0], b[0][0]], [a[0][1], b[0][1]], c=color, lw=1.0 if t != "PARKING" else .6, alpha=alpha)
    if pk:
        ax.scatter(*zip(*[v[0] for v in pk.values()]), s=22, c=color, marker="s", alpha=alpha, zorder=4, label=label)
        for v in pk.values():
            ax.text(v[0][0] + 6, v[0][1] + 6, str(v[2]), fontsize=5, color=color)
    ax.set_title(title); ax.set_aspect("equal"); ax.grid(alpha=.3)


mine, his = load(MINE), load(HIS)
hisx = cvx(HISCVX)
S = f"mine: {len(mine['runways'])} rwy, {len(mine['aprons'])} aprons, {len(mine['paths'])} paths, {len(mine['parking'])} parking"
T = f"roscohead: {len(his['runways'])} rwy, {len(his['aprons'])} aprons, {len(his['paths'])} paths, {len(his['parking'])} parking"

fig, axs = plt.subplots(1, 3, figsize=(24, 9))
draw_layout(axs[0], mine, mine["polys"], "Mine (red = exclusion/grass polygons, blue = objects)\n" + S)
draw_layout(axs[1], his, hisx, "roscohead (red = .cvx exclusion/flatten/water)\n" + T)
draw_layout(axs[2], mine, [], "Overlay: mine (solid) vs roscohead (outline)")
for a in his["aprons"]:
    axs[2].add_patch(MPoly(a, fc="none", ec="#d60", lw=1))
for r in his["runways"]:
    axs[2].add_patch(MPoly(rwy_poly(r), fc="none", ec="#d60", lw=1.5))
for ax in axs:
    ax.set_xlim(-1500, 1500); ax.set_ylim(-1500, 1500)
fig.tight_layout(); fig.savefig(os.path.join(HERE, "layout-compare.png"), dpi=80)

fig, axs = plt.subplots(1, 3, figsize=(24, 9))
draw_taxi(axs[0], mine, "Mine: taxi paths + parking\n" + S, "#06c")
draw_taxi(axs[1], his, "roscohead: taxi paths + parking\n" + T, "#d60")
draw_taxi(axs[2], mine, "Overlay (blue = mine, orange = roscohead)", "#06c", .8)
draw_taxi(axs[2], his, "Overlay (blue = mine, orange = roscohead)", "#d60", .8)
for ax in axs:
    ax.set_xlim(-1500, 1500); ax.set_ylim(-1500, 1500)
fig.tight_layout(); fig.savefig(os.path.join(HERE, "taxi-parking-compare.png"), dpi=80)
print(S); print(T)
