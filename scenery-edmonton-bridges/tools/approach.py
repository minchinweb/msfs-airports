"""Road approaches that carry a bridge deck on into the hill.

The decks are built for the raised run of an OSM way only.  The sim's terrain around them is the 2018 LiDAR / older ground, so at the
abutment the deck either hangs over a drop or stops against the slope and the road "drops" out of the model.  approach() continues the
road from the deck end: it follows the connecting OSM way when there is one (else straight on), starts at deck height and moves at
most GRADE towards the LiDAR bare-earth height, and fills the gap with a 4:1 grass embankment, so the asphalt reaches the ground and
then follows it.  Where the ground is above the road (a cutting) the road sinks into the terrain over the last FADE metres, as in
site_y79.road_fill.  Needs numpy + Pillow (lidar_pil.Grid).
"""
import json
import math

from bridgelib import ROOT, Axis, find_way, profile, ASPHALT, GRASS, CONC, WHITE, YELLOWR  # noqa: F401
from lidar_pil import Grid

REF = ROOT / "docs/edmonton-bridges/reference"
GRADE = 0.06       # m/m, steepest the road moves towards the ground
STEP = 4.0
SLOPE = 4.0        # embankment side slope (horizontal : vertical)
FADE = 14.0        # m over which the end of the approach sinks into the ground
SKIP = ("path", "sidewalk", "walkway", "cycleway", "stair", "footway", "bike", "steps", "trail", "stub", "link_ped", "pedestrian", "rail", "lrt", "track")
_grids = {}
_ways = {}


def _grid(folder):
    if folder not in _grids:
        _grids[folder] = Grid(REF / folder / "elevation/dtm-2018-1m.tif")
    return _grids[folder]


def _all_ways(folder):
    """[(osm id, part, nodes)] of every open road-like way in the site's geometry.json."""
    if folder in _ways:
        return _ways[folder]
    out, stack = [], [json.load(open(REF / folder / "geometry.json", encoding="utf-8"))]
    while stack:
        o = stack.pop()
        if isinstance(o, dict):
            if "osm_way" in o and isinstance(o.get("nodes"), list) and len(o["nodes"]) > 1:
                nd = [tuple(p) for p in o["nodes"]]
                part = str(o.get("part", "")).lower()
                if nd[0] != nd[-1] and not any(k in part for k in SKIP):
                    out.append((o["osm_way"], part, nd))
            stack += list(o.values())
        elif isinstance(o, list):
            stack += o
    _ways[folder] = out
    return out


def _d(p, q):
    return math.hypot((p[0] - q[0]) * 111320.0, (p[1] - q[1]) * 111320.0 * math.cos(math.radians(p[0])))


def continuation(folder, way, at_end):
    """Nodes of the road that continues `way` past its end (at_end) or start, oriented away from it; None when nothing joins."""
    nodes = find_way(folder, way)
    p, prev = (nodes[-1], nodes[-2]) if at_end else (nodes[0], nodes[1])
    ref = (p[0] - prev[0], (p[1] - prev[1]) * math.cos(math.radians(p[0])))
    rl = math.hypot(*ref) or 1.0
    best = None
    for wid, _part, nd in _all_ways(folder):
        if wid == way:
            continue
        for end in (0, 1):
            q = nd[0] if end == 0 else nd[-1]
            if _d(p, q) > 3.0:
                continue
            o = nd if end == 0 else nd[::-1]
            v = (o[1][0] - o[0][0], (o[1][1] - o[0][1]) * math.cos(math.radians(p[0])))
            dot = (v[0] * ref[0] + v[1] * ref[1]) / ((math.hypot(*v) or 1.0) * rl)
            if dot > 0.3 and (best is None or dot > best[0]):
                best = (dot, o)
    return best[1] if best else None


def approach(m, fr, folder, way, way_ax, s_edge, sign, y0, w, datum, maxlen=110.0):
    """Add the road that carries on from station s_edge of `way` (axis way_ax, in frame fr) towards its end (sign +1) or its start
    (sign -1): first the rest of the way itself, then the connecting road, else straight on.  y0 = deck height at s_edge (m above
    `datum`), w = width."""
    cum = way_ax.cum
    pts = [way_ax.at(s_edge)[:2]]
    if sign > 0:
        pts += [way_ax.p[i] for i, c in enumerate(cum) if c > s_edge + 0.5]
    else:
        pts += [way_ax.p[i] for i, c in reversed(list(enumerate(cum))) if c < s_edge - 0.5]
    nxt = continuation(folder, way, sign > 0)
    if nxt is not None:
        pts += [fr.en(*p) for p in nxt[1:]]
    else:                                # straight on along the last segment
        (e0, n0), (e1, n1) = pts[-2] if len(pts) > 1 else way_ax.at(s_edge)[:2], pts[-1]
        ln = math.hypot(e1 - e0, n1 - n0)
        if ln < 1e-6:
            de, dn = way_ax.at(s_edge)[2:]
            de, dn = de * sign, dn * sign
        else:
            de, dn = (e1 - e0) / ln, (n1 - n0) / ln
        pts.append((e1 + de * maxlen, n1 + dn * maxlen))
    if len(pts) < 2:
        return None
    ax = Axis(pts)
    L = min(ax.L, maxlen)
    if L < 8.0:
        return None
    g = _grid(folder)

    def ground(s, t):
        e, n = ax.en(s, t)
        la, lo = fr.ll(e, n)
        v = g.at(la, lo)
        return None if v != v else v - datum
    rows, y = [], y0
    prev_g = None
    ss = [i * STEP for i in range(int(L / STEP) + 1)]
    for s in ss:
        gc, gl_, gr_ = ground(s, 0.0), ground(s, w / 2 + 4.0), ground(s, -(w / 2 + 4.0))
        if gc is None:
            gc = prev_g if prev_g is not None else y
        prev_g = gc
        gl_ = gc if gl_ is None else gl_
        gr_ = gc if gr_ is None else gr_
        y += max(-GRADE * STEP, min(GRADE * STEP, gc + 0.35 - y)) if s > 0 else 0.0
        rows.append((s, y, gc, gl_, gr_))
    n = len(rows)
    out = []
    for i, (s, yv, gc, gl_, gr_) in enumerate(rows):
        sink = 0.0
        if L - s < FADE:
            sink = 2.5 * (1 - (L - s) / FADE)
        yd = yv - sink
        out.append((s, yd, max(0.3, yd - gl_ + 0.3), max(0.3, yd - gr_ + 0.3), yd - gc))
    for a, b in zip(out[:-1], out[1:]):
        if max(a[4], b[4]) < -1.0:       # road well below the terrain: nothing to show
            continue
        c = ax.p3((a[0] + b[0]) / 2, 0, (a[1] + b[1]) / 2 - 6)
        m.poly([ax.p3(a[0], -w / 2, a[1]), ax.p3(b[0], -w / 2, b[1]), ax.p3(b[0], w / 2, b[1]), ax.p3(a[0], w / 2, a[1])], ASPHALT, c)
        for sg, k in ((1, 2), (-1, 3)):
            m.poly([ax.p3(a[0], sg * w / 2, a[1]), ax.p3(b[0], sg * w / 2, b[1]),
                    ax.p3(b[0], sg * (w / 2 + SLOPE * b[k]), b[1] - b[k]), ax.p3(a[0], sg * (w / 2 + SLOPE * a[k]), a[1] - a[k])], GRASS, c)
    return ax
