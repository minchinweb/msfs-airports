"""T127 Davies elevated guideway (Valley Line Southeast LRT) and P157 Davies station.

Reference: docs/edmonton-bridges/reference/T127-davies (NOTES.md, SOURCES.md, HANDOFF-T2.md).

Sourced:
  * plan: the two OSM bridge tracks in geometry.json (`tracks`, lrt-tracks.json routes 4 and 5).  The model axis is their mean line;
    each track keeps its own offset from it (4.3 m apart on the line, 13 m apart through the station);
  * station: OSM building way 735311921 "Davies Station" (93 m x 20.6 m, building:levels 4, roof:shape round) and platform way
    1157283680 (centre platform, 8 m wide), in geometry.json `osm_added_2026_11_23`;
  * pier stations and heights: the 2018 LiDAR caught most of the piers standing without their girders (first return 4 to 14 m
    above the bare earth, 35 to 40 m apart on the line, about 22 m apart through the station).  The spikes are sampled into
    elevation/t127-samples.json (`python -I site_t127.py --sample`, needs the gitignored clips).  A spike is a pier when it stands
    more than 6 m up, not more than 1.5 m above the median of the spikes within 60 m (cranes), and not well below a taller spike
    within 45 m (piers still being built).  The 2019 aerial shows no piers yet between about 950 m and 1,060 m, so that gap and the two ends are filled at even
    spacing, kept clear of the roads and railways underneath;
  * sections: the 2019 aerial shows precast U-trough girders, one per track, with spare girders lying on the site; the
    Commons photographs show Y piers (one shaft forking into two arms, one arm per girder) on the line, round columns under wide
    caps at the station, the station's glazed upper band, white panels, the curved roof with a timber soffit, and the open
    ground floor with glass rooms (reference/T127-davies/photos).
Assumed (flagged, no published figure): rail top 1.2 m above the LiDAR pier top (0.2 m bearing, 1.0 m from girder soffit to rail);
U girder 4.9 m wide over the webs, 2.2 m deep, webs 1.2 m above the rail; track centres at least 5.1 m apart (the 2019 aerial shows
a 10 m wide pair of girders, wider than the OSM 4.3 m spacing allows); Y pier sizes (shaft 1.2 m x 1.8 m, fork at 45 % of the
height); the ends of the structure (rail top 1.0 m above the ground where the OSM bridge ways end, retained fill until the deck is
4.5 m up); station heights (ground floor up to the pier caps, glazed band from 1.3 m to 5 m above the rail, roof crest 6.2 m above the rail,
clerestory, 12 m upswept overhang at both ends; the shape is from the ETS "Tap to Pay" drone shot, youtube QIa6F95k4aU); overhead-line masts every 50 m.  No signals, signs or lamps.
Park and ride (P157): the two ETS lots in OSM (amenity=parking, park_ride=yes; about 42,900 m2 for the 1,300 stalls Wikipedia gives),
paved in the model (asphalt) at the median 2018 bare earth inside each, with a flatten polygon at that level, and filled with the
sim's own parked cars by <CarParking> rows beside the OSM parking aisles (the CYXD method, airport-cyxd/tools/gen_parking.py; no
carsHeading, which fails the BGL compiler).  Row depth 5.5 m and aisle 6.5 m are assumed.
"""
import json, math, sys
from bridgelib import *

CODE, TITLE = "T127", "Davies guideway and station"
REF = ROOT / "docs/edmonton-bridges/reference/T127-davies"
LAT0, LON0 = 53.5003, -113.4486
DATUM = 670.00
STATION_WAY, PLATFORM_WAY = 735311921, 1157283680

# U girder section about the track centre (t) and the rail top (y = 0)
G_BOT, G_FLOOR, G_TOP = -1.0, -0.45, 1.2
G_HB, G_HF, G_HT, G_WEB = 1.70, 1.89, 2.45, 0.30
MIN_HALF = 2.55          # track offset from the axis, at least
RAIL_OVER_PIER = 1.2
END_RISE = 1.0           # rail top above the ground where the OSM bridge ways end
FILL_H = 4.5             # retained fill until the rail is this far above the ground
MAX_SPAN = 40.0


def _geo():
    return json.loads((REF / "geometry.json").read_text(encoding="utf-8"))


def centreline():
    """[(lat, lon)] about every metre of the mid line of the two tracks (south to north): each metre of track A paired with the
    nearest point of track B.  Returns the points and the half separation at each."""
    g = _geo()
    fr = Frame(LAT0, LON0)
    A = fr.axis(g["tracks"][0]["points"])
    B = fr.axis(g["tracks"][1]["points"][::-1])
    pts, half = [], []
    for i in range(int(A.L) + 1):
        a = A.en(min(float(i), A.L))
        sb, _ = _closest(B, *a)
        b = B.en(sb)
        pts.append(fr.ll((a[0] + b[0]) / 2, (a[1] + b[1]) / 2))
        half.append(math.hypot(a[0] - b[0], a[1] - b[1]) / 2)
    return pts, half


def sample():
    """Bare earth on the axis and the highest first return within 6 m of it, every metre (needs the gitignored 2018 clips)."""
    from lidar_pil import Grid
    dsm, dtm = Grid(REF / "elevation/dsm-2018-1m.tif"), Grid(REF / "elevation/dtm-2018-1m.tif")
    fr = Frame(LAT0, LON0)
    pts, _ = centreline()
    ax = fr.axis(pts)
    rows = []
    for s in range(int(ax.L) + 1):
        top = -1e9
        for t in range(-6, 7):
            la, lo = fr.ll(*ax.en(s, t))
            top = max(top, dsm.at(la, lo))
        la, lo = fr.ll(*ax.en(s, 0))
        rows.append([s, round(dtm.at(la, lo), 2), round(top, 2)])
    # park-and-ride lots: median bare earth inside each (the 2018 ground was still a building site; the lots are graded flat)
    from shapely.geometry import Point
    lots = {}
    for w in _geo()["osm_added_2026_11_23"]["park_and_ride"]:
        if w["role"] != "lot":
            continue
        P = _poly(w["nodes"])
        x0, y0, x1, y1 = P.bounds
        v = sorted(dtm.at(la, lo) for la in _frange(y0, y1, 0.00005) for lo in _frange(x0, x1, 0.00008) if P.contains(Point(lo, la)))
        lots[str(w["osm_way"])] = round(v[len(v) // 2], 2)
    out = dict(note="2018 LiDAR (AB-Edmonton / NRCAN 1 m DTM and DSM) along the mean line of the two T127 tracks (site_t127.centreline), "
                    "one row per metre from the south end: [s m, bare earth m, highest first return within 6 m of the axis m]. "
                    "The flight pre-dates the girders; the first-return spikes are the piers then standing. "
                    "lots: median bare earth (m) inside each park-and-ride lot polygon, by OSM way id.",
               rows=rows, lots=lots)
    (REF / "elevation/t127-samples.json").write_text(json.dumps(out, separators=(",", ":")), encoding="utf-8")
    print("wrote", len(rows), "rows")


def _frange(a, b, step):
    v = a
    while v < b:
        yield v
        v += step


def _poly(nodes, fr=None):
    """Shapely polygon of [lat, lon] nodes: (lon, lat), or (east, north) metres with a frame."""
    from shapely.geometry import Polygon
    return Polygon([fr.en(la, lo) if fr else (lo, la) for la, lo in nodes])


def park_and_ride(fr, levels):
    """The two ETS park-and-ride lots (OSM, geometry.json `osm_added_2026_11_23` park_and_ride).  Returns
    (pavement [(polygon e/n, level m)], car rows [(title, polygon e/n)]).  Rows: 5.5 m deep (stall) beside a 6.5 m aisle, one per side of
    each aisle segment, so the sim (which lines its cars up with a CarParking polygon's longest edge) parks them square to the aisle;
    cut back from the other aisles' driving lanes, footways and cycleways (1.5 m), service roads (3.5 m), grass islands and bus
    platforms, and kept 0.5 m inside the lot."""
    from shapely.geometry import LineString, Polygon
    from shapely.ops import unary_union
    ways = _geo()["osm_added_2026_11_23"]["park_and_ride"]
    lots = [(w, _poly(w["nodes"], fr)) for w in ways if w["role"] == "lot"]
    aisles = [LineString([fr.en(*p) for p in w["nodes"]]) for w in ways if w["role"] == "aisle"]
    cut = [a.buffer(3.25, cap_style=2) for a in aisles]
    islands = []
    for w in ways:
        if w["role"] != "obstacle":
            continue
        t, pts = w["tags"], [fr.en(*p) for p in w["nodes"]]
        closed = len(pts) > 3 and pts[0] == pts[-1]
        if closed and (t.get("landuse") == "grass" or t.get("public_transport") == "platform" or t.get("highway") == "platform"):
            g = Polygon(pts).buffer(0.5)
            islands.append(g)
            cut.append(g)
        elif t.get("highway") in ("footway", "cycleway"):
            cut.append(LineString(pts).buffer(1.5, cap_style=2))
        elif t.get("highway") == "service":
            cut.append(LineString(pts).buffer(3.5, cap_style=2))
        elif closed:
            cut.append(Polygon(pts).buffer(0.5))
    cut = unary_union(cut)
    inside = unary_union([P.buffer(-0.5, join_style=2) for _w, P in lots])
    rows, taken = [], []
    for k, a in enumerate(aisles):
        c = list(a.coords)
        for p, q in zip(c[:-1], c[1:]):
            seg = LineString([p, q])
            if seg.length < 6.0:
                continue
            for side in ("left", "right"):
                strip = seg.buffer(8.75, cap_style=2, single_sided=True) if side == "left" else seg.buffer(-8.75, cap_style=2, single_sided=True)
                band = seg.buffer(3.25 if side == "left" else -3.25, cap_style=2, single_sided=True)
                g = strip.difference(band).difference(cut).intersection(inside)
                if taken:
                    g = g.difference(unary_union(taken))
                for piece in getattr(g, "geoms", [g]):
                    if piece.geom_type != "Polygon" or piece.area < 30.0:
                        continue
                    piece = piece.simplify(0.3)
                    if piece.is_empty or piece.geom_type != "Polygon":
                        continue
                    rows.append(("Davies park and ride, aisle %d, %s row" % (k + 1, side), piece))
                    taken.append(piece.buffer(0.2))
    pave = [(P.difference(unary_union(islands)) if islands else P, levels[str(w["osm_way"])]) for w, P in lots]
    return pave, rows


def _smooth(v, k):
    return [sum(v[max(0, i - k):i + k + 1]) / len(v[max(0, i - k):i + k + 1]) for i in range(len(v))]


def _crossings(fr, ax):
    """Stations where an OSM road or railway in geometry.json `osm_added_2026_11_23` crosses the axis."""
    out = []
    for w in _geo().get("osm_added_2026_11_23", {}).get("crossing_ways", []):
        p = [fr.en(*q) for q in w["nodes"]]
        for a, b in zip(p[:-1], p[1:]):
            for i in range(len(ax.p) - 1):
                c, d = ax.p[i], ax.p[i + 1]
                den = (d[0] - c[0]) * (b[1] - a[1]) - (d[1] - c[1]) * (b[0] - a[0])
                if abs(den) < 1e-9:
                    continue
                u = ((a[0] - c[0]) * (b[1] - a[1]) - (a[1] - c[1]) * (b[0] - a[0])) / den
                v = ((a[0] - c[0]) * (d[1] - c[1]) - (a[1] - c[1]) * (d[0] - c[0])) / den
                if 0 <= u <= 1 and 0 <= v <= 1:
                    out.append(ax.cum[i] + u * (ax.cum[i + 1] - ax.cum[i]))
    return sorted(out)


def piers_and_profile(rows, L, cross):
    gnd = [r[1] for r in rows]
    h = [r[2] - r[1] for r in rows]
    # spikes: the highest point of each run of samples more than 6 m up
    peaks, cur = [], []
    for s, v in enumerate(h):
        if v > 6.0:
            cur.append(s)
        elif cur:
            k = max(cur, key=lambda i: h[i])
            peaks.append((k, rows[k][2]))
            cur = []
    # cranes: drop a spike more than 1.5 m above the median top of the spikes within 60 m (itself included)
    def med(v):
        v = sorted(v)
        return v[len(v) // 2]
    peaks = [(s, top) for s, top in peaks if top <= med([q for r, q in peaks if abs(r - s) <= 60]) + 1.5]
    # piers still being built: drop a spike more than 1.0 m (plus 6 % of the distance) below another within 45 m
    peaks = [(s, top) for s, top in peaks if all(top >= q - 1.0 - 0.06 * abs(r - s) for r, q in peaks if 0 < abs(r - s) <= 45)]
    # at least 18 m apart, the taller one kept
    peaks.sort(key=lambda p: -h[p[0]])
    chosen = []
    for s, top in peaks:
        if all(abs(s - c[0]) >= 18 for c in chosen):
            chosen.append((s, top))
    chosen.sort()
    ctrl = [(0.0, gnd[0] + END_RISE)] + [(float(s), top + RAIL_OVER_PIER) for s, top in chosen] + [(L, gnd[-1] + END_RISE)]
    yf = profile(ctrl)
    yr = _smooth([yf(s) for s in range(len(rows))], 12)
    yr[0], yr[-1] = ctrl[0][1], ctrl[-1][1]
    # where the structure stands on piers: rail more than FILL_H above the ground
    up = [s for s in range(len(rows)) if yr[s] - gnd[s] > FILL_H]
    s_a, s_b = up[0], up[-1]
    stations = [s for s, _ in chosen if s_a + 2 <= s <= s_b - 2]
    stations = [float(s_a)] + stations + [float(s_b)]
    full = []
    for a, b in zip(stations[:-1], stations[1:]):
        full.append(a)
        n = math.ceil((b - a) / MAX_SPAN)
        for k in range(1, n):
            s = a + (b - a) * k / n
            for c in cross:                       # 8 m clear of a crossing road or railway
                if abs(s - c) < 8:
                    s = c + (8 if s >= c else -8)
            full.append(s)
    full.append(stations[-1])
    return full, yr, gnd, (s_a, s_b), [s for s, _ in chosen]


def sweep(m, ax, ss, sec, sws):
    """Extrude a convex section along the axis.  sec(s) -> [(t, y), ...] (same count at every station, in order round the
    section); sws: one swatch, or one per section edge.  Ends are capped."""
    n = len(sec(ss[0]))
    sws = sws if isinstance(sws, (list, tuple)) else [sws] * n
    prev = None
    for s in ss:
        cur = [ax.p3(s, t, y) for t, y in sec(s)]
        if prev:
            c = [sum(p[i] for p in prev + cur) / (2 * n) for i in range(3)]
            for i in range(n):
                j = (i + 1) % n
                m.poly([prev[i], prev[j], cur[j], cur[i]], sws[i], c)
        prev = cur
    for s, other in ((ss[0], ss[1]), (ss[-1], ss[-2])):
        p = [ax.p3(s, t, y) for t, y in sec(s)]
        o = [ax.p3(other, t, y) for t, y in sec(other)]
        c = [sum(q[i] for q in o) / n for i in range(3)]
        m.poly(p, sws[0], c)


def build():
    fr = Frame(LAT0, LON0)
    d = json.loads((REF / "elevation/t127-samples.json").read_text(encoding="utf-8"))
    rows = d["rows"]
    pts, half = centreline()
    ax = fr.axis(pts)
    L = ax.L
    cross = _crossings(fr, ax)
    piers, yr_m, gnd_m, (s_a, s_b), lidar = piers_and_profile(rows, L, cross)
    hs = _smooth([max(MIN_HALF, v) for v in half], 8)

    def at(v, s):
        s = min(max(s, 0.0), len(v) - 1.0)
        i = min(int(s), len(v) - 2)
        return v[i] + (v[i + 1] - v[i]) * (s - i)

    Y = lambda s: at(yr_m, s) - DATUM          # rail top
    G = lambda s: at(gnd_m, s) - DATUM         # bare earth
    T = lambda s: at(hs, s)                    # track offset from the axis
    m = BMesh()

    geo = _geo()["osm_added_2026_11_23"]
    def way(i):
        return next(w for w in geo["station_ways"] if w["osm_way"] == i)
    stn = [_closest(ax, *fr.en(*p)) for p in way(STATION_WAY)["nodes"]]
    st0, st1 = min(p[0] for p in stn), max(p[0] for p in stn)
    sw0, sw1 = min(p[1] for p in stn), max(p[1] for p in stn)
    plat = [_closest(ax, *fr.en(*p)) for p in way(PLATFORM_WAY)["nodes"]]
    pl0, pl1 = min(p[0] for p in plat), max(p[0] for p in plat)
    y_st = sum(Y(s) for s in range(int(st0), int(st1) + 1)) / (int(st1) - int(st0) + 1)
    Ys = lambda s: y_st if st0 - 1 <= s <= st1 + 1 else Y(s)   # the platform is level
    g_st = min(G(s) for s in range(int(st0), int(st1) + 1))

    # stations along the axis: every 6 m plus the axis vertices (thinned)
    def stations(a, b, step=6.0):
        k = max(1, math.ceil((b - a) / step))
        return [a + (b - a) * i / k for i in range(k + 1)]

    # --- the two tracks: U girders on piers, retained fill at the ends, a flat deck through the station
    for sg in (1, -1):
        tc = lambda s, sg=sg: sg * T(s)
        for a, b, kind in ((0.0, s_a, "fill"), (s_a, st0, "girder"), (st1, s_b, "girder"), (s_b, L, "fill")):
            ss = stations(a, b)
            if kind == "girder":
                Yg = Ys
                sweep(m, ax, ss, lambda s: [(tc(s) - G_HB, Yg(s) + G_BOT), (tc(s) + G_HB, Yg(s) + G_BOT),
                                            (tc(s) + G_HF, Yg(s) + G_FLOOR), (tc(s) - G_HF, Yg(s) + G_FLOOR)], CONC)
                for e in (1, -1):
                    sweep(m, ax, ss, lambda s, e=e: [(tc(s) + e * G_HF, Yg(s) + G_FLOOR), (tc(s) + e * G_HT, Yg(s) + G_TOP),
                                                     (tc(s) + e * (G_HT - G_WEB), Yg(s) + G_TOP),
                                                     (tc(s) + e * (G_HF - G_WEB), Yg(s) + G_FLOOR)], CONC)
            else:
                Yg = Y
                # retained fill: precast panel walls from the ground to the track bed, upstands as on the girders
                sweep(m, ax, ss, lambda s: [(tc(s) - G_HT, G(s) - 0.5), (tc(s) + G_HT, G(s) - 0.5),
                                            (tc(s) + G_HT, Yg(s) + G_FLOOR), (tc(s) - G_HT, Yg(s) + G_FLOOR)],
                      [PIERBEIGE, PIERBEIGE, CONC, PIERBEIGE])
                for e in (1, -1):
                    sweep(m, ax, ss, lambda s, e=e: [(tc(s) + e * G_HT, Yg(s) + G_FLOOR), (tc(s) + e * G_HT, Yg(s) + G_TOP),
                                                     (tc(s) + e * (G_HT - G_WEB), Yg(s) + G_TOP),
                                                     (tc(s) + e * (G_HT - G_WEB), Yg(s) + G_FLOOR)], CONC)
            _track(m, ax, ss, tc, Yg)
        _track(m, ax, stations(st0, st1), tc, lambda s: y_st)
        # abutment wall where the fill meets the girders
        for s in (s_a, s_b):
            prism(m, [ax.en(s - 0.6, tc(s) - G_HT - 0.3), ax.en(s + 0.6, tc(s) - G_HT - 0.3),
                      ax.en(s + 0.6, tc(s) + G_HT + 0.3), ax.en(s - 0.6, tc(s) + G_HT + 0.3)], G(s) - 0.5, Y(s) + G_FLOOR, CONCD)

    # --- piers (through the station too: the 2018 LiDAR has them about 22 m apart there; round columns under a cap)
    for s in piers:
        _pier(m, ax, s, T(s), Ys(s) + G_BOT, g_st if st0 <= s <= st1 else G(s))

    # --- overhead line masts on the outer webs every 50 m, cantilever over each track
    for k in range(int(L // 50) + 1):
        s = 10 + 50 * k
        if s > L - 5 or st0 - 6 <= s <= st1 + 6:
            continue
        for sg in (1, -1):
            t = sg * (T(s) + G_HT + 0.25)
            beam(m, ax.p3(s, t, Ys(s) - 0.4), ax.p3(s, t, Ys(s) + 7.2), 0.3, 0.3, GREY)
            beam(m, ax.p3(s, t, Ys(s) + 6.7), ax.p3(s, sg * T(s), Ys(s) + 6.7), 0.15, 0.15, GREY)

    _station(m, ax, st0, st1, sw0, sw1, pl0, pl1, y_st, g_st, T)

    # --- park and ride: asphalt at each lot's level (the generator flattens the terrain to it), cars from <CarParking> rows
    import shapely
    pave, rows_cp = park_and_ride(fr, d["lots"])
    terrain_extra, car_parks = [], []
    for P, lvl in pave:
        for g in getattr(P, "geoms", [P]):
            for tri in shapely.constrained_delaunay_triangles(g).geoms:
                q = list(tri.exterior.coords)[:3]
                cx, cz = sum(x for x, _ in q) / 3, sum(z for _, z in q) / 3
                m.poly([(x, lvl - DATUM + 0.05, z) for x, z in q], ASPHALT, (cx, lvl - DATUM - 1.0, cz))
            ring = list(g.exterior.simplify(0.3).coords)[:-1]
            terrain_extra.append(("flatten", "%s %s park and ride level" % (CODE, TITLE), lvl, [fr.ll(x, z) for x, z in ring]))
    for title, g in rows_cp:
        car_parks.append((title, [fr.ll(x, z) for x, z in list(g.exterior.coords)[:-1]]))

    return dict(code=CODE, title=TITLE, lat0=LAT0, lon0=LON0, alt=DATUM, parts=[("br_t127_davies", m)], frame=fr, axis=ax,
                terrain_extra=terrain_extra, car_parks=car_parks,
                views=[("a", 120.0, 25.0), ("b", 300.0, 30.0), ("c", 200.0, 60.0)], preview=dict(span=1500.0, water=False),
                info=dict(piers=piers, lidar=lidar, s_a=s_a, s_b=s_b, st=(st0, st1), y_st=y_st + DATUM, g_st=g_st + DATUM,
                          cross=cross, y=lambda s: Y(s) + DATUM, g=lambda s: G(s) + DATUM, L=L))


def _closest(ax, e, n):
    best = (1e18, 0.0, 0.0)
    for i in range(len(ax.p) - 1):
        a, b = ax.p[i], ax.p[i + 1]
        dx, dy = b[0] - a[0], b[1] - a[1]
        ln2 = dx * dx + dy * dy or 1.0
        u = max(0.0, min(1.0, ((e - a[0]) * dx + (n - a[1]) * dy) / ln2))
        x, y = a[0] + u * dx, a[1] + u * dy
        dd = (e - x) ** 2 + (n - y) ** 2
        if dd < best[0]:
            ln = math.sqrt(ln2)
            best = (dd, ax.cum[i] + u * ln, (-(e - x) * dy + (n - y) * dx) / ln)
    return best[1], best[2]


def _track(m, ax, ss, tc, Yg):
    """Two concrete plinths and two rails (1.435 m gauge) on the girder floor."""
    for r in (-0.72, 0.72):
        sweep(m, ax, ss, lambda s: [(tc(s) + r - 0.3, Yg(s) + G_FLOOR), (tc(s) + r + 0.3, Yg(s) + G_FLOOR),
                                    (tc(s) + r + 0.3, Yg(s) - 0.18), (tc(s) + r - 0.3, Yg(s) - 0.18)], CONCD)
        sweep(m, ax, ss, lambda s: [(tc(s) + r - 0.04, Yg(s) - 0.18), (tc(s) + r + 0.04, Yg(s) - 0.18),
                                    (tc(s) + r + 0.04, Yg(s)), (tc(s) + r - 0.04, Yg(s))], RAILSTEEL)


def _pier(m, ax, s, half, y_top, ground):
    """Y pier where the girders sit side by side, round columns under a cap beam where they are apart (the station)."""
    yb = ground - 1.0
    if half <= 3.5:
        hgt = y_top - ground
        yf = ground + 0.55 * hgt - 0.4                 # fork
        # shaft: 1.2 m along the line, 1.8 m across, widening a little to the fork
        frustum(m, [ax.en(s - 0.6, -0.9), ax.en(s + 0.6, -0.9), ax.en(s + 0.6, 0.9), ax.en(s - 0.6, 0.9)],
                [ax.en(s - 0.6, -1.3), ax.en(s + 0.6, -1.3), ax.en(s + 0.6, 1.3), ax.en(s - 0.6, 1.3)], yb, yf, CONC)
        for sg in (1, -1):
            # arm: from the fork out to under the girder centre, 1.2 m along the line
            t_in, t_out = sg * 0.2, sg * half
            q_bot = [ax.en(s - 0.6, t_in), ax.en(s + 0.6, t_in), ax.en(s + 0.6, sg * 1.3), ax.en(s - 0.6, sg * 1.3)]
            q_top = [ax.en(s - 0.6, t_out - sg * 1.1), ax.en(s + 0.6, t_out - sg * 1.1), ax.en(s + 0.6, t_out + sg * 1.1),
                     ax.en(s - 0.6, t_out + sg * 1.1)]
            frustum(m, q_bot, q_top, yf, y_top - 0.2, CONC)
            prism(m, [ax.en(s - 0.5, t_out - 0.9), ax.en(s + 0.5, t_out - 0.9), ax.en(s + 0.5, t_out + 0.9),
                      ax.en(s - 0.5, t_out + 0.9)], y_top - 0.2, y_top, CONCD)
    else:
        cap_h = 1.8
        cols = [0.0] if half <= 6.0 else [-(half - 1.5), half - 1.5]
        for t in cols:
            e, n = ax.en(s, t)
            cyl(m, e, n, 0.9, 0.9, yb, y_top - cap_h + 0.05, CONC, n=16)
        w = half + G_HT
        frustum(m, [ax.en(s - 1.2, -w + 1.5), ax.en(s + 1.2, -w + 1.5), ax.en(s + 1.2, w - 1.5), ax.en(s - 1.2, w - 1.5)],
                [ax.en(s - 1.2, -w), ax.en(s + 1.2, -w), ax.en(s + 1.2, w), ax.en(s - 1.2, w)], y_top - cap_h, y_top, CONC)


def _station(m, ax, st0, st1, sw0, sw1, pl0, pl1, y, g, T):
    """P157 Davies station: the OSM footprint at deck level, open ground floor with glass rooms, white panel belly, glazed upper
    band leaning out, barrel roof with a timber soffit overhanging both ends, centre platform."""
    tw = max(abs(sw0), abs(sw1))
    ss = [st0, st1]
    # belly: white panels round the girders and pier caps, from the cap soffits to the track bed
    yb = y + G_BOT - 2.3
    ribbon(m, ax, st0, st1, -tw, tw, yb, y + G_FLOOR, WHITE, sw_bot=WHITE)
    # walls above the deck: white band to 1.3 m above the rail, then the glazed band leaning out to the eaves
    for sg in (1, -1):
        sweep(m, ax, ss, lambda s, sg=sg: [(sg * (tw - 0.3), y + G_FLOOR), (sg * tw, y + G_FLOOR), (sg * tw, y + 1.3),
                                           (sg * (tw - 0.3), y + 1.3)], WHITE)
        sweep(m, ax, ss, lambda s, sg=sg: [(sg * (tw - 0.3), y + 1.3), (sg * tw, y + 1.3), (sg * (tw + 0.8), y + 5.0),
                                           (sg * (tw + 0.5), y + 5.0)], GLASS)
        # mullions every 4.5 m
        k = int((st1 - st0) // 4.5)
        for i in range(k + 1):
            s = st0 + (st1 - st0) * i / k
            beam(m, ax.p3(s, sg * (tw + 0.05), y + 1.3), ax.p3(s, sg * (tw + 0.85), y + 5.0), 0.25, 0.25, WHITE)
    # roof (ETS drone shot, youtube QIa6F95k4aU at 0:00-0:03): a shallow standing-seam curve from eave to eave whose ends run 12 m
    # past the end walls and sweep up over the tracks, timber soffit; a raised glazed clerestory along the middle
    OVER, LIFT, rise = 12.0, 3.0, 1.2
    half = tw + 0.9
    nseg = 8

    def lift(s):
        d = max(st0 - s, s - st1, 0.0)
        return LIFT * (d / OVER) ** 2

    def arc(u, s):
        tt = -half + 2 * half * u
        return tt, y + 5.0 + rise * (1 - (tt / half) ** 2) + lift(s)
    ss_roof = sorted(set([st0 - OVER + OVER * k / 6 for k in range(7)] + [st0 + (st1 - st0) * k / 16 for k in range(17)]
                         + [st1 + OVER * k / 6 for k in range(7)]))
    for i in range(nseg):
        sweep(m, ax, ss_roof, lambda s, i=i: [(arc(i / nseg, s)[0], arc(i / nseg, s)[1] - 0.5), (arc((i + 1) / nseg, s)[0], arc((i + 1) / nseg, s)[1] - 0.5),
                                              arc((i + 1) / nseg, s), arc(i / nseg, s)], [TIMBER, WHITE, WHITEST, WHITE])
    # clerestory: 7 m wide, glazed sides 1.6 m tall, on the crest from 5 m inside each end wall
    yc = y + 5.0 + rise
    sweep(m, ax, [st0 + 5.0, st1 - 5.0], lambda s: [(-3.5, yc - 0.3), (3.5, yc - 0.3), (3.5, yc + 1.6), (-3.5, yc + 1.6)],
          [WHITE, GLASS, WHITEST, GLASS])
    # platform (OSM way 1157283680): concrete, yellow edge strips, a glass lift and stair enclosure in the middle
    pw = T((pl0 + pl1) / 2) - 1.65
    ribbon(m, ax, pl0, pl1, -pw, pw, y + G_FLOOR, y + 0.35, CONC, sw_top=PANEL)
    for t0, t1 in ((pw - 0.6, pw), (-pw, -pw + 0.6)):
        ribbon(m, ax, pl0, pl1, t0, t1, y + 0.35, y + 0.37, YELLOW)
    sm = (pl0 + pl1) / 2
    ribbon(m, ax, sm - 6.0, sm + 6.0, -2.2, 2.2, y + 0.35, y + 3.2, GLASS, sw_top=WHITE)
    # ground floor: glass rooms set back under the belly, a solid service block, columns along the edges
    ribbon(m, ax, st0 + 8.0, st0 + (st1 - st0) * 0.62, -tw + 2.5, tw - 2.5, g - 0.3, yb - 0.05, GLASS, sw_top=WHITE)
    ribbon(m, ax, st0 + (st1 - st0) * 0.62, st1 - 6.0, -tw + 2.5, tw - 2.5, g - 0.3, yb - 0.05, PANEL, sw_top=WHITE)
    k = int((st1 - st0) // 12)
    for i in range(k + 1):
        s = st0 + 1.0 + (st1 - st0 - 2.0) * i / k
        for sg in (1, -1):
            e, n = ax.en(s, sg * (tw - 0.8))
            cyl(m, e, n, 0.35, 0.35, g - 0.3, yb, CONC, n=10)


if __name__ == "__main__":
    if "--sample" in sys.argv:
        sample()
