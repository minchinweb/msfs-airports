"""R11 Walterdale Bridge (2017): twin through-arch, 206 m, no river piers, 32 hangers, shared-use path hung on the east.

NOTES.md / OPEN-QUESTIONS.md: ribs are steel boxes 2.5 m tapering to 1.4 m, leaning ~13.5 degrees toward each other with five to
seven cross struts; 16 hangers per plane at ~10 m (first near chainage 49, last near 204); expansion joints at 14 and 246 m on way
175326660 (so the 230 m deck lies between them); crown 52.8 m above the river (LiDAR); deck 14.7 m above the river; rib feet near
chainage 32 and 229.  The rib rise above the roadway is 40 m (2019 award submission).  Rib spacing is an assumption.
Axis runs south -> north along the road way; t positive = west.
"""
import math
from bridgelib import *

CODE, TITLE = "R11", "Walterdale Bridge"
RIVER = 614.21
F = "R11-walterdale"
DECK = 14.7           # road deck top above the river (LiDAR median 629.05 - 614.21 is 14.84 with kerbs; 14.7 taken)
CROWN = 52.8          # top of the rib at the crown
FOOT = 12.5           # rib springing, a little under the road
S0, S1 = 14.0, 246.0  # deck between the expansion joints
SF0, SF1 = 27.0, 233.0
TR = 9.0              # rib plane offset at deck level
TC = 0.9              # rib plane offset at the crown


def build():
    fr0 = Frame(53.5283, -113.5017)
    ax0 = fr0.axis(find_way(F, 175326660))
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(mid[0], mid[1])
    fr = Frame(lat0, lon0)
    ax = fr.axis(find_way(F, 175326660))
    m = BMesh()
    SM = (SF0 + SF1) / 2.0
    HALF = (SF1 - SF0) / 2.0
    rise = CROWN - FOOT

    def rib_y(s):
        x = (s - SM) / HALF
        return FOOT + rise * (1 - x * x)

    def rib_t(y, sg):
        return sg * (TR - (TR - TC) * max(0.0, y - FOOT) / rise)

    # deck: steel box-girder edge beams + orthotropic deck, asphalt, barriers
    ribbon(m, ax, S0, S1, -9.2, 9.2, DECK - 1.5, DECK, CONCD, step=30.0, sw_top=ASPHALT, sw_bot=RAILSTEEL, sw_side=RAILSTEEL)
    ribbon(m, ax, S0, S1, 5.6, 8.6, DECK, DECK + 0.12, CONC, step=30.0)                    # west footway
    for tt in (-8.9, 5.5, 8.9):
        ribbon(m, ax, S0, S1, tt - 0.18, tt + 0.18, DECK, DECK + 0.95, CONC, step=30.0)
    railing(m, ax, S0, S1, 8.9, DECK + 0.95, h=0.6, post_step=3.0, sw_post=RAILSTEEL, rails=1, step=30.0)
    railing(m, ax, S0, S1, -8.9, DECK + 0.95, h=0.6, post_step=3.0, sw_post=RAILSTEEL, rails=1, step=30.0)
    # abutments and the road approach slabs
    for s, sg in ((S0, -1), (S1, 1)):
        ribbon(m, ax, s - 3.0, s + 3.0, -19.0, 11.0, -3.0, DECK - 1.5, CONC)
    # shared-use path: its own mapped way (it bows away from the road); floor-beam extensions every 10 m, delta piers at the banks
    pax = fr.axis(find_way(F, 451293733))
    PATH_Y = DECK - 1.7
    ps0, ps1 = 12.0, pax.L - 12.0
    ribbon(m, pax, ps0, ps1, -4.0, 4.0, PATH_Y - 0.6, PATH_Y, CONC, step=10.0)
    railing(m, pax, ps0, ps1, -4.0, PATH_Y, h=1.4, post_step=3.0, sw_post=RAILSTEEL, rails=2, step=10.0)
    railing(m, pax, ps0, ps1, 4.0, PATH_Y, h=1.4, post_step=3.0, sw_post=RAILSTEEL, rails=2, step=10.0)
    hang = [49.0 + i * (204.0 - 49.0) / 15.0 for i in range(16)]
    for s in hang:
        be, bn = ax.en(s, -9.2)
        sp_, tp_ = project(pax, be, bn)
        pe, pn = pax.en(sp_, 0.0)
        beam(m, (be, DECK - 1.0, bn), (pe, PATH_Y - 0.3, pn), 0.5, 0.7, RAILSTEEL)
        beam(m, ax.p3(s, -9.2, DECK - 0.8), ax.p3(s, 9.2, DECK - 0.8), 0.5, 0.8, RAILSTEEL)
    for s in (ps0 + 2, ps1 - 2, pax.L * 0.3, pax.L * 0.7):
        e, n = pax.en(s, 0.0)
        m.box(e - 0.7, e + 0.7, -2.0, PATH_Y - 0.6, n - 0.7, n + 0.7, CONCD)
    # support legs (concrete) under the four rib feet, then the ribs
    for s in (SF0, SF1):
        for sg in (-1, 1):
            e, n = ax.en(s, sg * TR)
            m.box(e - 2.4, e + 2.4, -4.0, FOOT, n - 3.0, n + 3.0, CONC)
    N = 40
    for sg in (-1, 1):
        for i in range(N):
            s0 = SF0 + (SF1 - SF0) * i / N
            s1 = SF0 + (SF1 - SF0) * (i + 1) / N
            y0, y1 = rib_y(s0), rib_y(s1)
            u = abs((s0 + s1) / 2 - SM) / HALF
            w = 1.4 + 1.1 * u
            lat = ax.p3(0, 1, 0)
            beam(m, ax.p3(s0, rib_t(y0, sg), y0), ax.p3(s1, rib_t(y1, sg), y1), w, w, WHITEST, (-ax.at((s0 + s1) / 2)[3], 0.0, ax.at((s0 + s1) / 2)[2]))
        # hangers: thin white pipes from the rib to the deck edge
        for s in hang:
            y = rib_y(s)
            beam(m, ax.p3(s, rib_t(y, sg), y), ax.p3(s, sg * 8.9, DECK + 0.1), 0.22, 0.22, WHITEST)
    # cross struts between the ribs, seven of them above the deck
    for s in (SM - 76, SM - 52, SM - 30, SM - 9, SM + 9, SM + 30, SM + 52, SM + 76):
        y = rib_y(s)
        beam(m, ax.p3(s, rib_t(y, -1), y), ax.p3(s, rib_t(y, 1), y), 0.9, 0.9, WHITEST)
    # lamps: slender single-arm poles outside the west barrier
    for i in range(8):
        s = S0 + 12 + i * 28
        e, n = ax.en(s, 8.6)
        de, dn = -ax.at(s)[3], ax.at(s)[2]
        lamp(m, e, n, DECK, 9.0, 2.2, -de, -dn)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_r11_walterdale", m)], frame=fr, axis=ax)
