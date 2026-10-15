"""R10 High Level Bridge (1913, CPR / City of Edmonton): 28 spans, 777 m, road deck under a rail deck.

Numbers: docs/edmonton-bridges/reference/R10-high-level/NOTES.md (1914 plate readings), elevation/README.md (2018 LiDAR).
Frame: axis runs north -> south along the straight part of the lower road way; s = 0 at the north end of the steel, left of travel = east.
Datum (y = 0) is the 2018 LiDAR river surface at this reach, 614.91 m (CGVD2013).  Rail deck base = +47.55 m at the north end.
"""
import math
from bridgelib import *

CODE, TITLE = "R10", "High Level Bridge"
RIVER = 614.91
K = 777.24 / 780.03          # the plate sums to 2,558 ft against the documented 2,550 ft

# supports along the bridge, plate readings (m), north -> south, scaled by K
def _s(x):
    return x * K

S27, S26, S25 = _s(36.6), _s(76.15), _s(116.31)
S24, S23, S22 = _s(205.26), _s(294.64), _s(383.59)
TOWER_W, TOWER_GAP = 15.06, 29.77
T_LEFT = [_s(414.02 + i * (TOWER_W + TOWER_GAP)) for i in range(6)]   # north leg of each of the six tall bents
LOW = [(_s(683.73), 12.4), (_s(715.33), 10.5), (_s(742.93), 10.5)]    # lower bents 9/8, 7/6, 5/4: (north leg s, width)
S_END = 777.24
# rail line to the base of the steel for the left / right leg (m), from the plate
T_H = [(37.2, 37.2), (37.2, 38.5), (41.7, 42.5), (42.2, 42.8), (36.8, 36.8), (31.9, 28.3)]
LOW_H = [(23.4, 20.3), (17.6, 15.0), (12.8, 9.6)]

TT = 6.0                 # truss lines at +-6.0 m (deck 11.89 m between)
DECK_W = 11.89
Y_RAIL0 = 47.55          # base of rail at the north end
GRADE_S = 0.0074         # rises southward from pier 22 (plate; the LiDAR deck reads +2.5 m by bent 9/8)
S_UPPER_END = LOW[0][0] + LOW[0][1] + 0.5   # rail deck stops after bent 9/8


def y_rail(s):
    return Y_RAIL0 + (max(0.0, min(s, LOW[0][0] + LOW[0][1]) - S22)) * GRADE_S


def y_road(s):
    """Top of the lower road deck: 5.84 m under the rail base, then a 5.45 percent ramp up to street level at the south abutment."""
    base = Y_RAIL0 - 5.84
    if s <= S22:
        return base
    s98 = LOW[0][0] + LOW[0][1]
    if s <= s98:
        return base + (s - S22) * GRADE_S
    return base + (s98 - S22) * GRADE_S + (s - s98) * 0.0545


# ground (2018 DTM under the road way, +19 m to structure stations), metres above the river
GROUND = profile([(0, 28), (45, 22.5), (71, 14), (96, 10.6), (122, 2.7), (148, 0), (328, 0), (354, 5.6), (380, 10), (405, 10.1),
                  (431, 9.8), (457, 9.6), (483, 6), (508, 8), (534, 6), (560, 9.6), (586, 11.3), (611, 16), (637, 21.9),
                  (663, 26.6), (686, 31.7), (703, 34.3), (725, 36.2), (748, 45.9), (800, 46)])


def make_axis(fr):
    import json
    g = json.load(open(ROOT / "docs/edmonton-bridges/reference/R10-high-level/geometry.json", encoding="utf-8"))
    road = [d for d in g["decks"] if d["osm_way"] == 22915822][0]
    pts = [fr.en(*p) for p in road["nodes"]]
    # the first two nodes are the straight run (653 m); the rest is the curve into Soullier Avenue
    ln = math.hypot(pts[1][0] - pts[0][0], pts[1][1] - pts[0][1])
    d = ((pts[1][0] - pts[0][0]) / ln, (pts[1][1] - pts[0][1]) / ln)
    start = (pts[0][0] - d[0] * 19.0, pts[0][1] - d[1] * 19.0)
    end = (start[0] + d[0] * S_END, start[1] + d[1] * S_END)
    return Axis([start, end])


def build():
    fr0 = Frame(53.531, -113.511)
    ax_ll = make_axis(fr0)
    # re-centre the model origin on the middle of the straight axis
    mid = ax_ll.at(S_END / 2)
    lat0, lon0 = fr0.ll(mid[0], mid[1])
    fr = Frame(lat0, lon0)
    ax = make_axis(fr)
    m = BMesh()
    ST, BR = BLACKST, RUST
    # --- piers in the river and on the banks --------------------------------------------------------------------
    HEAD = 29.5
    for s, name in ((S25, "25"), (S24, "24"), (S23, "23"), (S22, "22")):
        base_y = max(GROUND(s) - 3.0, -13.0)
        plan_top = nose_plan(ax, s, 0.0, 2.1, 5.2, 2.0)
        plan_bot = nose_plan(ax, s, 0.0, 3.0, 6.4, 3.0)
        frustum(m, plan_bot, plan_top, base_y, HEAD - 1.2, CONCD)
        prism(m, nose_plan(ax, s, 0.0, 2.6, 6.2, 0.0, (False, False)), HEAD - 1.2, HEAD, CONC)
    # north approach piers 26, 27 (concrete)
    for s in (S26, S27):
        base_y = GROUND(s) - 3.0
        top = 41.7 - 2.2
        prism(m, nose_plan(ax, s, 0.0, 1.6, 5.4, 0.0, (False, False)), base_y, top - 0.8, CONCD)
        prism(m, nose_plan(ax, s, 0.0, 2.2, 6.0, 0.0, (False, False)), top - 0.8, top, CONC)
    # north end: plate girders on the small footings 28 and 29
    for s in (3.0, 19.0):
        prism(m, nose_plan(ax, s, 0.0, 1.2, 5.4, 0.0, (False, False)), GROUND(s) - 3.0, 41.7 - 1.6, CONCD)
    for t in (-TT, TT):
        beam(m, ax.p3(0.0, t, y_rail(0) - 1.9), ax.p3(S27, t, y_rail(0) - 1.9), 0.8, 3.0, ST, ax.p3(0, 1, 0))

    # --- trusses: north Warren, river Baltimore, south Pratt and tower spans ------------------------------------------
    def span(s0, s1, kind, npan, depth, sub=False, big=False):
        for t in (-TT, TT):
            ytop = lambda s: y_rail(s) - 1.15
            ybot = (lambda s: y_rail(s) - 1.15 - depth)
            c = (1.0, 1.0) if big else (0.7, 0.7)
            w = (0.55, 0.55) if big else (0.35, 0.4)
            truss_plane(m, ax, t, s0, s1, ytop, ybot, npan, kind=kind, chord=c, web=w, sw=ST, sw_web=ST, sub=sub)

    DEPTH_RIVER = 14.6
    span(S27, S26, "warren", 6, 7.0)
    span(S26, S25, "warren", 6, 7.0)
    for a, b in ((S25, S24), (S24, S23), (S23, S22)):
        span(a, b, "pratt", 14, DEPTH_RIVER, sub=True, big=True)
    # the first south span and the spans between towers: shallow Pratt; inside each tower a short girder span
    prev = S22
    for tl in T_LEFT:
        span(prev, tl, "pratt", 6, 5.0)                     # approach Pratt span up to the tower
        span(tl, tl + TOWER_W, "warren", 3, 5.0)            # girder span inside the tower
        prev = tl + TOWER_W
    span(prev, LOW[0][0], "pratt", 6, 5.0)
    span(LOW[0][0], LOW[0][0] + LOW[0][1], "warren", 3, 5.0)

    # --- decks ---------------------------------------------------------------------------------------------------
    S_RAIL_END = LOW[0][0] + LOW[0][1]
    # rail deck: black plate-girder deck, timber-tie strip with two rails
    ribbon(m, ax, 0.0, S_RAIL_END, -DECK_W / 2, DECK_W / 2, lambda s: y_rail(s) - 0.75, lambda s: y_rail(s), ST, step=20.0,
           sw_top=BLACKST)
    ribbon(m, ax, 0.0, S_RAIL_END, -1.6, 1.6, lambda s: y_rail(s), lambda s: y_rail(s) + 0.16, TIMBER, step=20.0)
    for tr in (-0.72, 0.72):
        ribbon(m, ax, 0.0, S_RAIL_END, tr - 0.05, tr + 0.05, lambda s: y_rail(s) + 0.16, lambda s: y_rail(s) + 0.3, RAILSTEEL, step=20.0)
    # catenary: poles beside the deck every 24 m, one contact wire
    n_pole = int((S_RAIL_END - S27) // 24)
    for i in range(n_pole + 1):
        s = S27 + 8 + i * 24
        if s > S_RAIL_END - 4:
            break
        for tt in (-5.5,):
            beam(m, ax.p3(s, tt, y_rail(s)), ax.p3(s, tt, y_rail(s) + 6.2), 0.25, 0.25, LAMP)
            beam(m, ax.p3(s, tt, y_rail(s) + 6.0), ax.p3(s, 0.0, y_rail(s) + 5.7), 0.12, 0.12, LAMP)
    beam(m, ax.p3(0.0, 0.0, y_rail(S27) + 5.6), ax.p3(S_RAIL_END, 0.0, y_rail(S_RAIL_END) + 5.6), 0.05, 0.05, LAMP)
    # lower road deck: asphalt, concrete sidewalks, floor beams every panel
    S_ROAD0, S_ROAD1 = 0.0, S_END
    ribbon(m, ax, S_ROAD0, S_ROAD1, -3.5, 3.5, lambda s: y_road(s) - 0.7, lambda s: y_road(s), ASPHALT, step=15.0, sw_side=CONCD)
    for sg in (-1, 1):
        a, b = (3.5, DECK_W / 2 + 0.05) if sg > 0 else (-DECK_W / 2 - 0.05, -3.5)
        ribbon(m, ax, S_ROAD0, S_ROAD1, a, b, lambda s: y_road(s) - 0.7, lambda s: y_road(s) + 0.15, CONC, step=15.0)
        # barrier rail (red) at the road edge, pipe handrail on the outer edge
        te = sg * 3.5
        ribbon(m, ax, S_ROAD0, S_ROAD1, te - 0.1, te + 0.1, lambda s: y_road(s) + 0.15, lambda s: y_road(s) + 0.75, RAILRED, step=15.0)
        railing(m, ax, S_ROAD0, S_ROAD1, sg * (DECK_W / 2), lambda s: y_road(s) + 0.15, h=1.1, post_step=4.0, sw_post=BLACKST,
                rails=2, step=15.0)
    for i in range(int((S_ROAD1 - S_ROAD0) // 6.3)):
        s = S_ROAD0 + 3.0 + i * 6.3
        beam(m, ax.p3(s, -DECK_W / 2, y_road(s) - 1.25), ax.p3(s, DECK_W / 2, y_road(s) - 1.25), 0.4, 1.1, BR)
    # bottom lateral bracing in the river spans
    for a, b in ((S25, S24), (S24, S23), (S23, S22)):
        dp = (b - a) / 14
        for i in range(14):
            y = y_rail(a) - 1.15 - DEPTH_RIVER
            x_brace(m, ax, a + i * dp, a + (i + 1) * dp, -TT, TT, y, 0.3, 0.3, BR)

    # --- steel towers and low bents -------------------------------------------------------------------------------
    def bent(s_left, width, hl, hr):
        legs = []
        for k, (s, h) in enumerate(((s_left, hl), (s_left + width, hr))):
            ytop = y_rail(s) - 1.15 - 5.0 - 0.5
            base = y_rail(s) - h if h > 0 else ytop - 12
            legs.append((s, base, ytop))
        # concrete pedestals under the four legs, then leg columns on the truss lines
        for s, base, ytop in legs:
            for t in (-TT, TT):
                e, n = ax.en(s, t)
                post = ax.p3(s, t, 0)
                prism(m, [ax.en(s - 1.4, t - 1.4), ax.en(s + 1.4, t - 1.4), ax.en(s + 1.4, t + 1.4), ax.en(s - 1.4, t + 1.4)], base - 4.0, base + 1.2, CONCD)
        # columns in storeys of about 7.3 m with horizontal struts and X bracing on the four faces
        (sa, ba, ta), (sb, bb, tb) = legs
        nst = max(2, int(round(((ta + tb) / 2 - (ba + bb) / 2) / 7.3)))
        for t in (-TT, TT):
            for (s, base, ytop) in legs:
                beam(m, ax.p3(s, t, base + 1.2), ax.p3(s, t, ytop), 1.0, 1.0, ST, ax.p3(0, 1, 0))
        for k in range(nst + 1):
            fa = k / nst
            ya = ba + 1.2 + (ta - ba - 1.2) * fa
            yb = bb + 1.2 + (tb - bb - 1.2) * fa
            if 0 < k:
                for t in (-TT, TT):  # along-bridge struts
                    beam(m, ax.p3(sa, t, ya), ax.p3(sb, t, yb), 0.5, 0.5, ST)
                beam(m, ax.p3(sa, -TT, ya), ax.p3(sa, TT, ya), 0.5, 0.5, ST)
                beam(m, ax.p3(sb, -TT, yb), ax.p3(sb, TT, yb), 0.5, 0.5, ST)
            if k < nst:
                fa2 = (k + 1) / nst
                ya2 = ba + 1.2 + (ta - ba - 1.2) * fa2
                yb2 = bb + 1.2 + (tb - bb - 1.2) * fa2
                for t in (-TT, TT):
                    beam(m, ax.p3(sa, t, ya), ax.p3(sb, t, yb2), 0.35, 0.35, ST)
                    beam(m, ax.p3(sa, t, ya2), ax.p3(sb, t, yb), 0.35, 0.35, ST)
                for s, y1, y2 in ((sa, ya, ya2), (sb, yb, yb2)):
                    beam(m, ax.p3(s, -TT, y1), ax.p3(s, TT, y2), 0.35, 0.35, ST)
                    beam(m, ax.p3(s, -TT, y2), ax.p3(s, TT, y1), 0.35, 0.35, ST)

    for tl, (hl, hr) in zip(T_LEFT, T_H):
        bent(tl, TOWER_W, hl, hr)
    for (sl, w), (hl, hr) in zip(LOW, LOW_H):
        bent(sl, w, hl, hr)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_r10_high_level", m)],
                frame=fr, axis=ax)
