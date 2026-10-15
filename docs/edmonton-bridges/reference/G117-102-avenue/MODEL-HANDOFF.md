# G117 102 Avenue at Groat Road — model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Reviewed using only the files in this folder (NOTES.md, SOURCES.md, geometry.json, three photos).

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 639.2 m (2,097 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 616.81 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Main deck height** (`road_deck`, DSM median): 662.50 m, 45.69 m above the river. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** no usable night photo found (see `../../DATA-SOURCES.md`).
- **Street-level photos:** 5 daytime Mapillary frames in `street/` (CC BY-SA, credits in `street/SOURCES.md`). They show railings, barriers, lamp posts, lane and sidewalk layout and approach shape from the road; not the underside or truss depth. Check them before treating those items below as open.
- **Open questions:** the other session's review (`CURSOR-HANDOFF.md`) re-checked against this data, item by item, in `OPEN-QUESTIONS.md`. Read it before the blocking items below.

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions.** Plan position, length, lane count and the structure type are known. Deck elevation, deck width, girder count and girder depth along the span are not. I can build a correct-looking plan view and a plausible girder-and-abutment model. The vertical position must be set from terrain or a guess.

## What the folder gives me

| Fact | Value | From |
| --- | --- | --- |
| Structure type | Single-span steel girder, integral concrete abutments. "Haunched" is EIA wording only. | NOTES.md, SOURCES.md (Structurae, EIA) |
| Total length | 113 m | NOTES.md, geometry.json dimensions (design paper) |
| Main steel span | 83 m | NOTES.md, geometry.json (design paper; Alberta row prints 83.0) |
| Abutment length | 15.6 m each | NOTES.md (design paper) |
| Span, other source | roughly 100 m | NOTES.md (ENR) |
| Girder depth at ends | roughly 4.2 m | NOTES.md (ENR) |
| Ravine depth | 22 m. This is ravine depth, not deck height. | NOTES.md |
| Bearings and piles | Sliding bearings at the front of each abutment. Hybrid steel and concrete piles at the back. | NOTES.md |
| Banks | Steep, vegetated, soil nails on the banks. | NOTES.md (EIA, ENR) |
| Road centreline | Way 25601853, 111.9 m, west node (53.543012, -113.541177), east node (53.543009, -113.539485). | geometry.json |
| Road | 4 lanes, asphalt, 50 km/h, width tag 13.6 (unconfirmed), layer 1. | geometry.json |
| North footway | Way 114503872, 120.9 m, (53.543132, -113.541154) to (53.543119, -113.539326). | geometry.json |
| South footway | Way 114503875, 112.1 m, three nodes, lat about 53.542932 to 53.542924. | geometry.json |
| Protected bike lane | Way 1230468990, 111.7 m, (53.543099, -113.541183) to (53.543096, -113.539494). Between the road and the north footway. | geometry.json |
| Approaches | 12.9 m and 10.7 m mapped stubs, width tags 15 and 14. | geometry.json |
| Groat Road below | Two one-way carriageways, 2 lanes each. Ways 37749243 and 484577623. | geometry.json |
| Opened | 15 July 2016. Replaced a 1910 trestle, demolished July 2014. | NOTES.md |
| Photos | Deck, barrier, railing, signal gantry, abutment end wall. 9 Sept 2016. | photos/ |

Figures that conflict or nearly conflict inside the folder:

- Length: 113 m, 111.9 m centreline, roughly 100 m (ENR). The folder says these are different extents. 83 m plus 2 x 15.6 m is 114.2 m, close to 113 m. NOTES.md says they were deliberately not added.
- Road width: tag 13.6 m on the deck, 14 and 15 on the approach stubs. None confirmed.
- Footway lengths: 120.9 m (north) against 111.9 m (road). The north footway runs past the road ends, about 1.5 m west and 10.5 m east (my calculation from node longitudes).
- Girder depth 4.2 m is "at the ends" only. Nothing for midspan.

## Build spec I would use from this alone

Derived from geometry.json (my calculations, flat-earth at lat 53.543, 66,180 m per degree of longitude, 111,200 m per degree of latitude):

- **Heading.** The deck runs west to east. Bearing about 90 degrees (the east node is 0.3 m south of the west node).
- **Plan length.** 112 m along the road centreline. Set the structure ends at the two road nodes.
- **Deck midpoint.** About (53.54301, -113.54033). This is close to the project centre (53.5430, -113.5403).
- **Offsets from road centreline.** Bike lane line about 9.7 m north. North footway line about 13.3 m north. South footway line about 8.9 m south. These are mapped line positions, not surveyed edges.
- **Groat Road underneath.** Runs about north-south, nearly square to the deck (skew near 0). The two carriageways cross the deck line at about lon -113.54040 and -113.54028, about 8 m apart. The main span is centred on this crossing.

Components:

1. **Deck slab.** 112 m long. Width: I would use 13.6 m of road plus the barrier, bike lane and the two footways. By the offsets this gives about 22 m out to out centreline of the footways. Treat as an assumption.
2. **Road surface.** Dark asphalt, white lane lines, double yellow centre (deck-signals.jpg). Four lanes. The photos show a raised concrete median island at the signal.
3. **Protected bike lane.** North side, asphalt, separated by a continuous low concrete barrier (deck-downtown.jpg). White raised kerb strip on the traffic side.
4. **Sidewalks.** Both sides. Light grey concrete with a broom finish (railing-sidewalk.jpg). Concrete kerb between sidewalk and road on the south side (deck-signals.jpg).
5. **Railing.** Galvanised steel. Two or three horizontal round rails, tapering angled posts, thin vertical infill bars. Mounted on baseplates at the deck edge (railing-sidewalk.jpg).
6. **Concrete barrier.** Plain pale grey, jersey-style. Segmented joints, about waist height (deck-downtown.jpg).
7. **End walls and abutments.** Pale grey concrete. The end wall has a large circular recessed opening filled with a dark rusty steel grid (railing-sidewalk.jpg). Abutments 15.6 m long each (design paper).
8. **Girders.** Steel, 83 m main span. Depth 4.2 m at the ends (ENR), shallower at midspan (haunched). Midspan depth and girder count unknown. I would place 4 to 5 girders as a placeholder.
9. **Light poles.** Tall curved single-arm poles, galvanised or light grey. Spaced along both sides (deck-downtown.jpg). Spacing not measured.
10. **Signal mast arm.** Galvanised horizontal arm with three signal heads over the lanes, plus a separate bicycle signal head (deck-signals.jpg). It is at the east end in the photo; the folder does not say which end.
11. **Signs.** "Signals Stop Line" sign on a pole in the median. Black-and-yellow hazard marker on a post (deck-signals.jpg).

Colours read from the photos: concrete light grey; steel galvanised silver-grey; asphalt dark grey; sidewalk mid-light grey; end-wall grid rust brown; lane lines white and yellow. The girder colour is not seen. I would use a galvanised or weathering-steel grey and flag it.

Elevation and placement: deck elevation is not in the folder. I would put the deck at a fixed height above the Groat Road centreline sampled from the sim terrain at the crossing, and choose that height as an assumption. The 22 m ravine depth is an upper bound for the drop to the road. Do not use it as the height.

LOD ideas:

- **Far (above 1,500 ft).** Deck box, abutment boxes, a simplified girder underside, a road texture with lane lines. No railings in geometry. Draw the railing as a texture strip.
- **Mid.** Add barrier, railing as an alpha-textured plane, light poles, and the mast arm.
- **Near.** Full railing posts, circular end-wall opening, girder haunch profile.

## Gaps and conflicts, ranked by harm to the model

1. **No deck elevation or clearance over Groat Road.** The bridge could float or sit in the ground. Blocking for vertical placement.
2. **No girder count and no girder depth profile.** The underside is the main thing a flyer sees. Only the end depth (4.2 m) is known.
3. **No published deck width and no lane, sidewalk or bike-lane widths.** I only have offsets between mapped lines (and an unconfirmed 13.6 m tag).
4. **No side elevation photo.** None of the three photos show the girders, abutments from the side, the haunch, or the ravine. Silhouette is a guess.
5. **Length ambiguity.** 111.9, 112.1, 113, roughly 100 and 83 plus 2 x 15.6 are all near each other. The 113 m is not matched to a start and end.
6. **No crossfall or longitudinal grade.** I would build flat.
7. **Terrain interaction not described.** I cannot say whether the sim's terrain will cover the ravine and approaches or leave a gap.
8. **No girder colour or finish.** The only steel seen is the railing.
9. **No light-pole spacing or signal-mast position.** Night lighting unknown.

## Handoff requests

| # | Request | Status |
| --- | --- | --- |
| 1 | Deck elevation above sea level at both abutments and at midspan, and clearance over the Groat Road surface. Source: as-built drawing, city LiDAR, or a surveyed sheet. Also the Groat Road surface elevation at the crossing. | Blocking |
| 2 | One or more side photos of the full bridge from the Groat Road ravine or from the LRT/valley side, showing girders, haunch, and both abutments. Open licence if possible. | Blocking |
| 3 | Girder count and cross-section: girder spacing, midspan depth, deck overhang. A section drawing or one underside photo. | Blocking for a close fly-by, nice-to-have for 1,000 ft or higher |
| 4 | Measured deck width and lane, bike-lane, barrier and sidewalk widths. Confirm the 13.6 m road tag. | Blocking for correct cross-section, nice-to-have at altitude |
| 5 | Abutment and end-wall photo from below or from the side, showing the slope and the circular opening, and soil-nailed banks. | Nice-to-have |
| 6 | Girder paint or steel finish (colour). A photo from below. | Nice-to-have |
| 7 | Terrain question for the model builder: does the sim terrain sit in the ravine at the correct depth, and will it clip the abutments or the road below? Test with the project's elevation data at the crossing. Also decide whether Groat Road below needs its own road mesh. | Blocking before placement |
| 8 | Whether the deck needs collision and a drivable or walkable surface. Check how the sim treats road and bridge layers in this project (the bridges project convention). | Nice-to-have |
| 9 | Night lighting: pole count, spacing, lamp colour (the photos show curved arm poles but no night view). | Nice-to-have |
| 10 | Which end the signal mast arm is at, and its height. The deck-signals photo shows it but no direction. | Nice-to-have |
| 11 | Check whether the 113 m total is end-of-abutment to end-of-abutment, and where the 111.9 m mapped road ends fall relative to the abutments. | Nice-to-have |
