"""F256 100 Street Funicular (2018) with the Frederick G. Todd Lookout footbridge and the urban stair.
NOTES.md: one glass cabin on two rails on a steel beam on screw piles, track way 490235928 (64.0 m plan), 66.0 m at 23.5 degrees
(DIALOG); terrain drop 24.6 m (663.04 to 638.46); urban stair 6 m wide with Kebony treads beside it; footbridge 50 m main span + 19.4 m
+ 19 m lookout cantilever, two weathering-steel girders, precast deck, timber-slat-clad sides, one round concrete pier, glass elevator
shaft.  Datum (y = 0) is the footbridge deck, 637.74 m (2018 DSM median); river 613.74 m.
"""
import math
from bridgelib import *

CODE, TITLE = "F256", "100 Street Funicular and footbridge"
RIVER = 637.74
F = "F256-funicular"
TOP_Y, BOT_Y = 663.04 - 637.74, 638.46 - 637.74


def build():
    lat0, lon0 = 53.539305, -113.487472
    fr = Frame(lat0, lon0)
    m = BMesh()
    # funicular
    ft = fr.axis(find_way(F, 490235928))
    L = ft.L
    yf = lambda s: TOP_Y - (TOP_Y - BOT_Y) * s / L
    ribbon(m, ft, 0.0, L, -0.9, 0.9, lambda s: yf(s) - 0.7, lambda s: yf(s) - 0.1, DGREY, step=64.0)
    for t in (-0.6, 0.6):
        ribbon(m, ft, 0.0, L, t - 0.05, t + 0.05, lambda s: yf(s) - 0.1, lambda s: yf(s) + 0.05, RAILSTEEL, step=64.0)
    for i in range(int(L // 6) + 1):
        s = 1 + i * 6
        for t in (-0.7, 0.7):
            beam(m, ft.p3(s, t, yf(s) - 3.0), ft.p3(s, t, yf(s) - 0.7), 0.3, 0.3, DGREY)
    a, b = 24.0, 27.0                                    # glass cabin 3 m x 2.2 m on the slope
    beam(m, ft.p3(a, 0, yf(a) + 0.5), ft.p3(b, 0, yf(b) + 0.5), 2.2, 0.3, DGREY)
    beam(m, ft.p3(a, 0, yf(a) + 1.9), ft.p3(b, 0, yf(b) + 1.9), 2.1, 2.1, GLASSLT)
    prism(m, [ft.en(-1, -4), ft.en(-1, 4), ft.en(9, 4), ft.en(9, -4)], TOP_Y + 2.9, TOP_Y + 3.2, DGREY)    # upper canopy
    for s, t in ((-0.7, -3.6), (-0.7, 3.6), (8.7, -3.6), (8.7, 3.6)):
        beam(m, ft.p3(s, t, TOP_Y - 0.4), ft.p3(s, t, TOP_Y + 2.9), 0.2, 0.2, DGREY)
    # urban stair: two mapped runs, falling with the hill
    s1, s2 = fr.axis(find_way(F, 533867743)), fr.axis(find_way(F, 1301170658))
    tot = s1.L + 3.9 + s2.L
    ys = lambda s: TOP_Y - 0.1 - (TOP_Y - BOT_Y - 1.0) * s / tot
    ribbon(m, s1, 0.0, s1.L, -3.0, 3.0, lambda s: ys(s) - 0.4, lambda s: ys(s), TIMBER, step=8.0)
    ribbon(m, s2, 0.0, s2.L, -3.0, 3.0, lambda s: ys(s + s1.L + 3.9) - 0.4, lambda s: ys(s + s1.L + 3.9), TIMBER, step=8.0)
    # footbridge
    fb = fr.axis(find_way(F, 533867748))
    Lb = fb.L
    ribbon(m, fb, 0.0, Lb, -1.9, 1.9, -1.5, -0.1, RUST, step=10.0)                   # two weathering-steel girders + precast deck
    ribbon(m, fb, 0.0, Lb, -1.9, 1.9, -0.25, 0.0, CONC, step=10.0)
    for t in (-1.9, 1.9):
        ribbon(m, fb, 0.0, Lb, t - 0.05, t + 0.05, 0.0, 1.35, TIMBER, step=10.0)     # timber-slat-clad sides
    for t in (-1.5, 1.5):
        ribbon(m, fb, 0.0, Lb, t - 0.03, t + 0.03, 1.35, 1.4, RAILSTEEL, step=10.0)
    e, n = fb.en(52.0, 0.0)
    cyl(m, e, n, 1.0, 1.1, -13.0, -1.5, CONC, n=16)                                  # round concrete pier
    e, n = fb.en(Lb - 21.0, 0.0)
    for dx, dz in ((-1.6, -1.6), (1.6, -1.6), (1.6, 1.6), (-1.6, 1.6)):               # steel-framed glass elevator shaft
        beam(m, (e + dx, -19.0, n + dz), (e + dx, 3.4, n + dz), 0.25, 0.25, DGREY)
    prism(m, [(e - 1.6, n - 1.6), (e + 1.6, n - 1.6), (e + 1.6, n + 1.6), (e - 1.6, n + 1.6)], -19.0, 3.2, GLASSLT)
    prism(m, [(e - 1.9, n - 1.9), (e + 1.9, n - 1.9), (e + 1.9, n + 1.9), (e - 1.9, n + 1.9)], 3.2, 3.5, DGREY)
    return dict(code=CODE, title=TITLE, lat0=lat0, lon0=lon0, alt=RIVER, parts=[("br_f256_funicular", m)], frame=fr, axis=fb)
