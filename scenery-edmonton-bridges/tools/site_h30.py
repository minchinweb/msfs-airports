"""H30 Whitemud Creek arch (Anthony Henday Drive over Whitemud Creek, southwest Edmonton: 53.4286, -113.5630).

Not a bridge deck: the Henday runs on fill, and the creek and a pedestrian / wildlife path pass under it through a semi-circular arch
tunnel, completed 2005 (Canadian Consulting Engineer, "Three Crossings on Henday"; discoverAPEGA).  Sourced: one span of 20 m on 7 m
walls, the path raised inside the arch 7 m above the creek, a "giant oculus" in the centre.  The Commons photo (Kurt Bauschardt,
2012, reference/H30-whitemud-creek/photos) shows the highway on a grass embankment with the arch as a white shell portal, and the
path on a girder bridge with crosshead piers running into it.

From the 2019 City aerial (0.57 m, traced here as east / north metres from the site centre):
- the tunnel runs at about 352 degrees true under both carriageways, 83 m between the outer faces of the two portals;
- each portal is the arch shell cut back by a sloping plane: from above it is a D, 20 m across the outer face and 12.75 m (south)
  or 13.5 m (north) deep, rimmed in white, open to the sky, with transverse beams at path level showing through it;
- the oculus is a 14 m ring in the median, centred on the tunnel axis, with the same beams below;
- stepped retaining walls flare out from both portals.
From the 2018 LiDAR (elevation/h30-samples.json): creek bed 658.1-658.3 m, the highway on the fill 678.3-679.6 m, the floor seen
through the oculus about 664 m.  The bare-earth model has the fill cut away over the tunnel (a trench along the creek line).

The path deck is level at 667.1-667.6 m (first return) on both approach bridges: 9 m above the creek bed, not the published 7 m.
The sources tie the path to the springing ("raised within the arch"), so the springing is put at the measured path level, 667.0 m,
and the walls run 8.8 m from the creek bed (the published 7 m is probably from the benches beside the creek, not the bed).

Assumed (flagged): a true semicircle of 10 m inner radius (crown 677.0 m inside, 677.6 m outside, 1-2 m under the road), shell
0.6 m; the floor flat at the creek bed; the beams 0.6 x 0.9 m every 3.4 m spanning the full width; the path deck 3.4 m wide, on those
beams inside the tunnel and on single-column crosshead piers every 11.5 m outside; the path line from OSM; collar, wall and rim
thicknesses; collar and wingwall tops from the 2018 first return.  The highway over the tunnel is left to the sim's own terrain and
road: the openings (the two D's and the oculus) are flattened to below the floor so the terrain does not fill them.
"""
import json, math, sys
from bridgelib import *

CODE, TITLE = "H30", "Whitemud Creek arch"
F = "H30-whitemud-creek"
LAT0, LON0 = 53.4286, -113.5630
DATUM = 650.00
SAMPLES = ROOT / "docs/edmonton-bridges/reference" / F / "elevation/h30-samples.json"

# tunnel, traced on the 2019 aerial (east, north m from LAT0, LON0)
S_FACE = (0.6, -42.25)       # centre of the south portal's outer face (the straight edge of the D)
N_FACE = (-10.75, 40.0)      # same, north portal
D_S, D_N = 12.75, 13.5       # depth of each D from the outer face to the crown of the cut
OCULUS_S, OCULUS_R = 40.9, 7.0   # oculus centre (m along the tunnel from the south face) and inner radius

FLOOR = 658.2               # creek bed, 2018 bare earth either side of the portals
SPRING = 667.0              # springing at the path level (see the docstring)
R = 10.0                     # inner radius: 20 m span
SHELL = 0.6
WALL = 0.8
BEAM_STEP, BEAM_W, BEAM_D = 3.4, 0.6, 0.9
PATH_W = 3.4
PATH_TOP = 667.2            # path deck, 2018 first return along both approach bridges (667.1-667.6 m)
NTH = 24                     # segments round the half circle

# stepped retaining walls, traced on the 2019 aerial from each portal corner outward (east, north m)
WINGS = [
    [(-20.5, 38.25), (-29.0, 37.5), (-30.0, 47.0), (-35.0, 47.0)],
    [(-1.0, 41.75), (6.0, 42.0), (5.0, 52.5), (12.0, 53.5), (12.0, 59.0)],
    [(-9.75, -43.0), (-9.75, -45.5), (-16.5, -46.0), (-16.0, -56.5), (-22.0, -56.75)],
    [(11.0, -41.5), (19.0, -41.0), (20.0, -51.0), (28.0, -50.5)],
]
PATH_WAYS = (493371666, 493371668, 493371667)   # north bridge piece, through the tunnel, south bridge piece

GRID = dict(e0=-60, n0=-90, nx=121, ny=191)      # 1 m sample grid


def sample():
    """Write the 2018 DSM / DTM on a 1 m grid around the site (needs numpy, Pillow and the gitignored clips)."""
    from lidar_pil import Grid
    base = ROOT / "docs/edmonton-bridges/reference" / F / "elevation"
    fr = Frame(LAT0, LON0)
    out = dict(GRID)
    for k in ("dsm", "dtm"):
        g = Grid(base / ("%s-2018-1m.tif" % k))
        rows = []
        for j in range(GRID["ny"]):
            n = GRID["n0"] + j
            row = []
            for i in range(GRID["nx"]):
                v = g.at(*fr.ll(GRID["e0"] + i, n))
                row.append(None if v != v else round(v, 2))
            rows.append(row)
        out[k] = rows
    SAMPLES.write_text(json.dumps(out, separators=(",", ":")), encoding="utf-8")
    print("wrote", SAMPLES)


class Lidar:
    def __init__(self):
        d = json.loads(SAMPLES.read_text(encoding="utf-8"))
        self.d = d

    def at(self, k, e, n):
        """Bilinear height (m ASL) from layer k at (e, n)."""
        d = self.d
        x, y = e - d["e0"], n - d["n0"]
        i, j = int(math.floor(x)), int(math.floor(y))
        fx, fy = x - i, y - j
        a = d[k]
        vals = []
        for (jj, ii, w) in ((j, i, (1 - fx) * (1 - fy)), (j, i + 1, fx * (1 - fy)), (j + 1, i, (1 - fx) * fy), (j + 1, i + 1, fx * fy)):
            if 0 <= jj < d["ny"] and 0 <= ii < d["nx"] and a[jj][ii] is not None:
                vals.append((a[jj][ii], w))
        sw = sum(w for _, w in vals)
        return sum(v * w for v, w in vals) / sw if sw else float("nan")

    def near(self, k, e, n, r=1.0, how=max):
        vals = [self.at(k, e + a, n + b) for a in (-r, 0, r) for b in (-r, 0, r)]
        vals = [v for v in vals if v == v]
        return how(vals) if vals else float("nan")


# geometry -------------------------------------------------------------------------------------------
def wall_line(m, pts, ybot, ytop, th, sw, sw_top=None):
    """Wall of thickness `th` centred on the plan polyline pts [(e, n)], bottom / top heights per vertex (model y)."""
    for k in range(len(pts) - 1):
        (e0, n0), (e1, n1) = pts[k], pts[k + 1]
        ln = math.hypot(e1 - e0, n1 - n0) or 1.0
        ox, oz = -(n1 - n0) / ln * th / 2, (e1 - e0) / ln * th / 2
        b0, b1, t0, t1 = ybot[k], ybot[k + 1], ytop[k], ytop[k + 1]
        A_ = [(e0 + ox, b0, n0 + oz), (e1 + ox, b1, n1 + oz), (e1 + ox, t1, n1 + oz), (e0 + ox, t0, n0 + oz)]
        B_ = [(e0 - ox, b0, n0 - oz), (e1 - ox, b1, n1 - oz), (e1 - ox, t1, n1 - oz), (e0 - ox, t0, n0 - oz)]
        c = ((e0 + e1) / 2, (b0 + b1 + t0 + t1) / 4, (n0 + n1) / 2)
        m.poly(A_, sw, c)
        m.poly(B_, sw, c)
        m.poly([A_[3], A_[2], B_[2], B_[3]], sw if sw_top is None else sw_top, c)
        m.poly([A_[0], A_[1], B_[1], B_[0]], sw, c)
        m.poly([A_[0], A_[3], B_[3], B_[0]], sw, c)
        m.poly([A_[1], A_[2], B_[2], B_[1]], sw, c)


def build():
    lid = Lidar()
    fr = Frame(LAT0, LON0)
    A = Axis([S_FACE, N_FACE])
    L = A.L
    m = BMesh()
    y = lambda h: h - DATUM          # noqa: E731  (m ASL -> model y)
    ths = [math.pi * i / NTH for i in range(NTH + 1)]

    def lo(th):
        return D_S * math.sin(th)

    def hi(th):
        return L - D_N * math.sin(th)

    def gap(t):
        return math.sqrt(OCULUS_R ** 2 - t * t) if abs(t) < OCULUS_R else 0.0

    def P(s, th, r):
        return A.p3(s, r * math.cos(th), y(SPRING + r * math.sin(th)))

    # arch shell: inner and outer skins, cut at both portals (the D openings) and round the oculus --------------------------------
    for th0, th1 in zip(ths[:-1], ths[1:]):
        thm = (th0 + th1) / 2
        ends = {}
        for r in (R, R + SHELL):
            g0, g1 = gap(r * math.cos(th0)), gap(r * math.cos(th1))
            if g0 > 0 or g1 > 0:
                pieces = [((lo(th0), lo(th1)), (OCULUS_S - g0, OCULUS_S - g1)), ((OCULUS_S + g0, OCULUS_S + g1), (hi(th0), hi(th1)))]
            else:
                pieces = [((lo(th0), lo(th1)), (hi(th0), hi(th1)))]
            ends[r] = pieces
            for (a0, a1), (b0, b1) in pieces:
                k = max(1, int(math.ceil(max(b0 - a0, b1 - a1) / 3.0)))
                for i in range(k):
                    f0, f1 = i / k, (i + 1) / k
                    q = [P(a0 + (b0 - a0) * f0, th0, r), P(a1 + (b1 - a1) * f0, th1, r), P(a1 + (b1 - a1) * f1, th1, r), P(a0 + (b0 - a0) * f1, th0, r)]
                    sm = (a0 + b0 + a1 + b1) / 4
                    if r == R:
                        m.poly(q, CONCD, A.p3(sm, 3 * R * math.cos(thm), y(SPRING + 3 * R * math.sin(thm))))
                    else:
                        m.poly(q, WHITEST, A.p3(sm, 0.0, y(SPRING)))
        # cut faces joining the two skins at every piece end
        for (pi, po) in zip(ends[R], ends[R + SHELL]):
            for which in (0, 1):
                (i0, i1), (o0, o1) = pi[which], po[which]
                q = [P(i0, th0, R), P(i1, th1, R), P(o1, th1, R + SHELL), P(o0, th0, R + SHELL)]
                inward = 0.5 if which == 0 else -0.5
                m.poly(q, WHITEST, A.p3((i0 + i1) / 2 + inward, (R + SHELL / 2) * math.cos(thm), y(SPRING + (R + SHELL / 2) * math.sin(thm))))

    # side walls (7 m by the sources; here from the creek bed to the springing, which the LiDAR puts at the path level) -----------
    for sg in (-1, 1):
        t0, t1 = sorted((sg * R, sg * (R + WALL)))
        ribbon(m, A, 0.0, L, t0, t1, y(FLOOR - 0.6), y(SPRING), CONC, step=6.0)
    ribbon(m, A, -2.0, L + 2.0, -R, R, y(FLOOR - 0.5), y(FLOOR), CONCD, step=6.0, sw_top=BALLAST)

    # transverse beams at path level, wall to wall
    s = BEAM_STEP / 2
    while s < L:
        beam(m, A.p3(s, -R, y(PATH_TOP - 0.3 - BEAM_D / 2)), A.p3(s, R, y(PATH_TOP - 0.3 - BEAM_D / 2)), BEAM_D, BEAM_W, CONC)
        s += BEAM_STEP

    # rims: a collar on the cut edge of each portal, up to the fill beside it (2018 first return); the oculus collar -----------
    ro = R + SHELL
    for face in ("s", "n"):
        pts, bot, top = [], [], []
        for th in ths:
            sc = lo(th) if face == "s" else hi(th)
            e, n = A.en(sc, ro * math.cos(th))
            yb = SPRING + ro * math.sin(th)
            into = 1.5 if face == "s" else -1.5
            ge, gn = A.en(sc + into, (ro + 1.0) * math.cos(th) + (1.0 if math.cos(th) >= 0 else -1.0))
            g = lid.near("dsm", ge, gn, 1.0, max)
            pts.append((e, n))
            bot.append(y(yb - 0.3))
            top.append(y(min(679.0, max(yb + 0.4, g if g == g else yb + 0.4))))
        wall_line(m, pts, bot, top, 0.5, WHITEST)
    oe, on = A.en(OCULUS_S, 0.0)
    med = sorted(lid.at("dsm", oe + 10.5 * math.cos(a), on + 10.5 * math.sin(a)) for a in [2 * math.pi * i / 16 for i in range(16)])
    g_oc = med[len(med) // 2]
    ring = [A.en(OCULUS_S + (OCULUS_R + 0.25) * math.cos(a), (OCULUS_R + 0.25) * math.sin(a)) for a in [2 * math.pi * i / 32 for i in range(33)]]
    bot = []
    for e, n in ring:
        s_, t_ = project(A, e, n)
        bot.append(y(SPRING + math.sqrt(max(0.0, ro ** 2 - t_ * t_)) - 0.6))
    wall_line(m, ring, bot, [y(g_oc + 0.25)] * len(ring), 0.5, WHITEST)
    # grass apron round the oculus: hides the step where the flattened terrain inside meets the median
    for i in range(32):
        a0, a1 = 2 * math.pi * i / 32, 2 * math.pi * (i + 1) / 32
        q = [A.en(OCULUS_S + r_ * math.cos(a), r_ * math.sin(a)) for r_, a in ((OCULUS_R + 0.5, a0), (OCULUS_R + 0.5, a1), (OCULUS_R + 3.5, a1), (OCULUS_R + 3.5, a0))]
        m.poly([(e, y(g_oc + 0.08), n) for e, n in q], GRASS, (oe, y(g_oc - 5.0), on))

    # stepped retaining walls, tops from the 2018 first return along the wall line
    for w in WINGS:
        tops = [y(lid.near("dsm", e, n, 1.0, max)) for e, n in w]
        wall_line(m, w, [y(FLOOR - 0.6)] * len(w), tops, 0.5, CONC)

    # path: OSM ways chained (north bank -> tunnel -> south bank), deck level from the 2018 first return (667.1-667.6 m) ----------
    nodes = []
    for wid in PATH_WAYS:
        nn = find_way(F, wid)
        nodes += nn if not nodes else nn[1:]
    P_ = fr.axis(nodes)
    ytop = profile([(0.0, 666.65 - DATUM), (6.0, PATH_TOP - DATUM), (P_.L, PATH_TOP - DATUM)])
    ribbon(m, P_, 0.0, P_.L, -PATH_W / 2, PATH_W / 2, lambda s: ytop(s) - 0.9, ytop, CONC, step=3.0, sw_top=CONC, sw_bot=CONCD)
    for sg in (-1, 1):
        railing(m, P_, 0.0, P_.L, sg * (PATH_W / 2 - 0.1), ytop, h=1.1, post_step=2.5, sw_post=RAILSTEEL, step=6.0)

    def in_tunnel(s):
        e, n = P_.en(s)
        sa, ta = project(A, e, n)
        return 0.5 < sa < L - 0.5 and abs(ta) < R + WALL

    inside = [s_ for s_ in [P_.L * i / 400 for i in range(401)] if in_tunnel(s_)]
    s_in, s_out = min(inside), max(inside)
    piers = []
    for s0, s1, d in ((s_in, 0.0, -1), (s_out, P_.L, 1)):
        s_ = s0 + d * 11.5
        while (s_ - s1) * d < -4.0:
            piers.append(s_)
            s_ += d * 11.5
    for s_ in piers:
        e, n = P_.en(s_)
        gnd = lid.near("dtm", e, n, 1.0, min)
        yb = ytop(s_) - 0.9
        if gnd != gnd or yb - y(gnd) < 1.0:
            continue
        ribbon(m, P_, s_ - 0.5, s_ + 0.5, -0.7, 0.7, y(gnd - 0.5), yb - 0.9, CONC)
        ribbon(m, P_, s_ - 0.6, s_ + 0.6, -2.1, 2.1, yb - 0.9, yb, CONC)
    for s_, d in ((0.0, 1), (P_.L, -1)):
        e, n = P_.en(s_)
        gnd = lid.near("dtm", e, n, 1.5, min)
        ribbon(m, P_, min(s_, s_ + d * 1.2), max(s_, s_ + d * 1.2), -PATH_W / 2 - 0.3, PATH_W / 2 + 0.3, y(gnd - 0.5), ytop(s_), CONC)

    # terrain: the openings are flattened to below the floor so the sim's ground does not fill them -------------------------------
    extra = []
    oc = [fr.ll(*A.en(OCULUS_S + (OCULUS_R + 1.0) * math.cos(a), (OCULUS_R + 1.0) * math.sin(a))) for a in [2 * math.pi * i / 24 for i in range(24)]]
    extra.append(("flatten", "%s %s oculus" % (CODE, TITLE), FLOOR - 0.3, oc))
    for face in ("s", "n"):
        edge = []
        for th in ths:
            sc = lo(th) if face == "s" else hi(th)
            sc += 1.0 if face == "s" else -1.0
            edge.append(A.en(sc, (ro + 0.5) * math.cos(th)))
        sf = -1.0 if face == "s" else L + 1.0
        ring_ = [A.en(sf, (ro + 0.5))] + edge + [A.en(sf, -(ro + 0.5))]
        extra.append(("flatten", "%s %s %s portal" % (CODE, TITLE, "south" if face == "s" else "north"), FLOOR - 0.3, [fr.ll(e, n) for e, n in ring_]))
    return dict(code=CODE, title=TITLE, lat0=LAT0, lon0=LON0, alt=DATUM, parts=[("br_h30_whitemud_arch", m)], frame=fr,
                terrain_extra=extra,
                views=[("a", 250.0, 18.0), ("b", 80.0, 30.0), ("c", 300.0, 60.0)], preview=dict(span=150.0, water=False))


if __name__ == "__main__":
    if "--sample" in sys.argv:
        sample()
