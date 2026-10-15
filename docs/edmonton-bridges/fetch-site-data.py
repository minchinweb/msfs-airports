"""Fetch City of Edmonton 2019 orthophoto and NRCan/City 2018 LiDAR DEM clips for each bridge reference folder.

Run with the venv that has rasterio, pyproj, numpy, pillow:  python fetch-site-data.py [site ...]
Writes reference/<site>/aerial/ortho-2019.jpg (+ .json with bounds) and reference/<site>/elevation/{dtm,dsm}-2018-1m.tif
and prints river-surface and deck statistics. Re-runnable.
"""
import glob, io, json, math, os, sys, urllib.request
import numpy as np, rasterio
from rasterio.windows import from_bounds
from pyproj import Transformer
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ORTHO = "https://gis.edmonton.ca/site1/rest/services/Imagery_Public/2019_RGB_Pictometry/ImageServer/exportImage"
DEM = "https://canelevation-dem.s3.ca-central-1.amazonaws.com/hrdem-lidar/AB-Edmonton-1m-%s.tif"
to3979 = Transformer.from_crs(4326, 3979, always_xy=True)
to3776 = Transformer.from_crs(4326, 3776, always_xy=True)
MARGIN, MINHALF, RES = 120.0, 250.0, 0.2

def points(o, out):
    if isinstance(o, list):
        if len(o) == 2 and all(isinstance(v, (int, float)) for v in o) and 53 < o[0] < 54 and -114 < o[1] < -113:
            out.append(o)
        else:
            for v in o: points(v, out)
    elif isinstance(o, dict):
        for v in o.values(): points(v, out)

def site_bounds(folder):
    d = json.load(open(os.path.join(folder, "geometry.json")))
    pts = []; points(d, pts)
    lat = [p[0] for p in pts]; lon = [p[1] for p in pts]
    clat, clon = d["centre"]
    ky = 111320.0; kx = 111320.0 * math.cos(math.radians(clat))
    half_y = max(MINHALF, max(abs(max(lat) - clat), abs(min(lat) - clat)) * ky + MARGIN)
    half_x = max(MINHALF, max(abs(max(lon) - clon), abs(min(lon) - clon)) * kx + MARGIN)
    return clat, clon, half_x, half_y

def fetch_ortho(x0, y0, x1, y1, out, RES=RES):
    w = int((x1 - x0) / RES); h = int((y1 - y0) / RES)
    img = Image.new("RGB", (w, h)); T = 2000
    for ty in range(0, h, T):
        for tx in range(0, w, T):
            tw, th = min(T, w - tx), min(T, h - ty)
            bx0 = x0 + tx * RES; bx1 = bx0 + tw * RES
            by1 = y1 - ty * RES; by0 = by1 - th * RES
            q = f"{ORTHO}?bbox={bx0},{by0},{bx1},{by1}&bboxSR=3776&imageSR=3776&size={tw},{th}&format=jpg&f=image"
            img.paste(Image.open(io.BytesIO(urllib.request.urlopen(urllib.request.Request(q, headers={"User-Agent": "curl/8.0 msfs-airports-reference-fetch"}), timeout=180).read())), (tx, ty))
    img.save(out, quality=82)
    return w, h

def main():
    want = sys.argv[1:]
    folders = sorted(set(os.path.dirname(f) for f in glob.glob(os.path.join(HERE, "reference", "**", "geometry.json"), recursive=True)))
    for folder in folders:
        name = os.path.relpath(folder, os.path.join(HERE, "reference")).replace("\\", "/")
        if want and not any(w in name for w in want): continue
        clat, clon, hx, hy = site_bounds(folder)
        cx, cy = to3776.transform(clon, clat)
        res = max(RES, round(2 * max(hx, hy) / 8000, 2))  # keep the long side under about 8000 px
        x0, x1, y0, y1 = [round(v / res) * res for v in (cx - hx, cx + hx, cy - hy, cy + hy)]
        os.makedirs(os.path.join(folder, "aerial"), exist_ok=True)
        os.makedirs(os.path.join(folder, "elevation"), exist_ok=True)
        png = os.path.join(folder, "aerial", "ortho-2019.jpg")
        w, h = fetch_ortho(x0, y0, x1, y1, png, res)
        json.dump({"source": "City of Edmonton Imagery_Public/2019_RGB_Pictometry ImageServer", "crs": "EPSG:3776 (NAD83(CSRS) / 3TM 114)",
                   "pixel_m": res, "width": w, "height": h, "xmin": x0, "xmax": x1, "ymin": y0, "ymax": y1,
                   "note": "north up; world file semantics: pixel (c,r) -> x=xmin+(c+0.5)*pixel_m, y=ymax-(r+0.5)*pixel_m"},
                  open(png.replace(".jpg", ".json"), "w"), indent=1)
        # DEM clips in EPSG:3979
        corners = [to3979.transform(*to3776.transform(x, y, direction="INVERSE")) for x in (x0, x1) for y in (y0, y1)]
        bx = (min(c[0] for c in corners), min(c[1] for c in corners), max(c[0] for c in corners), max(c[1] for c in corners))
        for k in ("dtm", "dsm"):
            with rasterio.open(DEM % k) as ds:
                win = from_bounds(*bx, ds.transform).round_offsets().round_lengths()
                a = ds.read(1, window=win)
                prof = dict(driver="GTiff", height=a.shape[0], width=a.shape[1], count=1, dtype="float32", crs=ds.crs,
                            transform=ds.window_transform(win), nodata=ds.nodata, compress="deflate", predictor=3)
                with rasterio.open(os.path.join(folder, "elevation", f"{k}-2018-1m.tif"), "w", **prof) as o:
                    o.write(a, 1)
        print(name, "ortho", w, h, "dem", a.shape, flush=True)

if __name__ == "__main__":
    main()
