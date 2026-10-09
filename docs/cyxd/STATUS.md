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

