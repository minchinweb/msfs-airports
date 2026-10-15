"""Rewrite this folder's DEM clips from NRCAN-Edmonton_2018-1m. Delete after use."""
import json, os
import rasterio
from rasterio.windows import from_bounds
from pyproj import Transformer

HERE = os.path.dirname(os.path.abspath(__file__))
DEM = "https://canelevation-dem.s3.ca-central-1.amazonaws.com/hrdem-lidar/NRCAN-Edmonton_2018-1m-%s.tif"
ortho = json.load(open(os.path.join(HERE, "aerial", "ortho-2019.json"), encoding="utf-8"))
to3979 = Transformer.from_crs(3776, 3979, always_xy=True)
x0, x1, y0, y1 = ortho["xmin"], ortho["xmax"], ortho["ymin"], ortho["ymax"]
corners = [to3979.transform(x, y) for x in (x0, x1) for y in (y0, y1)]
bx = (min(c[0] for c in corners), min(c[1] for c in corners), max(c[0] for c in corners), max(c[1] for c in corners))
print("bounds 3979", bx)
for k in ("dtm", "dsm"):
    with rasterio.open(DEM % k) as ds:
        win = from_bounds(*bx, ds.transform).round_offsets().round_lengths()
        a = ds.read(1, window=win)
        print(k, a.shape, "nodata frac", float((a == ds.nodata).mean()) if ds.nodata is not None else "n/a")
        prof = dict(
            driver="GTiff",
            height=a.shape[0],
            width=a.shape[1],
            count=1,
            dtype="float32",
            crs=ds.crs,
            transform=ds.window_transform(win),
            nodata=ds.nodata,
            compress="deflate",
            predictor=3,
        )
        out = os.path.join(HERE, "elevation", f"{k}-2018-1m.tif")
        with rasterio.open(out, "w", **prof) as o:
            o.write(a, 1)
        print("wrote", out)
