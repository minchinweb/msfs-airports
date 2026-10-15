"""R15 Dawson Bridge (1912): five riveted through-truss spans, 236.5 m, four concrete river piers.

NOTES.md: spans west -> east 43.3, 43.3, 43.3 (camelback), 76.2 (Pennsylvania, 14 panels), 30.5 (Pratt); piers read from the 2019
aerial at 44.5, 87.9, 131.1 and 207.0 m on way 22916476 (abutments near 1.0 and 237.6); clear roadway 8.1 m; sidewalks 2.65 m on
brackets outside the trusses; steel-blue paint.  Truss depth, pier height and plan are assumptions.  Deck top 17.9 m above the
2018 river (DSM 631.01 - 612.83 = 18.18 including traffic).
"""
import math
from bridgelib import *

CODE, TITLE = "R15", "Dawson Bridge"
RIVER = 612.83
F = "R15-dawson"
DECK = 17.9
YB = 16.6            # bottom chord centre
TT = 4.6             # truss lines


def build():
    fr0 = Frame(53.549, -113.467)
    ax0 = fr0.axis(find_way(F, 22916476))
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(mid[0], mid[1])
    fr = Frame(lat0, lon0)
    ax = fr.axis(find_way(F, 22916476))
    L = ax.L
    m = BMesh()
    ST, WB = DAWSONBLUE, DAWSONBLUE
    sup = [1.0, 44.5, 87.9, 131.1, 207.0, 237.6]
    def camel(f):
        hmax, hend = 8.4, 5.4
        return hend + (hmax - hend) * min(1.0, f / 0.25, (1 - f) / 0.25)
    def penn(f):
        return 6.2 + (12.4 - 6.2) * (1 - (2 * f - 1) ** 2)
    pratt = lambda f: 6.4
    specs = [(camel, 8, "pratt", False), (camel, 8, "pratt", False), (camel, 8, "pratt", False), (penn, 14, "pratt", True), (pratt, 6, "pratt", False)]
    for (hf, n, kind, sub), a, b in zip(specs, sup[:-1], sup[1:]):
        through_truss_span(m, ax, a, b, TT, YB, n, hf, kind=kind, sub=sub, sw=ST, sw_web=WB, chord=(0.8, 0.9), web=(0.4, 0.5))
    # deck: asphalt between the trusses, yellow centre line, brackets and timber-plank sidewalks outside, lattice railing
    ribbon(m, ax, 0.0, L, -TT, TT, DECK - 0.9, DECK, ASPHALT, step=30.0, sw_side=DARK, sw_bot=DARK)
    ribbon(m, ax, 0.0, L, -0.08, 0.08, DECK, DECK + 0.02, YELLOW, step=30.0)
    for sg in (-1, 1):
        ribbon(m, ax, 0.0, L, sg * (TT + 0.5), sg * (TT + 3.15), DECK - 0.7, DECK - 0.4, TIMBER, step=30.0)
        railing(m, ax, 0.0, L, sg * (TT + 3.15), DECK - 0.4, h=1.3, post_step=2.5, sw_post=ST, rails=3, step=30.0)
        ribbon(m, ax, 0.0, L, sg * (TT - 0.3) - 0.2, sg * (TT - 0.3) + 0.2, DECK, DECK + 0.6, CONCD, step=30.0)
    for s in sup[1:-1]:
        pass
    # brackets under the sidewalks at every floor beam
    for s in [1.0 + i * 5.4 for i in range(int(L // 5.4))]:
        for sg in (-1, 1):
            beam(m, ax.p3(s, sg * TT, YB - 0.4), ax.p3(s, sg * (TT + 3.2), DECK - 0.7), 0.3, 0.5, ST)
    # piers: solid tapered concrete shafts, nose on both ends
    for s in sup[1:-1]:
        top = YB - 0.7
        base = -6.0
        frustum(m, nose_plan(ax, s, 0.0, 3.0, 6.0, 2.6), nose_plan(ax, s, 0.0, 2.1, 5.2, 2.0), base, top - 1.0, PIERBEIGE)
        prism(m, nose_plan(ax, s, 0.0, 2.4, 5.8, 0.0, (False, False)), top - 1.0, top, CONC)
    # abutments
    for s, sg in ((sup[0], -1), (sup[-1], 1)):
        ribbon(m, ax, s - 2.0 if sg < 0 else s - 1.0, s + 1.0 if sg < 0 else s + 2.0, -8.0, 8.0, -3.0, YB - 0.7, CONC)
    # lamps on the approach
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_r15_dawson", m)], frame=fr, axis=ax)
