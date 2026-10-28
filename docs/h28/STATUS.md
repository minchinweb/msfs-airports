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
