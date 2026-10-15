# R9 Dudley B. Menzies Bridge: model handoff review

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Reviewed using only this folder (NOTES.md, SOURCES.md, geometry.json, 8 photos).

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 614.9 m (2,017 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 614.92 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Main deck height** (`east_track`, DSM median): 638.28 m, 23.36 m above the river. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** 3 photos in `night/` with a lighting description in `night/SOURCES.md`.
- **Street-level photos:** 5 daytime Mapillary frames in `street/` (CC BY-SA, credits in `street/SOURCES.md`). They show railings, barriers, lamp posts, lane and sidewalk layout and approach shape from the road; not the underside or truss depth. Check them before treating those items below as open.
- **Open questions:** the other session's review (`CURSOR-HANDOFF.md`) re-checked against this data, item by item, in `OPEN-QUESTIONS.md`. Read it before the blocking items below.

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions.** The plan path, the cross-section (10 m deck, 4.5 m box), the form of the piers and walkway, and the colours are all there. No vertical number is there: no deck height, no pier height, no span lengths. A 1,000-3,500 ft view will accept a plausible deck height. A close fly-by will show the guess. The deck height and the terrain interaction need one decision before build (see Handoff requests).

## What the folder gives me

Each item shows its source.

### Plan geometry
- Two track centrelines, 20 and 19 nodes. Source: geometry.json, ways 700467672 (east, 685.1 m) and 37834327 (west, 682.3 m). Format is [lat, lon], EPSG:4326. These are plan lengths along the nodes.
- A bridge outline polygon, 38 nodes. Source: geometry.json, way 533052900. Width is about 9.0 m mid-run and 9.5-10.5 m near the ends (NOTES.md).
- Portal stubs: north 16.4 m and 16.3 m, south 9.6 m each. Source: geometry.json approaches.
- Walkway centreline: way 424285379, 296.4 m, plus stubs 51.9 m, 28.2 m and a link of 8.8 m. Source: geometry.json. NOTES.md says it is partial and is not a survey of the three river spans.
- Ends of the elevated run:
  - South: 53.527348, -113.515518 and 53.527387, -113.515571.
  - North: 53.532641, -113.510717 and 53.532662, -113.510829.
  - Source: geometry.json, NOTES.md.
- Centre point: 53.531, -113.512. Source: geometry.json.

### Cross-section and structure
- Top deck about 10 m wide (PCL via NOTES.md and SOURCES.md). The OSM outline is about 9.0-10.5 m wide. Wikipedia repeats the 10 m from PCL, so it is not a second source.
- Box about 4.5 m deep by 4.5 m wide. Hollow. Segments 2.5 m long, epoxy joints. Holes in webs and bottom slab (PCL via NOTES.md). The photos show round holes in the walkway soffit, which is a different surface (underside-walkway.jpg).
- Spans: 7 continuous box spans, of which 3 are the main river spans. Plus 2 slab-and-girder spans at the north abutment and 4 slab spans at the south abutment (NOTES.md, geometry.json dimensions).
- Two tracks, direct fixation, no ballast (NOTES.md; deck-tracks-night.jpg).
- Catenary poles on the centreline between the tracks, with contact wire over each track (NOTES.md; deck-tracks-night.jpg). Poles also stand at the deck edge in some views (elevation-from-north-bank.jpg shows a centre row).
- Blue railings along both edges of the top deck (elevation-train-and-walkway.jpg, deck-tracks-night.jpg).
- Piers: single round column and a wide cap, a lollipop form. The walkway passes through or beside the cap (pier-column-and-walkway.jpg, elevation-train-and-walkway.jpg, elevation-beside-high-level.jpg). Source for the form text: NOTES.md (Malik).
- Walkway: hangs under the 3 main river spans only. Concrete path, yellow centre line, blue railings with vertical balusters, blue hangers from the soffit (underside-walkway.jpg, elevation-box-and-walkway.jpg).
- Spiral ramp at the near end of the walkway (elevation-beside-high-level.jpg, lower centre). Two ramps total per PCL.
- North portal: concrete headwall in the slope with openings, the deck still elevated at the headwall, a roof slab with a fence above (north-portal.jpg).
- Plan gap to the High Level (not surveyed): minimum 49.4 m; the east track is 57.9-67.9 m away through the middle (geometry.json).
- Gauge is 1,435 mm. Overhead line is 600 V DC (NOTES.md).

### Flagged conflicts inside the folder
- **Length:** 530 m (PCL and Wikipedia; the seven-span box) against 600 m (Hibbard 1990 and Structurae) against 682-685 m (mapped plan length). NOTES.md explains the three as three different extents, but none of them is reconciled with the others. Abutment span lengths are missing, so they cannot be reconciled.
- **Pier-to-box width:** the box is 4.5 m wide and the deck is 10 m wide. The folder gives no overhang. That is a gap, not a conflict.
- **Outline width:** the OSM outline is 9.0 m mid-run against the 10 m published figure. The 10 m wins as a published figure. The outline is a mapper's polygon.
- **Pier count:** photos show about 3 piers in the river view and 1 near the bank. NOTES.md says no count is published. The photos do not settle the count.
- **Opening year:** the project list says 1989 and NOTES.md says August 1992. NOTES.md resolves this. 1989 is Government Centre.
- **Photo railing colour:** in elevation-beside-high-level.jpg the railing reads pale blue and the structure beige. In elevation-train-and-walkway.jpg the box reads light grey. These differ with light, not in fact.

## Build spec I would use from this alone

### Placement and heading (derived by me from geometry.json; no sim check)
- Origin: the centre 53.531, -113.512. Make the model in a local metres frame from the two track polylines.
- The plan is curved, not straight. The south end heads about 52 degrees (true) toward NE. The middle runs about 19 degrees. Overall chord south to north is about 29 degrees and about 669 m. These bearings are my own calculation from the nodes (first segment of way 700467672, middle segment, and the end points). They are not stated in the folder. Recheck them with a script.
- Use the track nodes as the spline. Do not use one straight bearing.
- Orientation: the model runs south (University) to north (downtown portal). The High Level is to the east. Do not model it (NOTES.md says so).
- Elevation: not available. See Gaps.

### Components
1. **Box girder, main run.** 4.5 m by 4.5 m hollow box, extruded along the track spline. Treat 530 m as the box length only (NOTES.md). Place it between the two abutment structures. Where the box starts and stops is not given.
2. **Top deck slab.** About 10 m wide, laid on the box. Thickness unknown. Visible edge and soffit as a thin slab. Use a placeholder thickness and flag it.
3. **Abutment spans.** 2 slab-and-girder spans (north) and 4 slab spans (south). Lengths unknown. Plain slab, same deck width, lower depth than the box (my assumption; the photos show the north approach is a shallower arched underside, north-portal.jpg).
4. **Piers.** Round column, wide cap. Count, height and spacing unknown. Place them under the box. Three main river spans means a pier at each span joint inside the river run.
5. **Walkway.** Hung under the three main river spans. Concrete path, yellow centre line, blue railings, blue hangers. Width unknown. Follow way 424285379 for the path (296.4 m, partial).
6. **Spiral ramps.** Two, one at each walkway end, described only by photo. No dimensions.
7. **Track bed.** Two direct-fixation tracks, gauge 1,435 mm. Spacing is mapped at 4.3-7.8 m (mostly 4.6-5.4 m). Use the mapped centrelines.
8. **Catenary.** Centre-line poles with contact wire. Height unknown. Poles are thin. At 1,000+ ft this is a line of poles and wires. Use a low-poly pole and a single wire strip.
9. **North portal headwall.** Concrete wall, openings for the tracks, a roof slab. Dimensions unknown.
10. **South portal.** No photo. Model a plain dark opening at the end of the slab span.
11. **Deck lighting (night).** Rows of warm lights along both edges, low (deck-tracks-night.jpg). Emissive strips. A blue lamp is on the centre pole.

### Materials and colours (read from the photos)
- Box and piers: light grey to pale beige concrete, weathered, with form-board lines (elevation-train-and-walkway.jpg, pier-column-and-walkway.jpg, elevation-box-and-walkway.jpg).
- Railings, hangers, walkway frames: a mid sky-blue, close to a bright light blue in direct sun and a darker teal in shade. I would use an sRGB near (40, 140, 210) for the sun-lit read. That is my read from the photos, not a sampled value.
- Walkway deck: grey concrete with a yellow centre line (underside-walkway.jpg).
- Walkway soffit: white or off-white painted concrete, with round vent holes (underside-walkway.jpg).
- Track: dark steel rails, grey deck between. Contact wire thin and dark.
- Portal headwall: pale concrete with grey roll doors (north-portal.jpg).

### LOD ideas
- LOD0 (over 2,000 ft): one extruded box ribbon, deck colour, blue edge lines, 3 pier boxes, no wires.
- LOD1 (about 1,000-2,000 ft): add the railing as a textured strip, the walkway as a ribbon with hanger lines, round piers, the poles as thin quads.
- LOD2 (close): real railings, hanger frames, the pier cap shape, wires, the portal headwall detail.
- Use one atlas for concrete and one for blue steel.

## Gaps and conflicts, ranked by how much they hurt the model

1. **No deck elevation and no height above the river or the valley floor.** Every vertical position is a guess. This is the biggest error source in a fly-by. (NOTES.md, geometry.json: deck_elevation_asl_m, height_above_river_m both null.)
2. **No pier count, spacing or height; no span lengths.** The rhythm of the piers is the most visible feature from 1,000-3,500 ft. The photos show only the shape. (NOTES.md, geometry.json.)
3. **No bridge-end positions for the box against the abutments.** The 530 m box and 600 m or 685 m total cannot be split into box and abutment sections. (NOTES.md, geometry.json.)
4. **Terrain and water interaction unknown.** The folder says nothing about where the river bank meets the piers, or whether the sim's terrain meets the north and south portal. The portal openings sit in a slope.
5. **Deck overhang, slab thickness and soffit shape.** The box is 4.5 m wide and the deck 10 m. The cross-section shape is visible in no photo. The side view shows a deep light box with a sloped or flat soffit edge, but no end-on view exists. (elevation-train-and-walkway.jpg shows a side only.)
6. **Walkway width, hanger spacing and drop below the soffit.** underside-walkway.jpg gives hanger pairs at regular intervals, but nothing is scaled.
7. **Catenary pole height and spacing.** Visible from the air as a line, so a wrong guess shows only in close views.
8. **South portal has no photo.** Only a note says nothing was found.
9. **Spiral ramps have no dimensions.** They are a small part of a distant view.
10. **Curve radius.** Derived from nodes, but the OSM polyline is coarse, with long straight pieces (for example 53.530175 to 53.531741). The curve of the box is shown more smoothly in the photos.
11. **Photo coverage.** No end-on or cross-section view of the box. No plan-view aerial of the whole crossing. No photo of the abutment spans from the south. Four of the eight files are 1,280 px thumbnails.
12. **Train and catenary use.** No instruction on whether to model a train. NOTES.md does not say. I assume none.

## Handoff requests

Each one is something a researcher can act on.

### Blocking
1. **Deck elevation.** The deck height above sea level (with datum) at the south portal, the middle of the river and the north portal. Sources: City of Edmonton drawings, the PCL or Engineers Collaborative sheets, LiDAR or a DEM, or a survey benchmark. Also the river water level in the same datum. A DEM and the sim's own terrain height at the piers would do if drawings are not available.
2. **Pier count and position.** A plan with the pier centres, or the span lengths for the 7 box spans, 2 north spans and 4 south spans. Fallback: count and place the piers from a high-resolution aerial or satellite image, with the shadows, and say it is measured from imagery.
3. **Pier and box vertical sizes.** The height from the river bed or ground to the soffit for the main river piers. Fallback: the height from the photo, using the known 4.5 m box depth as a scale in elevation-train-and-walkway.jpg.
4. **Terrain and water decision.** Does the sim's terrain or the water mesh at this location sit where the piers land? Check in the sim (a test marker) or ask the project owner. State whether the model needs flatten polygons, a pier base below the water, or a skirt. The user should confirm, because this folder cannot.

### Nice-to-have
5. **Box end-on cross-section.** A drawing or a photo from the end showing the box, the 10 m deck, the overhang and the soffit shape.
6. **Deck slab thickness and overhang.** From a drawing or a close edge photo.
7. **Walkway.** Width, drop below the soffit, hanger spacing, and exactly which three spans it covers.
8. **Catenary.** Pole height and spacing, and contact-wire height. Also whether the poles sit on the centreline only.
9. **Track spacing.** One published or measured figure for the track centres, to replace the mapped 4.3-7.8 m range.
10. **South portal photo.** An open photo of the University tunnel mouth, or a satellite crop.
11. **North portal sizes.** Width and height of the headwall and the openings, from a drawing or a scaled photo.
12. **Spiral ramps.** Plan view and approximate size of the two ramps, from imagery.
13. **Colour reference.** One photo in even light, or the paint name, for the blue and the concrete. Also whether the soffit is painted white along the whole box or only under the walkway.
14. **Night lighting.** A second view of the edge lights (spacing, colour temperature) and whether the walkway is lit. deck-tracks-night.jpg shows the top deck only.
15. **Collision and road surface.** State whether the deck needs a drivable or a walkable surface in the sim. Nothing in the folder asks for it. Default: none.
16. **Train.** Say whether a train should be modeled on the deck. Default: none.
17. **Length reconciliation.** A source that gives the box start and end positions in the same frame as the 685 m plan length, so the 530 m box and the abutments can be placed.
