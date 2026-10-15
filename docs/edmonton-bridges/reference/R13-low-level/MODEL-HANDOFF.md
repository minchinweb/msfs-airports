# R13 Low Level Bridge: model handoff review

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Reviewed using only this folder (NOTES.md, SOURCES.md, geometry.json, 11 photos).

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 613.7 m (2,014 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 613.74 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Main deck height** (`road_deck`, DSM median): 630.96 m, 17.22 m above the river. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** 3 photos in `night/` with a lighting description in `night/SOURCES.md`.

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions.** Plan shape, span count, truss type, lane layout, sidewalk side and look are solid. Deck elevation, truss depth, pier height and deck thickness are not in the folder. I would have to take the deck height from the sim's own terrain or scale it off photos. That makes the model buildable but not dimensionally accurate vertically.

## What the folder gives me

| Fact | Value | Source |
| --- | --- | --- |
| Two parallel bridges, one-way each, 2 lanes each | east deck = 1900 span, northbound; west deck = 1948/49 span, southbound | NOTES.md "Bridge"; geometry.json decks |
| Type | Pratt through truss, steel, riveted, horizontal chords | NOTES.md; photos elevation-aligned-spans, piers-from-river |
| Spans | 4 per bridge | NOTES.md (2008 paper, Wikipedia, HistoricBridges, Structurae) |
| Span length | 53 m each (2008 paper) OR 51.8 m (170 ft, HistoricBridges) | NOTES.md. CONFLICT, small |
| Panels per span | 7 (northbound only) | NOTES.md (HistoricBridges) |
| Structure length | northbound 213.1 m; southbound 211.7 m | NOTES.md |
| Mapped centreline length | east 213.9 m; west 212.6 m | geometry.json |
| Centreline end points, east deck | S 53.537494,-113.485273 to N 53.538433,-113.488094 | geometry.json way 31882107 |
| Centreline end points, west deck | N 53.538352,-113.488166 to S 53.537419,-113.485362 | geometry.json way 22916473 |
| Outline of both decks | 23.4 m wide at N end, 23.5 m at S end; long edges 211.1 m (W) and 212.0 m (E) | geometry.json way 462866197 |
| Truss centreline spacing, northbound | 7925 mm (after 1980; was 6096 mm) | NOTES.md (2008 paper) |
| Piers | 3 concrete piers in the river per bridge (northbound), on timber piles; abutment at each bank | NOTES.md |
| Sidewalks | one per bridge, on the OUTER side (east for NB, west for SB); none in the gap | NOTES.md; geometry.json ways 302605469, 302605430 |
| Sidewalk surface | concrete, lattice railing | photo sidewalk-plaque.jpg; geometry.json (west way) |
| Members | angles, cover plates, gussets, lattice; 40 percent replaced in 2006, bolted | NOTES.md |
| Surface | asphalt, 50 km/h | geometry.json |
| Approaches | five-plus OSM ways with plan lengths and node lists | geometry.json "approaches" |

Derived by me from geometry.json (plain trig, not in the folder):
- Axis runs about 118.5 degrees true from the north end to the south end. Northbound traffic heads about 298.5 degrees.
- Centreline-to-centreline distance between the two decks is about 10.2 m. The two end nodes sit at the same station along the axis, so the decks are not staggered in plan.
- Straight in plan. Each deck is a two-node line.

### Conflicts inside the folder
- Span 53 m vs 51.8 m. Four spans give 212 m or 207.2 m. The total is 213.1 m. Neither adds up exactly. Allow bearing and abutment slop of 1 to 6 m.
- Northbound 213.1 m vs mapped 213.9 m. Southbound 211.7 m vs mapped 212.6 m. NOTES.md says use OSM for plan, published for structure length.
- Outline 23.4 m across both decks vs 10.2 m centreline spacing and 7.925 m truss spacing. Consistent only if each deck carries about 6 m of outside overhang, sidewalk and railing. Not stated.
- Pier count: 3 in the water per NOTES.md. Photos elevation-aligned-spans and elevation-toward-downtown show 2 piers clearly in the channel. A third sits at the left bank edge in elevation-aligned-spans. This is plausible but unconfirmed.
- Colour: SOURCES.md says the paint colour was not used to date either span. Photos disagree: pale sage grey-green (both-decks-oblique, both-decks-from-north, sidewalk-toward-downtown), rust-brown and grey (elevation-aligned-spans, 2024), and grey-green NB vs rust-brown SB floor system (underside-and-pier, Sept 2026, which is after the 2025 SB repairs).
- Cannot tell from the folder which side in underside-and-pier is which span.
- Truss outline vs sources: "Wikipedia says twin of the same design", "unique" per City memo. Photos show them near-identical in outline.

## Build spec I would use from this alone

**Placement and orientation**
- Two straight decks. Use geometry.json end nodes as the deck centreline ends. Heading axis about 118.5 degrees true. East (downstream) deck = NB, west (upstream) deck = SB. Centreline spacing 10.2 m.
- Z: the folder gives no deck elevation. Snap to the sim's terrain at the abutments and read the river level off the sim. Treat the deck as flat. No grade is given. The photos show a level deck on the river spans. See requests.

**Components (per bridge)**
1. Four simple Pratt through-truss spans, each about 53 m (use 52.5 m to fit the 213 m total, or use the mapped lengths). Two truss planes per bridge, 7.925 m apart on the NB bridge. Assume the same for SB (unverified).
2. 7 panels per span, from HistoricBridges. Each panel about 7.6 m. Photo elevation-aligned-spans shows closer to 7 to 8 diagonals per span and fits.
3. Top chord horizontal, inclined end posts, verticals, diagonals in Pratt pattern (diagonals lean toward the span centre), portal bracing at both ends of each span, top lateral bracing and sway bracing overhead. Seen in both-decks-oblique, piers-from-river. Photo both-decks-oblique also shows X-bracing in the centre panels.
4. Lattice-laced built-up members: box sections with lattice webs on diagonals and posts (sidewalk-toward-downtown, underside-and-pier, sidewalk-plaque). Rivet heads visible. Model as boxes with a normal map or alpha lattice.
5. Floor system under the deck: stringers, floor beams, cross-bracing (underside-and-pier). Hanging below the roadway, visible from river level. Depth not given. Photos suggest a visible floor system roughly 1 to 1.5 m, not measured.
6. Deck: asphalt, 2 lanes per bridge, 50 km/h.
7. Outer sidewalk, concrete, one per bridge, outside the truss, with diamond-lattice railing, square posts with pyramid caps, light sage/grey paint (sidewalk-plaque, sidewalk-toward-downtown, piers-from-river). Sidewalk shelters the outer bottom chord.
8. Gap between spans: open to the sky, about 10.2 m minus the deck widths. A utility pipe (insulated, grey) runs along the gap under the decks in underside-and-pier. Optional detail.
9. Piers: three per bridge. Concrete shafts, one rectangular shaft under each bridge, side by side with a narrow joint. Shaft base flares/chamfers out toward the water, with an angled nose upstream (piers-from-river, underside-and-pier). Board-formed concrete, stained cream/grey.
10. Abutments at each bank: concrete, with rock rip-rap slope on the north bank (piers-from-river, underside-and-pier).
11. Approaches: ramps as ribbons along the geometry.json approach ways, pulled to the sim terrain. NOTES.md says Grierson Hill Bridge (N258), funicular (F256), Rossdale (N259), and Scona/Connors (N260) are other projects. Do NOT include them.
12. Road lighting and a traffic signal gantry at the south end (both-decks-oblique, both-decks-from-north). Optional.

**Materials and colours (read from the photos)**
- Truss and railing: pale sage grey-green, roughly RGB 190/200/180 in sun. Use as the baseline from both-decks-oblique and sidewalk-plaque.
- Rust-brown overlay for the older floor system and parts of the trusses (underside-and-pier, elevation-aligned-spans). Choose one grade; I would use pale sage on both bridges for the fly-by view.
- Piers: light cream-grey concrete, brown/rust streaks, darker waterline stain.
- Deck: mid-dark grey asphalt, yellow centre line on approaches.
- Sidewalk: light grey concrete.
- Do not model winter snow.

**LOD ideas**
- LOD0 (far, 1,000 to 3,500 ft): trusses as slim box frames plus alpha-textured diagonal pattern, deck slab, 6 pier boxes. Skip rivets and lattice detail.
- LOD1 (close fly-by): real chord, post and diagonal geometry, railing, floor beams.
- LOD2: add lattice, plate detail, rivets via normal map, sidewalk lamps.
- Truss open panels read as see-through from above; the model must keep the gap open. That matters most at 1,000 to 3,500 ft.

## Gaps and conflicts (ranked by how much they hurt)

1. **No deck elevation or clearance to the river** (vertical datum, deck, soffit, water). I must guess it from sim terrain. A wrong height floats the bridge or buries the piers. Hurts most.
2. **No truss depth.** The look of the trusses from the air depends on it. Must scale from photos. Only proportions are readable. No scale reference in-frame beyond vehicles.
3. **No pier height, size, or footprint.** Photos show tall shafts with visible flared bases but no numbers. Waterline in the photos varies with the season.
4. **No deck, roadway or sidewalk widths in metres.** Only the 7.925 m truss spacing (NB), 10.2 m centreline spacing (derived), and the 23.4 m outline.
5. **Span staggering unclear.** pair-and-james-macdonald and both-decks-oblique hint that truss joints on the two bridges may not line up. The folder says the piers sit side by side (underside-and-pier) but not whether span lengths match exactly.
6. **Southbound truss details (panel count, spacing, member sizes) not given.** I would copy NB.
7. **Pier and foundation behaviour vs sim terrain/water**: not addressed in the folder.
8. **Colour state to model** (which paint, rust or not). Photos conflict.
9. **Grade and crossfall** not given. I assume flat on the river spans.
10. **Night lighting and bridge lamps not covered.** Night photos are listed but not saved ("Not downloaded").
11. **Rail/streetcar remnants**: none visible; no action.

## Handoff requests

| # | Request | Blocking? |
| --- | --- | --- |
| 1 | Find the deck elevation above sea level (and datum) for the east and west decks, or the deck height above the river at a stated gauge. Try City of Edmonton bridge inventory, drawings, Alberta bridge sheets, or LiDAR/DEM. If none, record the elevation read from the sim's own terrain at both abutments and mid-river. | Blocking for placement accuracy. Workable with the sim terrain as a fallback. |
| 2 | Truss depth (chord to chord) and out-to-out truss width for both spans, from drawings or from a photo with a known scale (e.g. a photographed vehicle or a lamp). | Blocking for correct profile. Can scale from photos if not found. |
| 3 | Pier height from footing to underside, pier plan size, and cutwater shape, for one pier. | Nice-to-have. Visible only close in. |
| 4 | Deck, roadway, sidewalk, and railing widths (m) for both bridges. | Blocking for the cross-section. Can be derived from the 23.4 m outline if the truss spacing is accepted. |
| 5 | Confirm whether the SB bridge truss centreline spacing equals 7.925 m, and the SB panel count and span lengths. | Nice-to-have. |
| 6 | Straight-on side elevation photo of EACH bridge separately (the existing elevation photos show the two in line). One photo of the deck end-on from each portal at road level. | Nice-to-have. Helps portal bracing and the clear height. |
| 7 | A top-down or high oblique photo showing both bridges and whether panel points line up along the axis. | Nice-to-have. |
| 8 | Which paint colour is current for each bridge in 2026 (grey-green vs rust-brown), with a dated photo of each bridge from the same angle. Note which side of underside-and-pier is which bridge. | Nice-to-have. |
| 9 | Texture refs: a close photo of truss member lattice, a close photo of the pier concrete, and road surface, for a PBR texture. Current photos are 1,920 px and give a usable base for sidewalk-plaque and underside-and-pier only. | Nice-to-have. |
| 10 | Check how the sim draws this site: do the sim's water and terrain polygons cover the pier bases? Does the sim already have an autogen or photogrammetry bridge here that would double up? Determine whether a water exclusion or a flatten is needed at the piers. Test in the sim. | Blocking before final placement. Cannot be answered from this folder. |
| 11 | Night lighting: roadway lamp spacing and colour, any bridge accent lighting. A night photo from the "Not downloaded" list would help. | Nice-to-have. |
| 12 | Collision and road-surface needs: confirm whether the decks must carry sim road/vehicle traffic or only a visual model. If a road must be drivable, request longitudinal grade and approach-ramp elevations. | Nice-to-have unless traffic or collision is required. |
| 13 | Gradient and tie-in elevations where McDougall Hill and Connors Road leave the decks. | Blocking if approach ramps are in scope; otherwise nice-to-have. |
