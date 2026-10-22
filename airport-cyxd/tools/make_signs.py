"""Rasterise the Esso oval and the NAV CANADA plaque -> tools/assets/esso_sign.png and navcan_sign.png (1024 x 1024, power of two; each is
drawn at its true board aspect and squashed to a square, then stretched back onto the oval polygon in gen_buildings.py).
    python -I airport-cyxd/tools/make_signs.py"""
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


if __name__ == "__main__":
    esso().save(HERE / "assets/esso_sign.png")
    navcan().save(HERE / "assets/navcan_sign.png")
    lawoffice().save(HERE / "assets/lawoffice_sign.png")
    nwi().save(HERE / "assets/nwi_sign.png")
    efc().save(HERE / "assets/efc_sign.png")
    goa().save(HERE / "assets/goa_sign.png")
