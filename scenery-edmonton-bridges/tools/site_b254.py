"""B254 Muttart Conservatory (1976): four glass pyramids and the support greenhouses.
Apex positions are the 2018 DSM peaks inside each OSM ring (+-2 m): tropical 53.535532, -113.477289 (645.43 m); temperate 53.534903,
-113.477293 (645.16 m); arid 53.535211, -113.476792 (641.11 m); feature 53.535218, -113.47777 (641.23 m).  Floor-to-apex heights 24 m
(tropical, temperate) and 18 m (arid, feature); floor areas 660 and 381 m2, taken as square bases of 25.7 m and 19.5 m, turned 45
degrees to the grid (the mapped ring edges run SE).  Datum (y = 0) is the ground at the pyramid ring edge, 627.9 m; the pyramids stand
in a berm, so the model runs to the floor (about 4 to 6.5 m below the datum) and the sim terrain hides the rest.  The six support
greenhouses are placed in the west ring (way 1287216690, ground 622.05 m) with an assumed 4.5 m eave and 2.5 m ridge.  Glass is opaque
pale blue-green (no transparency yet).
"""
import math
from bridgelib import *

CODE, TITLE = "B254", "Muttart Conservatory"
RIVER = 627.9
F = "P152-muttart/B254-conservatory"
G0 = 627.9
PYR = [("tropical", 53.535532, -113.477289, 645.43, 24.0, 25.7),
       ("temperate", 53.534903, -113.477293, 645.16, 24.0, 25.7),
       ("arid", 53.535211, -113.476792, 641.11, 18.0, 19.5),
       ("feature", 53.535218, -113.47777, 641.23, 18.0, 19.5)]


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
    for name, la, lo, apex, h, side in PYR:
        e, n = fr.en(la, lo)
        pyramid(m, e, n, apex - G0, h, side)
    # west ring: six gabled glass houses along its long axis
    ring = [fr.en(*p) for p in find_way(F, 1287216690)]
    cx, cy, d, lo_, hi_ = pca_axis(ring)
    perp = (-d[1], d[0])
    wid = [(p[0] - cx) * perp[0] + (p[1] - cy) * perp[1] for p in ring]
    w0, w1 = min(wid), max(wid)
    base = 622.05 - G0
    nh = 6
    seg = (hi_ - lo_) / nh
    for i in range(nh):
        a, b = lo_ + i * seg + 0.5, lo_ + (i + 1) * seg - 0.5
        P = lambda s, t: (cx + d[0] * s + perp[0] * t, cy + d[1] * s + perp[1] * t)
        q = [P(a, w0), P(b, w0), P(b, w1), P(a, w1)]
        prism(m, q, base - 1.0, base + 4.5, GLASSLT)
        mid0, mid1 = P(a, (w0 + w1) / 2), P(b, (w0 + w1) / 2)
        ridge = base + 4.5 + 2.5
        m.poly([(q[0][0], base + 4.5, q[0][1]), (q[1][0], base + 4.5, q[1][1]), (mid1[0], ridge, mid1[1]), (mid0[0], ridge, mid0[1])], GLASSLT, ((q[0][0] + q[2][0]) / 2, base, (q[0][1] + q[2][1]) / 2))
        m.poly([(q[3][0], base + 4.5, q[3][1]), (q[2][0], base + 4.5, q[2][1]), (mid1[0], ridge, mid1[1]), (mid0[0], ridge, mid0[1])], GLASSLT, ((q[0][0] + q[2][0]) / 2, base, (q[0][1] + q[2][1]) / 2))
        beam(m, (mid0[0], ridge, mid0[1]), (mid1[0], ridge, mid1[1]), 0.2, 0.2, DGREY)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_b254_muttart_conservatory", m)], frame=fr,
                axis=Axis([(0, 0), (1, 0)]))
