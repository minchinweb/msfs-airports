# CYXD hangars: footprints, method and open questions (2026-10-12, updated 2026-10-21)

**Update 2026-10-21 (user corrections, see `street-view-review.md`):** Hangar 39 is the big pale-blue double hall (OSM 230718901, 107 x 90.5 m) next to Hangar 38, not OSM 230718900; that way holds Hangar 40 (Canadian Helicopters, white roof at its NW end). The "Hangar 9" photos are Hangar 8, so there is no Hangar 9 model or photo. Hangar 3 (81.6 x 25.7 m, traced from the 2014 imagery), the dark-blue hangar north of it (OSM 325272095) and Hangar 20 (the Esso building, traced) are now built. The table rows below are updated; the older reasoning notes further down are kept for the record.

`airport-cyxd/tools/hangars.py` builds Hangars 3 (+ tan annex), 4, 5, 6, 7, 8, 11, 14, 18, 20, 38, 39, 40 and the dark-blue hangar north of Hangar 3.
`gen_buildings.py` calls `hangars.place()`; run `python -I airport-cyxd/tools/gen_buildings.py` from the repo root to regenerate.

## Where the footprints come from
- **Google Earth could not be used** (no way to pull imagery from it here). Instead I used Esri World Imagery **Wayback 2014-02-20** tiles
  (release 10; summer imagery with every hangar still standing, zoom 17, about 0.7 m per pixel) as the ca. 2010-2014 aerial. A 2017 release (zoom 19,
  0.18 m per pixel) was used to check roof shapes where buildings still stood. The imagery is copyright Esri / Maxar and is used here as measuring
  reference only; only small annotated crops are kept in `footprints/`. Do not redistribute them.
- **OSM history**: the outlines OSM held in 2016 (Overpass `[date:"2016-01-01T00:00:00Z"]`) fit the 2014 imagery to a few metres, so each hangar is the minimum
  rotated rectangle of its 2016 OSM way (centre, long-axis bearing, size). Present-day OSM has only Hangar 14; the rest were removed after demolition.
- **Hangar 18** is in neither: it was traced by hand from the 2014 imagery (`footprints/hangar18-tower-frame.jpg`, 10 m grid, tower frame rotated to heading 48).
- Pictures: `footprints/east-line.jpg` (Hangars 4 to 11), `footprints/west-38-39.jpg`, `footprints/north-west-complex.jpg` (the large red-roofed complex,
  built 2026-10-21 as `north_main` with four neighbours, see STATUS.md).

## Table
| Hangar | OSM way (2016) | Centre lat, lon | Heading (front) | Front x depth (m) | Confidence in which building it is |
|---|---|---|---|---|---|
| 4 | 325273554 | 53.573457, -113.508430 | 0 (N) | 33.5 x 71.1 | medium (order along the line, 71 m long axis N-S) |
| 5 | 325270299 | 53.572793, -113.508364 | 270 (W) | 53.1 x 43.3 | medium-high (street number 11936 109 St fits its distance from Hangar 11) |
| 6 | 325267780 | 53.572135, -113.508405 | 270 | 41.9 x 46.2 | medium-high (white roof, NW of the NAIT parkade) |
| 7 | 325271251 | 53.571617, -113.508378 | 270 | 36.4 x 39.3 | medium-high (steel-blue roof, directly NW of the parkade) |
| 8 | 325268698 | 53.570358, -113.508293 | 270 | 66.3 x 52.9 | medium (the parkade stands just NE of it, as in the "8" photos) |
| 3 | traced (OSM 325273617 is a short trace) | 53.574710, -113.508533 | 90 (E, landside) | 81.6 x 25.7 | high (roundel in photos 38-45); length from the 2014 imagery roof, OSM says 76 m |
| - | 325272095 | 53.575629, -113.508404 | 180 (S) | 20.7 x 24.6 | the dark-blue gabled hangar at 5 109 St; no number visible; door end assumed to face south |
| 9 | none | - | - | - | **no photo, no footprint** (the old "Hangar 9" photos are Hangar 8) |
| 20 | not in OSM 2016 | 53.569788, -113.521578 | 228 (SW) | 45 x 45 upper tier + 8-10 m lower tier | the Esso building (user), measured on the 2014 imagery; 150 m SE of the old terminal |
| 11 | 325268748 | 53.569251, -113.508228 | 0 (N) | 86.3 x 64.0 | high (same spot as the 1944 USAAF "T3" box; barrel-vault shadow on its north end; annexes) |
| 14 | 230718920 | 53.565714, -113.517130 | 90 (E) | 100.0 x 90.8 | high (OSM "Hangar #14") |
| 18 | traced | 53.568740, -113.519699 | 48 (NE) | 60 x 43 (+ rear wing) | medium (position from the 2014 imagery, 78 m NW of the tower) |
| 38 | 230718902 | 53.573308, -113.529714 | 138 (SE) | 68.8 x 64.0 | medium (see below) |
| 39 | 230718901 | 53.574052, -113.528731 | 138 (SE) | 107.0 x 90.5 | medium-high: the pale-blue double hall, adjacent to the olive Hangar 38 in photo 26; Hangar 40 is at its NW (left) end in photo 28 |
| 40 | 230718900 (white NW part) | 53.575205, -113.529565 | 318 (NW, to the car park) | 38 x 25 | high (the user; roundel, brick office and white block in photos 29-31); the blue-grey gabled hall at the SE end of that OSM way is not built |

Old generic placements removed from the generator (`SKIP`): "Hangar 11", "Hangar 14", "USAAF hangar T1" (1944-photo box about 40 m north of Hangar 7) and
"USAAF hangar T2" (a box on Hangar 8's spot). The three USAAF boxes land on the 2014 buildings that became Hangars 7, 8 and 11.

## Reasoning that needs confirming
- **East line numbering.** From north to south the line is 4, 5, 6, 7 (Hangar 7 is directly NW of the NAIT parkade, as in the "RCMP hangar" photo), then 8, then 11.
  Between Hangar 7 and Hangar 8 (and between 8 and 11) there is only pavement and car parking in 2014, so **Hangar 9 and 10 are not on this line**; I could
  not find them. Hangar 9 is built (`cyxd_hangar9` in modelLib) but unplaced; set `HANGAR9_PLACEMENT = (lat, lon, heading)` in `hangars.py` once the spot is known.
- **38 vs 39.** The west group on 121 St has three hangars: a pale-blue gabled one at the SW (OSM 230718902), a big flat-roofed double hall in the middle (OSM 230718901,
  **not built**, 114 x 97 m) and a blue gabled one at the NW (OSM 230718900). Photos taken from the south-east show Hangar 38 on the **left (SW)** of Hangar 39, and the
  north side shot of 39 shows 38 at the right edge, so 38 = SW building and 39 = NW building. Swap the two rows in `HANGARS` if that is wrong. The fire address
  (12009 121 St NW) sits beside the NW building.
- **Door and gable directions** are mostly from the photos where visible: Hangar 11's arched end faces north (its shadow is arch-shaped), Hangar 14's museum front faces east
  (landside), 18 and 38/39 face their apron (NE and SE). For 5, 6, 7, 8 the gable end with the sliding doors is assumed to face west (the apron); for 4 it faces north.
  These could be wrong; check in the sim against the photos.
- **Hangar 6 colours**: white gable ends and green long sides (from "green and white"); the roundel is on the east end.
- Door counts, leaf widths, window grids and sign texts are estimates from photos. Lettering ("Alberta Aviation Museum", "Edmonton Flying Club", the 1956
  Northwest Industries sign) is only suggested with bars; there is no text rendering in the generator.

## What each model contains (see the docstrings for details)
- 4: pale-yellow ribbed gable end with arched door opening, "4" roundel, brick block east of the front, orange-panelled neighbour west.
- 5: tan ribbed hall with cream upper band, four white door leaves, two-storey bronze-glass office at the landside end, "5" roundel on the south wall.
- 6: white ends / green sides, three sliding leaves, low white annex with blue door, "6" on the east gable.
- 7: steel-blue hall, wide white two-tier door, "7" roundel beside it, slate-blue annex with awning.
- 8: STEEL hall with a full-width glazed door wall, taller end block with "8", low wing with roof clerestory.
- 11: white barrel vault (seven peach leaves), the 1950s three-storey clapboard annex with control cab, big roof sign and "11" roundel, fire escape, two-storey east wing.
- 14 (reworked 2026-10-21): the front is the SOUTH gable: two-storey white clapboard west wing, glazed and solid green door bays under a white band with the ALBERTA AVIATION MUSEUM lettering, teal awning, white pilaster, glazed lobby to the east corner. East wall (2014 aerial): tall upper windows over a low lean-to. Frontage displays (Bomarc, Norseman, memorial, Voodoo, black sign) are separate models, see `tools/display_aircraft.py`.
- 18: Flying Club building (glazed upper floor, balcony, fascia), green hangar with two white leaves, white wing with swoosh and "18", striped rear wing.
- 38: mustard ribbed hall, two door panels with cream trim, "38" roundel with canopy.
- 39: pale-blue main bay (tall leaves) plus lower bay, louvre panels, green guide posts, "39" on the side wall, two-storey rear wing.
