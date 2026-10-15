# B255 Fairmont Hotel Macdonald - model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 667.1 m (2,189 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 613.74 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** 1 photos in `night/` with a lighting description in `night/SOURCES.md`.
- **Street-level photos:** 5 daytime Mapillary frames in `street/` (CC BY-SA, credits in `street/SOURCES.md`). They show railings, barriers, lamp posts, lane and sidewalk layout and approach shape from the road; not the underside or truss depth. Check them before treating those items below as open.
- **Open questions:** the other session's review (`CURSOR-HANDOFF.md`) re-checked against this data, item by item, in `OPEN-QUESTIONS.md`. Read it before the blocking items below.

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions.** The footprint ring, the style, the materials and good photos of three sides are enough for a 1,000-3,500 ft silhouette. Every height is missing or conflicting, and there is no ground elevation. I must pick a ridge height and a grade myself. Close fly-bys would need more.

## What the folder gives me

| Fact | Source |
| --- | --- |
| Footprint ring, 34 corners, closed, WGS84 [lat, lon]. Traced from Bing, not surveyed. | geometry.json `ways[0].nodes`, way 198826612 |
| Centre 53.540305, -113.489500 (mean of corners). | geometry.json `centre`, NOTES.md Plan |
| Mapped perimeter 247.2 m. Node box 71.4 m N-S by 70.3 m E-W. Edge lengths listed. | geometry.json, NOTES.md Plan |
| Style: Canadian chateau (designation) or neo-gothic (Emporis). L-shaped, diagonal recessed entrance, turret. | NOTES.md Massing; geometry.json `dimensions` |
| Seven-storey Indiana limestone facades, steep dormered roofs, high chimneys, projecting towers, turret roof, finials. | NOTES.md Massing, SOURCES.md (City statement, HistoricPlaces.ca) |
| Roof structure: high gable, hip dormers. Copper roofing. | NOTES.md Roof; SOURCES.md (HS 5265) |
| Entrance: five arches, four pillars, two pilasters, on the street face (100 St side). | NOTES.md Entrance face; roof-and-turrets.jpg |
| Rear facades face the river valley. Hotel fronts 100 Street and McDougall Hill. | NOTES.md Wings |
| Funicular upper node 69.2 m from centre at bearing 187.6 deg (south). | geometry.json `map_distances` |
| Low Level north nodes 228.2 m (156.0 deg) and 234.6 m (157.9 deg) from centre. | geometry.json `map_distances` |
| 1953 wing demolished 1986. It is not part of the present building. | NOTES.md, SOURCES.md |
| Colours seen in photos: see the build spec. | photos |

**Conflicts inside the folder**
- Storeys: 7 (designation, 4 sources), 10 (survey, original), 11 (Emporis, Wikipedia), 1 (OSM tag, unusable).
- Height: 47.7 m / 156 ft (Wikipedia, cites Emporis), but Emporis itself says 155.51 ft architectural and 167.49 ft tip. OSM `height=47`, unit not stated. The two sources agree within about 0.2 m if 155.51 ft is read as 47.4 m, but the notes say not to convert. I do not.
- Facade: Indiana limestone (designation) vs sandstone, brown (Emporis, OSM, Wikidata). OSM colour `#eee1ce`.
- Roof colour: green in roof-and-turrets.jpg, dark grey/black in river-face.jpg, from-river.jpg and skyline-from-south.jpg, "blackened with age" in the survey, OSM `#808000`.
- Plan: "L-shaped" vs survey "irregular". The ring is irregular.
- Hotel photos show an apparent 8-10 window rows. That matches 7 stone storeys plus roof/attic levels. It is my reading, not a published count.

## Build spec I would use from this alone

**Placement**
- Import the 34 nodes. Convert to local metres about the centre. Extrude the ring.
- From the edge lengths, the main edges run nearly N-S and E-W, so there is no large rotation. The ring itself fixes orientation. Do not rotate the model.
- The ring has a 3.1 to 2.0 m run of short edges on the west-south-west side (nodes 7 to 13). That is the curved or diagonal corner. It matches the rounded bay at the lower-left of from-river.jpg.
- Origin at the centre point. Heading 0. Model in true N-up coordinates.
- Elevation: not in the folder. I will have to take the sim's terrain height at the centre, then check by eye. (Gap 1.)

**Components**
1. Main mass: ring extrusion, stone walls. Height is an assumption (see gaps). Candidate range from the folder: 155.51 ft (architectural) and 167.49 ft (tip), or 47.7 m. I would use the Emporis pair for eave-to-ridge and tip only as a labelled assumption, not a fact.
2. Steep hipped and gabled roof on each wing, with hip dormers along the eaves. Dormers: no count published. I would read the count from the photos and keep it per-wing, not exact.
3. Conical turrets. From the photos: one at the west (river-side left) corner of the river face, one at the street corner near the entrance (roof-and-turrets.jpg), one smaller central one, and a gabled end bay on the east. Each has a finial or cross. Positions are visual only.
4. Gabled projecting central bay on the street face, with a stone balcony on corbels and a stepped facade. Visible in roof-and-turrets.jpg.
5. Chimneys, tall and square, stone. At least three visible in from-river.jpg.
6. Base arcade: a row of round arches along the base of the river face with a balustraded terrace above (river-face.jpg, from-river.jpg).
7. Entrance portico on the street face, balustraded top, arches (roof-and-turrets.jpg).
8. Windows: regular grid of small white-framed windows. Use a texture, not geometry, at long range.

**Materials and colours (from photos)**
- Wall stone: pale buff to pinkish tan, around the OSM `#eee1ce` in shade-free light. It reads darker in shade and warm gold at dusk. Use a sandstone/limestone base colour, with the roof dark.
- Roof: dark grey, nearly black slate-like in 4 of 5 photos. Green copper patina on turret cones and some slopes in roof-and-turrets.jpg. Plan: dark grey main roofs, green turret cones. Marked as assumption.
- Window frames white. Window glass dark.
- Night: wall-lit facade in warm orange (river-face.jpg). Windows lit warm. A few dormers lit.

**LOD ideas**
- LOD0 (over 2 nm): extruded ring, stepped roof block, four cone turrets. One material.
- LOD1 (1,000 to 3,500 ft): add dormers, gables, chimneys, window texture.
- LOD2 (fly-by): add arcade, portico, balustrades, corbelled balcony, finials.
- Collision: none needed unless the sim places it as a building users can hit. Treat as a normal building collision mesh.

## Gaps and conflicts, ranked

1. **No height.** No ridge height, no turret height, no eave height, and the three published figures disagree or are unlabelled. This sets the whole massing. A 5 to 10 m error is visible against the neighbours (Telus-type tower behind, from-funicular.jpg).
2. **No ground elevation or datum.** The hotel sits on the top of a bank. Without a grade, the model may float or sink against the sim's terrain. Funicular and Low Level are 69 to 235 m away, with no elevation either.
3. **Roof colour conflict.** Green vs black. At 1,000 to 3,500 ft it is the most visible colour.
4. **Plan is a traced ring, not surveyed.** Source is Bing. Details such as the curved corner and wing joins may be off by a few metres.
5. **No turret or dormer counts and no positions.** Only photo-estimated. No elevations or plan drawings.
6. **No wall-by-wall height steps.** Photos show different roof ridge levels per wing (from-river.jpg). No numbers.
7. **No facing-direction labels for the photos.** river-face.jpg is captioned "south face" in SOURCES.md. from-river.jpg is from the river side. The street face (roof-and-turrets.jpg) direction is not stated. I infer the street face is west to north-west from the entrance corner, but the folder does not say it.
8. **Photos are all one-point views.** No view of the north or east faces, and no straight-down view of the roof.
9. **Storey count conflict (7/10/11).** It changes window rows and floor lines only. Lower importance if the height is set from a source.
10. **Facade material conflict.** Limestone vs sandstone. Colour from the photos settles it for the texture.
11. **No night-lighting spec.** Only river-face.jpg.

## Handoff requests

| # | Request | Blocking? |
| --- | --- | --- |
| 1 | Ground elevation (ASL, with datum) at the hotel, at 100 Street grade and at the river-side base. A LiDAR or City of Edmonton contour value will do. | Blocking |
| 2 | One published height with a stated reference point. Ridge or eave of the main roof and top of the tallest turret. Try the City of Edmonton heritage file, the Fairmont fact sheet, or a measured drawing. If none, a photogrammetry or shadow-based estimate, clearly marked. | Blocking |
| 3 | Check whether MSFS 2024 already draws this hotel (photogrammetry or autogen) at the centre point, and at what height. If yes, the model needs to replace or sit on it, and the ground and height can be read from the sim. | Blocking |
| 4 | Roof colour decision: current copper or slate colour as seen in a recent photo in good light, from above if possible. A Bing or Google aerial of the roofs would settle it. | Blocking for colour quality |
| 5 | Aerial or oblique roof views from all four sides, so wing ridge lines, turret positions and the roof plan can be traced. | Nice-to-have, strongly suggested |
| 6 | Turret and dormer counts and positions, from a plan, an elevation drawing, or the aerial in 5. | Nice-to-have |
| 7 | Street-face and north-face photos and the compass direction of each saved photo. | Nice-to-have |
| 8 | Check the outline against a better source (City of Edmonton building footprint, orthophoto). Look at the curved corner (nodes 7 to 13) in particular. | Nice-to-have |
| 9 | A night photo of the roof with the lit facade, and whether the facade is floodlit all year. | Nice-to-have |
| 10 | Confirm the demolished 1953 wing is not in the sim's building layer, so we do not also model it. | Nice-to-have |
| 11 | Collision: confirm the sim treats scenery models as solid, and whether the hotel needs a simple hull. | Nice-to-have |
