"""R9 Dudley B. Menzies Bridge (1992): Capital Line LRT, two tracks on a concrete segmental box girder, hung walkway.

NOTES.md: 530 m seven-span box (three river spans, walkway hung under them), a two-span slab structure at the north abutment and a
four-span slab structure at the south, single lollipop columns, ~4.5 m deep box, catenary poles on the centreline.  The span split
(55, 63, 3 x ~98, 63, 55) is an assumption fitted to 530 m and the 294 m walkway; pier stations are not published.
Deck top: the 2018 DSM along the track reads a constant 638.2 m (rail top), so the deck top is taken as 638.0 m.
Axis runs south -> north, midway between the two track ways; t positive = west.
"""
import math
from bridgelib import *

CODE, TITLE = "R9", "Dudley B. Menzies Bridge"
RIVER = 614.92
F = "R9-menzies"
DECK_TOP = 638.0 - RIVER


def build():
    fr0 = Frame(53.531, -113.512)
    ax0 = mid_axis(fr0, find_way(F, 700467672), find_way(F, 37834327))
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(mid[0], mid[1])
    fr = Frame(lat0, lon0)
    ax = mid_axis(fr, find_way(F, 700467672), find_way(F, 37834327))
    L = ax.L
    walk = [fr.en(*p) for p in find_way(F, 424285379)]
    ws = [project(ax, *p) for p in walk]
    sw0, sw1 = min(s for s, t in ws), max(s for s, t in ws)
    tw = sum(t for s, t in ws) / len(ws)
    # span layout: 3 river spans under the walkway, 2 + 2 box spans each side, slab spans out to the portals
    river = (sw1 - sw0) / 3.0
    box0, box1 = sw0 - 63.0 - 55.0, sw1 + 63.0 + 55.0
    piers = [box0, box0 + 55.0, box0 + 118.0, sw0 + river, sw0 + 2 * river, sw1, sw1 + 63.0, box1]
    piers = sorted(set(round(p, 2) for p in piers))
    south = [box0 * i / 4.0 for i in range(0, 4)]                   # four slab spans at the south abutment
    north = [box1 + (L - box1) * i / 2.0 for i in range(1, 2)]    # two at the north (one pier between)
    slab_piers = south[1:] + north
    ground = ground_profile(F, 700467672, RIVER)
    m = BMesh()
    # deck: box girder over the box spans, shallower slab elsewhere
    def soff(s):
        return DECK_TOP - 4.5 if box0 <= s <= box1 else DECK_TOP - 1.4
    ribbon(m, ax, 0.0, L, -4.8, 4.8, DECK_TOP - 0.45, DECK_TOP, CONC, step=12.0, sw_bot=CONC, sw_side=CONC)
    ribbon(m, ax, box0, box1, -2.4, 2.4, DECK_TOP - 4.5, DECK_TOP - 0.45, CONCD, step=12.0)
    for a, b in ((0.0, box0), (box1, L)):
        ribbon(m, ax, a, b, -3.8, 3.8, DECK_TOP - 1.4, DECK_TOP - 0.45, CONCD, step=12.0)
    # parapets, direct-fixation rails, catenary
    for tt in (-4.7, 4.7):
        ribbon(m, ax, 0.0, L, tt - 0.15, tt + 0.15, DECK_TOP, DECK_TOP + 1.0, CONC, step=12.0)
    for tt in (-2.0, 2.0):
        ribbon(m, ax, 0.0, L, tt - 0.9, tt + 0.9, DECK_TOP, DECK_TOP + 0.12, CONCD, step=12.0)
        for r in (-0.72, 0.72):
            ribbon(m, ax, 0.0, L, tt + r - 0.04, tt + r + 0.04, DECK_TOP + 0.12, DECK_TOP + 0.28, RAILSTEEL, step=12.0)
    k = int(L // 42)
    for i in range(k + 1):
        s = 6 + i * 42
        if s > L - 4:
            break
        beam(m, ax.p3(s, 0, DECK_TOP), ax.p3(s, 0, DECK_TOP + 6.4), 0.35, 0.35, LAMP)
        beam(m, ax.p3(s, -2.6, DECK_TOP + 5.9), ax.p3(s, 2.6, DECK_TOP + 5.9), 0.14, 0.14, LAMP)
    st = ax.stations(0.0, L, 10.0)
    for tt in (-2.0, 2.0):
        for a, b in zip(st[:-1], st[1:]):
            beam(m, ax.p3(a, tt, DECK_TOP + 5.2), ax.p3(b, tt, DECK_TOP + 5.2), 0.05, 0.05, LAMP)
    # lollipop columns under every pier station
    for s in piers + slab_piers:
        g = ground(s)
        top = soff(s) if s in piers else DECK_TOP - 1.4
        e, n = ax.en(s, 0.0)
        if s in piers:
            cyl(m, e, n, 1.7, 1.55, g - 3.0, top - 2.6, CONCD, n=16)
            cyl(m, e, n, 1.55, 3.4, top - 2.6, top - 0.1, CONC, n=16)
        else:
            cyl(m, e, n, 1.2, 1.2, g - 3.0, top - 0.1, CONCD, n=12)
    # walkway hung under the river spans: blue deck 3.2 m wide, 3 m below the soffit, with railings and hangers
    yw = DECK_TOP - 4.5 - 3.4
    ribbon(m, ax, sw0, sw1, tw - 1.6, tw + 1.6, yw - 0.4, yw, BLUEWALK, step=15.0)
    for tt in (tw - 1.6, tw + 1.6):
        railing(m, ax, sw0, sw1, tt, yw, h=1.2, post_step=3.0, sw_post=BLUEWALK, sw_rail=BLUEWALK, rails=2, step=15.0)
    for i in range(int((sw1 - sw0) // 18) + 1):
        s = sw0 + 4 + i * 18
        if s < sw1:
            beam(m, ax.p3(s, tw - 1.0, yw), ax.p3(s, tw - 1.0, DECK_TOP - 4.5), 0.18, 0.18, BLUEWALK)
            beam(m, ax.p3(s, tw + 1.0, yw), ax.p3(s, tw + 1.0, DECK_TOP - 4.5), 0.18, 0.18, BLUEWALK)
    # tunnel portals at both ends: dark opening in a concrete head wall
    for s, sg in ((0.0, -1), (L, 1)):
        beam(m, ax.p3(s, 0, DECK_TOP - 3.0), ax.p3(s + sg * 0.6, 0, DECK_TOP - 3.0), 9.0, 0.1, DARK)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_r9_menzies", m)], frame=fr, axis=ax)
