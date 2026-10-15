# Z125 Wellington Bridge — model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 653.3 m (2,144 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface:** this clip holds no river reach, so no water figure applies. For a ravine or rail crossing use the ground heights above and below.
- **Main deck height** (`road_deck`, DSM median): 664.35 m. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** no usable night photo found (see `../../DATA-SOURCES.md`).
- **Street-level photos:** none (no Mapillary frame within 250 m).

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions (plan-view massing only).** Position, heading, plan length and approximate plan width come from geometry.json. Span type is known (single clear-span girder). Deck elevation, ravine depth, girder depth, width and material are not in the folder. There are no photos (SOURCES.md: "Photos saved: None"). I can build a plausible low-detail girder deck. I cannot build a faithful ravine crossing or a close fly-by model.

## What the folder gives me

| Fact | Value | From |
| --- | --- | --- |
| Centre | 53.5431, -113.5481 | geometry.json `centre` |
| Type, finished | Clear-span girder, one span, no piers | NOTES.md; geometry.json `dimensions` |
| Girder material | Unknown: steel (Option A) or NU2400 concrete girder (Option B). No award found | NOTES.md; SOURCES.md (ConstructConnect) |
| Old bridge (being removed) | 1932 three-span concrete arch, 4 lanes, sidewalk each side | NOTES.md; SOURCES.md (City) |
| Status 2026-10-14 | Under construction, completion "end of 2026", landscaping 2027 | NOTES.md |
| Road deck centreline (way 37749246) | (53.543048, -113.548582) to (53.543047, -113.547489), 72.3 m, node order west to east | geometry.json `decks[0]` |
| North MUP (way 842281120) | (53.543112, -113.548514) to (53.543109, -113.547411), 73.0 m | geometry.json |
| South way (845134789) | 3 nodes, lat about 53.54298, lon -113.548527 to -113.547488, 68.7 m | geometry.json |
| Outline ring (1227946189) | corners (53.543118,-113.548575), (53.543121,-113.547509), (53.542972,-113.547508), (53.542969,-113.548574). Long sides 70.5 m, short sides 16.6 m | geometry.json `decks[3]`, `dimensions.outline_edge_lengths_m` |
| Layer | 1 (all bridge parts) | geometry.json tags |
| Lanes / speed | 4 lanes, 50 km/h | geometry.json tags |
| Out-to-out width | 23.78 m (April 2024 preliminary, not for construction; later "to be reduced") | NOTES.md; SOURCES.md |
| Right-of-way | 30.6 m | NOTES.md |
| Path widths | North shared path 4.2 m, south sidewalk 2.8 m (2023 arch-era proposal) | NOTES.md |
| Crossfall | 2.5 %, then 4.0 %, then parabolic crown over 10 to 15 m (preliminary drawing) | NOTES.md |
| Finished furniture | Barriers, handrails, decorative streetlights, "some historical elements at roadway level" (unspecified) | NOTES.md; SOURCES.md |
| Approach ways | W: 9.1 m, width tag 14. E: 113.3 m, width tag 15, asphalt, bicycle designated. North MUP stubs 11.1 m (W) and 9.4 m (E) | geometry.json `approaches` |

### Conflicts inside the folder

- Width: OSM tag 12.4 m, outline short side 16.6 m, approach tags 14 and 15 m, drawing 23.78 m. NOTES.md says none were reconciled. Four lanes at 12.4 m is also tight.
- Length: 70.5 m (outline), 72.3 m (road), 73.0 m (MUP), 68.7 m (south way). Spread of 4.3 m. None is a structural span.
- Year: 1932 (City) vs 1910 (Alberta). Irrelevant to the finished model.
- Bridge number: B003 vs B499. Not merged.
- Ravine name: Ramsey / Ramsay / Wellington / Groat. Irrelevant to geometry.
- Path widths 4.2 + 2.8 are from the arch scheme and the 23.78 m is from a different scheme. They may not apply to the girder.

## Build spec I would use from this alone

Frame: local origin at the road centreline midpoint (about 53.543048, -113.548036). X axis east. Heading about 90 degrees true (east-west; the two road nodes differ by 0.000001 deg of latitude). Y up. Z north.

Components:

1. **Deck slab.** 72.3 m long (road centreline) by an assumed width. Use 16.6 m (outline short side), since it is the only width tied to a mapped bridge outline. Thickness: not given. I would use a placeholder and mark it assumed.
2. **Girders under the deck.** One clear span, no piers. Girder count, depth and spacing are not given. Build a plain underside with 2 to 3 shallow, dark beams, flat at the ends. Mark the depth as assumed.
3. **Abutments.** Not described. Build simple concrete blocks at each end, the deck length less nothing, since the ravine slope is not given.
4. **Road surface.** 4 lanes asphalt, centred. Crossfall 2.5 % each way as a crown (the drawing's 4.0 % and parabolic part skipped for LOD).
5. **North shared path.** 4.2 m concrete, on the north side. Mapped MUP lies about 7 m north of the road centreline.
6. **South sidewalk.** 2.8 m concrete, on the south side. Mapped south way lies about 7.5 m south of the centreline.
7. **Barriers and handrails.** Both edges. Height not given.
8. **Streetlights.** Decorative, both sides. Spacing and style not given. Place as simple poles.
9. **Approach stubs.** 9.1 m west, and some east length. Short, to blend into terrain.

LOD ideas: LOD0 (over 2,000 ft) deck, abutments, rails as one mesh. LOD1 adds girders, lights and lane marks. Close fly-by is not supportable without more data.

Materials and colours: no photo, so none read from photos. Defaults: light grey concrete for deck edges, barriers and abutments; dark asphalt for the road; grey concrete for paths; steel grey for rails if steel, or light grey concrete girders if NU2400. All assumed.

Elevation: not published (geometry.json `deck_elevation_asl_m` is null; `clearance_to_ravine_m` is null). I cannot set the deck height or the abutment height. Layer 1 only says it is above grade.

## Gaps and conflicts (worst first)

1. **No deck elevation or ravine depth.** The model would float or bury. Biggest risk.
2. **No width for the built girder.** Range is 12.4 to 23.78 m.
3. **No photos at all.** No colour, shape, rail style or historical elements.
4. **Girder type unknown** (steel or NU2400). Changes the underside look and colour.
5. **No girder depth, deck thickness, barrier height, abutment form.**
6. **Span length is the mapped road line (72.3 m), not structural.** Abutment setback unknown.
7. **Historical elements and light style undefined.**
8. **Construction state.** Whether to show finished or under-construction is not stated for the sim date. NOTES.md says to model the finished girder.
9. **Terrain interaction** not addressed in the folder.

## Handoff requests

| # | Request | Blocking? |
| --- | --- | --- |
| 1 | Deck elevation (ASL) at both ends, plus ravine floor elevation under the span, from a DEM or LiDAR. State the datum. | Blocking |
| 2 | Girder-design out-to-out deck width (revised after August 2024), from City drawings or tender documents. | Blocking |
| 3 | Any photo of the new girder or construction progress with a usable licence, ideally one side elevation and one from below. If none, an own-photo or screenshot with reuse permission. | Blocking for close views; nice-to-have for high altitude |
| 4 | Whether the girder is steel or NU2400 concrete, and girder depth, deck thickness. | Nice-to-have (needed for close views) |
| 5 | Abutment type and where they sit relative to the ravine rim. | Nice-to-have |
| 6 | Barrier and handrail height and style, and what the "historical elements at roadway level" are. | Nice-to-have |
| 7 | Streetlight style and spacing. Also night-lighting intent (emissive heads, colour). | Nice-to-have |
| 8 | Ground check: does the sim's default terrain or photogrammetry cover the ravine and old arch? Check in the sim whether terrain clips the span, and whether a flatten or exclusion polygon is needed under the bridge. | Blocking before placement |
| 9 | Confirm the road surface needs: collision on deck and paths, and whether the way is gameplay-driveable (the OSM way is closed, `highway=construction`). | Nice-to-have |
| 10 | Which state to model on the sim date (complete or under construction) and whether the old arch should be shown or hidden. | Nice-to-have |
