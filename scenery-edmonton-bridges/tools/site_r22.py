"""R22 Clover Bar Railway Bridge (Grand Trunk Pacific, 1907-08, CN Wainwright Subdivision): single track, about 504 m.

Axis: OSM way 23426591 reversed so it runs NW -> SE (s = 0 at the NW end); the outline is way 654886208 (7.1 to 7.9 m wide).
Sourced: length (abutments at 5 and 510 m, LiDAR ground crossing, = 504 m published), rail top 651.4 m (2018 LiDAR, 41.5 m above
the 610.00 m datum; published 42 m), steel deck trusses on tan concrete river piers with cutwaters, steel trestle towers and plate
girders on the approaches, single track (gauge 1435), 95 ft = 29 m piers on the slopes (Edmonton Bulletin 1906).
Read from the 2019 aerial (3.3 px/m): river piers at 141, 210, 279 and 354 m, trestle bents at 23.5, 55, 86, 401, 433 and 465 m.
Assumed: truss depth 14.5 m (2011 photograph proportion against the 4.7 m locomotive), panel counts, plane spacing, bent shape,
pier taper, plate-girder depths, walkway.  Colour: black steel, tan piers.
"""
import math
from bridgelib import *
from t2lib import *

CODE, TITLE = "R22", "Clover Bar Railway Bridge"
DATUM = 610.00
F, WAY, OUTLINE = "R22-clover-bar-railway", 23426591, 654886208
RAIL_TOP = 651.40 - DATUM
DECK = RAIL_TOP - 0.40                      # stringer top / tie bottom
TRUSS_YB = DECK - 14.5                      # bottom chord centre
SUP = [5.0, 23.5, 55.0, 86.0, 141.0, 210.0, 279.0, 354.0, 401.0, 433.0, 465.0, 510.0]
# span kinds between SUP[i] and SUP[i+1]: ("g", depth) plate girder, ("t", panels) truss
KINDS = [("g", 3.0), ("g", 3.2), ("g", 3.4), ("t", 6), ("t", 8), ("t", 8), ("t", 8), ("g", 3.8), ("g", 3.4), ("g", 3.4), ("g", 3.6)]
RIVER_PIERS = [141.0, 210.0, 279.0, 354.0]
TOWERS = [23.5, 55.0, 86.0, 401.0, 433.0, 465.0]
TT = 2.3                                    # truss plane offset


def tower(m, ax, s, y_top, y_base):
    h = y_top - y_base
    n = max(2, int(round(h / 7.5)))
    hs, ht_top, ht_base = 1.6, 2.2, 2.2 + min(1.6, h * 0.05)
    lev = [y_base + h * i / n for i in range(n + 1)]
    wt = lambda y: ht_base + (ht_top - ht_base) * (y - y_base) / (h or 1)
    for sa in (-hs, hs):
        for sg in (-1, 1):
            beam(m, ax.p3(s + sa, sg * ht_base, y_base), ax.p3(s + sa, sg * ht_top, y_top), 0.6, 0.6, BLACKST)
    for i, y in enumerate(lev):
        for sa in (-hs, hs):
            beam(m, ax.p3(s + sa, -wt(y), y), ax.p3(s + sa, wt(y), y), 0.3, 0.3, BLACKST)
        for sg in (-1, 1):
            beam(m, ax.p3(s - hs, sg * wt(y), y), ax.p3(s + hs, sg * wt(y), y), 0.3, 0.3, BLACKST)
        if i < n:
            y1 = lev[i + 1]
            for sa in (-hs, hs):    # X across the track
                beam(m, ax.p3(s + sa, -wt(y), y), ax.p3(s + sa, wt(y1), y1), 0.25, 0.25, BLACKST)
                beam(m, ax.p3(s + sa, wt(y), y), ax.p3(s + sa, -wt(y1), y1), 0.25, 0.25, BLACKST)
            for sg in (-1, 1):      # X along the track
                beam(m, ax.p3(s - hs, sg * wt(y), y), ax.p3(s + hs, sg * wt(y1), y1), 0.25, 0.25, BLACKST)
                beam(m, ax.p3(s + hs, sg * wt(y), y), ax.p3(s - hs, sg * wt(y1), y1), 0.25, 0.25, BLACKST)
    # cap and footing
    beam(m, ax.p3(s, -ht_top - 0.3, y_top + 0.15), ax.p3(s, ht_top + 0.3, y_top + 0.15), 0.5, 0.9, BLACKST)
    prism(m, nose_plan(ax, s, 0.0, 2.6, ht_base + 1.2, 0.0, (False, False)), y_base - 1.5, y_base + 0.4, CONCD)


def plate_girder(m, ax, s0, s1, depth):
    for t in (-1.25, 1.25):
        ribbon(m, ax, s0, s1, t - 0.1, t + 0.1, DECK - depth, DECK - 0.5, BLACKST, step=10.0)
        ribbon(m, ax, s0, s1, t - 0.5, t + 0.5, DECK - 0.5, DECK - 0.3, BLACKST, step=10.0)
        ribbon(m, ax, s0, s1, t - 0.5, t + 0.5, DECK - depth - 0.15, DECK - depth, BLACKST, step=10.0)
    k = max(1, int(round((s1 - s0) / 6.0)))
    for i in range(k + 1):
        s = s0 + (s1 - s0) * i / k
        beam(m, ax.p3(s, -1.25, DECK - depth * 0.5), ax.p3(s, 1.25, DECK - depth * 0.5), depth * 0.5, 0.12, BLACKST)


def track(m, ax, s0, s1):
    ribbon(m, ax, s0, s1, -1.4, 1.4, DECK - 0.5, DECK + 0.2, TIMBER, step=20.0)        # ties on the stringers
    for t in (-0.7175, 0.7175):
        ribbon(m, ax, s0, s1, t - 0.08, t + 0.08, DECK + 0.2, RAIL_TOP, RAILSTEEL, step=20.0)
    for sg in (-1, 1):                                                                  # walkway and handrail
        ribbon(m, ax, s0, s1, min(sg * 1.4, sg * 3.2), max(sg * 1.4, sg * 3.2), DECK - 0.3, DECK, TIMBER, step=20.0)
        railing(m, ax, s0, s1, sg * 3.2, DECK, h=1.1, post_step=3.0, sw_post=BLACKST, rails=2, step=20.0, post_w=0.1)


def river_pier(m, ax, s, y_base):
    top = TRUSS_YB - 0.5
    bot = nose_plan(ax, s, 0.0, 2.3, 4.6, 2.2)
    tp = nose_plan(ax, s, 0.0, 1.5, 3.0, 1.5)
    frustum(m, bot, tp, y_base, top - 1.2, SAND)
    prism(m, nose_plan(ax, s, 0.0, 1.9, 3.5, 0.0, (False, False)), top - 1.2, top, SAND)


def build():
    fr0, ax0, _ = load_axis(F, WAY, True)
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(mid[0], mid[1])
    fr, ax, _ = load_axis(F, WAY, True, origin=(lat0, lon0))
    L = ax.L
    k = L / 514.2
    sup = [s * k for s in SUP]
    ground = ground_fn(F, WAY, DATUM, True, L)
    m = BMesh()
    for (kind, v), a, b in zip(KINDS, sup[:-1], sup[1:]):
        if kind == "g":
            plate_girder(m, ax, a, b, v)
        else:
            for t in (-TT, TT):
                truss_plane(m, ax, t, a, b, DECK - 0.9, TRUSS_YB, v, kind="pratt", chord=(0.8, 0.9), web=(0.4, 0.5), sw=BLACKST, sw_web=BLACKST)
            S = [a + (b - a) * i / v for i in range(v + 1)]
            for s in S:                                   # floor beams and sway struts
                beam(m, ax.p3(s, -TT, DECK - 1.0), ax.p3(s, TT, DECK - 1.0), 1.0, 0.4, BLACKST)
                beam(m, ax.p3(s, -TT, (DECK + TRUSS_YB) / 2), ax.p3(s, TT, (DECK + TRUSS_YB) / 2), 0.3, 0.3, BLACKST)
            for i in range(v):
                x_brace(m, ax, S[i], S[i + 1], -TT, TT, DECK - 1.2, 0.25, 0.25, BLACKST)
                x_brace(m, ax, S[i], S[i + 1], -TT, TT, TRUSS_YB, 0.25, 0.25, BLACKST)
            for t in (-1.25, 1.25):                       # stringers
                ribbon(m, ax, a, b, t - 0.2, t + 0.2, DECK - 1.3, DECK - 0.3, BLACKST, step=20.0)
    track(m, ax, sup[0], sup[-1])
    # abutments
    for s, sg in ((sup[0], -1), (sup[-1], 1)):
        ribbon(m, ax, s - (3.0 if sg < 0 else 0.0), s + (0.0 if sg < 0 else 3.0), -3.6, 3.6, ground(s) - 2.0, DECK - 0.3, CONCD)
    # supports
    for s in RIVER_PIERS:
        river_pier(m, ax, s * k, min(-6.0, ground(s * k) - 1.5))
    for s in TOWERS:
        top = DECK - 3.4 - 0.2
        tower(m, ax, s * k, top, ground(s * k) - 0.5)
    # girder / truss transition towers on top of the 354 pier
    tower(m, ax, 354.0 * k, DECK - 3.4 - 0.2, TRUSS_YB - 0.5)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=DATUM, parts=[("br_r22_clover_bar_railway", m)], frame=fr, axis=ax)
