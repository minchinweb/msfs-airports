# T133 Stony Plain Road replacement — model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Reviewed from this folder only (NOTES.md, SOURCES.md, geometry.json). The folder has no photos.

## Verdict

**Ready with assumptions.** The plan-view layout, cross-section parts and single-span/no-pier type are solid. Span length, deck elevation, girder depth and all colours are not in the folder. I would have to pick them. At 1,000-3,500 ft AGL this is a flat slab with rails and a rail corridor. That is enough for a plain model. A close fly-by would look generic.

## What the folder gives me

| Fact | Value | Source |
| --- | --- | --- |
| Centre | 53.5478, -113.5458 (lat, lon) | NOTES.md, geometry.json `centre` |
| Type | Single span, no piers, integral abutments, no deck joints | NOTES.md Bridge; agreement 4-3.2 |
| Girders | Reference design: steel haunched girder on concrete abutments on piles. Installed Aug 2023. Each 78,000 kg. Haunched in the installed bridge is unconfirmed. | NOTES.md; geometry.json `dimensions` |
| Deck | Full-depth cast-in-place concrete deck. Separate trackway slab in the middle. | NOTES.md (4-3.2.9.A, 4-3.2.12.A) |
| Span | Minimum 46 m. This is a requirement, not as-built. | NOTES.md; geometry.json |
| Width | Reference design 25.4 m. Old bridge 18.4 m. | NOTES.md; site location study |
| Cross-section | Two centre LRT tracks, one vehicle lane each way (City), north sidewalk 4.2 m min, south shared-use path 4.2 m min | NOTES.md Width, Deck |
| Lane width | 4.0 m min, gutter lip by trackway to barrier face | NOTES.md (3-2.11.8.B) |
| Barrier | TL-4 single-slope concrete barrier, steel bicycle rail both outside edges, rail top at least 0.37 m above concrete top | NOTES.md (4-3.2.10) |
| Surface | Asphalt (ACP) at least 80 mm. Concrete sidewalk and path. | NOTES.md; geometry.json tags |
| Abutment | Exposed seat height at most 1.2 m. Wildlife bench at mid-height of each headslope. 28 m MSE wall at SE end (EIA estimate). East abutment shifted slightly south. | NOTES.md |
| Clearance | Min 6 m over Groat Road. Not a measured height. | NOTES.md; geometry.json |
| Grades | Longitudinal min 0.5 percent. Lanes 2 percent crossfall away from centre. Walks 2 percent toward road. | NOTES.md (4-3.2.11) |
| Alignment | Slightly curved horizontally. Vertical profile "remains the same" (no values). | NOTES.md |
| Status | Road opened 30 Nov 2024. LRT tracks and slab being finished in 2026. Line not in service. | NOTES.md What opened |
| Plan lines | 6 ways with lat/lon nodes: 2 road carriageways, 2 track ways, north footway, south cycleway | geometry.json `decks` |
| Under road | Groat Road NW, 2 lanes one-way each way, asphalt, 60 km/h | geometry.json `under_groat_road` |
| Approach roads and LRT lines | Full node lists | geometry.json `approaches` |

**Derived by me from geometry.json node coordinates (haversine/flat-earth, approximate, mapper accuracy):**
- Bridge axis runs about ENE-WSW. North carriageway chord from (53.547959,-113.545566) to (53.547812,-113.546449) is about 60.5 m at bearing about 254 deg (east to west). Axis is about 74/254 deg true.
- Groat Road under the bridge runs about 143/323 deg true (from ways 521661800 and 521661798). The crossing is skewed about 20 deg off square. This is my estimate.
- Mapped centreline spacing across the deck, at about -113.5458: footway to cycleway about 20 m perpendicular. Track to track about 5.4 m. Footway to north road about 3.8 m. South road to cycleway about 5 m. These are mapped lines, not surveyed. The total fits the 25.4 m reference width once edge widths are added.

**Conflicts inside the folder**
- Lanes: City says one lane each way. Map tags `lanes=2` on each carriageway. NOTES.md keeps both. I would build one lane each way.
- Sidewalk: City project history does not mention a north sidewalk. Marigold, the agreement and the site study do. Build it.
- Mapped way lengths (60.7, 57.3, 58.2, 58.4, 57.5 m) differ from each other and from the 46 m minimum. NOTES.md says none is the span.
- The 8 m shorter note and the 60.7 m mapped length were deliberately not combined. Adding them would give nothing reliable.
- Ways 1160377622 (west to east) and 1222393198 (east to west) are labelled as paired tracks, but their endpoints differ. The ends of the track ways do not line up with the road ways. Expect mapping noise of several metres.

## Build spec I would use from this alone

Placement
- Origin at 53.5478, -113.5458. Deck axis heading about 74 deg true (derived). Mapped ways are the layout. Do not trust one way's length.
- Deck elevation: unknown. Use terrain elevation read at the Groat Road centreline under the bridge plus a clearance value I pick. I would use 6 m clearance plus structure depth (an assumption, marked as such). Alternatively read the sim ground at both abutments and set the deck to hold a 0.5 percent or more grade between them (assumption).
- Span: assume a nominal plan length of about 60 m between abutment faces, because the mapped lines are 57-61 m and the agreement minimum is 46 m. This is a choice, not data. Add short approach slab stubs to blend into the road.

Components
1. Two integral abutments, concrete, seat height up to 1.2 m exposed, with wingwalls or sloped embankments. Colour grey concrete.
2. Steel girder fascia, single span. Count and depth unknown. I would show a plain fascia of about 2.5 to 3 m deep at midspan (assumption), haunched deeper at the ends as in the reference design. Painted steel or weathering steel colour is unknown.
3. Cast-in-place concrete deck, total width 25.4 m (reference design). Concrete edge slab.
4. Centre trackway slab, two tracks about 5.4 m apart (derived). Rails, with a ballast-free concrete slab. No wires or poles are documented here. Add them only if told.
5. Two travel lanes, one each side of the track slab, 4.0 m min each. Asphalt dark grey. Concrete gutter strip next to the trackway.
6. North sidewalk and south shared-use path, each at least 4.2 m. Light concrete.
7. TL-4 single-slope concrete barriers separating the walks from the lanes, with a steel bicycle rail on top (0.37 m or more above concrete). Also a pedestrian rail (installed per 2026 update) and an LRV barrier railing.
8. Optional: MSE wall at the SE end (up to 28 m, estimate), wildlife benches on the headslopes.
9. Road and track approaches use the approach ways in geometry.json (Stony Plain Road both sides, Valley Line both sides) as short ramps blending into terrain.

Materials and colours: none available from photos. I would use neutral concrete grey for deck, barriers and abutments, dark asphalt grey for lanes, mid-grey steel for the fascia and rails. All are assumptions.

LOD ideas
- LOD0 (over 2,000 ft): box deck with lane/track/path colour strips, abutments, girder fascia as a single darker band.
- LOD1 (under 2,000 ft): add barriers, bicycle rail, track slab with two rails, haunched girder profile.
- Close fly-by: add lamp posts if confirmed (lit=yes on the road way suggests lighting), pedestrian rail, expansion of the east MSE wall.

Sim concerns
- Mark the road and path as collision/road surface only if the sim needs it. Keep Groat Road underneath open. Do not rely on the sim's terrain under the deck.

## Gaps and conflicts (ranked by damage to the model)

1. Deck elevation is not published. Deck height above Groat Road and above the sim terrain is a guess. This affects visible clearance and where the abutments meet terrain.
2. As-built span length is not published. Only the 46 m minimum and noisy mapped lines.
3. No photos at all, and no licensed ones. Girder depth, count, haunch, fascia colour, barrier shape, rail style, lamp style and abutment look are all assumed.
4. Girder depth, count and haunched status are unknown.
5. As-built width unknown. 25.4 m is the reference design.
6. Lanes: one each way or two each way is unresolved between City and map.
7. Skew and curvature are derived from mapped lines only. The folder says the alignment is "slightly curved" but gives no radius.
8. Terrain: no statement on how the sim's own terrain or the existing OSM-based road and rail will interact. No data on the bridge or terrain cut under the deck.
9. Overhead contact line (voltage 750, electrified=contact_line is only a mapper tag) is not documented as built on this bridge.
10. Night lighting is not documented, beyond `lit=yes` on the north road way.

## Handoff requests

Blocking
1. Deck elevation: find the surveyed or published road elevation (ASL) at both abutments and at Groat Road below, or a stated deck-to-road height. A researcher can try City survey data, the lidar DEM, or construction drawings. This is blocking. Without it I use a 6 m minimum plus an assumed structure depth.
2. At least one open or permitted side elevation photo of the finished or girder-set bridge, from Groat Road, showing fascia, girder depth, haunch, abutment and wing walls. Blocking for any close fly-by quality. Not blocking for a high-altitude model.
3. As-built span length or abutment face-to-face length. Ask for a plan, an as-built drawing or a measurement on aerial imagery. Blocking for scale accuracy. The assumption of about 60 m is otherwise used.

Nice-to-have
4. One deck-level photo showing lane layout, barrier, bicycle rail, pedestrian rail, LRV barrier and track slab, to settle the one-or-two lane question and the railing styles.
5. Girder count and depth. A construction photo of the girders before the deck was poured would settle both.
6. Colour reference: steel fascia paint or weathering steel, barrier colour, asphalt, path colour. A single colour photo is enough.
7. Overhead catenary: whether poles and wires are installed on the bridge and their positions and heights. Needed only if wires are to be modelled.
8. Lighting: lamp type, spacing and height on the bridge, and whether it is lit at night. Also any LRT-specific lighting.
9. Terrain interaction: check, in the sim, whether the default terrain or OSM-generated road/rail at this spot sits above or below the planned deck, and whether the Groat Road cut is deep enough for the bridge to be visible. The research agent cannot answer this from the folder. Someone with the sim needs to check it. Blocking only if the terrain clips the deck.
10. Whether the sim's own auto-generated bridge or road geometry already exists here, so the model does not duplicate it.
11. Mid-2026 status: confirm what is built on the track slab (rails, wires, poles) at the time of the sim's data, so the model matches.
12. Groat Road below: confirm the sim road and its cut line up with the underpass so the clearance reads right.
13. Whether to model the SE MSE wall (about 28 m, estimate) and the wildlife benches. Photo or drawing would settle it.
