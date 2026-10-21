"""B254 Muttart Conservatory (1976): four glass pyramids and the support greenhouses.
Apex positions are the 2018 DSM peaks inside each OSM ring (+-2 m): tropical 53.535532, -113.477289 (645.43 m); temperate 53.534903,
-113.477293 (645.16 m); arid 53.535211, -113.476792 (641.11 m); feature 53.535218, -113.47777 (641.23 m).  Floor-to-apex heights 24 m
(tropical, temperate) and 18 m (arid, feature); floor areas 660 and 381 m2, taken as square bases of 25.7 m and 19.5 m, turned 45
degrees to the grid (the mapped ring edges run SE).  Datum (y = 0) is the ground at the pyramid ring edge, 627.9 m; the pyramids stand
in a berm, so the model runs to the floor (about 4 to 6.5 m below the datum) and the sim terrain hides the rest.  The support
greenhouses (west ring, way 1287216690, ground 622.05 m) follow the 2019 orthophoto: long bays with the ridge along the ring's NW-SE axis,
an assumed 4.5 m eave and 2.5 m ridge.  Glass is opaque
pale blue-green (no transparency yet).
"""
import math
from bridgelib import *

PYRAMIDS = False     # the four glass pyramids are switched off until the model is better; the support greenhouses stay
CODE, TITLE = "B254", "Muttart Conservatory"
RIVER = 627.9
F = "P152-muttart/B254-conservatory"
G0 = 627.9
PYR = [("tropical", 53.535532, -113.477289, 645.43, 24.0, 25.7),
       ("temperate", 53.534903, -113.477293, 645.16, 24.0, 25.7),
       ("arid", 53.535211, -113.476792, 641.11, 18.0, 19.5),
       ("feature", 53.535218, -113.47777, 641.23, 18.0, 19.5)]


# (kind, (s0, s1, t0, t1)) in metres in the west ring's PCA frame; kind g = gabled house, n = narrow low link, s = flat glazed spine,
# b = flat-roofed service building.  Read off the 2019 orthophoto (docs/.../P152-muttart/B254-conservatory/aerial) turned to the axis.
HOUSES = [("g", (-34.3, 8.3, 0.9, 14.5)),       # A, NW bay on the NE side of the SW range
          ("n", (-38.3, 7.3, -4.2, 0.7)),       # B, low link
          ("g", (-57.7, 8.3, -20.6, -4.6)),     # C, widest house
          ("n", (-42.7, -5.7, -26.2, -19.6)),   # D, low link
          ("g", (-44.3, -5.1, -40.2, -26.4)),   # E
          ("g", (-5.1, 80.9, -45.8, -28.8)),    # F, the long SE house
          ("g", (17.3, 64.3, -3.8, 11.5)),      # G, stand-alone NE bay
          ("g", (15.7, 62.7, -24.2, -9.2)),     # H, stand-alone NE bay
          ("s", (8.3, 15.7, -28.8, 18.9)),      # spine joining the ranges
          ("b", (9.7, 37.3, 17.5, 31.9))]       # service building (flat roof)


def pyramid(m, e, n, apex_y, height, side, rot=math.radians(45)):
    floor = apex_y - height
    half = side / 2.0
    def corners(y):
        k = (apex_y - y) / height
        h = half * k
        return [(e + h * math.sqrt(2) * math.cos(rot + math.pi / 4 + i * math.pi / 2), n + h * math.sqrt(2) * math.sin(rot + math.pi / 4 + i * math.pi / 2)) for i in range(4)]
    base = corners(floor)
    for i in range(4):
        a, b = base[i], base[(i + 1) % 4]
        m.poly([(a[0], floor, a[1]), (b[0], floor, b[1]), (e, apex_y, n)], GLASSLT, (e, floor + height * 0.3, n))
    # steel frame: hip ribs, horizontal rings every 3 m, a louvred band under the apex
    for a in base:
        beam(m, (a[0], floor, a[1]), (e, apex_y, n), 0.25, 0.25, DGREY)
    y = floor + 3.0
    while y < apex_y - 1.0:
        ring = corners(y)
        for i in range(4):
            a, b = ring[i], ring[(i + 1) % 4]
            beam(m, (a[0], y, a[1]), (b[0], y, b[1]), 0.12, 0.12, DGREY)
        y += 3.0
    top = corners(apex_y - height * 0.12)
    for i in range(4):
        a, b = top[i], top[(i + 1) % 4]
        beam(m, (a[0], apex_y - height * 0.12, a[1]), (b[0], apex_y - height * 0.12, b[1]), 0.6, 0.6, METAL)


def build():
    pts = [(la, lo) for _n, la, lo, *_r in PYR]
    lat0 = sum(p[0] for p in pts) / 4
    lon0 = sum(p[1] for p in pts) / 4
    fr = Frame(lat0, lon0)
    m = BMesh()
    for name, la, lo, apex, h, side in (PYR if PYRAMIDS else []):
        e, n = fr.en(la, lo)
        pyramid(m, e, n, apex - G0, h, side)
    # west ring: six gabled glass houses along its long axis
    ring = [fr.en(*p) for p in find_way(F, 1287216690)]
    cx, cy, d, lo_, hi_ = pca_axis(ring)
    perp = (-d[1], d[0])
    wid = [(p[0] - cx) * perp[0] + (p[1] - cy) * perp[1] for p in ring]
    w0, w1 = min(wid), max(wid)
    base = 622.05 - G0
    P = lambda s, t: (cx + d[0] * s + perp[0] * t, cy + d[1] * s + perp[1] * t)
    # Support greenhouses, measured on the 2019 orthophoto turned to the ring's long axis (axis runs NW -> SE; s along it from the ring
    # centroid, t across, positive to the NE).  The houses are long gabled bays with the ridge along the axis: three on the SW range
    # (C, E, F, with narrow lower links B and D between), two stand-alone bays on the NE side (G, H), a glazed spine joining them
    # and a flat-roofed service building at the NE end.  Eave/ridge heights are assumed (4.5 + 2.5 m; links 3.2 + 1.8 m).
    for kind, (s0, s1, t0, t1) in HOUSES:
        q = [P(s0, t0), P(s1, t0), P(s1, t1), P(s0, t1)]
        if kind == "b":
            prism(m, q, base - 1.0, base + 6.5, CONC)
            continue
        eave, rise = {"g": (4.5, 2.5), "n": (3.2, 1.8), "s": (3.5, 0.0)}[kind]
        prism(m, q, base - 1.0, base + eave, GLASSLT)
        if not rise:
            continue
        tm = (t0 + t1) / 2
        mid0, mid1 = P(s0, tm), P(s1, tm)
        ridge = base + eave + rise
        c0 = ((q[0][0] + q[2][0]) / 2, base, (q[0][1] + q[2][1]) / 2)
        m.poly([(q[0][0], base + eave, q[0][1]), (q[1][0], base + eave, q[1][1]), (mid1[0], ridge, mid1[1]), (mid0[0], ridge, mid0[1])], GLASSLT, c0)
        m.poly([(q[3][0], base + eave, q[3][1]), (q[2][0], base + eave, q[2][1]), (mid1[0], ridge, mid1[1]), (mid0[0], ridge, mid0[1])], GLASSLT, c0)
        for sa in (s0, s1):   # gable ends
            a, b2, tp = P(sa, t0), P(sa, t1), P(sa, tm)
            m.poly([(a[0], base + eave, a[1]), (b2[0], base + eave, b2[1]), (tp[0], ridge, tp[1])], GLASSLT, c0)
        beam(m, (mid0[0], ridge, mid0[1]), (mid1[0], ridge, mid1[1]), 0.2, 0.2, DGREY)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_b254_muttart_conservatory", m)], frame=fr,
                axis=Axis([(0, 0), (1, 0)]))
