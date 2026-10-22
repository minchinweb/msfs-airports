# CYXD status and handoff notes

Last reviewed: 2026-10-22. Branch `agents/claude/1`. Package `airport-cyxd/` (source `PackageSources/Scenery/airport-cyxd/CYXD.xml`; package version is still 0.2.1 and there is no release note yet for any of the work below).

Era: deliberately a-historical, 1940-1985, with the surviving 2010-2014 hangars. Detail that is finished lives in the per-folder `SOURCES.md` files and in git history; this file keeps only what is current.

## Where things stand

- **Last in-sim checks:** approaches and ATIS (2026-10-09, after a full sim restart: ILS 34 Y, NDB 34 Z, NDB 16, LOC(BC) 16 Z, RNAV 12 Y, RNAV 30 Y all show); the NDB site models and textures (2026-10-10); Hangar 16 front offset (2026-10-17); a first in-sim look at the buildings, which produced the user-correction rounds of 2026-10-21.
- **Everything else below is built (last build exit 0, empty `_RPTErrors.xml`) but not viewed in the sim.** Restart the sim after a rebuild; a rebuild does not reload scenery in a running sim.
- **Not tested in the sim:** the CITY4 departure showing in the flight planner; the procedure-turn legs (`PI` + `CF` transitions, copied from the SDK `SimpleNavData` sample); jetway object orientation (Megalink for GATE 1 never seen); the fuel-truck service stands; whether the wind tee animation runs for a scenery `LibraryObject`.
- Open questions and the to-do list: `open-questions.md`. Reference link index: `reference-links.md`.

## Navigation and runways (in `CYXD.xml`)

- **Approaches** match the 2010 CAP 3 plates (`procedures-2010.md`, plate screenshots in `charts/procedures-2010/`): ILS 34 Y (IF ULIXU, MIRAN, ZXD FAF), LOC 34 X, NDB 34 Z, NDB 16 Y, LOC(BC) 16 Z, with the plate missed approaches. RNAV 12 Y (LPV) and RNAV 30 Y (LNAV) have no plates: fixes are invented unnamed waypoints on the extended centrelines and altitudes are placeholders. NDB approaches carry `gpsOverlay`. `LEFAT` is a 2004-era fix, so not period-correct for 1940-85.
- **Procedure turns** use a `<Transition transitionType="FULL">` holding a `PI` leg (the 45 deg barb heading, 10 NM limit) then a `CF`.
- **Departure:** `EDMONTON City FOUR DEP` (`CITY4`) for runways 12, 16, 30, 34: `VA` to 3200 then `VM`, enroute transitions to AROUK, ABENY, NUPPS, REFIO, BACOS. Climb gradients and ATC vectors cannot be encoded. Compile gotcha: a `Name=` attribute on the departure gives `CompileMemory failed`; use the SDK sample's lowercase `name`.
- **Navaids:** ZXD (201 kHz) and XD (266 kHz) match OurAirports. The IXD DME (109.5, 032X) and the glideslope sit at 53.5689, -113.5110; the localizer is at the north end. Our XD is 4.5 nm due north of the DME, as on the plate. Rwy 34 ILS has `backCourse` FALSE. Approach `heading` is magnetic (user decision; the SDK docs are silent).
- **ATIS** 125.4; 114.9 is the VOT in the CFS but is still configured as a second ATIS.
- **Displaced thresholds** (2007 aerodrome chart, 1978 On Track table): 12 = 800 ft, 30 = 1187 ft, 16 = 500 ft, 34 = 540 ft, 04 = 194.1 m, 22 = 40.2 m. PAPI/VASI positions were not adjusted (`biasZ` may need tuning). The 1978 chart's VASIS/AVASIS symbols are all modelled as PAPI4.
- **Traffic patterns:** right traffic on 30 and 34 (AOPA directory), left assumed on 12/16. Lighting: 12/30 MIRL and 16/34 HIRL as listed; 04/22 edge LOW is unsourced.
- **Runway 04/22** (the 1978 "03/21", closed some time between 1979 and 1994; `runway-04-22-closure.md`): heading 57.78 true, measured on the 1944 aerial (the old 63.0 was wrong); `RunwayStart` 57.78 / 237.78; threshold markings on, others off, no approach lights. Taxi nodes and signs were re-projected for the new heading. Taxiways A/B/C/W beyond the hold-shorts are still skewed from the old axis, and parking connector nodes 83-86 (now replaced, see Parking) ran ~60 m from the centreline.
- **Historical runway names** (c.1942, var 25 E): 04/22 = 3/21, 12/30 = 11/29, 16/34 = 15/33. MSFS derives numbers from heading and magvar, so these are for signage notes only.
- **Taxiways and ground cover:** the grass polygons have runway and taxiway corridors cut out (shapely); hold-short nodes and signs were repositioned; turns at hold-shorts are below ~25 deg. `Grass over construction 6` used to hide the 22 end of rwy 04.
- **Closures:** 16/34 on 2010-08-03 (NOTAM), 12/30 at 23:59 on 2013-11-30. Neither is 04/22.
- **Alpha 7 / Bravo 3 airways and the Municipal One departure** (1984 CASB report; Alpha 7 = Edmonton to Peace River, Bravo 3 = Whitecourt to Peace River, map on PDF p.65): noted in `departures/charts-navaids-archives.md`. Airways and SIDs from that era are not authorable here and nothing in `CYXD.xml` changed; an era-correct SID would need an early-1980s plate.

## Reference sources used for the airfield layout

- 1944 National Archives aerial `aerials/national-archives-1944-RG-18-AA-208-27-ac.jpg`: **not a clean north-up vertical** (grid streets tilt ~5.7 deg, Kingsway ~10.5 deg; a runway-X fit and a street-junction fit disagree by ~90 m). Anchor positions locally (street grid, OSM outlines), not with one similarity transform.
- RCAF Manual of Aerodromes p.90 (c.1942): wind tee and beacon positions (placed by scaling the sketch, +-20 m). 1978 On Track pages (circuits, landing distances, the aerodrome plan and an oblique aerial, not yet used to place buildings). Both are in `departures/`.
- 2016 OSM outlines (Overpass `date:` query) fit the Esri Wayback 2014 imagery to a few metres; method and per-hangar table are in `hangar-footprints.md`. Imagery is measuring reference only.
- The 2014 Google Earth aerial and the oblique Flickr/Commons shots (`hangar17-tower-photos/`, `aerials/`) for heights, doors and signs.
- Photo folders are one per building (`hangarNN-photos/`, plus `aerials/`, `administration-building-photos/`, `hudson-general-photos/`, `transmitter-site-photos/`, `ndb-photos/`, `departures/`); each has a `SOURCES.md` or `SOURCES-streetview.md`.

## Buildings and scenery: the generator pipeline

`CYXD.xml` holds generated blocks between BEGIN/END markers. **Do not hand-edit them; edit the generator and re-run.**

| Script (`airport-cyxd/tools/`) | Writes |
|---|---|
| `gen_buildings.py` (+ `hangars.py`, `display_aircraft.py`) | glTF models in `PackageSources/modelLib/`, their `LibraryObject` placements, building exclusion polygons, tree-exclusion polygons (`VEG_EXCL`), `ExclusionRectangle`s (`OBJECT_RECTS`). Reads `docs/cyxd/historic-buildings-genericbuilding.xml` for the older generic placements. |
| `gen_aprons.py` (`--write`) | front-door `Apron` polygons from each hangar's door wall to existing pavement; `DOORS`, `GROW`, `HOLD`, `KEEP_CLEAR` tables. |
| `gen_parking.py` (`--write`, `--map`) | parking spots, PARKING connector paths, jetways, one apron, fuel and service stands. |
| `make_maps.py` | the maps in `docs/cyxd/maps/`, redrawn from `CYXD.xml`. |
| `make_signs.py` | sign textures (`esso`, `navcan`, `lawoffice`, `nwi`, `goa`, `museum`, `efc`). |

Run with `python -I` from the repo root. Build with `build.bat cyxd` (see `CLAUDE.md`).

Lessons that apply to every model:
- `GenericBuilding` is rejected by the 2024 compiler (C2151); buildings are flat-colour or textured glTF models in the `cyxd-modellib` group, placed as `LibraryObject`s.
- The sim places glTF model +X to the WEST of the object heading, so models are mirrored once at the end (`Mesh.mirror_x`). Verified for the NDB sites; the transmitter site and wind tee were not mirrored; check them.
- `Mesh.poly` uses Newell's method for normals (a zero-area start caused vanishing barrel-vault end walls). Avoid coplanar faces (z-fighting): overshoot or inset by 5 cm or more.
- `Mesh.window` builds glass on a closed backing box sunk into the wall; `m.keepout(...)` skips windows that touch a region.
- Every building gets an exclusion polygon (footprint + 6 m) so sim-generated buildings do not double up. A base-scenery object may need an `ExclusionRectangle` (`excludeAllObjects`) instead, as at XD and the tower.
- Palette is 36 swatches; changing it rewrites every model's UVs.
- Generic placements (`SKIP` in `gen_buildings.py`) are dropped where a new model stands on them: Hangars 11 and 14, USAAF T1/T2/T4, BCATP rows A, B, C, the generic Administration Building, the old north-complex boxes.

## What is built (all models in `hangars.py` / `gen_buildings.py` unless noted)

- **East line:** Hangars 3 (+ tan annex), 4 (arched airside frontage, two doors), 5 (curtain-wall office), 6, 7, 8 (north door wall, tall block with LAW OFFICE signs), 11 (barrel vault, three-storey annex, NORTHWEST INDUSTRIES board, 1956 form), the dark-blue gabled hangar north of Hangar 3 (unnumbered), plus Hangar 20 (Esso) and Hangar 19.
- **Tower group:** control tower "17" (post-c.1972; annex, ladder shaft, NAV CANADA plaque), Aerocentre / Shell hangar group (Hangar 16, five bays, Shell pecten texture), Hangar 15 (47 x 54 m + east wing), Hangar 14 (museum, South-gable door bays, 18-window walls; frontage displays: Bomarc, Norseman, memorial, Voodoo, sign), Hangar 18 / Edmonton Flying Club (three blocks).
- **West group:** Hangars 38, 39 (pale-blue double hall), 40 (three masses).
- **Terminal and garage:** old terminal Hangar 21 (162 x 70 m, four boarding bays on the NE face; landside, lounge and walkway reworked 2026-10-22 from the lean-corrected 2017 aerial and MS-1270.213.1 / .3). The landside is two storeys of brick in two planes that meet at a jog at x 28. The NW section stands at z -16 with a sloped metal band on top; the SE block is at z -12.9. There is no low cream wing. A flat concrete awning with a pale ribbed fascia (top 4.9 m) runs along the landside: 4.3 m deep on the NW section, and 10 m deep on brick piers along the SE block, ending flush with the SE end wall. Tall red masts with braces stand on the fascia at 3.6 m spacing, along the NW section and on the last 25 m of the SE block. Under the awning's SE end are a brick block with the school sign and a white shed. Other details: the two "21" roundels (landside face by the corner, SE end wall by a teal banner) and the rooftop penthouse. The glazed viewing lounge is an L that wraps the SE corner (user, 2026-10-22; this replaces the 2026-10-21 "apron face only" answer). It is cantilevered 3 m off both the SE end wall (z 5.5..16) and the apron face (x 65.5..78.5), with a glass roof sloping up to the walls and hipped at the corner. The apron leg's length is a guess; MS-1270.213.1 shows only the end leg, and ET-28-900 (1982) is too coarse to measure. It is gone by 2017. The apron canopy now stops at x 64. The walkway is 7.5 m wide, moved 2 m SE (x -39.2..-31.7), and ends in a brick head-house at the foot of the NW section. Renders: `compare/terminal-render-*.png`. The parkade is garage 22 ("Mk 12", 2026-10-22). The plan is measured from the Esri Wayback 2017-05-03 zoom-20 tiles, rotated into the garage frame and corrected for image lean. It is 74 m wide and 100 m deep along the arms, 114 m with the stepped front, with a notch at the NE back corner. It has ground parking and three decks (4.0 / 7.2 / 10.4 m). Each deck is a flat U round a 37 m bay whose floor slopes down to the back, one storey over 44 m; the slopes are stacked. The front has four segments, each set back 5.65 m from the one to its west, and each deck sits 4.15 m behind the one below. Stair towers: three on the SW face (the user confirmed the middle one), one at the back notch, the lift housing, and the "22" tower at the front east. There are two "22" roundels: one on the front face of the east tower, and one airside on the NW face of the notch stair; the airside spot is a guess, since no photo shows it. User answers (2026-10-22): the front roundel is on the right face, keep the NE back notch, and the ground storey only looks taller because it has no boards. Checked against MS-1270.213.3 with a fitted camera (camera about 150 m in front and 50 m SW, 33 m up, f = 1217 px on the 2000 px view). Deck heights are still the old estimate. Offline renders: `compare/parkade-render-*.png`.
- **Historic (1938 and later):** the 1938 barrel-vault hangar with two brick towers (`cyxd_hangar_1938_landmark`) and the second ("orange") hangar (`cyxd_hangar_second`, shifted 18 m NE to keep the Chateau Nova Hotel clear; how to restore it is in the comment above `ORANGE_LAT`). The first 1930s hangar (stucco arch, tower, wing) is not built.
- **North hangar complex:** five models at the OSM position (main block as two bays with the 1944 gap, shop, annex, bay 3, outbuilding).
- **Other:** NDB sites XD and ZXD (fenced, sheds, masts), ILS glideslope hut, beacon and animated wind tee (RCAF sketch), radio transmitter site at the ETS Mitchell Garage (`transmitter-site-photos/`), 15 older generic buildings from the 1944 photo (some now skipped), hotels not modelled.
- **Aprons:** generated front-door aprons for Hangars 4-8, 11, 15, 18, 19, 20, 38, 39, 40, the Aerocentre, Shell, the north main block, bay 3, the outbuilding and the old terminal. Held back (`HOLD`): Hangar 3, the dark-blue hangar, the second hangar, the north shop and annex (office / back-to-back), Hangar 14 (museum, by design).
- **Parking:** 45 spots from `gen_parking.py`. GATE 1 = wide-body on the terminal's NW end (Megalink jetway), GATE 2-4 = narrow-body on the NE face (Link jetways); ramp stands down the SW hangar line, at Hangars 38 / 39 / 40 (`helicopterStand` on two), in the north court; GA scrabble by the tower; FUEL stands at Hangars 20 (Esso) and 16 (Shell) with a trial `FUEL_TRUCK` service stand each (delete the block if no truck shows). Airline codes skipped (user).

## Known assumptions to check in the sim

- Door and gable directions: Hangar 3's airside wall (generic), the dark-blue hangar's door (assumed south), which end of Hangar 3 carries the entrance bump, Hangar 40's front, the 1938 hangar's tall-tower end (it is mirrored).
- Hangar 8's tall-block end; Hangar 38 = SW and 39 = NW groups were settled by the user (39 is the pale-blue double hall).
- Hangar 14's ladder / north-end windows; Hangar 15's SE gable; second hangar and 1938 hangar are positioned to +-50 m.
- Exclusion polygons around the old terminal's stray sim-generated building (polygon plus `ExclusionRectangle`); XD's sim-generated mast.
- The 14 m shift of the second hangar and its exclusion's effect on OSM building 131 Airport Rd.

## roscohead's CYXD (a friend's design; ask before copying wholesale, attribute in release notes)

`alt-roscohead/` and `compare/compare.py` (`layout-compare.png`, `taxi-parking-compare.png`). His file has no approaches or navaids. Candidates to adopt, in order of value: (1) taxi network (251 paths vs ours; keep our names and signs, import geometry selectively), (2) parking clusters at north/southwest/south (superseded in part by our parking rebuild), (3) ground-cover control (flatten + water exclusion in `roscohead-cyxd.cvx.xml`), (4) his 6 `LibraryObject`s and 3 `CarParking` objects, (5) apron detail (18 vs our 5, though gen_aprons now adds more). Keep ours: signs, painted elements, windsock, frequencies, ILS/NDBs, jetways, magvar 343.78 (his `magvar="14"` looks wrong). Confirm with the user which pieces they want before importing.

## Instructions for Claude when resuming

1. Read this file and `open-questions.md`, then `git log --oneline -8` and `git status`.
2. Before touching anything generated, edit the generator, re-run it, then rebuild (`build.bat cyxd`, sim closed; read `_build/last-build.txt`; build notes are in `CLAUDE.md`). Restart the sim to see changes.
3. Ask the user for in-sim results before reworking anything listed under "Known assumptions".
4. Commit with a leading robot emoji and the Co-Authored-By trailer. Bump the package version and add a ReleaseNotes entry (0.2.2) once the user confirms the changes work.
