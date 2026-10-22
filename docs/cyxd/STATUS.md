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
- Is the 04/22 pavement visible in any historical imagery to settle position, and does the user want it to match the real 1990s footprint or roscohead's? (Partly answered: position was settled from the 1944 photo, see "Runway 04 realigned". The strip is already absent from the 6 June 2012 aerial, `aerials/Edmonton_City_Centre_Airport.jpg`; when it stopped operating is in `runway-04-22-closure.md`.)
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
4. Build with `build.bat cyxd` from the repo root (from bash: `cmd.exe //c build.bat cyxd`); see `CLAUDE.md`. Read `_build/last-build.txt` for the result instead of asking the user to copy console output. Calling `fspackagetool` directly from the agent shell exited at once ("Attached to EXE"); if `build.bat` reports no build (exit code 2), retry with `-window`, and failing that ask the user to build in DevMode.
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
- Added `RNAV 12 Y` (LPV on the real plate) and `RNAV 30 Y` (LNAV). No plates: fixes are invented unnamed waypoints on the extended centrelines (XD12I/XD12F, XD30I/XD30F; FAF 4.5 nm, IF 8.5 nm from the thresholds), altitudes are placeholders (IF 5200, FAF 3700, runway end 2400 A), missed approach direct to ZXD hold. Final leg is `TF` to the runway (no recommended navaid). MSFS has no LPV/LNAV distinction here.
- Added second ATIS 114.9 MHz.
- Added NDB 34 Z earlier (ZXD, circling-only in reality).
- Historical (~1942, RCAF/DoT, variation 25 deg E) runway designations: 04/22 = 3/21 (4,500 ft), 12/30 = 11/29 (5,700 ft per the page), 16/34 = 15/33 (5,700 ft). MSFS numbers runways from heading and magvar, so these cannot be set in the file; they are for signage/chart notes only.
- Closures per the page: 16/34 closed 2010-08-03 (page also says October 2010); 12/30 closed 2013-11-30. City of Edmonton releases confirm both: 16/34 by NOTAM on 3 August 2010 (the first phase of the 2009 council decision, so "October 2010" is a later wording of the same event), 12/30 at 23:59 on 30 November 2013. Neither is 04/22; see `runway-04-22-closure.md`.
- Number of the 04/22 pavement over time (from `runway-04-22-closure.md`): 3/21 c.1942 (var 25 E), 03/21 in 1978 (var 23 E). The 20 Nov 2008 CFS prints var 17 E, which gives about 41 deg magnetic for our 57.78 deg true, i.e. 04. No CFS or directory found that publishes "04/22"; the 2008 CFS and AOPA 2007/08 list only 12/30 and 16/34.
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

## Edmonton radio transmitter site
Added to `tools/gen_buildings.py` (model `cyxd_transmitter_site`): 1950s radio transmitter site from the radiocom.ca "Edmonton Radio" article (photo 4: 118 Ave & 156 St, now the Northwest Transit Garage). Placed at 53.57055, -113.58378 (OSM node for 15204 118 Ave NW), ~4 km west of CYXD, heading 0. White/red-roof building + shed + 10 red/white striped masts (35-55 m). Layout and mast count are approximated from one photo; exclusion polygon 165 x 75 m covers the site. Unverified in sim.

Reference photo: `docs/cyxd/edmonton-transmitter-site-radiocom.jpg` (Watts_Edmonton_04.jpg from https://radiocom.ca/z_station_Edmonton.htm, article covers Edmonton Radio 1955-58; photo is uncaptioned apart from the overlay text "Edmonton transmitter site, 118 Ave and 156 st.").

## Wind tee and beacon (RCAF sketch)
Source: RCAF & D of T Aerodrome, Edmonton, Alberta, p.90 of the RCAF Manual of Aerodromes and Seaplane Bases Vol. 2 (c.1942) - https://rcaf.info/wp-content/uploads/2022/05/Edmonton-Alberta-RCAF-Manual-of-aerodromes-and-seaplane-bases-Vol-2-RCAF-DofT-Aerodrome_Page_1.jpg - saved as `docs/cyxd/rcaf-manual-of-aerodromes-edmonton-p90.jpg`. Also gives 53 34 N 113 31 W, var 25 E, elev 2185 ft, runways 3-21 4500x200, 11-29 and 15-33 5700x200 (all hard surfaced), radio range 266 kc/s "XD", aerodrome 3.35 mi from R.R. at 61 deg magnetic.
- The sketch shows a wind tee and a beacon west of the runway 3 (04) end, plus two small buildings beside the beacon (not added; also three larger buildings south of 11 end ~ the BCATP row).
- Placed by scaling the sketch (runway 3-21 = 1372 m): beacon 53.572005, -113.529643 (~66 m from rwy 04, clear of taxiways/aprons/signs); wind tee 53.573710, -113.528688 (~25 m clear of GA parking 76, ~14 m from an apron, 179 m from rwy 04). Wind tee model `cyxd_wind_tee` (animated: the head node swings about the post via a ModelInfo behaviour, `ASOBO_GT_Anim_Code` with `(A:AMBIENT WIND DIRECTION,degrees) dnor`, ANIM_LENGTH 360, 9 quaternion keys; head points into the wind; object heading must stay 0. UNVERIFIED that the sim runs this behaviour for a scenery LibraryObject - if the tee is static, that is why); beacon is the sim's own `Beacon CIVILIAN/AIRPORT` object. Scaled-from-sketch accuracy only (+/- ~20 m). Both are emitted by `tools/gen_buildings.py`.
- Windsock already in the file is a separate object at the east side (53.56715, -113.51394), no conflict.

## LOC(BC) DME RWY 16 rebuilt from the TSB report (uncompiled)
Source: TSB Aviation Investigation Report A04W0200 (Beech King Air C-FGXH, Edmonton, 10 Sep 2004), https://aviation-safety.net/wikibase/349241 (ASN summary, blocks scripts) - PDF saved as `docs/cyxd/tsb-a04w0200-king-air-edmonton-2004.pdf`, Appendix A figures as `docs/cyxd/tsb-a04w0200-loc-bc-dme-16-figure.png`.
- Plate data from the figures: course 163 mag inbound (343 mag back course), IF **LEFAT** at 10 DME, min 4300 ft to 7.5 DME, min 3700 to 5.5 DME, min 3400 from 5.5 DME, XD NDB (266) at 4.5 DME, step at 0.6 DME. DME is the IXD DME. Also: localizer intercept 8.8 nm from threshold, field wx/MSA 4100 ft.
- Our XD NDB is 4.5 nm due north of the IXD DME, matching the plate. The 343.8 mag course is 360 true here, so LEFAT = 10 nm due north of the DME: 53.735568, -113.511002 (named waypoint `LEFAT`); unnamed `XD16A` (7.5 DME) and `XD16B` (5.5 DME) added as step-down points.
- Approach `LOCALIZER_BACKCOURSE` 16 Z now: IF LEFAT 4300 > XD16A 4300 > XD16B 3700 > XD 3400 (FAF) > RW16 (2400 A, MAP). Altitudes after XD and the missed approach are still placeholders (the 0.6 DME step altitude is not legible). The older NDB 16 Y approach was not changed (no plate for it); LEFAT is a 2004-era fix, so it is not period-correct for 1940-85.

## 1984 Alpha 7 routing (CASB report 84-H40006)
Source: CASB occurrence report 84-H40006 (Wapiti Aviation PA-31-350 C-GXUC, 19 Oct 1984, 20 mi SE of High Prairie; released under ATIP request AI-2023-00023), saved as `docs/cyxd/casb-84-h40006-wapiti-402-alpha7-1984.pdf`. About the accident, not CYXD; only the departure and route context is useful.
- Flights left Edmonton Municipal (CYXD) from runway 34 on the "Municipal One" departure, then Alpha 7 (low-level airway, Edmonton NDB to Peace River NDB; MEA 7000, MOCA 5600 near High Prairie). Appendix A sketch: Edmonton, Athabasca, Swan Hills NDB, High Prairie, Peace River, heading roughly NW.
- No departure plate, fixes or altitudes are given, and airways/SIDs are not authorable in this package, so nothing was changed in `CYXD.xml`. An era-correct SID would need an early-1980s plate (CFS/RAC).
- Report read through Appendix B (pdf p.1-66); Appendices C-E not read.

## 1978 aerodrome sketch (On Track, 1978)
Source: https://rcaf.info/wp-content/uploads/2023/02/On-Track-1978-Edmonton-Muni-2.jpg, saved as `docs/cyxd/rcaf-on-track-1978-edmonton-muni-2.jpg` (aerial photo plus plan; elev 2200, var 23E, right-hand circuits Rwys 21, 29, 34, all runways 200 ft wide, "XD" NDB 3.8 nm on bearing 167).
- Runway lengths: 16/34 5700 ft asphalt, 11/29 5868 ft concrete, 03/21 4451 ft concrete. Runway 03 shown "Closed" at the west end beside taxiway W/Z: that is the stub before the displaced threshold, not a closed runway (both directions still publish landing distances; `runway-04-22-closure.md`).
- "All thresholds displaced" table (landing distance in ft): 03 3814, 11 5068, 16 5190, 21 4319, 29 4681, 34 5160. Displacement = length - landing: 03 637 ft (194.1 m), 21 132 ft (40.2 m), 11 800, 29 1187, 16 510, 34 540. The 11/29/16/34 values match the displaced thresholds already in CYXD.xml. The take-off column (21, 29, 34, 03, 11, 16) is paired row by row with the landing column; its numbers are not given separately.
- Added `OffsetThreshold` to runway 04/22 (04 = 194.1 m, 22 = 40.2 m); it had none. Uncompiled, unverified in sim. Runway 04/22 `Markings threshold` set TRUE so the threshold bars show at the displaced thresholds (other 04/22 markings unchanged). Our pavement is 1372 m (4501 ft) against 4451 ft here; length not changed.
- Taxiways on the sketch: A (west side and south apron), B (east side), C (north apron), plus W, Z, T, Y, X-style stubs; aprons I-V (I south-west, II east, III north, IV west, V north-centre). Not compared in detail with CYXD.xml taxi names.
- The top half of the same image is an oblique aerial photo of the field (c.1978, source credit not shown). Use it as a reference for historical building placement (hangars, terminal and apron buildings, car parks, surrounding streets as they stood in the late 1970s), alongside the 1944 aerial and the City Archives photos. The sketch below it shows only a few building footprints. Not yet used to place or move any building; the photo is oblique, so measure against runway positions rather than scaling directly.
- Symbols: V in a circle at the 16 end = VASIS; VA in a circle at the 11 and 29 ends = abbreviated VASIS (AVASIS), a one-bar type. Reading from period CFS legends, not confirmed against this source. We model all of them as PAPI4 (no VASIS in MSFS); the sketch shows none at 21, 03, 34.
- Closure of the whole 03/21 strip (the pavement this project calls 04/22): researched 2026-10-14, written up in `runway-04-22-closure.md`. Still an operating runway in this 1978 guide. Out of the operating inventory before Edmonton Airports' 1995 plan, which budgeted overlays of the two remaining runways. No exact day found. Not the 2010 or 2013 closures. To close the gap (1979-1994), a dated CFS or air photo is needed; also in `open-questions.md`.

## Sources used for reference material (all in docs/cyxd/)
- `edmonton-transmitter-site-radiocom.jpg`: radiocom.ca Edmonton Radio article, photo 4.
- `rcaf-manual-of-aerodromes-edmonton-p90.jpg`: RCAF Manual of Aerodromes p.90 (URL above).
- `rcaf-on-track-1978-edmonton-muni-1.jpg`: text page of the 1978 On Track entry (landing distances, circuits, noise rules). `rcaf-on-track-1978-edmonton-muni-2.jpg` is the plan (1978 section above). `rcaf-on-track-1978-page1.jpg` is a separate page.
- `runway-04-22-closure.md`: when runway 04/22 stopped operating (research note, 2026-10-14).
- Earlier sources (pilotnav, OurAirports, airports-worldwide, AOPA, VTA chart, articles/) are noted in the sections above.
- `tsb-a04w0200-king-air-edmonton-2004.pdf`, `tsb-a04w0200-loc-bc-dme-16-figure.png`: TSB report A04W0200 (see LOC(BC) DME RWY 16 section).

## Transmitter site moved, NDB sites XD / ZXD (2026-10-10, uncompiled)
- Transmitter site moved to the NE corner of 118 Ave / 156 St: 53.57102, -113.58875, over the ETS Mitchell Garage bus barns (OSM way 325221281; depot way 645478395). Exclusion polygon covers the whole depot outline (in `gen_buildings.py` as `DEPOT`) plus the site footprint.
- XD (53.6436, -113.513) and ZXD (53.4994, -113.513) now have a fenced site each (`cyxd_ndb_xd`, `cyxd_ndb_zxd`, generated by `gen_buildings.py`). Source photos: `docs/cyxd/ndb-photos/` (Google Street View, Apr/Jun 2009).
  - ZXD: chain-link fence from OSM way 429420220 (about 52 x 40 m, gate node 5220567714 at the NE corner), two red/white lattice masts (photo 1 shows two; 25 m is an estimate), peaked red-shingle shed east of the tower.
  - XD: fence around the OSM grass lot (way 671418837, 90 x 90 m, gate gap on the south side where 109 St ends), 55 m mast (estimate), larger grey-shingle building in the SW corner of the lot.
  - Mast heights, shed sizes and the gate positions are read from photos, not measured.
- Maps: `docs/cyxd/maps/` (made by a scratchpad script, not committed to tools).

### NDB sites follow-up (2026-10-10, built and checked in sim)
- The sim places glTF model +X to the WEST of the object heading, so the site models are mirrored once at the end (`Mesh.mirror_x`). Verified for the NDB sites (fence now matches the OSM lot). The 1938 landmark hangar, transmitter site and wind tee were NOT mirrored; check them in the sim.
- ZXD shed east of the towers, door on the east end of the south face. XD shed in the SW corner of the lot.
- XD: the sim's own mast was still there with a polygon exclusion; an `ExclusionRectangle` (excludeAllObjects) was added over the lot. Result not yet confirmed.
- Textures: procedural siding and red/grey shingle tiles in `modelLib/texture/` (made by `gen_buildings.py`), used on the NDB sheds and the transmitter building (`Mesh(textured=True)`). Built and showing in sim. Other buildings are still flat colour.
- Grass polygon over the transmitter site depot hides the aerial photo.

## Control tower, post-c.1972 (2026-10-10, uncompiled)
- Model `cyxd_control_tower` (generated by `gen_buildings.py`, `control_tower()`), placed at 53.56814038, -113.51851571, heading 138 (OSM way 182921011: `aircraft_control` tower, ~11 x 10 m; way 325232689 is the historic tower + annex, 273 m2). Photos and sources: `docs/cyxd/tower-photos/` (see `SOURCES.md`).
- Shape from the photos: chamfered-rectangle shaft, 7 floors of 3.3 m (grey x5, salmon band, white top), 2 windows per face per floor, steel stair cage on one face, balcony and rail, red-orange cab leaning outward with red roof, antennas, flat-roofed grey annex (three blocks from the OSM outline). Blue disc with yellow seven-segment "17" on two faces (+Z and -Z). Heights (about 29 m to the cab roof) are estimates.
- BCATP hangar B (row B) is skipped by the generator because the tower stands on it (it overlapped the tower footprint). Re-enable by removing "bcatp hangar row b" from `SKIP`.
- Exclusions: a building polygon over the tower and annex, plus an `ExclusionRectangle` (all objects) 36 x 33 m around it, as at XD.
- Other buildings at the end of the airport's life carried the same blue numbered discs ("18" on the hangar east of the tower, per the JetPhotos shot); not added yet. `number_disc()` can put them on any model.

- Tower round 2 (from in-sim render): numerals were mirrored (the east/up/north authoring frame is left-handed, reading direction u = n x up); tower shaft/cab/stair turned 90 deg anticlockwise so the "17" roundel faces NE (toward runway 12/30) and the stair cage is on the NW face, annex unchanged (SW); roundel is now a 16 cm thick white-rimmed disc with 5 cm raised numerals.

## Aerocentre and Shell hangar (2026-10-10, uncompiled)
- Added `cyxd_aerocentre` (40 x 16 x 8.4 m, two-storey, navy piers/parapet, cream-grey infill, glazed ground floor) and `cyxd_shell_hangar` (55 x 45 x 9 m, cream ribbed-metal walls with new `cyxd_ribbed.png`, low gable roof, red eave trim, two striped door leaves, open bay, Shell sign over a roller door). Both generated by `gen_buildings.py`; fronts face NE (heading 48), set along the SW edge of apron 1 SE of the tower (tower frame x +11 / +30.5, z +45 / +97.5).
- Sizes, set-backs and the exact positions are estimates from photos (flickr aerial `flickr_33836413.jpg`, Mack Male 2010 `..._4846273897_.jpg`, jasonwoodhead23 Shell-hangar and 2014 aerial shots); no OSM outline exists (the area has been redeveloped as Blatchford). New refs saved in `docs/cyxd/tower-photos/` (`Edmonton_muni_airport__11165253083_.jpg` Shell hangar, `EDMONTON_MUNI__11094252276_.jpg` captioned "Centennial flight center hanger 15": a pale-blue clad building with a "15" roundel, probably not the Aerocentre's back side).
- BCATP hangar C skipped (the Shell hangar and Aerocentre stand on it).

### Shell hangar rework, Hangar 15, jetway 2 removed (2026-10-10, uncompiled)
- Jetway for parking 2 (8 m in front of the Shell hangar) deleted from `CYXD.xml`; the GATE 2 parking spot itself is still there (39 m off the hangar front). Jetway 1 stands 12 m from Hangar 15's exclusion area; left alone.
- Shell hangar front, from the NW (north) end: sign (redrawn Shell pecten: red outline, seven yellow ribs, base), grey roller shutter in a yellow frame and a sectional door in a narrow column; open bay; three striped door leaves; blank wall at the SE (south) end with a "16" roundel. Door/bay widths are guesses from one oblique photo.
- Hangar 15 (`cyxd_hangar15`, 47 x 28 x 7.6 m + roof, pale-blue ribbed cladding on a grey base, "15" roundels on both gable ends, slate door recess airside, offices and two awnings landside): placed between the Shell hangar and Hangar 14 (tower frame x +24, z +156.5, heading 48), from the 2014 aerial (`EDMONTON_MUNI_AIRPORT__15439598181_.jpg`, the pale-blue hangar north of the museum) and the landside shot `EDMONTON_MUNI__11094252276_.jpg` (caption "hanger 15"). Size and position are estimates; no other photos yet.
- Shell hangar moved 5 m NW so its NW end wall touches the Aerocentre's SE end (front still 5 m behind the Aerocentre's); extra airside "15" roundel on Hangar 15.
- Jetway for parking 1 (in front of Hangar 15) deleted too; the GATE 1 parking spot remains.
- Hangar 15 airside redone from the 2014 aerial crop: four grey-beige sliding leaves with a dark glazing strip across x +1.8..-22.3 (the NW/tower end), beige-grey lower wall beside them, plain pale-blue end bay at the south end, airside "15" roundel moved to the south end (x +17). The 2014 photo also shows a lower dark-slate-doored hangar attached to Hangar 15's north end (16 m long); not modelled.
- Hangar 15 re-oriented from an in-sim comparison with the 2014 aerial: 47 x 30 m, heading 138, long SE ('south') wall carries the four-leaf doors (SW end bay plain, "15" roundel at the SW end), NE corner of that wall kept where it was; centre in tower frame x +33.5, z +165. The Shell hangar is shown mostly demolished in the 2014 aerial (frame only); ours is the pre-demolition building.
- Hangar 15 rebuilt again (in-sim review): the doors are in the south gable end (ridge runs back along the 40 m depth), 47 x 40 m (NW end unchanged, extended 10 m south), SE face z +190 in tower frame; the NW end is 30 m from the Shell hangar (no longer anywhere near touching). "15" roundels on the south gable (SW end) and the north gable; offices/awnings moved to the SW eave wall. Low east wing added (16.5 x 26 x 5.8 m, flush with the south face, dark slate sliding doors with a glazing strip, white parapet band) from the 2014 aerial.
- East wing doors now face NE (toward the runway): wing model 26 x 16.5 m, heading 48, same footprint and position as before.
- Hangar 15 main part enlarged to the in-sim comparison with the 2014 aerial: 47 x 54 m (about 7 m more at each gable end, centre unchanged, tower frame z 143..197); east wing moved 7 m south to stay flush with the south face.

- (The temporary pavement hiding near Hangar 15 was undone; draw flags are back to TRUE.)
- East wing reworked from the orange outline: it runs the full length of Hangar 15 and a little more (56.5 x 14.5 x 5.8 m, from x_t -4.5 to 10, z_t 142.5..199), eight slate door leaves on the NE face (toward the runway). It now overlaps apron 1 by about 7 m at its edge and stays 4.5 m clear of the GATE 1 parking circle.
- East wing: "15" roundel (0.65 m radius) on the parapet band above the doors, mid-length, facing NE (the taxiway).

## Hangar 7 (not built yet)
Two reference photos saved in `hangar7-photos/` (see its SOURCES.md): teal upper band with "HANGAR 7" lettering, cream ribbed lower wall with glazing, blue "7" roundel on a white panel at the corner.

## Hangar 4 (not built yet)
Reference photo in `hangar4-photos/` (see its SOURCES.md): yellow ribbed gable end with a wide arched open door, "4" roundel at the upper right, brick annex on one side and an orange-panelled building on the other.

## Hangars 6 and 7 (not built yet)
Reference photo in `hangar6-7-photos/` (see its SOURCES.md): Hangar 6 in front (pale blue-grey side wall, green end wall, "6" roundel), Hangar 7 behind it in blue with a "7" roundel. More Hangar 7 photos are in `hangar7-photos/`.

## Hangar 5 (not built yet)
Reference photo in `hangar5-photos/` (see its SOURCES.md): landside two-storey bronze-glass office block in front, ribbed tan hangar behind with a "5" roundel high on its upper band; Transport Canada / Western Aircraft Services.

## Hangar 9 (no photo, no footprint)
The photos once filed here are Hangar 8 (user, 2026-10-21; now in `hangar8-photos/`, see its SOURCES.md): large hangar with a full-width glazed sliding-door wall under a canopy roof, pale ribbed upper wall and gently pitched roof; no roundel visible in this view.

## Hangar 8 (not built yet)
Two reference photos in `hangar8-photos/` (see its SOURCES.md): grey hangar with a full-width glazed door wall under a canopy, a taller end block with the "8" roundel, and a long low glazed-clerestory wing; the NAIT parkade is behind it.

## Hangar 18 / Edmonton Flying Club (not built yet)
Reference photos in `hangar18-photos/` (see its SOURCES.md). A composite building just north of the control tower, not a box: white two-storey clubhouse with observation room and balcony, green ribbed hangar with two white door leaves, and a striped side wing; "18" roundel.

## Hangar 11 (USAAF T3, 1942; already placed as a plain box)
Reference photos and article notes in `hangar11-photos/` (see its SOURCES.md). Barrel-vault wartime hangar with white cladding, tan sliding doors, three-storey annex with fire escape and "11" roundel; boarded up from 2013, Municipal Historic Resource in 2022, destroyed by a suspicious fire on 22 April 2024. To replace the OSM-footprint box when we build it.

## First hangar, c.1929-31 (not built yet; the 1938 landmark is a merge)
Photos and the list of changes are in `first-hangar-photos/SOURCES.md`. Main finding: `cyxd_hangar_1938_landmark` merges the first hangar's tower and wing with the 1938 barrel-vault hangar; they should be two models.

University of Alberta archive.org items (2026-10-17, `ualberta-archive-photos/`): postcard PC013987 shows the 1938 hangar (barrel vault, brick tower at each end) nearest the terminal, plus a larger second barrel-vault hangar NW of it with a long pale two-storey wing and a brick tower; the second hangar is not identified. Neither is Hangar 11 / Northwest Industries (east side). The postcard's "1929" date is wrong (1938 or later). PC013720 is a clear view of the Administration Building and drive; WCWdb_2534.pdf is the 1937 plan (amended 1943): its SW-NE strip is labelled N 57 deg 30' E (true), which agrees with our 04/22 heading of 57.78; position not checked. Details in the folder's SOURCES.md.

- Hangars 6/7: added an oblique NAIT-parkade photo ("RCMP hangar", looking NW) to `hangar6-7-photos/` with colours of Hangars 7 (steel-blue), 6 (white) and 5 (bronze/charcoal glazed).

## Hangars 39 and 38 (not built yet)
Eight reference photos and notes in `hangar39-photos/` (see its SOURCES.md): Hangar 39 "old PWA hangar" (pale blue/white, door wall facing south, "39" roundel) and Hangar 38 (mustard yellow, "38" roundel) just west of it.

## Hangars 4-8, 11, 14, 18, 38, 39 built (2026-10-12, built OK, not yet checked in the sim)
- New module `airport-cyxd/tools/hangars.py` (called from `gen_buildings.py`): ten new models plus an unplaced Hangar 9. Palette grew to 32 swatches; new ribbed/brick textures (`cyxd_ribbed_green/mustard/steel/tan/white/yellow/teal`, `cyxd_brick`). The old generic placements for Hangar 11, Hangar 14 and USAAF T1/T2 are skipped (`SKIP`) because the new models stand on them.
- Footprints and the reasoning (OSM 2016 outlines checked against the Esri Wayback 2014 imagery, since Google Earth could not be used) are in `docs/cyxd/hangar-footprints.md`; the link index is `docs/cyxd/reference-links.md`; annotated crops are in `docs/cyxd/footprints/`.
- Build: `build.bat cyxd` (sim closed) gave exit 0, empty `_RPTErrors.xml`, `modelLib.BGL` 265 kB. `fspackagetool.exe` stayed alive afterwards and had to be killed (the result was already written).
- **Open questions for the user**: (1) where is Hangar 9 (set `HANGAR9_PLACEMENT` in `hangars.py`); (2) is Hangar 38 the SW and 39 the NW of the west group; (3) gable/door directions of 4-8 are assumed, check against the photos in the sim; (4) Hangar 8 vs the "tall end block" side.
- **Full question list and to-do list: `docs/cyxd/open-questions.md`.** Not done yet: adjust Hangar 15's face to the west line-up photo; Hangar 16 front (five bands, indented bay, box-out next to the Shell hangar); wind sock position (from the PWA 737 video); static PWA 737; Hangar 14 static displays (Bomarc, mounted aircraft); split the 1938 landmark into the first hangar and the 1938 hangar (`first-hangar-photos/SOURCES.md`); General Aviation Centre, Canadian Helicopters hangar and the big NW complex are not built.

## Approaches and SID matched to the 2010 CAP 3 plates (2026-10-14, built OK, not yet checked in sim)
Source: `docs/cyxd/procedures-2010.md` and the plate screenshots in `docs/cyxd/charts/procedures-2010/` (CAP 3, 11 Feb 2010, pages 94-97). Rewrote the ILS 34 Y, NDB 16 Y, LOC(BC) 16 Z and NDB 34 Z approaches in `CYXD.xml` and added LOC 34 X.
- Fix names on the plate: **ULIXU** (IF, 14 DME, N53 20.16 W113 30.83; the earlier notes said ULURU, which is a misreading), **MIRAN** (9.2 DME, N53 24.98 W113 30.77), **KIPUN** (N53 44.81 W113 30.79), **LEFAT** (10 DME, N53 44.08 W113 30.77; moved ~100 m to the plate position). New waypoints XD16C (2.65 DME, MDA step) and XD34A (1.4 DME, 2800 step) are read from the profile views. HH16N removed.
- ILS 34 Y: IF ULIXU 4100, MIRAN, ZXD (3200, FAF), RW34. NDB 34 Z: IF ZXD 4100, procedure turn L, 343 inbound, 3200 at ZXD, then RW34. NDB 16 Y: KIPUN 4300, XD, procedure turn L, 3400 at XD, step to the 2740 MDA. LOC(BC) 16 Z: unchanged route, MDA 2600 added. LOC 34 X: MIRAN 4100, ZXD 3200, 2800 step, MDA 2660.
- Missed approaches are now the plate ones: climb to 4400, track 163 to ZXD (rwy 16) or 343 to XD (rwy 34). Was 3100/4200 placeholders going to ZXD. NDB approaches have `gpsOverlay="TRUE"` (plates are titled GNSS).
- Procedure turns follow the SDK sample `D:\MSFS\MSFS 2024 SDK\Samples\DevmodeProjects\Sceneries\SimpleNavData\PackageSources\data\SimpleNavData.xml`: a `<Transition transitionType="FULL">` holding a `PI` leg then a `CF`. `PI magneticCourse` is the 45 deg barb heading (outbound + 45 for a left turn: 28.8 at XD, 208.8 at ZXD), `distance` is the 10 NM limit. This reading of the sample is unverified in the sim. NDB 16 also has a KIPUN transition straight to XD (no PT; my interpretation of the plan view).
- **EDMONTON City FOUR DEP** added as `<Departure name="CITY4">` (SDK sample structure: RunwayTransitions, empty CommonRouteLegs, EnrouteTransitions). Runways 12, 16, 30, 34: `VA` on runway heading to 3200 (noise abatement, covers the 2800/2500 gradient altitudes), then `VM`. Enroute transitions are single `IF` legs at the plate exit fixes AROUK (N54 16.7 W114 26.3), ABENY (N54 15.1 W113 04.5), NUPPS (N53 08.8 W113 30.3), REFIO (N52 59.1 W114 18.3), BACOS (N52 32.1 W113 38.4), each `-7000`. Climb gradients and ATC vectors cannot be encoded. First attempt used `Name=` attributes per the docs and gave `CompileMemory failed`; the sample's lowercase `name` on `Departure` and no name on `EnrouteTransitionLegs` compiles. Not checked in the sim whether CITY4 shows in the flight planner.
- Not done: RNAV 12/30 (no plates found), radio-range approaches (1940s). The VOT 114.9 MHz is still configured as ATIS 2; the CFS lists it as the VOT.
- Build: `build.bat cyxd -window` (sim closed) gave exit 0, empty `_RPTErrors.xml`, `CYXD.bgl` 34,305 bytes. Gotchas: a leftover "Microsoft Flight Simulator 2024" launch dialog (`gamingservicesui`, with `gamelaunchhelper`) from an earlier build makes the next `build.bat` report "NO BUILD" until it is closed; run one build at a time; use `cmd /c "cd /d <repo> && .uild.bat cyxd -window"`. Kill `fspackagetool` afterwards. Restart the sim to see the changes.

### Hangar 16 rebuild: Aerocentre, Shell hangar, north block, landside wing (2026-10-17, built, not viewed in the sim)
- Source and reasoning: `docs/cyxd/hangar16-photos/SOURCES.md` (photos, 2014 imagery footprint check, OSM way 15822817). Overlay of the new rectangles: `docs/cyxd/footprints/shell-aerocentre-new-model-overlay.png`.
- `aerocentre()` now has **five bays** counted from the SE end (next to the Shell hangar), widths 9.0 / 8.0 / 7.2 / 7.0 / 6.8 m; **bay 2 is the entrance**, recessed 2.4 m behind two angled panels (cream panel with an AEROCENTRE sign board on the NW side, dark glass on the SE side) under the overhanging upper floor; drive-through at the NW end; 38 x 20 x 8.4 m. Placed at tower frame (x 8, z 44), heading 48.
- `shell_hangar()` is now the whole group in one model, origin at tower frame (x 37, z 79): hangar 45 x 42 x 9.4 m (x 6-51, z 63-108, front 8 m behind the Aerocentre front), a two-storey 8 m north block (x 18-48, z 50-63) against the Aerocentre's back wall, and a one-storey 4.8 m landside wing (x 48-68, z 50-104, grey ribbed, yellow posts). The earlier Shell hangar sat 10-15 m too far SE.
- New `shell_logo()` / `shell_sign()`: pecten of a red outline, seven scalloped yellow lobes and a stem, on a white board with a dark rim; a second sign sits high on the hangar's NW end wall. Open bay and the three striped leaves kept.
- Judgement calls: hangar front offset 8 m (aerial and OSM say ~11, the ground photos say flush; the earlier model used 5); hangar south end z 108 (2014 roof ~104, OSM trace 116); Aerocentre z 25-63 (roof 27-62, OSM 44-75). Check against `tower-photos/Edmonton_City_Centre_Airport__4846273897_.jpg` in the sim. Not built: the box-out at the Aerocentre's SE end, the second stepped-back two-storey block, the red STARS sign, the AEROCENTRE lettering (only a bar and swoosh stand in for it).
- Built with `build.bat cyxd -window` (exit 0, `_RPTErrors.xml` empty).

### Hangar 16 fixes after the first in-sim look (2026-10-17, generated, **not built**: the sim was running)
- Front offset (8 m) confirmed good in the sim.
- Aerocentre: ribbon windows and ground glazing now continue round the SE end wall (the 8 m clear of the hangar), per `Edmonton_City_Centre_Airport__4846273897_.jpg`. The landside NW corner of the upper floor is cut at **45 degrees** (5.5 m legs) over the open drive-through, with a three-pane ribbon on the diagonal face (`flickr_woodhead_14669349810.jpg`; OSM has no diagonal); navy columns now carry the overhang **down to the ground** (the first pier started 0.5 m up). The mid-height navy band no longer shares a plane with the cream spandrel (z-fighting): it stands 5 cm proud.
- Shell sign: the pecten is now a texture (`tools/assets/shell_sign.png`, written to `modelLib/texture/cyxd_shell.png`) traced from the SVG `docs/cyxd/hangar16-photos/shell-pecten-reference.svg` by `tools/make_shell_sign.py`; `Mesh.poly` takes `tex=` / `uvs=`. Two sign boards: the hangar front column and the NW end wall.
- STARS: red bar (8 x 0.6 m) high on the landside wing's NW end wall (lettering not added).
- To see it: close the sim and run `build.bat cyxd -window`, or rebuild from DevMode, then restart the sim.

### Hangar 16 rework from the 2014 Google Earth aerial and the 2012 street view (2026-10-17, built, not viewed in the sim)
- Both references are saved (`aerials/google-earth-hangar16-201407*.jpg`, `hangar16-photos/streetview-27-airport-rd-landside-201206.png`); scale (8.94 m bar = about 7.6 px/m on the lowres copy), registration and measurements are in `hangar16-photos/SOURCES.md`.
- Aerocentre now 28 x 20.5 m (it was 38 x 16 then 38 x 20), at tower frame x -4..16.5, z 44..72. The 45-degree **corner cut-off is replaced by a "horn"**: a 6.2 x 6.9 m triangle of upper floor projecting from the landside NW corner (windows on its diagonal face), over the drive-through, on columns that reach the ground.
- Shell group (one model, origin x 36.75, z 87.5): hangar x 7..46, z 72..117 (45 x 39 x 9.4); **north wing** (2 storeys, 8 m) x 16.5..46, z 58..72; **west wing** (one storey, 4.8 m, lower than both) x 46..68, z 58..113. The **STARS red band wraps the west wing's north corner**, with the ground-floor windows starting just round the corner (landside face and the end wall). The blue "16" roundel is on the hangar's landside wall by its NW corner; a Shell sign on the SE part of that wall; the NW end-wall sign moved up into the gable.
- Front offset between the Aerocentre and the hangar is now 11 m (aerial) instead of the 8 m you had judged good: one value to tune if it looks wrong (`x0` of the Aerocentre in `aerocentre()` and the hangar `z1` in `shell_hangar()`).

### Hangar 16 follow-ups (2026-10-17, built, not viewed in the sim)
- **Shell logos were upside down**: `Mesh.poly` reversed the corner list to fix the winding but not the `uvs`; it now reverses them too (checked numerically: the top corners of all three sign quads carry v = 0).
- The hangar roof is **flat** with a red parapet trim all round (Street View `streetview-19-airport-rd-landside-south-201206.png`). Added a two-row glazed ribbon with yellow frames on the landside wall, and on the south (SE) end wall a ribbon of six small windows near the top above vertical panel seams; the end-wall detail is read from one oblique photo, so treat it as approximate.
- Hangar 16 heights (from `hangar16-photos/flickr_woodhead_14669349810.jpg`): the hangar stands as much above the north wing as the north wing stands above the west wing. Now west wing 4.8 m, north wing 8.0 m, hangar 11.2 m (was 9.4); step of about 3.2 m. Built, not viewed in the sim.

## Street View review, Hangar 4/38/39 changes, old terminal stands (2026-10-18, built OK, not viewed in the sim)
- 82 landside Street View screenshots filed into per-building folders (`hangar3-photos/` ... `hangar40-photos/`, `building21-terminal-photos/`, `other-buildings-photos/`, plus new files in the existing hangar folders); each has `SOURCES-streetview.md`. Identification, review findings, the pedestal-aircraft verdict and the built / outstanding list are in `street-view-review.md`.
- `hangars.py`: Hangar 4 now faces the runway (heading 270, door on the 71 m west wall: an interpretation, see the review); Hangars 38 and 39 raised (ridges 15.7 m / 17.6 m) and placed side by side (39 moved 120 m SE-ward from its OSM spot at the user's request); Hangar 5 lower wall brown; Hangar 18 landside facade with the "18" roundel.
- `CYXD.xml`: four jetway stands at the old terminal (Building 21, OSM way 230718907) read from the pavement strips in the 2014 imagery (`footprints/terminal21-stands-overlay.png`): gate 7 relocated, new gates 10-12 (parking 118-120), PARKING paths, one new apron. Gate 7's old position overlapped the northern stand. Built with `build.bat cyxd` (exit 0, `_RPTErrors.xml` empty). Check in the sim that the jetways reach the aircraft.

## User corrections and four new buildings (2026-10-21, built OK, not viewed in the sim)
- **Photo corrections (user):** `canadian-helicopters-photos/` is Hangar 40 (moved to `hangar40-photos/`); the "Hangar 9" photos are Hangar 8 (moved to `hangar8-photos/`; the unplaced Hangar 9 model and `modelLib/cyxd_hangar9` are deleted); `hangar37-photos/` are Hangar 38 (merged into `hangar38-photos/`, folder gone); Hangar 20 is the Esso building (`hangar20-photos/`, copies of the Street View shots). There is no Hangar 37 evidence left.
- **Hangar 39 re-identified and re-placed:** it is the big pale-blue double hall (OSM 230718901, 107 x 90.5 m, heading 138) next to Hangar 38, with Hangar 40 at its north-west end in photo 28. That undoes the 2026-10-18 move that put a 56 x 79 m box 44 m E / 50 N of Hangar 38 (that box stood on the double hall's footprint). The new model has two tall bays (walls 14 m, ridge 17 m) and a lower 13 m service strip; the "39" roundel position is assumed.
- **New models** (all in `hangars.py`; palette now 36 swatches, so every model's UVs were rewritten):
  - Hangar 3: 81.6 x 25.7 m pale-blue flat-roofed hangar at 53.574710, -113.508533, heading 90 (landside east), traced from the 2014 Wayback roof (OSM 325273617 is 76 m and about 8 m off); tall south part 8.2 m stepping to 6.4 m at the north end, navy fascia and red line, cream roller doors, teal window columns, entrance bump, "3" roundel. Airside wall is generic (no photo). Tan block annex at its south end is a separate small model.
  - Dark-blue gabled hangar north of it (OSM 325272095, 24.6 x 20.7 m): navy walls, grey roof, white end with a roller door (assumed to face south), blue air-handler box. Unnumbered.
  - Hangar 20 (Esso): 45 x 45 m upper tier plus an 8-10 m lower tier on its SW and SE sides, at 53.569788, -113.521578, heading 228, measured on the 2014 imagery (not in OSM). Esso oval, glazed bands, rounded front corners, "20" roundel.
  - Hangar 40 (Canadian Helicopters): 38 x 25 m, the white roof at the NW end of OSM 230718900, heading 318 (front to the car park). White hall with a big door, brick office with awnings and a gabled canopy, taller white block with the "40" roundel. The blue-grey gabled hall at the SE end of that OSM way is not built.
- **Assumptions to check in the sim:** door directions of the dark-blue hangar and Hangar 3's airside wall; which end of Hangar 3 carries the entrance bump; the Hangar 40 front direction.
- Build: `build.bat cyxd` exit 0, `_RPTErrors.xml` empty (14 bytes). `gamelaunchhelper` and `gamingservicesui` were still running afterwards (the permission classifier blocked killing them last time); dismiss the dialog by hand.

### Follow-up (2026-10-21, later)
- **Hangar 19** (user: the low brown/tan building beside the Esso building, photos 06-09; maybe the General Aviation Centre): built from the 2014 aerial, not OSM (nothing mapped there in 2016). About 65 x 29 m, long axis bearing 142, centre 53.569158, -113.520582, heading 232 (front faces Airport Rd). Two low tan wings, brick centre, stair tower. The `general-aviation-centre-photos/` building (two-storey brick with a tan drum and sign) does not obviously match it, so the General Aviation Centre link is unproven.
- **Hangar 40:** the big door is now on the gable wall opposite the landside (user).

- **Hangar 39 reworked (user, using `hangar39-photos/13207255803.jpg` and `13207268493.jpg`):** two gabled bays 13 m apart with a lower set-back middle block (roller door, two doors), a steel truss frame across the gap at the front, a 12 m back wing across the full width (the "pale blue stepped blocks" in the Street View shots), recessed white door walls with two tiers of louvres, and blue piers projecting at both sides of each door wall. Built OK, not seen in the sim.

### West-lineup photo review and ILS glideslope hut (2026-10-21)
- Photo `west-lineup-photos/flickr_woodhead_13858722704.jpg` is taken from the NAIT parkade roof looking WSW across the airfield (1024 px, so only gross shapes). H15, H19 and H20 airside views checked against the user markup: **H15 wing** now has a pale blue-grey face with a central cluster of window bays and a porthole instead of dark slate doors; **H20** got a long ribbon window over the SE half of its NE (airside) wall and a big dark door (15 x 7.6 m) in the NW half; **H19** airside is a long low dark-brown/tan face with a red-brick block toward the SE end (left in the photo), roughly where the model has it but nearer the SE end than the model's centre block; not changed.
- **ILS glideslope hut:** the small red-and-white checkerboard hut in the infield (user markup 2) sits at the 2014 aerial hut at 53.568983, -113.511000, 9 m north of the glideslope point already in `CYXD.xml` (53.568901, -113.511002). New model `cyxd_gs_hut`: 5.5 x 4.5 x 3 m, checks on all walls, door on the east face, a 9 m mast and antenna box 5.7 m north. Built OK, not seen in the sim.

### User corrections round (2026-10-21, built OK, not viewed in the sim)
- **Hangar 14**: main door bays moved to the south gable end (heading now 180, 90.8 x 100 m); museum entrance, glazing and canopy moved to the east wall.
- **Hangar 15**: landside (north gable) "15" roundel removed; airside roundels stay.
- **Tower (17)**: the sign the photos show is an oval NAV CANADA plaque on the annex wall by the entrance (`oval_sign`, texture `make_signs.py`); there is no roundel on the tower itself. The stair cage was replaced by a narrow flat-plated ladder shaft (photos 11094305354 / 11094396223); it is still on the NW face. Which face the ladder is on was not re-checked against the user's "north side".
- **Exclusion**: new polygon "No buildings: Airport Road to runway 12/30" (rectangle in the 12/30 frame, 36-314 m SW of the centreline, -110..445 m along it; Airport Road is OSM way 15824250, 318 m from the centreline). Hand-written in `CYXD.xml` (not in the generated block).
- **Jetways** 3 and 4 (in front of Hangar 18) deleted; the GATE 3 / 4 parking spots remain.
- **Hangar 20**: Esso oval is now a texture (blue rim, white, red "Esso", `esso_sign.png`); airside "20" roundel above the big door.
- **Hangars 38 / 39**: landside (back wall) roundels added to both; Hangar 39 also has an airside "39" on the set-back middle block.
- **Hangar 40**: heading 318 -> 228 and moved to 53.574931, -113.528590, so it stands at right angles to Hangar 39 with its landside wall facing the car park behind 39 (about 66 m NW along, 72 m NE across from 39's centre; position is judged, not measured).
- **Hangar 4**: ridge turned so the west door wall is the gable end (ridge E-W, rise 4.4 m over the 71 m width).
- **Hangar 5**: offices moved to the south side; "5" roundel above them.
- **Hangar 8**: landside windows (two rows plus doors) and LAW OFFICE / AVIATION signs (`lawoffice_sign.png`) on the end block.
- **Hangar 11**: roof vents now sit on the barrel roof; NORTHWEST INDUSTRIES LTD. roof board and COMMERCIAL AIRCRAFT SERVICE lettering (1956 photo); fire escape moved to the landside (east) face.
- Textures `esso`, `navcan`, `lawoffice`, `nwi` are produced by `tools/make_signs.py` and copied by `gen_buildings.py`.
- Deferred: the building south of Hangar 11 (`open-questions.md`).

### Hangar 18 rebuilt as three blocks (2026-10-21, built OK, not viewed in the sim)
- `hangar18()` now has three stacked blocks (road to apron): C landside club block (white pilastered wall with window slots on Airport Rd, entrance with the FLYING CLUB board, glazed club room at the SE end with a roof overhang, viewing deck over a lower block, fascia lettering, "18" roundel), B middle block (teal base, striped upper wall, cream pier with door), A airside block (olive hangar with two white leaves on its SE face, pier, white wing with swoosh and "18"). Footprint 70 x 84 m, centre 53.568558, -113.519833, heading 48. Measurement and video notes: `hangar18-photos/SOURCES.md`, overlay `footprints/hangar18-three-blocks.png`.
- Uncertain: the aerial shows no clear roof for C (placed 13 m deep on the road side of B, from the street views); the hangar doors now face SE (toward the tower), as in the video, not NE as before.
- New texture `efc` (`make_signs.py`).

## Follow-up round (2026-10-21, later)
- **BCATP hangar row A removed** (added to `SKIP` in `gen_buildings.py`): its 75 x 100 m generic box overlapped the Hangar 18 complex (brown roof in the sim).
- **Hangar 40 enlarged** to fill the hole in the sim aerial (user: the grass patch NW of H39 is where it stood): 72 x 46 m, heading 228, centred 53.575004, -113.529385 (measured from the screenshot at about 1.73 px/m, ±3 m). The white part is kept (hall deepened to 46 m) and the blue-grey gabled hall of OSM 230718900 is added at the SE end.
- **Hangar 18 landside club block shifted 18 m toward the tower (SE)** to the user's purple box (x about -2..62 in the complex frame); complex is now 88 x 84 m, centre 53.568498, -113.519742.
- Not viewed in the sim.

## Old terminal (Hangar 21) and parking garage (2026-10-21, built OK, not viewed in the sim)
- Footprints measured on Esri Wayback release 14035 (2017-08-10, zoom 19, 0.18 m/px); the overlay is `footprints/terminal21-2017-overlay.png` (red = terminal parts, green/cyan = garage tiers, drawn from the model parameters).
- `cyxd_hangar21`: heading 51, centre 53.570940, -113.523178, 162 x 70 m. Dark-brick north wing (9.5 m) with the "21" roundel and red fins on its landside face, a two-storey brick spine along the apron with a glazed ground floor and canopy, a lower cream landside wing with a glazed entrance, a taller SE block, and a covered walkway on piers to the garage. Era is a blend of the 2012 (cream, glazed) and 2019 (brick, Amiskwaciy Academy) Street View shots.
- `cyxd_garage22`: heading 58, centre 53.570567, -113.524067, 100 x 72 m. Open piered ground floor, three brown-clad decks stepping down toward the SE (10.4 / 7.2 / 4.0 m), stair tower at the NW end, "22" roundel on the NE face (photo 14).
- Not modelled: the curved grass berms between the gates, flagpoles, the school sign. Heights are guessed from shadows. The existing gate 7 and 10-12 jetways were left as they were.
- Hangar 19 was already built earlier today (see the follow-up above); nothing new was done for it.

## Jetways and the 1938 hangar (2026-10-21, built OK, not viewed in the sim)
- Jetways for gates 5, 6, 8 and 9 removed from `CYXD.xml`; only the four at the old terminal (gates 7, 10, 11, 12) remain. The GATE parking spots themselves are untouched (gates 1-9 still carry `passengerAccessType="JETWAY"`, so a gate without a bridge may show in the sim as a gate with none; say if you want those spots removed or turned into ramp parking).
- `hangar_1938` (the "landmark") reworked from the later research: the 30 x 13 m office wing and the first-hangar tower are gone (they belong to the 1930s first hangar, still unbuilt, see `first-hangar-photos/SOURCES.md`). It is now the barrel vault (corrugated steel walls, dark roof) with a tall stepped five-storey brick tower flush with the front at the right and a shorter brick tower at the left (EA-160-402, postcard PC013987), a front with four timber door leaves with small panes (Fort Edmonton replica) and tall windows either side. It is now mirrored once like the other models, which changes which end the tall tower is at in the sim; check it. Tower sizes (10 x 10 x 20 m and 8 x 8 x 13.5 m) are estimates.

## Second hangar ("orange") built (2026-10-21, built OK, not viewed in the sim)
- `cyxd_hangar_second` (`hangar_second()` in `hangars.py`): 70 x 44 m massing model, heading 57.78: a pale two-storey flat-roofed wing with ribbon windows and a red band (left), brick towers flush with the front at both ends of a barrel-vault hall (dark roof, big door opening with four timber leaves under the arched front), a low service block behind the wing. Wing and tower details are guesses; sources are postcard PC013987, ET-28-900 (1982) and the 1944 aerial.
- **Moved 14 m toward the apron (NE)** from its proper position (53.56945, -113.52610) so its building exclusion keeps the Chateau Nova Hotel (OSM 230718905, whose NE corner reaches into the footprint); the exclusion now clears the hotel and the 1938 hangar's exclusion. How to restore the proper position and the larger 70 x 55 m reading is in the comment block above `ORANGE_LAT` in `hangars.py` (`ORANGE_SHIFT_NE_M = 0.0`; the hotel is then excluded unless rebuilt).
- The exclusion also removes (assumption, unchecked in the sim) the part of OSM building 131 Airport Rd that it touches.

## Hangar 4 two doors (2026-10-21, built OK, not viewed in the sim)
- From the 1989 City of Edmonton archive photo (`City of Edmonton Archive photos/1989/EA-207-425.JPG`, airside view of Hangars 4-7): Hangar 4's runway wall has two doors, a dark open one at the north end and a white closed one at the south end, with a two-storey orange-panelled bay (windows) between them. `hangar4()` now has both (north door x 3..32 m, orange bay -4.5..3, south door -30..-4.5 in model frame), the "4" roundel moved onto the orange bay, and the old orange block off the south end removed. Widths are scaled from the photo (about 0.175 m/px at the hangar), so they are ±3 m.
- The same photo shows Hangars 6 and 7 painted blue in 1989 with dark open doors under white canopies, and Hangar 5 tan/brown with a dark open door. The models keep the later (2010s) white/green and white-door look; not changed.

- Follow-up: Hangar 4 keeps the arch. The Government of Alberta sign moved to the north (viewer-left) shoulder of the north door and the "4" roundel back onto the yellow wall at the door's south shoulder (north door now x 5..32, 1.5 m strip before the orange bay), as in `Edmonton_City_Centre_Airport__4846283523_.jpg`. Hangar 5's west wall is tan closed doors (user), so it stays; its glazed office is now 22 x 30 m, flush with the west wall, with windows on the west face too.

## Review round "Oct 21 Mk 3" (2026-10-21, built OK, not viewed in the sim)
Offline check renders used a throwaway software rasteriser (scratchpad, not committed).
- **Stray building SE of the terminal:** nothing of ours stands there (our parts are all inside the terminal footprint; OSM only has the school and the Fire Station 8 outline under the garage), so it is a sim-generated building. New exclusion polygon "Old terminal: SE end and landside surroundings" (terminal frame x -20..150, z -95..-18). Not confirmed in the sim; if it persists it is not a building the polygon types cover.
- **Jetways** 7, 10, 11, 12 moved so each root stands at the building face (z 36 on the spine's apron wall, gate 7 on the north wing's NW end wall); the GATE parking spots moved 25 m out along the new headings (231 for 10-12, 141 for gate 7). Gates 10-12 are 32 m apart. Each gets a small boarding bay with a door in `hangar21()` (authored x = footprint x - 5, z = footprint z - 17.5). Jetway-object origin convention still unverified.
- **Terminal:** walkway from the garage now runs straight into the spine's landside wall (floor 5.2, roof 7.4, over the low wing) instead of ending on the low wing's roof; viewing lounge moved from the landside to the apron (NE) face at the SE end.
- **Garage:** ceilings added under the three decks (the open ground floor had no underside, so the decks vanished from below); lower tiers have 1.1 m parapets.
- **Hangar 15:** landside "15" roundel on the SW eave wall toward the NW end. **Hangar 18:** the cream pier z-fought with the teal/tan airside face of the middle block (now 12 cm proud); roundels on the office wing's NW end wall and near its NW corner on the landside. **Hangar 39:** walls 16.7 m (a third above Hangar 38's 12.5 m), doors, louvres, truss and roundels scaled.
- **Hangar 40:** exactly three masses, as the user says: a brick office with the landside entrance in the middle, a gabled white hangar on each side (equal size, the SE one 3.5 m forward of the office); the separate tall block and the extra blue-grey hall are gone; office roof is flat grey with a red parapet, not a red slab.
- **Hangar 4:** the airside wall is now a 1.3 m frontage with real arched recesses (dark hall, maroon columns, raised arch surround, closed white door set back); Government of Alberta sign is a texture (`goa_sign.png`, `make_signs.py`) with the name.
- **Hangar 5:** office wing 11 m wide, full depth, glazed on the south end, airside and landside; "5" roundels airside (beside the door header, south corner) and landside (south end of the east wall, Street View 50/51).
- **Hangar 6:** airside roundel at x 18.2. **Hangar 8:** door wall and main gable turned to face north (door wall on the hall's north end wall, ridge N-S, projecting sidebars, lean-to canopy); landside from Street View 59/61 (roundel and signs on the tall block, ribbon windows, glazed hall). Interpretation: the hall stays at the north end of the footprint, so the footprint is unchanged.

## 2026-10-21 Hangar 14 front and frontage displays (generated, not yet built or seen in the sim)
- Hangar 14 reworked from the Commons photo, Street View and the 2014 aerial (`tower-photos/EDMONTON_MUNI_AIRPORT__15439598181_.jpg`): lettering, glazed door bays, awnings and lobby are on the SOUTH face (the earlier "entrance on the east wall" was wrong); west two-storey wing; east wall = tall upper windows over a lean-to. New `museum` texture (`make_signs.py`): the building lettering and the black roadside sign.
- New models in `tools/display_aircraft.py`: `cyxd_h14_bomarc`, `_norseman`, `_memorial`, `_voodoo`, `_sign` at the OSM nodes (sign 9 m NW of the Bomarc, position estimated). The sign is the current black logo sign (2022+); the older blue "AIR MUSEUM" board (2019 Street View) is not built.
- Build needs the sim closed (see CLAUDE.md). Check in the sim: lettering reads left to right from Kingsway, awning and door positions, pole heights and tilt angles.
- Hangar 14 windows and doors counted (later the same evening): a perspective fit of `h14-kingsway-81` (residual < 0.1 %) shows 18 upper windows on an even pitch on the west wall; the 2014 aerial gives the east wall the same 18 bays from 7.2 m, 15 visible because a porch block (59-78 m) hides three. Pitch 5.1 m is calibrated from the east wall (the aerial) and the 100 m length, not measured directly. Lower small windows: 2.85 m (west, read off photo 81) and 2.55 m (east). Every window now has a frame and 2 x 2 panes (`pane_x` / `pane_z` in `hangars.py`) and doors have frames, rails and a light (`door_x` / `door_z`). Added: west lean-to ledge, one-storey block at 47-67 m, west doors at 14 and 45 m, east lean-to from the south face, east porch block, V marks beside the lettering (texture now 36 x 1.4 m). Built OK (exit 0) with the sim closed.
- Still guessed: north-end windows (no photo), the pane layout of the upper windows (photo 79 suggests 2 x 2), the exact porch-block shapes, the ladder at the west wing corner.

## Hangar 11 landside pass (2026-10-21)
- The south annex now runs the full width (x -29..43) so its landside end is flush with the long wing's wall; the old 19 m gap and the separate stair tower are gone. Roundel moved to the landside corner (3rd floor, as in 11094273884).
- Single fire escape (it had a free-standing ladder floating beside the landings): ladder up the south face next to the landside corner, carried 1 m above the roof, two landings with green doors on the landside face beside it. Photo 64 shows a second, smaller escape near the chimney at the north end of the wing; not modelled.
- Relief: corner boards, belt courses at the floor lines, framed double-hung windows with sills (`win_x`/`win_z`), a one-storey block in front of the wing (10 windows + door, photos 65/66), U-Haul double doors.
- Counts (guessed from photos 63/64/65, pitch 2.3 m): 27 per floor on the wing, ground row skipped behind the low block; 5 per floor on the annex's landside face; 20 across the annex south face. Not measured by perspective fit.
- Still guessed: whether the annex really spans the whole south end (the 1956 photo suggests a lower wing beside it), the wing's south start, chimney shed.
## Review round "Oct 21 Mk 4" (2026-10-21, built OK, not viewed in the sim)
- **Vanishing front walls and roofs of the blue (1938) and orange hangars: found.** The end-cap polygons of both barrel vaults start with two identical points, so `Mesh.poly` took a zero cross product as the normal (zero normal, winding unchecked): the end walls were culled and unlit. `Mesh.poly` now uses Newell's method (robust for any polygon); an offline check of all 60-odd .gltf files finds no triangle whose winding disagrees with its normal. If the roof still vanishes from the ground in the sim it is not this bug.
- **Tree exclusion (new, there was none before):** the building polygons never removed trees. New `veg_xml` writes polygons with `VegetationScale/Density 0` and `ExclusionFlags 7` (the pattern in the bridges package). One convex-hull polygon covers Hangars 38, 39 and 40 plus 14 m all round, so it includes the ground between 38 and 39. Defined in `hangars.place()` (`VEG_EXCL`).
- **Building between the garage and the old terminal:** the polygon from Mk 3 covered only the SE end. Now a polygon over the whole block (terminal frame x -100..100, z -130..45) AND an `ExclusionRectangle` (`excludeAllObjects`, as for the tower and XD) over its bounding box, in case it is a base-scenery object that building polygons do not touch (`OBJECT_RECTS`). Still unconfirmed in the sim.
- **Garage 22 rebuilt open:** a paved ground deck, a column grid, and per level a concrete slab with a 1.1 m brown cladding band on the rim and an open slot above it (Street View 15-18); decks at 10.4 / 7.2 / 4.0 m reaching x 30 / 40 / 50. The top-deck "dish" was dropped; the "22" roundel moved onto the stair tower's NE face.
- **Hangar 40:** an airside door on each hall (four leaves, header) and an airside "40" above each; the landside roundel stays.
- **Roundels:** Hangar 19 airside (brick centre), Hangar 8 on the sidebar beside the big door, Hangar 7 landside (high at the corner of the 109 St wall), Hangar 4 landside near the south end (Street View 47).
- **Hangar 14 vents:** the six air handlers sat at the ridge height on the pitched roof; `roof_vents` now takes a height function and they follow the pitch.
- **NWI sign:** lettering is now Franklin Gothic Medium thickened, set letter by letter with wide tracking, jitter, rough edges and faded ink (`painted_text` in `make_signs.py`), after the 1956 photo.
- **Hangar 5 office:** curtain wall (`curtain()` in `hangars.py`): three bronze panes and a dark spandrel with thin dark mullions standing 18 cm proud, on the south end, airside and landside faces (Wikimedia 11094269004, Street View 50). Landside: a low dark-grey annex at the north end with a man door and two round vents (Street View 48/49), plus a man door near the south end.
- **Window depth (all `hangars.py` models):** `Mesh.window` can add a projecting grey surround and a deeper sill (`Mesh.frame`, set by `fmesh()`); skipped past 48 000 vertices. New palette swatch `GLASSB` (index 36).
- **Hangar 4:** the eave trim now stops at the orange bay (front faces were coplanar), the bay is 10 cm taller, the airside roundel moved down off the trim; landside "4" roundel and two man doors (Street View 46/47).
- **Hangar 3 (z-fighting on the navy end bars, again):** the fascia's end boxes sat exactly on the end walls' planes (x = +-40.8 and the step at x = 28). They now overshoot the walls by 6 cm, and at the step both fascias are buried inside a wider (+-15 cm) navy cap. Checked with a pairwise coplanar-overlap script: no same-direction coplanar overlaps left on the end walls.
- **Hangar 3:** the step wall between the two parapet heights stood flush with the parapets' outer faces (coplanar); now 5 cm inside.
- **Dark-blue hangar (north of Hangar 3):** the roller door sits behind projecting jambs and a header, with ribs and a bottom rail.

### Hangar 8 landside, second pass (2026-10-21)
- Wing now steps down (Street View 59): 8.6 m part by the block (ground row, first-floor ribbon of six big panes starting on the block, roof clerestory with glazing on three sides), then a 6.2 m part at the far end with smaller windows. Ground row is a few windows and doors, not a continuous row; the tall narrow window moved from the hall onto the block under the roundel.
- Signs resized and moved from the photo: LAW OFFICE 5.0 x 0.85 m across the block/wing joint at y 7.8, AVIATION 4.4 x 0.6 m a step lower and further along; thin widely spaced regular-weight capitals (`arial.ttf`, via `painted_text`) on pale boards with a dark edge and a backing board. The wing is only 21 m long in the footprint, so the tiers are compressed against the photo.
- Hangar 8 landside recount (same day, from a 2x crop of Street View 59): the previous ribbon rows had their x range reversed (negative gap, overlapping panes) - fixed. Photo counts used: tall narrow window under the roundel; ground tier window, window, door, long strip window, glass door, window; ribbon of ~8 panes starting under the tower; clerestory of ~8 panes; far end a one-storey skirt (window, door) with 3 small windows above. The tower (13 m) now stands over the wing start, set back 0.5 m, with the roundel on a lower 11 m slab; LAW OFFICE sits across the tower base and AVIATION on the eaves cornice. Profile added: plinth, navy band under the ribbon, eaves cornice, downpipes, slab pilaster, projecting skirt, navy window surrounds, roofs on the wing (the wall boxes were open-topped).

## Window frames (2026-10-21, review feedback)
- `Mesh.window` (gen_buildings.py): glass is now the front face of a closed dark backing box sunk 0.1 m into the wall (no see-through); surround/sill boxes start 0.06 m inside the wall (they used to start 4 cm off it and float); `pane_x`/`pane_z` mullions likewise embedded. Applies to every model. Not built or seen in the sim.
- Exclusion: `m.keepout(x0, x1, y0, y1, z0, z1)` (model frame, before `mirror_x`) in a building function; any window (`window`, `rows_x/z`, `window_row`, `pane_x/z`, `win_x/z`) whose box touches it is skipped. Add it before the window calls.
## Parkade (garage 22) Mk 5 (2026-10-21, generated, not built or seen in the sim)
- Only perimeter columns now. Every deck is a U: flat side slabs and NW end round a central bay (30 m wide, from x -14 model frame) whose ramp slab descends about 7 % to the level below; the lowest ramp reaches the ground near x 40 and is the vehicle entrance (edge beams, gate island, ticket posts, barrier booms, yellow bollards outside the SE mouth). Shape from `footprints/terminal21-2017-overlay.png`; bay width/start are read off the aerial (+-3 m).
- Sideboards (user clarified, Street View 15 `parking-garage-15-streetview-201607.png`): the long brown ribbed boards along the side. The deck-rim boards existed; the ground-level one (block plinth 0.9 m, board to the first slab, x -50..45) was missing and is added on both long sides. The extra "22" roundel was removed.
- White box: it was the generic "Administration Building" (50 x 20 x 10 m, 1940s-50s, `historic-buildings-genericbuilding.xml`) at terminal frame (66, -12), inside the old terminal's landside; not in any 2012-2019 photo or the 2017 aerial, so it is now in `SKIP` in `gen_buildings.py`.
- New tree-exclusion polygon "Between the parking garage and the old terminal" (terminal frame x -60..100, z -62..-22) in `hangars.place()` (`VEG_EXCL`).

### Second (orange) hangar enlarged from ET-28-900 (2026-10-21, not built)
- 1982 photo ET-28-900 (not the Hudson General 1990 photo): scale from the horizon-distance ratio against the foreground white building and the parked twins gives about 0.9-1.0 m/px at the hangar. Resized from 70 x 44 x 12.5 m to 80 x 52 m, crest 15.5 m (wall 9, rise 6.5, span 44), wing 8.8 m, towers 15 and 17.5 m, doors 8.4 m high. NE shift 14 -> 18 m. Estimate good to about +-20 %. The hotel (OSM 230718905) clearance was NOT re-checked (no outline in the repo); verify in the sim.
- Stepped front (Street View 14, archive MS-1270.213.3): the tiers already step back 10 m per level toward the SE (decks reach x 30 / 40 / 50). Now each tier also overhangs the one below (columns stop 3 m short of the slab edge, ground columns 4 m short), and the ground board stops at x 46. The photo shows the top deck as a flat U with its centre sloping down toward the SE end, as modelled; the bay is widened to 36 m (was 30). Not done (unclear from the photos): finer 5 m half-steps seen in the aerial, and the possibly fourth deck on the tall NW end.

- Hangar 7 landside reworked from Street View 54-56: seven awning windows, a glazed entrance with awning and crest sign, one man door, roundel raised to 6.5 m; the annex moved to two white lean-tos on the +x wall (photo 56), dark band removed.
- Level check against MS-1270.213.3: three above-ground decks (4.0 / 7.2 / 10.4 m) over an open ground level with perimeter columns, tiers stepping down to the SE, tall NW end with the stair tower, U decks with a sloped centre bay: the model matches, no geometry change. Offline previews (software z-buffer rasteriser, flat shading, not committed script) in `docs/cyxd/compare/parkade-render-*.png`: photo angle, SE front, aerial, NW end, NE side.
- Parkade Mk 6 (user review of the renders; not built): the bay now slopes DOWN TOWARD THE BACK (NW) from deck level at the front, 44 m long, to a 10 m flat landing against a back wall (the landing is the next deck's top, the lowest lands on the ground) with nose-in stall stripes; U decks open to the front. Entrance moved to the left-most (-Z, SW) quarter of the front (ground level, gate island at z -27). Front steps back in quarters toward +Z (east, toward the terminal): left quarter full extent, the bay half 6 m less, the right quarter 12 m less (ESTIMATED from MS-1270.213.3 and the 2017 aerial; no surveyed footprint exists). The "22" roundel stays on the stair tower's NE (land side) face; the photos actually show a roundel on an angled tower near the east end of the front, not reproduced. Renders redone with a ground plane, depth shading and outlines (`docs/cyxd/compare/parkade-render-*.png`).
