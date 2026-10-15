# Bridges: remaining blocking items

Written 2026-10-14, after the elevation, aerial and night data landed (`DATA-SOURCES.md`, `RIVER-LEVEL.md`, `ELEVATION.md`). Every `reference/<site>/MODEL-HANDOFF.md` now opens with an "Update 2026-10-14" block holding that site's ground, river and deck heights. This file ranks what still blocks modelling, by who or what can clear it. Codes are those in `PRIORITY.md`.

## 1. Cleared by the new data

All 21 handoffs asked for deck ASL, water ASL, datum or terrain heights. These are answered at the level the 2018 LiDAR allows (first-return deck tops, river surface, bare earth). The High Level check matches the handoff's own figure (47.54 m against 47.55 m). Nothing more to research for: R8, R9, R10, R11, R12, R13, R14, R15, G116, G117, G119, N258, N259, N260, T133, Z125, F256, P152, B254, B255, V257 on that one question.

## 2. Answerable from the files we have, but not yet extracted

Work, not research. Each is a measurement on the 0.2 m aerial or a DSM-minus-DTM subtraction.

| Item | Sites | How |
| --- | --- | --- |
| Clearance over the road, rail or ravine below | G116, G117, G119, N258, N259, N260, T133, Z125 | Deck DSM minus the DTM under the span. Deck DSM is already in each `elevation/README.md`. |
| Deck width, outline and approach shape | all | Measure on `aerial/ortho-2019.jpg` (bounds in the `.json`). |
| Pier and abutment positions, end points, span lengths | R8 (pier count, positions, true end points), R10 (4 river piers, 28-support layout), G116, G119, T133, R9, R12, R13, R15, N258 (pier columns), Z125 | Same. Piers show as shadows and caps in the High Level sample. |
| Roof ridge and tower heights | B255 (blocking item 2), B254 | DSM over the roof minus ground. Marked as an estimate. B255 reads 677.0 m at the outline against ground about 614 to 640 m (the hotel sits on the slope; take grade at 100 Street from the DTM). |
| Ramp grades and tie-in heights | R13, P152, R14, N259 | DTM profile along the road. |
| Track and ramp terrain profile at 25 m steps | P152 (blocking item 2) | DTM sampling along the line. |
| Plan view of the crossing (G116 item 4) | G116 | The aerial. |

## 3. Needs the sim (only William can clear these)

| Item | Sites |
| --- | --- |
| ~~Does MSFS 2024 already draw this bridge?~~ **Answered by William:** no bridge is drawn. Some show only as bridge-shaped features in the aerial texture where they cross land, so a model may need to hide or sit over that texture. The High Level was treated as a solid ridge of land joining the two banks, so R10 needs the terrain under the span lowered or cut away, or the span will sit on a ridge. | R10 (cut the ridge); the rest only the texture overlap |
| Does the sim's terrain or water clip the piers and abutments, or the ravine cut? Test with a box at the lat/lon. | R8, R13, G116, G117, G119, N258, N260, T133, Z125 (R10 is the ridge case above) |
| Datum check: the LiDAR is CGVD2013, the sim has its own geoid and mesh. Compare the sim's ground height at a bridge end with `elevation/README.md`. The CYXD runway gives a one-off comparison with no sim visit. | all |
| P152 heading check (49 deg true, within 2 deg) | P152 |
| ~~Who owns the Valley Line ramp?~~ **Decided by William:** the bridge (R14) owns it and runs it to the edge of the station (P152). R14 and P152 need the join point in lat/lon, and the DTM profile along it. | R14, P152 |

## 4. Needs photos, drawings or documents

None of these can come from LiDAR. Cheapest source first.

| Item | Sites |
| --- | --- |
| Side and underside photo of the span, openly licensed (girder count, depth, abutment and pier form) | G116 (also deck and rail photo), G117, G119, N258, N259, N260 (B065 itself, not the 98 Avenue spans), T133, Z125, R12 (close deck and Rossdale approach), R14 (north end and finished 98 Avenue crossing), R15 (underside) |
| Truss or girder depth, truss spacing, deck thickness | R12, R13, R15, R9, G117, T133, Z125, N259, N260 |
| Plan tables: lane, shoulder, sidewalk and barrier widths | G116, G117, G119, N260, R12, R11, R13, R15, Z125 (post-August 2024 girder width) |
| R10: the 1914 plate is already in `R10-high-level/photos/elevation-drawing-railway-age.png` and its labels are legible (checked 2026-10-14): piers 4 to 29, spans 129'-9" and 131'-9" north, 291'-10½" and 293'-3" and 291'-10½" main, 99'-10" then 97'-8" south spans with 49'-5" tower bents, tower 140'-0", grades 0.74% and 5.45%. Not settled: the short spans between piers 9 and 4 near Soullier Avenue. A sharper scan would only help there. | R10 (mostly answered) |
| R14 pylon survey, pier dimensions (only 8.5 m base known) | R14 |
| Platform width and shape, canopy size, ramp shape | P152 |
| B254 base side, berm height, support greenhouses | B254 |
| Roof colour from a recent daylight photo | B255 (roof), R8 (steel or grey, post-2020), R15 (paint spec; photos HDR) |
| R9 south portal photo; R9 spiral ramps | R9 |
| V257 aerial or high-angle view for the roof layout, and the 2026 wheelchair lift | V257 |

## 5. Night lighting still missing

Photos exist and are described for R10, R9, R11, R13, F256, P152, B255. **No usable night photo for R12, R14, R15, R8, G116, G117, G119, T133, Z125, N258, N259, N260, V257.** Dawson and Tawatinâ are the two most visible. The R13 frames are from 2006 and 2009, so they may not match present lighting. Colour temperatures are by eye from long exposures. A lamp specification for the City street lights would settle the road bridges in one go.

## Suggested order

1. Extract the section 2 measurements: R10, R9, R8, R13, R12, R11, R14, R15, G116, G117 first, matching `PRIORITY.md`. Most blockers disappear at once.
2. The datum check in section 3 (CYXD runway comparison needs no sim; the in-sim check needs William).
3. Photos for the ravine road bridges in section 4, which have the worst coverage: G116, G117, G119, N258, N259, N260, T133, Z125.
