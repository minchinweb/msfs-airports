"""Rasterise the Esso oval and the NAV CANADA plaque -> tools/assets/esso_sign.png and navcan_sign.png (1024 x 1024, power of two; each is
drawn at its true board aspect and squashed to a square, then stretched back onto the oval polygon in gen_buildings.py).
    python -I airport-cyxd/tools/make_signs.py"""
import math
from pathlib import Path
import random

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).resolve().parent
FONTS = Path("C:/Windows/Fonts")
SS = 2


def text_fit(d, txt, font_file, box, fill, anchor_xy=None):
    """Draw txt as large as fits in box (x0, y0, x1, y1), centred."""
    x0, y0, x1, y1 = box
    size = 400
    while size > 8:
        f = ImageFont.truetype(str(FONTS / font_file), size)
        l, t, r, b = d.textbbox((0, 0), txt, font=f)
        if r - l <= x1 - x0 and b - t <= y1 - y0:
            break
        size -= 4
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    d.text((cx - (r + l) / 2, cy - (b + t) / 2), txt, font=f, fill=fill)


def painted_text(im, txt, font_file, box, fill, seed=1, track=0.07, wobble=0.012, bold=0.045):
    """Sign-painter lettering (user, 2026-10-21: the NWI sign looked too modern and too exact against the 1950s photo): a heavy condensed grotesque
    set letter by letter with wide tracking, each letter a little off the baseline, size and angle, then the edge roughened, softened and the ink
    faded, so it reads as hand-painted on a board instead of typeset."""
    rnd = random.Random(seed)
    x0, y0, x1, y1 = box
    bw, bh = x1 - x0, y1 - y0
    size = 600
    while size > 10:
        f = ImageFont.truetype(str(FONTS / font_file), size)
        adv = [f.getlength(c) for c in txt]
        total = sum(adv) + track * size * (len(txt) - 1)
        l, t, r, b = f.getbbox("H")
        if total <= bw and (b - t) <= bh * 0.86:
            break
        size -= 4
    cap = b - t
    mask = Image.new("L", im.size, 0)
    x = x0 + (bw - total) / 2
    base = y0 + (bh + cap) / 2
    for c, a in zip(txt, adv):
        if c != " ":
            sz = int(size * (1 + rnd.uniform(-0.025, 0.025)))
            ff = ImageFont.truetype(str(FONTS / font_file), sz)
            tile = Image.new("L", (int(sz * 1.6), int(sz * 1.6)), 0)
            ImageDraw.Draw(tile).text((sz * 0.3, sz * 0.2), c, font=ff, fill=255)
            tile = tile.rotate(rnd.uniform(-0.8, 0.8), resample=Image.BICUBIC)
            top = ff.getbbox("H")[1]
            dy = rnd.uniform(-wobble, wobble) * bh
            mask.paste(255, (int(x - sz * 0.3), int(base - cap - (top - sz * 0.2) * 0 + dy - sz * 0.2 - top + 0)), tile)
        x += a + track * size
    k = int(size * bold) | 1  # thicken the strokes: the painted letters are heavier than Franklin Gothic Medium
    mask = mask.filter(ImageFilter.MaxFilter(max(3, k)))
    m = np.asarray(mask.filter(ImageFilter.GaussianBlur(max(1.0, size * 0.012))), dtype=np.float32) / 255.0
    noise = np.random.RandomState(seed).normal(0.0, 0.16, m.shape).astype(np.float32)
    noise = np.asarray(Image.fromarray(((noise + 1) * 127).clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.4)), dtype=np.float32) / 127.0 - 1.0
    m = np.clip((m - 0.5 + noise * 0.5) * 3.2 + 0.5, 0.0, 1.0)  # rough, slightly soft edge
    fade = 0.86 + 0.14 * np.random.RandomState(seed + 7).rand(*m.shape).astype(np.float32)
    a = (m * fade)[..., None]
    arr = np.asarray(im.convert("RGB"), dtype=np.float32)
    ink = np.array(fill, dtype=np.float32)
    im.paste(Image.fromarray((arr * (1 - a) + ink * a).astype(np.uint8)))


def esso(w=2000, h=800):
    im = Image.new("RGB", (w, h), (255, 255, 255))
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, w, h), fill=(0, 56, 147))                       # blue outer rim (the polygon is the oval itself)
    d.ellipse((w * 0.035, h * 0.07, w * 0.965, h * 0.93), fill=(255, 255, 255))
    d.ellipse((w * 0.06, h * 0.13, w * 0.94, h * 0.87), fill=(0, 56, 147))  # blue band
    d.ellipse((w * 0.075, h * 0.17, w * 0.925, h * 0.83), fill=(255, 255, 255))
    text_fit(d, "Esso", "ariblk.ttf", (w * 0.17, h * 0.25, w * 0.83, h * 0.75), (227, 24, 55))
    return im.resize((1024, 1024), Image.LANCZOS)


def navcan(w=2000, h=900):
    im = Image.new("RGB", (w, h), (205, 207, 206))
    d = ImageDraw.Draw(im)
    d.ellipse((w * 0.01, h * 0.02, w * 0.99, h * 0.98), fill=(150, 153, 152))
    d.ellipse((w * 0.03, h * 0.07, w * 0.97, h * 0.93), fill=(214, 217, 216))
    d.ellipse((w * 0.06, h * 0.13, w * 0.94, h * 0.87), fill=(192, 195, 194))
    text_fit(d, "NAV CANADA", "georgiab.ttf", (w * 0.17, h * 0.34, w * 0.83, h * 0.60), (84, 88, 90))
    d.line([(w * 0.28, h * 0.70), (w * 0.5, h * 0.64), (w * 0.72, h * 0.70)], fill=(120, 124, 125), width=int(h * 0.02))
    return im.resize((1024, 1024), Image.LANCZOS)


def lawoffice():
    """Top half: LAW OFFICE board (5.0 x 0.85 m); bottom half: AVIATION board (4.4 x 0.6 m); each stretched over half the square.
    Street View 59 (2012): thin, widely spaced regular-weight capitals on a pale board with a dark edge line, AVIATION in a lighter grey."""
    im = Image.new("RGB", (1024, 1024), (236, 236, 232))
    for k, (txt, aspect, bg, edge, ink, track) in enumerate((
            ("LAW OFFICE", 5.0 / 0.85, (234, 234, 228), (64, 68, 72), (44, 46, 50), 0.16),
            ("AVIATION", 4.4 / 0.6, (226, 228, 226), (110, 114, 118), (86, 90, 94), 0.30))):
        w = 2000
        h = int(w / aspect)
        b = Image.new("RGB", (w, h), bg)
        d = ImageDraw.Draw(b)
        d.rectangle((0, 0, w - 1, h - 1), outline=edge, width=max(3, int(h * 0.05)))
        d.rectangle((int(h * 0.09), int(h * 0.09), w - 1 - int(h * 0.09), h - 1 - int(h * 0.09)), outline=tuple(int(c * 0.5 + bg[0] * 0.5) for c in edge), width=2)
        painted_text(b, txt, "arial.ttf", (w * 0.05, h * 0.16, w * 0.95, h * 0.84), ink, seed=31 + k, track=track, wobble=0.0, bold=0.0)
        im.paste(b.resize((1024, 512), Image.LANCZOS), (0, 512 * k))
    return im


def nwi():
    """Top half: the roof sign board NORTHWEST INDUSTRIES LTD. (28 x 2.8 m); bottom half: COMMERCIAL AIRCRAFT SERVICE (26 x 1.5 m) as it
    was painted on the annex's second-floor band (1956 photo, docs/cyxd/hangar11-photos/flickr_woodysworld1_11393738936.jpg)."""
    im = Image.new("RGB", (1024, 1024), (236, 236, 230))
    for k, (txt, aspect, bg) in enumerate((("NORTHWEST INDUSTRIES LTD.", 28 / 2.8, (240, 240, 236)), ("COMMERCIAL AIRCRAFT SERVICE", 26 / 1.5, (233, 233, 227)))):
        w = 2400
        h = int(w / aspect)
        b = Image.new("RGB", (w, h), bg)
        d = ImageDraw.Draw(b)
        if k == 0:
            d.rectangle((0, 0, w - 1, h - 1), outline=(60, 64, 70), width=int(h * 0.03))
        painted_text(b, txt, "framd.ttf", (w * 0.04, h * 0.16, w * 0.96, h * 0.84), (26, 30, 46), seed=11 + k)
        im.paste(b.resize((1024, 512), Image.LANCZOS), (0, 512 * k))
    return im


def efc():
    """Top half: dark fascia lettering EDMONTON FLYING CLUB (14 x 0.8 m); bottom half: the landside entrance board, white with red
    lettering on two lines (4.4 x 1.7 m).  Hangar 18 (Flickr 11094398653, the 2013 Street View, the airside video)."""
    im = Image.new("RGB", (1024, 1024), (60, 52, 50))
    w = 2800
    h = int(w / (14 / 0.8))
    b = Image.new("RGB", (w, h), (74, 64, 60))
    text_fit(ImageDraw.Draw(b), "EDMONTON FLYING CLUB", "arialbd.ttf", (w * 0.05, h * 0.15, w * 0.95, h * 0.85), (236, 232, 224))
    im.paste(b.resize((1024, 512), Image.LANCZOS), (0, 0))
    w = 1760
    h = int(w / (4.4 / 1.7))
    b = Image.new("RGB", (w, h), (244, 244, 240))
    d = ImageDraw.Draw(b)
    d.rectangle((0, 0, w - 1, h - 1), outline=(150, 40, 40), width=int(h * 0.05))
    text_fit(d, "EDMONTON", "arialbd.ttf", (w * 0.1, h * 0.12, w * 0.9, h * 0.47), (200, 36, 40))
    text_fit(d, "FLYING CLUB", "arialbd.ttf", (w * 0.1, h * 0.52, w * 0.9, h * 0.88), (200, 36, 40))
    im.paste(b.resize((1024, 512), Image.LANCZOS), (0, 512))
    return im


def goa():
    """Government of Alberta sign on Hangar 4 (4.6 x 0.55 m): white board, blue "Alberta" logo box at the left, GOVERNMENT OF ALBERTA in
    grey capitals (docs/cyxd/hangar4-photos/Edmonton_City_Centre_Airport__4846283523_.jpg).  Stretched over the whole square."""
    w = 2760
    h = int(w / (4.6 / 0.55))
    b = Image.new("RGB", (w, h), (246, 246, 244))
    d = ImageDraw.Draw(b)
    d.rectangle((0, 0, w - 1, h - 1), outline=(120, 124, 130), width=int(h * 0.04))
    lw = int(w * 0.17)
    d.rectangle((0, 0, lw, h - 1), fill=(34, 62, 150))
    text_fit(d, "Alberta", "ariali.ttf", (lw * 0.08, h * 0.2, lw * 0.92, h * 0.8), (255, 255, 255))
    text_fit(d, "GOVERNMENT OF ALBERTA", "arial.ttf", (lw + w * 0.03, h * 0.18, w * 0.97, h * 0.82), (50, 54, 60))
    return b.resize((1024, 1024), Image.LANCZOS)


def museum():
    """Top half: ALBERTA AVIATION MUSEUM in dark green serif capitals on the white band over the doors (36 x 1.4 m with the V marks; the 2011 Commons photo and
    Street View 210410 / 210439); bottom half: the black two-post roadside sign (1.9 x 2.8 m face) with the club logo oval, the LED panel and the
    "History Takes Flight!" board (Street View 210439, 210533, 210605).  Each half is drawn at its true aspect and squashed into 1024 x 512."""
    im = Image.new("RGB", (1024, 1024), (238, 238, 234))
    w = 3600
    h = int(w / (36 / 1.4))
    b = Image.new("RGB", (w, h), (238, 238, 234))
    d = ImageDraw.Draw(b)
    text_fit(d, "ALBERTA   AVIATION   MUSEUM", "georgiab.ttf", (w * 0.1667, h * 0.12, w * 0.8333, h * 0.88), (34, 74, 58))
    for cx in (w * 0.5 - w * 0.467, w * 0.5 + w * 0.467):                       # the small "V" wing marks either side of the lettering
        d.polygon([(cx - h * 0.28, h * 0.2), (cx - h * 0.1, h * 0.2), (cx, h * 0.62), (cx + h * 0.1, h * 0.2), (cx + h * 0.28, h * 0.2),
                   (cx + h * 0.07, h * 0.82), (cx - h * 0.07, h * 0.82)], fill=(34, 74, 58))
    im.paste(b.resize((1024, 512), Image.LANCZOS), (0, 0))
    w, h = 760, 1120
    b = Image.new("RGB", (w, h), (22, 22, 24))
    d = ImageDraw.Draw(b)
    d.ellipse((w * 0.06, h * 0.05, w * 0.94, h * 0.37), fill=(236, 236, 232))                    # logo oval: white rim, blue sky, red aircraft
    d.ellipse((w * 0.1, h * 0.08, w * 0.9, h * 0.34), fill=(36, 78, 160))
    d.ellipse((w * 0.2, h * 0.15, w * 0.8, h * 0.27), fill=(120, 170, 220))
    d.polygon([(w * 0.28, h * 0.22), (w * 0.62, h * 0.19), (w * 0.74, h * 0.2), (w * 0.62, h * 0.225)], fill=(200, 40, 40))
    d.line([(w * 0.42, h * 0.17), (w * 0.5, h * 0.21)], fill=(200, 40, 40), width=8)
    text_fit(d, "ALBERTA   AVIATION   MUSEUM", "georgiab.ttf", (w * 0.2, h * 0.085, w * 0.8, h * 0.145), (236, 236, 232))
    d.rectangle((w * 0.07, h * 0.43, w * 0.93, h * 0.7), fill=(16, 16, 20), outline=(90, 90, 96), width=6)   # LED panel
    cols = [(240, 90, 60), (250, 210, 60), (90, 200, 120), (80, 160, 240), (200, 100, 220)]
    for k, txt in enumerate(("Volunteers", "Needed", "APPLY ONLINE")):
        text_fit(d, txt, "arialbd.ttf", (w * 0.12, h * (0.45 + 0.08 * k), w * 0.88, h * (0.51 + 0.08 * k)), cols[k])
    d.rectangle((w * 0.07, h * 0.74, w * 0.93, h * 0.89), fill=(176, 178, 184), outline=(90, 90, 96), width=6)  # board
    text_fit(d, "History Takes flight!", "ariali.ttf", (w * 0.12, h * 0.77, w * 0.88, h * 0.86), (40, 40, 48))
    im.paste(b.resize((1024, 512), Image.LANCZOS), (0, 512))
    return im


def gac():
    """Top half: the arched GENERAL AVIATION CENTRE board over the drum porch of Hangar 19 (5.7 x 2.0 m to the top of the arch; black, a blue
    twin-engine airliner among pale clouds, yellow capitals; Commons EDMONTON_MUNI_(11094203585)); the model cuts the arch out of the
    rectangle.  Bottom half: "77 Airport Rd." in brushed-steel letters on the stucco fascia of the curved entrance (5.0 x 0.7 m;
    Commons EDMONTON_MUNI_(11094283326)).  Each half is drawn at its true aspect and squashed into 1024 x 512."""
    im = Image.new("RGB", (1024, 1024), (190, 152, 140))
    w = 2280
    h = int(w / (5.7 / 2.0))
    b = Image.new("RGB", (w, h), (18, 18, 22))
    d = ImageDraw.Draw(b)
    for cx, cy, s, col in ((0.16, 0.5, 1.0, (236, 240, 244)), (0.24, 0.55, 0.8, (120, 170, 220)), (0.82, 0.52, 1.0, (236, 240, 244)),
                           (0.74, 0.56, 0.8, (120, 170, 220)), (0.33, 0.42, 0.6, (120, 170, 220))):  # clouds
        for dx, dy, r in ((-0.05, 0.03, 0.05), (0.0, 0.0, 0.07), (0.05, 0.03, 0.05)):
            rr = r * s * h
            d.ellipse(((cx + dx * s) * w - rr, (cy + dy * s) * h - rr, (cx + dx * s) * w + rr, (cy + dy * s) * h + rr), fill=col)
    blue, dark = (70, 140, 215), (30, 70, 130)
    d.polygon([(w * 0.30, h * 0.47), (w * 0.62, h * 0.30), (w * 0.70, h * 0.29), (w * 0.66, h * 0.36), (w * 0.36, h * 0.52)], fill=blue)  # fuselage
    d.polygon([(w * 0.41, h * 0.14), (w * 0.46, h * 0.14), (w * 0.56, h * 0.64), (w * 0.50, h * 0.66)], fill=blue)  # wing
    d.polygon([(w * 0.62, h * 0.31), (w * 0.69, h * 0.12), (w * 0.72, h * 0.13), (w * 0.70, h * 0.30)], fill=blue)  # fin
    for ex, ey in ((0.44, 0.27), (0.51, 0.52)):  # engines
        d.ellipse((w * (ex - 0.025), h * (ey - 0.06), w * (ex + 0.025), h * (ey + 0.06)), fill=dark)
    text_fit(d, "GENERAL AVIATION CENTRE", "ariblk.ttf", (w * 0.05, h * 0.7, w * 0.95, h * 0.93), (240, 196, 40))
    im.paste(b.resize((1024, 512), Image.LANCZOS), (0, 0))
    w = 2400
    h = int(w / (5.0 / 0.7))
    b = Image.new("RGB", (w, h), (190, 152, 140))
    d = ImageDraw.Draw(b)
    text_fit(d, "77  Airport  Rd.", "arial.ttf", (w * 0.08, h * 0.12, w * 0.92, h * 0.88), (214, 214, 210))
    im.paste(b.resize((1024, 512), Image.LANCZOS), (0, 512))
    return im


def aerocentre():
    """AEROCENTRE logo painted on the cream spandrel of the Aerocentre's third front bay (4.4 x 0.75 m): black heavy italic capitals, the
    A crossed by a red swoosh (Commons 4846273897 / 4846891790, Flickr 33836413).  Stretched over the whole square."""
    w = 2640
    h = int(w / (4.4 / 0.75))
    b = Image.new("RGB", (w, h), (214, 208, 190))
    d = ImageDraw.Draw(b)
    text_fit(d, "AEROCENTRE", "ariblki.ttf" if (FONTS / "ariblki.ttf").exists() else "arialbi.ttf",
             (w * 0.05, h * 0.18, w * 0.95, h * 0.86), (24, 24, 28))
    d.polygon([(w * 0.03, h * 0.70), (w * 0.17, h * 0.10), (w * 0.21, h * 0.06), (w * 0.10, h * 0.62)], fill=(200, 36, 40))  # swoosh over the A
    return b.resize((1024, 1024), Image.LANCZOS)


def cessna():
    """Cessna board high on Hangar 15's NW gable near the landside corner (1.8 x 2.2 m; Street View 17 / 25 Airport Rd, Jun 2012, and
    Commons 11094252276): white board, a round emblem over the CESSNA name.  Too small in the photos to read the artwork, so this is a
    generic stand-in: a navy disc with a white swept wing and a red stripe, navy lettering.  Stretched over the whole square."""
    w = 1800
    h = 2200
    b = Image.new("RGB", (w, h), (240, 240, 236))
    d = ImageDraw.Draw(b)
    d.rectangle((20, 20, w - 20, h - 20), outline=(40, 52, 110), width=24)
    cx, cy, r = w / 2, h * 0.38, w * 0.33
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(30, 50, 120))
    d.polygon([(cx - r * 0.85, cy + r * 0.10), (cx + r * 0.80, cy - r * 0.42), (cx + r * 0.62, cy - r * 0.12), (cx - r * 0.55, cy + r * 0.30)],
              fill=(244, 244, 244))
    d.polygon([(cx - r * 0.70, cy + r * 0.42), (cx + r * 0.70, cy + r * 0.02), (cx + r * 0.60, cy + r * 0.20), (cx - r * 0.45, cy + r * 0.55)],
              fill=(200, 36, 40))
    text_fit(d, "CESSNA", "arialbd.ttf", (w * 0.08, h * 0.70, w * 0.92, h * 0.88), (30, 50, 120))
    return b.resize((1024, 1024), Image.LANCZOS)


# Right half of the 11-point maple leaf, top tip to stem, in leaf units (1 = the width of the flag's white square), from
# airport-h28/tools/gen_port.py; mirrored for the left.  The stem's centre point is dropped from the outline (it is collinear).
LEAF_R = [(0.0, 0.50), (0.07, 0.37), (0.14, 0.41), (0.11, 0.15), (0.21, 0.27), (0.25, 0.21), (0.42, 0.25), (0.37, 0.10),
          (0.44, 0.06), (0.24, -0.09), (0.28, -0.17), (0.05, -0.13), (0.06, -0.32), (0.0, -0.32)]
LEAF = LEAF_R[:-1] + [(-u, v) for u, v in reversed(LEAF_R[1:-1])]


def leaf(d, cx, cy, size, fill):
    """Maple leaf centred on (cx, cy) in a white square of width `size` (pixels)."""
    d.polygon([(cx + x * size, cy - (y - 0.09) * size) for x, y in LEAF], fill=fill)


def union_jack(img, x0, y0, x1, y1):
    """Union Jack pasted into the box of img (simplified: centred red saltire); drawn on its own tile so the diagonals stop at the edge."""
    tile = Image.new("RGB", (int(x1 - x0), int(y1 - y0)))
    union_jack_draw(ImageDraw.Draw(tile), 0, 0, tile.width, tile.height)
    img.paste(tile, (int(x0), int(y0)))


def union_jack_draw(d, x0, y0, x1, y1):
    w, h = x1 - x0, y1 - y0
    d.rectangle((x0, y0, x1, y1), fill=(1, 33, 105))
    t = h * 0.2
    for a, b in (((x0, y0), (x1, y1)), ((x0, y1), (x1, y0))):
        d.line([a, b], fill=(255, 255, 255), width=int(t))
        d.line([a, b], fill=(200, 16, 46), width=int(t * 0.35))
    d.rectangle((x0, y0 + h * 0.5 - t * 0.85, x1, y0 + h * 0.5 + t * 0.85), fill=(255, 255, 255))
    d.rectangle((x0 + w * 0.5 - t * 0.85, y0, x0 + w * 0.5 + t * 0.85, y1), fill=(255, 255, 255))
    d.rectangle((x0, y0 + h * 0.5 - t * 0.5, x1, y0 + h * 0.5 + t * 0.5), fill=(200, 16, 46))
    d.rectangle((x0 + w * 0.5 - t * 0.5, y0, x0 + w * 0.5 + t * 0.5, y1), fill=(200, 16, 46))


def shield(d, x0, y0, x1, y1):
    """Heater-shield outline points for the box."""
    w, h = x1 - x0, y1 - y0
    pts = [(x0, y0), (x1, y0), (x1, y0 + h * 0.55)]
    pts += [(x0 + w * 0.5 + w * 0.5 * math.cos(math.radians(a)), y0 + h * 0.55 + h * 0.45 * math.sin(math.radians(a))) for a in range(0, 181, 15)]
    return pts


def flags():
    """Flag atlas, four 2:1 flags stacked (each 1024 x 256 after squashing; the model's quads are 2:1): row 0 Canada, row 1 Alberta,
    row 2 the RCAF ensign (air-force blue, Union Jack canton, maple-leaf roundel in the fly), row 3 the Canadian Red Ensign (1957-65:
    red, Union Jack canton, the arms of Canada in the fly; on the Bomarc's fins).  The memorial flies Canada, Alberta and the RCAF ensign
    (user, 2026-11-03)."""
    out = Image.new("RGB", (1024, 1024), (255, 255, 255))
    W, H = 1024, 512
    red = (213, 43, 30)
    # Canada
    b = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(b)
    d.rectangle((0, 0, W / 4, H), fill=red); d.rectangle((W * 3 / 4, 0, W, H), fill=red)
    leaf(d, W / 2, H / 2, H, red)
    out.paste(b.resize((1024, 256), Image.LANCZOS), (0, 0))
    # Alberta: ultramarine field, the provincial shield in the centre
    b = Image.new("RGB", (W, H), (0, 38, 100)); d = ImageDraw.Draw(b)
    sx0, sy0, sx1, sy1 = W / 2 - H * 0.27, H * 0.12, W / 2 + H * 0.27, H * 0.88
    sh = shield(d, sx0, sy0, sx1, sy1)
    d.polygon(sh, fill=(240, 196, 40))                                                     # wheat field (base)
    m = Image.new("L", (W, H), 0); ImageDraw.Draw(m).polygon(sh, fill=255)
    lay = Image.new("RGB", (W, H)); ld = ImageDraw.Draw(lay)
    hh = sy1 - sy0
    ld.rectangle((sx0, sy0, sx1, sy0 + hh * 0.2), fill=(255, 255, 255))                   # St George's cross chief
    ld.rectangle((sx0, sy0 + hh * 0.07, sx1, sy0 + hh * 0.13), fill=(200, 16, 46))
    ld.rectangle((W / 2 - hh * 0.03, sy0, W / 2 + hh * 0.03, sy0 + hh * 0.2), fill=(200, 16, 46))
    ld.rectangle((sx0, sy0 + hh * 0.2, sx1, sy0 + hh * 0.55), fill=(70, 130, 210))       # sky
    ld.polygon([(sx0, sy0 + hh * 0.55), (sx0 + (sx1 - sx0) * 0.25, sy0 + hh * 0.3), (sx0 + (sx1 - sx0) * 0.5, sy0 + hh * 0.45),
                (sx0 + (sx1 - sx0) * 0.72, sy0 + hh * 0.26), (sx1, sy0 + hh * 0.55)], fill=(245, 245, 250))   # snow peaks
    ld.rectangle((sx0, sy0 + hh * 0.55, sx1, sy0 + hh * 0.68), fill=(40, 130, 60))       # green hills
    ld.rectangle((sx0, sy0 + hh * 0.68, sx1, sy1), fill=(240, 196, 40))
    b.paste(lay, (0, 0), m)
    d.line(sh + [sh[0]], fill=(250, 250, 250), width=4)
    out.paste(b.resize((1024, 256), Image.LANCZOS), (0, 256))
    # RCAF ensign
    b = Image.new("RGB", (W, H), (110, 160, 205)); d = ImageDraw.Draw(b)
    union_jack(b, 0, 0, W / 2, H / 2)
    cx, cy, r = W * 0.75, H * 0.5, H * 0.3
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(30, 50, 120))
    d.ellipse((cx - r * 0.68, cy - r * 0.68, cx + r * 0.68, cy + r * 0.68), fill=(255, 255, 255))
    leaf(d, cx, cy, r * 1.05, red)
    out.paste(b.resize((1024, 256), Image.LANCZOS), (0, 512))
    # Canadian Red Ensign
    b = Image.new("RGB", (W, H), (200, 16, 46)); d = ImageDraw.Draw(b)
    union_jack(b, 0, 0, W / 2, H / 2)
    sx0, sy0, sx1, sy1 = W * 0.75 - H * 0.2, H * 0.22, W * 0.75 + H * 0.2, H * 0.8
    sh = shield(d, sx0, sy0, sx1, sy1)
    d.polygon(sh, fill=(255, 255, 255))
    hh, ww = sy1 - sy0, sx1 - sx0
    d.rectangle((sx0, sy0, sx0 + ww / 2, sy0 + hh * 0.3), fill=(200, 16, 46))           # England / Scotland / Ireland / France, simplified
    d.rectangle((sx0 + ww / 2, sy0, sx1, sy0 + hh * 0.3), fill=(240, 200, 40))
    d.rectangle((sx0, sy0 + hh * 0.3, sx0 + ww / 2, sy0 + hh * 0.55), fill=(30, 60, 160))
    d.rectangle((sx0 + ww / 2, sy0 + hh * 0.3, sx1, sy0 + hh * 0.55), fill=(240, 240, 240))
    for k in (-1, 0, 1):                                                                 # three red maple leaves on the white base
        leaf(d, (sx0 + sx1) / 2 + k * ww * 0.3, sy0 + hh * 0.74, hh * 0.2, red)
    d.line(sh + [sh[0]], fill=(240, 200, 40), width=3)
    out.paste(b.resize((1024, 256), Image.LANCZOS), (0, 768))
    return out


if __name__ == "__main__":
    flags().save(HERE / "assets/flags_sign.png")
    cessna().save(HERE / "assets/cessna_sign.png")
    aerocentre().save(HERE / "assets/aerocentre_sign.png")
    esso().save(HERE / "assets/esso_sign.png")
    navcan().save(HERE / "assets/navcan_sign.png")
    lawoffice().save(HERE / "assets/lawoffice_sign.png")
    nwi().save(HERE / "assets/nwi_sign.png")
    efc().save(HERE / "assets/efc_sign.png")
    goa().save(HERE / "assets/goa_sign.png")
    museum().save(HERE / "assets/museum_sign.png")
    gac().save(HERE / "assets/gac_sign.png")
