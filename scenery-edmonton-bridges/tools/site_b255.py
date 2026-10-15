"""B255 Fairmont Hotel Macdonald (1915), 10065 100 Street.  Chateau style: limestone walls, steep copper roof (green with age), turrets.
Outline: OSM way 198826612 (Bing-traced, 2,426 m2).  LiDAR: ground at the building edge 666.83 m; tallest point 48.1 m above it
(published 47.7 m), second peak 45.3 m, at least four more at 41.7 to 43.8 m; the main roof ridge 35 to 38 m.  The eave height (27 m,
seven storeys), the 0.40 roof ratio, the turret footprints and the placement of the four lower turrets are assumptions: no drawings.
Datum (y = 0): the ground, 666.83 m.
"""
import math
from bridgelib import *

CODE, TITLE = "B255", "Fairmont Hotel Macdonald"
RIVER = 666.83
F = "B255-hotel-macdonald"
EAVE, RIDGE, K = 27.0, 37.0, 0.40


def wall(m, a, b, y0, y1, sw, out):
    mx, mz = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    ln = math.hypot(b[0] - a[0], b[1] - a[1])
    if ln < 0.05:
        return
    nx, nz = out * (b[1] - a[1]) / ln, out * -(b[0] - a[0]) / ln
    c = (mx - nx * 3.0, (y0 + y1) / 2, mz - nz * 3.0)
    m.poly([(a[0], y0, a[1]), (b[0], y0, b[1]), (b[0], y1, b[1]), (a[0], y1, a[1])], sw, c)


def tower(m, e, n, half, h_wall, apex, rot=0.0):
    """Square tower with a pyramidal copper roof and a dark cornice band."""
    pts = [(e + half * math.cos(rot + math.pi / 4 + i * math.pi / 2) * math.sqrt(2), n + half * math.sin(rot + math.pi / 4 + i * math.pi / 2) * math.sqrt(2)) for i in range(4)]
    prism(m, pts, -3.0, h_wall, CREAM, sw_top=CREAM)
    big = scale_poly(pts, 1.12)
    prism(m, big, h_wall - 0.5, h_wall + 0.3, SAND)
    for i in range(4):
        a, b = big[i], big[(i + 1) % 4]
        m.poly([(a[0], h_wall + 0.3, a[1]), (b[0], h_wall + 0.3, b[1]), (e, apex, n)], COPPER, (e, h_wall - 2.0, n))


def build():
    fr0 = Frame(53.5403, -113.4895)
    ring = [fr0.en(*p) for p in find_way(F, 198826612)]
    if ring[0] == ring[-1]:
        ring = ring[:-1]
    cx = sum(p[0] for p in ring) / len(ring)
    cz = sum(p[1] for p in ring) / len(ring)
    lat0, lon0 = fr0.ll(cx, cz)
    fr = Frame(lat0, lon0)
    ring = [fr.en(*p) for p in find_way(F, 198826612)]
    if ring[0] == ring[-1]:
        ring = ring[:-1]
    area = sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(ring, ring[1:] + ring[:1])) / 2
    out = 1.0 if area > 0 else -1.0       # outward normal of an edge a->b is out * (dz, -dx) for a counter-clockwise ring
    m = BMesh()
    n = len(ring)
    inner = [(p[0] * K, p[1] * K) for p in ring]
    for a, b, ia, ib in zip(ring, ring[1:] + ring[:1], inner, inner[1:] + inner[:1]):
        wall(m, a, b, -3.0, EAVE, CREAM, out)
        # string course and eave band
        wall(m, a, b, EAVE - 0.8, EAVE + 0.0, SAND, out)
        c = (0.0, EAVE - 10.0, 0.0)
        m.poly([(a[0], EAVE, a[1]), (b[0], EAVE, b[1]), (ib[0], RIDGE, ib[1]), (ia[0], RIDGE, ia[1])], COPPER, c)
    for i, j, k in triangulate(inner):
        m.poly([(inner[i][0], RIDGE, inner[i][1]), (inner[j][0], RIDGE, inner[j][1]), (inner[k][0], RIDGE, inner[k][1])], COPPER,
               ((inner[i][0] + inner[j][0] + inner[k][0]) / 3, RIDGE - 10.0, (inner[i][1] + inner[j][1] + inner[k][1]) / 3))
    # window bands: dark strips on the long street faces (storey lines)
    for a, b in zip(ring, ring[1:] + ring[:1]):
        ln = math.hypot(b[0] - a[0], b[1] - a[1])
        if ln < 12:
            continue
        ux, uz = (b[0] - a[0]) / ln, (b[1] - a[1]) / ln
        nx, nz = out * uz, -out * ux
        for y0 in (4.0, 8.5, 13.0, 17.5, 22.0):
            p0 = (a[0] + ux * 1.5 + nx * 0.06, y0, a[1] + uz * 1.5 + nz * 0.06)
            p1 = (b[0] - ux * 1.5 + nx * 0.06, y0, b[1] - uz * 1.5 + nz * 0.06)
            p2 = (p1[0], y0 + 1.9, p1[2])
            p3 = (p0[0], y0 + 1.9, p0[2])
            m.poly([p0, p1, p2, p3], DARK, (a[0] - nx * 3, y0, a[1] - nz * 3))
    # towers and turrets (tallest 48.1 m above ground at 53.540318, -113.489602; second 45.3 m at 53.540053, -113.489756)
    t1 = fr.en(53.540318, -113.489602)
    t2 = fr.en(53.540053, -113.489756)
    tower(m, t1[0], t1[1], 3.6, 32.0, 48.1)
    tower(m, t2[0], t2[1], 3.2, 30.0, 45.3)
    for idx, ap in ((3, 43.8), (20, 42.5), (25, 42.0)):
        e, z = ring[idx]
        e, z = e * 0.9, z * 0.9
        tower(m, e, z, 2.6, 28.0, ap)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_b255_hotel_macdonald", m)], frame=fr,
                axis=Axis([(0, 0), (1, 0)]))
