# Bridges: remaining blocking items

Written 2026-10-14, revised after the LiDAR measurements, the street-photo readings and the merge of the other session's review (`CURSOR-HANDOFF.md`). Per-site detail, item by item, is in `reference/<site>/OPEN-QUESTIONS.md` (21 files); this file ranks what is left by who or what can clear it. Codes are those in `PRIORITY.md`. Companion files: `DATA-SOURCES.md`, `RIVER-LEVEL.md`, `ELEVATION.md`, `MEASUREMENTS.md`, `STREET-READINGS.md`.

## 1. Cleared by the data

- **Deck elevation ASL, water level, datum** (the number one blocker in every handoff and in the other session's review): answered at 2018 LiDAR accuracy for R8, R9, R10, R11, R12, R13, R15, G116, G117, G119, N258, N259, N260, F256 (terrain), B255, V257, and approximately for T133 and Z125 (the old structures). The High Level check matches the handoff's own figure (47.54 m against 47.55 m).
- **Clearance and ground under the road and ravine bridges:** G116, G119, N258, N259 and N260 carry a deck top 5.4 to 8.4 m above the road below, so about 4 to 5 m clear after the deck, matching the mapped `maxheight` tags. G117 is 14.4 m (median) and up to 23.6 m above its ravine; T133 8.0 m; Z125 9.1 m (old structure).
- **Overall deck widths** (plus or minus 1 m): N258 11.5 m, N259 13.0 m, G117 24 m, T133 18 m (matches the old 18.4 m), R8 19 m, R12 26 to 27 m. Not usable for trusses and arches (R9, R10, R11, R14, R15).
- **High Level (R10):** spans, river-pier heights and tower-bent heights read from the 1914 plate (`R10-high-level/NOTES.md`).
- **B255:** ground at the building edge 666.8 m, roof maximum 48.1 m above it (the published 47.7 m is probably to the tallest point). This replaces the earlier note that put the ground at 614 to 640 m.
- **B254:** apex positions of the four pyramids, from the DSM peaks (`P152-muttart/B254-conservatory/OPEN-QUESTIONS.md`).
- **Valley Line ramp:** William decided R14 owns it and runs it to the edge of the P152 stop. The join is the two ramp-way ends at 53.536207, -113.480002 and 53.536104, -113.4801 (`R14-tawatina/OPEN-QUESTIONS.md`).
- **Street-level detail** for G116, G117, G119, N258, N259, N260, T133, R12, R13, R15 (railing types, barriers, lamp type, lane layout): `STREET-READINGS.md`.

## 2. Data that does not exist yet (not fixable by more measuring)

The 2018 LiDAR and the 2019 aerial predate these structures, and the 2024 LiDAR mosaic repeats the 2018 values there.

| Site | What is missing |
| --- | --- |
| R14 Tawatinâ | Every vertical figure: deck elevations, pylon height, pier and span layout, the finished ramp grade. **The R14 deck row in `ELEVATION.md` is not a deck.** Needs drawings, an as-built, or photos with a scale. |
| P152 Muttart stop | Platform elevation (about 622 m, at grade, unverified), canopy plan, the storage track. |
| Z125 Wellington | Which girder was built; the finished deck, span and width. The data shows the old arch. No Mapillary frame within 250 m. |
| T133 Stony Plain | The new girders and the Valley Line West deck. The data shows the old bridge (which does agree with the published 18.4 m width and 6 m clearance). |
| F256 Funicular | Heights of the finished structure (terrain is answered). |

## 3. Can be measured from the files we hold, not done yet

| Item | Sites |
| --- | --- |
| Pier and abutment positions and individual span lengths, from the aerial | R8 (seven spans), R9, R12, R13 (also the 1900 bay length, 53 m or 51.8 m), R15, G119 (two column piers seen), T133, N258 (column count), R10 (check the plate against the aerial) |
| Truss and arch geometry: panel counts, truss depth, rib spacing, struts, hangers, delta piers | R11 (ribs, struts, hangers, delta piers), R13 (truss depth), R15 (truss depth, panel counts) |
| Roof structure: turret count, ridge against turret, outline against the Bing ring | B255 |
| McDougall Hill way node list (one OSM fetch) | N259 |
| Separate the individual decks where several sit at the same level (raised width merges them) | G116, N260, R8 |
| Review the street frames not yet read | R8, R9, R10, R11, R14, F256, P152, B254, B255, V257 |

## 4. Needs the sim (only William can clear these)

| Item | Sites |
| --- | --- |
| Does the sim's terrain or water clip the piers and abutments or the ravine cut? Test with a box at the lat/lon. | R8, R13, G116, G117, G119, N258, N260, T133, Z125 |
| High Level terrain cut: the sim has it as a solid ridge (answered by William), so lower or cut the terrain under the span. | R10 |
| Datum check: the LiDAR is CGVD2013; compare the sim's ground height at a bridge end with `elevation/README.md`. The CYXD runway gives a no-sim comparison. | all |
| P152 heading check (49 degrees true, within 2 degrees). | P152 |
| Texture overlap: no bridges are drawn in the sim, but some show as bridge-shaped marks in the aerial texture where they cross land. | all |

## 5. Needs photos, drawings or documents

None of these can come from LiDAR or road-level photos.

| Item | Sites |
| --- | --- |
| Girder, slab or truss depth and the underside (road-level frames cannot see it; G119 is the only site seen from below and only roughly) | G116, G117, G119, N258, N259, N260, T133, Z125, R8, R12, R13, R15, R9 |
| Pier height and the plan size of shafts | R9, R12, R13, R15 (R10 done) |
| Abutments only, or piers? | N259 |
| Plan tables: lane, shoulder, sidewalk and barrier widths as designed | G116, G117, G119, N260, R12, R11, R13, R15, Z125 |
| R14: pylon height, as-built pier count and spans, finished ramp | R14 |
| Which structures the Journal's two 1971 approach bridges are | R12 |
| B126 wording (Scona or Connors) | N260 |
| Platform width, canopy size | P152 |
| B254: berm height, glass-line sill, support-house pitch and count | B254 |
| Roof colour from a recent photo (copper, steel or grey, paint spec) | B255, R8, R15 |
| R9: the University tunnel mouth, the soffit-to-walkway distance, which part is the river spans | R9 |
| V257: freeboard and the deck line; a view from above | V257 |
| F256: the as-built length along the rails | F256 |

## 6. Night lighting still missing

Photos exist and are described for R10, R9, R11, R13, F256, P152, B255. **No usable night photo for R12, R14, R15, R8, G116, G117, G119, T133, Z125, N258, N259, N260, V257.** Street-level frames are daytime, so they show the lamp fixture (curved-arm cobra-head, grey) but not the colour. The R13 night frames are from 2006 and 2009. A lamp specification for the City street lights would settle the road bridges in one go.

## Suggested order

1. The section 3 measurements (pier positions, spans, truss geometry, roofs). Needs no one else.
2. The section 4 datum check, then the in-sim clipping tests.
3. Source documents for section 5, in the order of `PRIORITY.md`, starting with the structures whose heights are in no data (R14, then Z125 and T133).
