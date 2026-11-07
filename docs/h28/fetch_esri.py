"""Download Esri World Imagery clips of Del Bonita / H28 into docs/h28/esri/ (gitignored).

    python -I docs/h28/fetch_esri.py

North is up. Each file is an export in WGS84; the bbox is west,south,east,north.
"""
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent / "esri"
# name: (bbox west,south,east,north, pixel size)
SHOTS = {
    "imagery-overview.png": ("-112.802,48.9935,-112.755,49.0065", "1400,900"),
    "imagery-west-end.png": ("-112.7925,48.9968,-112.7845,49.0006", "1600,1000"),
    "imagery-ports.png": ("-112.7925,48.9948,-112.7860,49.0012", "1400,1600"),
    "imagery-strip.png": ("-112.7885,48.9976,-112.7700,48.9996", "1800,500"),
    "strip-border.png": ("-112.7892,48.99815,-112.7720,48.99905", "2000,500"),
    "strip-road.png": ("-112.7896,48.9946,-112.7876,49.0014", "500,1800"),
    "alberta-sign.png": ("-112.7895,49.0000,-112.7865,49.0025", "1200,1400"),
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (bbox, size) in SHOTS.items():
        url = (
            "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/export"
            f"?bbox={bbox}&bboxSR=4326&imageSR=4326&size={size}&format=png&f=image"
        )
        req = urllib.request.Request(url, headers={"User-Agent": "h28-research/1.0"})
        dest = OUT / name
        with urllib.request.urlopen(req, timeout=90) as r:
            dest.write_bytes(r.read())
        print(f"{name}  {dest.stat().st_size} bytes  bbox {bbox}")


if __name__ == "__main__":
    main()
