# R15 Dawson Bridge - model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

## Verdict

**Ready with assumptions.** Plan shape, span lengths, span order, pier count, deck widths and colour are solid. No vertical data exists (deck elevation, truss depth, pier height, river clearance). Those must be assumed or read from the sim's terrain and from photo proportions. At 1,000-3,500 ft that is enough for a convincing silhouette. A close fly-by will expose the guessed truss depth and pier height.

## What the folder gives me

Source tags: N = NOTES.md, S = SOURCES.md, G = geometry.json, P = photo.

### Plan and spans
- Five simply supported riveted steel through-truss spans, west to east: 43.3, 43.3, 43.3, 76.2, 30.5 m (N, G `spans_west_to_east_m`, S TAC 2011). Same drawing in feet: 142, 142, 142, 250, 100 (N, G).
- Four concrete river piers on spread footings, one abutment per bank (N, S). Pier stations from the west abutment, computed from the spans: 43.3, 86.6, 129.9, 206.1 m.
- Span families (N, S HistoricBridges): 3 Camelback, 1 Pennsylvania (14 panels, the 76.2 m span), 1 small Pratt (east, 30.5 m). The same page's structure line calls the approach spans Camelback and omits the Pratt.
- Length between abutment walls 236.5 m (N, G). Total length also reported as 236.6 m.
- Deck centreline, OSM way 22916476 (G `decks[0]`): west node 53.548355, -113.468868. East node 53.549123, -113.465525. Length 237.1 m.
- Heading, my calculation from those two nodes: 85.5 m north and 220.9 m east. That is about 069 deg true, east-northeast. The west end is Riverdale. The east end is Forest Heights (N). The bridge is a straight line in plan (G has only 2 nodes).
- Footprint outline, OSM way 642360972 (G): long sides 236.2 m, ends 14.4 m. The end width is the mapped outline, not a structural width (G).
- Sidewalk centrelines, OSM (G). My calculation: about 5.7 m north and about 5.7 m south of the road centreline, so about 11.4 m apart.

### Cross-section
- Clear width 8.1 m (N, S, G). Two lanes, asphalt (N, G, P east-portal).
- Sidewalks: one each side, outside the trusses, on brackets. Wood, 2.65 m clear (before 2010: 1.5 m) (N, G).
- Deck, 2010 sandwich plate: 10 mm steel, 25 mm elastomer, 10 mm steel, 45 mm in all. Panels 1.9 m wide by 8.6 m long (8.5 m in the award text). Five lines of W460x74 stringers (N, G).
- Steel deck is planar, no crossfall. Asphalt 40 mm at the edges to 100 mm at the centre (N).

### Truss and detail
- Built-up members: angles, cover plates, gussets, lattice webs. Rivets 19 or 22 mm (N).
- Post-2010 members have plasma-cut lattice holes in a solid web (N).
- The south truss is about 10 percent heavier than the north (N). Not visible at sim scale.
- Lattice railing on the sidewalk: diamond lattice between posts with pyramidal caps (P sidewalk-and-truss). A 2016 photo. The 2026 barrier replacement is undescribed (N).
- East portal (P east-portal, pre-2010): X and diagonal portal bracing, a sway-frame top lateral, an overhead sign. Concrete jersey barriers at the road end. Sidewalks outside the truss, behind a steel fence.

### Colours and materials, from the photos
- Truss: mid to light blue paint. In east-portal it is light blue-grey. In elevation-five-spans it is saturated sky blue, but that photo is heavy HDR, so treat the saturation as exaggerated. Use about desaturated steel-blue (my reading, not a sampled value).
- Piers: pale grey-beige weathered concrete, solid shafts, wider toward the water (N, P elevation photos). They look wedge-shaped with a sloped face (P elevation-and-east-bank).
- Sidewalk deck: brown wood planks (P sidewalk-and-truss). Roadway: dark grey asphalt, with a yellow centre line (P east-portal).
- Water: brown and silty in summer, blue-green in autumn (P). Not part of this model.

### Conflicts inside the folder
- Length: 236.5 m against 236.6 m (N). The spans sum to 236.6 m (43.3x3 + 76.2 + 30.5). Use the span sum for the station layout. The 236.5 m is the wall-to-wall length. The 0.1 m difference does not matter.
- Width: 8.1 m clear (N, S) against 12.5 m (Wikipedia, Structurae), against OSM `width=7`, against a 14.4 m footprint end. These measure different things, but nothing states which. A 13.4 m sum (8.1 + 2x2.65) plus truss members fits the 14.4 m footprint better than 12.5 m.
- Panel length 8.6 m against 8.5 m. Irrelevant at sim scale.
- Span families: Pratt listed on one HistoricBridges line and omitted on another (N).
- Sidewalk surface: the south OSM way is tagged asphalt. The design says wood on both sides (N, G).
- NOTES.md says "north/south lane" for the train and the sidewalks. The bridge runs ENE, so north and south are the sides in the plan, which matches the OSM sidewalk sides.

## Build spec I would use from this alone

### Placement
- Origin: the west deck node 53.548355, -113.468868, at the deck centreline. X axis along the bridge at heading 069 deg true. Or use the midpoint of the two nodes, about 53.548739, -113.467197. Do not use the folder's "centre" 53.549, -113.467 for placement, as it is not on the line.
- Stations along the axis from the west abutment wall: piers at 43.3, 86.6, 129.9, 206.1 m. Abutments at 0 and 236.6 m. Plan offset from the OSM centreline start: the OSM line is 237.1 m, so the abutment walls sit about 0.25 m inside each end (assumption).
- Vertical: no elevation is given. Set the deck at the sim terrain height of the road at each end, read from the sim after placement. Assume a constant (planar) deck grade between the abutments, since the grade line was not raised (N). A different grade at each end is possible and not stated.
- Piers extend down to below the water. The water surface is the sim's river. Run the pier shafts far below the water (assume at least 10 m, unverified) so terrain and water cannot expose a floating base.

### Components
1. **Deck slab, 5 spans.** Width 8.1 m (clear roadway). Asphalt, dark grey, 0.1 m thick. Add a yellow centre line. Two lanes. Steel soffit, dark grey-blue. Floor beams at panel spacing. Depth is assumed.
2. **Sidewalks, 2 x 2.65 m.** Brown wood planks outside the trusses, centred about 5.7 m from the centreline. Carried on brackets. Level with, or slightly below, the roadway (assumption).
3. **Railing.** Diamond lattice panels with posts and caps, about 1.2 m high (assumption), on the outer edge. Lattice should be an alpha-cut texture or a simple mesh, not a modelled lattice.
4. **Five truss spans, two trusses per span.** One per side, at about 4.5 to 5 m from the centreline (assumption: sits between the 8.1 m clear roadway and the sidewalk).
   - Spans 1 to 3, 43.3 m: polygonal Camelback outline, five-sided top chord. P elevation photos show about 5 panels per span (my count, from a low-resolution view).
   - Span 4, 76.2 m, higher: 14 panels (S, HistoricBridges). Polygonal top chord, subdivided panels with counter bracing (P sidewalk-and-truss, elevation).
   - Span 5, 30.5 m, east, shorter and lower: a small Pratt, about 5 panels (assumption from P elevation-five-spans).
   - Depth: from photo proportions only. The Pennsylvania span is visibly about 1/6 to 1/7 of its length deep at the peak (my estimate, not in the folder). The lower spans are visibly shallower, about 1/6 to 1/7 of their length too. These are guesses.
   - Portal frames and sway bracing: X bracing at each end of each span (P east-portal). A top lateral bracing layer at roughly truss height.
5. **Four piers.** Concrete, grey-beige. Rectangular tapering shafts with a sloped face, wider at the water line (N, P). Plan size and height are assumed. In the photos the shaft looks about as tall as 1/3 to 1/2 of the visible height from water to deck (my reading, imprecise).
6. **Abutments.** Concrete walls at each end, blocks or wing walls. Add concrete barriers at the road ends (P east-portal).
7. **Approach stubs.** Short deck ramps blending into the sim's roads. West: Rowland Road, 2 lanes, 10 m wide for 21.4 m, then 135.7 m (G). East: two one-way carriageways, 4 m each, 48.5 m and 112.3 m (G). Prefer to let the sim's road network do this and only model the bridge.

### Materials
- Truss steel: steel-blue, roughness about 0.6 (assumption), no metallic shine, with a rivet/panel normal map if the budget allows. Piers: concrete, light grey-beige, rough. Deck: asphalt, dark grey. Sidewalk: wood, brown. All are read from photos by eye. No RGB was sampled.

### LOD ideas
- LOD0 (under about 500 m): full 3D chords, diagonals, portals, lattice railing as texture, rivet normal map.
- LOD1 (500 to 1,500 m): chords and main diagonals as boxes, no rivets, lattice as one alpha plane.
- LOD2 (beyond about 1,500 m): deck, piers, and a blue silhouette block per span with a diagonal pattern texture.
- Keep the five spans as separate nodes, so the long-span height difference stays visible at 3,500 ft.

### Other
- Night lighting: not documented. The 2016 photo is dusk and shows lit road lamps beyond the bridge and a lit street below the lattice. No lamp positions. Treat as unknown.
- Collision: model the roadway deck as a thin slab surface so vehicles and the sim ground can interact. No data on surface type in the sim. The sim may snap AI roads to its own network.

## Gaps and conflicts, ranked by damage to the model

1. **No elevations at all.** No deck, soffit, water, or pier height. The pier height and the clearance over the river set the whole look from the side. Hurts a lot at close range, moderately at altitude. Source of risk: placing the deck too high or too low relative to the sim's terrain and the valley slope.
2. **No truss depth and no panel counts** for the Camelback spans and the Pratt span. These set the silhouette. Photo estimates are low-resolution.
3. **No close-up photo of a pier, a footing, or the underside.** The pier shape (taper, nose, plan size) is read from two side views only. No photo shows the soffit or floor-beam depth.
4. **No survey of the approach grades.** The deck may slope up or down at each end. The valley slope on each bank is unknown, so the abutment height and the ramp length are unknown.
5. **Width ambiguity.** 8.1 m clear is firm. Truss spacing is not stated. The 12.5 m and 14.4 m figures are unreconciled.
6. **Barrier and railing after the 2026 work is undescribed.** The only railing photo is from 2016.
7. **Colour is from photos only.** Two photos are strongly HDR-processed, so the blue saturation is unreliable. No paint spec.
8. **No night-lighting data.** No lamp type or spacing on the deck.
9. **Pre-2010 photos** (east-portal, elevation-and-east-bank) show the old sidewalk and deck. Use them only for the truss and portal.
10. **No aerial or underside photo** (S says none openly licensed exists).

## Handoff requests

Each is a task for a later researcher. B = blocking, N = nice-to-have.

1. **(B) Deck and water elevation.** Find the deck elevation above sea level at both abutments and the normal river water level at the bridge, from the City's LiDAR, a contour map, or the Alberta bridge inventory. Otherwise a surveyed datum is needed to say whether the sim's terrain and water meet the pier bases. If there is nothing, state the deck-to-water height from any photo with a known scale.
2. **(B) Truss depth and pier height.** Find the truss height at the chord peak for the 76.2 m span and for a 43.3 m span, and the pier shaft height and plan size. Sources: the City's drawings, a TAC or Canadian Consulting Engineer paper figure at higher resolution, or a photo with a known-size object. The 1912 general arrangement figure has small elevation numbers that are not legible in the reproductions. Ask for the original drawing.
3. **(B) Ground and terrain interaction in the sim.** Check, in the sim, whether the terrain mesh at the Dawson site is cut at the valley, whether the river is a flat water polygon, and at what height the water sits. Decide whether the piers need to extend below the water or end in a terrain footing. This cannot be answered from the folder.
4. **(B) Placement check.** Place the OSM centreline in the sim and compare to the sim's own road and bridge. Record the offset and heading, and whether the sim already has an auto-generated bridge to remove or exclude. The 069 deg heading comes from my calculation of the two OSM nodes only.
5. **(N) Truss detail photos.** A straight side elevation of each span type (Camelback, Pennsylvania, Pratt), taken square on from the river bank, to count panels and read proportions. Plus a top-down view to check the top lateral bracing.
6. **(N) Pier close-ups.** Upstream face, downstream face, and plan. Needed for the nose shape and the batter. A drone or low-water bank photo.
7. **(N) Underside photo.** Floor-beam depth, stringers, bearings. The October 2025 City bulletin says scaffolding hung from a barge, so there may be City photos.
8. **(N) Colour reference.** A sampled paint colour or a City maintenance spec for the truss blue, in non-HDR daylight. Also the concrete tone.
9. **(N) Railing and barrier after June 2026.** A photograph taken after the late-September 2026 completion, from the deck, to confirm whether the lattice railing and the barrier were changed.
10. **(N) Lighting.** Lamp style, spacing, and whether there are lights on the trusses. A night photo of the bridge from the bank.
11. **(N) Approach grades.** From the City's or the OSM-adjacent LiDAR, the gradient of the east carriageways and the west road to natural grade, so the abutment blocks and ramps can be sized.
12. **(N) Width.** What the 12.5 m (Wikipedia, Structurae) measures, and the centre-to-centre distance of the trusses.
