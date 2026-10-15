"""H52 Sherwood Park Cloverleaf (Sherwood Park Freeway over Anthony Henday Drive, Strathcona County): four overpass decks, the
flyover, three loops, collector ramps and the freeway / Wye Road approaches.

Sourced (docs/edmonton-bridges/reference/H52-sherwood-park-cloverleaf NOTES.md, HANDOFF-T2.md):
  * plan: OSM ways (decks 34572698 E-7 eastbound, 232709695 W-8 westbound, 103485448 EN1-9 flyover over Henday, 103485443 EN2-10
    flyover over the freeway; approaches; loops; the extra ramps and the two Henday carriageways were added to geometry.json from the
    OSM API on 2026-10-15);
  * heights: 2018 LiDAR.  Roads sit on embankment, so the road surface is the bare-earth crown (max DTM within 3 m of the centreline)
    sampled by `python -I site_h52.py --sample` (needs the gitignored .tif clips) into elevation/h52-samples.json, which build()
    reads; deck levels come from a robust straight-line fit to the first returns along each deck (lowered 0.12 m for vehicles);
  * inventory (Alberta file 75543): E-7 and W-8 type WG (welded girder), two spans; EN1-9 WG two spans; EN2-10 NU (concrete girder)
    two spans.  The prints 16.1 / 19.8 / 13.9 / 13.9 are read here as deck widths, 128.5 / 128.5 / 123.5 / 71.5 as total length, and
    65.5 / 65.5 / 63.0 / 36.5 as the longer span (so the second span is 63.0, 63.0, 60.5, 35.0);
  * girder depth follows from the published 5.3 m posted clearance over Henday (E-7, W-8, EN1-9) and 5.3 m assumed over the freeway
    for EN2-10: soffit = road under + 5.3 m + 0.1 m.
Assumed (flagged): the readings of the inventory prints above, pier on the median centre (west / first span the longer), girder
line counts, column sizes, steel girder colour (painted grey), ramp roadway widths (8.6 m one lane, 11.6 m two), approach widths
from the lane tags, 4:1 slopes, lamp positions.  Colour: asphalt, concrete, steel, grass slopes.
"""
import json, math, sys
from bridgelib import *
from t2lib import *

CODE, TITLE = "H52", "Sherwood Park Cloverleaf"
DATUM = 700.00
F = "H52-sherwood-park-cloverleaf"
LAT0, LON0 = 53.513, -113.344
SAMPLES = ROOT / "docs/edmonton-bridges/reference" / F / "elevation/h52-samples.json"
SLOPE = 4.0
STEP = 6.0
MAXAPP = 1000.0

# chains: name, ways in travel order, deck ways, far widths (start, end)
CHAINS = {
    "eb": dict(ways=[373938261, 995106404, 34572698, 373938269], far=(14.0, 14.5), inner=True),
    "wb": dict(ways=[32834429, 232709695, 995106405, 505630336], far=(14.5, 14.5), inner=True),
    "fly": dict(ways=[496863878, 430222935, 103485448, 103485449, 103485443, 103485442, 1261356104, 496863877], far=(11.6, 11.6)),
}
RAMPS = [("sw_loop", [1262002013, 1286998212, 32834242], 8.6), ("nw_loop", [38001208], 8.6), ("n_out", [103485440], 8.6),
         ("ne_loop", [103485444], 8.6), ("s_in", [333132008], 8.6), ("s_wye", [103485445], 8.6), ("s_wb", [103485446], 8.6)]
# deck: chain, way, width, lanes, girder lines, girder colour (None = default), column radius, spans (first, second), under axes
DECKS = [
    dict(name="E7", chain="eb", way=34572698, wd=16.1, lanes=3, n=6, gsw=None, r=0.7, spans=(65.5, 63.0), under=("henday_n", "henday_s")),
    dict(name="W8", chain="wb", way=232709695, wd=19.8, lanes=4, n=7, gsw=None, r=0.7, spans=(65.5, 63.0), under=("henday_n", "henday_s")),
    dict(name="EN1", chain="fly", way=103485448, wd=13.9, lanes=2, n=5, gsw=None, r=0.65, spans=(63.0, 60.5), under=("henday_n", "henday_s")),
    dict(name="EN2", chain="fly", way=103485443, wd=13.9, lanes=2, n=5, gsw="CONCD", dmax=2.1, r=0.6, spans=(36.5, 35.0), under=("eb", "wb")),
]
HENDAY = {"henday_n": 245395446, "henday_s": 430222934}


def chain(fr, ways):
    nodes, marks, cum = [], {}, 0.0
    for w in ways:
        pts = find_way(F, w)
        if nodes:
            assert math.hypot(*[a - b for a, b in zip(fr.en(*pts[0]), fr.en(*nodes[-1]))]) < 0.5, ("chain break", w)
        nodes += pts if not nodes else pts[1:]
        marks[w] = cum
        cum += fr.axis(pts).L
    return fr.axis(nodes), marks


def _roads(fr):
    roads = {}
    for name, c in CHAINS.items():
        ax, marks = chain(fr, c["ways"])
        roads[name] = dict(ax=ax, marks=marks, chain=True, far=c["far"], inner=c.get("inner", False))
    for name, ways, w in RAMPS:
        ax, marks = chain(fr, ways)
        roads[name] = dict(ax=ax, marks=marks, ramp=True, w=w)
    for k, w in HENDAY.items():
        roads[k] = dict(ax=fr.axis(find_way(F, w)), under=True)
    return roads


def _cross(dax, other, step=0.5):
    """Station on dax closest to the polyline `other`."""
    op = [other.en(s, 0) for s in other.stations(0, other.L, 1.0)]
    best = (1e9, 0.0)
    for s in dax.stations(0, dax.L, step):
        e, n = dax.en(s, 0)
        d = min((e - a) ** 2 + (n - b) ** 2 for a, b in op)
        if d < best[0]:
            best = (d, s)
    return best[1], math.sqrt(best[0])


def layout(fr, roads):
    """Pier / abutment stations (along each chain) for every deck."""
    out = {}
    for d in DECKS:
        r = roads[d["chain"]]
        dax = fr.axis(find_way(F, d["way"]))
        base = r["marks"][d["way"]]
        cs = [_cross(dax, roads[u]["ax"]) for u in d["under"]]
        assert all(c[1] < 6 for c in cs), (d["name"], cs)
        sp = sum(c[0] for c in cs) / len(cs)
        a0, a1 = sp - d["spans"][0], sp + d["spans"][1]
        out[d["name"]] = dict(base=base, L=dax.L, sp=sp, cross=[c[0] for c in cs], a0=base + a0, a1=base + a1, pier=base + sp,
                              s0=a0, s1=a1)
    return out


def sample():
    """Write h52-samples.json: DTM crown and side ground along every axis every STEP m (heights above DATUM), DSM along the chains,
    Henday pavement and ground at every pier."""
    from lidar_pil import Grid
    base = ROOT / "docs/edmonton-bridges/reference" / F / "elevation"
    dtm, dsm = Grid(base / "dtm-2018-1m.tif"), Grid(base / "dsm-2018-1m.tif")
    fr = Frame(LAT0, LON0)

    def at(g, e, n):
        return g.at(*fr.ll(e, n))
    out = {}
    roads = _roads(fr)
    for name, r in roads.items():
        ax = r["ax"]
        w = r["w"] if r.get("ramp") else 12.0
        ss = [min(ax.L, i * STEP) for i in range(int(ax.L / STEP) + 2)]
        rec = dict(ss=ss, crown=[], gl=[], gr=[])
        for s in ss:
            v = [x for x in (at(dtm, *ax.en(s, t)) for t in (-3, -1.5, 0, 1.5, 3)) if x == x]
            rec["crown"].append(round(max(v) - DATUM, 3) if v else None)
            for key, sg in (("gl", 1), ("gr", -1)):
                v = [x for x in (at(dtm, *ax.en(s, sg * (w / 2 + d))) for d in (10, 14, 18, 22, 26, 30)) if x == x]
                rec[key].append(round(min(v) - DATUM, 3) if v else None)
        if r.get("chain"):
            rec["dsm"] = [round(at(dsm, *ax.en(s, 0)) - DATUM, 3) for s in ss]
        out[name] = rec
    lay = layout(fr, roads)
    br = {}
    for d in DECKS:
        L = lay[d["name"]]
        ax = roads[d["chain"]]["ax"]
        cols = _cols(d)
        e0, n0 = ax.en(L["pier"], 0)
        foot = [x for x in (at(dtm, *ax.en(L["pier"], t)) for t in cols) if x == x]
        rec = dict(pier_ground=round(min(foot) - DATUM, 3) if foot else None)
        if d["under"][0].startswith("henday"):
            pv = []
            for u, cs in zip(d["under"], L["cross"]):
                dax = fr.axis(find_way(F, d["way"]))
                e, n = dax.en(cs, 0)
                v = sorted(x for x in (at(dtm, e + a, n + b) for a in (-3, 0, 3) for b in (-3, 0, 3)) if x == x)
                pv.append(round(v[len(v) // 2] - DATUM, 3))
            rec["under_road"] = pv
        br[d["name"]] = rec
    out["bridges"] = br
    SAMPLES.write_text(json.dumps(out), encoding="utf-8")
    print("wrote", SAMPLES)


def _cols(d):
    k = 4 if d["wd"] < 17 else 5
    sp = (d["wd"] - 4.4) / (k - 1)
    return [-(d["wd"] - 4.4) / 2 + i * sp for i in range(k)]


def _fill(v):
    v = list(v)
    last = None
    for i, x in enumerate(v):
        if x is None or x != x:
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
    n = len(v)
    return [sum(v[max(0, i - k):i + k + 1]) / len(v[max(0, i - k):i + k + 1]) for i in range(n)]


def road_fill(m, ax, s0, s1, y_fn, w_fn, gl, gr, fade=(0.0, 0.0), lines=False, taper=(False, False), inner=None):
    """Raised road on a 4:1 embankment: asphalt top, grass slopes down to the side ground.  Where the fill is lower than 0.8 m the
    road sinks into the ground (it vanishes below the terrain), and it does the same over the `fade` lengths at open ends.
    inner = (sign, gap_fn): on that side the slope is cut short at half the gap to the parallel carriageway and closed with a vertical
    grass skirt, so the two embankments do not run through each other."""
    rows = []
    for s in ax.stations(s0, s1, STEP):
        w, yv = w_fn(s), y_fn(s)
        h = ((yv - gl(s)) + (yv - gr(s))) / 2 + 0.3
        sink = 0.9 * max(0.0, min(1.0, (1.0 - h) / 0.8))
        if fade[0] and s - s0 < fade[0]:
            sink = max(sink, 3.0 * (1 - (s - s0) / fade[0]))
        if fade[1] and s1 - s < fade[1]:
            sink = max(sink, 3.0 * (1 - (s1 - s) / fade[1]))
        yd = yv - sink
        f = 1.0
        if taper[0]:
            f = min(f, (s - s0) / 12.0)
        if taper[1]:
            f = min(f, (s1 - s) / 12.0)
        rows.append(dict(s=s, w=w, y=yd, hl=max(0.25, yd - gl(s) + 0.3), hr=max(0.25, yd - gr(s) + 0.3), sink=sink, h=h, f=f))
    for r in rows:
        for sg, key in ((1, "hl"), (-1, "hr")):
            wd = SLOPE * r[key] * r["f"]
            r["sw" + key] = wd
            if inner and inner[0] == sg:
                lim = max(0.3, inner[1](r["s"]) / 2 - 0.15)
                r["sw" + key] = min(wd, lim)
    for a, b in zip(rows[:-1], rows[1:]):
        if max(a["h"], b["h"]) < 0.0:
            continue
        c = ax.p3((a["s"] + b["s"]) / 2, 0, (a["y"] + b["y"]) / 2 - 6)
        m.poly([ax.p3(a["s"], -a["w"] / 2, a["y"]), ax.p3(b["s"], -b["w"] / 2, b["y"]), ax.p3(b["s"], b["w"] / 2, b["y"]),
                ax.p3(a["s"], a["w"] / 2, a["y"])], ASPHALT, c)
        for sg, key in ((1, "hl"), (-1, "hr")):
            wa, wb = a["sw" + key], b["sw" + key]
            ya, yb = a["y"] - min(a[key], wa / SLOPE), b["y"] - min(b[key], wb / SLOPE)
            m.poly([ax.p3(a["s"], sg * a["w"] / 2, a["y"]), ax.p3(b["s"], sg * b["w"] / 2, b["y"]),
                    ax.p3(b["s"], sg * (b["w"] / 2 + wb), yb), ax.p3(a["s"], sg * (a["w"] / 2 + wa), ya)], GRASS, c)
            if ya > a["y"] - a[key] + 0.01 or yb > b["y"] - b[key] + 0.01:       # skirt under a shortened slope
                m.poly([ax.p3(a["s"], sg * (a["w"] / 2 + wa), ya), ax.p3(b["s"], sg * (b["w"] / 2 + wb), yb),
                        ax.p3(b["s"], sg * (b["w"] / 2 + wb), b["y"] - b[key]), ax.p3(a["s"], sg * (a["w"] / 2 + wa), a["y"] - a[key])],
                       GRASS, c)
        if lines and a["sink"] == 0.0 and b["sink"] == 0.0:
            for sg, sw in ((1, YELLOWR), (-1, WHITE)):
                ta, tb = sg * (a["w"] / 2 - 0.45), sg * (b["w"] / 2 - 0.45)
                m.poly([ax.p3(a["s"], ta - 0.08, a["y"] + 0.02), ax.p3(b["s"], tb - 0.08, b["y"] + 0.02),
                        ax.p3(b["s"], tb + 0.08, b["y"] + 0.02), ax.p3(a["s"], ta + 0.08, a["y"] + 0.02)], sw, c)


def _fit(pts, tol=0.4):
    """Robust straight line (s, y): least squares, then drop points further than tol and refit (3 passes)."""
    for _ in range(4):
        n = len(pts)
        ms, mv = sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n
        k = sum((p[0] - ms) * (p[1] - mv) for p in pts) / (sum((p[0] - ms) ** 2 for p in pts) or 1)
        keep = [p for p in pts if abs(p[1] - (mv + k * (p[0] - ms))) <= tol]
        if len(keep) < 8:
            break
        pts = keep
    return ms, mv, k


def _near_d(ax, other, s):
    e, n = ax.en(s, 0)
    return min(math.hypot(e - a, n - b) for a, b in other)


def build():
    fr = Frame(LAT0, LON0)
    smp = json.loads(SAMPLES.read_text(encoding="utf-8"))
    roads = _roads(fr)
    lay = layout(fr, roads)
    m = BMesh()
    decks = {d["name"]: d for d in DECKS}
    info = {}
    # first pass: profiles, deck fits, widths
    for name, r in roads.items():
        if r.get("under"):
            continue
        sp, ax = smp[name], r["ax"]
        ss = sp["ss"]
        crown = _smooth(sp["crown"], 1)
        r["gl"] = profile(list(zip(ss, _smooth(sp["gl"], 2))))
        r["gr"] = profile(list(zip(ss, _smooth(sp["gr"], 2))))
        if r.get("inner"):                       # the inner (left) side faces the other carriageway: use the outer ground for both
            r["gl"] = r["gr"]
        if r.get("ramp"):
            r["y"] = profile([(s, c - 0.1) for s, c in zip(ss, crown)])
            r["ok"] = (min(s for s, c in zip(ss, sp["crown"]) if c is not None), max(s for s, c in zip(ss, sp["crown"]) if c is not None))
            continue
        brs = [decks[k] for k in decks if decks[k]["chain"] == name]
        pins = []
        for d in sorted(brs, key=lambda d: lay[d["name"]]["a0"]):
            L = lay[d["name"]]
            base, a0, a1 = L["base"], L["a0"], L["a1"]
            dax_L = L["L"]
            pts = [(s - base, v) for s, v in zip(ss, sp["dsm"]) if base + 4 < s < base + dax_L - 4]
            ms, mv, k = _fit(pts)
            d["ydeck"] = (lambda s, ms=ms, mv=mv, k=k: mv + k * (s - ms) - 0.12)      # s along the deck way
            L["y0"], L["y1"] = d["ydeck"](L["s0"]), d["ydeck"](L["s1"])
            pins += [(a0, a1, L)]
        # bare earth under the deck ends is not the road: within 25 m of an abutment, where the first return is well above it, use it
        near = lambda q: min([min(abs(q - L["a0"]), abs(q - L["a1"])) for _, _, L in pins] or [1e9])
        crown = [ds - 0.12 if (ds - c > 0.4 and near(q) < 25) else c for q, c, ds in zip(ss, crown, sp["dsm"])]
        yap = profile([(s, c - 0.1) for s, c in zip(ss, crown)])
        corr = []
        for a0, a1, L in pins:
            corr += [(a0, L["y0"] - yap(a0)), (a1, L["y1"] - yap(a1))]
        r["yap"], r["corr"] = yap, corr

        def y_all(s, yap=yap, corr=corr):
            if s <= corr[0][0]:
                return yap(s) + corr[0][1] * max(0.0, 1 - (corr[0][0] - s) / 90.0)
            if s >= corr[-1][0]:
                return yap(s) + corr[-1][1] * max(0.0, 1 - (s - corr[-1][0]) / 90.0)
            for (sa, ca), (sb, cb) in zip(corr[:-1], corr[1:]):
                if s <= sb:
                    return yap(s) + ca + (cb - ca) * (s - sa) / ((sb - sa) or 1.0)
        r["y"] = y_all

        def w0(s, r=r, pins=pins, brs=brs):
            ds = min([max(L["a0"] - s, s - L["a1"], 0.0) for _, _, L in pins])
            wd = brs[0]["wd"]
            far = r["far"][0] if s < pins[0][2]["a0"] else r["far"][1]
            return wd + (far - wd) * min(1.0, ds / 60.0)
        r["w0"] = w0
    # widths limited by the parallel carriageway, and the gap between them
    ptsd = {k: [roads[k]["ax"].en(s, 0) for s in roads[k]["ax"].stations(0, roads[k]["ax"].L, 2.0)] for k in ("eb", "wb")}
    for a, b in (("eb", "wb"), ("wb", "eb")):
        ra, rb = roads[a], roads[b]

        def hw(s, ra=ra, rb=rb, b=b):
            d = _near_d(ra["ax"], ptsd[b], s)
            e, n = ra["ax"].en(s, 0)
            sb = min(rb["ax"].stations(0, rb["ax"].L, 2.0), key=lambda q: (rb["ax"].en(q, 0)[0] - e) ** 2 + (rb["ax"].en(q, 0)[1] - n) ** 2)
            wa, wb = ra["w0"](s), rb["w0"](sb)
            ha = min(wa / 2, (d - 0.6) * wa / (wa + wb))
            hb = min(wb / 2, (d - 0.6) * wb / (wa + wb))
            return ha, hb, d
        ra["hw"] = hw
    for a in ("eb", "wb"):
        ra = roads[a]
        ra["w"] = lambda s, ra=ra: 2 * ra["hw"](s)[0]
        ra["gap"] = lambda s, ra=ra: ra["hw"](s)[2] - ra["hw"](s)[0] - ra["hw"](s)[1]
    for name in ("fly",):
        roads[name]["w"] = roads[name]["w0"]
    # roads
    for name, r in roads.items():
        if r.get("under"):
            continue
        ax = r["ax"]
        if r.get("ramp"):
            lo, hi = r["ok"]
            w = r["w"]
            road_fill(m, ax, lo, hi, r["y"], lambda s, w=w: w, r["gl"], r["gr"], fade=(40.0 if lo > 1 else 0.0, 40.0 if hi < ax.L - 7 else 0.0), lines=True)
            continue
        inn = (1, r["gap"]) if r.get("inner") else None
        ds = sorted([decks[k] for k in decks if decks[k]["chain"] == name], key=lambda d: lay[d["name"]]["a0"])
        segs = []
        first, last = lay[ds[0]["name"]], lay[ds[-1]["name"]]
        segs.append((max(0.0, first["a0"] - MAXAPP), first["a0"], (120.0, 0.0), (False, True)))
        for p, q in zip(ds[:-1], ds[1:]):
            segs.append((lay[p["name"]]["a1"], lay[q["name"]]["a0"], (0.0, 0.0), (True, True)))
        segs.append((last["a1"], min(ax.L, last["a1"] + MAXAPP), (0.0, 120.0), (True, False)))
        for s0, s1, fd, tp in segs:
            if s1 - s0 > 1.0:
                road_fill(m, ax, s0, s1, r["y"], r["w"], r["gl"], r["gr"], fade=fd, taper=tp, inner=inn, lines=True)
    # decks
    rep = []
    for d in DECKS:
        r = roads[d["chain"]]
        ax, L = r["ax"], lay[d["name"]]
        sub = Axis([ax.en(s, 0) for s in ax.stations(L["a0"], L["a1"], 0)])
        yl = lambda s, d=d, L=L: d["ydeck"](s + L["s0"])
        sm = smp["bridges"][d["name"]]
        slab = 0.32
        if "under_road" in sm:
            under_y = max(sm["under_road"])
        else:
            ys = []
            for u, cs in zip(d["under"], L["cross"]):
                dax = fr.axis(find_way(F, d["way"]))
                e, n = dax.en(cs, 0)
                uax = roads[u]["ax"]
                su = min(uax.stations(0, uax.L, 1.0), key=lambda q: (uax.en(q, 0)[0] - e) ** 2 + (uax.en(q, 0)[1] - n) ** 2)
                ys.append(roads[u]["y"](su))
            under_y = max(ys)
        top = yl(L["sp"] - L["s0"])
        depth = min(d.get("dmax", 3.4), max(1.4, top - slab - (under_y + 5.3 + 0.1)))
        # ground under the deck ends for the abutments
        g0 = lambda s, r=r, L=L: r["yap"](L["a0"] if s < sub.L / 2 else L["a1"]) - 0.1
        girder_deck(m, sub, 0.0, sub.L, yl, -d["wd"] / 2, d["wd"] / 2, g0, n_girders=d["n"], depth=depth, slab=slab, inner=+1, sidewalk=0,
                    left_sign=+1, carriage=d["lanes"] * 3.65 + 0.6, lanes=d["lanes"], lamp_step=36.0,
                    girder_sw=globals()[d["gsw"]] if d["gsw"] else None)
        q = L["sp"] - L["s0"]
        ys = yl(q) - slab - depth - 0.15
        gy = (sm["pier_ground"] if sm["pier_ground"] is not None else under_y) - 0.4
        cols = _cols(d)
        for t in cols:
            e, nn = sub.en(q, t)
            cyl(m, e, nn, d["r"], d["r"], gy, ys - 0.9, CONC, n=12)
        prism(m, nose_plan(sub, q, 0.0, 1.0, max(cols) + 1.2, 0.0, (False, False)), ys - 0.9, ys, CONCD)
        rep.append((d["name"], round(L["s0"], 1), round(L["s1"], 1), round(sub.L, 1), round(depth, 2), round(under_y + DATUM, 2),
                    round(yl(q) + DATUM, 2), round(L["L"], 1)))
    print("decks (name, abut0, abut1, length, girder depth, road under, deck top, osm way length):")
    for x in rep:
        print("  ", x)
    return dict(code=CODE, title=TITLE, lat0=LAT0, lon0=LON0, alt=DATUM, parts=[("br_h52_sherwood_park", m)], frame=fr,
                views=[("a", 205.0, 35.0), ("b", 120.0, 30.0), ("c", 20.0, 60.0)], preview=dict(span=1500.0, water=False))


if __name__ == "__main__":
    if "--sample" in sys.argv:
        sample()
