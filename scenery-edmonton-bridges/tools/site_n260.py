"""N260 Scona / Connors roadworks on the south bank: five short road decks (B126 and neighbours), each a girder slab on abutments.
Street frames: concrete parapet 0.9 to 1 m with a metal top rail, no sidewalk, curved single-arm lamps at the outside edge.
Widths are the LiDAR raised widths where a deck stands alone and an assumed 10 m / 8 m where several merge (G116, N260, R8 decks were
not separated).  Each deck follows its OSM way and its measured raised run.
"""
from bridgelib import *
import approach

CODE, TITLE = "N260", "Scona / Connors road bridges"
RIVER = 613.66
F, SITE = "N260-scona-connors", "N260-scona-connors"
DECKS = [(22959547, 9.8), (34388891, 10.0), (22916470, 10.0), (106711204, 10.0), (106711230, 8.0)]


def build():
    fr0 = Frame(53.5348, -113.4838)
    ax0 = fr0.axis(find_way(F, 22916470))
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(*mid[:2])
    fr = Frame(lat0, lon0)
    m = BMesh()
    ax = None
    for way, w in DECKS:
        a_ = fr.axis(find_way(F, way))
        ax = ax or a_
        a, b, _ = run_info(SITE, way)
        slab_bridge(m, a_, a, b, w, deck_fit(F, way, RIVER, a, b), depth=1.7, parapet_h=0.95, rail_sw=RAILSTEEL,
                    piers=[(a + b) / 2] if b - a > 60 else [], lamps=[(a + 8, 1), (b - 8, 1)])
        yf = deck_fit(F, way, RIVER, a, b)
        for sign, s_edge in ((-1, a), (1, b)):       # carry each road on into the hill
            approach.approach(m, fr, F, way, a_, s_edge, sign, yf(s_edge), w, RIVER, maxlen=70.0)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_n260_scona_connors", m)], frame=fr, axis=ax)
