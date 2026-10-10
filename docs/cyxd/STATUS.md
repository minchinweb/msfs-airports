# CYXD status and handoff notes

Last updated: 2026-10-08. Branch: `agents/claude/1` (worktree). Package: `airport-cyxd/` (source `PackageSources/Scenery/airport-cyxd/CYXD.xml`, package version in `PackageDefinitions/...` is still 0.2.1; no release note yet for these changes).

## What was done (commits 60563f8, cc83512, 5e8a5f5)

1. **Approaches rewritten** (none compiled or tested in sim):
   - ILS 34 (IXD, 109.5): `backCourse` now FALSE; localizer + DME moved to the north end (lat 53.58266), glideslope to ~300 m past the displaced 34 threshold (lat 53.56852). Previously all three sat at runway centre.
   - Legs completed with attributes the SDK docs mark required (TF `turnDirection`, CF recommended fix/theta/rho/true+magnetic course/distance, CA altitude, HM distance/time).
   - NDB 16 simplified to IF XD -> CF RW16 (163.8 mag). Procedure turn dropped (no plate to base it on).
   - New LOC(BC) 16 approach (`LOCALIZER_BACKCOURSE`, suffix Z), based on a 2004 TSB report mentioning "LOC (BC) DME RWY 16". Added last so it is easy to delete if it breaks compile.
   - Approach `heading` is now magnetic (343.8 / 163.8), per user. Leg true courses are true.
2. **Displaced thresholds** added (`OffsetThreshold`) from the 2007 aerodrome chart: 12 = 800 ft, 30 = 1187 ft, 16 = 500 ft, 34 = 540 ft. Rwy 04 untouched.
3. **ATIS** 125.4 added.
4. **Comparison** of roscohead's CYXD (`docs/cyxd/alt-roscohead/`) vs ours: `docs/cyxd/compare/compare.py` -> `layout-compare.png`, `taxi-parking-compare.png`.

## Why approaches were not showing (best diagnosis)

- `Packages/.../CYXD.bgl` was last compiled 2025-11-22, with the old approaches to "runway 04" and 180 deg headings. The source was edited later but never rebuilt. A rebuild is the first thing to try.
- Also fixed: back-course ILS flag, localizer/glideslope placement, missing required leg attributes, bad NDB 16 final leg (fix type LOCALIZER, course 0).

## What the user needs to test next

1. **Rebuild in the MSFS 2024 SDK** (DevMode > Project Editor > build `airport-CYXD-edmonton-blatchford-field.xml`). `fspackagetool` would not run headless from the agent shell (exits immediately, "Attached to EXE"), so no compile has been verified.
   - If it fails with `BGLCompiler | CompileMemory failed` (no detail in `_PackageInt/_RPTErrors.xml`), bisect: delete the LOC(BC) 16 `Approach` first, then the NDB 16, then `fixType="RUNWAY"` on the final CF legs (docs list only NDB, TERMINAL_NDB, TERMINAL_WAYPOINT, VOR, WAYPOINT for leg fix types, but ADE exports RUNWAY).
   - Send the compiler message back; it narrows things quickly.
2. In sim: check that CYXD shows ILS 34, NDB 16, LOC(BC) 16 in the world map / flight planner approach list, and that the ILS captures (localizer on 343 mag, GS 3 deg).
3. Check the displaced thresholds look right (runway markings, PAPI/VASI positions on 12/16 were not adjusted, `biasZ` may need tuning) and that approach lights on 34 still sit sensibly.
4. Confirm ATIS tunes at 125.4.
5. Unresolved doubts: whether `Approach heading` should be magnetic (user says yes; docs are silent); whether HH16N should stay a terminal waypoint.

## Open questions: Runway 04 alignment

Our runway 04 is heading 63.0 deg true, centre (53.57487, -113.51968), 1372 m. roscohead's is heading 57.78 deg, centre (53.57521, -113.51896), 1372 m. The overlay in `layout-compare.png` shows ours rotated about 5 deg relative to his, while 12 and 16 line up closely. Questions for the user:
- What is the source of the 63 deg figure (a chart, imagery, a measurement)? "04" implies roughly 40 deg magnetic; with ~17 deg E variation that is ~57 deg true, which matches roscohead (57.8), not 63. Was 63 meant to be a magnetic-vs-true mix-up, or a deliberate historical alignment?
- Our `RunwayStart` headings are 61.2 / 241.2, which disagree with the runway's own heading of 63.0. Which one is right?
- Is the 04/22 pavement visible in any historical imagery to settle position, and does the user want it to match the real 1990s footprint or roscohead's?
- Our 04 has most markings off (`threshold`, `edges`, `touchdown`, `precision` FALSE) and no approach lights; his has threshold/edge markings. Intentional (closed/abandoned runway)?

## How we might integrate the other CYXD design (roscohead)

His file has no approaches, ILS or NDBs, so nothing there for navigation. Candidates to adopt, roughly in order of value:
1. **Taxi network.** 251 paths vs our 133, with taxiways running alongside the runways and curved connectors. Import selectively; do not overwrite ours (we have 12 taxiway names, 56 signs, and signs are keyed to our path naming). Plan: take his path geometry for the main loop, then re-run naming and re-place signs.
2. **Parking.** His has 22 spots incl. clusters at north, southwest and south that ours lacks (ours has 29, mostly an east strip). Compare against the chart's apron layout before adding. Watch the type/radius per spot.
3. **Ground-cover control** (`roscohead-cyxd.cvx.xml`): exclusion/flatten/water vectors. Ours uses `Polygon` exclusions in the main XML; his adds flatten + water-exclusion polygons that may fix terrain issues near the runways.
4. **Scenery objects.** His 6 `LibraryObject`s and 3 `CarParking` objects. Cheap to add once positions are verified against the chart.
5. **Apron detail.** 18 aprons vs our 5, with surface variety (two surface GUIDs).
6. Keep ours: signs, painted elements, windsock, frequencies, ILS/NDBs, jetway set, magvar 343.78 (his `magvar="14"` looks wrong).

Credit: his work is a friend's; ask before copying wholesale, and attribute in release notes.

## Instructions for Claude when resuming

1. Read this file, then `git log --oneline -8` and `git status`. Confirm the CYXD.xml approach/threshold changes are still in place (`grep -n "Approach type\|OffsetThreshold\|ATIS" airport-cyxd/PackageSources/Scenery/airport-cyxd/CYXD.xml`).
2. Ask the user for the result of the SDK rebuild and in-sim test (section above) before changing approach data again. Do not re-derive the diagnosis; act on the compiler/sim result.
3. If the user answers the Runway 04 questions, adjust `<Runway number="04">` heading/centre and its `RunwayStart` elements together, then regenerate the plots with `python docs/cyxd/compare/compare.py` (needs matplotlib) and check the overlay.
4. Do not try `fspackagetool` from the agent shell again; it does not work headless here.
5. Commit with a leading robot emoji and the Co-Authored-By trailer from the session reminder. Leave the untracked `.claude/` folder alone. Bump the package version and add a ReleaseNotes entry (0.2.2) when the user confirms the changes work.
6. Before importing anything from roscohead's files, confirm with the user which pieces they want.

## Historic buildings (updated 2026-10-08, uncompiled)

Era: deliberately a-historical, 1940-1985. 15 `GenericBuilding` objects at the end of `CYXD.xml` (legacy generic buildings, all texture indices 0, appearance untested). Positions from `docs/cyxd/National Archives/RG-18-AA-208-27-ac.jpg` (1944, north-up, rotated ~6 deg; anchored on Hangar 14's published position, 2.2 m/px; ~30 m error). Generator script was a scratchpad throwaway; coordinates are in the XML comments.
- Hangar 14 (68 x 98 m, N-S), Hangar 11 (taken as USAAF T3, 70 x 60 m), T1, T2, T4 on the east apron, three BCATP hangars (A, B, C) in a row along Kingsway (long axis NW-SE).
- West side: 1938 arched hangar + tower (replica at Fort Edmonton Park, per user; see City Archives 1937-39 photos), 1937 office wing, Administration Building near the circular drive (1950 photo EA-10-838: 3-storey centre block with control tower).
- Hotels, south side of Kingsway (across from the field), placed by street address, +-100 m: Chateau Louis (11727 Kingsway, tower + low wing, 1980s photos) 53.56713, -113.52435; Edmonton Inn (11834 Kingsway, brick tower) 53.56875, -113.52816. Chateau Nova (2005) skipped as out of era.
- Photos not used: `1975 ca/EA-784-*` show a jet terminal that looks like Edmonton International, not City Centre. 1980s photos (ET-28-*) show flat-roofed blue-grey hangars, a tall white control tower, red brick building; not yet modelled.
- Delete the block if compile fails (CompileMemory failure is unresolved).
- 1944 field also shows: three runways incl. 04/22 (SW-NE), a large hangar complex with a long apron at the north end (not yet modelled).
- North hangar complex (added): two adjacent 84 x 88 m bays plus a separate east bay, a shop/office with parking lot, an annex and a small outbuilding, from the 1944 photo (display px ~850-1005, 535-630). Positions in XML comments. 21 generic buildings total.
- OpenStreetMap (Overpass, 2026-10-08) used for buildings that still exist: Hangar 14 (way 230718920, 91 x 100 m incl. lean-tos, axis-aligned, centre 53.56571, -113.51713; matched my photo placement within ~20 m, which validates the 1944 georeference), Edmonton Inn (230718927, 14 levels, centre 53.56872, -113.52376, L-shaped), Chateau Louis (325236282) and its Conference Centre (325235666). Hotels were moved ~150-290 m from my earlier address-based guess. Hangar 11 is gone from OSM (burned 2024). Chateau Nova Hotel (230718905) is 2005, skipped. Hotel wing/tower splits are simplified guesses from the OSM outlines.

## Runway 04 realigned (2026-10-08)

Measured the 04/22 centreline in the 1944 National Archives photo (ridge fit, calibrated against 16/34 and 12/30; photo rotation ~7 deg): ~56-57 deg true, +-2. Runway 04 heading changed 63.0 -> 57.78 (roscohead's value) and both `RunwayStart` headings set to 57.78 / 237.78 (were 61.2 / 241.2); starts moved to their original distances (539 m SW, 393 m NE) from the unchanged centre along the new axis. The measured line sits ~65-70 m SE of our centre (and roscohead's), within georeference error, so the centre was not moved. `layout-compare.png` is not regenerated. 1975 photos (`1975 ca/`) are ignored and not committed: they show Edmonton International, not City Centre. The old 04 taxi nodes lay exactly on the 63 deg axis, so they were re-projected: runway nodes 37, 47, 40, 42, 51 and hold-shorts 21, 9, 54 keep their along/across position relative to the runway centre in the new frame (moved 26-63 m); node 38 (04 x 12/30) and node 41 (04 x 16/34) were moved to the true new crossings of those centrelines (20 m and 53 m, both stay on their own runway axes); 17 taxiway signs with 04/22 in the label were moved/rotated by the same rotation (-5.22 deg). Parking taxi nodes 83-86 and their parking spots were NOT moved and now sit ~60 m from the 04 centreline (were ~100 m): check in-sim. Other far-end taxiways (A, B, C beyond the hold-shorts) were not reshaped, so their first legs are slightly skewed.

## RNAV approaches, second ATIS, historical runway names (2026-10-09, uncompiled)

Source: https://www.airports-worldwide.com/canada/alberta/edmonton_city_centre_alberta.php (data as of ~2013 closure).
- Added `RNAV 12 Y` (LPV on the real plate) and `RNAV 30 Y` (LNAV). No plates: fixes are invented unnamed waypoints on the extended centrelines (CY12I/CY12F, CY30I/CY30F; FAF 4.5 nm, IF 8.5 nm from the thresholds), altitudes are placeholders (IF 5200, FAF 3700, runway end 2400 A), missed approach direct to ZXD hold. Final leg is `TF` to the runway (no recommended navaid). MSFS has no LPV/LNAV distinction here.
- Added second ATIS 114.9 MHz.
- Added NDB 34 Z earlier (ZXD, circling-only in reality).
- Historical (~1942, RCAF/DoT, variation 25 deg E) runway designations: 04/22 = 3/21 (4,500 ft), 12/30 = 11/29 (5,700 ft per the page), 16/34 = 15/33 (5,700 ft). MSFS numbers runways from heading and magvar, so these cannot be set in the file; they are for signage/chart notes only.
- Closures per the page: 16/34 closed 2010-08-03 (page also says October 2010); 12/30 closed 2013-11-30.
- The page says "no ILS" (late-life state), but PilotNav lists ILS or NDB 34 and the DME IXD is 032X (= 109.5 MHz), so ILS 34 stays.

### Navaid positions checked against OurAirports (2026-10-09)
- ZXD (201 kHz) and XD (266 kHz) positions/frequencies match OurAirports exactly.
- IXD DME (109.5 MHz) is listed at 53.568901, -113.511002, 671 m, i.e. near the 34 glideslope, not the localizer. DME and glideslope both moved there (glideslope alt unchanged at 664.77 m); localizer stays at the north end. Uncompiled.

### Traffic patterns and lighting (2026-10-09)
- AOPA directory: right traffic on runways 30 and 34. Set 12/30 and 16/34 to primary (12, 16) LEFT / secondary (30, 34) RIGHT (were the reverse). 04/22 unchanged (not in the directory). Left traffic on 12/16 is assumed.
- Lighting checked: 12/30 edge MEDIUM and 16/34 edge HIGH match MIRL/HIRL. 16/34 also has center MEDIUM, which the directory does not list; left as is. 04/22 edge LOW is unsourced.
- FBO names saved in `fbos.md`.

### In-sim result (2026-10-09)
All approaches show in the sim after a full sim restart: ILS 34 Y, NDB 34 Z, NDB 16, LOC(BC) 16 Z, RNAV 12 Y, RNAV 30 Y. A package rebuild alone does not reload scenery in a running sim; restart the sim after rebuilding. RNAV approaches carry `lnav`/`lpv` flags and `isIAF/isIF/isFAF/isMAP` leg flags (2024 schema).

## Historic buildings as custom models (2026-10-09, uncompiled)

`GenericBuilding` is rejected by the 2024 compiler (C2151), so buildings are now flat-colour glTF models in a new `cyxd-modellib` asset group (`PackageSources/modelLib/`), placed as `LibraryObject`s in `CYXD.xml` between the BEGIN/END markers.
- Regenerate with `python -I airport-cyxd/tools/gen_buildings.py` (reads `docs/cyxd/historic-buildings-genericbuilding.xml`, the source of truth for positions/sizes/headings). Do not hand-edit the generated block.
- 16 placements, 13 models. Hotels (Edmonton Inn, Chateau Louis) skipped until tower/wing splits are known.
- Landmark `cyxd_hangar_1938_landmark` merges the old 1938 hangar, tower and 1937 office wing: 42 x 44 m barrel-vault hangar (7 m walls + 6 m arch), 11 x 11 x 22 m main tower flush with the front face on its right, a 30 x 13 m two-storey gabled office wing continuing right, and a 6 x 6 x 14 m small tower at the hangar's left front corner. Based on City Archives EA-160-398/402/466/1331/1332 and EA-10-3181-44-2, and the 1944 aerial. Front (doors) faces the object heading (59 deg, ENE). Dimensions and the left/right arrangement are estimates: check in-sim whether the tower/wing are on the correct side (mirror = flip X in `hangar_1938`).
- Ridge direction of generic roofs is along the longer footprint side. Assumed model +Z = object heading; verify in-sim.

## Grass vs taxiways, 04/22 connectivity check (2026-10-09, uncompiled)
- "Grass over construction 6" sat on the last ~90 m of runway 04 (22 end) and on taxiway B's first legs (51->9, 8->51); that is why they looked hidden. Cut runway and taxiway corridors (runway width +3 m, taxi width/2 +2 m) out of all eight grass polygons with shapely; no overlaps remain. G6 shrank from 7,520 to 960 m2 (most of it was over the runway). Layer is unchanged at -50.
- Hold-short nodes 8 (B, east of the 22 end), 20 (A) and 34 (W, 04 end) were not rotated with the runway realignment and had drifted to 77-110 m from the centreline; restored to their pre-realign runway-frame offsets (about 45-50 m). Nearby signs are now 25-30 m from them again (were 46-69 m).
- Checked: runway 04 path nodes 37, 47, 38, 40, 41, 42, 51 all lie on the centreline (|across| < 3 m); hold-shorts 34, 20, 21, 54, 8, 9 sit 41-62 m off it, each connected to a runway node.
- Not changed: parking connector nodes 83-86 run parallel to 04 only ~55-68 m off the centreline (taxi edge ~10 m from the runway edge); moving them would drag the parking spots. Far-end taxiways A/B/C/W beyond the hold-shorts are still skewed from the old 63 deg axis.

## Round 2 fixes after in-sim review (2026-10-10, uncompiled)
- Hold-short angles at the 22 end: taxiway B node 10 moved onto the straight line 9->11 (turn at 9 was -52 deg, now -6); taxiway C nodes 54 and 113 moved onto the straight line 40->14 (hold line 60 m from the centreline; turn at 54 was 45 deg, now 0) and the two C signs next to 54 moved with it. Turns at hold-shorts are now all below ~25 deg.
- Two signs ('m<16l 22', 'm<22 l 34 d[B>]') had been rotated onto runway 16/34 by the earlier realignment; put back beside the runways at (520, 634) and (517, 466) m (local frame), 12-15 m clear of all runway/taxiway surfaces. No other sign is on a runway or taxiway.
- Buildings (generated by `tools/gen_buildings.py`):
  - headings snapped parallel to the nearest runway/taxiway: east apron hangars 0, BCATP rows 138 (rwy 12/30), 1938 landmark 57.78 (rwy 04), admin 
-3.6, north complex -1.0 (taxiway III).
  - north complex shifted off taxiway III: bays 1 and 2 20 m south, shop 25 m south, annex 10 m north (now beyond the taxiway); BCATP row A 3.7 m W / 1.5 m S off taxiway X. All 15 buildings are now clear of every runway and taxiway and of each other.
  - USAAF hangar T4 removed: the sim's own generated building east of the 30/34 junction is used instead.
  - an exclusion polygon ("No generated buildings: ...", footprint + 6 m) is generated for each building so the sim's autogen buildings do not double up. Existing polygon "no apron buildings" kept.
