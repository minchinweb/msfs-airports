"""H28 power-line routing map, drawn from the positions the scenery uses (airport-h28/tools/gen_powerline.py), with the
poles the user circled on the Esri frame in review (2026-11-07) marked in purple. Sources: that review, the Sep 2025
Street View (docs/h28/reference/streetview-2025-09-*), the CLUI 2014 photo and the mindtrip aerial.

    python -I docs/h28/powerline_map.py

Writes docs/h28/powerline-routing-2025.png. North up. The US line runs on south past the bottom of the frame.
"""
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "airport-h28" / "tools"))
import gen_field as gf  # noqa: E402
import gen_port as gp  # noqa: E402
import gen_powerline as pl  # noqa: E402

LAT_M, LON_M = gp.LAT, gp.LON
LAT0, LON0 = 48.99600, -112.79060
LAT_TOP, LON_RIGHT = 49.00115, -112.78480
SCALE = 2.2
OX, OY = 40, 84

WF, CL, BORDER, ROAD_C = gf.WF, gf.CL, gf.BORDER, pl.ROAD_C
PARK_S, PARK_E = gf.PARK_S, gf.PARK_E
POCKET_N, POCKET_E = gf.POCKET_N, gf.POCKET_E
NF = CL + 13.4 / LAT_M
RW_W = -112.788063


def east(m):
    return WF + m / LON_M


def north(m, base=BORDER):
    return base + m / LAT_M


def ll(p):
    """(lat, lon) of a gen_powerline pole or light tuple (title, lat, lon, ...)."""
    return p[1], p[2]


# Poles the user circled in review (read off the purple marks on the Esri frame).
REVIEW = [(48.998894, east(33)), (pl.SOUTH, east(33)), (pl.SOUTH, east(136)), (48.99779, east(139)),
          (48.99710, east(139))]
US = [ll(p) for p in pl.US_POLES]
CA = [ll(p) for p in pl.CA_POLES]
P_TREES, P_TX, P_SOCK, P_S1 = US[0], US[1], US[2], US[3]
CA_N_END, P_CA_END = CA[0], CA[-1]
GUY_ANCHOR = (P_CA_END[0] - pl.GUY / LAT_M, P_CA_END[1])
L_EAST, L_WEST_N, L_WEST_S = ll(pl.L_EAST), ll(pl.L_WEST_N), ll(pl.L_WEST_S)

MON_308A = (48 + 59 / 60 + 54.8 / 3600, -(112 + 47 / 60 + 18.5 / 3600))
MON_308B = (48 + 59 / 60 + 54.8 / 3600, -(112 + 47 / 60 + 17.7 / 3600))


def px(lat, lon):
    return OX + (lon - LON0) * LON_M * SCALE, OY + (LAT_TOP - lat) * LAT_M * SCALE


W = int(px(LAT0, LON_RIGHT)[0] + 360)
H = int(px(LAT0, LON0)[1] + 40)
im = Image.new("RGB", (W, H), "#f6f3ea")
d = ImageDraw.Draw(im)
F = r"C:\Windows\Fonts\%s.ttf"
font = ImageFont.truetype(F % "arial", 15)
font_s = ImageFont.truetype(F % "arial", 13)
font_b = ImageFont.truetype(F % "arialbd", 18)
font_h = ImageFont.truetype(F % "arialbd", 22)

GREEN, GREEN_D, PURPLE, ORANGE, GREY = "#1f7a3a", "#2b5fb0", "#7b3fa0", "#e2701f", "#777"


def poly(pts, fill, outline):
    d.polygon([px(*p) for p in pts], fill=fill, outline=outline)


def line(pts, fill, width=4):
    d.line([px(*p) for p in pts], fill=fill, width=width)


def dashed(pts, fill, width=2, dash=9, gap=6):
    flat = [px(*p) for p in pts]
    for (x0, y0), (x1, y1) in zip(flat, flat[1:]):
        dist = math.hypot(x1 - x0, y1 - y0) or 1
        ux, uy = (x1 - x0) / dist, (y1 - y0) / dist
        t = 0.0
        while t < dist:
            t2 = min(dist, t + dash)
            d.line([(x0 + ux * t, y0 + uy * t), (x0 + ux * t2, y0 + uy * t2)], fill=fill, width=width)
            t += dash + gap


def ring(p, r, col, width=2, fill="#f6f3ea"):
    x, y = px(*p)
    d.ellipse([x - r, y - r, x + r, y + r], fill=fill, outline=col, width=width)


def pole(p, confirmed):
    if confirmed:
        ring(p, 9, PURPLE, 3)
    ring(p, 5, GREEN, 2)


def light(p):
    x, y = px(*p)
    d.ellipse([x - 7, y - 7, x + 7, y + 7], fill="#ffd21f", outline="#8a6a00", width=2)
    d.line([(x - 12, y), (x + 12, y)], fill="#8a6a00", width=1)
    d.line([(x, y - 12), (x, y + 12)], fill="#8a6a00", width=1)


def ball(p):
    x, y = px(*p)
    d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=ORANGE, outline="#8a3a00")


def callout(p, s, dx, dy, fill, f=None):
    """Label placed dx, dy pixels from the point, with a thin leader line back to it."""
    x, y = px(*p)
    tw, th = d.multiline_textbbox((0, 0), s, font=f or font_s, spacing=2)[2:]
    tx, ty = x + dx, y + dy
    ex = min(max(x, tx), tx + tw)
    ey = ty if y < ty else ty + th
    d.line([(x, y), (ex, ey)], fill="#999", width=1)
    d.multiline_text((tx, ty), s, fill=fill, font=f or font_s, spacing=2)


def mid(a, b, t):
    return a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t


def text(p, s, fill="#222", f=None, dx=0, dy=0):
    x, y = px(*p)
    d.multiline_text((x + dx, y + dy), s, fill=fill, font=f or font_s, spacing=2)


# Ground: airport (pocket, strip, US parking), runway, road, border.
poly([(POCKET_N, WF), (POCKET_N, POCKET_E), (NF, POCKET_E), (NF, LON_RIGHT), (BORDER, LON_RIGHT), (BORDER, PARK_E),
      (PARK_S, PARK_E), (PARK_S, WF)], "#e4ecd4", "#b7c4a4")
poly([(CL + 10 / LAT_M, RW_W), (CL + 10 / LAT_M, LON_RIGHT), (CL - 10 / LAT_M, LON_RIGHT), (CL - 10 / LAT_M, RW_W)],
     "#d9d6c8", "#a39e90")
poly([(LAT_TOP, ROAD_C - 6 / LON_M), (LAT_TOP, ROAD_C + 6 / LON_M), (LAT0, ROAD_C + 6 / LON_M),
      (LAT0, ROAD_C - 6 / LON_M)], "#d0d0d0", "#9a9a9a")
# tree clump west of the road at the border (Esri), rough outline
poly([(north(12), ROAD_C - 75 / LON_M), (north(12), ROAD_C - 9 / LON_M), (north(-22), ROAD_C - 9 / LON_M),
      (north(-22), ROAD_C - 75 / LON_M)], "#cfdcc0", "#9fb48c")
text((north(12), ROAD_C - 74 / LON_M), "trees", "#5d7a4c", dx=3, dy=2)
line([(BORDER, LON0), (BORDER, LON_RIGHT)], "#c9a227", 2)

buildings = [(f[2], f[3] + gp.DX, f[4], f[5], "CBSA" if f[0] == "cbsa_main" else "")
             for f in gp.FOOTPRINTS if f[2] > BORDER]
mx, mz = gp.MAST[0], gp.MAST[1]  # radio mast, from the CBSA office centre
office = next(f for f in gp.FOOTPRINTS if f[0] == "cbsa_main")
x, y = px(office[2] + mz / LAT_M, office[3] + gp.DX + mx / LON_M)
d.polygon([(x, y - 7), (x - 6, y + 5), (x + 6, y + 5)], outline="#5c6b7a", width=2)
d.text((x + 8, y - 4), "mast", fill="#5c6b7a", font=font_s)
for la, lo, w, dep, name in buildings:
    x, y = px(la, lo)
    d.rectangle([x - w / 2 * SCALE, y - dep / 2 * SCALE, x + w / 2 * SCALE, y + dep / 2 * SCALE],
                fill="#c5d0da", outline="#5c6b7a")
    if name:
        d.text((x - 60, y - 9), name, fill="#1e3344", font=font_b)

for p, name in ((MON_308A, "308A"), (MON_308B, "308B")):
    x, y = px(*p)
    d.polygon([(x, y - 6), (x - 5, y + 4), (x + 5, y + 4)], fill="#b8a37a", outline="#5a4a2a")

# Windsock
x, y = px(BORDER, PARK_E - 3 / LON_M)
d.polygon([(x, y), (x + 14, y - 4), (x + 14, y + 4)], fill="#e8541e")
text((BORDER, PARK_E - 3 / LON_M), "windsock", "#a33a10", dx=4, dy=-24)

# Canadian line: vertical four-wire arrangement, east of the highway behind the port buildings, dead-ends north
# of the pocket with a guy wire.
line(CA, GREEN_D, 5)
for p in CA:
    pole(p, False)
dashed([P_CA_END, GUY_ANCHOR], GREY, 2, 4, 3)
x, y = px(*GUY_ANCHOR)
d.line([(x - 5, y), (x + 5, y)], fill=GREY, width=3)

# US line: tree clump -> over the road (one ball) -> transformer pole -> windsock pole (three balls) -> south, clipped
# at the bottom of the frame.
shown = [p for p in US if p[0] >= LAT0]
line(shown + [(LAT0, P_SOCK[1])], GREEN, 4)
for p in shown:
    pole(p, False)
x, y = px(*P_TX)
d.rectangle([x + 7, y - 14, x + 15, y - 4], fill="#8a8f96", outline="#333")  # transformer can
by_title = {p[0]: ll(p) for p in pl.US_POLES}
for (a, b), ts in pl.BALL_SPANS.items():
    for t in ts:
        ball(mid(by_title[a], by_title[b], t))
t_road = pl.BALL_SPANS[(pl.WEST, pl.TX)][0]

# Road lights and their single-wire feeds (the drop from the tree-clump pole is assumed: dashed).
for p in (L_EAST, L_WEST_N, L_WEST_S):
    light(p)
for a, b in pl.FEEDS:
    if a[0] == pl.WEST:
        dashed([ll(a), ll(b)], GREEN, 1, 5, 4)
    else:
        line([ll(a), ll(b)], GREEN, 1)

for p in REVIEW:  # the user's circles, over the modelled poles
    ring(p, 9, PURPLE, 3, fill=None)

# Labels
text((LAT_TOP, ROAD_C), "AB-62 / MT-213", "#444", dx=10, dy=6)
text((49.00030, LON0), "CANADA", "#3d5a40", font_b, dx=6)
text((48.99700, LON0), "UNITED STATES", "#3d5a40", font_b, dx=6)
text((CL, east(240)), "runway 07  →", "#4a463c", font, dy=-9)
text((BORDER, LON0), "border", "#8a7010", dx=6, dy=4)
callout(CA_N_END, "north end: the line stops here and does not\ncontinue up the highway (Street View j).\n"
        "Feed not seen: underground, or a low-voltage\nline from a service at the port?", 30, -110, GREEN_D)
text((49.00005, pl.CA_EAST), "Canadian line: 4 wires,\nvertical arrangement,\nbehind the port buildings",
     GREEN_D, dx=12, dy=-20)
callout(P_CA_END, "dead-end pole,\nguy wire to just north\nof the airport fence", 30, -75, GREEN_D)
callout(P_TREES, "US line starts in the tree clump\n(Street View h)", -150, 70, GREEN)
callout(P_TX, "transformer pole", 10, 40, "#222")
text(P_SOCK, "pole by the windsock,\nline turns south", "#222", dx=12, dy=8)
text(P_S1, "US line: 3 wires,\ndue south across\nthe fields", GREEN, dx=14, dy=-20)
text((LAT0, P_SOCK[1]), f"continues south: {pl.US_SOUTH} poles south of the windsock,\n{pl.US_SPACING:.0f} m apart "
     f"({pl.US_SOUTH * pl.US_SPACING:.0f} m)", GREEN, dx=12, dy=-40)
callout(L_EAST, "light, east side of the road, north of the border:\nsingle wire to the transformer pole", 190, -85,
        "#6b5200")
callout(L_WEST_N, "lights, west side of the road, either side of the border:\nsingle wire between them; fed from the US line\nat the tree-clump pole (that drop assumed)",
        -260, -110, "#6b5200")
callout(mid(P_TREES, P_TX, t_road), "ball over the middle of the road", -120, 130, "#b0500f")
text(mid(P_TX, P_SOCK, 0.5), "3 balls", "#b0500f", dx=-20, dy=10)
callout(MON_308A, "monument 308A", -200, -40, "#5a4a2a")
callout(MON_308B, "monument 308B", 150, -60, "#5a4a2a")

# North arrow and scale
ax, ay = 60, H - 74
d.polygon([(ax, ay - 26), (ax - 7, ay), (ax + 7, ay)], fill="#222")
d.text((ax - 6, ay + 4), "N", fill="#222", font=font_b)
sx, sy = 110, H - 52
d.line([(sx, sy), (sx + 50 * SCALE, sy)], fill="#222", width=3)
for xx in (sx, sx + 50 * SCALE):
    d.line([(xx, sy - 5), (xx, sy + 5)], fill="#222", width=2)
d.text((sx + 38, sy + 6), "50 m", fill="#222", font=font_s)

d.text((24, 14), "H28 power lines — as modelled", fill="#222", font=font_h)
d.text((24, 46), "North up.  Two separate systems: a Canadian line inside the port that dead-ends north of the airport, and a US line "
       "along the border that turns south at the windsock.", fill="#444", font=font_s)

lx, ly = W - 330, 96
d.rounded_rectangle([lx - 14, ly - 14, W - 18, ly + 290], radius=8, fill="#fffdf8", outline="#ddd6c4")
d.text((lx, ly), "Legend", fill="#222", font=font_b)
rows = ["can", "us", "drop", "pp", "p", "light", "ball", "guy", "border"]
labels = {
    "can": "Canadian line (4 wires)",
    "us": "US line (3 wires)",
    "drop": "Feed to a light (single wire)",
    "pp": "Your circle in review",
    "p": "Modelled pole",
    "light": "Road light (tall wooden pole)",
    "ball": "Orange marker ball",
    "guy": "Guy wire and anchor",
    "border": "Border",
}
for i, k in enumerate(rows):
    y = ly + 36 + i * 27
    c = (lx + 13, y + 6)
    if k == "can":
        d.line([(lx, y + 6), (lx + 26, y + 6)], fill=GREEN_D, width=5)
    elif k == "us":
        d.line([(lx, y + 6), (lx + 26, y + 6)], fill=GREEN, width=4)
    elif k == "drop":
        d.line([(lx, y + 6), (lx + 26, y + 6)], fill=GREEN, width=1)
    elif k == "pp":
        d.ellipse([c[0] - 9, c[1] - 9, c[0] + 9, c[1] + 9], outline=PURPLE, width=3)
    elif k == "p":
        d.ellipse([c[0] - 5, c[1] - 5, c[0] + 5, c[1] + 5], outline=GREEN, width=2)
    elif k == "light":
        d.ellipse([c[0] - 7, c[1] - 7, c[0] + 7, c[1] + 7], fill="#ffd21f", outline="#8a6a00", width=2)
    elif k == "ball":
        d.ellipse([c[0] - 5, c[1] - 5, c[0] + 5, c[1] + 5], fill=ORANGE, outline="#8a3a00")
    elif k == "guy":
        for xx in range(lx, lx + 26, 7):
            d.line([(xx, y + 6), (xx + 4, y + 6)], fill=GREY, width=2)
    else:
        d.line([(lx, y + 6), (lx + 26, y + 6)], fill="#c9a227", width=2)
    d.text((lx + 36, y - 2), labels[k], fill="#222", font=font_s)

dest = r"docs\h28\powerline-routing-2025.png"
im.save(dest)
print(dest, im.size)
