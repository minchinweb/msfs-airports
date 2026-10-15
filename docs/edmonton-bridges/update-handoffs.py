"""Insert or refresh the 'elevation, aerial and night data' block in every reference/<site>/MODEL-HANDOFF.md.
Needs data/elevation-summary.json (analyze-elevation.py) and the elevation clips (fetch-site-data.py) for the ground height at the centre."""
import glob, json, os, re
import rasterio
from pyproj import Transformer
HERE = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(HERE, "data", "elevation-summary.json")))
t = Transformer.from_crs(4326, 3979, always_xy=True)
BEGIN, END = "<!-- data-update:begin -->", "<!-- data-update:end -->"
PICK = ("upper_deck", "road_deck", "lower_road_deck", "lrt_track", "east_track", "road", "pier")
for hp in sorted(glob.glob(os.path.join(HERE, "reference", "**", "MODEL-HANDOFF.md"), recursive=True)):
    folder = os.path.dirname(hp); name = os.path.relpath(folder, os.path.join(HERE, "reference")).replace("\\", "/")
    e = S.get(name)
    if not e: continue
    clat, clon = json.load(open(os.path.join(folder, "geometry.json")))["centre"]
    with rasterio.open(os.path.join(folder, "elevation", "dtm-2018-1m.tif")) as ds:
        x, y = t.transform(clon, clat); ground = float(next(ds.sample([(x, y)]))[0])
    ok = e["water_pixels_within_0.1m"] >= 20000
    deck = None
    for k in PICK:
        deck = next((d for d in e["decks"] if d["part"].startswith(k)), None)
        if deck: break
    rel = "../" * (len(name.split("/")) + 1)
    L = [BEGIN, "## Update 2026-10-14: elevation, aerial and night data now in this folder", "",
         f"- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): {ground:.1f} m ({ground * 3.28084:,.0f} ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`."]
    if ok: L.append(f"- **River surface here** (2018 LiDAR): {e['water_surface_mode_m']:.2f} m. Gauge conversion and the seasonal range (about ±0.5 m) are in `{rel}RIVER-LEVEL.md`.")
    else: L.append("- **River surface:** this clip holds no river reach, so no water figure applies. For a ravine or rail crossing use the ground heights above and below.")
    if deck: L.append(f"- **{'Roof' if 'outline' in deck['part'] and name.startswith('B255') else 'Main deck'} height** (`{deck['part']}`, DSM median): {deck['dsm_median']:.2f} m" + (f", {deck['median_above_water_m']:.2f} m above the river." if ok else ".") + " It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.")
    L.append(f"- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.")
    nd = os.path.join(folder, "night")
    n = len(glob.glob(os.path.join(nd, "*.jpg")))
    L.append(f"- **Night lighting:** {n} photos in `night/` with a lighting description in `night/SOURCES.md`." if n else "- **Night lighting:** no usable night photo found (see `" + rel + "DATA-SOURCES.md`).")
    sd = os.path.join(folder, "street")
    k = len(glob.glob(os.path.join(sd, "*.jpg")))
    L.append(f"- **Street-level photos:** {k} daytime Mapillary frames in `street/` (CC BY-SA, credits in `street/SOURCES.md`). They show railings, barriers, lamp posts, lane and sidewalk layout and approach shape from the road; not the underside or truss depth. Check them before treating those items below as open." if k else "- **Street-level photos:** none (no Mapillary frame within 250 m).")
    oq = os.path.join(folder, "OPEN-QUESTIONS.md")
    if os.path.exists(oq): L.append("- **Open questions:** the other session's review (`CURSOR-HANDOFF.md`) re-checked against this data, item by item, in `OPEN-QUESTIONS.md`. Read it before the blocking items below.")
    L += ["", "Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `" + rel + "BLOCKERS.md`.", END, ""]
    s = open(hp, encoding="utf-8").read()
    s = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n*", "", s, flags=re.S)
    s = s.replace("## Verdict", "\n".join(L) + "\n## Verdict", 1)
    open(hp, "w", encoding="utf-8").write(s)
    print("updated", name)
