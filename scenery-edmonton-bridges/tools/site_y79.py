"""Y79 Bremner Cloverleaf (Highway 21 over Highway 16, Strathcona County): two overpasses, two loops, outer ramps, Highway 21 approaches.

Sourced (docs/edmonton-bridges/reference/Y79-bremner NOTES.md, HANDOFF-T2.md):
  * plan: OSM ways (decks 32829979 east / northbound, 153737445 west / southbound; Highway 21 approaches; NE loop 32834983, SE loop
    32835223; the outer ramps and stubs added to geometry.json from Overpass on 2026-10-15);
  * heights: 2018 LiDAR.  Ramps and approaches sit on embankment, so their road surface is the bare-earth (DTM) crown, sampled by
    `python -I site_y79.py --sample` (needs the gitignored .tif clips) into elevation/y79-samples.json, which build() reads;
    the deck levels are the first-return medians along the decks (677.27 m east, 677.70 m west);
  * N-1 (east): 3 spans 29 / 16.2 / 29 m, 5 girder lines per span (the inspection's "15 girders" = 3 x 5), concrete, clear roadway
    14.2 m, eight columns on two piers; S-6 (west): 2 spans 38.65 m, weathering steel, clear roadway 16.6 m, five piles on one pier.
    Girder depth follows from the published 5.3 m posted clearance over the Highway 16 pavement (DTM 670.0-670.3 m).
Assumed: pier and abutment stations along the OSM line, S-6 girder count (6), column sizes, ramp roadway width 8.6 m, 4:1 slopes,
approach width 12 m tapering into the deck width, lamp positions.  Colour: asphalt, concrete, rust steel (S-6), grass slopes.
"""
import json, math, sys
from bridgelib import *
from t2lib import *

CODE, TITLE = "Y79", "Bremner Cloverleaf"
DATUM = 670.00
F = "Y79-bremner"
LAT0, LON0 = 53.5702, -113.2461
SAMPLES = ROOT / "docs/edmonton-bridges/reference" / F / "elevation/y79-samples.json"
RAMP_W = 8.6
SLOPE = 4.0
STEP = 6.0
APPROACH = 300.0

NB = ("nb", [1278901802, 1259559956, 1278901805, 32829979, 1278901804, 32830235, 1259559954], 32829979, 14.2)
SB = ("sb", [32831204, 153737445, 1281358648, 1281358649], 153737445, 16.6)
RAMPS = [("ne_loop", 32834983), ("se_loop", 32835223), ("nw_out", 153737435), ("sw_in", 32834795), ("ne_in_a", 91930051),
         ("ne_in_b", 1264725793), ("w16_ne", 153737436), ("se_a", 1259559957), ("se_b", 1259559962), ("se_out", 32830192),
         ("sw_stub", 91930054), ("nw_stub", 1259559955)]
# along the deck way: abutment stations, pier stations, girder depth, slab, column offsets/radius, girder lines, girder colour, lift
DECK = {
    32829979: dict(s0=0.65, s1=74.85, piers=[29.65, 45.85], depth=1.30, slab=0.27, cols=[-5.4, -1.8, 1.8, 5.4], r=0.45, n=5, gsw=None, lift=-0.12),
    153737445: dict(s0=11.35, s1=88.65, piers=[50.0], depth=1.85, slab=0.30, cols=[-6.4, -3.2, 0.0, 3.2, 6.4], r=0.5, n=6, gsw="RUST", lift=-0.12),
}


def chain(fr, ways):
    nodes, marks, cum = [], {}, 0.0
    for w in ways:
        pts = find_way(F, w)
        nodes += pts if not nodes else pts[1:]
        marks[w] = cum
        cum += fr.axis(pts).L
    return fr.axis(nodes), marks


def _roads(fr):
    roads = {}
    for name, ways, bw, wd in (NB, SB):
        ax, marks = chain(fr, ways)
        roads[name] = dict(ax=ax, marks=marks, bridge=bw, wd=wd)
    for name, w in RAMPS:
        roads[name] = dict(ax=fr.axis(find_way(F, w)), ramp=True)
    return roads


def sample():
    """Write y79-samples.json: DTM crown height and side ground along every axis every STEP m (heights above DATUM)."""
    from lidar_pil import Grid
    base = ROOT / "docs/edmonton-bridges/reference" / F / "elevation"
    dtm, dsm = Grid(base / "dtm-2018-1m.tif"), Grid(base / "dsm-2018-1m.tif")
    fr = Frame(LAT0, LON0)

    def at(g, e, n):
        return g.at(*fr.ll(e, n))
    out = {}
    for name, r in _roads(fr).items():
        ax = r["ax"]
        w = RAMP_W if r.get("ramp") else 12.0
        ss = [min(ax.L, i * STEP) for i in range(int(ax.L / STEP) + 2)]
        rec = dict(ss=ss, crown=[], gl=[], gr=[])
        for s in ss:
            v = [x for x in (at(dtm, *ax.en(s, t)) for t in (-3, -1.5, 0, 1.5, 3)) if x == x]
            rec["crown"].append(round(max(v) - DATUM, 3) if v else None)
            for key, sg in (("gl", 1), ("gr", -1)):
                v = [x for x in (at(dtm, *ax.en(s, sg * (w / 2 + d))) for d in (10, 14, 18, 22, 26, 30)) if x == x]
                rec[key].append(round(min(v) - DATUM, 3) if v else None)
        if not r.get("ramp"):
            rec["dsm"] = [round(at(dsm, *ax.en(s, 0)) - DATUM, 3) for s in ss]
        out[name] = rec
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


def road_fill(m, ax, s0, s1, y_fn, w_fn, gl, gr, fade=(0.0, 0.0), lines=False, taper=(False, False)):
    """Raised road on a 4:1 embankment: asphalt top, grass slopes down to the side ground.  Where the fill is lower than 0.8 m the
    road sinks into the ground (it vanishes below the terrain), and it does the same over the `fade` lengths at open ends."""
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
    for a, b in zip(rows[:-1], rows[1:]):
        if max(a["h"], b["h"]) < 0.0:
            continue
        c = ax.p3((a["s"] + b["s"]) / 2, 0, (a["y"] + b["y"]) / 2 - 6)
        m.poly([ax.p3(a["s"], -a["w"] / 2, a["y"]), ax.p3(b["s"], -b["w"] / 2, b["y"]), ax.p3(b["s"], b["w"] / 2, b["y"]),
                ax.p3(a["s"], a["w"] / 2, a["y"])], ASPHALT, c)
        for sg, key in ((1, "hl"), (-1, "hr")):
            m.poly([ax.p3(a["s"], sg * a["w"] / 2, a["y"]), ax.p3(b["s"], sg * b["w"] / 2, b["y"]),
                    ax.p3(b["s"], sg * (b["w"] / 2 + SLOPE * b[key] * b["f"]), b["y"] - b[key]),
                    ax.p3(a["s"], sg * (a["w"] / 2 + SLOPE * a[key] * a["f"]), a["y"] - a[key])], GRASS, c)
        if lines and a["sink"] == 0.0 and b["sink"] == 0.0:
            for sg, sw in ((1, YELLOWR), (-1, WHITE)):
                ta, tb = sg * (a["w"] / 2 - 0.45), sg * (b["w"] / 2 - 0.45)
                m.poly([ax.p3(a["s"], ta - 0.08, a["y"] + 0.02), ax.p3(b["s"], tb - 0.08, b["y"] + 0.02),
                        ax.p3(b["s"], tb + 0.08, b["y"] + 0.02), ax.p3(a["s"], ta + 0.08, a["y"] + 0.02)], sw, c)


def build():
    fr = Frame(LAT0, LON0)
    smp = json.loads(SAMPLES.read_text(encoding="utf-8"))
    m = BMesh()
    for name, r in _roads(fr).items():
        sp, ax = smp[name], r["ax"]
        ss = sp["ss"]
        crown = _smooth(sp["crown"], 1)
        gl = profile(list(zip(ss, _smooth(sp["gl"], 2))))
        gr = profile(list(zip(ss, _smooth(sp["gr"], 2))))
        if r.get("ramp"):
            y = profile([(s, c - 0.1) for s, c in zip(ss, crown)])
            ok = [s for s, c in zip(ss, sp["crown"]) if c is not None]       # no LiDAR beyond the clip: end the ramp there
            lo, hi = min(ok), max(ok)
            road_fill(m, ax, lo, hi, y, lambda s: RAMP_W, gl, gr, fade=(40.0 if lo > 1 else 0.0, 40.0 if hi < ax.L - 7 else 0.0), lines=True)
            continue
        bw, wd = r["bridge"], r["wd"]
        d = DECK[bw]
        base = r["marks"][bw]
        Lw = fr.axis(find_way(F, bw)).L
        a0, a1 = base + d["s0"], base + d["s1"]
        pts = [(s - base, v) for s, v in zip(ss, sp["dsm"]) if base + 4 < s < base + Lw - 4]
        med = sorted(v for _, v in pts)[len(pts) // 2]
        pts = [p for p in pts if abs(p[1] - med) < 0.35]
        n = len(pts)
        ms, mv = sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n
        k = sum((p[0] - ms) * (p[1] - mv) for p in pts) / (sum((p[0] - ms) ** 2 for p in pts) or 1)

        def ydeck(s, ms=ms, mv=mv, k=k, d=d):      # s along the deck way
            return mv + k * (s - ms) + d["lift"]
        # bare earth under the deck ends is not the road: within 25 m of an abutment, where the first return is well above it, use the first return
        crown = [ds - 0.12 if (ds - c > 0.4 and min(abs(q - a0), abs(q - a1)) < 25) else c for q, c, ds in zip(ss, crown, sp["dsm"])]
        yap = profile([(s, c - 0.1) for s, c in zip(ss, crown)])
        c0, c1 = ydeck(d["s0"]) - yap(a0), ydeck(d["s1"]) - yap(a1)

        def y_all(s, yap=yap, a0=a0, a1=a1, c0=c0, c1=c1, base=base):
            if s <= a0:
                return yap(s) + c0 * max(0.0, 1 - (a0 - s) / 90.0)
            return yap(s) + c1 * max(0.0, 1 - (s - a1) / 90.0)

        def w_fn(s, a0=a0, a1=a1, wd=wd):
            dd = max(a0 - s, s - a1, 0.0)
            return wd + (12.0 - wd) * min(1.0, dd / 60.0)
        road_fill(m, ax, max(0.0, a0 - APPROACH), a0, y_all, w_fn, gl, gr, fade=(120.0, 0.0), taper=(False, True))
        road_fill(m, ax, a1, min(ax.L, a1 + APPROACH), y_all, w_fn, gl, gr, fade=(0.0, 120.0), taper=(True, False))
        sub = Axis([ax.en(s, 0) for s in ax.stations(a0, a1, 0)])
        yl = lambda s, d=d, ydeck=ydeck: ydeck(s + d["s0"])
        girder_deck(m, sub, 0.0, sub.L, yl, -wd / 2, wd / 2, lambda s: 0.3, n_girders=d["n"], depth=d["depth"], slab=d["slab"],
                    inner=+1, sidewalk=0, left_sign=+1, carriage=11.1, lamp_step=36.0,
                    girder_sw=globals()[d["gsw"]] if d["gsw"] else None)
        for s in d["piers"]:
            q = s - d["s0"]
            ys = yl(q) - d["slab"] - d["depth"] - 0.15
            for t in d["cols"]:
                e, nn = sub.en(q, t)
                cyl(m, e, nn, d["r"], d["r"], -1.5, ys - 0.9, CONC, n=12)
            prism(m, nose_plan(sub, q, 0.0, 0.9, wd / 2 - 1.2, 0.0, (False, False)), ys - 0.9, ys, CONCD)
    return dict(code=CODE, title=TITLE, lat0=LAT0, lon0=LON0, alt=DATUM, parts=[("br_y79_bremner", m)], frame=fr,
                views=[("a", 205.0, 35.0), ("b", 120.0, 30.0), ("c", 20.0, 60.0)], preview=dict(span=1300.0, water=False))


if __name__ == "__main__":
    if "--sample" in sys.argv:
        sample()
