# Tier 1 models: what was built, from what, and what is assumed

Written 2026-10-14. These are the first models in `scenery-edmonton-bridges` (version 0.2.0): the whole of `PRIORITY.md` section 1, the downtown valley. Built, compiled with `build.bat bridges` (exit 0, `_RPTErrors.xml` empty). **Not yet seen in the sim.** Every model was checked against the 2019 orthophoto (plan overlay) and a software preview, not against the sim.

## How it is made

- Generator: `scenery-edmonton-bridges/tools/gen_bridges.py [site ...] [--preview DIR]`. One module per site (`site_r10.py` ...) built on `bridgelib.py`, which reuses the CYXD generator's `Mesh` and palette (`airport-cyxd/tools/gen_buildings.py`) and appends 22 swatches (black/dark brown-grey steel, rust, sage green, concrete, asphalt, copper green, Dawson blue, glass and so on) after the 32 CYXD ones. Flat colour, no textures, one palette PNG (`modelLib/texture/bridge_palette.png`).
- Geometry comes from the OSM ways in each `reference/<site>/geometry.json`, the 2018 LiDAR figures (`MEASUREMENTS.md`, `data/measurements.json`, each `elevation/profiles.csv`) and the dimensions in each `NOTES.md`. Nothing is traced by eye except where this file says so.
- Frame: east / up / north metres around the model origin, mirrored once at the end (the sim places model +X to the west), heading 0. y = 0 is the **site datum**, placed at an absolute altitude (`altitudeIsAgl="FALSE"`, `snapToGround="FALSE"`). For the river bridges the datum is the 2018 LiDAR river surface at that reach. It is CGVD2013 and has **not** been checked against the sim (`BLOCKERS.md` section 4).
- A glTF holds at most 65,535 vertices here, so big bridges are split into chunks placed at the same point (the High Level is two).
- Placements are cached in `tools/placements.json` and written between the BEGIN/END markers of `PackageSources/Scenery/edmonton-bridges/edmonton-bridges.xml`.
- Checks: `tools/overlay.py <site> <reference folder> out.png [crop_m]` draws the plan over the 2019 orthophoto (the aerials are gitignored; `fetch-site-data.py` regenerates them). `--preview` renders three painter's-algorithm views per model; the preview mis-sorts big triangles, so a stray wedge in it is not a model fault.
- Build gotchas: `tools/make_layout.py` writes `Packages/<pkg>/layout.json` when `build.bat` closes `fspackagetool` before the tool has written it (it did, for this package). If `build.bat` reports "NO BUILD", kill `gamingservicesui` and `gamelaunchhelper` first (the leftover launch dialog from the previous run).

## Models

| Code | Model | Origin lat, lon | Datum alt m |
| --- | --- | --- | --- |
| R10 | `br_r10_high_level` (x2 chunks) | 53.529261, -113.511572 | 614.91 |
| R9 | `br_r9_menzies` | 53.529747, -113.512454 | 614.92 |
| R11 | `br_r11_walterdale` | 53.528383, -113.501700 | 614.21 |
| R15 | `br_r15_dawson` | 53.548739, -113.467197 | 612.83 |
| R13 | `br_r13_low_level` | 53.537959, -113.486669 | 613.74 |
| R12 | `br_r12_james_macdonald` | 53.535781, -113.488533 | 613.73 |
| R14 | `br_r14_tawatina` | 53.539450, -113.477140 | 613.26 |
| N258 | `br_n258_grierson` | 53.538564, -113.488789 | 613.74 |
| N259 | `br_n259_rossdale` | 53.537724, -113.493132 | 613.74 |
| N260 | `br_n260_scona_connors` | 53.536406, -113.484159 | 613.66 |
| F256 | `br_f256_funicular` | 53.539305, -113.487472 | 637.74 (the footbridge deck) |
| V257 | `br_v257_riverboat` | 53.539620, -113.481959 | 613.66 (water) |
| B255 | `br_b255_hotel_macdonald` | 53.540305, -113.489500 | 666.83 (ground) |
| P152 | `br_p152_muttart_stop` | 53.536424, -113.479491 | 621.94 (rail top) |
| B254 | `br_b254_muttart_conservatory` | 53.535216, -113.477286 | 627.90 (ground at the ring) |
| R20 | `br_r20_beverly` | 53.570941, -113.373183 | 610.00 |
| R21 | `br_r21_clover_bar` | 53.572051, -113.371974 | 610.00 |
| R22 | `br_r22_clover_bar_railway` | 53.573075, -113.370999 | 610.00 |
| R6 | `br_r6_quesnell` (x2 chunks) | 53.506262, -113.566653 | 618.30 |
| W85 | `br_w85_fox_drive` | 53.503135, -113.560877 | 618.30 |

## Sourced and assumed, per model

- **R10 High Level.** Sourced: all 28 span stations and the six tower and three low bent heights from the 1914 plate (`R10-high-level/NOTES.md`), scaled by 777.24/780.03 to the documented length; truss depth 15.24 m; rail deck base 47.55 m above the river (LiDAR 47.54); river piers 25 to 22 at the plate's head height (29.5 m above the river); axis fitted to the first two road nodes, 19 m past each end. The plan matches the aerial, and the river pier caps sit on the pier tips in the photo. Assumed: truss lines at plus or minus 6.0 m, chord and member sizes, pier plan (11 m across, nose both ends), the lower road 5.84 m below the rail deck, the rail deck ending after bent 9/8, catenary poles every 24 m. Colour is dark brown-grey (street frame). **The sim has the valley wall here as a solid ridge, so the terrain under the span needs lowering or cutting (William).**
- **R9 Menzies.** Sourced: both track ways (axis midway between them, curved), deck top 638.0 m (LiDAR 638.2 rail top), box 4.5 m deep, 530 m seven-span box, walkway way (294 m, so the three river spans are about 98 m each). Assumed: the other four box spans (55, 63, 63, 55), the slab spans at the abutments, pier stations, deck width 9.6 m, lollipop column size, no tunnel portals beyond a dark head wall.
- **R11 Walterdale.** Sourced: 206 m rib span, 230 m deck between joints at 14 and 246 m, 16 hangers per plane from 49 to 204 m, ribs lean about 13.5 degrees, rib crown 52.8 m and 40 m above the roadway, deck 14.7 m, east path from its own mapped way. Assumed: rib plane spacing (9.0 m at the deck, 0.9 m at the crown), parabolic rib shape, eight struts, deck widths, concrete leg sizes.
- **R15 Dawson.** Sourced: five spans 43.3 x 3, 76.2, 30.5 m, piers at 44.5, 87.9, 131.1 and 207.0 m (aerial), camelback and Pennsylvania span types, 8.1 m roadway, 2.65 m sidewalks, steel-blue paint. Assumed: truss depth (8.4, 12.4 and 6.4 m), pier size and height, deck 17.9 m above the river.
- **R13 Low Level.** Sourced: four 53 m spans, 7-panel Pratt, piers at 52.4, 105.3, 158.4 m (aerial), truss lines 7.925 m apart, outer sidewalk with lattice rail on each bridge, two colours (sage green east, rust-brown west). Assumed: truss depth 9 m, pier plan, deck 17.0 m, which colour is which span.
- **R12 James MacDonald.** Sourced: both carriageway ways, 11.1 m slabs, parapet with tan open rail, twin-arm lamps, haunched girders. **Assumed: five equal spans (pier stations are not published), girder depths 1.9 and 3.4 m, pier shapes.**
- **R14 Tawatina and the ramp.** Sourced: 100 / 110 / 50 m river spans (the pier stations match the two river cofferdams in the 2019 aerial), 3.5 m by 11 m box, two pylons 30 m above the deck with seven stays per side per leg at 17.4 to 26.2 degrees, path under the box, park spans about 40 m, ramp at 5.6 percent down to the platform level. **The levels are assumed**: the LiDAR predates the bridge. Rail top 18.6 m above the river (632.0 m) over the water, falling 2 percent to 98 Avenue, then 5.6 percent to 8.68 m (621.94 m at the stop). Chosen to meet the published clearances (navigation window, 5.5 m over 98 Avenue), not measured.
- **P152 Muttart stop.** Sourced: both platform rings (104 m long, 11.5 m apart), the line direction. Assumed: platform width 3.5 m, canopy (40 m glass roof, 3.3 m high), track spacing, level.
- **B254 Muttart Conservatory.** Sourced: pyramid apex positions and tops (DSM peaks), floor-to-apex heights 24 and 18 m, floor areas 660 and 381 m2 as square bases turned 45 degrees (matches the aerial), support-house ring. Assumed: square bases, berm, six gabled houses of 4.5 m eave. Glass is opaque.
- **B255 Hotel Macdonald.** Sourced: the 34-point outline, ground 666.83 m, tallest point 48.1 m, second 45.3 m. Assumed: eave 27 m, ridge 37 m, a simple hip roof, the lower turrets, window bands. No drawings; it is a massing model, not a faithful chateau.
- **F256 funicular and footbridge.** Sourced: the track way, 24.6 m drop, urban stair ways, footbridge way, spans (50 m main, 19 m lookout), timber-clad sides, one round pier, glass elevator shaft. Assumed: cabin position and size, canopy, stair width, pier and shaft heights.
- **V257 Edmonton Riverboat.** Sourced: 51.8 x 12.0 m, outline orientation, bow west, colours. Assumed: all deck heights.
- **N258, N259, N260.** Sourced: ways, raised runs and deck lines from the LiDAR, widths (N258 11.5 m, N259 13.0 m), parapet types. Assumed: girder depths 1.5 to 1.7 m, a centre column at N258, abutments only at N259, the N260 deck widths (several decks were merged in the LiDAR width).

- **R20 Beverly, R21 Clover Bar, R22 Clover Bar Railway (Tier 2, the Bridges checkpoint, 2026-10-15).** Helpers in `tools/t2lib.py`, LiDAR profiles from `tools/lidar_pil.py` (Pillow only; `profiles.csv` did not exist for these sites). One common datum, 610.00 m, for all three (the clips give 610.14, 610.07 and 609.84). Sourced: axes and deck footprints from the OSM ways and outlines, deck and rail levels from the 2018 LiDAR (R20 22.1 to 23.0 m, R21 22.5 to 25.3 m, R22 rail top 41.5 m above the datum), three lanes each, R22 single track and length 504 m, 29 m approach piers, blue steel railing (2011 photograph). Assumed: **every pier station and shape on the two highway decks** (R20 read from the 2015 photograph, R21 copied as fractions because the far deck is hidden behind R20), girder depths 3.0 and 2.8 m, which carriageway carries which name, R22 truss depth 14.5 m, panel counts, plate-girder depths, towers. R22 river piers and trestle bents are read from the aerial. The three structures are separate (plan gap about 100 m), so there is no seam to match beyond the shared datum. Details and sim checks: `reference/R20-beverly/`, `R21-clover-bar/`, `R22-clover-bar-railway/` `HANDOFF-T2.md`.
- **R6 Quesnell and W85 Fox Drive / Campbell Bridge (Tier 2, 2026-10-15).** `tools/site_r6.py`, `site_w85.py` (helpers `t2lib.py`, LiDAR `profiles.csv` written by `lidar_pil.py`). One datum, 618.30 m, for both (clips give 618.44 river and 618.09 creek). **R6 sourced:** plan from the OSM carriageways (axis midway between them, S to N), 315.7 m; deck level a quadratic through the 2018 first returns (18.3 to 20.7 m above the datum); six spans 50 / 54.9 x 3 / 53.3 + 46.6 m and five piers (PIEVC, IABSE 2008); two steel cap extensions per pier (ten, CISC Alberta 2011 page and the 2015 photographs); deck width -25.4 to +22.0 m, the median barrier, the 4.2 m east path and the Fox Drive merge lane read off the 2019 aerial. **R6 assumed:** the order of the spans (simple span at the south end), shaft spacing and size, 14 girder lines, haunch depths, cap depth, lane widths. **W85 sourced:** plan, 89.1 m, three lanes each way, south sidewalk and north path (OSM), deck level 9.5 to 10.1 m above the datum (LiDAR), overall width -16.0 to +17.5 m (aerial), railing and lamps (2012 photograph). **W85 assumed:** everything under the deck (three 29.7 m spans, two bents of six columns, 12 concrete girders 1.5 m deep) because no source or photograph shows the underside. The two bridges are 430 m apart and do not touch; the Fox Drive ramp between them is a ground road and is not modelled, so the only seam is the shared datum and palette. Details and sim checks: `reference/R6-quesnell/HANDOFF-T2.md`, `reference/W85-fox-drive/HANDOFF-T2.md`.

## Left for William, and what is still missing

- In the sim: whether the terrain clips piers and abutments; the datum offset (compare a model's datum with the sim's ground at the site); the High Level ridge; whether the models need LODs for far views (each has one LOD at minSize 0).
- No night lighting, no transparency, no textures on any of these. Glass is opaque. Lamps are plain poles.
- The two unbuilt-in-data structures (R14 verticals, the Muttart ramp grade) and every "assumed" item above are marked for replacement when drawings or photos with a scale turn up (`BLOCKERS.md` section 5).
- N258 to N260 and G116 and the other ravine decks that share a road with these are not part of Tier 1.
