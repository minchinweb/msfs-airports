"""Plot CYXD runways with displaced thresholds: committed (HEAD) vs working copy."""
import math, os, subprocess
import xml.etree.ElementTree as ET
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

HERE = os.path.dirname(os.path.abspath(__file__))
REL = "airport-cyxd/PackageSources/Scenery/airport-cyxd/CYXD.xml"
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LAT0, LON0 = 53.5725, -113.5210
KX = 111195 * math.cos(math.radians(LAT0)); KY = 111195

def xy(lat, lon):
    return ((float(lon) - LON0) * KX, (float(lat) - LAT0) * KY)

def runways(root):
    out = []
    for r in root.iter("Runway"):
        cx, cy = xy(r.get("lat"), r.get("lon"))
        h = math.radians(float(r.get("heading")))
        L = float(r.get("length")); W = float(r.get("width"))
        off = {o.get("end"): float(o.get("length")) for o in r.findall("OffsetThreshold")}
        out.append(dict(num=r.get("number"), c=(cx, cy), u=(math.sin(h), math.cos(h)), L=L, W=W,
                        p=off.get("PRIMARY", 0), s=off.get("SECONDARY", 0)))
    return out

def pt(r, along, across=0):
    ux, uy = r["u"]
    return (r["c"][0] + ux * along - uy * across, r["c"][1] + uy * along + ux * across)

def draw(ax, rws, title):
    for r in rws:
        h = r["L"] / 2; w = r["W"] / 2
        ax.add_patch(Polygon([pt(r, -h, -w), pt(r, h, -w), pt(r, h, w), pt(r, -h, w)], fc="#bbbbbb", ec="k", lw=.8))
        for a0, a1, col in ((-h, -h + r["p"], "#e8a33d"), (h - r["s"], h, "#e8a33d")):
            if a1 - a0 > 0.5:
                ax.add_patch(Polygon([pt(r, a0, -w), pt(r, a1, -w), pt(r, a1, w), pt(r, a0, w)], fc=col, ec="none", hatch="//"))
        n = int(r["num"]); rec = (n + 18 - 1) % 36 + 1
        for sgn, label, d in ((-1, f"{n:02d}", r["p"]), (1, f"{rec:02d}", r["s"])):
            x, y = pt(r, sgn * (h + 60), 0)
            ax.text(x, y, label, ha="center", va="center", fontsize=11, weight="bold")
            if d > 0.5:
                x, y = pt(r, sgn * (h - d), 0)
                tx, ty = pt(r, sgn * (h - d), sgn * -(w + 100))
                ax.text(tx, ty, f"{d:.0f} m\n({d/0.3048:.0f} ft)", ha="center", va="center", fontsize=8, color="#a05a00")
                a = pt(r, sgn * (h - d), -w - 6); b = pt(r, sgn * (h - d), w + 6)
                ax.plot([a[0], b[0]], [a[1], b[1]], color="r", lw=1.5)
    ax.set_aspect("equal"); ax.set_title(title, fontsize=11); ax.grid(alpha=.25)
    ax.set_xlabel("east (m)"); ax.set_ylabel("north (m)")

before = ET.fromstring(subprocess.check_output(["git", "-C", ROOT, "show", "HEAD:" + REL]))
after = ET.parse(os.path.join(ROOT, REL)).getroot()
fig, axs = plt.subplots(1, 2, figsize=(16, 8.5), sharex=True, sharey=True)
draw(axs[0], runways(before), "Before (committed): 04/22 has no displaced thresholds")
draw(axs[1], runways(after), "After: 04 = 194 m (637 ft), 22 = 40 m (132 ft)")
axs[0].set_xlim(-1100, 1100); axs[0].set_ylim(-1000, 1000)
fig.suptitle("CYXD displaced thresholds (orange hatch; red line = landing threshold); source: 1978 On Track sketch", fontsize=12)
fig.tight_layout()
out = os.path.join(HERE, "threshold-compare.png")
fig.savefig(out, dpi=110); print(out)
