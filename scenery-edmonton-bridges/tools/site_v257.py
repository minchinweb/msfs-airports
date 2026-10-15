"""V257 Edmonton Riverboat (the Edmonton Queen), docked at Rafter's Landing, bow pointing west (18 Jun 2018 photo note).
NOTES.md: steel paddlewheeler, 51.8 m x 12.0 m (Transport Canada), enclosed lower deck and open upper deck, white house, blue hull,
red stripe along the deck line, blue canopy, two red stern wheels (16 ft).  Freeboard, deck heights and canopy height are not published
(assumed).  Placed along the longest axis of OSM way 1373511013 on the 2018 river surface (613.66 m).
"""
import math
from bridgelib import *

CODE, TITLE = "V257", "Edmonton Riverboat"
RIVER = 613.66
F = "V257-river-queen"
L, B = 51.8, 12.0


def build():
    fr0 = Frame(53.5396, -113.4819)
    pts = [fr0.en(*p) for p in find_way(F, 1373511013)]
    cx, cy, d, lo, hi = pca_axis(pts, toward=(-1.0, 0.0))     # bow points west
    mid = (lo + hi) / 2
    lat0, lon0 = fr0.ll(cx + d[0] * mid, cy + d[1] * mid)
    fr = Frame(lat0, lon0)
    # stern at s = 0, bow at s = L, centred on the origin
    ax = Axis([(-d[0] * L / 2, -d[1] * L / 2), (d[0] * L / 2, d[1] * L / 2)])
    m = BMesh()
    hull = [ax.en(0, -B / 2), ax.en(0, B / 2), ax.en(L - 8, B / 2), ax.en(L, 2.5), ax.en(L, -2.5), ax.en(L - 8, -B / 2)]
    prism(m, hull, -1.8, 1.2, BLUE)
    prism(m, scale_poly(hull, 1.012), 0.9, 1.3, RED)                         # red stripe on the deck line
    house = [ax.en(4, -5.3), ax.en(4, 5.3), ax.en(L - 10, 5.3), ax.en(L - 6, 3.0), ax.en(L - 6, -3.0), ax.en(L - 10, -5.3)]
    prism(m, house, 1.3, 4.3, WHITE)
    for sg in (-1, 1):                                                       # window band along the lower deck
        ribbon(m, ax, 6, L - 11, sg * 5.32 - 0.02, sg * 5.32 + 0.02, 2.2, 3.5, DARK)
    prism(m, [ax.en(3.5, -5.6), ax.en(3.5, 5.6), ax.en(L - 10, 5.6), ax.en(L - 5, 3.0), ax.en(L - 5, -3.0), ax.en(L - 10, -5.6)], 4.3, 4.65, WHITE)
    for s in [5 + i * 6.2 for i in range(int((L - 17) // 6.2) + 1)]:         # canopy posts and blue canopy
        for sg in (-1, 1):
            beam(m, ax.p3(s, sg * 5.3, 4.65), ax.p3(s, sg * 5.3, 7.6), 0.14, 0.14, WHITE)
    prism(m, [ax.en(4.5, -5.9), ax.en(4.5, 5.9), ax.en(L - 12, 5.9), ax.en(L - 12, -5.9)], 7.6, 7.95, BLUE)
    prism(m, [ax.en(L - 24, -3.4), ax.en(L - 24, 3.4), ax.en(L - 15, 3.4), ax.en(L - 15, -3.4)], 4.65, 7.2, WHITE)  # wheelhouse
    prism(m, [ax.en(L - 24.6, -3.8), ax.en(L - 24.6, 3.8), ax.en(L - 14.4, 3.8), ax.en(L - 14.4, -3.8)], 7.2, 7.5, BLUE)
    for sg in (-1, 1):                                                       # two red stern wheels
        wheel(m, ax, -0.3, 1.6, 2.4, sg * 3.1 - 0.7, sg * 3.1 + 0.7, RED)
    for sg in (-2.5, 2.5):                                                   # flag poles
        beam(m, ax.p3(L - 20, sg, 7.95), ax.p3(L - 20, sg, 11.5), 0.1, 0.1, LAMP)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_v257_riverboat", m)], frame=fr, axis=ax)
