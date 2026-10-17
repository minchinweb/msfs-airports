"""Rasterise the Shell pecten (first two paths of docs/cyxd/hangar16-photos/shell-pecten-reference.svg) onto a white sign board
-> tools/assets/shell_sign.png (1024 x 882, the 3.6 x 3.1 m board).  Run once; gen_buildings.py copies the PNG into modelLib.
    python -I airport-cyxd/tools/make_shell_sign.py"""
import re
from pathlib import Path
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
SVG = HERE.parents[1] / "docs/cyxd/hangar16-photos/shell-pecten-reference.svg"
OUT = HERE / "assets/shell_sign.png"
W, H, SS = 1024, 882, 4


def path_points(d, steps=12):
    toks = re.findall(r"[MmLlHhVvCcZz]|-?\d*\.?\d+(?:e-?\d+)?", d)
    i, cur, start, pts, cmd = 0, (0.0, 0.0), (0.0, 0.0), [], None
    num = lambda: float(toks[i])
    while i < len(toks):
        if re.fullmatch(r"[A-Za-z]", toks[i]):
            cmd = toks[i]
            i += 1
            if cmd in "Zz":
                cur = start
                continue
        rel = cmd.islower()
        c = cmd.upper()
        if c == "M":
            x, y = num(), float(toks[i + 1]); i += 2
            cur = (cur[0] + x, cur[1] + y) if rel else (x, y)
            start = cur; pts.append(cur); cmd = "l" if rel else "L"
        elif c == "L":
            x, y = num(), float(toks[i + 1]); i += 2
            cur = (cur[0] + x, cur[1] + y) if rel else (x, y); pts.append(cur)
        elif c == "H":
            x = num(); i += 1
            cur = (cur[0] + x, cur[1]) if rel else (x, cur[1]); pts.append(cur)
        elif c == "V":
            y = num(); i += 1
            cur = (cur[0], cur[1] + y) if rel else (cur[0], y); pts.append(cur)
        elif c == "C":
            v = [float(t) for t in toks[i:i + 6]]; i += 6
            if rel:
                v = [v[k] + cur[k % 2] for k in range(6)]
            p0, p1, p2, p3 = cur, (v[0], v[1]), (v[2], v[3]), (v[4], v[5])
            for s in range(1, steps + 1):
                t = s / steps
                a, b, c_, e = (1 - t) ** 3, 3 * t * (1 - t) ** 2, 3 * t * t * (1 - t), t ** 3
                pts.append((a * p0[0] + b * p1[0] + c_ * p2[0] + e * p3[0], a * p0[1] + b * p1[1] + c_ * p2[1] + e * p3[1]))
            cur = p3
    return pts


def main():
    svg = SVG.read_text()
    paths = re.findall(r'<path[^>]*? d="([^"]+)"[^>]*?fill="(#[0-9a-fA-F]{6})"', svg)
    red = next(path_points(d) for d, f in paths if f.lower() == "#cc2229")
    yel = next(path_points(d) for d, f in paths if f.lower() == "#f6d330")
    xs, ys = [p[0] for p in red], [p[1] for p in red]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    s = 0.60 * W * SS / (x1 - x0)
    ox = W * SS / 2 - (x0 + x1) / 2 * s
    oy = H * SS / 2 - (y0 + y1) / 2 * s
    tr = lambda pts: [(x * s + ox, y * s + oy) for x, y in pts]
    im = Image.new("RGB", (W * SS, H * SS), (244, 244, 240))
    dr = ImageDraw.Draw(im)
    rim = 22 * SS
    dr.rectangle([0, 0, W * SS - 1, H * SS - 1], outline=(70, 74, 80), width=rim)
    dr.polygon(tr(red), fill=(204, 34, 41))
    dr.polygon(tr(yel), fill=(246, 211, 48))
    OUT.parent.mkdir(exist_ok=True)
    im.resize((W, H), Image.LANCZOS).save(OUT, optimize=True)
    print(OUT, OUT.stat().st_size)


main()
