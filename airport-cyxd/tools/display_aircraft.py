"""Alberta Aviation Museum frontage on Kingsway: Bomarc missile, Norseman CF-HPY on its green pylon, the stone memorial with three
flagpoles, and the CF-101B Voodoo on its blue pole.  Imported by hangars.py (place()).

Positions are the OSM `historic=aircraft` / `historic=monument` nodes (checked against the Street View photos in
docs/cyxd/hangar14-photos/).  Order from the north: museum sign, Bomarc, Norseman, memorial, Voodoo.  Kingsway runs bearing ~126 here, with
the displays on its NE side; the aircraft face across the road (bearing ~216).

Each model is built in (east, up, north) metres around its own origin (pole / pedestal base) and mirrored once at the end (see hangars.py).
Aircraft are drawn in a local frame (x = starboard, y = up, z = nose) and posed with Pose (yaw to bearing, then pitch, then bank).
"""
import math
from gen_buildings import *  # noqa: F401,F403

ROAD_BEARING = 126.0
FACE = 216.0  # the displays look across Kingsway, to the SW

# vector helpers -----------------------------------------------------------------------------
def sub(a, b): return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
def add(a, b): return (a[0] + b[0], a[1] + b[1], a[2] + b[2])
def mul(a, k): return (a[0] * k, a[1] * k, a[2] * k)
def cross(a, b): return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])
def norm(a):
    l = math.sqrt(sum(x * x for x in a)) or 1.0
    return (a[0] / l, a[1] / l, a[2] / l)
def mid(pts): return tuple(sum(p[i] for p in pts) / len(pts) for i in range(3))


class Pose:
    """Local (x starboard, y up, z nose) -> world (east, up, north): pitch about x, bank about the nose axis, yaw to `bearing`."""

    def __init__(self, bearing=0.0, pitch=0.0, bank=0.0, pivot=(0.0, 0.0, 0.0)):
        self.b, self.p, self.k, self.o = (math.radians(bearing), math.radians(pitch), math.radians(bank), pivot)

    def vec(self, v):
        x, y, z = v
        y, z = y * math.cos(self.p) + z * math.sin(self.p), z * math.cos(self.p) - y * math.sin(self.p)
        x, y = x * math.cos(self.k) + y * math.sin(self.k), y * math.cos(self.k) - x * math.sin(self.k)
        return (x * math.cos(self.b) + z * math.sin(self.b), y, -x * math.sin(self.b) + z * math.cos(self.b))

    def pt(self, p):
        return add(self.vec(p), self.o)


ID = Pose()


# solids -------------------------------------------------------------------------------------
def prism3(m, T, a, b, sw_top, sw_bot=None, sw_side=None):
    """Convex prism between corner loops `a` (bottom) and `b` (top), given in local coordinates (same corner order)."""
    A, B = [T.pt(p) for p in a], [T.pt(p) for p in b]
    c = mid(A + B)
    m.poly(B, sw_top, c)
    m.poly(A, sw_bot if sw_bot is not None else sw_top, c)
    n = len(A)
    for i in range(n):
        j = (i + 1) % n
        m.poly([A[i], A[j], B[j], B[i]], sw_side if sw_side is not None else sw_top, c)


def slab(m, T, pts_xz, y0, y1, sw_top, sw_bot=None, sw_side=None):
    prism3(m, T, [(x, y0, z) for x, z in pts_xz], [(x, y1, z) for x, z in pts_xz], sw_top, sw_bot, sw_side)


def fin(m, T, pts_zy, x0, x1, sw):
    prism3(m, T, [(x0, y, z) for z, y in pts_zy], [(x1, y, z) for z, y in pts_zy], sw)


def tbox(m, T, x0, x1, y0, y1, z0, z1, sw):
    slab(m, T, [(x0, z0), (x1, z0), (x1, z1), (x0, z1)], y0, y1, sw)


def loft(m, T, stations, top, bottom=None, n=14, caps=True):
    """Closed body through elliptical rings (z, cx, cy, rx, ry); ring vertex 0 is the top."""
    bottom = top if bottom is None else bottom
    rings = [[(cx + rx * math.sin(2 * math.pi * i / n), cy + ry * math.cos(2 * math.pi * i / n), z) for i in range(n)]
             for z, cx, cy, rx, ry in stations]
    cens = [(cx, cy, z) for z, cx, cy, rx, ry in stations]
    for k in range(len(rings) - 1):
        c = T.pt(mid([cens[k], cens[k + 1]]))
        for i in range(n):
            j = (i + 1) % n
            sw = top if math.cos((i + 0.5) * 2 * math.pi / n) > -0.2 else bottom
            m.poly([T.pt(rings[k][i]), T.pt(rings[k][j]), T.pt(rings[k + 1][j]), T.pt(rings[k + 1][i])], sw, c)
    if caps:
        for ring, cen, other in ((rings[0], cens[0], cens[1]), (rings[-1], cens[-1], cens[-2])):
            m.poly([T.pt(p) for p in ring], bottom, T.pt(other))


def rod3(m, T, p0, p1, w, sw):
    """Square strut of side w from p0 to p1 (local coordinates)."""
    d = norm(sub(p1, p0))
    a = norm(cross(d, (0, 1, 0))) if abs(d[1]) < 0.95 else (1.0, 0.0, 0.0)
    b = cross(d, a)
    corners = [add(mul(a, sx * w / 2), mul(b, sy * w / 2)) for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
    r0 = [T.pt(add(p0, c)) for c in corners]
    r1 = [T.pt(add(p1, c)) for c in corners]
    c = T.pt(mid([p0, p1]))
    for i in range(4):
        j = (i + 1) % 4
        m.poly([r0[i], r0[j], r1[j], r1[i]], sw, c)
    m.poly(r0, sw, c)
    m.poly(r1, sw, c)


def tube(m, pts, r, sw, side, n=8):
    """Round tube along the polyline `pts` (world coordinates); `side` is the horizontal normal of the plane the path lies in."""
    rings = []
    for i, p in enumerate(pts):
        t = norm(sub(pts[min(i + 1, len(pts) - 1)], pts[max(i - 1, 0)]))
        v = cross(t, side)
        rings.append([add(p, add(mul(side, r * math.cos(2 * math.pi * k / n)), mul(v, r * math.sin(2 * math.pi * k / n)))) for k in range(n)])
    for i in range(len(pts) - 1):
        c = mid([pts[i], pts[i + 1]])
        for k in range(n):
            j = (k + 1) % n
            m.poly([rings[i][k], rings[i][j], rings[i + 1][j], rings[i + 1][k]], sw, c)
    m.poly(rings[0], sw, pts[1])
    m.poly(rings[-1], sw, pts[-2])


def revolve(m, profile, sw, cx, cz, n=12, sws=None):
    """Body of revolution about the vertical axis through (cx, cz); profile = [(y, r), ...] from the bottom up.  sws = optional colour per segment."""
    rings = [[(cx + r * math.sin(2 * math.pi * i / n), y, cz + r * math.cos(2 * math.pi * i / n)) for i in range(n)] for y, r in profile]
    for k in range(len(rings) - 1):
        c = (cx, (profile[k][0] + profile[k + 1][0]) / 2, cz)
        for i in range(n):
            j = (i + 1) % n
            m.poly([rings[k][i], rings[k][j], rings[k + 1][j], rings[k + 1][i]], sws[k] if sws else sw, c)
    m.poly(rings[0], sws[0] if sws else sw, (cx, profile[1][0], cz))
    m.poly(rings[-1], sws[-1] if sws else sw, (cx, profile[-2][0], cz))


def disc(m, c, n, r, sw, k=20):
    """Flat disc at world point c facing along n."""
    n = norm(n)
    a = norm(cross(n, (0, 1, 0))) if abs(n[1]) < 0.95 else (1.0, 0.0, 0.0)
    b = cross(n, a)
    m.poly([add(c, add(mul(a, r * math.cos(2 * math.pi * i / k)), mul(b, r * math.sin(2 * math.pi * i / k)))) for i in range(k)], sw, sub(c, n))


def roundel(m, T, c, n, r):
    """RCAF roundel (blue ring, white ring, red centre) on a surface at local point c with local outward normal n."""
    wn = norm(T.vec(n))
    wc = T.pt(c)
    for k, (rr, sw) in enumerate(((r, BLUE), (r * 0.68, WHITE), (r * 0.36, RED))):
        disc(m, add(wc, mul(wn, 0.03 + 0.02 * k)), wn, rr, sw)


LEAF = [(0, 1.0), (.15, .66), (.3, .74), (.27, .40), (.60, .54), (.52, .26), (.96, .10), (.86, -.12), (.40, -.20), (.12, -.30), (.05, -.38), (.05, -1.0)]
LEAF = LEAF + [(-x, y) for x, y in LEAF[:0:-1]]   # full outline: right half down the stem, then the left half back up


def maple_flag(m, wc, along, up, wn, w, h, off=0.03):
    """Canadian flag (red | white | red in 1:2:1, 2:1 overall, red maple leaf on the white) centred on world point wc, lying in the plane spanned by the
    unit vectors along / up, facing wn.  Drawn one-sided; call it again with the opposite normal for the back."""
    at = lambda a, b, e=0.0: add(add(add(wc, mul(along, a)), mul(up, b)), mul(wn, off + e))
    back = sub(wc, wn)
    for a0, a1, sw in ((-w / 2, -w / 4, RED), (w / 4, w / 2, RED)):
        m.poly([at(a0, -h / 2), at(a1, -h / 2), at(a1, h / 2), at(a0, h / 2)], sw, back)
    m.poly([at(-w / 4, -h / 2, .004), at(w / 4, -h / 2, .004), at(w / 4, h / 2, .004), at(-w / 4, h / 2, .004)], WHITE, back)
    k = h * 0.30
    pts = [at(x * k, y * k + 0.04 * h, .008) for x, y in LEAF]
    cen = at(0, 0.1 * k + 0.04 * h, .008)
    for i in range(len(pts)):
        m.poly([cen, pts[i], pts[(i + 1) % len(pts)]], RED, back)


def flag(m, T, c, n, w, h):
    """Canadian flag on a vertical surface (the fin): c = local centre, n = local +-x outward normal, nose direction runs along the flag."""
    maple_flag(m, T.pt(c), norm(T.vec((0, 0, 1))), norm(T.vec((0, 1, 0))), norm(T.vec(n)), w, h)


def wrap_roundel(m, ax, az, wn, y, r, R):
    """RCAF roundel wrapped onto a vertical cylinder of radius R about (ax, az): rings of small quads follow the curved skin, each colour a
    hair above the last (no flat plate standing off the body)."""
    th0 = math.atan2(wn[0], wn[2])
    for k, (rr, sw) in enumerate(((r, BLUE), (r * .68, WHITE), (r * .36, RED))):
        Rk = R + .006 * (k + 1)
        P = lambda dx, dy: (ax + Rk * math.sin(th0 + dx / R), y + dy, az + Rk * math.cos(th0 + dx / R))
        n = 16
        rings = [[P(rr * j / 3 * math.cos(2 * math.pi * i / n), rr * j / 3 * math.sin(2 * math.pi * i / n)) for i in range(n)] for j in (1, 2, 3)]
        c = (ax, y, az)
        for i in range(n):
            q = (i + 1) % n
            m.poly([P(0, 0), rings[0][i], rings[0][q]], sw, c)
            for j in (1, 2):
                m.poly([rings[j - 1][i], rings[j - 1][q], rings[j][q], rings[j][i]], sw, c)


def stripe(m, T, pts, h, sw, side):
    """Cheat line: ribbon of height h through the local points `pts`, lying on a fuselage side (side = +1 starboard, -1 port)."""
    for a, b in zip(pts[:-1], pts[1:]):
        q = [T.pt((a[0] + 0.03 * side, a[1] - h / 2, a[2])), T.pt((b[0] + 0.03 * side, b[1] - h / 2, b[2])),
             T.pt((b[0] + 0.03 * side, b[1] + h / 2, b[2])), T.pt((a[0] + 0.03 * side, a[1] + h / 2, a[2]))]
        m.poly(q, sw, T.pt((0, a[1], a[2])))


def arc_pole(base, f, radius, phi_end, n=14):
    """Path of a C-shaped pole in the vertical plane along horizontal direction f: it leaves the ground at base and sweeps back and up under the belly.  Returns world points."""
    pts = []
    for i in range(n + 1):
        phi = phi_end * i / n
        s = -radius * math.sin(phi)
        pts.append((base[0] + f[0] * s, radius - radius * math.cos(phi), base[2] + f[1] * s))
    return pts


# Voodoo -------------------------------------------------------------------------------------
def voodoo():
    """McDonnell CF-101B Voodoo 101060 on a curved blue pole, nose up and pointing across Kingsway (the Street View photos 73-77, 211150).
    CF-101B: 20.5 m long, 12.1 m span, T-tail; grey with red cheat line, red-white-red flag on the fin, roundels on wings and sides."""
    m = Mesh()
    bearing, pitch, H, s0, R = FACE, 28.0, 9.2, 2.2, 4.1
    f = (math.sin(math.radians(bearing)), math.cos(math.radians(bearing)))
    T = Pose(bearing, pitch, 6.0, (-f[0] * s0, H, -f[1] * s0))
    loft(m, T, [(10.5, 0, .05, .03, .03), (10.1, 0, .05, .30, .28), (9.0, 0, .05, .62, .58), (7.5, 0, .1, .95, .8), (5.5, 0, .2, 1.2, 1.0),
                (2.5, 0, .1, 1.3, 1.1), (-1, 0, 0, 1.35, 1.1), (-5, 0, -.05, 1.3, 1.05), (-8, 0, -.1, 1.15, .9), (-10, 0, -.1, 1.0, .8)],
         ACGREY, GREY, n=16)
    loft(m, T, [(7.6, 0, .95, .03, .03), (7.0, 0, 1.05, .4, .28), (5.5, 0, 1.2, .5, .42), (4.2, 0, 1.2, .45, .35), (3.6, 0, .95, .03, .03)], GLASS, n=10)
    for sx in (-1, 1):
        loft(m, T, [(-9.9, sx * .55, -.1, .5, .5), (-10.8, sx * .55, -.1, .45, .45)], DGREY, n=10)
        tbox(m, T, sx * 1.35 - .12, sx * 1.35 + .12, -.5, .6, 2.2, 4.6, DGREY)  # intake ducts at the wing roots
        slab(m, T, [(sx * 1.1, 1.4), (sx * 6.05, -3.4), (sx * 6.05, -5.1), (sx * 1.1, -4.4)], -.45, -.1, ACGREY, GREY)
        slab(m, T, [(sx * .12, -8.6), (sx * 2.9, -9.9), (sx * 2.9, -10.7), (sx * .12, -10.6)], 5.25, 5.4, ACGREY, GREY)
        roundel(m, T, (sx * 3.9, -.1, -3.3), (0, 1, 0), .6)
        roundel(m, T, (sx * 3.9, -.45, -3.3), (0, -1, 0), .6)
        roundel(m, T, (sx * 1.38, .1, 1.5), (sx, 0, 0), .5)
        stripe(m, T, [(sx * 1.2, .35, 7.5), (sx * 1.3, .3, 3), (sx * 1.35, .25, -2), (sx * 1.3, .2, -6), (sx * 1.15, .15, -9)], .22, RED, sx)
        flag(m, T, (sx * .12, 3.3, -9.0), (sx, 0, 0), 1.7, .85)
    fin(m, T, [(-5.2, .2), (-9.9, .2), (-10.4, 5.3), (-8.7, 5.3)], -.12, .12, ACGREY)   # base sunk into the fuselage spine (it used to float 0.1-0.2 m above it)
    tube(m, arc_pole((0.0, 0.0, 0.0), f, R, 2.75), .3, BLUE, (-f[1], 0.0, f[0]), n=10)
    # round concrete plaque the pole stands on, with a bronze plate; sunk 0.05 below the ground so no face is coplanar with it
    revolve(m, [(-.05, 1.9), (.16, 1.9), (.16, .05)], LROOF, 0, 0, n=24)
    disc(m, (0.0, .18, 0.0), (0, 1, 0), 1.3, BRONZE, k=24)
    m.mirror_x()
    return m


# Norseman -----------------------------------------------------------------------------------
def norseman():
    """Noorduyn Norseman V CF-HPY on floats, on a curved green pylon among green cut-out fir trees: cream-yellow, mint cowl and wingtips,
    green cheat line, silver floats; 9.8 m long, 15.7 m span (Street View photos 210501, 211150-211358)."""
    m = Mesh()
    bearing, pitch, bank, H, s0, R = FACE, 20.0, 6.0, 5.6, 1.6, 2.3
    f = (math.sin(math.radians(bearing)), math.cos(math.radians(bearing)))
    T = Pose(bearing, pitch, bank, (-f[0] * s0, H, -f[1] * s0))
    loft(m, T, [(4.0, 0, .05, .6, .72), (2.0, 0, .1, .66, .88), (-1.0, 0, .12, .62, .82), (-3.4, 0, .25, .38, .6), (-5.0, 0, .5, .08, .2)], YELLOWR, n=12)
    loft(m, T, [(5.0, 0, .05, .1, .1), (4.9, 0, .05, .5, .5), (4.5, 0, .05, .66, .66), (4.0, 0, .05, .66, .66)], MINT, n=12)
    for sx in (-1, 1):
        slab(m, T, [(sx * .3, 2.5), (sx * 6.9, 2.5), (sx * 6.9, .3), (sx * .3, .3)], 1.3, 1.6, YELLOWR)
        slab(m, T, [(sx * 6.9, 2.5), (sx * 7.85, 2.4), (sx * 7.85, .4), (sx * 6.9, .3)], 1.3, 1.6, MINT)
        slab(m, T, [(sx * .1, -4.0), (sx * 2.4, -4.2), (sx * 2.4, -4.9), (sx * .1, -5.0)], .55, .66, YELLOWR)
        rod3(m, T, (sx * .55, -.2, 1.7), (sx * 3.7, 1.35, 1.6), .1, YELLOWR)
        rod3(m, T, (sx * .55, -.2, 1.0), (sx * 3.7, 1.35, 1.0), .08, YELLOWR)
        rod3(m, T, (sx * .1, .6, -4.3), (sx * 1.6, .55, -4.3), .06, YELLOWR)
        loft(m, T, [(4.4, sx * 1.5, -2.1, .04, .04), (3.8, sx * 1.5, -2.1, .36, .34), (2.0, sx * 1.5, -2.1, .5, .44), (-1.5, sx * 1.5, -2.1, .5, .44),
                    (-3.4, sx * 1.5, -2.1, .36, .3), (-4.1, sx * 1.5, -2.1, .04, .04)], LROOF, GREY, n=10)   # floats: a little bigger than before
        for zz in (1.9, 1.5, -.6, -1.0):        # float struts: fuselage side to the float deck
            rod3(m, T, (sx * .5, -.5, zz), (sx * 1.45, -1.7, 1.7 if zz > 0 else -.8), .12, DGREY)
        rod3(m, T, (sx * .5, -.5, 1.7), (sx * 1.5, -1.7, 1.7), .1, DGREY)
        rod3(m, T, (sx * .1, -.9, 1.7), (sx * 1.5, -1.7, 1.7), .1, DGREY)   # spreader under the belly
        rod3(m, T, (sx * .5, .35, 2.0), (sx * 3.6, 1.35, 2.0), .12, YELLOWR)     # wing struts: cabin side up to the wing underside (front pair + rear pair)
        rod3(m, T, (sx * .5, .35, .5), (sx * 3.6, 1.35, .6), .12, YELLOWR)
        rod3(m, T, (sx * .1, 1.0, 1.9), (sx * 1.6, 1.4, 1.9), .12, YELLOWR)     # cabin-roof braces to the wing root
        rod3(m, T, (sx * .1, 1.0, .7), (sx * 1.6, 1.4, .7), .12, YELLOWR)
        stripe(m, T, [(sx * .66, .15, 3.9), (sx * .66, .12, 1), (sx * .6, .2, -2.4), (sx * .38, .35, -3.4)], .16, GREEN, sx)
    tbox(m, T, -.4, .4, .6, 1.5, .3, 2.5, YELLOWR)         # centre section: cabin roof into the wing (the wings used to hover above the fuselage)
    # propeller: spinner, hub and three blades on the cowl face
    loft(m, T, [(5.55, 0, .05, .02, .02), (5.4, 0, .05, .16, .16), (5.1, 0, .05, .24, .24), (4.95, 0, .05, .2, .2)], MINT, n=10)
    for a in (90, 210, 330):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        def bp(r, wd, zz):
            return [(ca * r - sa * wd, .05 + sa * r + ca * wd, zz), (ca * r + sa * wd, .05 + sa * r - ca * wd, zz)]
        lo = bp(.15, .12, 5.1) + bp(1.55, .08, 5.1)[::-1]
        hi = bp(.15, .12, 5.2) + bp(1.55, .08, 5.2)[::-1]
        prism3(m, T, lo, hi, DARK)
    fin(m, T, [(-3.0, .7), (-4.9, .4), (-5.0, 2.5), (-4.0, 2.7)], -.06, .06, YELLOWR)
    # pylon: C-shaped green strap, base on the ground at the model origin; cut-out fir trees stand in front (the Street View photos)
    arc = arc_pole((0.0, 0.0, 0.0), f, R, 2.9)
    # mount: the strap's top end runs on into a cradle under the fuselage belly between the floats (it used to stop in mid-air)
    end = arc[-1]
    zs = min((z / 10.0 for z in range(-50, 51)), key=lambda z: math.hypot(*(T.pt((0, -1.0, z))[i] - end[i] for i in (0, 2))))
    cradle = T.pt((0, -1.0, zs))
    tube(m, arc + [cradle], .2, GREEN, (-f[1], 0.0, f[0]), n=8)
    tbox(m, T, -.45, .45, -1.15, -.7, zs - 1.0, zs + 1.0, GREEN)
    tbox(m, ID, -.9, .9, -.05, .25, -.6, .6, LROOF)                       # concrete footing under the strap
    for dx, dz in ((-3.6, -2.0), (-2.2, 3.0), (3.2, -3.4), (4.4, 1.0)):
        x, z = dx, dz
        for k, (r, y0, y1) in enumerate(((1.0, 0.0, 1.8), (.75, 1.7, 3.0), (.45, 2.9, 4.0))):
            prism3(m, ID, [(x - r, y0, z - .04), (x + r, y0, z - .04), (x + r, y0, z + .04), (x - r, y0, z + .04)],
                   [(x - r * .6, y1, z - .04), (x + r * .6, y1, z - .04), (x + r * .6, y1, z + .04), (x - r * .6, y1, z + .04)], GREEN)
    m.mirror_x()
    return m


# Bomarc -------------------------------------------------------------------------------------
def bomarc():
    """CIM-10B Bomarc 60447 standing nose-up on a grey concrete pedestal inside a low blue rail on a brick pad: white, RCAF roundels, red flag
    on the tail fins, grey ramjet pods with copper nozzles.  14.2 m long, 5.5 m span.  The wing plane lies along Kingsway."""
    m = Mesh()
    u = (math.sin(math.radians(ROAD_BEARING)), 0.0, math.cos(math.radians(ROAD_BEARING)))   # along the road
    v = (math.sin(math.radians(FACE)), 0.0, math.cos(math.radians(FACE)))                   # across it, toward the road
    W = lambda d, y, e=0.0: (u[0] * d + v[0] * e, y, u[2] * d + v[2] * e)
    m.box(-2.6, 2.6, 0, .08, -2.6, 2.6, BRICKD)                                              # brick pad
    for sx in (-1, 1):
        for sz in (-1, 1):
            m.box(sx * 1.5 - .05, sx * 1.5 + .05, 0, .95, sz * 1.5 - .05, sz * 1.5 + .05, BLUE)
    for y in (.5, .9):
        m.box(-1.5, 1.5, y, y + .06, -1.55, -1.45, BLUE)
        m.box(-1.5, 1.5, y, y + .06, 1.45, 1.55, BLUE)
        m.box(-1.55, -1.45, y, y + .06, -1.5, 1.5, BLUE)
        m.box(1.45, 1.55, y, y + .06, -1.5, 1.5, BLUE)
    revolve(m, [(.08, 1.15), (3.0, .72), (3.05, .72)], GREY, 0, 0, n=8)
    body = [(3.0, .42), (3.4, .445), (11.0, .445), (12.4, .41), (13.8, .33), (15.2, .24), (16.4, .14), (17.2, .03)]
    revolve(m, body, RWHITE, 0, 0, n=12)
    for d in (1, -1):                      # delta wings, in the road plane
        pts = [W(d * .44, 9.8), W(d * 2.75, 7.5), W(d * 2.75, 6.8), W(d * .44, 6.8)]
        prism3(m, ID, [(p[0] - v[0] * .06, p[1], p[2] - v[2] * .06) for p in pts], [(p[0] + v[0] * .06, p[1], p[2] + v[2] * .06) for p in pts], RWHITE)
        for e in (1, -1):
            disc_c = W(d * 1.8, 7.6, e * .09)
            wn = (v[0] * e, 0.0, v[2] * e)
            for k, (rr, sw) in enumerate(((.48, BLUE), (.33, WHITE), (.17, RED))):
                disc(m, add(disc_c, mul(wn, .02 * k)), wn, rr, sw)
        ex, ez = W(d * 1.2, 0)[0], W(d * 1.2, 0)[2]                                           # ramjet pods
        revolve(m, [(5.2, .36), (5.45, .43), (7.2, .43), (9.0, .43), (9.6, .3), (9.9, .05)], GREY, ex, ez, n=10,
                sws=[BRICK, GREY, GREY, RWHITE, RWHITE])
    for (a, b) in ((u, v), (v, u)):         # cruciform tail fins
        for d in (1, -1):
            pts = [(a[0] * d * .44, 3.05, a[2] * d * .44), (a[0] * d * 1.55, 3.05, a[2] * d * 1.55), (a[0] * d * 1.55, 4.1, a[2] * d * 1.55), (a[0] * d * .44, 6.3, a[2] * d * .44)]
            prism3(m, ID, [(p[0] - b[0] * .05, p[1], p[2] - b[2] * .05) for p in pts], [(p[0] + b[0] * .05, p[1], p[2] + b[2] * .05) for p in pts], RWHITE)
    for e in (1, -1):                       # body roundels and the flag on the fin face
        wn = (v[0] * e, 0.0, v[2] * e)
        wrap_roundel(m, 0.0, 0.0, wn, 9.0, .34, .445)   # follows the body's curved skin
        fc = (wn[0] * .1 + u[0] * 1.1, 4.3, wn[2] * .1 + u[2] * 1.1)
        fp = [add(fc, add(mul(u, sx * .3), (0, sy * .35, 0))) for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1))]
        m.poly([add(p, mul(wn, .02)) for p in fp], RED, sub(fc, wn))
    m.mirror_x()
    return m


# Memorial -----------------------------------------------------------------------------------
def memorial():
    """Stone memorial block with a bronze plaque on a round paved pad, three flagpoles (Canada, Alberta, a third flag) beside it; Street View 211249."""
    m = Mesh()
    ring_r = 5.2
    revolve(m, [(0, ring_r), (.18, ring_r), (.2, ring_r - .3)], LROOF, 0, 0, n=20)
    revolve(m, [(.2, ring_r - .3), (.22, 0.05)], GREY, 0, 0, n=20)
    m.box(-1.0, 1.0, .2, 2.7, -.55, .55, WALL)
    m.box(-1.15, 1.15, 2.7, 2.9, -.65, .65, WALL)
    m.box(-.7, .7, .9, 2.2, -.575, -.55, BRONZE)       # plaque, facing the road side (-Z in the pre-mirror frame is south-west enough)
    m.box(-.7, .7, .9, 2.2, .55, .575, BRONZE)
    for k, (x, z, col) in enumerate(((-3.4, -1.0, RED), (-1.9, -2.7, BLUE), (3.3, -1.5, DARK))):
        m.box(x - .05, x + .05, .2, 9.0, z - .05, z + .05, METAL)
        if col == RED:                                 # Canadian flag (maple leaf), both faces
            for sz in (1, -1):
                maple_flag(m, (x + .05 + .85, 8.45, z), (1, 0, 0), (0, 1, 0), (0, 0, sz), 1.7, .85)
            continue
        fl = [(x + .05, 8.9, z), (x + 1.7, 8.9, z), (x + 1.7, 7.7, z), (x + .05, 7.7, z)]
        m.poly(fl, col, (x + 1, 8.3, z - 1))
        m.poly(fl[::-1], col, (x + 1, 8.3, z + 1))
    m.mirror_x()
    return m


# Museum sign ---------------------------------------------------------------------------------
def museum_sign():
    """The black two-post roadside sign north of the Bomarc (Street View 210439, 210533, 210605): arched head with the logo oval, an LED
    panel and the "History Takes Flight!" board, textured from tools/assets/museum_sign.png (bottom half); face toward the NW."""
    m = Mesh(textured=True)
    th = math.radians(300.0)
    n = (math.sin(th), math.cos(th))
    ux, uz = -n[1], n[0]
    y0, FW, FH, R = 1.7, 1.9, 2.8, 0.95
    outline = [(-R, 0.0), (R, 0.0)] + [(R * math.cos(math.radians(a)), FH - R + R * math.sin(math.radians(a))) for a in range(0, 181, 15)]
    P = lambda u, v, e=0.0: (ux * u + n[0] * e, y0 + v, uz * u + n[1] * e)
    m.poly([P(u, v, 0.1) for u, v in outline], WHITE, P(0, FH / 2, -1), tex="museum",
           uvs=[(0.5 + u / FW, 1.0 - 0.5 * v / FH) for u, v in outline])
    m.poly([P(u, v, -0.1) for u, v in outline], DARK, P(0, FH / 2, 1))
    for i, (u, v) in enumerate(outline):
        j = (i + 1) % len(outline)
        m.poly([P(u, v, -0.1), P(outline[j][0], outline[j][1], -0.1), P(outline[j][0], outline[j][1], 0.1), P(u, v, 0.1)], DARK, P(0, FH / 2, 0))
    for s in (-0.7, 0.7):
        c = (ux * s, 0.0, uz * s)
        a = [(c[0] + ux * dx + n[0] * dn, 0.0, c[2] + uz * dx + n[1] * dn) for dx, dn in ((-.1, -.09), (.1, -.09), (.1, .09), (-.1, .09))]
        prism3(m, ID, a, [(p[0], y0 + FH * 0.6, p[2]) for p in a], DARK)
    m.mirror_x()
    return m


def _sign_pos():
    """9 m up Kingsway (NW) from the Bomarc and 3 m toward the road."""
    e = 9.0 * math.sin(math.radians(306)) + 3.0 * math.sin(math.radians(216))
    n_ = 9.0 * math.cos(math.radians(306)) + 3.0 * math.cos(math.radians(216))
    return 53.5651172 + n_ / KY, -113.5178105 + e / KX


# (model name, comment, builder, lat, lon): origin = pole / pedestal base, heading 0
DISPLAY = [
    ("cyxd_h14_sign", "Alberta Aviation Museum: black roadside sign with logo, LED panel and History Takes Flight board (Street View)", museum_sign, *_sign_pos()),
    ("cyxd_h14_bomarc", "Alberta Aviation Museum: CIM-10B Bomarc 60447 on its pedestal (OSM node)", bomarc, 53.5651172, -113.5178105),
    ("cyxd_h14_norseman", "Alberta Aviation Museum: Noorduyn Norseman CF-HPY on a green pylon (OSM node)", norseman, 53.5649030, -113.5173357),
    ("cyxd_h14_memorial", "Alberta Aviation Museum: memorial with three flagpoles (OSM node)", memorial, 53.5646807, -113.5168757),
    ("cyxd_h14_voodoo", "Alberta Aviation Museum: CF-101B Voodoo 101060 on a blue pole (OSM node)", voodoo, 53.5645597, -113.5163768),
]
