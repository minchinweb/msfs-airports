"""R20 Beverly Bridge (1972 steel plate-girder deck, the south Highway 16 / Yellowhead carriageway): OSM way 61430014, 322 m.

NOTES.md / HANDOFF-T2.md: deck centreline and outline (way 642360969) from OSM; deck top is a quadratic through the 2018 LiDAR
first returns on the way (22.1 to 23.0 m above the 610.00 m river datum); lateral extent -8.8..+10.5 m about the way from the
outline; three lanes (11.1 m, way width tag); the City names a south-side sidewalk.  Pier stations (54, 129, 207, 280 m) and the
pier shape (tall concrete columns, single under the first two stations, twin under the last two) are read from the 12 May 2015
photograph, girder depth (3.0 m, five lines) from its proportions: all assumed.  Blue steel railing from the 2011 photograph.
Axis runs NW -> SE, t positive = north.
"""
from bridgelib import *
from t2lib import *

CODE, TITLE = "R20", "Beverly Bridge"
DATUM = 610.00
F, WAY, OUTLINE = "R20-beverly", 61430014, 642360969
PIERS = [54.0, 129.0, 207.0, 280.0]
DEPTH, SLAB = 3.0, 0.3


def build():
    fr0, ax0, _ = load_axis(F, WAY, False)
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(mid[0], mid[1])
    fr, ax, _ = load_axis(F, WAY, False, origin=(lat0, lon0))
    L = ax.L
    tlo, thi, _s0, _s1 = outline_t(F, OUTLINE, fr, ax)
    y = deck_quad(F, WAY, DATUM, False, L)
    ground = ground_fn(F, WAY, DATUM, False, L)
    m = BMesh()
    girder_deck(m, ax, 0.0, L, y, tlo, thi, ground, n_girders=5, depth=DEPTH, slab=SLAB, inner=+1, sidewalk=-1, left_sign=+1)
    for i, s in enumerate(PIERS):
        ysoff = y(s) - SLAB - DEPTH - 0.15
        yb = min(-6.0, ground(s) - 1.5)
        if i < 2:   # single wide column under a cap
            prism(m, nose_plan(ax, s, 0.0, 1.0, 2.6, 0.0, (False, False)), yb, ysoff - 1.5, CONC)
            prism(m, nose_plan(ax, s, 0.0, 1.4, 6.4, 0.0, (False, False)), ysoff - 1.5, ysoff, CONC)
        else:       # twin columns
            for t in (-3.4, 3.4):
                prism(m, nose_plan(ax, s, t, 0.9, 0.9, 0.0, (False, False)), yb, ysoff - 1.1, CONC)
            prism(m, nose_plan(ax, s, 0.0, 1.2, 6.2, 0.0, (False, False)), ysoff - 1.1, ysoff, CONC)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=DATUM, parts=[("br_r20_beverly", m)], frame=fr, axis=ax)
