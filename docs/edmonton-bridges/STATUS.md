# Edmonton bridges status

Last updated: 2026-11-23 (reference data refetched; see the 2026-11-23 section). Package: `scenery-edmonton-bridges/` (project `scenery-edmonton-bridges.xml`, definition `PackageDefinitions/cardboardgt-scenery-edmonton-bridges.xml`, version 0.1.0).

## What this is

Version 0.2.0 holds the Tier 1 downtown valley: 15 models and 16 placements (R10, R9, R11, R15, R13, R12, R14, P152, B254, B255, F256, V257, N258, N259, N260). Flat-colour glTF built by `scenery-edmonton-bridges/tools/gen_bridges.py` from the reference data; what is sourced and what is assumed is in `docs/edmonton-bridges/MODEL-NOTES.md`. Compiled, not yet seen in the sim. `PackageOrderHint` is `CUSTOM_WORLD_SCENERY` because these are city objects, not an airport.

## Build

From the repo root: `build.bat bridges` (PowerShell: `cmd /c ".\build.bat bridges"`). Short name `bridges` matches the folder `scenery-edmonton-bridges`. See `CLAUDE.md` for the SDK path override.

Built on 2026-10-14 with the sim closed (the 0.1.0 text follows; 0.2.0 compiled the same way, with a `ModelLib` asset group added). `_PackageInt/_RPTErrors.xml` is empty and `Packages/cardboardgt-scenery-edmonton-bridges/Scenery/cardboardgt/edmonton-bridges/edmonton-bridges.bgl` was written (56 bytes, nothing placed). `fspackagetool` did not write `layout.json`; one was added from the built files so the package folder has an index. Both `Packages/` and `_PackageInt/` are gitignored.

## What to model

Three inventories. `docs/edmonton-bridges/bridges.md` is the North Saskatchewan crossings from Devon to Scotford. `docs/edmonton-bridges/freeway-bridges.md` is the freeway structures on VFR lines among CYXD, CYED, CYEG, CZVL, CFB6, and CEZ3. `docs/edmonton-bridges/lrt.md` is the above-ground LRT stations, viaducts, and extension bridges. The freeway list names the cross road on the QE2, Yellowhead, Henday, Whitemud, and Sherwood Park Freeway decks, and records the Henday, Whitemud, Terwillegar, Groat, and Capilano bridges left off. Highway 16 west of the Henday, Highway 21, and the other crossings added on 14 October are plotted as crosses and still left off the include list. Deck, approach, ramp, and cross-road geometry for every plotted road and river bridge is in `bridge-geometry.json`. Above-ground LRT centreline geometry, including construction and unfunded alignments, is in `lrt-tracks.json`. The build order is `docs/edmonton-bridges/PRIORITY.md`. It ranks every included and excluded bridge, viaduct, and station by how it reads from the air, whether it falls on a VFR approach, and whether it is a named fix on the Edmonton VFR terminal chart or the City Centre helicopter chart. First box is the High Level Bridge and the Dudley B. Menzies Bridge together. Reference briefs for R8–R15, the Groat ravine decks G116, G117, Z125, T133, and G119, P152 and B254, N258, N259, N260, F256, and V257 are in `docs/edmonton-bridges/reference/`. Numbers are unique across every prefix. Bridge codes use 1–136. Stops are P137–P189, at-grade track is K190–K253, and the later codes are listed in `lrt.md` and `bridges.md`. The prompt for the next reference subagent is `docs/edmonton-bridges/reference-prompt.md`. Fill the braces and send one structure at a time. The named checkpoints Bridges, Quesnell, Bremner Cloverleaf, and Sherwood Park Cloverleaf come next. Do not place anything inside the `CYXD Airport Area` polygon; NAIT and Blatchford Gate are inside it.

## 2026-11-23 H27 / H28 built

H27 Calgary Trail / Gateway (19 decks, including the four CCE trellis structures and the curved 2 South flyover) and H28 Blackmud Creek arches (three open-spandrel arch structures) are modelled by `tools/site_h27.py`, `tools/site_h28.py` and the shared `tools/henday.py`. The package builds (exit 0). Neither has been seen in the sim. H28 is at 53.4348, -113.5134, 1.5 km west of where the brief placed it. Details and the sim checks are in `reference/H27-calgary-trail-gateway/HANDOFF-T2.md`.

## 2026-11-23 model checks

Corrected to the official Alberta bridge records (Structure-Export.csv, the same source as the 2026-11-23 search): R20 Beverly to file 77132 (commit `c3502ce`: five spans, 320.1 m, 19.2 m deck, piers moved) and R21 Clover Bar to file 02032 (commit `19e11a9`: the present bridge is the 2001 five-span girder, 320 m; the 1953 truss was removed). The R21 model was rebuilt; the R20 pier check was done in plan (`tools/overlay.py r20`: the deck lines up, the piers cannot be seen from above).

Checked against 2018 data and the sources, notes only: H52 (`3b86dda`, the layout matches the 2013 Alberta update; the name "Sherwood Park Cloverleaf" is kept as a project key but is partly wrong for the 2016 interchange), H39 (`8677f2f`, the NW leg opened 2011; nine of ten decks within 0.2 m of the 2018 DSM, EN3-14 is 0.45 m below its median), R6 (`d5f5866`, spans and piers match the 2008 PIEVC report; the model differs in continuous spans 3 and 4, girder-line count and cap type, all left as they are).

The palette: `bridgelib.py` now cuts the shared palette back to the 32 CYXD swatches (commit `d66dc9f`). The CYXD palette had grown to 41, so bridge swatches had moved and every bridge recoloured on each run. The generated palette is byte-identical to the committed `bridge_palette.png`. R20 and R21 had been built with the moved swatches, so their texture coordinates are corrected in the same commit.

Not committed: the working tree still holds the generator's output for the other bridge sites (positions and normals changed by the 2026-11-23 elevation refetch: F256 by 32 positions and 484 normals). It needs a decision before it is committed or discarded, and the build compiles it.

## 2026-11-23 reference data (no model changes)

`fetch-site-data.py` was fixed to fill the AB-Edmonton-1m nodata cells from NRCAN-Edmonton_2018-1m, and all 29 reference folders with a `geometry.json` were refetched. The 2018 DEM tifs and 2019 aerial jpgs are now on disk for every folder (gitignored). The gitignored data is about 290 MB of DEM and 116 MB of aerial. `analyze-elevation.py` was rerun. The only change to `ELEVATION.md` is added rows: H39, H52, R6, R20, R21, R22, W85 and Y79 now have deck heights. None of the figures for the existing 21 sites moved. The eight new sites are not in `PRIORITY.md` and have no models. `BLOCKERS.md` is updated to match. The git diff on `ELEVATION.md`, `data/elevation-summary.json` and the `ortho-2019.json` bounds files is not committed.

## Next

1. Open the sim and look: terrain clipping at piers, the datum, the High Level ridge (`MODEL-NOTES.md`, last section). Then fix what shows, by changing the site modules and rerunning `tools/gen_bridges.py`.
2. `build.bat bridges` (clear `gamingservicesui` and `gamelaunchhelper` first if it says NO BUILD), then `python -I scenery-edmonton-bridges/tools/make_layout.py` if `Packages/.../layout.json` is missing.
3. Next boxes in `PRIORITY.md` (its first unticked box is T127): section 2 open landmarks (T127, H30, H50, T135, T131), then section 3 Yellowhead exchanges, then section 4 R8 Groat with the ravine decks G116, G117, G119, T133 and Z125. Tier 2 sites R20, R21, R22, R6, Y79, H52, H39, H27 and H28 are modelled (ticked in `PRIORITY.md`); none has been seen in the sim.
4. Night lighting and transparent glass are not done for any model.

## 2026-10-19 changes (built, exit 0; not seen in the sim)

From the in-sim review. All of it is generated by `tools/gen_bridges.py`; the new modules are `tools/terrain.py` and `tools/approach.py`.

- **Tree exclusion**: every exclusion polygon now also sets `VegetationDensity` / `VegetationScale` 0, `ExclusionFlags` 7 and `ExcludeRocks` (attribute GUIDs from `PackageSources/airport-2fa2-belleview/sceneries/2FA2.xml`). Covers all bridges, the Valley Line R9/R14/P152 and the new K209 track.
- **Terrain polygons** (`terrain.py`): a flatten polygon at river level over the river run of each span (R6, R9-R15, R20-R22) and for the Groat Road Bridge (R8, no model); this should remove the ground "curtain" / strip under the decks (Groat, James MacDonald, Walterdale old-bridge land-fill). The river run is the stretch of the 2018 bare-earth profile within 1.5 m of its lowest sample. `grass` polygons (the CYXD "Grass over construction" material) cover the footprint over land to hide paths in the aerial under the decks. P152 is flattened to its platform level (station was buried). The 1913 Walterdale truss is cleared with an estimated strip 12-48 m west of the road way (`EXTRA` in `terrain.py`; no geometry survives, adjust from the sim).
- **Landable**: the model material carries `ASOBO_tags` Collision + Road, so every bridge is solid.
- **Lanes**: James MacDonald (3 lanes per one-way carriageway), Low Level (2 per span) and Walterdale (3) have dashed white lane lines, no yellow centre line. Dawson (two-way) keeps its yellow line.
- **Low Level**: both spans (truss and floor) in the sea-green swatch.
- **Approaches** (`approach.py`): N258 (Grierson), N259 (Rossdale / McDougall Hill), the N260 decks and Dawson (west end 150 m, east end 70 m) carry the road on from the deck end along the connecting OSM way (else straight on), moving at most 6% towards the LiDAR ground and ending in a 4:1 grass embankment.
- **Switched off**: B255 Hotel Macdonald (dropped from `ORDER` in `gen_bridges.py`, neither placed nor excluded) and the four B254 pyramids (`PYRAMIDS = False`; the greenhouses stay).
- **K209**: Valley Line track Muttart to Strathearn, two tracks, 1.6 km, ballast + rails + catenary, heights from `reference/P152-muttart/elevation/track-to-strathearn.json` (2018 LiDAR sampled along the OSM ways).
- **F256 funicular**: lifted up to 1.2 m at the top; the tree exclusion clears its footprint.

Not done: replacing the Walterdale construction in the aerials (no newer imagery fetched), and the cars that drive down the bank and across the river bed (the sim's traffic follows its own road layer on the terrain; no scenery setting known). If the flatten / grass polygons misbehave in the sim, remove the `terr` block in `gen_bridges.py` or the `kind` in `exclusions.polygon_xml`.
