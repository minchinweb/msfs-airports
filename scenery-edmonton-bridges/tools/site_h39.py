"""H39 Henday / Yellowhead west (Anthony Henday Drive over Yellowhead Trail, Edmonton): ten decks, two Henday carriageways, the
directional ramps and flyovers.

Sourced (docs/edmonton-bridges/reference/H39-henday-yellowhead-west NOTES.md, HANDOFF-T2.md):
  * plan: OSM ways (decks 22916287 N-1, 22916290 S-6, 273639882 NW-7, 135719193 SE-8, 153725899 WS1-9, 43402325 WS2-10, 43402275
    WS3-11, 132571388 EN1-12, 43531503 EN2-13, 43531474 EN3-14; the ramp chains and the Yellowhead carriageways were added to
    geometry.json from the OSM API on 2026-10-15);
  * heights: 2018 LiDAR.  Roads sit on embankment, so the road surface is the bare-earth crown (max DTM within 3 m of the centreline)
    sampled by `python -I site_h39.py --sample` (needs the gitignored .tif clips) into elevation/h39-samples.json, which build()
    reads; deck levels are a robust quadratic fit to the first returns along each deck, lowered 0.12 m for vehicles and rails;
  * Alberta file 85047 inspections: spans (N-1 44 + 40 m, S-6 46.025 + 45.053, NW-7 46.038 + 45.084, SE-8 45.088 + 46.04, WS1-9 58.488,
    WS2-10 45.354 + 37.075 + 42.221, WS3-11 63.954 + 42.751, EN1-12 40.537, EN2-13 44.054 + 36.914 + 30.049, EN3-14 45.945 + 38.468),
    clear roadway (16.6, 17.1, 8.3, 8.3, 13.9 ...), pier columns (4, 3, 1, 1, none, 2 + 2, 2, none, 2 + 2, 2), girder type (WG
    weathering steel; NU concrete on WS2-10, EN2-13, EN3-14, five lines);
  * girder depth follows from the published clearances (5.5 to 5.8 m over Yellowhead, 9 to 9.9 m over Henday): soffit = road under +
    clearance, capped by a span-based depth.
Assumed (flagged): where the structure sits inside the OSM line (spans centred on the mean of the crossings with the road underneath,
middle span of the three-span decks centred), girder counts of the WG decks, column sizes and cap beams, ramp roadway width 8.6 m,
approach widths, 4:1 slopes, lamps.  Colour: asphalt, concrete, rust (weathering steel), grass slopes.
"""
import json, math, sys
import numpy as np
from bridgelib import *
from t2lib import *

CODE, TITLE = "H39", "Henday / Yellowhead west"
DATUM = 680.00
F = "H39-henday-yellowhead-west"
LAT0, LON0 = 53.574, -113.662
SAMPLES = ROOT / "docs/edmonton-bridges/reference" / F / "elevation/h39-samples.json"
SLOPE = 4.0
STEP = 6.0
LAST = None
MAXAPP = 600.0
RAMP_W = 8.6
MAIN_W = 14.5

# chains: ways in travel order; kind main = Henday carriageway (inner side faces the other), ramp = single carriageway
CHAINS = {
    "hnb": dict(ways=[279661277, 22916287, 601916867], far=MAIN_W, inner=True),
    "hsb": dict(ways=[1025356482, 198515213, 22916290, 847002330, 22916292, 847002329], far=MAIN_W, inner=True),
    "nw": dict(ways=[499079876, 1285934488, 43072628, 273639882, 153725851], far=RAMP_W),
    "se": dict(ways=[135927518, 1286221278, 499078195, 135719193, 135719192], far=RAMP_W),
    "ws": dict(ways=[499789126, 1286248798, 153725852, 153725899, 153725850, 43402325, 153725854, 43402275, 153725855, 641722671, 847002313],
               far=RAMP_W),
    "en": dict(ways=[132978477, 132571388, 153725888, 43531503, 43531499, 43531474, 153725874], far=RAMP_W),
    "ne_e": dict(ways=[22911977], far=RAMP_W),
    "ne_n": dict(ways=[256516540], far=RAMP_W),
    "w_s": dict(ways=[431012835], far=RAMP_W),
    "sb_w": dict(ways=[135719195], far=RAMP_W),
}
# Yellowhead carriageways (not drawn; the road under the Henday decks): eastbound, westbound
YH = {"yh_e": [60064623, 256516539], "yh_w": [1287655151, 313692014, 279472325, 61423533]}
UNDER = dict(YH)
UNDER.update({"hnb": CHAINS["hnb"]["ways"], "hsb": CHAINS["hsb"]["ways"], "ws_ramp": [153725855], "en_ramp": [153725874],
              "se": CHAINS["se"]["ways"], "nw": CHAINS["nw"]["ways"]})
# deck: chain, way, clear width, lanes, girder lines, girder colour, spans, column offsets (per pier line), column radius, under groups,
#       clearance over the road under (m), max girder depth
DECKS = [
    dict(name="N1", chain="hnb", way=22916287, wd=16.6, lanes=3, n=6, gsw="RUST", spans=(44.0, 40.0), cols=[-5.4, -1.8, 1.8, 5.4], r=0.5,
         under=("yh_e", "yh_w"), clr=5.8, dmax=2.1, lamps=36.0),
    dict(name="S6", chain="hsb", way=22916290, wd=17.1, lanes=3, n=6, gsw="RUST", spans=(46.025, 45.053), cols=[-5.2, 0.0, 5.2], r=0.55,
         under=("yh_e", "yh_w"), clr=5.8, dmax=2.2, lamps=36.0),
    dict(name="NW7", chain="nw", way=273639882, wd=8.3, lanes=1, n=4, gsw="RUST", spans=(46.038, 45.084), cols=[0.0], r=1.0,
         under=("yh_e", "yh_w"), clr=5.5, dmax=2.2, lamps=0.0),
    dict(name="SE8", chain="se", way=135719193, wd=8.3, lanes=1, n=4, gsw="RUST", spans=(45.088, 46.04), cols=[0.0], r=1.0,
         under=("yh_e", "yh_w"), clr=5.6, dmax=2.2, lamps=0.0),
    dict(name="WS1", chain="ws", way=153725899, wd=13.9, lanes=1, n=5, gsw="RUST", spans=(58.488,), cols=[], r=0.6,
         under=("en_ramp",), clr=5.5, dmax=2.6, lamps=0.0),
    dict(name="WS2", chain="ws", way=43402325, wd=13.9, lanes=1, n=5, gsw="CONCD", spans=(45.354, 37.075, 42.221), cols=[-3.4, 3.4], r=0.6,
         under=("hnb", "hsb", "se"), clr=9.0, dmax=1.95, lamps=0.0),
    dict(name="WS3", chain="ws", way=43402275, wd=13.9, lanes=1, n=5, gsw="RUST", spans=(63.954, 42.751), cols=[-3.4, 3.4], r=0.6,
         under=("yh_e", "yh_w"), clr=5.6, dmax=2.9, lamps=0.0),
    dict(name="EN1", chain="en", way=132571388, wd=13.9, lanes=1, n=5, gsw="RUST", spans=(40.537,), cols=[], r=0.6,
         under=("ws_ramp",), clr=5.5, dmax=2.3, lamps=0.0),
    dict(name="EN2", chain="en", way=43531503, wd=13.9, lanes=1, n=5, gsw="CONCD", spans=(44.054, 36.914, 30.049), cols=[-3.4, 3.4], r=0.6,
         under=("hsb", "hnb", "nw"), clr=7.7, dmax=1.95, lamps=0.0),
    dict(name="EN3", chain="en", way=43531474, wd=13.9, lanes=1, n=5, gsw="CONCD", spans=(45.945, 38.468), cols=[-3.4, 3.4], r=0.6,
         under=("yh_e", "yh_w"), clr=5.7, dmax=1.95, lamps=0.0),
]


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
        roads[name] = dict(ax=ax, marks=marks, far=c["far"], inner=c.get("inner", False), main=c["far"] == MAIN_W)
    return roads


def _dense(fr, ways, step=1.0):
    pts = []
    for w in ways:
        ax = fr.axis(find_way(F, w))
        pts += [ax.en(s, 0) for s in ax.stations(0, ax.L, step)]
    return np.array(pts)


def _cross(dax, dense, step=0.5):
    """Station on dax closest to the dense point set; (station, distance)."""
    ss = dax.stations(0, dax.L, step)
    P = np.array([dax.en(s, 0) for s in ss])
    d = np.sqrt(((P[:, None, :] - dense[None, ::2, :]) ** 2).sum(-1)).min(1)
    i = int(d.argmin())
    return ss[i], float(d[i])


def layout(fr, roads):
    """Abutment and pier stations along each deck way (s relative to the deck way start) and along its chain."""
    out = {}
    dense = {k: _dense(fr, v) for k, v in UNDER.items()}
    for d in DECKS:
        dax = fr.axis(find_way(F, d["way"]))
        cs = [_cross(dax, dense[u]) for u in d["under"]]
        assert all(c[1] < 8 for c in cs), (d["name"], cs)
        cs.sort()
        c = sum(x[0] for x in cs[:2]) / len(cs[:2])
        sp = d["spans"]
        if len(sp) == 1:
            a0, a1, piers = c - sp[0] / 2, c + sp[0] / 2, []
        elif len(sp) == 2:
            a0, a1, piers = c - sp[0], c + sp[1], [c]
        else:
            p1, p2 = c, c + sp[1]       # first pier in the median between the first two roads under, the rest follow the spans
            a0, a1, piers = p1 - sp[0], p2 + sp[2], [p1, p2]
        base = roads[d["chain"]]["marks"][d["way"]]
        out[d["name"]] = dict(base=base, L=dax.L, cross=[x[0] for x in cs], s0=a0, s1=a1, piers=piers, a0=base + a0, a1=base + a1)
    return out


def sample():
    """Write h39-samples.json: DTM crown and side ground along every axis every STEP m (heights above DATUM), DSM along the chains,
    pavement under each deck and ground at each pier."""
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
        w = 12.0 if r["main"] else RAMP_W
        ss = [min(ax.L, i * STEP) for i in range(int(ax.L / STEP) + 2)]
        rec = dict(ss=ss, crown=[], gl=[], gr=[])
        for s in ss:
            v = [x for x in (at(dtm, *ax.en(s, t)) for t in (-3, -1.5, 0, 1.5, 3)) if x == x]
            rec["crown"].append(round(max(v) - DATUM, 3) if v else None)
            for key, sg in (("gl", 1), ("gr", -1)):
                v = [x for x in (at(dtm, *ax.en(s, sg * (w / 2 + d))) for d in (10, 14, 18, 22, 26, 30)) if x == x]
                rec[key].append(round(min(v) - DATUM, 3) if v else None)
        dv = [at(dsm, *ax.en(s, 0)) for s in ss]
        rec["dsm"] = [round(v - DATUM, 3) if v == v else None for v in dv]
        out[name] = rec
    lay = layout(fr, roads)
    br = {}
    for d in DECKS:
        L = lay[d["name"]]
        ax = roads[d["chain"]]["ax"]
        dax = fr.axis(find_way(F, d["way"]))
        pg = []
        for q in L["piers"]:
            foot = [x for x in (at(dtm, *ax.en(L["base"] + q, t)) for t in d["cols"]) if x == x]
            pg.append(round(min(foot) - DATUM, 3) if foot else None)
        pv = []
        for cs in L["cross"]:
            e, n = dax.en(cs, 0)
            v = sorted(x for x in (at(dtm, e + a, n + b) for a in (-3, 0, 3) for b in (-3, 0, 3)) if x == x)
            pv.append(round(v[len(v) // 2] - DATUM, 3) if v else None)
        br[d["name"]] = dict(pier_ground=pg, under_road=pv)
    out["bridges"] = br
    SAMPLES.write_text(json.dumps(out), encoding="utf-8")
    print("wrote", SAMPLES)


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


def _fit2(pts, tol=0.4):
    """Robust quadratic (s, y): least squares, drop points further than tol, refit (4 passes).  Returns coefficients and the s mean."""
    ms = sum(p[0] for p in pts) / len(pts)
    pts = [(p[0] - ms, p[1]) for p in pts]
    co = None
    for _ in range(5):
        x = np.array([p[0] for p in pts])
        y = np.array([p[1] for p in pts])
        co = np.polyfit(x, y, 2)
        keep = [p for p in pts if abs(p[1] - np.polyval(co, p[0])) <= tol]
        if len(keep) < 8 or len(keep) == len(pts):
            break
        pts = keep
    return co, ms


def road_fill(m, ax, s0, s1, y_fn, w_fn, gl, gr, fade=(0.0, 0.0), taper=(False, False), clip=None):
    """Raised road on a 4:1 embankment: asphalt top, grass slopes down to the side ground.  Where the fill is lower than 0.8 m the
    road sinks into the ground (it vanishes below the terrain), and it does the same over the `fade` lengths at open ends.
    clip(s, sign) = the largest slope width allowed on that side (a similar-level road alongside): the slope is cut short there and
    closed with a vertical grass skirt, so two embankments do not run through each other."""
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
            if clip:
                wd = min(wd, max(0.3, clip(r["s"], sg, r["w"])))
            r["sw" + key] = wd
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
        if a["sink"] == 0.0 and b["sink"] == 0.0:
            for sg, sw in ((1, YELLOWR), (-1, WHITE)):
                ta, tb = sg * (a["w"] / 2 - 0.45), sg * (b["w"] / 2 - 0.45)
                m.poly([ax.p3(a["s"], ta - 0.08, a["y"] + 0.02), ax.p3(b["s"], tb - 0.08, b["y"] + 0.02),
                        ax.p3(b["s"], tb + 0.08, b["y"] + 0.02), ax.p3(a["s"], ta + 0.08, a["y"] + 0.02)], sw, c)


def build():
    fr = Frame(LAT0, LON0)
    smp = json.loads(SAMPLES.read_text(encoding="utf-8"))
    roads = _roads(fr)
    lay = layout(fr, roads)
    m = BMesh()
    decks = {d["name"]: d for d in DECKS}
    # first pass: profiles, deck fits, widths
    for name, r in roads.items():
        sp, ax = smp[name], r["ax"]
        ss = sp["ss"]
        crown = _smooth(sp["crown"], 1)
        r["gl"] = profile(list(zip(ss, _smooth(sp["gl"], 2))))
        r["gr"] = profile(list(zip(ss, _smooth(sp["gr"], 2))))
        ok = [s for s, c in zip(ss, sp["crown"]) if c is not None]       # no LiDAR beyond the clip: end the road there
        r["ok"] = (min(ok), max(ok))
        brs = sorted([d for d in DECKS if d["chain"] == name], key=lambda d: lay[d["name"]]["a0"])
        r["brs"] = brs
        if not brs:
            r["y"] = profile([(s, c - 0.1) for s, c in zip(ss, crown)])
            r["w0"] = lambda s, r=r: r["far"]
            continue
        pins = []
        for d in brs:
            L = lay[d["name"]]
            base = L["base"]
            pts = [(s - base, v) for s, v in zip(ss, sp["dsm"]) if v is not None and base + 4 < s < base + L["L"] - 4]
            co, ms = _fit2(pts)
            d["ydeck"] = (lambda s, co=co, ms=ms: float(np.polyval(co, s - ms)) - 0.12)      # s along the deck way
            L["y0"], L["y1"] = d["ydeck"](L["s0"]), d["ydeck"](L["s1"])
            pins.append(L)
        near = lambda q: min([min(abs(q - L["a0"]), abs(q - L["a1"])) for L in pins])
        # bare earth under the deck ends is not the road: within 25 m of an abutment, where the first return is well above it, use it
        crown = [(ds - 0.12) if (ds is not None and c is not None and ds - c > 0.4 and near(q) < 25) else c
                 for q, c, ds in zip(ss, crown, sp["dsm"])]
        yap = profile([(s, c - 0.1) for s, c in zip(ss, _fill(crown))])
        corr = []
        for L in pins:
            corr += [(L["a0"], L["y0"] - yap(L["a0"])), (L["a1"], L["y1"] - yap(L["a1"]))]
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
            best = r["far"]
            for d, L in zip(brs, pins):
                ds = max(L["a0"] - s, s - L["a1"], 0.0)
                best = max(best, r["far"] + (d["wd"] - r["far"]) * (1.0 - min(1.0, ds / 60.0)))
            return best
        r["w0"] = w0
    global LAST
    LAST = (roads, lay)
    # drawn ranges per road
    for name, r in roads.items():
        ax = r["ax"]
        lo, hi = r["ok"]
        brs = r["brs"]
        fl = (40.0 if lo > 1 else 0.0, 40.0 if hi < ax.L - 7 else 0.0)
        if not brs:
            if r["main"]:
                raise AssertionError("main road without a deck")
            r["segs"] = [(lo, hi, fl, (False, False))]
            continue
        segs = []
        first, last = lay[brs[0]["name"]], lay[brs[-1]["name"]]
        mx = MAXAPP if r["main"] else 1e9
        s0 = max(lo, first["a0"] - mx)
        segs.append((s0, first["a0"], (120.0 if (r["main"] and s0 > lo + 1) else fl[0], 0.0), (False, True)))
        for p, q in zip(brs[:-1], brs[1:]):
            segs.append((lay[p["name"]]["a1"], lay[q["name"]]["a0"], (0.0, 0.0), (True, True)))
        s1 = min(hi, last["a1"] + mx)
        segs.append((last["a1"], s1, (0.0, 120.0 if (r["main"] and s1 < hi - 1) else fl[1]), (True, False)))
        r["segs"] = [x for x in segs if x[1] - x[0] > 1.0]
    # neighbour table: points of every drawn road at 3 m, with the level and half width there
    P = []
    for name, r in roads.items():
        ax = r["ax"]
        for s0, s1, _f, _t in r["segs"]:
            for s in ax.stations(s0, s1, 3.0):
                e, n = ax.en(s, 0)
                P.append((e, n, r["y"](s), r["w0"](s) / 2, hash(name) % 100003))
    for name, r in roads.items():
        r["id"] = hash(name) % 100003
    P = np.array(P)

    def make_clip(r):
        ax, myid, y_fn, w_fn = r["ax"], r["id"], r["y"], r["w0"]
        oth = P[P[:, 4] != myid]
        cache = {}

        def clip(s, sg, w):
            key = round(s, 3)
            if key not in cache:
                e, n, de, dn = ax.at(s)
                yv = y_fn(s)
                dx, dy = oth[:, 0] - e, oth[:, 1] - n
                d = np.hypot(dx, dy)
                near = (d < 60.0) & (np.abs(oth[:, 2] - yv) < 3.0)
                lat = -dn * dx + de * dy                         # offset to the left of travel
                cache[key] = []
                for sgn in (1, -1):
                    side = near & (lat * sgn > 0.2 * d)
                    if side.any():
                        gap = (np.abs(lat[side]) - oth[side, 3] - w / 2).min()
                        cache[key].append(max(0.3, gap / 2 - 0.15))
                    else:
                        cache[key].append(1e9)
            return cache[key][0 if sg > 0 else 1]
        return clip
    for name, r in roads.items():
        ax = r["ax"]
        clip = make_clip(r)
        for s0, s1, fd, tp in r["segs"]:
            road_fill(m, ax, s0, s1, r["y"], r["w0"], r["gl"], r["gr"], fade=fd, taper=tp, clip=clip)
    # decks
    rep = []
    for d in DECKS:
        r = roads[d["chain"]]
        ax, L = r["ax"], lay[d["name"]]
        sub = Axis([ax.en(s, 0) for s in ax.stations(L["a0"], L["a1"], 0)])
        yl = lambda s, d=d, L=L: d["ydeck"](s + L["s0"])
        sm = smp["bridges"][d["name"]]
        slab = 0.32
        under_y = max(v for v in sm["under_road"] if v is not None)
        top = yl((L["piers"][0] if L["piers"] else (L["s0"] + L["s1"]) / 2) - L["s0"])
        depth = min(d["dmax"], max(1.2, top - slab - (under_y + d["clr"] + 0.1)))
        g0 = lambda s, r=r, L=L, sub=sub: r["yap"](L["a0"] if s < sub.L / 2 else L["a1"]) - 0.1
        girder_deck(m, sub, 0.0, sub.L, yl, -d["wd"] / 2, d["wd"] / 2, g0, n_girders=d["n"], depth=depth, slab=slab,
                    inner=+1 if r["inner"] else 0, sidewalk=0, left_sign=+1, carriage=d["wd"] - 0.9, lanes=d["lanes"], lamp_step=d["lamps"],
                    girder_sw=globals()[d["gsw"]])
        for q, pg in zip(L["piers"], sm["pier_ground"]):
            qq = q - L["s0"]
            ys = yl(qq) - slab - depth - 0.15
            gy = (pg if pg is not None else under_y) - 0.4
            for t in d["cols"]:
                e, nn = sub.en(qq, t)
                cyl(m, e, nn, d["r"], d["r"], gy, ys - 0.9, CONC, n=12)
            half_t = (max(d["cols"]) + 1.2) if len(d["cols"]) > 1 else d["wd"] / 2 - 1.5
            prism(m, nose_plan(sub, qq, 0.0, 0.9 if len(d["cols"]) > 1 else 1.3, half_t, 0.0, (False, False)), ys - 0.9, ys, CONCD)
        rep.append((d["name"], round(L["s0"], 1), round(L["s1"], 1), round(sub.L, 1), round(depth, 2), round(under_y + DATUM, 2),
                    round(top + DATUM, 2), round(L["L"], 1)))
    print("decks (name, abut0, abut1, length, girder depth, road under, deck top, osm way length):")
    for x in rep:
        print("  ", x)
    return dict(code=CODE, title=TITLE, lat0=LAT0, lon0=LON0, alt=DATUM, parts=[("br_h39_henday_yellowhead", m)], frame=fr,
                views=[("a", 205.0, 35.0), ("b", 120.0, 30.0), ("c", 20.0, 60.0)], preview=dict(span=2200.0, water=False))


if __name__ == "__main__":
    if "--sample" in sys.argv:
        sample()
