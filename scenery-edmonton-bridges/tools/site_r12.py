"""R12 James MacDonald Bridge (1971): two 3-lane concrete girder carriageways on 97/98 Avenue, 340 m.

geometry.json: way 25455305 (westbound) and 25455308 (eastbound), 11.1 m slabs, 12 to 19 m apart.  Street frames: grey concrete
parapet ~1 m with a tan open railing (1.4 to 1.5 m overall), twin-arm lamps along the deck, no sidewalk.  Photos: haunched girders,
wall piers in the channel.  Pier stations are NOT published: five equal spans are assumed (flagged in the handoff).
Deck top 17.6 m above the 2018 river (613.73 m; DSM 631.52).
"""
import math
from bridgelib import *

CODE, TITLE = "R12", "James MacDonald Bridge"
RIVER = 613.73
F = "R12-james-macdonald"
DECK = 17.6


def carriage(m, fr, way):
    ax = fr.axis(find_way(F, way))
    L = ax.L
    n = 5
    piers = [L * i / n for i in range(1, n)]
    def soff(s):  # girder depth: 1.9 m at mid-span, 3.4 m over a pier
        d = min([abs(s - p) for p in piers] + [L / n / 2])
        return DECK - (1.9 + 1.5 * max(0.0, 1 - d / 12.0))
    ribbon(m, ax, 0.0, L, -5.55, 5.55, soff, DECK, CONCD, step=6.0, sw_top=ASPHALT, sw_side=CONC)
    for sg in (-1, 1):
        tc = sg * 5.35
        ribbon(m, ax, 0.0, L, tc - 0.2, tc + 0.2, DECK, DECK + 1.0, CONC, step=30.0)
        railing(m, ax, 0.0, L, tc, DECK + 1.0, h=0.5, post_step=2.5, sw_post=SAND, sw_rail=SAND, rails=1, step=30.0)
    lane_dashes(m, ax, 0.0, L, -5.15, 5.15, 3, DECK)    # one-way, three lanes: dashed white lines
    for p in piers:
        for tt in (-2.2, 2.2):
            e, nn = ax.en(p, tt)
            prism(m, nose_plan(ax, p, tt, 1.1, 1.6, 0.0, (False, False)), -5.0, soff(p) - 0.2, CONCD)
        prism(m, nose_plan(ax, p, 0.0, 1.5, 4.6, 0.0, (False, False)), soff(p) - 1.2, soff(p), CONC)
    for s, sg in ((0.0, -1), (L, 1)):
        ribbon(m, ax, s - (3.0 if sg < 0 else 0.0), s + (0.0 if sg < 0 else 3.0), -6.0, 6.0, -3.0, DECK - 1.8, CONC)
    for i in range(int(L // 36)):
        s = 18 + i * 36
        e, nn = ax.en(s, 5.6)
        de, dn = -ax.at(s)[3], ax.at(s)[2]
        lamp(m, e, nn, DECK + 1.0, 9.5, 2.0, -de * (1 if True else -1), -dn)
    return ax


def build():
    fr0 = Frame(53.536, -113.488)
    ax0 = fr0.axis(find_way(F, 25455305))
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(*mid[:2])
    fr = Frame(lat0, lon0)
    m = BMesh()
    ax = carriage(m, fr, 25455305)
    carriage(m, fr, 25455308)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_r12_james_macdonald", m)], frame=fr, axis=ax)
