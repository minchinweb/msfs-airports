# H28 / CEQ4 Whetstone International: status

Project: `airport-h28/airport-H28-del-bonita-whetstone-intl.xml` (package `cardboardgt-airport-h28-whetstone`, v0.0.1). Spec and decisions: `SPEC.md`. Build: `.\build.bat h28` (sim closed; see CLAUDE.md build notes).

## Built (2026-10-27, builds OK, not yet seen in the sim)
- `Airport` H28, name "Whetstone Intl (CEQ4)", marker moved to the runway midpoint (48.99868, -112.77713), magvar 12.5, test radius 2,000 m.
- One runway numbered 07 (the sim would call it 08/26), true heading 89.97, 1,353 m x 20 m, centred on the sim default runway's midpoint (so 120 m trimmed from each end of the default 1,594 m). Surface `{322DE917-E25D-4AD8-BFBB-4D5F4D259413}`, which the user found in the Project Editor and thinks is striped grass.
- Starts about 30 m in from each end; 122.8 CTAF.
- Four small GA tie-downs, two north and two south of the runway about 100 m from the west end, with grass taxi paths (`drawSurface` false) and a windsock on the north side.

## Not done yet
- Check in the sim: that the runway reads 07/25 and matches the aerial strip, and that the grass surface looks right (plain vs striped).
- Runway position and length were not measured against imagery (the spec's to-do); the border straddle is only as good as the sim default (centreline 48.99868, about 12 m north of the OSM boundary).
- Vegetation-exclusion polygon (only the runway's `excludeVegetationAround` is set), threshold double cones, edge cones, fences, mowed polygon.
- PAPI on 07, threshold reflectors; the port of entry buildings and lights; the power line; RNAV 25 and RNAV-A.
- A world-map search for "CEQ4".

## 2026-10-27 update
- Sim check by user: north-south alignment perfect (aerial cones visible); grass looks striped up close.
- Runway now keeps the sim's old east end (lon -112.766217) and is cut at the west (centre -112.77548). Tie-downs, taxi points and windsock shifted +0.0033 deg lon to follow.
- Added `DeleteAirport` (all TRUE) to remove the default 08/26 runway; PAPI-2 (3.5 deg) on 07 added. Both build clean; not yet seen in the sim.
- Still to do: cones, fences, mowed polygon, port buildings, power line, RNAV approaches.

## 2026-10-27 (later): polygon, approach, magvar

- Library GUIDs (fence, cone, pole, sign) still needed from the Scenery Editor; VectorPlacement/LibraryObject syntax is confirmed from the SDK docs (see chat notes).
- Fixed airport `magvar`: was 12.5 (which the XML reads as west); now 347.09 (12.91 E, matching Little Navmap's value).
- Added a vegetation/building exclusion polygon over the strip and the west parking (L shape; strip south edge = border line, fence = runway west end).
- Added fictional RNAV (GPS) RWY 25: IF WH25I 10 NM, FAF WH25F 5 NM, MAP at the threshold, MDA 4800 ft, missed climb then hold at WH25I. Waypoint region "K2" is a guess. Unverified in the sim.
- Not yet done: RNAV (GPS)-A circling, mowed-grass material polygon (needs a material GUID), buildings. North parking spots (lat 48.99908) are about 25 m north of the strip's north edge; move them if the real layout is south only.

## 2026-10-27 (evening)

- magvar now written as -12.91 (negative = east, per the SDK docs); same meaning as 347.09.
- Added: wooden power pole, 43 white cones (south edge: 62/95/127 m then every 61 m; north edge from 202 m every 61 m; extra at 202 and 266 m where red-white pairs sit; red cone model still missing), 7-wire farm fence along the west side and parking (spacing 5 m is a guess), fence posts at corners, "Runway Grass" and "Taxi Grass" material polygons, RNAV (GPS)-A circling approach (final course 300 magnetic, MAP over the field, MDA 5000). Approach comments now spell out IF/FAF/MAP/TF/CA/DF/HM.
- WARNING: opening the project in the Scenery Editor re-saves H28.xml and DROPS the Waypoint and Approach elements (seen 2026-10-27). Keep the approaches out of any editor round-trip or re-run `gen_h28.py`-style insertion afterwards.
- The user's H28v2 / H28v3 folders in the main checkout are Scenery Editor saves of this project (cone test placement, polygon v0.5.0).

## Cones (2026-10-27)

- `airport-h28/tools/gen_cones.py` builds two glTF models into `PackageSources/modelLib/` (white cone with a black top, and an all-red cone; 0.45 m tall, 0.4 m base) plus `texture/h28_palette.png`, adds a ModelLib group to the package definition, swaps the library cone in H28.xml for the white model and places red cones 1.5 m east of the white cones at 202 m and 266 m (3 of them; the north edge has no cone at 266 m). Re-run it after any regeneration of the cones. Models compile (`modellib.bgl`); not seen in the sim yet.

## Layout pass (2026-10-27, late)

`airport-h28/tools/fix_h28_layout.py` (re-runnable): removed the Runway/Taxi Grass material polygons; runway stays 20 m wide, with a second striped-grass Apron (37 m wide, full strip length) around it; striped-grass `Apron` over the parking area (tiling/heading guessed, stripe direction unchecked); 4 parking spots + 2 taxi points inside the parking area; cones scaled x3, in pairs at the same stations on both edges (62, 95, 127, then 202 and every 61 m to the east mark at 1152 m), red cone 1.5 m inboard of the white at 202 m and 1152 m on both edges; power pole heading 90; fence replaced by two lines of wooden posts (first post model, 6 m spacing) 13.4 m either side of the centreline along the runway length (FAA: 4 ft fences 44 ft left and right). Road-side and parking perimeter fences dropped. Build NOT run: the sim was open (exit 2); rebuild with the sim closed.

## Port of entry and village (2026-10-27)

`airport-h28/tools/gen_port.py` (re-runnable) builds ten flat-colour glTF models into `modelLib/h28_port_*` (palette `texture/h28_port_palette.png`) and writes their placements and a building-exclusion polygon each into H28.xml between `BEGIN/END port of entry and village`.
- Canada (north of the border): CBSA main building with an inspection canopy over the highway lane, plus four sheds.
- US (south): CBP main building with canopy, a booth/outbuilding, a shed, and two stables (the "village").
- Footprints and sizes are OSM's (Overpass via the mail.ru mirror). Heights, colours and canopies are estimates; no Street View photos of the ports are in the repo yet.
- **Position assumption to check:** OSM's highway is at lon -112.7884, about 270 m west of the sim's road. Every OSM position is shifted 246 m east (`DX`) so the highway lines up 20 m west of the strip's west fence. If the ports sit wrongly in the sim, change `DX` and re-run.
- Night: window strips and canopy undersides use an emissive material; untested whether it glows only at night. Pole lights and the facade textures are still to do.
- Built OK (`_RPTErrors.xml` empty); not yet seen in the sim.

## Power line and pole lights (2026-10-27)

`airport-h28/tools/gen_powerline.py` (run `gen_port.py` first; it owns the palette): three-wire spans (9.4 m up, 1.2 m sag, 60 m long) north and south of the existing pole on the border line, library poles at each span end, and four orange marker balls on the first span north (across the strip). Also a pole-light model (7 m steel pole, lamp head, `ASOBO_macro_light` night-only light) with four placed around each main port building's plaza (8 lights total).
- Unchecked in the sim: wire height against the library pole's real height, whether the pole's cross-arm lines up with the wires, light direction and brightness (intensity 3000, cone 120, symmetric), and that `day_night_cycle` means night-only.
- Built OK (`_RPTErrors.xml` empty).

## Rework pass (2026-10-28): runway, fences, cones, power line, port positions

Built OK with the sim closed (`_RPTErrors.xml` empty); not yet seen in the sim. Supersedes the layout, cone, fence, power-line and `DX` notes above. Re-run order: `gen_port.py`, `gen_cones.py`, `gen_field.py`, `gen_powerline.py` (all in `airport-h28/tools/`). `fix_h28_layout.py` is gone; `gen_field.py` replaces it.

- **The sim aerial matches OSM** (DevMode top-down 2026-10-28: road centre at -112.7884). The old 246 m east shift of the buildings (`DX`) came from cutting the runway too short at the west. `DX` is now 0, so our buildings sit on the sim's generated ones, and their exclusion polygons remove those.
- **Runway** keeps its centreline and east end (-112.766217). The west end goes back to the sim default (-112.788063, 6 m inside the west fence), so it is 1,595 m x 65 ft. The published 4,440 ft lies between the threshold double cones: 200 m east of the west fence (where the 2012 red-white cones are) and 4,440 ft further east, about 49 m from the east fence. The marker is at the new midpoint (-112.77714). PAPI `biasX` is 12 m (inside the fence). Unclear: the SDK says `biasZ` is measured from the runway centre, FSX measured it from the end, so check where the PAPI lands.
- **Fenced field**, from the OSM aerodrome outline (way 1208466528) and Google Earth 2012: strip fences 13.4 m (44 ft) each side of the centreline over the full length (the south one on the border); west fence at -112.78815; US parking 138 x 77 m south of the border at the west end; Canadian pocket 74 m long, out to 24 m north of the centreline. The fence is our own glTF (wooden posts every 5 m, four wires): 8 edge models `h28_fence_0..7`, 175 placements. Striped-grass aprons cover strip, pocket and parking; the no-vegetation/buildings polygon covers the whole field out to the road shoulder.
- **Cones**: the side faces were wound inside-out (only the inner face drew); fixed in `gen_cones.py`. Model is now squatter (0.6 m tall, 0.9 m base), placed at scale 2. White cones on both edges (9.9 m off the centreline) evenly spaced about 200 ft between the threshold stations, plus 62/95/127 m in the west overrun. A red cone sits 2 m outboard of the white one at each threshold.
- **Tie-downs**: 4 in the US parking (30 m south of the border, nose north), 2 in the Canadian pocket (radius 6 m), taxi paths to a runway entry point 70 m from the west fence.
- **Power lines** (own pole models with the cross-arm at 9.4 m and wires at 9.5 m = the FAA's 31 ft): south line from the road shoulder to a transformer pole in the US parking (33 m east of the fence, 70 ft south of the centreline), then east to a pole by the windsock, with balls on that span. North line: road to a dead-end pole just north of the Canadian pocket. Neither crosses the strip. Routing is read from the photos; low confidence on the north line and on where the south line ends.
- **CBSA** office: no canopy (the 2025 photos show none), white walls, grey roof; its pole lights are by the lane on its west side.
- Windsock: NE corner of the US parking, on the border line.

To check in the sim: cone faces; fence look (posts and wires visible?); wire and cross-arm heights; PAPI position; tie-downs clear of the fences; that buildings overlap the aerial's.
Ideas not done: CBSA lattice radio mast (photo 05), facade textures, a gate in the west fence.

## Road props and night lighting (2026-10-28, later)

Built OK (sim closed, `_RPTErrors.xml` empty); not yet seen in the sim. Run order is now `gen_port`, `gen_cones`, `gen_field`, `gen_powerline`, `gen_props`.
- `gen_props.py`: `h28_barrel` (orange/white traffic drum with a black base, 0.95 m) and `h28_jersey` (12.5 ft concrete New Jersey profile). 16 drums along the CBSA lane divider: OSM way 1147664053 (barrier=bollard) every 5 m, plus 3 at its ends. In reality the divider is tall delineator posts with drums at the ends; here all of them are drums, as asked. 20 Jersey barriers in a row on the west edge of the grass island between the CBP inspection lane and the through road, lat 48.99640-48.99712. **That position is a guess**; no photo in the repo shows them.
- Lighting review: the lights were `ASOBO_macro_light`, which is deprecated in MSFS 2024 (the SDK's Blender add-on converts it to a street light). They are now `ASOBO_street_light` (names from the SDK's `io_scene_gltf2_msfs_2024/blender/msfs_lights.py`): night only, `flare_enabled` true (the lens flare is what shows from a distance), beam turned straight down (node -Z rotated to -Y; check that it isn't pointing up), warm white.
  - Plaza lights: 8 m, 6,000 cd, 140 deg cone, 4 per port.
  - New highway lights: 10 m, 2.5 m arm over the road, 10,000 cd, 6 of them on the east shoulder from the CBSA lane to the CBP approach. One is at the border, at the runway's west end, as a beacon for the 07 threshold.
  - The emissive windows and the CBP canopy underside are unchanged (always lit, day too).
- To check at night: flares visible from 5-10 nm; light pools on the ground under the lamps; whether brighter lamps or more of them are needed.

## In-sim fixes (2026-10-28, after the first in-sim look)

- **Lights:** the beams pointed up. The SDK's Blender exporter (`io/com/msfs_light_extensions.py`) adds a 180° X turn to every light, so an MSFS light shines along node +Z; down is the rotation `[0.7071, 0, 0, 0.7071]`. Each lamp also has an all-round, flare-only light (30,000 cd, 360°) so it shows from the air. Beams are now 165°. Unverified in the sim.
- **Exclusions:** `ExclusionFlags` is a bitmask (1 roads, 2 street lights, 4 power lines, 8 feature points; SDK Scenery XML Properties). The field polygon and a new corridor polygon use 6 and ExcludeTIN. The corridor (`gen_port.CORRIDOR`) covers both ports and the road between them. It removes the sim's buildings, street lights and power lines, and clears trees 15–20 m back from our buildings.
- **CBSA office:** now a drive-through (`gen_port.drive_through`): grey siding, an open north–south bay with a lit ceiling, and a red-gabled annex at the south-west. It is 6 m east of the OSM footprint so the sim's road traffic clears it. Its four pole lights stand 8 m off the north and south faces, either side of the bay. Shed colours: shed2 cream, shed4 brown.
- **Cones:** the sim culled lone 1.2 m cones after about four pairs. Each station is now one model across the runway: `h28_cones_edge` has the two white cones, and `h28_cones_07` has white and red on both edges, red 2 m outboard (heading 0 at 07, 180 at 25). The red cones were already on the edge lines; the photo's inward offset is perspective.

## Second in-sim pass (2026-10-28)

- **Lights at distance:** only the PAPI showed from about 1 NM. The lamps were lone 8–10 m models, and the sim culls small models (and their lights with them) by their size on screen, as it did the cones. Each side's lamps are now one model: `h28_lights_ca` has the 4 CBSA plaza lamps and the 2 road lights north of the border, about 90 m across. `h28_lights_us` has the 4 CBP lamps and the 4 road lights south of the border, about 240 m across. They are built by `gen_powerline.merge`. The flare-only light is now 60,000 cd. Unverified in the sim.
- **CBSA detail** (seen from the US parking start, a few hundred feet away; after refs 04–08):
  - The office block is grey siding with pilasters, framed lit windows, doors, a white fascia and dark cap, a navy "Del Bonita" sign over the bay, a roof unit and a roof pole.
  - The open north–south drive-through bay (`BAY`) has a concrete floor, yellow bollards, a lit ceiling and inspection windows on both sides.
  - The cream annex is on the east, with red gable ends, white trim, a shingle roof (ridge north–south) and a chimney.
  - There is a Canadian flag on a 9 m pole (the maple leaf is ear-clipped geometry from `gen_port.LEAF`; CYXD has no flag texture to borrow), and a 42 m three-legged lattice radio mast east-south-east, with cross-arms, antennas and a cabinet.
  - Garages (`gen_port.garage`) have low gables, white corner boards and fascia, and sectional doors on the road side. shed1 and shed3 are white doubles; shed2 and shed4 are cream singles, so shed4 is no longer brown.
- The layout of the CBSA faces was worked out from the photos. From the south you see the office at the left, then the bay, then the red gable, with the mast behind. Refs 05, 06 and 08 look north at the south face, and ref 04 looks south at the north face. The tiny brown shed in ref 04 is not in OSM and is not modelled.

## Lamp heights and roof colour (2026-10-30)

Built OK (sim closed, `_RPTErrors.xml` empty); not yet seen in the sim.
- **Merged lamps follow the ground:** a merged light model is placed at one altitude, so the lamps were all level with its origin, and some floated. `gen_powerline.py` now raises or lowers each lamp by its ground height relative to the model origin. The heights come from the USGS EPQS (3DEP 1 m LiDAR, which covers both sides of the border here) and are cached in `airport-h28/tools/ground.json`, so re-runs work offline; delete the file to re-fetch. LiDAR offsets: Canadian lamps within 0.3 m; the US road lights 1.4–2.2 m below the CBP origin, the US plaza lamps 0.2–0.8 m below it. Lamp poles also run 4 m into the ground (`SINK`) to cover differences between the sim's terrain and the LiDAR. If lamps still float, the sim's terrain differs by more than that; raise `SINK` or check in DevMode.
- **CBSA roofs:** the garage roofs were `GREY` (170,174,176), close to white in the sim; the colour had not been dropped. The 2025 Street View (refs 04, 05) shows slate-grey shingles, so garages and the annex now use a new `SLATE` swatch (104,112,124), added at the end of the palette. The office's flat roof stays `TRIM`. Adding a swatch moves every palette UV, so re-run all the generators in order after any palette change.

## Flashing red beacons (2026-10-31)
- `gen_port.BEACON`: red, all-round, flare-only, night-only, 30 flashes a minute, 60,000 cd (`flash_frequency` is per minute, `flash_duration` in seconds; `Mesh.lights` entries take an optional 7th item, a dict of `ASOBO_street_light` overrides). One sits on a post above the CBSA radio mast; one tops the border road light at the runway's west end (lat 48.99853, in `h28_lights_us`). Regenerated with `gen_port.py` then `gen_powerline.py`. Not yet built or checked in the sim.

## Welcome to Alberta sign (2026-11-07)

`airport-h28/tools/gen_sign.py` (own marker block in H28.xml; independent of the palette, so it runs in any order). Reworked the same day to match `reference/fbgroup-02-alberta-welcome-sign.jpg`:
- The model has its own 2048 x 2048 texture (`texture/h28_sign_alberta.png`, linear filtering with mipmaps): the board face with real lettering (Arial Bold, each line stretched to its box in the photo), the wild rose decal (pink flower, bud, teal leaves, black outline, white sticker edge), a lighter frame round a recessed rough-sawn panel, plus wood, gravel, concrete, soil and end-grain swatches. The back is plain wood.
- Geometry is measured off the photo, with the board taken as 16 ft (4.88 m) wide: board 1.42-3.90 m up, tall 12 x 12 in posts (4.36 m), shorter outer posts (3.44 m left, 2.89 m right), legs under the board ends, a gravel bed with timber edging, and a cream planter in front of the right posts.
- **Position from Esri imagery** (`fetch_esri.py`, new `alberta-sign.png` clip): the gravel pad shows at the north edge of the house yard north of the CBSA sheds, 22.4 m east of the road centre, square to the road. Placed at 49.00066, -112.78809, facing south. The old estimate was 49.00150, about 95 m too far north.
- Built OK (sim closed, `_RPTErrors.xml` empty; texture compiled to KTX2). Not yet seen in the sim. To check: the lettering reads the right way round; the sign isn't culled at a distance, since a lone 7 m model may vanish the way the lone cones did. If it is culled, merge it into a larger model. Also check whether the CBSA sheds hide it from the US parking, about 250 m south.
