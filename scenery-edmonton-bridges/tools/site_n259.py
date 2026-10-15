"""N259 Rossdale Road Bridge over McDougall Hill Road, way 37120045 (49 m; raised run 12.9 to 42.2 m, width 13.0 m).
Street frame: three lanes, steel rail on tan concrete posts at both edges, no sidewalk, no lamps on the deck.  Abutments only (assumed;
the brief lists piers as open).
"""
from bridgelib import *

CODE, TITLE = "N259", "Rossdale Road Bridge"
RIVER = 613.74
F, SITE, WAY = "N259-rossdale-mcdougall", "N259-rossdale-mcdougall", 37120045


def build():
    fr0 = Frame(53.5377, -113.4931)
    ax0 = fr0.axis(find_way(F, WAY))
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(*mid[:2])
    fr = Frame(lat0, lon0)
    ax = fr.axis(find_way(F, WAY))
    a, b, _ = run_info(SITE, WAY)
    y = deck_fit(F, WAY, RIVER, a, b)
    m = BMesh()
    slab_bridge(m, ax, a, b, 13.0, y, depth=1.5, parapet_h=0.7, parapet_sw=SAND, rail_sw=RAILSTEEL)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_n259_rossdale", m)], frame=fr, axis=ax)
