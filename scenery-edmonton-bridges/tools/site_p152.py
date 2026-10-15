"""P152 Muttart stop (Valley Line, at grade): two 104 m side platforms 11.5 m apart with two tracks between, low canopies.
Platform rings: OSM ways 1157283683 (west) and 1157283685 (east), tagged shelter=yes, lit=yes.  The line runs about 49 degrees true
(SW -> NE); the R14 ramp arrives at the NE end.  Platform level 621.94 m = the 2018 ground at the stop (unverified; the stop was built
after the survey).  Canopy size and shape are assumptions (a low canopy over the middle 40 m of each platform).  Datum (y = 0) = rail
top at the platforms, alt 621.94 m.  Axis runs SW -> NE; t positive = NW (the west platform).
"""
import math
from bridgelib import *

CODE, TITLE = "P152", "Muttart stop"
RIVER = 621.94
F = "P152-muttart"
WEST = [(53.5361554, -113.4801367), (53.536772, -113.4789592)]
EAST = [(53.5360782, -113.4800218), (53.5366913, -113.4788446)]


def build():
    fr0 = Frame(53.5364, -113.4795)
    ax0 = mid_axis(fr0, WEST, EAST, n=1)
    mid = ax0.at(ax0.L / 2)
    lat0, lon0 = fr0.ll(*mid[:2])
    fr = Frame(lat0, lon0)
    ax = mid_axis(fr, WEST, EAST, n=1)
    L = ax.L
    m = BMesh()
    # ballast bed and tracks between the platforms, 4 m apart.  Same section as the R14 ramp that arrives at s = L (fill top -0.3,
    # slab -0.3..-0.18, rails to -0.02), which ends exactly here, so the two models meet flush and in the same colours.
    ribbon(m, ax, 0.0, L, -4.2, 4.2, -1.6, -0.3, CONCD, step=40.0, sw_top=BALLAST)
    for tt in (-2.0, 2.0):
        ribbon(m, ax, -6.0, L, tt - 0.9, tt + 0.9, -0.3, -0.18, CONCD)
        for r in (-0.72, 0.72):
            ribbon(m, ax, -6.0, L, tt + r - 0.04, tt + r + 0.04, -0.18, -0.02, RAILSTEEL)
    # platforms: concrete on fill, 3.5 m wide, tactile strip on the edge
    for sg in (-1, 1):
        t0, t1 = (4.0, 7.5) if sg > 0 else (-7.5, -4.0)
        ribbon(m, ax, 0.0, L, t0, t1, -1.6, 0.35, CONC, step=40.0, sw_top=CONC, sw_side=CONCD)
        te = 4.15 if sg > 0 else -4.15
        ribbon(m, ax, 0.0, L, te - 0.3, te + 0.3, 0.35, 0.37, YELLOW)
        railing(m, ax, 0.0, L, sg * 7.4, 0.35, h=1.1, post_step=4.0, sw_post=DGREY, rails=1)
        # canopy over the middle 40 m: glass roof on a steel frame, posts at the back edge
        s0, s1 = L / 2 - 20, L / 2 + 20
        ribbon(m, ax, s0, s1, sg * 4.2 - 0.0 if False else min(sg * 4.2, sg * 7.3), max(sg * 4.2, sg * 7.3), 3.3, 3.55, GLASSLT)
        for s in [s0 + i * 8.0 for i in range(6)]:
            for t in (sg * 7.0, sg * 4.6):
                beam(m, ax.p3(s, t, 0.35), ax.p3(s, t, 3.35), 0.18, 0.18, DGREY)
        # back wall of the shelter (glass screen)
        ribbon(m, ax, s0 + 4, s1 - 4, sg * 7.0 - 0.04, sg * 7.0 + 0.04, 0.35, 2.4, GLASSLT)
    # catenary poles between the tracks, contact wires
    for i in range(int(L // 36) + 1):
        s = 4 + i * 36
        beam(m, ax.p3(s, 0.0, 0.0), ax.p3(s, 0.0, 7.0), 0.3, 0.3, GREY)
        beam(m, ax.p3(s, -2.4, 6.6), ax.p3(s, 2.4, 6.6), 0.15, 0.15, GREY)
    for tt in (-2.0, 2.0):
        beam(m, ax.p3(-6.0, tt, 5.6), ax.p3(L, tt, 5.6), 0.05, 0.05, LAMP)
    # light poles at the outer platform edges
    for sg in (-1, 1):
        for s in (10.0, 30.0, 52.0, 74.0, 94.0):
            e, n = ax.en(s, sg * 7.4)
            de, dn = -ax.at(s)[3] * sg, ax.at(s)[2] * sg
            lamp(m, e, n, 0.35, 6.5, 1.2, -de, -dn)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_p152_muttart_stop", m)], frame=fr, axis=ax)
