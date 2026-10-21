"""K209 Valley Line at-grade track, Muttart (P152) to Strathearn (P153): two tracks, about 1.6 km, on ballast with catenary poles.
The 2019 aerial and the sim ground pre-date this stretch of the line, so the track is modelled here.  Geometry: the two OSM
railway=light_rail surface ways of docs/edmonton-bridges/lrt-tracks.json from the SW end of the Muttart platforms to the Strathearn
stop (reference/P152-muttart/elevation/track-to-strathearn.json, densified to 10 m and sampled on the 2018 LiDAR bare earth).  Height:
rail top follows the ground (moving average over 7 samples = 60 m), the same section as P152 (ballast top 0.3 below the rail top,
concrete tie slab, rails 1.44 m apart).  Strathearn platforms are not built.  Catenary poles every 40 m outside each track, contact
wire 5.6 m above the rail.  The trees are excluded along the footprint by the generator's exclusion polygon.  Datum (y = 0) = 620.0 m.
"""
import json
from bridgelib import *

CODE, TITLE = "K209", "Valley Line track Muttart - Strathearn"
RIVER = 620.0          # datum (not a river here)
SRC = ROOT / "docs/edmonton-bridges/reference/P152-muttart/elevation/track-to-strathearn.json"


def _smooth(v, k=3):
    return [sum(v[max(0, i - k):i + k + 1]) / len(v[max(0, i - k):i + k + 1]) for i in range(len(v))]


def build():
    d = json.loads(SRC.read_text(encoding="utf-8"))
    allp = [p for t in d["tracks"] for p in t]
    lat0 = sum(p[0] for p in allp) / len(allp)
    lon0 = sum(p[1] for p in allp) / len(allp)
    fr = Frame(lat0, lon0)
    m = BMesh()
    ax0 = None
    for t in d["tracks"]:
        pts = [(p[0], p[1]) for p in t]
        g = [p[2] if p[2] is not None else t[0][2] for p in t]
        ax = fr.axis(pts)
        ax0 = ax0 or ax
        gs = _smooth([v - RIVER for v in g])
        # axis stations are the polyline vertices (10 m apart), so profile() over the cumulative lengths gives y at every vertex
        y = profile(list(zip(ax.cum, gs)))
        L = ax.L
        ribbon(m, ax, 0.0, L, -2.2, 2.2, lambda s: y(s) - 1.6, lambda s: y(s) - 0.3, CONCD, sw_top=BALLAST)
        ribbon(m, ax, 0.0, L, -0.9, 0.9, lambda s: y(s) - 0.3, lambda s: y(s) - 0.18, CONCD)
        for r in (-0.72, 0.72):
            ribbon(m, ax, 0.0, L, r - 0.04, r + 0.04, lambda s: y(s) - 0.18, lambda s: y(s) - 0.02, RAILSTEEL)
        poles = [4 + i * 40.0 for i in range(int(L // 40) + 1)]
        for s in poles:
            sg = 1 if int(s // 40) % 2 == 0 else -1
            beam(m, ax.p3(s, sg * 3.2, y(s) - 0.3), ax.p3(s, sg * 3.2, y(s) + 7.0), 0.3, 0.3, GREY)
            beam(m, ax.p3(s, sg * 3.2, y(s) + 6.6), ax.p3(s, 0.0, y(s) + 6.6), 0.15, 0.15, GREY)
        for a, b in zip(poles[:-1], poles[1:]):
            beam(m, ax.p3(a, 0.0, y(a) + 5.6), ax.p3(b, 0.0, y(b) + 5.6), 0.05, 0.05, LAMP)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_k209_valley_line_track", m)], frame=fr, axis=ax0)
