"""R20 Beverly Bridge (1972 steel plate-girder deck, the south Highway 16 / Yellowhead carriageway): OSM way 61430014, 321.5 m.

Alberta Transportation bridge record, file 77132 (BEVERLY BRDG, B143; Structure-Export.csv, inspected 2023-08-16): five spans
54.9, 70.1, 70.1, 70.1, 54.9 m (nominal 320.1 m), gross deck width 19.2 m, total clear roadway 16.8 m, concrete piers and caps.
The record's span set is symmetric, so the interior piers sit at 54.9, 125.0, 195.1 and 265.2 m from either abutment.  The deck is
the 320.1 m between abutments, centred on the middle of the OSM way (0.7 m trimmed at each end); s = 0 is the OSM way's NW end.
Width: 19.2 m gross, centred on the OSM outline's middle (way 642360969).  South: 1.8 m sidewalk (City names a south-side sidewalk)
and the 2.4 m gross less clear roadway is split 1.8 m south / 0.6 m north.  Clear roadway 16.8 m = 11.1 m carriageway (three
3.7 m lanes, OSM width tag) plus 2.85 m shoulders each side.  Girder depth (3.0 m, five lines), slab and the pier shape
(tall concrete columns, single under the first two piers, twin under the last two) are assumed, not in the record.
Blue steel railing from the 2011 photograph.  Axis runs NW -> SE, t positive = north.
"""
from bridgelib import *
from t2lib import *

CODE, TITLE = "R20", "Beverly Bridge"
DATUM = 610.00
F, WAY, OUTLINE = "R20-beverly", 61430014, 642360969
SPANS = [54.9, 70.1, 70.1, 70.1, 54.9]          # Alberta file 77132
DECK_LEN = 320.1                                 # nominal bridge length, file 77132
GROSS_W, CLEAR_W = 19.2, 16.8                    # file 77132
CARRIAGE = 11.1                                  # three 3.7 m lanes (OSM width tag); 2 x 2.85 m shoulders make up the clear roadway
SIDEWALK_S, PARAPET_N = 1.8, 0.6                 # gross less clear = 2.4 m, split south / north
assert abs(CARRIAGE + 2 * 2.85 - CLEAR_W) < 1e-9 and abs(SIDEWALK_S + PARAPET_N + CLEAR_W - GROSS_W) < 1e-9
PIERS = [sum(SPANS[:i]) for i in range(1, len(SPANS))]   # 54.9, 125.0, 195.1, 265.2 from the first abutment
DEPTH, SLAB = 3.0, 0.3


def build():
    fr0, ax0, _ = load_axis(F, WAY, False)
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(mid[0], mid[1])
    fr, ax, _ = load_axis(F, WAY, False, origin=(lat0, lon0))
    L = ax.L
    s0 = (L - DECK_LEN) / 2                      # first abutment (NW), deck trimmed evenly from the OSM way ends
    s1 = s0 + DECK_LEN
    olo, ohi, _a, _b = outline_t(F, OUTLINE, fr, ax)
    om = (olo + ohi) / 2                         # outline centre, the deck's lateral centre
    tlo, thi = om - GROSS_W / 2, om + GROSS_W / 2
    t_c = (tlo + SIDEWALK_S + thi - PARAPET_N) / 2   # centre of the clear roadway, and of the carriageway
    y = deck_quad(F, WAY, DATUM, False, L)
    ground = ground_fn(F, WAY, DATUM, False, L)
    m = BMesh()
    girder_deck(m, ax, s0, s1, y, tlo, thi, ground, n_girders=5, depth=DEPTH, slab=SLAB, inner=+1, sidewalk=-1, left_sign=+1,
                sidewalk_w=SIDEWALK_S, carriage=CARRIAGE, t_c=t_c)
    for i, st in enumerate(PIERS):
        s = s0 + st
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
