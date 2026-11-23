"""R21 Clover Bar Bridge (the present north Highway 16 / Yellowhead carriageway, 2001 girder): OSM way 61431758, 355.1 m.

Alberta Transportation bridge record, file 02032 (CLOVERBAR BRIDGE, B292; Structure-Export.csv, inspected 2025-09-14, IN SERVICE,
first in service 2001): five spans 55, 70, 70, 70, 55 m (nominal 320 m, max span 70 m), gross deck width 17.5 m, total clear
roadway 16.6 m, concrete piers and caps, pile-founded abutments.  The record's span set is symmetric, so the interior piers sit at
55, 125, 195 and 265 m from either abutment.  The deck is the 320 m between abutments, centred on the middle of the OSM way (17.55 m
trimmed at each end); s = 0 is the OSM way's NW end, as in R20.  Width: 17.5 m gross, centred on the middle of the OSM outline
(way 642360970, -6.4 to +10.8 m about the way).  Clear roadway 16.6 m is centred on the deck and the carriageway is centred on it.
Assumed, not in the record: the 11.1 m carriageway (three 3.7 m lanes; the way has no width tag), 2.75 m shoulders each side, the
0.45 m edges, girder depth (2.8 m, five lines), slab, pier shape (wall piers under a cap), no sidewalk, blue steel railing on the
north edge (from the 2011 photograph taken from this deck).  Axis runs NW -> SE, t positive = north.
"""
from bridgelib import *
from t2lib import *

CODE, TITLE = "R21", "Clover Bar Bridge"
DATUM = 610.00
F, WAY, OUTLINE = "R21-clover-bar", 61431758, 642360970
SPANS = [55.0, 70.0, 70.0, 70.0, 55.0]          # Alberta file 02032
DECK_LEN = 320.0                                 # nominal bridge length, file 02032
GROSS_W, CLEAR_W = 17.5, 16.6                    # file 02032
CARRIAGE = 11.1                                  # ASSUMED: three 3.7 m lanes; no width tag on the way, no lane width published
EDGE = (GROSS_W - CLEAR_W) / 2                   # 0.45 m each side between the clear roadway and the deck edge
assert abs(CARRIAGE + 2 * 2.75 - CLEAR_W) < 1e-9  # ASSUMED: 2.75 m shoulders each side
PIERS = [sum(SPANS[:i]) for i in range(1, len(SPANS))]   # 55, 125, 195, 265 from the first abutment
DEPTH, SLAB = 2.8, 0.3


def build():
    fr0, ax0, _ = load_axis(F, WAY, True)
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(mid[0], mid[1])
    fr, ax, _ = load_axis(F, WAY, True, origin=(lat0, lon0))
    L = ax.L
    s0 = (L - DECK_LEN) / 2                      # first abutment (NW), deck trimmed evenly from the OSM way ends
    s1 = s0 + DECK_LEN
    olo, ohi, _a, _b = outline_t(F, OUTLINE, fr, ax)
    om = (olo + ohi) / 2                         # outline centre, the deck's lateral centre
    tlo, thi = om - GROSS_W / 2, om + GROSS_W / 2
    t_c = om                                     # clear roadway, carriageway and piers are centred on the deck
    y = deck_quad(F, WAY, DATUM, True, L)
    ground = ground_fn(F, WAY, DATUM, True, L)
    m = BMesh()
    girder_deck(m, ax, s0, s1, y, tlo, thi, ground, n_girders=5, depth=DEPTH, slab=SLAB, inner=-1, sidewalk=0, left_sign=-1,
                carriage=CARRIAGE, t_c=t_c)
    for st in PIERS:
        s = s0 + st
        ysoff = y(s) - SLAB - DEPTH - 0.15
        yb = min(-6.0, ground(s) - 1.5)
        prism(m, nose_plan(ax, s, t_c, 0.8, 4.6, 0.9), yb, ysoff - 1.3, PIERBEIGE)
        prism(m, nose_plan(ax, s, t_c, 1.3, GROSS_W / 2, 0.0, (False, False)), ysoff - 1.3, ysoff, CONCD)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=DATUM, parts=[("br_r21_clover_bar", m)], frame=fr, axis=ax)
