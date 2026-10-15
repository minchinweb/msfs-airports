"""Helpers shared by the Tier 2 Bridges-checkpoint models (R20, R21, R22): axes with a chosen travel direction, LiDAR curves in that
direction, the OSM outline's lateral extent, and a plate-girder highway deck.

All three axes are built NW -> SE (s = 0 at the north-west end, t positive to the north / left of that direction).  The profile
CSVs (`elevation/profiles.csv`, written by tools/lidar_pil.py) are in the OSM way's own direction, so `reverse=True` flips them.
"""
import csv, math
from bridgelib import *


def load_axis(folder, way, reverse, origin=None):
    nodes = find_way(folder, way)
    if reverse:
        nodes = nodes[::-1]
    fr = Frame(*(origin or nodes[0]))
    return fr, fr.axis(nodes), nodes


def _rows(folder, way):
    path = ROOT / "docs/edmonton-bridges/reference" / folder / "elevation/profiles.csv"
    return [(float(r["chainage_m"]), float(r["dtm_m"]), float(r["dsm_m"])) for r in csv.DictReader(open(path))
            if str(r["osm_way"]) == str(way)]


def ground_fn(folder, way, datum, reverse, L):
    """Bare earth above `datum` along the axis (25 m steps), s measured in the axis direction."""
    rows = _rows(folder, way)
    cl = max(r[0] for r in rows) or 1.0
    k = L / cl
    pts = [((cl - c) * k if reverse else c * k, d - datum) for c, d, _s in rows]
    return profile(pts)


def deck_quad(folder, way, datum, reverse, L, lift=-0.1, s0=0.0, s1=None, order=2, tol=0.45):
    """Least-squares polynomial (default quadratic) through the first-return deck samples, outliers (vehicles, lamp heads) dropped,
    lowered by `lift`: the deck top y(s) above `datum`."""
    rows = _rows(folder, way)
    cl = max(r[0] for r in rows) or 1.0
    k = L / cl
    s1 = L if s1 is None else s1
    pts = []
    for c, _d, dsm in rows:
        s = (cl - c) * k if reverse else c * k
        if s0 <= s <= s1:
            pts.append((s, dsm - datum))

    def fit(p):
        n = order + 1
        A = [[sum(x ** (i + j) for x, _ in p) for j in range(n)] for i in range(n)]
        b = [sum(y * x ** i for x, y in p) for i in range(n)]
        for i in range(n):  # gauss
            piv = max(range(i, n), key=lambda r: abs(A[r][i]))
            A[i], A[piv], b[i], b[piv] = A[piv], A[i], b[piv], b[i]
            for r in range(i + 1, n):
                f = A[r][i] / A[i][i]
                A[r] = [a - f * c for a, c in zip(A[r], A[i])]
                b[r] -= f * b[i]
        co = [0.0] * n
        for i in reversed(range(n)):
            co[i] = (b[i] - sum(A[i][j] * co[j] for j in range(i + 1, n))) / A[i][i]
        return co
    co = fit(pts)
    for _ in range(3):
        res = [y - sum(c * x ** i for i, c in enumerate(co)) for x, y in pts]
        keep = [p for p, r in zip(pts, res) if abs(r) <= tol]
        if len(keep) < order + 2:
            break
        pts = keep
        co = fit(pts)
    return lambda s: sum(c * s ** i for i, c in enumerate(co)) + lift


def outline_t(folder, outline_way, fr, ax):
    """(t_min, t_max, s_min, s_max) of an OSM outline ring in the axis frame."""
    ts, ss = [], []
    for la, lo in find_way(folder, outline_way):
        e, n = fr.en(la, lo)
        s, t = project(ax, e, n, 2000)
        ts.append(t)
        ss.append(s)
    return min(ts), max(ts), min(ss), max(ss)


def girder_deck(m, ax, s0, s1, y_fn, tlo, thi, ground, sup=(), n_girders=5, depth=3.0, slab=0.3, inner=+1, sidewalk=0,
                sidewalk_w=2.0, carriage=11.1, left_sign=+1, lamp_step=36.0, lamps_outer=True, pier_kind=None):
    """Plate-girder highway deck between s0 and s1 on abutments.

    tlo..thi: lateral extent of the deck.  inner: side (+1 / -1 in t) facing the other carriageway (concrete parapet there);
    the other side gets a blue 3-rail steel railing.  sidewalk: 0 none, or -1/+1 the side that has a raised footway.
    left_sign: side of travel's left edge (yellow edge line); carriage: carriageway width centred on t = 0.
    """
    L = s1 - s0
    # slab, asphalt top, concrete edges and underside
    ribbon(m, ax, s0, s1, tlo, thi, lambda s: y_fn(s) - slab, y_fn, CONC, step=12.0, sw_top=ASPHALT, sw_bot=CONCD)
    # girders
    tg = [tlo + 1.6 + i * (thi - tlo - 3.2) / (n_girders - 1) for i in range(n_girders)]
    for t in tg:
        ribbon(m, ax, s0, s1, t - 0.1, t + 0.1, lambda s: y_fn(s) - slab - depth, lambda s: y_fn(s) - slab, DGREY, step=12.0, caps=True)
        ribbon(m, ax, s0, s1, t - 0.4, t + 0.4, lambda s: y_fn(s) - slab - depth - 0.12, lambda s: y_fn(s) - slab - depth, DGREY, step=12.0)
    k = max(1, int(round(L / 7.5)))
    for i in range(k + 1):
        s = s0 + L * i / k
        y = y_fn(s) - slab - depth * 0.5
        beam(m, ax.p3(s, tg[0], y), ax.p3(s, tg[-1], y), depth * 0.55, 0.12, DGREY)
    # edge fascia (visible side face of the deck)
    for t, sg in ((tlo, -1), (thi, 1)):
        ribbon(m, ax, s0, s1, t - 0.05 if sg < 0 else t - 0.2, t + 0.2 if sg < 0 else t + 0.05, lambda s: y_fn(s) - slab - 0.55, y_fn, CONC, step=12.0)
    # lane lines: dashed white, yellow on the left edge of the carriageway, white on the right edge
    for j, off in enumerate((-carriage / 2 + carriage / 3, -carriage / 2 + 2 * carriage / 3)):
        ds = 9.0
        s = s0 + 2.0
        while s + 3.0 < s1:
            ribbon(m, ax, s, s + 3.0, off - 0.07, off + 0.07, lambda q: y_fn(q), lambda q: y_fn(q) + 0.02, WHITE, step=None, caps=False)
            s += ds
    tl, tr = left_sign * carriage / 2, -left_sign * carriage / 2
    ribbon(m, ax, s0, s1, tl - 0.08, tl + 0.08, y_fn, lambda s: y_fn(s) + 0.02, YELLOWR, step=12.0, caps=False)
    ribbon(m, ax, s0, s1, tr - 0.08, tr + 0.08, y_fn, lambda s: y_fn(s) + 0.02, WHITE, step=12.0, caps=False)
    # sides
    for sg in (-1, 1):
        edge = tlo if sg < 0 else thi
        tin = edge - sg * 0.25
        if sg == inner:
            ribbon(m, ax, s0, s1, tin - 0.25, tin + 0.25, y_fn, lambda s: y_fn(s) + 0.85, CONC, step=12.0)
            ribbon(m, ax, s0, s1, tin - 0.06, tin + 0.06, lambda s: y_fn(s) + 0.85, lambda s: y_fn(s) + 1.2, BLUEWALK, step=12.0)
        else:
            if sidewalk == sg:
                ribbon(m, ax, s0, s1, min(edge, edge - sg * sidewalk_w), max(edge, edge - sg * sidewalk_w), y_fn, lambda s: y_fn(s) + 0.18, CONC,
                       step=12.0, sw_top=CONC)
                railing(m, ax, s0, s1, edge - sg * 0.15, lambda s: y_fn(s) + 0.18, h=1.4, post_step=3.0, sw_post=BLUEWALK, rails=3, step=12.0, post_w=0.14)
                ribbon(m, ax, s0, s1, edge - sg * sidewalk_w - 0.2, edge - sg * sidewalk_w + 0.2, y_fn, lambda s: y_fn(s) + 0.45, CONC, step=12.0)
            else:
                ribbon(m, ax, s0, s1, edge - sg * 0.45 - 0.2, edge - sg * 0.45 + 0.2, y_fn, lambda s: y_fn(s) + 0.3, CONC, step=12.0)
                railing(m, ax, s0, s1, edge - sg * 0.3, lambda s: y_fn(s) + 0.3, h=1.1, post_step=3.0, sw_post=BLUEWALK, rails=3, step=12.0, post_w=0.14)
    # abutments (down to the ground) with a back wall
    for s, sg in ((s0, -1), (s1, 1)):
        yb = min(y_fn(s) - slab - depth - 1.0, ground(s) - 1.2)
        ribbon(m, ax, s - (1.8 if sg < 0 else 0.0), s + (0.0 if sg < 0 else 1.8), tlo - 0.7, thi + 0.7, yb, y_fn(s) - slab, CONCD)
    # lamps on the outer edge
    if lamp_step:
        outer = -inner
        s = s0 + lamp_step / 2
        while s < s1:
            e, n = ax.en(s, (thi if outer > 0 else tlo) - outer * 0.5)
            de, dn = -ax.at(s)[3], ax.at(s)[2]
            lamp(m, e, n, y_fn(s), 9.5, 2.2, -outer * de, -outer * dn)
            s += lamp_step
