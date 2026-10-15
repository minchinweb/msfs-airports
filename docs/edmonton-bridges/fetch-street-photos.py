"""Download Mapillary street-level frames near each bridge into reference/<site>/street/ with a SOURCES.md.
Run: python fetch-street-photos.py [site-substring ...]   (needs mapbox-vector-tile: pip install mapbox-vector-tile)
Token: env MAPILLARY_TOKEN, or the first line of the file named by env MAPILLARY_TOKEN_FILE. Never commit the token.
The images search endpoint returns nothing for this app, so candidates come from the z14 vector tiles and each pick is
fetched by id. Mapillary images are CC BY-SA 4.0 (credit the creator). Panoramas are skipped."""
import glob, json, math, os, sys, time, urllib.request
import mapbox_vector_tile as mvt
HERE = os.path.dirname(os.path.abspath(__file__))
TOK = os.environ.get("MAPILLARY_TOKEN") or open(os.environ["MAPILLARY_TOKEN_FILE"]).read().strip()
UA = {"User-Agent": "msfs-airports-reference/1.0"}
RADIUS, PICKS, Z = 80.0, 5, 14

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()

def points(o, out):
    if isinstance(o, list):
        if len(o) == 2 and all(isinstance(v, (int, float)) for v in o) and 53 < o[0] < 54 and -114 < o[1] < -113: out.append(o)
        else:
            for v in o: points(v, out)
    elif isinstance(o, dict):
        for v in o.values(): points(v, out)

def tile_of(lat, lon):
    n = 2 ** Z
    return int((lon + 180) / 360 * n), int((1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n)

def tile_images(x, y):
    t = mvt.decode(get(f"https://tiles.mapillary.com/maps/vtp/mly1_public/2/{Z}/{x}/{y}?access_token={TOK}"))
    n = 2 ** Z; out = []
    for f in t.get("image", {}).get("features", []):
        px, py = f["geometry"]["coordinates"]; ext = 4096
        lon = (x + px / ext) / n * 360 - 180
        lat = math.degrees(math.atan(math.sinh(math.pi * (1 - 2 * (y + 1 - py / ext) / n))))
        out.append((lat, lon, f["properties"]))
    return out

def dist(a, b):
    return math.hypot((a[0] - b[0]) * 111320, (a[1] - b[1]) * 111320 * math.cos(math.radians(a[0])))

def bearing_gap(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)

for folder in sorted(set(os.path.dirname(f) for f in glob.glob(os.path.join(HERE, "reference", "**", "geometry.json"), recursive=True))):
    name = os.path.relpath(folder, os.path.join(HERE, "reference")).replace(os.sep, "/")
    if sys.argv[1:] and not any(s in name for s in sys.argv[1:]): continue
    g = json.load(open(os.path.join(folder, "geometry.json"))); pts = []; points(g, pts); pts.append(g["centre"])
    tiles = {tile_of(*p) for p in pts}
    tiles |= {tile_of(p[0] + dy, p[1] + dx) for p in pts for dy in (-.001, .001) for dx in (-.0015, .0015)}
    allimg = [(lat, lon, pr) for x, y in tiles for lat, lon, pr in tile_images(x, y) if not pr.get("is_pano")]
    for rad in (RADIUS, 250.0):  # widen once if the bridge has no frames close by
        cand = {pr["id"]: (lat, lon, pr, d) for lat, lon, pr in allimg for d in [min(dist((lat, lon), p) for p in pts)] if d <= rad}
        if cand: break
    year = lambda pr: time.gmtime(pr["captured_at"] / 1000).tm_year
    ranked = sorted(cand.values(), key=lambda c: -(c[2].get("quality_score", 0) + 0.05 * max(0, year(c[2]) - 2015) - c[3] / 400))
    chosen = []
    for c in ranked:
        if all(c[2]["sequence_id"] != k[2]["sequence_id"] and (dist(c[:2], k[:2]) > 30 or bearing_gap(c[2]["compass_angle"], k[2]["compass_angle"]) > 60) for k in chosen):
            chosen.append(c)
        if len(chosen) == PICKS: break
    out = os.path.join(folder, "street"); rows = []
    if chosen: os.makedirs(out, exist_ok=True)
    for lat, lon, pr, d in chosen:
        i = pr["id"]
        det = json.loads(get(f"https://graph.mapillary.com/{i}?fields=id,captured_at,compass_angle,thumb_2048_url,creator&access_token={TOK}"))
        fn = f"mly-{i}.jpg"; dest = os.path.join(out, fn)
        if not os.path.exists(dest): open(dest, "wb").write(get(det["thumb_2048_url"])); time.sleep(0.5)
        who = (det.get("creator") or {}).get("username", "?")
        rows.append(f"| `{fn}` | {time.strftime('%Y-%m-%d', time.gmtime(det['captured_at'] / 1000))} | {who} | {det['compass_angle']:.0f} | {d:.0f} | https://www.mapillary.com/app/?pKey={i} |")
    if chosen:
        open(os.path.join(out, "SOURCES.md"), "w", encoding="utf-8").write(
            "# Street-level photos\n\nMapillary frames, 2048 px, licence CC BY-SA 4.0 (credit the creator). Daytime only, taken from the road, so they show railings, barriers, lamp posts, lane layout and approaches, not the underside. Heading is degrees true the camera faces; distance is metres from the nearest point of the bridge geometry. Chosen by quality score, recency and spread of viewpoint, one per capture sequence. Where a bridge has no frame within 80 m the search widens to 250 m (see the distance column).\n\n"
            "| File | Taken | Creator | Heading | Metres away | Page |\n| --- | --- | --- | --- | --- | --- |\n" + "\n".join(rows) + "\n")
    print(name, len(cand), "candidates,", len(chosen), "saved")
