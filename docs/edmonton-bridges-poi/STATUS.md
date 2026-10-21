# Edmonton POI markers

Package `scenery-edmonton-bridges-poi` (0.1.0). One `<LandmarkLocation type="POI">` (216 markers, 2026-10-19) for every location with a centre: every structure boxed in `docs/edmonton-bridges/PRIORITY.md` (all sections, including 6 excluded and 9 do not model, e.g. G118, P147, P148, T136, Z124, P182-P189), every `draw-map.py` catalogue entry (river, freeway, skipped, LRT structures and stations, so Clover Bar, Sherwood Park, Stony Plain and Highway 16/16A crossings are in), and the built extras from `placements.json` (B254, B255, F256, V257, N258-N260). Name is the bare code (`H39`). At-grade track sections (K190-K253) have no point centre and no marker.

Regenerate: `python -I scenery-edmonton-bridges-poi/tools/gen_poi.py`, then `build.bat scenery-edmonton-bridges-poi`.

- Centres: `draw-map.py` catalogue, else "Centre lat, lon" in the box line. B264, B267 and B274 have no sourced centre; `EXTRA` in `gen_poi.py` holds estimates (B264 midway between B263 and B265 on 83 Street; B267 midpoint of OSM road way 31849128 "51069 Range Road 215", Strathcona County, about 53.385, -113.070, not near Redwater; B274 at 97 Street and 102 Avenue). All three are approximate and need a survey.
- `alt` is the site datum from placements.json where there is one, else 650 m; `offset` 40 m lifts the marker. Not checked in the sim: if markers sit underground or too high, change `GROUND_DEFAULT` / `OFFSET` in `gen_poi.py`.
- `distToShowMarker` 20 km.
- Built 2026-10-17, not seen in the sim. Needs a sim restart, and markers must be enabled in the sim's marker visibility settings.
