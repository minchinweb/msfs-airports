# R10 High Level Bridge: model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Reviewed from this folder only (NOTES.md, SOURCES.md, geometry.json, 11 photos). No other source used.

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 614.8 m (2,017 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 614.91 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Main deck height** (`upper_deck_streetcar`, DSM median): 662.45 m, 47.54 m above the river. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** 8 photos in `night/` with a lighting description in `night/SOURCES.md`.

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions.** The overall envelope is well sourced: length, deck width, deck gap, truss depth, span pattern, deck order and plan line. Three things are not in the folder and I would have to assume them: absolute deck elevation (ASL), river pier height, and the south tower/approach geometry. None stops a first model. The first two decide whether it sits right in the terrain.

## What the folder gives me

Source tags: N = NOTES.md, S = SOURCES.md, G = geometry.json, P = photo.

| Fact | Value | Source |
| --- | --- | --- |
| Structural length | 777.24 m (2,550 ft) | N, G dimensions |
| Spans | 28 total; 18 itemized | N, G |
| Centre river spans | 3 Pratt, 87.78 m (288 ft) each | N, G |
| South approach | 7 Pratt at 29.26 m (96 ft); 6 tower spans at 14.33 m (47 ft) on steel legs | N, G |
| North approach | 2 Warren at 39.62 m (130 ft) | N, G |
| Unitemized spans | 10, no lengths | N |
| Truss chord depth | 50 ft (15.24 m), main spans | N, P elevation-drawing-railway-age.png |
| Deck width | 11.89 m (39 ft), each deck | N, G |
| Deck gap | 6.10 m (20 ft); road top is 19 ft 2 in below base of rail | N, G |
| Rail-deck base height | 47.55 m (156 ft) above mean river level | N, G |
| Road | 2 lanes, one-way southbound, asphalt, sidewalk each side | N, G |
| Original road split | 23 ft roadway + 2 x 8 ft sidewalks = 39 ft | N |
| Current path widths (2016) | west 2.8 m, east 2.3 m | N (secondary, unretrieved) |
| Posted clearance | 3.2 m | N, G |
| Upper deck | one centre streetcar track now; originally CPR centre + a streetcar each side | N, P upper-deck-tracks-historical.jpg |
| River piers | 4, reinforced concrete | N |
| South tower height | 140 ft (ground to deck, plate reading) | N, P plate |
| Plate support numbering | 4 (south) to 29 (north); river piers are 22-25 | P plate |
| Plan lines (lat, lon) | Lower road: N end 53.532398,-113.509743 to S end 53.52608,-113.513026. Upper tram: 53.532768,-113.509572 to 53.526197,-113.513244 (+ stub to 53.526029,-113.51328) | G |
| Centre | 53.531, -113.511 | N, G |
| Slope | main spans level; south approach spans 0.74%; south street ramp 5.45%; south end ~10.34 ft above north end | N, P plate |

Derived by me from G (flat-earth maths, cos(lat) = 0.597):

- Lower-road N-end to S-end chord is about 736 m. Bearing N to S is about 197 deg true (about 17 deg west of south).
- The bridge runs NNE to SSW. Southbound traffic heads about 197 deg.
- Upper-deck line is about 20 to 30 m west of the road line (G says "sits west of the road centreline"). Offset not given in metres. That is odd for a deck that is meant to sit directly above the road.

Conflicts inside the folder:

- **Length.** 2,550 ft / 777.24 m (used) vs 2,478 ft / 755 m vs 2,800 ft (N). The OSM chord (about 736 m) fits neither. This is fine: the ways do not cover the full structure.
- **River span.** 3 x 288 ft = 864 ft. The plate reads 291'10.5" + 293'3" + 291'10.5" = 876.9 ft. N says rounding or bearings vs piers. Unreconciled.
- **Itemized length.** 18 spans sum to 633.38 m, 143.86 m short of 777.24 m. The 10 unitemized spans must fill this, and nothing says how.
- **Upper-deck height.** 156 ft (47.55 m, used) vs 152, 157, 160 ft, 46 m, 48 m, 49 m. Datums unknown.
- **Pier height.** about 125 ft vs "nearly 100 ft" vs 138 ft (1910 plan). 153.2 ft is crown-of-road above July 1906 low water on the plate.
- **Pier count.** 4 river + 62 small (N) vs "32 piers and pedestals" (N). The plate shows far fewer than 66 supports (numbers 4 to 29, so 26 at most).
- **Width.** 39 ft (deck) vs 43 ft (overall) vs 13 m. Use 11.89 m per deck. Overall width is unresolved.
- **Slope.** 0.74% and 10.34 ft are not the same measurement. Check: 0.74% over the 7 x 96 + 6 x 47 ft south spans (about 954 ft) is about 7 ft. This is my arithmetic, not a source figure.
- **Colour.** N says painted black. Photos show black in the winter shot, the north-end shot, the Menzies view and the oblique. Rust brown shows in elevation-with-streetcar.jpg (partly sun-lit) and the panorama. I read it as black steel with rust, not two colours. Unconfirmed.
- **Photo vs label.** north-portal-both-decks.jpg is labelled as a portal looking south. It shows a curving road with red guard rail, a bus, an SUV and a streetcar above on a plate-girder crossing. It is not a clean straight-on portal. The north-approach photos are mixed dates (1914, 1950s, 2000s).

## Build spec I would use from this alone

Everything not tagged "sourced" is my assumption.

**Placement**

- Model origin at 53.531, -113.511.
- Build along a straight axis at about 197 deg true (S end at 53.52608,-113.513026).
- Put structural length 777.24 m centred on the lower-road chord. This puts the ends about 20 m past each OSM road end.
- Hand-place the 4 river piers. Plate order, N to S: 22, 23, 24, 25 (25 on the north bank side per the plate, which reads left = north). Their lateral positions are not in the folder. I would scale from the plate span figures.
- Deck: upper-deck base at 47.55 m above mean water. Lower deck top = 47.55 - 5.84 m (19 ft 2 in) = 41.71 m above mean water. Water ASL is missing, so a terrain-referenced datum is needed. Placeholder: set deck height relative to the sim's water surface at the river.

**Components (sourced dims unless marked)**

1. Main river spans x3: Pratt/Baltimore deck truss, 87.78 m each (or plate 88.9 / 89.4 m), chord depth 15.24 m. Subdivided panels per the plate. Photos (underside, elevation-with-streetcar) show heavy diagonal web members and a rectangular upper chord.
2. Lower deck: 11.89 m wide, road about 7 m (23 ft; present lane width not given) plus sidewalks on brackets outside the truss line. Photo shows two lanes, a dashed lane line, red-painted barrier rails with black railings on top, snow berm at kerb.
3. Upper deck: 11.89 m wide, open, one central track with timber ties on steel plate-girder deck. Photos show a deck edge with riveted plate girders. No walls.
4. North approach: 2 Warren truss spans, 39.62 m (plate: 129'9", 131'9").
5. South approach: 7 Pratt spans (29.26 m) and 6 tower spans (14.33 m) on X-braced steel towers up to 140 ft (42.7 m). Plate shows tower bents, 2 steel legs plus cross bracing, concrete footings. Tower leg lengths vary with terrain.
6. River piers x4: tapered concrete shaft, flared base, pointed ice-breaker nose upstream face (visible in underside-pier-from-menzies.jpg). Footing 20 ft square at base (1910 proposal, not as-built). Height assumption: 125 ft (38 m) with the river piers' top at truss bearing.
7. Small concrete piers/pedestals: count unresolved. I would place the 26-ish supports from the plate.
8. Rail furniture: overhead catenary poles at regular spacing along the upper deck (elevation photos show about every 15 to 20 m, my reading), simple wire. Streetcar car optional (green with white stripe, number 247, in north-portal photo).
9. Lower-deck lighting: fluorescent strips under the upper deck (winter photo) plus overhead wires. Night spec not given.
10. Approach roads (not tagged bridge): N east branch 97.2 m, N west branch 109.4 m, S 146.4 m bending east. Plan lines in G. Use as ground-level road ribbons only.
11. Streetcar approaches: N 136.6 m, S 25.3 m (G).

**Materials and colours (read from photos)**

- Truss and steel: near black with rust-brown wash; matte, riveted gusset plates.
- Piers and footings: light warm grey concrete, vertical board-form marks.
- Lower deck: dark grey asphalt; sidewalks pale concrete.
- Rails: red barrier rails (low, on the road side), black pipe handrails above, yellow/black hazard stripes on columns (north-portal photo).
- Upper deck: dark timber ties and ballast-black steel.

**LOD**

- LOD0 (2,000 to 3,500 ft AGL): extruded truss silhouette with texture-faked diagonals, flat deck strips, concrete pier blocks.
- LOD1: modelled chords, verticals and diagonals for the 3 river spans. Tower bents as boxes with X-bracing.
- LOD2 (close fly-by): handrails, catenary poles, lights, gusset plates, pier nose. Rivets in normal map only.

## Gaps and conflicts, ranked by damage to the model

1. **No absolute elevation.** Deck ASL, water ASL and datum are all null. A model placed wrong floats or sinks. Blocking.
2. **No terrain cross-section.** I do not know the valley profile, the river centreline, or where the 4 river piers sit laterally. Pier and tower leg heights depend on it. Blocking for pier/tower foot placement.
3. **River pier height disagrees** (100 / 125 / 138 ft) and no schedule. Affects the most visible solid elements.
4. **South tower geometry.** Only 140 ft for one tower on the plate. No bent spacing, leg batter or plan footprint. The 10 unitemized spans leave the south approach layout uncertain.
5. **Truss detail.** Panel length and member sizes are not given for the river spans. The plate is small (447 px tall original), so I would scale by eye.
6. **Upper vs lower deck plan offset.** G puts the tram line west of the road line by an unquantified amount. Cross-section of how the two decks stack is only from photos.
7. **Ground clearance and water clipping.** Nothing on whether the sim's water or terrain mesh will intersect pier bases.
8. **Lane width, crossfall, deck thickness, sidewalk bracket detail.** Missing.
9. **Overall width** 43 ft vs 39 ft unresolved.
10. **Approaches.** 1914 and 1910 grades predate the 1931 and 1971 rebuilds. Present gradients not given.
11. **Night lighting.** Not covered beyond one photo of under-deck strips.
12. **Colour.** Black vs rust, no sampled swatches.

## Handoff requests

Each is something a later researcher can act on.

1. **Blocking.** Deck ASL and datum. Find a survey, LiDAR/DEM value (for example Alberta/City of Edmonton open data) or a City drawing giving top of road deck and river surface ASL.
2. **Blocking.** North Saskatchewan water surface elevation at the bridge in the sim (or the DEM-implied value), so that the 47.55 m figure can be applied in the sim's own terms.
3. **Blocking.** Plan positions of the 4 river piers and the 28-support layout: lat/lon or chainage along the bridge from the north end. Source: City bridge inventory, plate in higher resolution (HathiTrust seq. 1096), or a clear Google/Bing top-down view.
4. **Blocking.** Whether MSFS 2024 terrain or water will clip pier bases. Test with a box at the pier lat/lon in the sim, then note ground ASL at each foot.
5. **Blocking.** Full-resolution 1914 plate (or the OCR of its labels) so the 10 unitemized spans, tower heights and pier numbering can be read.
6. **Nice-to-have.** One head-on elevation per bridge type: north Warren spans, south tower spans, and a close view of a tower bent (leg spacing, bracing).
7. **Nice-to-have.** Cross-section drawing or photo straight along the bridge axis showing the two decks and the truss line, with road width, sidewalk bracket and track centre offset.
8. **Nice-to-have.** Photo set of the river pier: front, side, and the base nose and footing, plus a scale reference.
9. **Nice-to-have.** Colour reference: a daylight photo with a grey card or at least a mid-day, unfiltered view of the steel; confirm paint (black vs weathered brown) and its current repaint date.
10. **Nice-to-have.** Night photos: street lighting spacing, under-deck lighting, any bridge-wide architectural lighting. Mack Male's frames are listed in S as not downloaded.
11. **Nice-to-have.** Collision and road-surface needs: confirm whether the sim needs a drivable road surface, or whether this is a visual-only model with no collision. Document the project's decision.
12. **Nice-to-have.** Catenary and pole spacing and height, and whether the wires should be modelled.
13. **Nice-to-have.** Present lane width, crossfall, rail-deck width beside the car (all listed as missing in N).
14. **Nice-to-have.** Current approach gradients and the points where each approach meets natural grade (N says present values not published). Needed only if the approach roads are in scope.
