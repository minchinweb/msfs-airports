# N258 Grierson Hill Bridge — model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 624.8 m (2,050 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 613.74 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Main deck height** (`road_deck`, DSM median): 630.80 m, 17.06 m above the river. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** no usable night photo found (see `../../DATA-SOURCES.md`).

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Blocked for a faithful model. Ready only as a generic placeholder (ready with assumptions).**

The folder gives a precise plan line (59 m) and a clear identity. It gives no width, no clearance, no elevation, no deck type and no pier count. It has no photo of this deck. I would be inventing every vertical dimension.

## What the folder gives me

| Fact | Value | Source |
| --- | --- | --- |
| Structure | Road overpass, Grierson Hill Road NW over McDougall Hill Road | NOTES.md Bridge; geometry.json `crosses` |
| OSM way | 106711211, `bridge=yes`, `layer=1` | geometry.json decks[0] |
| Centre | 53.538564, -113.488789 | geometry.json `centre` |
| Deck nodes (NE to SW) | 53.538771, -113.48851 to 53.538357, -113.489068 | geometry.json decks[0].nodes |
| Plan length | 59.0 m stored nodes; 59.1 m live nodes. Same way, two precisions. Not a published length. | NOTES.md Length; geometry.json |
| Heading (my calc from nodes) | About 38.7 deg true (NE end) / 218.7 deg (SW end). Check before use. | derived from geometry.json nodes |
| Lanes | 2, two-way, asphalt, 50 km/h tag | geometry.json tags |
| Rebuilt | 2012: deck demolished and replaced, pier-column repairs, paving, new guardrail. $4.5 M. | NOTES.md Year; SOURCES.md (CBC, Sun) |
| Supports | "pier columns" (CBC), "pillars" (Sun). No count. | NOTES.md Piers |
| NE approach | Way 106711201, 158.4 m, 4 nodes, two lanes, rises to junction at 53.539882, -113.487015 | geometry.json approaches |
| Further NE | Way 697598868, 70.4 m, three lanes, to 53.5403724, -113.4863442 | geometry.json (live OSM read) |
| SW approach | Way 106711229, 29.4 m, then split at 53.538154, -113.489353 | geometry.json |
| SW road | Way 151895211, 203.8 m, one lane one-way, 15 nodes, to 53.537415, -113.492093 | geometry.json |
| Under-road | McDougall Hill Road, ways 1433098757 and 303665641, no layer tag | NOTES.md Bridge |
| Photo | from-funicular.jpg, 15 Dec 2017, CC BY-SA 2.0, 1,920 px | SOURCES.md |

Conflicts inside the folder: none on numbers. The name varies (Grierson Hill Bridge, Grierson Bridge, Grierson/McDougall Overpass). The 59.0 and 59.1 m figures are the same line. NOTES.md says the road deck is a "short span" and also that the grade separation "reads at 1,000 ft"; neither is quantified.

What the photo shows (viewed): a wood-deck footbridge on a concrete pier in the foreground, and the Low Level truss on the right (dark grey-green steel). It shows a road under the footbridge with streetlights, and a road curving up to the truss. This deck is not isolated. I could not identify it. The folder itself says so.

## Build spec I would use from this alone

Everything vertical below is an assumption, not data.

- **Placement.** Centre 53.538564, -113.488789. Axis along the two deck nodes, about 38.7 / 218.7 deg true. Length 59.0 m.
- **Deck.** Box slab, 59.0 m long. Width unknown. I would use a two-lane road plus guardrail as a placeholder, flagged as assumed. Top surface asphalt dark grey. Edge: concrete barrier or steel rail (form unpublished, "new guardrail" only).
- **Supports.** Pier columns, count unknown. Placeholder: one row of round or rectangular columns at mid-span plus abutments at each end. Assumed. Concrete grey.
- **Under road.** McDougall Hill Road is not in this model. It exists in the sim as roads or as the R13/Low Level scene. The deck must clear it. The clearance is unknown.
- **Elevation.** No deck or ground elevation in the folder. I would take ground from the sim terrain and set the deck height above it as an assumption.
- **Approaches.** Do not model them in this file. They are road ways. The sim will place the road surface from its own data. The model is the deck, rails and piers only.
- **LOD.** LOD0 (close): deck slab, barrier, piers, soffit. LOD1 (1,000-3,500 ft): single box slab and two or three posts. Skip lights and texture detail beyond a flat colour.
- **Do not model.** The hillside footbridge (way 1271848915, F256), the Low Level trusses, the Rossdale Road bridge (N259), or the pedestrian underpass.

## Gaps and conflicts, ranked

1. **No clearance under the deck and no deck elevation.** The whole point of this model is the grade separation. Without it I cannot set the height. The OSM `maxheight` tags (5.2, 5.0) are on the under-road. The folder says they are not a clearance.
2. **No photo of the deck.** I cannot read colour, rail type, pier shape, soffit, or abutment from any image. The one photo is a different structure.
3. **No width.** No `width` tag. Lane width unknown. Sidewalk presence unknown.
4. **No span count or pier layout.** Pier columns are named, but not counted or sized.
5. **Deck type unknown** (girder, slab, beam).
6. **Terrain interaction unknown.** The approaches sit on a hillside embankment (landslide fill, 1961). No grade points are given. The sim terrain may cut into or float away from the deck.
7. **Year of original deck unknown.** Low impact. The 2012 deck is what stands.
8. **Heading is my calculation.** Low risk, but not stated in the folder.

## Handoff requests

| # | Request | Blocking? |
| --- | --- | --- |
| 1 | Find the deck-to-road clearance (soffit to McDougall Hill pavement) and deck elevation ASL. Try a City bridge sheet, a drawing, or a measurement from a street-level photo with a known-size object. | Blocking |
| 2 | Get at least two openly licensed photos of the deck: one from McDougall Hill Road looking at the soffit and piers, one from the deck showing the rail and sidewalk. Or extract the City 2025 orthophoto tile 33183E593382N (7.5 cm) into `photos\`. | Blocking |
| 3 | Measure deck width from the 2025 orthophoto (curb to curb and outer to outer). | Blocking |
| 4 | Count pier columns and note their shape and spacing, from the orthophoto or a street photo. | Blocking |
| 5 | Get terrain heights at both ends and under the deck (DEM or the sim's own ground height) to confirm whether the sim terrain will clip the deck or leave a gap. | Blocking |
| 6 | Confirm the deck type and rail form (concrete barrier, steel rail, height). | Nice-to-have |
| 7 | Confirm sidewalk or no sidewalk on the deck. | Nice-to-have |
| 8 | Check whether the sim already draws McDougall Hill Road under the deck, and whether road auto-bridging from OSM conflicts with a placed model. | Nice-to-have, but check before building |
| 9 | Night lighting: are there streetlights on the deck? The 2017 photo shows lights on the hill road below. Count and spacing needed if lit. | Nice-to-have |
| 10 | Collision and road-surface need: decide whether the deck is a driveable surface or just a visual. The folder says nothing. | Nice-to-have |
| 11 | Concrete and asphalt colour reference from a close photo. | Nice-to-have |
| 12 | Original (pre-2012) year. | Nice-to-have |
