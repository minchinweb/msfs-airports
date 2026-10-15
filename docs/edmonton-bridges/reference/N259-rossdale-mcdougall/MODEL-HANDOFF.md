# N259 Rossdale Road over McDougall Hill: model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Reviewed from this folder only: NOTES.md, SOURCES.md, geometry.json, photos/from-west.jpg.

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 630.5 m (2,068 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 613.74 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Main deck height** (`road_deck`, DSM median): 636.19 m, 22.45 m above the river. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** no usable night photo found (see `../../DATA-SOURCES.md`).
- **Street-level photos:** 4 daytime Mapillary frames in `street/` (CC BY-SA, credits in `street/SOURCES.md`). They show railings, barriers, lamp posts, lane and sidewalk layout and approach shape from the road; not the underside or truss depth. Check them before treating those items below as open.
- **Open questions:** the other session's review (`CURSOR-HANDOFF.md`) re-checked against this data, item by item, in `OPEN-QUESTIONS.md`. Read it before the blocking items below.

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Blocked for a faithful model. Ready only as a plain placeholder slab with assumptions.**

The plan position and heading are good. Every vertical and cross-section number is missing: width, deck elevation, clearance, thickness, deck type. The one photo shows the structure as a few pixels in the lower right, behind trees. I could build a 49 m asphalt deck on a flat guess. I could not build anything that reads as this bridge up close.

At 1,000-3,500 ft the structure is small. A grey slab with parapets, correctly placed and oriented, would be acceptable from altitude. Close fly-bys would show invented detail.

## What the folder gives me

| Fact | Value | Source |
| --- | --- | --- |
| Centre (not surveyed) | 53.537724, -113.493132 (EPSG:4326, lat/lon) | geometry.json `centre`, NOTES.md |
| Deck centreline | 3 nodes: (53.537865, -113.4928469) NE, (53.5377277, -113.4931258), (53.5375852, -113.4934197) SW | geometry.json `decks[0].nodes` |
| Deck plan length | 49.1 m, OSM centreline. Not a published structure length | geometry.json, NOTES.md |
| Traffic | One-way, westbound (NE to SW), asphalt, 50 km/h tag. Lanes unknown | geometry.json `dimensions` |
| Layer | `layer=1`, `bridge=yes` since 2009. Road underneath is not bridge-tagged | geometry.json, NOTES.md |
| Crosses | McDougall Hill Road NW (way 636183922), 2 lanes, one-way, `sidewalk=no`. 165.5 m long. Does not share a node with the deck | NOTES.md, geometry.json `excluded` |
| Construction wording | Rehabilitation by Alberco, June 2013: hydro-blasting a CIP deck, new curbs, abutment repairs. CIP is not expanded | SOURCES.md (Alberco) |
| Approach NE | Way 36610268, 85.1 m, 4 nodes, down to a junction with McDougall Hill at 53.5382232, -113.4917136 | geometry.json `approaches` |
| Approach SW | Way 37120044, 40.0 m, 4 nodes, ends at 53.5373567, -113.4938829 (becomes 99 Avenue) | geometry.json |
| SW links | Ways 321190619 (24.4 m) and 321190620 (19.5 m, asphalt). They leave the deck's SW node and rejoin 37120044 | geometry.json |
| Photo | 2008 view from the west, camera 231 m west of centre. Concrete span and a curved road in the lower right | photos/from-west.jpg, SOURCES.md |
| Distance to N258 | 302.2 m (midpoint to midpoint). Not a clearance | NOTES.md |

Heading, derived by me from the node coordinates (flat-earth, cos(lat) = 0.594):
- Segment 1: about 230.3 deg true. Segment 2: about 230.7 deg true.
- The deck is effectively straight. Travel direction is about 231 deg true (SW). The axis is 51/231 deg.
- Offsets from the NE node to the SW node: about 31 m south, about 38 m west. That gives about 49 m, which matches the 49.1 m figure.

Conflicts inside the folder:
- No numeric conflicts. The folder says plainly that nothing is published.
- Name conflict: "MacDougall Drive" (news, Waze) vs "McDougall Hill Road" (OSM, Alberco). Not merged. Irrelevant to geometry.
- Year: none. Alberco gives June 2013 completion of a rehab. The Sun says carried over from 2012. The Montgomery line has no year.
- Photo vs text: NOTES.md says the span is "a concrete span over a lower road... with a curved road beside it". I could not confirm which structure in the photo is this deck (see below).

## Build spec I would use from this alone

Everything marked ASSUMED is my choice, not a folder fact.

**Placement and orientation**
- Origin at the deck midpoint 53.537724, -113.493132.
- Long axis at 231 deg true (travel direction). Model it as a straight deck. The 0.4 deg kink between segments is noise.
- Deck length 49.1 m along the axis. Add the shoulders and abutments inside this length unless told otherwise.
- Elevation: not available. I would take the sim's terrain height at the centre and place the deck at ASSUMED terrain + 0 m reference, then raise it. The raise amount is unknown. See handoff requests.

**Components**
1. Deck slab. 49.1 m long. Width ASSUMED 8-10 m for one-way, 2 lanes. NOT in the folder. Thickness ASSUMED 0.6-1.0 m. NOT in the folder.
2. Asphalt surface and 2 lane lines. Dark grey asphalt. ASSUMED: lane count 2.
3. Curbs on both sides. Alberco says new curbs. Form unknown. ASSUMED 0.2 m raised concrete.
4. Parapet or guardrail. Not described in the folder. In the photo something like a low concrete rail with a yellow edge line runs beside the road at the lower right. Treat it as ASSUMED.
5. Abutments, 2. Count is not published. Alberco only says "abutment repairs". ASSUMED a plain concrete wall at each end.
6. Piers. None known. ASSUMED none (single span).
7. Approach roads. Ways 36610268 (85.1 m) and 37120044 (40.0 m) from geometry.json, as ground-level or embankment roads. Link ways 321190619 and 321190620 as small ramps or road polylines.
8. Under-road. McDougall Hill Road 636183922 is not copied into geometry.json. I do not have its nodes. The deck crosses it in plan, but I cannot place it.

**Materials and colours (read from the photo, low confidence)**
- Concrete: light grey, weathered. The photo shows grey-beige concrete on the lower-right span.
- Asphalt: mid-to-dark grey with faded lane lines.
- A yellow painted line or yellow edge element appears at the span edge in the lower right.
- Colour is read from an 8-year-old photo (2008), before the 2013 rehab. Do not trust it for the current state.

**LOD ideas**
- LOD0 (3,500 ft): a single textured box strip plus road decals. No sub-parts.
- LOD1 (1,000 ft): slab with curbs, parapet strips, abutment boxes.
- LOD2 (close): thickness, joints, soffit, light poles if sourced.
- Keep the poly count tiny. The structure is small and sits among tall downtown buildings that the sim may already draw.

**Terrain and sim**
- A 49 m road overpass on a river-valley bank will fight with the sim's terrain mesh. Plan a terrain-flatten or exclusion polygon along the deck and approaches if the terrain shows through. Not testable from this folder.
- Road surface: ASSUMED decorative only (visual road). Collision and the sim's own road network are not covered.

## Gaps and conflicts, ranked by damage to the model

1. **No deck elevation, no clearance, no vertical datum.** The grade separation is the whole point of this structure (NOTES.md says "a model that joins them at one grade is the wrong interchange"). I cannot set the height. The only nearby figure is the OSM `maxheight=4.5` on the road under it. NOTES.md says it is not a clearance or an elevation.
2. **No width, lane count, or lane width.** The footprint is a guess.
3. **The under-road geometry is missing.** The deck crosses McDougall Hill Road, but the folder does not copy way 636183922's nodes. I cannot draw the road underneath or its relation to the deck. The crossing angle is unknown.
4. **No usable photo of the deck.** The one photo (from-west.jpg) shows downtown towers, a hotel tower, trees and a curved road. The span is small, in the lower right, and is cut off by the frame edge and foliage. I cannot read abutment form, parapet shape, soffit, or piers. Photo is 2008, pre-rehab.
5. **No deck type, thickness, abutment form, curb or railing form.** Only "CIP deck", "new curbs", "abutment repairs".
6. **No approach gradients or grade-meeting points.** Ramp length and ramp slope are unknown. I cannot say whether the approaches are on embankment, retaining walls or cut.
7. **No lighting, signage, or furniture info.** Night look is a guess. The photo shows tall street lights nearby, which may or may not belong to this deck.
8. **Unclear which structure in the photo is the deck.** The folder states the span is lower right with a curved road beside it. The camera bearing is not given, so I cannot confirm.
9. Minor: no year built. No bridge number. Name variants. These do not affect the model.

## Handoff requests

Each is for a later researcher. B = blocking, N = nice-to-have.

1. **B. Deck elevation and under-road elevation, in metres above sea level, with the datum.** Source ideas: City of Edmonton LiDAR or DEM, contour data, bridge inspection sheet. At minimum the height difference between McDougall Hill Road and the deck surface at the crossing point.
2. **B. Clearance under the deck and deck thickness (soffit to road surface).** A single photo taken from the road below, looking along the road, with a known-height object (vehicle, person) would be enough for a scaled estimate. State that it is an estimate.
3. **B. Deck width and lane count.** Measure from a City orthophoto or from a plan view, edge to edge including curbs. State the lane count.
4. **B. Nodes of McDougall Hill Road way 636183922 at the crossing.** Copy into geometry.json so I can draw the under-road and the crossing angle.
5. **B. At least two close photos of the deck itself.** One from the side (a profile showing parapet, curb, and slab edge) and one from underneath or from the end showing the abutment. Openly licensed, or a note saying a link is URL-only and what it shows.
6. **N. Parapet or railing form.** A close photo or a description. Include any yellow-painted edge, since the 2008 photo suggests one.
7. **N. Approach grading.** For each approach, the elevation at the far node (36610268 at 53.5382232, -113.4917136 and 37120044 at 53.5373567, -113.4938829), plus whether there is an embankment, a retaining wall or a cut.
8. **N. Current colour reference.** One recent colour photo of the concrete and asphalt after the 2013 rehab. The 2008 photo may not match.
9. **N. Street lights and signs.** Position and type of lights on or beside the deck. A night photo if one exists.
10. **N. Confirm which structure in from-west.jpg is N259.** Annotate the photo or give the camera bearing. If it is not N259, say so.
11. **N. Terrain interaction.** Check in the sim (or from the SDK terrain) whether the sim's terrain mesh sits above the deck level here. If it does, say how deep, and whether the project needs a flatten polygon. Also say whether the sim already has an OSM-derived road mesh on this spot that would z-fight with the model.
12. **N. Collision and road-surface need.** Decide whether the deck should be drivable or visual only. Decide whether it should replace the sim's own road. The folder does not say.
13. **N. Published structure length, span count and abutment count.** City bridge file, or an inspection report. The folder found none.
