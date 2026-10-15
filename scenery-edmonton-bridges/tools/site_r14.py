"""R14 Tawatina Bridge (2021) and the Valley Line guideway down to the Muttart stop (P152 owns the platforms).

NOTES.md: river bridge 260 m in three spans (100 N main, 110 S main, 50 side); extradosed concrete box 3.5 m deep x 11 m wide; two
pylons on the north river pier, 24 to 30 m above the deck (30 m taken), seven stays per leg per side at 17.4 to 26.2 degrees; path hung
under the box through piers; park guideway on piers about 40 m apart, then 98 Avenue spans, then a ramp (about -5.6 percent) on fill and
retaining walls to the stop.  NO deck elevations exist in the data (the 2018 LiDAR predates it).  ASSUMED levels, chosen to meet the
published clearances: rail top 18.6 m above the river (632.0 m ASL) over the river, falling 2 percent to 98 Avenue, then 5.6 percent
to the platform level 8.68 m (621.94 m, the 2018 ground at the stop).  Axis runs north -> south between the two track ways, t positive
= east.
"""
import math
from bridgelib import *

CODE, TITLE = "R14", "Tawatina Bridge and Valley Line ramp"
RIVER = 613.26
F = "R14-tawatina"
Y0 = 18.6
Y_PLAT = 8.68
BOX_H, BOX_W = 3.5, 11.0


def ways(F_, ids):
    out = []
    for i in ids:
        n = find_way(F_, i)
        out += n if not out or out[-1] != n[0] else n[1:]
    return out


def build():
    west = ways(F, [636427023, 1221895803, 1221895802, 1221212818])
    east = ways(F, [672849775, 1221212789, 1221895804])
    fr0 = Frame(53.5395, -113.4773)
    ax0 = mid_axis(fr0, west, east, n=60)
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(*mid[:2])
    fr = Frame(lat0, lon0)
    ax_b = mid_axis(fr, west, east, n=60)
    plat_end = fr.en((53.536772 + 53.5366913) / 2, (-113.4789592 - 113.4788446) / 2 * 1)
    last = ax_b.p[-1]
    ax = Axis(ax_b.p + [plat_end])
    SB = ax_b.L                     # end of the bridge-tagged structure
    L = ax.L
    m = BMesh()

    def y_rail(s):
        if s <= 260.0:
            return Y0
        if s <= SB:
            return Y0 - 0.02 * (s - 260.0)
        return max(Y_PLAT, Y0 - 0.02 * (SB - 260.0) - 0.056 * (s - SB))
    soff = lambda s: y_rail(s) - 0.3 - BOX_H
    # box girder along the bridge, trapezoidal (11 m top, 6.4 m soffit)
    ribbon(m, ax, 0.0, SB, -BOX_W / 2, BOX_W / 2, lambda s: y_rail(s) - 0.7, lambda s: y_rail(s) - 0.3, CONC, step=15.0)
    ribbon(m, ax, 0.0, SB, -3.2, 3.2, lambda s: soff(s), lambda s: y_rail(s) - 0.7, CONC, step=15.0, sw_side=CONCD)
    for sg in (-1, 1):  # sloped outer webs
        for a, b in zip(ax.stations(0.0, SB, 15.0)[:-1], ax.stations(0.0, SB, 15.0)[1:]):
            pass
    # ramp: fill between retaining walls, tapering
    ribbon(m, ax, SB, L, -4.2, 4.2, lambda s: max(y_rail(s) - 6.0, Y_PLAT - 1.0) if False else y_rail(s) - 0.5 - 5.0 * max(0.0, (y_rail(s) - Y_PLAT) / (y_rail(SB) - Y_PLAT)), lambda s: y_rail(s) - 0.3, CONCD, step=10.0, sw_top=BALLAST)
    # track slab, rails, parapets, catenary
    for tt in (-4.8, 4.8):
        ribbon(m, ax, 0.0, SB, tt - 0.17, tt + 0.17, lambda s: y_rail(s) - 0.3, lambda s: y_rail(s) + 0.9, CONC, step=15.0)
    for tt in (-2.0, 2.0):
        ribbon(m, ax, 0.0, L, tt - 0.9, tt + 0.9, lambda s: y_rail(s) - 0.3, lambda s: y_rail(s) - 0.18, CONCD, step=10.0)
        for r in (-0.72, 0.72):
            ribbon(m, ax, 0.0, L, tt + r - 0.04, tt + r + 0.04, lambda s: y_rail(s) - 0.18, lambda s: y_rail(s) - 0.02, RAILSTEEL, step=10.0)
    for i in range(int(L // 40)):
        s = 8 + i * 40
        beam(m, ax.p3(s, 0.0, y_rail(s)), ax.p3(s, 0.0, y_rail(s) + 7.0), 0.3, 0.3, GREY)
        beam(m, ax.p3(s, -2.4, y_rail(s) + 6.6), ax.p3(s, 2.4, y_rail(s) + 6.6), 0.15, 0.15, GREY)
    st = ax.stations(0.0, L, 10.0)
    for tt in (-2.0, 2.0):
        for a, b in zip(st[:-1], st[1:]):
            beam(m, ax.p3(a, tt, y_rail(a) + 5.6), ax.p3(b, tt, y_rail(b) + 5.6), 0.05, 0.05, LAMP)
    # river piers: two legs with the path passing between, cap under the box
    for s in (100.0, 210.0):
        for tt in (-3.0, 3.0):
            prism(m, nose_plan(ax, s, tt, 1.8, 1.4, 1.6, (False, False)), -6.0, soff(s) - 1.0, CONC)
        beam(m, ax.p3(s, -4.6, soff(s) - 0.5), ax.p3(s, 4.6, soff(s) - 0.5), 3.2, 1.0, CONC)
    for s in (260.0, 300.0, 340.0, 380.0, 415.0, 445.0):
        e, n = ax.en(s, 0.0)
        cyl(m, e, n, 1.4, 1.2, 2.0, soff(s) - 0.9, CONC, n=14)
        beam(m, ax.p3(s, -3.4, soff(s) - 0.45), ax.p3(s, 3.4, soff(s) - 0.45), 2.6, 0.9, CONC)
    # abutment at the north end
    ribbon(m, ax, -2.0, 4.0, -7.0, 7.0, 3.0, y_rail(0) - 0.7, CONC)
    # pylons on the north river pier: two tapered legs 30 m above the deck, seven stays per side per leg
    PH = 30.0
    for tt in (-4.6, 4.6):
        bot = nose_plan(ax, 100.0, tt, 2.0, 0.9, 0.0, (False, False))
        top = nose_plan(ax, 100.0, tt, 0.8, 0.55, 0.0, (False, False))
        frustum(m, bot, top, y_rail(100) - 0.3, y_rail(100) + PH, CONC)
        for side in (-1, 1):
            for k in range(7):
                hh = 16.0 + k * 2.0
                ang = math.radians(26.2 - k * (26.2 - 17.4) / 6.0)
                d = hh / math.tan(ang)
                sa = 100.0 + side * d
                beam(m, ax.p3(100.0, tt * 0.97, y_rail(100) + hh), ax.p3(sa, tt, y_rail(sa) - 0.3), 0.22, 0.22, WHITEST)
    # path hung under the main spans
    path_pts = fr.axis(find_way(F, 732161091))
    ps = [project(ax, *p)[0] for p in path_pts.p]
    p0, p1 = min(ps), max(ps)
    yp = lambda s: soff(s) - 2.5
    ribbon(m, ax, p0, p1, -2.2, 2.2, lambda s: yp(s) - 0.35, lambda s: yp(s), DGREY, step=15.0)
    for tt in (-2.2, 2.2):
        railing(m, ax, p0, p1, tt, yp, h=1.4, post_step=3.0, sw_post=DARK, rails=2, step=15.0)
    for i in range(int((p1 - p0) // 10)):
        s = p0 + 5 + i * 10
        for tt in (-1.5, 1.5):
            beam(m, ax.p3(s, tt, yp(s)), ax.p3(s, tt, soff(s)), 0.15, 0.15, DARK)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_r14_tawatina", m)], frame=fr, axis=ax)
