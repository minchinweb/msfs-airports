"""Redraw docs/cyxd/maps/ (airfield and overview maps) from CYXD.xml: runways, taxiways, aprons and every generated building.

Run from the repo root:  python -I airport-cyxd/tools/make_maps.py
Building footprints are the generated exclusion polygons shrunk by the generator's 6 m margin; objects without a polygon are drawn as markers.
"""
import math
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MPoly
from shapely.geometry import LineString, Polygon
from shapely.ops import unary_union

ROOT = Path(__file__).resolve().parents[2]
CYXD = ROOT / "airport-cyxd/PackageSources/Scenery/airport-cyxd/CYXD.xml"
OUT = ROOT / "docs/cyxd/maps"
KX, KY = 66170.0, 111200.0
MARGIN = 6.0
BEGIN, END = "BEGIN historic buildings", "END historic buildings"
RUNWAY_LABELS = {58: ("04", "22"), 138: ("12", "30"), 180: ("16", "34")}


def short(title):
    """Key text: drop OSM way ids and 'traced from ...' tails, then close any open bracket."""
    t = re.sub(r"(,|;| \()\s*(OSM|traced|replaces|c\.19|RCAF).*", "", title)
    t = re.sub(r"\s*\(?(Street View 2009|infield).*", "", t)
    if t.count("(") > t.count(")"):
        t += ")"
    return t


def classify(title, shape):
    low = title.lower()
    if "aerodrome beacon" in low:
        return "beacon"
    if "wind tee" in low:
        return "tee"
    if "ndb" in low:
        return "ndb"
    if "transmitter" in low:
        return "tx"
    return "bldg" if shape else "obj"


def main():
    text = CYXD.read_text(encoding="utf-8")
    root = ET.fromstring(text)
    ap = root.find("Airport")
    lat0, lon0 = float(ap.get("lat")), float(ap.get("lon"))

    def xy(lat, lon):
        return ((float(lon) - lon0) * KX, (float(lat) - lat0) * KY)

    def poly_xy(el):
        return [xy(v.get("lat"), v.get("lon")) for v in el.findall("Vertex")]

    runways = []
    for r in ap.findall("Runway"):
        cx, cy = xy(r.get("lat"), r.get("lon"))
        h = math.radians(float(r.get("heading")))
        half_l, half_w = float(r.get("length")) / 2, float(r.get("width")) / 2
        f, rt = (math.sin(h), math.cos(h)), (math.cos(h), -math.sin(h))
        pts = [(cx + a * rt[0] + b * f[0], cy + a * rt[1] + b * f[1]) for a, b in ((-half_w, -half_l), (half_w, -half_l), (half_w, half_l), (-half_w, half_l))]
        lab = RUNWAY_LABELS[round(float(r.get("heading")))]
        runways.append((pts, (cx - half_l * f[0] * 1.07, cy - half_l * f[1] * 1.07, lab[0]), (cx + half_l * f[0] * 1.07, cy + half_l * f[1] * 1.07, lab[1])))
    pts = {p.get("index"): xy(p.get("lat"), p.get("lon")) for p in ap.findall("TaxiwayPoint")}
    shapes = []
    for t in ap.findall("TaxiwayPath"):
        if t.get("type") not in ("TAXI", "PATH") or t.get("start") not in pts or t.get("end") not in pts:
            continue
        a, b = pts[t.get("start")], pts[t.get("end")]
        if a != b:
            shapes.append(LineString([a, b]).buffer(float(t.get("width")) / 2, cap_style=2))
    taxi = unary_union(shapes) if shapes else None
    aprons = [poly_xy(a) for a in ap.iter("Apron")]

    block = text[text.index(BEGIN):text.index(END)]
    foot = {}
    for pl in root.iter("Polygon"):
        d = pl.get("displayName", "")
        if d.startswith("No generated buildings: "):
            foot[d[len("No generated buildings: "):]] = poly_xy(pl)
    keep = []
    pat = r'<!-- (.*?) -->\s*<SceneryObject lat="([^"]+)" lon="([^"]+)"[^>]*heading="([^"]+)"'
    for m in re.finditer(pat, block, re.S):
        title = re.sub(r"\s+", " ", m.group(1))
        if title.startswith(("XD:", "control tower:", "old terminal")):
            continue
        lat, lon = float(m.group(2)), float(m.group(3))
        pg = foot.get(title.replace('"', "'")[:60])
        shape = None
        if pg and len(pg) >= 3 and "transmitter" not in title.lower():
            p = Polygon(pg)
            q = p.buffer(-MARGIN, join_style=2)
            shape = list((q if not q.is_empty else p).exterior.coords)[:-1]
        keep.append((title, lat, lon, xy(lat, lon), shape, classify(title, shape)))
    wind = None
    for so in root.iter("SceneryObject"):
        if so.find("Windsock") is not None:
            wind = xy(so.get("lat"), so.get("lon"))

    def inside(c, xlim, ylim):
        return xlim[0] < c[0] < xlim[1] and ylim[0] < c[1] < ylim[1]

    def draw(ax, xlim, ylim, numbered):
        for pts_, a, b in runways:
            ax.add_patch(MPoly(pts_, closed=True, fc="#999", ec="#444", lw=0.8, zorder=2))
            for x, y, lab in (a, b):
                if inside((x, y), xlim, ylim):
                    ax.text(x, y, lab, fontsize=9, fontweight="bold", ha="center", va="center", color="#333", zorder=6)
        if taxi is not None:
            for g in (taxi.geoms if hasattr(taxi, "geoms") else [taxi]):
                ax.add_patch(MPoly(list(g.exterior.coords), closed=True, fc="#e8e8e8", ec="#1f77b4", lw=1.0, zorder=1))
                for i in g.interiors:
                    ax.add_patch(MPoly(list(i.coords), closed=True, fc="white", ec="#1f77b4", lw=1.0, zorder=1))
        for a in aprons:
            ax.add_patch(MPoly(a, closed=True, fc="#d6d6c4", ec="#6b6b44", lw=0.9, ls="--", zorder=1))
        for n, (title, lat, lon, c, shape, kind) in enumerate(keep, 1):
            if kind == "bldg":
                ax.add_patch(MPoly(shape, closed=True, fc="#3a74b8", ec="#1f4e8c", lw=0.9, alpha=0.85, zorder=4))
            else:
                mk = {"tee": ("^", 9, "#2ca02c"), "beacon": ("*", 14, "#f2b705"), "ndb": ("o", 9, "#b79be0"), "tx": ("s", 11, "#c0504d"), "obj": ("D", 4, "#3a74b8")}[kind]
                ax.plot(*c, marker=mk[0], ms=mk[1], color=mk[2], mec="k", zorder=5)
            if numbered and kind != "obj" and inside(c, xlim, ylim):
                ax.annotate(str(n), c, fontsize=6.5, color="white" if kind == "bldg" else "k", fontweight="bold", ha="center", va="center", zorder=7)
        if wind and inside(wind, xlim, ylim):
            ax.plot(*wind, marker="v", ms=8, color="#ff7f0e", mec="k", zorder=5)
            ax.annotate("windsock (existing)", wind, xytext=(6, -3), textcoords="offset points", fontsize=7, color="#b35a00")
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_aspect("equal")
        ax.grid(alpha=0.25)

    OUT.mkdir(parents=True, exist_ok=True)
    fig = plt.figure(figsize=(17.5, 12.5))
    ax = fig.add_axes([0.075, 0.07, 0.52, 0.86])
    draw(ax, (-1250, 1000), (-1250, 1400), True)
    ax.set_title("CYXD buildings and objects - airfield (north up)")
    ax.set_xlabel("east of CYXD ref (m)")
    ax.set_ylabel("north (m)")
    half = (len(keep) + 1) // 2
    step = 0.89 / (half + 0.2)
    for col in range(2):
        x0 = 0.615 + col * 0.195
        if col == 0:
            fig.text(x0, 0.95, "Key (numbers on map)", fontsize=11, fontweight="bold")
        for j, n in enumerate(range(col * half, min(len(keep), (col + 1) * half))):
            title, lat, lon = keep[n][:3]
            y = 0.915 - j * step
            fig.text(x0, y, "%2d  %s" % (n + 1, short(title) if len(short(title)) <= 50 else short(title)[:48] + "..."), fontsize=7.2)
            fig.text(x0 + 0.012, y - step * 0.42, "%.5f, %.5f" % (lat, lon), fontsize=5.5, color="#555")
    fig.savefig(OUT / "cyxd-buildings-airfield.png", dpi=100)
    plt.close(fig)

    allx = [k[3][0] for k in keep]
    ally = [k[3][1] for k in keep]
    fig, ax = plt.subplots(figsize=(10, 11.8))
    draw(ax, (min(allx) - 800, max(allx) + 1300), (min(ally) - 1200, max(ally) + 1200), False)
    for title, lat, lon, c, shape, kind in keep:
        if kind in ("tx", "ndb"):
            label = title.split(" station")[0] + " (site)" if kind == "ndb" else title.split(" (")[0]
            ax.annotate(label, c, xytext=(8, 5), textcoords="offset points", fontsize=8, fontweight="bold", color="#5a2a82" if kind == "ndb" else "#8c2a2a")
    ax.set_title("CYXD overview: NDBs XD / ZXD, transmitter site (north up)")
    ax.set_xlabel("east of CYXD ref (m)")
    ax.set_ylabel("north (m)")
    fig.tight_layout()
    fig.savefig(OUT / "cyxd-buildings-overview.png", dpi=100)
    plt.close(fig)
    print(len(keep), "objects drawn")


if __name__ == "__main__":
    main()
