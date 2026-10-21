"""Terrain polygons that go with the bridge models: the river-channel flatten under each span, the grass mask on the banks, and
sites that have no model (Groat Road Bridge) or an old bridge to clear (Walterdale 1913 truss).

Why: the sim's terrain / photogrammetry carries the real bridge as ground (a curtain or a strip of land from deck level down to
the water), and the 2018 imagery shows the paths and roads under a deck.  Per site this gives
  flatten  - terrain levelled to the river surface across the river part of the span (footprint of the model, inside the band
             between the two banks); polygon altitude = river datum, attribute set from 2FA2.xml / CYXD.xml (FlattenMode,
             PreciseTerraforming, ForceElevation), plus buildings / photogrammetry / trees / rocks removed;
  grass    - the "Grass over construction" ground material on the footprint over land (the abutments and the bank under the deck),
             so a path or road seen in the aerial does not show through under the deck.
The river part is read from the bare-earth profile of the site's main OSM way (docs/edmonton-bridges/reference/<folder>/elevation/
profiles.csv, 25 m steps): the run around the lowest sample where the ground is within RISE of it.  Nothing here has been seen in
the sim.  Needs shapely.
"""
import csv
import math

from bridgelib import ROOT, Frame, find_way
import exclusions

REF = ROOT / "docs/edmonton-bridges/reference"
RISE = 1.5          # m above the lowest ground sample that still counts as river
BAND = 70.0         # m each side of the axis; the footprint is cut by the band between the banks
GRASS_MIN = 60.0    # m2, drops slivers of the grass mask

# site -> (reference folder, OSM way of the main deck, kind of footprint)
RIVER = {
    "r9": ("R9-menzies", 700467672),
    "r10": ("R10-high-level", 22915822),
    "r11": ("R11-walterdale", 175326660),
    "r12": ("R12-james-macdonald", 25455305),
    "r13": ("R13-low-level", 31882107),
    "r14": ("R14-tawatina", 1221895804),
    "r15": ("R15-dawson", 22916476),
    "r20": ("R20-beverly", 61430014),
    "r21": ("R21-clover-bar", 61431758),
    "r22": ("R22-clover-bar-railway", 23426591),
    "r6": ("R6-quesnell", 22916674),
}

# sites whose whole footprint is levelled to the site datum (the sim ground pre-dates the structure and buries it)
LEVEL = {"p152"}

# no model: the polygons are the ways buffered by `width` m each side
FLATTEN_ONLY = {
    "r8": dict(code="R8", title="Groat Road Bridge", folder="R8-groat", way=22916458, others=[191843040, 27265608], width=9.0),
}

# Extra clearing relative to a site's own axis (s along, t across, positive to the left / west), for things the sim shows that
# the model does not replace.  kind "exclude" clears buildings / photogrammetry / trees; "flatten" also levels the river part.
# Walterdale: the 1913 truss stood just west of the 2017 arch (reference/R11-walterdale/NOTES.md); no geometry survives, so the
# strip (t 12 to 48 m west of the road way, about 11 m of old deck either side of an assumed centre 30 m west) is an estimate.
EXTRA = {
    "r11": [dict(title="old 1913 Walterdale truss (estimated)", t0=12.0, t1=48.0, s0=-15.0, s1=None, flatten=True)],
}


def _profile(folder, way):
    rows = []
    for r in csv.DictReader(open(REF / folder / "elevation/profiles.csv")):
        if str(r["osm_way"]) == str(way):
            try:
                d = float(r["dtm_m"])
            except ValueError:
                continue
            if d == d:
                rows.append((float(r["chainage_m"]), d))
    rows.sort()
    return rows


def river_span(folder, way):
    """(s0, s1, lowest ground) of the river run along an OSM way, or None when the profile never gets near a river."""
    rows = _profile(folder, way)
    if len(rows) < 3:
        return None
    k = min(range(len(rows)), key=lambda i: rows[i][1])
    lo = rows[k][1]
    lim = lo + RISE
    i0 = i1 = k
    while i0 > 0 and rows[i0 - 1][1] <= lim:
        i0 -= 1
    while i1 < len(rows) - 1 and rows[i1 + 1][1] <= lim:
        i1 += 1

    def edge(a, b):    # chainage where the ground crosses `lim` between rows a (low) and b (high)
        (sa, da), (sb, db) = rows[a], rows[b]
        return sa + (sb - sa) * (lim - da) / (db - da) if db != da else sa
    s0 = 0.0 if i0 == 0 else edge(i0, i0 - 1)
    s1 = rows[-1][0] if i1 == len(rows) - 1 else edge(i1, i1 + 1)
    return s0, s1, lo


def _band(ax, s0, s1, w=BAND):
    from shapely.geometry import Polygon
    n = max(2, int((s1 - s0) / 5.0))
    ss = [s0 + (s1 - s0) * i / n for i in range(n + 1)]
    left = [ax.en(s, w) for s in ss]
    right = [ax.en(s, -w) for s in ss]
    return Polygon(left + right[::-1]).buffer(0)


def _polys(geom):
    if geom.is_empty:
        return []
    return list(geom.geoms) if hasattr(geom, "geoms") else [geom]


def site_polygons(name, res):
    """[(kind, title, alt, [(lat, lon), ...])] for one built site.  Must run before bridgelib.save_chunks mirrors the mesh."""
    from shapely.ops import unary_union
    out = []
    fr = res["frame"]
    prs = exclusions.pieces(res)
    if name in LEVEL:
        for g in prs:
            out.append(("flatten", "%s %s level" % (res["code"], res["title"]), res["alt"], exclusions.ring_ll(g, fr)))
    if name in RIVER and prs:
        folder, way = RIVER[name]
        span = river_span(folder, way)
        ax = fr.axis(find_way(folder, way))
        foot = unary_union(prs)
        if span:
            band = _band(ax, span[0], span[1])
            for g in _polys(foot.intersection(band)):
                if g.area >= exclusions.MIN_AREA:
                    out.append(("flatten", "%s %s river" % (res["code"], res["title"]), res["alt"], exclusions.ring_ll(g, fr)))
            land = foot.buffer(-exclusions.MARGIN, join_style=2).difference(band)
        else:
            land = foot.buffer(-exclusions.MARGIN, join_style=2)
        for g in _polys(land):
            if g.area >= GRASS_MIN and not g.interiors:
                out.append(("grass", "%s %s bank" % (res["code"], res["title"]), res["alt"], exclusions.ring_ll(g, fr)))
        for ex in EXTRA.get(name, []):
            s1 = ax.L + 15.0 if ex["s1"] is None else ex["s1"]
            strip = _band_strip(ax, ex["s0"], s1, ex["t0"], ex["t1"])
            out.append(("exclude", "%s %s: %s" % (res["code"], res["title"], ex["title"]), res["alt"], exclusions.ring_ll(strip, fr)))
            if ex["flatten"] and span:
                for g in _polys(strip.intersection(_band_strip(ax, span[0], span[1], ex["t0"], ex["t1"]))):
                    if g.area >= exclusions.MIN_AREA:
                        out.append(("flatten", "%s %s: %s river" % (res["code"], res["title"], ex["title"]), res["alt"], exclusions.ring_ll(g, fr)))
    return out


def _band_strip(ax, s0, s1, t0, t1):
    from shapely.geometry import Polygon
    n = max(2, int((s1 - s0) / 5.0))
    ss = [s0 + (s1 - s0) * i / n for i in range(n + 1)]
    return Polygon([ax.en(s, t1) for s in ss] + [ax.en(s, t0) for s in ss[::-1]]).buffer(0)


def flatten_only(name):
    """Polygons for a bridge with no model: ways buffered by `width`, river part flattened, the rest left alone."""
    from shapely.geometry import LineString
    from shapely.ops import unary_union
    c = FLATTEN_ONLY[name]
    nodes = find_way(c["folder"], c["way"])
    fr = Frame(*nodes[len(nodes) // 2])
    ax = fr.axis(nodes)
    span = river_span(c["folder"], c["way"])
    if not span:
        return []
    shapes = [LineString([fr.en(*p) for p in nodes]).buffer(c["width"], cap_style=2)]
    for w in c["others"]:
        shapes.append(LineString([fr.en(*p) for p in find_way(c["folder"], w)]).buffer(c["width"], cap_style=2))
    foot = unary_union(shapes)
    band = _band(ax, span[0], span[1])
    out = []
    for g in _polys(foot.intersection(band)):
        if g.area >= exclusions.MIN_AREA:
            out.append(("flatten", "%s %s river" % (c["code"], c["title"]), span[2], exclusions.ring_ll(g, fr)))
    return out
