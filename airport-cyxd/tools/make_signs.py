"""Rasterise the Esso oval and the NAV CANADA plaque -> tools/assets/esso_sign.png and navcan_sign.png (1024 x 1024, power of two; each is
drawn at its true board aspect and squashed to a square, then stretched back onto the oval polygon in gen_buildings.py).
    python -I airport-cyxd/tools/make_signs.py"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

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
    """Top half: LAW OFFICE board (7.6 x 1.1 m); bottom half: AVIATION board (5.6 x 0.8 m); each stretched over half the square."""
    im = Image.new("RGB", (1024, 1024), (236, 236, 232))
    for k, (txt, aspect) in enumerate((("LAW OFFICE", 7.6 / 1.1), ("AVIATION", 5.6 / 0.8))):
        w = 2000
        h = int(w / aspect)
        b = Image.new("RGB", (w, h), (238, 238, 234))
        d = ImageDraw.Draw(b)
        d.rectangle((0, 0, w - 1, h - 1), outline=(90, 94, 96), width=int(h * 0.06))
        text_fit(d, txt, "arialbd.ttf", (w * 0.05, h * 0.2, w * 0.95, h * 0.8), (52, 56, 58))
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
        text_fit(d, txt, "arialbd.ttf", (w * 0.04, h * 0.18, w * 0.96, h * 0.82), (30, 34, 52))
        im.paste(b.resize((1024, 512), Image.LANCZOS), (0, 512 * k))
    return im


if __name__ == "__main__":
    esso().save(HERE / "assets/esso_sign.png")
    navcan().save(HERE / "assets/navcan_sign.png")
    lawoffice().save(HERE / "assets/lawoffice_sign.png")
    nwi().save(HERE / "assets/nwi_sign.png")
