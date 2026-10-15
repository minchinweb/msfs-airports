# F256 100 Street Funicular: model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

## Verdict

**Ready with assumptions.** Plan positions are good. The footbridge, lookout, track and stair can be placed from `geometry.json`. Track slope length and grade are published. Missing: bridge width, as-built rise, any elevation, gauge, cabin height. I would assume those and flag them. Nothing here blocks a 1,000-3,500 ft model. Close fly-bys will look generic.

## What the folder gives me

Source tags: N = NOTES.md, S = SOURCES.md, G = geometry.json, P = photo.

### Plan geometry (G, OSM, 14 Oct 2026)
- Footbridge outline, way 1271848915: 12 corners, perimeter 191.0 m. Edge lengths 3.6, 3.5, 48.5, 19.1, 21.2, 4.4, 19.8, 1.1, 1.3, 16.8, 3.2, 48.7 m (G). Centre 53.539305, -113.487472 (G, N).
- Footbridge centreline, way 533867748: 7 nodes, 91.0 m horizontal, bends in the short middle segments (G). North end 53.5396096, -113.4880256. South end 53.5390824, -113.4870404.
- Kink segments: ways 702363113 (5.8 m), 1271848916 (15.7 m), 702363114 (8.8 m) (G).
- Track, way 490235928: two nodes, upper 53.5396888, -113.4896381, lower 53.5394103, -113.4887917. 64.0 m horizontal (G, N).
- Stair ways 533867743 (37.9 m) and 1301170658 (22.7 m), wood, `width=6` tag (G). Gap between them 3.9 m. South end is 5.6 m from the lower track node.
- Bridge steps 535658874 (13.6 m), 622160716 (14.4 m) (G).
- Lower track node to bridge north node: 55.3 m (G). No mapped link.
- Footbridge centre is 105.4 m from the Low Level 1900 north node, bearing 23.0 deg (G).
- Upper track node is 173.1 m from that node, bearing 323.8 deg (G).

### Derived by me from G (checkable)
- Track bearing, upper to lower: about 119 deg true (ESE), from 31 m south and 56 m east. The car descends toward ESE.
- Footbridge bearing, north end to south end: about 132 deg true (SE). Straight-line chord about 88 m.
- Track and bridge are not collinear. The track lower node sits about 55 m WNW of the bridge north end.

### Published figures
- Track: 66.0 m along a 23.5 deg grade (S: award submission, CISC; N). Journal says 55 m (N, S). Mapped 64.0 m horizontal (G).
- Cabin: one car, 3 m by 2.2 m, 20 people (S: City). Speed 2 m/s, 48 s run (N, S).
- Bridge: 50.0 m main span, 19.4 m span, 19.0 m cantilever. Two weathering-steel girders, precast deck segments about 3 m long, cementitious topping, Kebony platforms (N, S).
- Supports: one concrete pier plus the steel-framed glass elevator shaft, which carries the bridge (N). Pier seen in the 15 Dec 2017 photo cited in N, not in this folder.
- Clearance about 6 m above Grierson Hill Road (S: City, N).
- Lookout: 19 m cantilever, 19 m above river bank. Glass railing, built-in seating (N, S).
- Urban stair: 4.5 to 7.5 m wide, Kebony treads, hollow precast concrete benches, galvanized steel stringers (N, S).
- Upper canopy: galvanized steel, glass and wood, over below-grade concrete rooms (N).
- Elevator: up to 10 people (N).
- Hours 7 am to 9 pm (S, G). Opened 7 Dec 2017.

### From photos
- `car.jpg`: cabin is a black-framed glass box with black glass side panels, on a pale grey/white steel base. Floor is stepped to the slope. Two dark rails on a galvanized steel truss beam. Grey galvanized steel-grate walkway with a pipe rail runs beside the track. Black mesh fence at the lower end. Telus tower and trees behind.
- `track-and-car.jpg`: upper station is a small glass-and-steel canopy at the top, below the tall tower. Long glass balustrade with galvanized posts and textured/frit glass panels beside the track. Concrete piers and galvanized steel posts under the stair.
- `lookout-elevator.jpg`: elevator shaft is a glass box (four glazed panels with point fixings) with a metal louvre top band, sitting on a grey concrete-looking deck. Railings are galvanized steel with vertical bars. Deck flares open near the shaft. Funicular stair is visible on the hill at left.
- `lookout-and-truss.jpg`: from the river, the lookout is a long rust/weathering-steel underside cantilevering out of the trees at the top of the bank. Low Level truss is at the left edge.
- `lookout-from-below.jpg`: lookout end is a rectangular box deck with a weathering-steel (brown-red) underside, dark railing, glass panel at the left end. It projects over the trees.
- `stairs-toward-low-level.jpg` (night): wood treads, pale concrete bench blocks, glass rail on one side, grey metal rail with embedded vertical LED strips on the other, steel handrail. Warm light. Gives the night lighting look.

## Build spec I would use from this alone

Frame: local metres, X east, Y up, Z north. Build from lat/lon with R = 6378137 m. Set the origin at the footbridge centre (53.539305, -113.487472). One glTF with sub-nodes, or three: track, footbridge+lookout, stair.

### 1. Footbridge (weathering steel + deck)
- Plan: the 12-corner outline in G, extruded as a deck. Use the 7-node centreline in G as the spine. Width taken from the outline: the short edges (3.6, 3.5, 3.2, 4.4 m) suggest about 3.5 m, with a wider flared area at the lookout. This is my reading of G and not a published width. Assume 3.5 m on the main run.
- Heading: north end to south end about 132 deg. The short middle segments bend.
- Layers: two weathering-steel girders (colour: rust-brown from `lookout-from-below.jpg`). Deck top: warm wood tone on the span (15 Dec 2017 photo, cited in N only), grey topping at the lookout (`lookout-elevator.jpg`). Railing: galvanized steel with vertical bars, height assumed 1.1 m.
- Elevation: deck about 6 m above Grierson Hill Road (S: City). Road ASL is not given. Lookout 19 m above the bank (S).
- Piers: one concrete pier under the span, plus the glass elevator shaft at the south end. Pier position is not given. I would place it under the 48.5 m edge, mid-span (assumption).

### 2. Lookout and elevator
- South end of the bridge. Cantilever 19 m beyond the shaft (S).
- Glass elevator box about 3 m square plan, two stories of glass plus a louvre band on top. Size is assumed from the photo against the railing. Not published.
- Deck: grey. Underside: weathering steel. Glass railing and seating (S, N).

### 3. Funicular track
- Line from the upper node to the lower node, bearing about 119 deg. Use 66.0 m slope length and 23.5 deg grade as published. That gives plan length of about 60.5 m and rise of about 26.3 m (my arithmetic). The mapped plan length is 64.0 m. I would stretch the track to the mapped nodes so it sits on the map, and mark the grade as unresolved.
- Beam: galvanized steel truss under two rails. Rail gauge assumed about 1.5 m (not published).
- One cabin. 3.0 by 2.2 m footprint (axis unresolved). Height assumed about 2.4 m. Black frame, glass, pale grey base. Park it at the lower station for the static model.
- Upper canopy: small glass and galvanized steel box at the top, with a below-grade concrete room (not modelled).
- Walkway grate beside the track, pipe rail, black fence at the bottom.

### 4. Urban stair
- Parallel to the track, on the south side, from the OSM ways 533867743 and 1301170658. Width assumed 6 m (OSM tag, in the City's 4.5-7.5 m range). Wood treads, pale concrete bench blocks, glass balustrade on one side. Steel posts and piers underneath.

### LOD ideas
- LOD0 (1,000-3,500 ft): a single extruded footbridge with the brown steel underside, a thin line of track with a small dark box, a wood stair strip, a box deck for the lookout. About 500 to 1,500 triangles. Colour texture only.
- LOD1 (close): railings as alpha-card textures, girders, pier, glass elevator, cabin detail, stair benches.
- Glass: use a low-alpha PBR material. Avoid many transparent layers.

### Placement and sim notes
- No elevation exists in the folder. Terrain must supply the base. Anchor the bridge with the 6 m clearance over the road, and anchor the lookout using 19 m above the bank. Both need a terrain read in the sim.
- Night: add emissive strips on the stair rail (from `stairs-toward-low-level.jpg`), warm lamps.
- Collision: none needed from the folder.

## Gaps and conflicts, ranked by harm

1. **No elevation or datum.** No deck, soffit, lookout or station ASL. The whole vertical placement relies on "6 m above the road" and "19 m above the bank". Both need terrain heights that the folder does not have. High harm: the model can float or clip.
2. **Track length and rise conflict.** 55 m (Journal), 66.0 m (award, at 23.5 deg), 64.0 m (mapped, horizontal). 66.0 at 23.5 deg gives about 60.5 m plan, which does not match 64.0 m. The 2015 25 m drop on 55 m slope implies about 27 deg, which does not match 23.5 deg. The folder does not resolve this. Medium-high harm: track height and slope are wrong by a few metres.
3. **Bridge width not published.** OSM outline gives about 3.5 m on the short edges, but the City stair is 4.5-7.5 m and the 2015 boardwalk is 6 m. Medium harm.
4. **Bridge edge lengths do not match published spans.** Outline edges 48.5 and 48.7 m are close to the 50.0 m main span. 19.1, 19.8 and 21.2 m are close to the 19.4 m span and 19.0 m cantilever. G says they were not matched. Total published length is missing. Mapped centreline 91.0 m (G) vs 91.1 m (Grierson notes, cited in G). Low harm for the 0.1 m. The span layout is a medium gap.
5. **Pier position and form.** One concrete pier is mentioned. The location and size are not given. The pier photo is in another folder. Medium-low harm.
6. **Cabin axis and height.** 3 by 2.2 m, no height, no axis. Photos show it clearly as taller than the rail beam. Low-medium harm.
7. **Gauge and beam size.** Not published. Low harm at altitude.
8. **Deck material split.** Wood-coloured span (2017 photo in another folder) vs grey deck at the lookout. Low harm.
9. **Photo coverage.** No aerial. No view of the bridge from the road in this folder. No plan view of the lookout shape. Medium harm for outline accuracy. The OSM outline is the only plan source.
10. **Stair width tag 6 vs published 4.5-7.5 m.** Low harm.
11. **Name variants (Lookout / Overlook).** No model impact.

## Handoff requests

**Blocking**
1. Ground elevation at the lower and upper track nodes, the bridge north and south ends, and the point on Grierson Hill Road under the bridge, from a City LiDAR/DEM source. State the datum. Needed to place all of it vertically. Also check what the sim terrain does there, since the bank is steep.
2. An as-built track rise or an elevation difference between the upper and lower stations. Resolve the 55 / 64 / 66 m question with one source (shop drawing, City engineering page, or survey).
3. A published or measured bridge deck width, plus the plan shape of the lookout (a top-down aerial or a City orthophoto crop). Without it the outline is a guess.

**Nice-to-have**
4. A close-up from the road looking up at the footbridge: pier shape, girder depth, soffit height. Photos of the 15 Dec 2017 frame should be copied here, since it is cited and not in this folder.
5. Cabin height and gauge. A side view of the car at the lower station.
6. Pier count and position.
7. Colour refs. Weathering steel tone, Kebony tone and grey topping tone, in daylight, flat-lit.
8. Night lighting list: which parts are lit (stair rail strips, lookout, canopy, cabin). Photo of the lookout at night.
9. Terrain interaction: is the track and stair fully above ground, or cut in? The photos suggest raised steel on piers. Confirm whether to flatten or exclude terrain.
10. Collision: do we want the lookout deck walkable? Probably no need. Confirm.
11. Whether the Hotel Macdonald, the Telus tower and the Low Level model will carry the context, so this model stays small.
