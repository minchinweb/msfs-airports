"""Shared builder for the Henday sites made from OSM ways and the 2018 LiDAR alone (H27 Calgary Trail / Gateway, H28 Blackmud Creek).

Every deck is a "seed" OSM bridge way.  Its chain is the seed plus the connecting ways before and after it (up to REACH m each way,
following the OSM topology in geometry.json `osm_added_2026_11_23`), so the deck can be found in the LiDAR wherever OSM cuts the
way, and the approach can run on past the deck end.

sample(site) reads the gitignored 1 m DSM / DTM clips and writes elevation/<site>-samples.json (committed): along each chain every
STEP m the first return at the centreline, the bare earth at the centreline, the embankment crown (highest bare earth within 3 m) and
the side ground left and right; and the bare earth where every other road, railway or stream crosses the chain.  build_site() reads
only that file and geometry.json.

From the samples:
  * the structure is the run of the chain where the first return stands more than RUN_H above the bare earth (the DTM is
    interpolated under a deck), grown by 2 m at each end;
  * the deck top is a robust polynomial through the first returns over the run, lowered 0.12 m (traffic, rails), as in H39;
  * the road under each crossing is the bare earth there.
Assumed (flagged in each site docstring): deck widths from the lane count (3.7 m lanes, 3.0 m right and 1.0 m left shoulder,
0.5 m concrete barriers), girder depth, pier sizes, where the piers stand (in the gaps between the roads under the deck, never more
than MAXSPAN apart), approach widths and 4:1 slopes.
"""
import json, math
from bridgelib import *

REF = ROOT / "docs/edmonton-bridges/reference"
STEP = 2.0
REACH = 170.0
RUN_H = 1.5
MAXSPAN = 46.0
SLOPE = 4.0
GRADE = 0.06
APP_MAX = 150.0
MAXDROP = 6.0      # m: the side slope stops 24 m out; beyond it the sim's terrain carries the embankment (valleys, loops)
LANE, SH_R, SH_L, BARRIER = 3.7, 3.0, 1.0, 0.5


def width(lanes):
    return lanes * LANE + SH_R + SH_L + 2 * BARRIER


# OSM topology -------------------------------------------------------------------------------------
def _ways(folder):
    g = json.load(open(REF / folder / "geometry.json", encoding="utf-8"))
    return {w["osm_way"]: w for w in g["osm_added_2026_11_23"]["ways"]}


def _key(p):
    return (round(p[0], 6), round(p[1], 6))


def chain_ways(folder, seed, reach=REACH):
    """[(way, reversed?)] in travel order, the seed in the middle, extended along OSM prev / next ways by about `reach` m each side.
    Where several ways join, the one that turns least is taken."""
    W = _ways(folder)
    road = {k: w for k, w in W.items() if w["tags"].get("highway") and not w.get("clipped_out")}
    starts, ends = {}, {}
    for k, w in road.items():
        starts.setdefault(_key(w["nodes"][0]), []).append(k)
        ends.setdefault(_key(w["nodes"][-1]), []).append(k)
    fr = Frame(*W[seed]["nodes"][0])

    def vec(a, b):
        ea, na = fr.en(*a)
        eb, nb = fr.en(*b)
        ln = math.hypot(eb - ea, nb - na) or 1.0
        return ((eb - ea) / ln, (nb - na) / ln)

    out = [seed]
    used = {seed}
    # forward
    cur, run = seed, 0.0
    while run < reach:
        nd = road[cur]["nodes"]
        d0 = vec(nd[-2], nd[-1])
        cands = [k for k in starts.get(_key(nd[-1]), []) if k not in used]
        if not cands:
            break
        nxt = max(cands, key=lambda k: sum(a * b for a, b in zip(d0, vec(road[k]["nodes"][0], road[k]["nodes"][1]))))
        out.append(nxt)
        used.add(nxt)
        run += fr.axis(road[nxt]["nodes"]).L
        cur = nxt
    # backward
    cur, run = seed, 0.0
    while run < reach:
        nd = road[cur]["nodes"]
        d0 = vec(nd[0], nd[1])
        cands = [k for k in ends.get(_key(nd[0]), []) if k not in used]
        if not cands:
            break
        prv = max(cands, key=lambda k: sum(a * b for a, b in zip(d0, vec(road[k]["nodes"][-2], road[k]["nodes"][-1]))))
        out.insert(0, prv)
        used.add(prv)
        run += fr.axis(road[prv]["nodes"]).L
        cur = prv
    return out


def chain_axis(folder, fr, ways):
    """Axis through the chain and {way: (s_start, s_end)}."""
    W = _ways(folder)
    pts, marks, cum = [], {}, 0.0
    for w in ways:
        nd = W[w]["nodes"]
        ax = fr.axis(nd)
        marks[w] = (cum, cum + ax.L)
        cum += ax.L
        pts += [fr.en(*p) for p in (nd if not pts else nd[1:])]
    return Axis(pts), marks


def _seg_x(p, q, a, b):
    """Intersection parameter (u on p-q, v on a-b) of two segments or None."""
    d1 = (q[0] - p[0], q[1] - p[1])
    d2 = (b[0] - a[0], b[1] - a[1])
    den = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(den) < 1e-9:
        return None
    u = ((a[0] - p[0]) * d2[1] - (a[1] - p[1]) * d2[0]) / den
    v = ((a[0] - p[0]) * d1[1] - (a[1] - p[1]) * d1[0]) / den
    if 0 <= u <= 1 and 0 <= v <= 1:
        return u, v
    return None


def crossings(folder, fr, ax, skip):
    """Every other road / railway / stream way crossing the axis: [(s, way, kind, (de, dn) of the crossing way, (e, n))]."""
    out = []
    for k, w in _ways(folder).items():
        if k in skip:
            continue
        t = w["tags"]
        kind = "stream" if t.get("waterway") else "rail" if t.get("railway") else "road" if t.get("highway") else None
        if kind is None or t.get("highway") in ("footway", "cycleway", "path", "service", "track", "steps"):
            continue
        q = [fr.en(*p) for p in w["nodes"]]
        for a, b in zip(q[:-1], q[1:]):
            for i, (p0, p1) in enumerate(zip(ax.p[:-1], ax.p[1:])):
                r = _seg_x(p0, p1, a, b)
                if r:
                    s = ax.cum[i] + r[0] * (ax.cum[i + 1] - ax.cum[i])
                    ln = math.hypot(b[0] - a[0], b[1] - a[1]) or 1.0
                    out.append((s, k, kind, ((b[0] - a[0]) / ln, (b[1] - a[1]) / ln), (a[0] + r[1] * (b[0] - a[0]), a[1] + r[1] * (b[1] - a[1]))))
    out.sort()
    return out


# sampling (needs the gitignored LiDAR clips) ------------------------------------------------------
def sample(folder, site, lat0, lon0, decks):
    from lidar_pil import Grid
    base = REF / folder / "elevation"
    dtm, dsm = Grid(base / "dtm-2018-1m.tif"), Grid(base / "dsm-2018-1m.tif")
    fr = Frame(lat0, lon0)

    def at(g, e, n):
        v = g.at(*fr.ll(e, n))
        return None if v != v else round(v, 3)
    out = {}
    for d in decks:
        ways = chain_ways(folder, d["seed"])
        ax, marks = chain_axis(folder, fr, ways)
        w = width(d["lanes"])
        ss = [round(i * STEP, 3) for i in range(int(ax.L / STEP) + 1)]
        rec = dict(ways=ways, ss=ss, dsm=[], dtm=[], crown=[], gl=[], gr=[])
        for s in ss:
            e, n = ax.en(s, 0)
            rec["dsm"].append(at(dsm, e, n))
            rec["dtm"].append(at(dtm, e, n))
            v = [x for x in (at(dtm, *ax.en(s, t)) for t in (-3, -1.5, 0, 1.5, 3)) if x is not None]
            rec["crown"].append(max(v) if v else None)
            for key, sg in (("gl", 1), ("gr", -1)):
                v = [x for x in (at(dtm, *ax.en(s, sg * (w / 2 + q))) for q in (8, 12, 16, 20, 24, 28)) if x is not None]
                rec[key].append(min(v) if v else None)
        xs = []
        for s, k, kind, _dir, (e, n) in crossings(folder, fr, ax, set(ways)):
            v = sorted(x for x in (at(dtm, e + a, n + b) for a in (-2, 0, 2) for b in (-2, 0, 2)) if x is not None)
            xs.append(dict(s=round(s, 2), way=k, kind=kind, ground=v[len(v) // 2] if v else None))
        rec["cross"] = xs
        out[str(d["seed"])] = rec
    path = base / ("%s-samples.json" % site)
    path.write_text(json.dumps(out), encoding="utf-8")
    print("wrote", path)


# profiles -----------------------------------------------------------------------------------------
def _fill(v):
    v = list(v)
    last = None
    for i, x in enumerate(v):
        if x is None:
            v[i] = last
        else:
            last = x
    last = None
    for i in reversed(range(len(v))):
        if v[i] is None:
            v[i] = last
        else:
            last = v[i]
    return v


def _smooth(v, k):
    v = _fill(v)
    return [sum(v[max(0, i - k):i + k + 1]) / len(v[max(0, i - k):i + k + 1]) for i in range(len(v))]


def _polyfit(pts, order, tol=0.4):
    import numpy as np
    ms = sum(p[0] for p in pts) / len(pts)
    pts = [(p[0] - ms, p[1]) for p in pts]
    co = None
    for _ in range(6):
        x = np.array([p[0] for p in pts])
        y = np.array([p[1] for p in pts])
        co = np.polyfit(x, y, order)
        keep = [p for p in pts if abs(p[1] - np.polyval(co, p[0])) <= tol]
        if len(keep) < order + 6 or len(keep) == len(pts):
            break
        pts = keep
    return lambda s: float(np.polyval(co, s - ms))


def find_run(rec, marks, seed):
    """(s0, s1) of the raised run around the middle of the seed way."""
    ss, dsm, dtm = rec["ss"], _fill(rec["dsm"]), _fill(rec["dtm"])
    a, b = marks[seed]
    mid = [i for i, s in enumerate(ss) if a <= s <= b]
    lvl = sorted(dsm[i] for i in mid)[len(mid) // 2]          # median first return on the seed: the deck level
    h = []
    for x, g in zip(dsm, dtm):
        if x > lvl + 3.0:          # a higher deck, sign or wire over this one: unknown, treated as raised
            x = lvl
        h.append(x - g)
    i0 = max(mid, key=lambda i: h[i])
    i = i0
    while i > 0 and h[i - 1] > RUN_H:
        i -= 1
    j = i0
    while j < len(ss) - 1 and h[j + 1] > RUN_H:
        j += 1
    return max(0.0, ss[i] - 2.0), min(ss[-1], ss[j] + 2.0), lvl


def deck_profile(rec, s0, s1, lvl, order):
    pts = [(s, x) for s, x in zip(rec["ss"], rec["dsm"]) if x is not None and s0 + 2 <= s <= s1 - 2 and abs(x - lvl) < 2.5]
    f = _polyfit(pts, order)
    return lambda s: f(s) - 0.12


# drawing ------------------------------------------------------------------------------------------
def deck_slab(m, ax, s0, s1, y, w, lanes, slab=0.3, edge_depth=0.9, t_off=0.0):
    """Concrete deck: asphalt top, fascia, concrete barriers both sides, painted lines (yellow left edge, white right edge, dashed lanes).
    t_off moves the deck sideways off the axis."""
    lo, hi = t_off - w / 2, t_off + w / 2
    ribbon(m, ax, s0, s1, lo, hi, lambda s: y(s) - slab, y, CONC, step=8.0, sw_top=ASPHALT, sw_bot=CONCD)
    for t0, t1 in ((lo, lo + 0.3), (hi - 0.3, hi)):
        ribbon(m, ax, s0, s1, t0, t1, lambda s: y(s) - edge_depth, lambda s: y(s) - slab, CONC, step=8.0)
    for t0, t1 in ((lo, lo + BARRIER), (hi - BARRIER, hi)):
        ribbon(m, ax, s0, s1, t0, t1, y, lambda s: y(s) + 0.85, CONC, step=8.0)
    cw = lanes * LANE
    tl = hi - BARRIER - SH_L            # left edge of travel (t positive = left)
    tr = tl - cw
    ribbon(m, ax, s0, s1, tl - 0.08, tl + 0.08, y, lambda s: y(s) + 0.02, YELLOWR, step=8.0, caps=False)
    ribbon(m, ax, s0, s1, tr - 0.08, tr + 0.08, y, lambda s: y(s) + 0.02, WHITE, step=8.0, caps=False)
    lane_dashes(m, ax, s0, s1, tr, tl, lanes, lambda s: y(s), dash=3.0, gap=9.0)


def girders(m, ax, s0, s1, y, w, depth, slab=0.3, spacing=2.6, t_off=0.0, sw=None):
    sw = CONCD if sw is None else sw
    n = max(3, int(round((w - 1.2) / spacing)) + 1)
    for i in range(n):
        t = t_off - w / 2 + 0.9 + i * (w - 1.8) / (n - 1)
        ribbon(m, ax, s0, s1, t - 0.12, t + 0.12, lambda s: y(s) - slab - depth, lambda s: y(s) - slab, sw, step=8.0)
        ribbon(m, ax, s0, s1, t - 0.4, t + 0.4, lambda s: y(s) - slab - depth, lambda s: y(s) - slab - depth + 0.25, sw, step=8.0)


def abutment(m, ax, s, sg, y, w, ground, t_off=0.0):
    """Wall at a deck end (sg -1 start, +1 end) down to the ground and below."""
    yb = min(y - 3.0, ground - 1.5)
    ribbon(m, ax, s - (1.5 if sg < 0 else 0.0), s + (0.0 if sg < 0 else 1.5), t_off - w / 2 - 0.5, t_off + w / 2 + 0.5, yb, y - 0.3, CONC)


def pier(m, ax, s, y_soffit, ground, w, t_off=0.0):
    """Hammerhead pier (deck up to 10 m wide) or a cap on two / three round columns."""
    yb = ground - 1.0
    cap0 = y_soffit - 1.4
    if w <= 10.5:
        prism(m, nose_plan(ax, s, t_off, 0.9, 1.3, 0.0, (False, False)), yb, cap0, CONC)
        frustum(m, nose_plan(ax, s, t_off, 0.9, 1.3, 0.0, (False, False)), nose_plan(ax, s, t_off, 0.9, w / 2 - 0.6, 0.0, (False, False)),
                cap0, cap0 + 0.8, CONC)
        prism(m, nose_plan(ax, s, t_off, 0.9, w / 2 - 0.6, 0.0, (False, False)), cap0 + 0.8, y_soffit, CONC)
    else:
        n = 2 if w < 15 else 3
        for i in range(n):
            t = t_off - (w / 2 - 2.5) + i * (w - 5.0) / (n - 1)
            e, nn = ax.en(s, t)
            cyl(m, e, nn, 0.6, 0.6, yb, cap0 + 0.2, CONC, n=12)
        prism(m, nose_plan(ax, s, t_off, 0.8, w / 2 - 0.4, 0.0, (False, False)), cap0, y_soffit, CONC)


def approach(m, ax, sa, sb, y_start, road, crown, gl, gr, w, ys_end=None):
    """Road from sa (the deck end, height y_start) towards sb.  It moves at most GRADE towards road(s), the first-return level along
    the centreline (the road surface itself; a jump of more than 1.5 m, a deck or sign overhead, is ignored).  Where the road stands
    more than 1.5 m above the bare-earth crown the fill is held by walls (the DTM leaves walled fill out) and the sides are vertical
    concrete walls; elsewhere 4:1 grass slopes to the side ground.  ys_end pins the far end too (a gap between two decks).  An open
    end sinks into the ground where the road is less than 0.8 m above its sides, and over its last 12 m."""
    sg = 1 if sb > sa else -1
    L = abs(sb - sa)
    n = max(1, int(L / 4.0))
    rows = []
    y = y_start
    for i in range(n + 1):
        s = sa + sg * L * i / n
        c = road(s)
        if c - y > 1.5:
            c = y
        c = max(c, crown(s) - 0.1)
        if i:
            y += max(-GRADE * L / n, min(GRADE * L / n, c - y))
        yv = y
        if ys_end is not None:          # blend to the pinned far end
            f = i / n
            ylin = y_start + (ys_end - y_start) * f
            yv = ylin if abs(c - ylin) > 1.0 else c + (ylin - c) * (1 - 4 * f * (1 - f))
        h = yv - (gl(s) + gr(s)) / 2
        sink = 0.9 * max(0.0, min(1.0, (1.0 - h) / 0.8)) if (i > 2 and ys_end is None) else 0.0
        if ys_end is None and L - L * i / n < 12.0:
            sink = max(sink, 2.5 * (1 - (L - L * i / n) / 12.0))
        yd = yv - sink
        rows.append((s, yd, min(MAXDROP, max(0.3, yd - gl(s) + 0.3)), min(MAXDROP, max(0.3, yd - gr(s) + 0.3)), h, yd - crown(s) > 1.5))
    for a, b in zip(rows[:-1], rows[1:]):
        if max(a[4], b[4]) < -0.5:
            continue
        c = ax.p3((a[0] + b[0]) / 2, 0, (a[1] + b[1]) / 2 - 6)
        m.poly([ax.p3(a[0], -w / 2, a[1]), ax.p3(b[0], -w / 2, b[1]), ax.p3(b[0], w / 2, b[1]), ax.p3(a[0], w / 2, a[1])], ASPHALT, c)
        walled = a[5] or b[5]
        for sgn, k in ((1, 2), (-1, 3)):
            if walled:
                for tt in (sgn * w / 2, sgn * (w / 2 + 0.6)):
                    m.poly([ax.p3(a[0], tt, a[1] + 0.85), ax.p3(b[0], tt, b[1] + 0.85), ax.p3(b[0], tt, b[1] - b[k] - 0.5),
                            ax.p3(a[0], tt, a[1] - a[k] - 0.5)], CONC, c)
                m.poly([ax.p3(a[0], sgn * w / 2, a[1] + 0.85), ax.p3(b[0], sgn * w / 2, b[1] + 0.85),
                        ax.p3(b[0], sgn * (w / 2 + 0.6), b[1] + 0.85), ax.p3(a[0], sgn * (w / 2 + 0.6), a[1] + 0.85)], CONC, c)
            else:
                m.poly([ax.p3(a[0], sgn * w / 2, a[1]), ax.p3(b[0], sgn * w / 2, b[1]), ax.p3(b[0], sgn * (w / 2 + SLOPE * b[k]), b[1] - b[k]),
                        ax.p3(a[0], sgn * (w / 2 + SLOPE * a[k]), a[1] - a[k])], GRASS, c)
        for sgn, sw in ((1, YELLOWR), (-1, WHITE)):
            t = sgn * (w / 2 - 0.6)
            m.poly([ax.p3(a[0], t - 0.08, a[1] + 0.02), ax.p3(b[0], t - 0.08, b[1] + 0.02), ax.p3(b[0], t + 0.08, b[1] + 0.02),
                    ax.p3(a[0], t + 0.08, a[1] + 0.02)], sw, c)


def trellis(m, fr, ax, s0, s1, y, w, under_dir, under_pt, under_ground, span=44.0, spacing=8.0, depth=2.0, slab=0.3):
    """Trellis beams (CCE 2008: 44 m spans, beams 8 m apart, 600 mm wide at the bottom, 1,300 mm top flange, integral abutments):
    beams square to the road underneath, `span` long and centred on it, spaced along it under the whole skewed deck, on two MSE walls
    parallel to the road under.  The beam top follows the deck soffit where the beam crosses the deck axis."""
    ue, un = under_dir
    ve, vn = -un, ue                                     # beam direction
    pe, pn = under_pt
    # deck footprint corners projected on the road-under direction
    proj = []
    for s in (s0, s1):
        for t in (-w / 2, w / 2):
            e, n = ax.en(s, t)
            proj.append((e - pe) * ue + (n - pn) * un)
    u0, u1 = min(proj), max(proj)
    k = int(math.floor((u1 - u0) / spacing))
    us = [u0 + (u1 - u0 - k * spacing) / 2 + i * spacing for i in range(k + 1)]
    deck_s = ax.stations(s0, s1, 1.0)
    pts = [(s, ax.en(s, 0)) for s in deck_s]
    tops = []
    for u in us:
        # where this beam line meets the deck axis
        best = min(pts, key=lambda q: abs((q[1][0] - pe) * ue + (q[1][1] - pn) * un - u))
        yt = y(best[0]) - slab
        tops.append(yt)
        c0 = (pe + ue * u - ve * span / 2, pn + un * u - vn * span / 2)
        c1 = (pe + ue * u + ve * span / 2, pn + un * u + vn * span / 2)
        beam(m, (c0[0], yt - depth / 2 - 0.1, c0[1]), (c1[0], yt - depth / 2 - 0.1, c1[1]), 0.6, depth - 0.2, CONC)
        beam(m, (c0[0], yt - 0.12, c0[1]), (c1[0], yt - 0.12, c1[1]), 1.3, 0.24, CONC)
    # MSE walls along the road under, under the beam ends
    wl = Axis([(pe + ue * (u0 - 3), pn + un * (u0 - 3)), (pe + ue * (u1 + 3), pn + un * (u1 + 3))])
    yb = under_ground - 1.0
    ytop = min(tops) - depth - 0.1
    for sgn in (-1, 1):
        t = sgn * span / 2
        ribbon(m, wl, 0, wl.L, t - 0.6 if sgn < 0 else t - 1.2, t + 1.2 if sgn < 0 else t + 0.6, yb, ytop, CONC, step=None)
        ribbon(m, wl, 0, wl.L, t - 0.9, t + 0.9, ytop, ytop + 0.4, CONCD)
    return us


def arch_structure(m, ax, sc, y, w, ground, creek_dir, span=40.0, cant=18.0, rise=7.5, rib_w=7.0, rib_t=0.4, slab=1.5, skew=15.0, lanes=3):
    """Open-spandrel deck-stiffened arch (CCE 2008, Blackmud Creek): `span` m arch with `rise`, the deck running on `cant` m past each
    springing; two ribs `rib_w` wide and `rib_t` thick; cellular deck slab `slab` deep.  The springing lines are skewed `skew` degrees,
    turned towards the creek.  sc = arch centre station; y(s) = deck top; ground(s) = bare earth under the axis."""
    de, dn = ax.at(sc)[2:]
    ce, cn = creek_dir
    along, across = ce * de + cn * dn, ce * -dn + cn * de
    k = math.tan(math.radians(skew)) * (1 if along * across > 0 else -1)
    s_a, s_b = sc - span / 2 - cant, sc + span / 2 + cant
    soffit = lambda s: y(s) - slab
    # deck (cellular slab shown as a deep slab, cantilevered top slab edge)
    deck_slab(m, ax, s_a, s_b, y, w, lanes, slab=0.35, edge_depth=0.35)
    ribbon(m, ax, s_a, s_b, -w / 2 + 2.0, w / 2 - 2.0, lambda s: y(s) - slab, lambda s: y(s) - 0.35, CONC, step=4.0, sw_bot=CONCD)
    yc = soffit(sc)                                    # crown at the soffit
    ys = yc - rise
    off = max(rib_w / 2 + 0.3, w / 4)
    for tc in (-off, off):
        sh = k * tc                                    # springing skew: the whole rib slides along the axis with t

        def ya(s, sh=sh):
            u = (s - (sc + sh)) / (span / 2)
            return ys + rise * (1 - u * u)
        n = 20
        ss = [sc + sh - span / 2 + span * i / n for i in range(n + 1)]
        for a, b in zip(ss[:-1], ss[1:]):
            c = ax.p3((a + b) / 2, tc, (ya(a) + ya(b)) / 2 - 2)
            for t0, t1, sw in ((tc - rib_w / 2, tc + rib_w / 2, CONC),):
                m.poly([ax.p3(a, t0, ya(a)), ax.p3(b, t0, ya(b)), ax.p3(b, t1, ya(b)), ax.p3(a, t1, ya(a))], sw, c)
                m.poly([ax.p3(a, t0, ya(a) - rib_t), ax.p3(b, t0, ya(b) - rib_t), ax.p3(b, t1, ya(b) - rib_t), ax.p3(a, t1, ya(a) - rib_t)], CONCD, c)
                for t in (t0, t1):
                    m.poly([ax.p3(a, t, ya(a) - rib_t), ax.p3(b, t, ya(b) - rib_t), ax.p3(b, t, ya(b)), ax.p3(a, t, ya(a))], CONC, c)
        # spandrel cross walls every 5 m from the springing to 3 m short of the crown
        q = 5.0
        while q < span / 2 - 3.0:
            for s in (sc + sh - span / 2 + q, sc + sh + span / 2 - q):
                ribbon(m, ax, s - 0.25, s + 0.25, tc - rib_w / 2 + 0.2, tc + rib_w / 2 - 0.2, ya(s) - 0.1, soffit(s), CONC)
            q += 5.0
        # springing footings, sunk into the embankment
        for s in (sc + sh - span / 2, sc + sh + span / 2):
            ribbon(m, ax, s - 2.0, s + 2.0, tc - rib_w / 2 - 0.3, tc + rib_w / 2 + 0.3, min(ys - 3.0, ground(s) - 2.0), ys + 0.5, CONCD)
    for s, sg in ((s_a, -1), (s_b, 1)):
        abutment(m, ax, s, sg, y(s), w, ground(s))
    return s_a, s_b


# site build -----------------------------------------------------------------------------------------
def build_site(folder, site, lat0, lon0, datum, decks, model):
    """decks: dicts with seed, lanes, kind ("girder" / "trellis" / "arch"), optional under (the trellis road-under way), order
    (deck profile polynomial order), depth (girder depth), t_off.  Returns the gen_bridges result."""
    fr = Frame(lat0, lon0)
    smp = json.loads((REF / folder / "elevation" / ("%s-samples.json" % site)).read_text(encoding="utf-8"))
    W = _ways(folder)
    m = BMesh()
    built = []
    for d in decks:
        rec = smp[str(d["seed"])]
        ax, marks = chain_axis(folder, fr, rec["ways"])
        if d.get("t_off"):                       # deck centred off the seed way (two ways on one deck): parallel axis
            ax = Axis([ax.en(min(max(c, 0.01), ax.L - 0.01), d["t_off"]) for c in ax.cum])
        s0, s1, lvl = find_run(rec, marks, d["seed"])
        if d.get("run"):
            s0, s1 = marks[d["seed"]][0] + d["run"][0], marks[d["seed"]][0] + d["run"][1]
        if d["kind"] == "trellis":
            s0, s1 = trellis_run(folder, fr, ax, rec, s0, s1, d, width(d["lanes"]) if "width" not in d else d["width"])
        y = deck_profile(rec, s0, s1, lvl, d.get("order", 2))
        w = d.get("width", width(d["lanes"]))
        ss = rec["ss"]
        crown = profile(list(zip(ss, _smooth(rec["crown"], 1))))
        gl = profile(list(zip(ss, _smooth(rec["gl"], 2))))
        gr = profile(list(zip(ss, _smooth(rec["gr"], 2))))
        dtm = profile(list(zip(ss, _fill(rec["dtm"]))))
        dsm = _fill(rec["dsm"])
        road = profile([(s_, sorted(dsm[max(0, i - 3):i + 4])[len(dsm[max(0, i - 3):i + 4]) // 2] - 0.12) for i, s_ in enumerate(ss)])
        under = [x for x in rec["cross"] if s0 + 1 < x["s"] < s1 - 1 and x["ground"] is not None and x["ground"] < y(x["s"]) - 3.0]
        rec_out = dict(seed=d["seed"], kind=d["kind"], s0=round(s0, 1), s1=round(s1, 1), L=round(s1 - s0, 1),
                       top=(round(y(s0) + 0.0, 2), round(y((s0 + s1) / 2), 2), round(y(s1), 2)), w=round(w, 1),
                       under=[(round(x["s"] - s0, 1), x["way"], x["kind"], x["ground"]) for x in under])
        yl = lambda s, y=y: y(s) - datum
        if d["kind"] == "arch":
            creek = [x for x in rec["cross"] if x["kind"] == "stream" and s0 < x["s"] < s1]
            xs = creek[0]
            cax = fr.axis(W[xs["way"]]["nodes"])
            sc = (s0 + s1) / 2 if d.get("centre") == "run" else xs["s"]
            cdir = cax_dir(cax, ax.en(xs["s"], 0))          # creek direction at the crossing
            a, b = arch_structure(m, ax, sc, yl, w, lambda s: dtm(s) - datum, cdir, lanes=d["lanes"])
            rec_out.update(arch_centre=round(sc - s0, 1), arch_ends=(round(a, 1), round(b, 1)), creek_bed=round(min(x for x in rec["dtm"] if x) , 2))
            s0, s1 = a, b
        else:
            deck_slab(m, ax, s0, s1, yl, w, d["lanes"])
            for s, sg in ((s0, -1), (s1, 1)):
                abutment(m, ax, s, sg, yl(s), w, dtm(s) - datum)
            if d["kind"] == "trellis":
                cand = [x for x in under if x["kind"] == "road"]
                x = [c for c in cand if c["way"] == d["under"]][0] if d.get("under") else min(cand, key=lambda c: c["ground"])
                wax = fr.axis(W[x["way"]]["nodes"])
                pt = ax.en(x["s"], 0)
                udir = cax_dir(wax, pt)
                us = trellis(m, fr, ax, s0, s1, yl, w, udir, pt, x["ground"] - datum)
                rec_out.update(trellis_under=x["way"], beams=len(us))
            else:
                depth = d.get("depth", 1.8)
                girders(m, ax, s0, s1, yl, w, depth)
                piers = place_piers(s0, s1, [x["s"] for x in under], d.get("piers"))
                for s in piers:
                    g = min([dtm(s)] + [x["ground"] for x in under if abs(x["s"] - s) < 25]) - datum
                    pier(m, ax, s, yl(s) - 0.3 - depth, g, w)
                rec_out.update(piers=[round(s - s0, 1) for s in piers])
        built.append(dict(d=d, ax=ax, marks=marks, s0=s0, s1=s1, y=yl, w=w, crown=lambda s, c=crown: c(s) - datum, road=lambda s, f=road: f(s) - datum,
                          gl=lambda s, f=gl: f(s) - datum, gr=lambda s, f=gr: f(s) - datum, ways=rec["ways"], rep=rec_out))
    # approaches: from each deck end along its chain, stopping half way to another deck on the same ways
    for b in built:
        ax = b["ax"]
        for end, sg in ((b["s0"], -1), (b["s1"], 1)):
            limit = 0.0 if sg < 0 else ax.L
            stop, pin = None, None
            for o in built:
                if o is b:
                    continue
                for oe in (o["s0"], o["s1"]):
                    e, n = o["ax"].en(oe, 0)
                    sp, dist = _closest(ax, e, n)
                    if dist < 2.5 and (sp - end) * sg > 0:
                        gap = abs(sp - end)
                        if stop is None or gap < abs(stop - end):
                            stop, pin = sp, o["y"](oe)
            far = end + sg * APP_MAX
            far = max(far, 0.0) if sg < 0 else min(far, ax.L)
            if stop is not None and abs(stop - end) < APP_MAX * 2:
                mid = (end + stop) / 2
                ymid = (b["y"](end) + pin) / 2
                if abs(mid - end) > 1.0:
                    approach(m, ax, end, mid, b["y"](end), b["road"], b["crown"], b["gl"], b["gr"], approach_w(b), ys_end=ymid)
                continue
            if abs(far - end) > 8.0:
                approach(m, ax, end, far, b["y"](end), b["road"], b["crown"], b["gl"], b["gr"], approach_w(b))
    print("%s decks (seed, kind, run start/end on the chain, length, deck top start/mid/end, width, roads under):" % site.upper())
    for b in built:
        print("  ", b["rep"])
    return dict(m=m, fr=fr, report=[b["rep"] for b in built])


def trellis_run(folder, fr, ax, rec, s0, s1, d, w, span=44.0):
    """The part of a raised run that lies on the trellis: stations where some point across the deck is between the two walls
    (within span / 2 of the road under), plus 2 m."""
    W = _ways(folder)
    under = [x for x in rec["cross"] if s0 < x["s"] < s1 and x["kind"] == "road" and (not d.get("under") or x["way"] == d["under"])]
    x = min(under, key=lambda c: c["ground"] if c["ground"] is not None else 1e9)
    wax = fr.axis(W[x["way"]]["nodes"])
    pt = ax.en(x["s"], 0)
    ue, un = cax_dir(wax, pt)
    inside = [s for s in ax.stations(s0, s1, 1.0)
              if any(abs(-(ax.en(s, t)[0] - pt[0]) * un + (ax.en(s, t)[1] - pt[1]) * ue) <= span / 2 for t in (-w / 2, 0.0, w / 2))]
    return max(s0, min(inside) - 2.0), min(s1, max(inside) + 2.0)


def approach_w(b):
    return b["w"] - 2 * BARRIER


def _closest(ax, e, n):
    best = (0.0, 1e9)
    for s in ax.stations(0, ax.L, 1.0):
        q = ax.en(s, 0)
        d = math.hypot(q[0] - e, q[1] - n)
        if d < best[1]:
            best = (s, d)
    return best


def cax_dir(cax, pt):
    s, _d = _closest(cax, *pt)
    return cax.at(s)[2:]


def place_piers(s0, s1, under, fixed=None):
    """Pier stations: `fixed` (offsets from s0) when given; else one in each gap of more than 14 m between the roads under the deck
    (in its middle), then more until no span is longer than MAXSPAN, kept 7 m clear of the roads."""
    if fixed is not None:
        return [s0 + f for f in fixed]
    under = sorted(under)
    piers = []
    for a, b in zip(under[:-1], under[1:]):
        if b - a > 14.0:
            piers.append((a + b) / 2)
    for _ in range(20):
        pts = [s0] + sorted(piers) + [s1]
        worst = max(zip(pts[:-1], pts[1:]), key=lambda p: p[1] - p[0])
        if worst[1] - worst[0] <= MAXSPAN:
            break
        mid = (worst[0] + worst[1]) / 2
        cands = [mid + d for d in sorted(range(-15, 16), key=abs)]
        ok = [c for c in cands if all(abs(c - u) >= 7.0 for u in under) and worst[0] + 10 < c < worst[1] - 10]
        if not ok:
            break
        piers.append(ok[0])
    return sorted(piers)
