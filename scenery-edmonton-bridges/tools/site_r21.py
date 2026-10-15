"""R21 Clover Bar Bridge (1953 original span, the north Highway 16 / Yellowhead carriageway): OSM way 61431758, 355 m.

The way runs SE -> NW; the axis here is reversed (NW -> SE, t positive = north) so it lines up with R20.  Deck top is a quadratic
through the 2018 LiDAR first returns (22.5 to 25.3 m above the 610.00 m datum, rising to the NW); lateral extent -6.4..+10.8 m
about the way from the outline (way 642360970), which is 344.5 m long.  Sourced: all of that, three lanes.  Assumed (flagged in
HANDOFF-T2.md): pier stations (the same fractions of the span as the 2015-photo reading on R20, abutments at the LiDAR ground
crossing), tan wall piers with round noses (the 2015 photograph shows wall piers on the far deck), girder depth 2.8 m, no
sidewalk, blue 3-rail steel railing as in the 2011 photograph taken from this deck.
"""
from bridgelib import *
from t2lib import *

CODE, TITLE = "R21", "Clover Bar Bridge"
DATUM = 610.00
F, WAY, OUTLINE = "R21-clover-bar", 61431758, 642360970
DEPTH, SLAB = 2.8, 0.3
A0, A1 = 10.8, 333.8                       # LiDAR ground crossing of the soffit, NW-based chainage
PIERS = [A0 + f * (A1 - A0) for f in (0.168, 0.401, 0.644, 0.871)]


def build():
    fr0, ax0, _ = load_axis(F, WAY, True)
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(mid[0], mid[1])
    fr, ax, _ = load_axis(F, WAY, True, origin=(lat0, lon0))
    L = ax.L
    tlo, thi, s0, s1 = outline_t(F, OUTLINE, fr, ax)
    y = deck_quad(F, WAY, DATUM, True, L)
    ground = ground_fn(F, WAY, DATUM, True, L)
    m = BMesh()
    girder_deck(m, ax, s0, s1, y, tlo, thi, ground, n_girders=5, depth=DEPTH, slab=SLAB, inner=-1, sidewalk=0, left_sign=-1)
    for s in PIERS:
        ysoff = y(s) - SLAB - DEPTH - 0.15
        yb = min(-6.0, ground(s) - 1.5)
        prism(m, nose_plan(ax, s, 0.0, 0.8, 4.6, 0.9), yb, ysoff - 1.3, PIERBEIGE)
        prism(m, nose_plan(ax, s, 0.0, 1.3, 5.6, 0.0, (False, False)), ysoff - 1.3, ysoff, CONCD)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=DATUM, parts=[("br_r21_clover_bar", m)], frame=fr, axis=ax)
