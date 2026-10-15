# G119 107 Avenue (Glenora Overpass) - model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 661.5 m (2,170 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface:** this clip holds no river reach, so no water figure applies. For a ravine or rail crossing use the ground heights above and below.
- **Main deck height** (`road_deck`, DSM median): 667.94 m. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** no usable night photo found (see `../../DATA-SOURCES.md`).

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

Ready with assumptions, as a plain-plan placeholder only. Plan geometry is good. Height, girder form, width and appearance are absent, and the folder has no photos. A recognisable model is blocked until the blocking requests below are answered.

## What the folder gives me

| Fact | Value | Source |
| --- | --- | --- |
| Name, file | Glenora Overpass, 107 Ave NW over Groat Road, Alberta B097 / 76536 | NOTES.md |
| Year built | 1967 | NOTES.md, SOURCES.md |
| Type | Grade separation, "GS 3", read (not confirmed) as 3 spans | NOTES.md, geometry.json |
| Structure | OSM outline `bridge:structure=beam` | geometry.json way 1510405388 |
| Rehab | Full rehab, done 2021 or planned 2022. Changes not described | NOTES.md (docs 126658, 119895, 126655) |
| South carriageway | 2 lanes, one-way eastbound, asphalt, 50 km/h, 75.8 m plan. Nodes (53.550914,-113.550336) to (53.550913,-113.54919) | geometry.json way 22928017 |
| North carriageway | 2 lanes, one-way westbound, asphalt, 50 km/h, 75.3 m plan. Nodes (53.551054,-113.549275) to (53.551054,-113.550414) | geometry.json way 158414123 |
| South footway | Concrete, 74.1 m, south of south carriageway, at lat 53.55083 | geometry.json way 114768445 |
| North footway | Concrete, 75.5 m, north of north carriageway, at lat 53.551134 | geometry.json way 159377842 |
| Outline ring | Corners (53.550816,-113.550262), (53.550815,-113.549148), (53.551144,-113.549339), (53.551144,-113.550453). Long edges 73.7 m, short edges 38.7 and 38.6 m | geometry.json way 1510405388 |
| Centreline end separation | 16.4 m west, 16.7 m east | NOTES.md, geometry.json |
| Under road | Groat Road NW, 2 lanes one-way each direction (two ways), 60 km/h, asphalt, no foot. Ways 611.2 m and 614.5 m | geometry.json ways 98093800, 157319879 |
| Centre | 53.5510, -113.5498 | NOTES.md, geometry.json |
| hgv | designated on both carriageways (live read) | NOTES.md |

Derived by me from geometry.json coordinates (not stated in the folder):
- Both carriageways run due east-west (constant latitude). Heading 090/270 true.
- Carriageway centreline spacing at mid-span is about 15.7 m (dlat 0.000141 deg). The 16.4 m and 16.7 m figures are end-node spacing, which includes the skew at the ends. Not a conflict, but they differ from the mid-span figure.
- Footway to footway spacing is about 33.8 m (dlat 0.000304 deg).
- The outline is a parallelogram. Its north edge sits about 12.6 m west of its south edge (dlon 0.000191 deg). That is a skew of about 19 degrees. It matches Groat Road crossing at an angle.
- Groat Road runs roughly NNW-SSE under the deck (nodes drift from lon -113.5509 at lat 53.5538 to lon -113.5476 at lat 53.5488).

No figures conflict inside the folder. Two soft tensions:
- 2021 completed vs 2022 planned rehab. Both kept in the notes.
- Outline short edges (38.7 m) vs footway spacing (33.8 m). Outline is the wider footprint, so it likely includes parapets or edge beams. Not stated.

## Build spec I would use from this alone

All dimensions below marked (assumed) are my placeholders. The folder does not give them.

Placement and orientation
- Origin at the deck centre, about 53.5510, -113.54976. Deck axis east-west, heading 090 true.
- Total length 73.7 m (outline long edge). Use this, not the 75.8 m carriageway length.
- Footprint: parallelogram from the four outline corners. Build the deck as a skewed slab so the end faces follow the outline's slanted short edges.
- Elevation: unknown. Do not copy the 4.8/4.9 m maxheight tags. Place on terrain with the underside at an assumed clearance (assumed, see requests).

Components
1. Deck slab, 73.7 m long, full outline width. Thickness (assumed).
2. Two carriageways, 2 lanes each, asphalt. Lane width (assumed). Medial gap between them: centreline spacing about 15.7 m minus carriageway widths.
3. Two concrete sidewalks outside the carriageways, one each side, at the mapped footway lines.
4. Parapets or railings along both outer edges. Type unknown. Use a plain solid barrier (assumed).
5. Beam girders under the deck (OSM says "beam"). Count and depth unknown (assumed).
6. Piers: "3 spans" implies 2 intermediate supports, plus abutments. Positions and shape unknown. Equal spans of about 24.6 m each (assumed, from 73.7 / 3).
7. Abutments at both ends.
8. Approach road stubs: 22.3 m, 21.4 m, 7.5 m, 5.1 m (geometry.json). The sim's road layer will probably supply these. Model them only if the deck needs a visible ramp.
9. Do not model Groat Road. It is the sim's road.

Materials and colours (no photo; all assumed)
- Deck and girders: weathered concrete grey.
- Asphalt: dark grey. Sidewalks: light grey concrete.
- Lane markings: white edge, yellow centre between the two carriageways' lanes is not needed since each carriageway is one-way. Use white dashed lane line.

LOD ideas
- LOD far (over 2 km): one extruded slab plus road texture, no piers.
- LOD mid: add parapets, sidewalks, girder underside.
- LOD near: piers, abutments, bearings, lamp posts.

## Gaps and conflicts, ranked by harm

1. No photograph at all. Colours, railing, girder form, pier shape, and the post-rehab look are all guesses. Biggest harm for close fly-bys.
2. Deck elevation and clearance over Groat Road unknown. The model's vertical placement and underpass shape are guesses. Groat Road drops into the ravine, so the grade under the deck is also unknown.
3. Deck width and lane/sidewalk widths unpublished. I can only use the OSM outline (about 36.6 m N-S) and footway spacing (about 33.8 m).
4. Span lengths and pier positions unknown. "3" is a read, not confirmed.
5. Rehab changes (2021/2022) not described. Railings or deck may differ from the 1967 form.
6. Deck thickness, girder depth, parapet height absent.
7. Terrain behaviour unknown. Whether the sim's default terrain or road mesh fills the underpass is not addressed.
8. Night lighting, lamp posts, signage not covered.

## Handoff requests

Blocking
1. Photos, at least: side elevation (looking from Groat Road), underside showing girders and piers, deck-level view showing railing and sidewalk, and one view along the deck. Open licence, or recorded as reference-only. Needed for colour and form.
2. Deck elevation above sea level, or clearance above Groat Road pavement. Any source: City drawings, survey, LiDAR or DEM profile at the crossing. Needed for placement.
3. Overall deck width (out to out), and carriageway, median and sidewalk widths. A Street View or aerial measurement is acceptable if flagged as measured.
4. Span lengths and pier or bent positions. A side photo with a known scale would do.

Nice-to-have
5. Girder type and count (steel plate or precast concrete) and depth.
6. Railing and parapet type and height.
7. What the 2021/2022 rehab replaced (deck, railing, bearings).
8. Terrain interaction: check how the sim's terrain and Groat Road look at the crossing. Say whether the ground rises into the underpass, so the model needs an excavated cut or whether a flat scenery polygon is needed.
9. Night lighting: lamp type, spacing, colour of light.
10. Road surface and collision: confirm the sim road layer already shows 107 Ave on the deck, so the model needs no drivable surface, or confirm it must carry its own road texture and collision.
11. Retaining walls or slopes at the abutments, and whether Groat Road passes through a cut with walls.
