"""N258 Grierson Hill Bridge: Grierson Hill Road over McDougall Hill Road, way 106711211 (59 m, two lanes, curbs, no sidewalk).
LiDAR: raised run 14.0 to 48.2 m on the way, width 11.5 m, deck about 6 m above the road below.  A large grey concrete column
(2 to 3 m) with W-beam guard rail stands at the roadside (street frame 5); one centre column assumed.  Light grey curved single-arm lamps.
"""
from bridgelib import *
import approach

CODE, TITLE = "N258", "Grierson Hill Bridge"
RIVER = 613.74
F, SITE, WAY = "N258-grierson", "N258-grierson", 106711211


def build():
    fr0 = Frame(53.5386, -113.4888)
    ax0 = fr0.axis(find_way(F, WAY))
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(*mid[:2])
    fr = Frame(lat0, lon0)
    ax = fr.axis(find_way(F, WAY))
    a, b, _ = run_info(SITE, WAY)
    y = deck_fit(F, WAY, RIVER, a, b)
    m = BMesh()
    slab_bridge(m, ax, a, b, 11.5, y, depth=1.6, parapet_h=0.9, rail_sw=RAILSTEEL, piers=[(a + b) / 2], pier_w=2.6,
                lamps=[(a + 6, 1), (b - 6, -1)])
    for sign, s_edge in ((-1, a), (1, b)):       # carry the road on into the hill at both ends
        approach.approach(m, fr, F, WAY, ax, s_edge, sign, y(s_edge), 11.5, RIVER)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_n258_grierson", m)], frame=fr, axis=ax)
