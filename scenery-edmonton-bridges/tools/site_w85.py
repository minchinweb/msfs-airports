"""W85 Fox Drive / Campbell Bridge (City of Edmonton, 1969; Fox Drive over Whitemud Creek): about 89 m, three lanes each way.

NOTES.md / HANDOFF-T2.md.  Axis: midway between the south carriageway (OSM way 25475831, eastbound) and the north carriageway
(25475833 + 944470767, westbound), run west -> east, t positive = north.  Sourced: plan and length (OSM, 89.1 m), carriageways
about 9.4 m apart, three lanes each way, 70 km/h, a concrete south sidewalk (way 582712471) and a north shared-use path (way
27265227), deck level (quadratic through the 2018 LiDAR first returns on the south way, 9.5 to 10.1 m above the creek surface),
the steel-pipe-rail and lamp detail seen in the 2 August 2012 photograph, median concrete barrier.  Deck overall width
(-16.0 .. +17.5 m about the axis) read from the 2019 aerial.  Assumed (flagged in HANDOFF-T2.md): everything under the deck: three
equal spans (29.7 m), two bents of six round columns, concrete girders 1.5 m deep at 2.9 m spacing, abutments at the LiDAR ground
crossing.  Colour: concrete, beige-tan railing.
"""
from bridgelib import *
from t2lib import *

CODE, TITLE = "W85", "Fox Drive Campbell Bridge"
DATUM = 618.30
F, SOUTH = "W85-fox-drive", 25475831
NORTH = (25475833, 944470767)
SLAB, DEPTH = 0.30, 1.5
TLO, THI = -16.0, 17.5
BENT_T = [-13.5, -8.0, -2.5, 3.0, 8.5, 14.0]


def build():
    nS = find_way(F, SOUTH)
    nN = (find_way(F, NORTH[0]) + find_way(F, NORTH[1])[1:])[::-1]
    fr0 = Frame(*nS[0])
    ax0 = mid_axis(fr0, nS, nN)
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(mid[0], mid[1])
    fr = Frame(lat0, lon0)
    ax = mid_axis(fr, nS, nN)
    L = ax.L
    y = deck_quad(F, SOUTH, DATUM, False, L)
    ground = ground_fn(F, SOUTH, DATUM, False, L)
    m = BMesh()
    ribbon(m, ax, 0.0, L, TLO, THI, lambda s: y(s) - SLAB, y, CONC, step=10.0, sw_top=ASPHALT, sw_bot=CONCD)
    ng = 12
    tg = [TLO + 1.2 + i * (THI - TLO - 2.4) / (ng - 1) for i in range(ng)]
    for t in tg:
        ribbon(m, ax, 0.0, L, t - 0.25, t + 0.25, lambda s: y(s) - SLAB - DEPTH, lambda s: y(s) - SLAB, CONC, step=10.0, sw_bot=CONCD)
    # lanes: south three eastbound (t -1.0 .. -9.0, edge at -10), north three westbound
    for sg in (-1, 1):
        for j in (1, 2):
            off = sg * (1.2 + j * 2.9)
            s = 2.0
            while s + 3.0 < L - 2:
                ribbon(m, ax, s, s + 3.0, off - 0.07, off + 0.07, lambda q: y(q), lambda q: y(q) + 0.02, WHITE, step=None, caps=False)
                s += 9.0
        ribbon(m, ax, 0.0, L, sg * 10.2 - 0.08, sg * 10.2 + 0.08, y, lambda s: y(s) + 0.02, WHITE, step=12.0, caps=False)
        ribbon(m, ax, 0.0, L, sg * 0.9 - 0.08, sg * 0.9 + 0.08, y, lambda s: y(s) + 0.02, YELLOWR, step=12.0, caps=False)
    ribbon(m, ax, 0.0, L, -0.45, 0.45, y, lambda s: y(s) + 1.0, CONC, step=12.0)           # median barrier
    # curbs, sidewalk (south, 2.0 m) and shared path (north, 3.0 m) with the beige pipe railing (2012 photograph)
    for t0, t1, edge, sg in ((-14.0, -11.0, TLO, -1), (11.0, 14.5, THI, 1)):
        ribbon(m, ax, 0.0, L, min(t0, t1), max(t0, t1), y, lambda s: y(s) + 0.15, CONC, step=12.0, sw_top=CONC)
        ribbon(m, ax, 0.0, L, sg * 10.6 - 0.2, sg * 10.6 + 0.2, y, lambda s: y(s) + 0.4, CONC, step=12.0)
    for edge in (TLO + 0.3, THI - 0.3):
        railing(m, ax, 0.0, L, edge, lambda s: y(s) + 0.15, h=1.4, post_step=2.5, sw_post=TAN, rails=3, step=12.0, post_w=0.14)
    # lamps on the outer edges, every 33 m, curving inward
    for sg, off in ((-1, TLO + 0.6), (1, THI - 0.6)):
        s = 12.0
        while s < L:
            e, n = ax.en(s, off)
            de, dn = -ax.at(s)[3], ax.at(s)[2]
            lamp(m, e, n, y(s), 9.0, 2.2, -sg * de, -sg * dn)
            s += 33.0
    # abutments
    for s, sg in ((0.0, -1), (L, 1)):
        yb = min(y(s) - SLAB - DEPTH - 1.0, ground(s) - 1.2)
        ribbon(m, ax, s - (1.8 if sg < 0 else 0.0), s + (0.0 if sg < 0 else 1.8), TLO - 0.5, THI + 0.5, yb, y(s) - SLAB, CONCD)
    # two bents: cap beam and six round columns
    for s in (L / 3, 2 * L / 3):
        ysoff = y(s) - SLAB - DEPTH - 0.1
        yb = min(-4.0, ground(s) - 1.5)
        prism(m, nose_plan(ax, s, 0.5 * (TLO + THI) * 0.97, 0.7, 0.5 * (THI - TLO) - 0.9, 0.0, (False, False)), ysoff - 1.0, ysoff, CONC)
        for t in BENT_T:
            e, n = ax.en(s, t)
            cyl(m, e, n, 0.5, 0.5, yb, ysoff - 1.0, PIERBEIGE, n=12)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=DATUM, parts=[("br_w85_fox_drive", m)], frame=fr, axis=ax)
