# Edmonton POI markers

Package `scenery-edmonton-bridges-poi` (0.1.0). One `<LandmarkLocation type="POI">` per structure code boxed in `docs/edmonton-bridges/PRIORITY.md` sections 1-5, 7 and 8, plus the built extras from `scenery-edmonton-bridges/tools/placements.json` (B254, B255, F256, V257, N258-N260). Name is the bare code (`H39`). Section 6 (excluded) and section 9 (do not model) are left out.

Regenerate: `python -I scenery-edmonton-bridges-poi/tools/gen_poi.py` (`--include-excluded` adds section 6), then `build.bat scenery-edmonton-bridges-poi`.

- Centres: `draw-map.py` catalogue, else "Centre lat, lon" in the box line. No centre yet for B264, B267, B274 (need survey), so they have no marker.
- `alt` is the site datum from placements.json where there is one, else 650 m; `offset` 40 m lifts the marker. Not checked in the sim: if markers sit underground or too high, change `GROUND_DEFAULT` / `OFFSET` in `gen_poi.py`.
- `distToShowMarker` 20 km.
- Built 2026-10-17, not seen in the sim. Needs a sim restart, and markers must be enabled in the sim's marker visibility settings.
