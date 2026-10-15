"""R6 Quesnell Bridge (Whitemud Drive over the North Saskatchewan, 1968, widened 2008-11): eight lanes, 315.7 m, six spans, five piers.

NOTES.md / HANDOFF-T2.md.  Axis: the line midway between the west carriageway (OSM way 22916674) and the east through ways
(22916673, 944470769, 297284104), run south -> north, t positive = west.  Sourced: plan (OSM), deck level (quadratic through the 2018
LiDAR first returns on the west way, 18.3 to 20.7 m above the river), six spans 50 / 3 x 54.9 / 53.3 + 46.6 m (PIEVC 2008, IABSE 2008),
five piers each with two shafts and, after the widening, ten steel cap extensions two per pier (CISC Alberta 2011 award page), deck
overall width and the position of the median barrier, east path (4.2 m, City 2018) and Fox Drive merge lane (OSM ramp 134926900)
measured on the 2019 aerial (0.2 m/px).  Assumed (flagged in HANDOFF-T2.md): which end holds the 50 m simple span (taken from the
south, the order the papers list them), pier shaft spacing and diameter, girder count and depth (haunched 3.4 m at supports, 1.9 m
at mid-span, 2.4 m constant on the simple span), cap depth, lane widths, railing details.  Concrete grey-beige, galvanised steel
cap extensions (2015 photograph).
"""
import math
from bridgelib import *
from t2lib import *

CODE, TITLE = "R6", "Quesnell Bridge"
DATUM = 618.30
F, WEST = "R6-quesnell", 22916674
EAST_WAYS = (22916673, 944470769, 297284104)
SLAB = 0.30
SPANS = [50.0, 54.9, 54.9, 54.9, 53.3, 46.6]          # south -> north (order assumed)
CONT = [False, True, True, True, True, True]           # span 0 is the simple span; piers 2..4 join continuous spans
TW = 22.0                                              # west edge, aerial
RE0 = -20.5                                            # east road edge beyond the Fox Drive merge
PATH_W = 4.2
SHAFT_T = 6.5
SHAFT_R = 1.25


def ramp_f(s):
    """1 at the south abutment (merge lane present) falling to 0 at s = 102 m."""
    return max(0.0, 1.0 - s / 102.0)


def re(s):
    return RE0 - 3.9 * ramp_f(s)


def te(s):
    return re(s) - 0.7 - PATH_W - 0.15


def vr(m, ax, s0, s1, tlo, thi, y0, y1, sw, top=None, side=None, bot=None, step=6.0):
    """ribbon with lateral extents given as functions of s."""
    f0, f1 = (y0 if callable(y0) else (lambda s, v=y0: v)), (y1 if callable(y1) else (lambda s, v=y1: v))
    top = sw if top is None else top
    side = sw if side is None else side
    bot = sw if bot is None else bot
    ss = ax.stations(s0, s1, step)
    for a, b in zip(ss[:-1], ss[1:]):
        c = ax.p3((a + b) / 2, (tlo((a + b) / 2) + thi((a + b) / 2)) / 2, (f0((a + b) / 2) + f1((a + b) / 2)) / 2)
        V = lambda s, t, f: ax.p3(s, t, f(s))
        m.poly([V(a, tlo(a), f1), V(b, tlo(b), f1), V(b, thi(b), f1), V(a, thi(a), f1)], top, c)
        m.poly([V(a, tlo(a), f0), V(a, thi(a), f0), V(b, thi(b), f0), V(b, tlo(b), f0)], bot, c)
        m.poly([V(a, thi(a), f0), V(b, thi(b), f0), V(b, thi(b), f1), V(a, thi(a), f1)], side, c)
        m.poly([V(a, tlo(a), f0), V(b, tlo(b), f0), V(b, tlo(b), f1), V(a, tlo(a), f1)], side, c)
    for s in (s0, s1):
        t0, t1 = tlo(s), thi(s)
        c = ax.p3(s, (t0 + t1) / 2, (f0(s) + f1(s)) / 2)
        m.poly([ax.p3(s, t0, f0(s)), ax.p3(s, t1, f0(s)), ax.p3(s, t1, f1(s)), ax.p3(s, t0, f1(s))], side, c)


def build():
    nW = find_way(F, WEST)[::-1]
    nE = find_way(F, EAST_WAYS[0]) + find_way(F, EAST_WAYS[1])[1:] + find_way(F, EAST_WAYS[2])[1:]
    fr0 = Frame(*nW[0])
    ax0 = mid_axis(fr0, nW, nE)
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(mid[0], mid[1])
    fr = Frame(lat0, lon0)
    ax = mid_axis(fr, nW, nE)
    L = ax.L
    y = deck_quad(F, WEST, DATUM, True, L)
    ground = ground_fn(F, WEST, DATUM, True, L)
    k = L / sum(SPANS)
    sup = [0.0]
    for sp in SPANS:
        sup.append(sup[-1] + sp * k)
    sup[-1] = L
    piers = sup[1:-1]

    def dep(s):
        i = max(0, min(len(SPANS) - 1, next((j for j in range(len(SPANS)) if s <= sup[j + 1] + 1e-6), len(SPANS) - 1)))
        a, b = sup[i], sup[i + 1]
        x = (s - a) / (b - a)
        if not CONT[i]:
            return 2.4
        # haunch toward the supports that join continuous spans (interior piers); the north abutment end is flat
        d = 1.9
        ends = [x, 1 - x]
        for j, e in enumerate(ends):
            hs = (i > 0) if j == 0 else (i < len(SPANS) - 1 and CONT[i + 1])
            if j == 0 and i == 1:
                hs = False        # span 1 meets the simple span at pier 1: flat end
            if hs and e < 0.25:
                d = max(d, 1.9 + 1.5 * ((0.25 - e) / 0.25) ** 2)
        return d

    soff = lambda s: y(s) - SLAB - dep(s)
    m = BMesh()
    W = lambda s: TW
    # deck slab with asphalt top, concrete sides and underside
    vr(m, ax, 0.0, L, te, W, lambda s: y(s) - SLAB, y, CONC, top=ASPHALT, side=CONC, bot=CONCD, step=6.0)
    # girders: steel-grey webs under the slab, 14 lines
    n = 14
    for i in range(n):
        f = (i + 0.5) / n
        tf = lambda s, f=f: te(s) + 0.9 + f * (TW - 0.9 - (te(s) + 0.9)) - 0.0
        vr(m, ax, 0.0, L, lambda s, tf=tf: tf(s) - 0.28, lambda s, tf=tf: tf(s) + 0.28, soff, lambda s: y(s) - SLAB, CONC, bot=CONCD, step=5.0)
        vr(m, ax, 0.0, L, lambda s, tf=tf: tf(s) - 0.65, lambda s, tf=tf: tf(s) + 0.65, lambda s: soff(s) - 0.18, soff, CONCD, step=5.0)
    # diaphragms every 8 m (the 2015 photograph shows steel cross-frames)
    kd = int(L // 8.0)
    for j in range(1, kd):
        s = j * L / kd
        a, b = te(s) + 1.0, TW - 1.0
        beam(m, ax.p3(s, a, soff(s) + dep(s) * 0.45), ax.p3(s, b, soff(s) + dep(s) * 0.45), 0.25, 0.2, RAILSTEEL)
    # lane markings: west carriageway t = 3.0 .. 18.8 (4 lanes), east 4 lanes from -3.0 to re - 1.6 (merge lane in the south)
    def dashed(tfn, s0=2.0, s1=None):
        s1 = L - 2.0 if s1 is None else s1
        s = s0
        while s + 3.0 < s1:
            a, b = s, s + 3.0
            vr(m, ax, a, b, lambda q: tfn(q) - 0.07, lambda q: tfn(q) + 0.07, lambda q: y(q), lambda q: y(q) + 0.02, WHITE, step=None, top=WHITE)
            s += 9.0
    for j in (1, 2, 3):
        dashed(lambda q, j=j: 3.0 + j * (18.8 - 3.0) / 4)
        dashed(lambda q, j=j: -(3.0 + j * ((-re(q) - 1.6) - 3.0) / 4))
    for tfn, sw_ in ((lambda q: 19.0, WHITE), (lambda q: -(-re(q) - 1.6), WHITE), (lambda q: 2.8, YELLOWR), (lambda q: -2.8, YELLOWR)):
        vr(m, ax, 0.0, L, lambda q, tfn=tfn: tfn(q) - 0.08, lambda q, tfn=tfn: tfn(q) + 0.08, lambda q: y(q), lambda q: y(q) + 0.02, sw_, step=12.0)
    # median barrier, west parapet, east barrier and path
    vr(m, ax, 0.0, L, lambda s: -0.65, lambda s: 0.65, y, lambda s: y(s) + 1.05, CONC, step=12.0)
    vr(m, ax, 0.0, L, lambda s: TW - 0.55, lambda s: TW - 0.05, y, lambda s: y(s) + 0.9, CONC, step=12.0)
    vr(m, ax, 0.0, L, lambda s: TW - 0.45, lambda s: TW - 0.15, lambda s: y(s) + 0.9, lambda s: y(s) + 1.25, RAILSTEEL, step=12.0)
    vr(m, ax, 0.0, L, lambda s: re(s) - 0.7, lambda s: re(s), y, lambda s: y(s) + 1.0, CONC, step=12.0)
    vr(m, ax, 0.0, L, lambda s: te(s) + 0.15, lambda s: re(s) - 0.7, y, lambda s: y(s) + 0.12, CONCD, top=CONC, step=12.0)
    # east outer railing follows the widening: posts every 3 m, three rails
    ss = ax.stations(0.0, L, 3.0)
    for s in ss:
        beam(m, ax.p3(s, te(s) + 0.2, y(s) + 0.12), ax.p3(s, te(s) + 0.2, y(s) + 1.35), 0.12, 0.12, RAILSTEEL)
    for hh in (0.55, 0.95, 1.35):
        vr(m, ax, 0.0, L, lambda s: te(s) + 0.15, lambda s: te(s) + 0.25, lambda s, hh=hh: y(s) + 0.12 + hh - 0.05, lambda s, hh=hh: y(s) + 0.12 + hh + 0.05, RAILSTEEL, step=6.0)
    # lamps: west edge every 40 m (2015 photograph), double-arm median lamps every 40 m offset by 20 m
    s = 20.0
    while s < L:
        e, nn = ax.en(s, TW - 0.4)
        de, dn = -ax.at(s)[3], ax.at(s)[2]
        lamp(m, e, nn, y(s), 10.0, 2.4, -de, -dn)
        s += 40.0
    s = 40.0
    while s < L - 10:
        e, nn = ax.en(s, 0.0)
        de, dn = -ax.at(s)[3], ax.at(s)[2]
        lamp(m, e, nn, y(s) + 1.0, 10.0, 2.6, de, dn)
        lamp(m, e, nn, y(s) + 1.0, 10.0, 2.6, -de, -dn)
        s += 40.0
    # abutments with wing-less back walls down to the bank
    for s, sg in ((0.0, -1), (L, 1)):
        yb = min(y(s) - SLAB - dep(s) - 1.0, ground(s) - 1.2)
        ribbon(m, ax, s - (2.0 if sg < 0 else 0.0), s + (0.0 if sg < 0 else 2.0), te(s) - 0.6, TW + 0.6, yb, y(s) - SLAB, CONCD)
    # piers: two circular shafts each, a concrete cap beam, and two steel cap extensions with inclined struts (CISC 2011)
    for s in piers:
        capb = soff(s) - 0.1
        capt = capb + 0.0
        capd = 2.0
        yb = min(-5.0, ground(s) - 1.8)
        for t in (-SHAFT_T, SHAFT_T):
            e, nn = ax.en(s, t)
            cyl(m, e, nn, SHAFT_R, SHAFT_R, yb, capb - capd, PIERBEIGE, n=16)
        prism(m, nose_plan(ax, s, 0.0, 1.4, SHAFT_T + 2.6, 0.0, (False, False)), capb - capd, capb, CONC)
        for sg in (-1, 1):
            t_in = sg * (SHAFT_T + 2.6)
            t_out = (TW - 2.2) if sg > 0 else (te(s) + 2.2)
            # box top element of the extension
            ribbon(m, ax, s - 1.3, s + 1.3, min(t_in, t_out), max(t_in, t_out), capb - 1.5, capb, RAILSTEEL, sw_top=CONCD)
            # inclined strut from the shaft bracket to the outer end
            beam(m, ax.p3(s, sg * (SHAFT_T + 1.3), capb - capd - 0.6), ax.p3(s, t_out - sg * 1.5, capb - 1.5), 0.55, 0.5, RAILSTEEL)
            beam(m, ax.p3(s, sg * (SHAFT_T + 1.3), capb - capd - 0.8), ax.p3(s, sg * (SHAFT_T + 1.3), capb - capd + 0.4), 0.9, 0.5, RAILSTEEL)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=DATUM, parts=[("br_r6_quesnell", m)], frame=fr, axis=ax,
                sup=sup, y=y)
