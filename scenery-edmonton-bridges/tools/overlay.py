"""Draw a site model's plan view over the City 2019 orthophoto to check position, heading and pier stations.

    python -I overlay.py <site> <reference-folder> <out.png> [crop_m]

e.g. python -I scenery-edmonton-bridges/tools/overlay.py r10 R10-high-level out.png
The orthophotos are gitignored (docs/edmonton-bridges/fetch-site-data.py regenerates them).  Needs numpy, Pillow, pyproj.
"""
import importlib, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bridgelib import ROOT, PALETTE  # noqa: E402


def main(site, folder, out, crop=None):
    import numpy as np
    from PIL import Image, ImageDraw
    from pyproj import Transformer
    Image.MAX_IMAGE_PIXELS = None
    res = importlib.import_module("site_" + site).build()
    fr = res["frame"]
    ref = ROOT / "docs/edmonton-bridges/reference" / folder / "aerial"
    j = json.load(open(ref / "ortho-2019.json"))
    im = Image.open(ref / "ortho-2019.jpg").convert("RGB")
    t = Transformer.from_crs(4326, 3776, always_xy=True)
    px = j["pixel_m"]
    over = Image.new("RGBA", im.size, (0, 0, 0, 0))
    dr = ImageDraw.Draw(over)
    ll0 = res["lon0"], res["lat0"]

    def pix(e, n):
        la, lo = fr.ll(e, n)
        x, y = t.transform(lo, la)
        return ((x - j["xmin"]) / px, (j["ymax"] - y) / px)
    tris = []
    for _name, m in res["parts"]:
        P, N, U, I = m.pos, m.nrm, m.uv, m.idx
        for k in range(0, len(I), 3):
            a, b, c = I[k], I[k + 1], I[k + 2]
            if N[a][1] > 0.5:
                tris.append(((P[a][1] + P[b][1] + P[c][1]) / 3, [pix(P[v][0], P[v][2]) for v in (a, b, c)], int(U[a][0] * len(PALETTE))))
    tris.sort(key=lambda r: r[0])
    for _y, pts, sw in tris:
        c = PALETTE[sw]
        dr.polygon(pts, fill=(255, 40, 40, 110), outline=(255, 255, 0, 160))
    im = Image.alpha_composite(im.convert("RGBA"), over).convert("RGB")
    cx, cy = pix(0, 0)
    if crop:
        r = crop / px
        im = im.crop((int(cx - r), int(cy - r), int(cx + r), int(cy + r)))
    im.thumbnail((2000, 2000))
    im.save(out)
    print(out, im.size)


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2], a[3], float(a[4]) if len(a) > 4 else None)
