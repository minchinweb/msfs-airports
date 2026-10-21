"""R13 Low Level Bridge: two riveted Pratt through-truss bridges side by side (1900 downstream/east = northbound, 1948 upstream/west
= southbound), four 53 m spans each, three river piers each.

NOTES.md: spans 4 x 53 m, 7 panels (HistoricBridges); piers read from the aerial on way 31882107 at 52.4, 105.3 and 158.4 m;
truss centrelines 7.925 m apart (1980 widening of the NB span); one outer sidewalk per bridge with a pale green diamond-lattice
railing; deck curbs with a steel W-beam rail; street frames show a rust-brown truss line and a pale sea-green one.  Colours: NB sage
green, SB rust-brown with the other bridge's floor colour (frames disagree).  Truss depth (9 m) is an assumption.
Both axes run south -> north; t positive = west (left).  Deck top 17.0 m above the 2018 river (613.74 m).
"""
import math
from bridgelib import *

CODE, TITLE = "R13", "Low Level Bridge"
RIVER = 613.74
F = "R13-low-level"
DECK = 17.0
YB = 16.0
TT = 3.96
SUP = [-0.4, 52.4, 105.3, 158.4, 212.4]


def one(m, fr, way, reverse, sw_truss, sw_floor, outer):
    nodes = find_way(F, way)
    if reverse:
        nodes = nodes[::-1]
    ax = fr.axis(nodes)
    L = ax.L
    k = L / 213.1
    sup = [s * k if 0 < s < 212 else s for s in SUP]
    for a, b in zip(sup[:-1], sup[1:]):
        through_truss_span(m, ax, a, b, TT, YB, 7, lambda f: 9.0, kind="pratt", sw=sw_truss, sw_web=sw_truss, chord=(0.7, 0.8), web=(0.38, 0.45))
    ribbon(m, ax, 0.0, L, -TT - 0.1, TT + 0.1, DECK - 0.8, DECK, ASPHALT, step=40.0, sw_side=CONCD, sw_bot=sw_floor)
    lane_dashes(m, ax, 0.0, L, -TT + 0.45, TT - 0.45, 2, DECK)   # one-way, two lanes
    for sg in (-1, 1):                          # curbs 0.75 m with a steel W-beam rail on top
        tc = sg * (TT - 0.45)
        ribbon(m, ax, 0.0, L, tc - 0.25, tc + 0.25, DECK, DECK + 0.75, CONC, step=40.0)
        ribbon(m, ax, 0.0, L, tc - 0.05, tc + 0.05, DECK + 0.75, DECK + 1.1, RAILSTEEL, step=40.0)
    to = outer * (TT + 0.4)                     # outer sidewalk with the lattice railing
    ribbon(m, ax, 0.0, L, min(to, to + outer * 2.4), max(to, to + outer * 2.4), DECK - 0.6, DECK - 0.3, CONC, step=40.0)
    railing(m, ax, 0.0, L, outer * (TT + 2.8), DECK - 0.3, h=1.3, post_step=2.4, sw_post=sw_truss, rails=3, step=40.0, post_w=0.2)
    for s in [i * 7.5 for i in range(int(L // 7.5) + 1)]:
        beam(m, ax.p3(s, outer * TT, YB - 0.5), ax.p3(s, outer * (TT + 2.8), DECK - 0.6), 0.3, 0.45, sw_floor)
    for a, b in zip(sup[1:-1], sup[1:-1]):
        s = a
        top = YB - 0.9
        prism(m, nose_plan(ax, s, 0.0, 1.6, 4.6, 1.8), -6.0, top, PIERBEIGE)
        prism(m, nose_plan(ax, s, 0.0, 1.9, 4.9, 0.0, (False, False)), top - 0.6, top, CONC)
    for s, sg in ((sup[0], -1), (sup[-1], 1)):
        ribbon(m, ax, s - (1.8 if sg < 0 else 0.4), s + (0.4 if sg < 0 else 1.8), -TT - 2.6, TT + 2.6, -3.0, YB - 0.9, CONC)
    return ax


def build():
    fr0 = Frame(53.538, -113.487)
    mids = [fr0.axis(find_way(F, 31882107)).at(106)[:2]]
    lat0, lon0 = fr0.ll(*mids[0])
    fr = Frame(lat0, lon0)
    m = BMesh()
    ax = one(m, fr, 31882107, False, SEAGREEN, SEAGREEN, -1)     # 1900 span, east, northbound
    one(m, fr, 22916473, True, SEAGREEN, SEAGREEN, 1)               # 1948 span, west, southbound
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_r13_low_level", m)], frame=fr, axis=ax)
