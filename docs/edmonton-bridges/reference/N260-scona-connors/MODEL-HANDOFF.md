# N260 Scona Road Bridge (B065) - model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Reviewed from this folder only: NOTES.md, SOURCES.md, geometry.json (decks, approaches, first part of ramps), three photos.

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 625.4 m (2,052 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 613.66 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** no usable night photo found (see `../../DATA-SOURCES.md`).

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Blocked for a faithful model. Ready only as a placeholder.** The folder has a good plan position and heading for one 50.4 m deck. It has no deck type, width, elevation, clearance, pier data, or usable photo of the span. The notes themselves say the three photos show other structures. I could only build a generic slab bridge. That is a guess, not a model.

## What the folder gives me

| Fact | Source |
| --- | --- |
| Name: Scona Road Bridge, B065, Scona Road over Connors Road. Not a Low Level deck. Not an R code. | NOTES.md "Name", geometry.json `name_note` |
| Built 1957. Minor rehab planned (start 2025 per inventory, 15 Jan 2024 per tender). Whether built, and what changed: unknown. | NOTES.md "Year", SOURCES.md |
| Centre 53.533941, -113.483610 (EPSG:4326, lat/lon). | geometry.json `centre` |
| Deck centreline way 22959547: 2 nodes, (53.5337467, -113.4838053) to (53.5341356, -113.4834149). Plan length 50.4 m, straight. | geometry.json `decks[0]` |
| Deck tags: 2 lanes, one-way, asphalt, 50 km/h, layer 1, expressway, no maxheight, no width, no bridge:structure. | geometry.json `decks[0].tags` |
| Travel direction on the deck: south (uphill) end to north (downhill). So Scona traffic goes down the hill, toward the river. | NOTES.md "Bridge", geometry.json |
| Road under it: Connors Rd way 34388889, one-way, eastbound, not bridge-tagged, no lanes tag, no maxheight. Crosses in plan, no shared node. | NOTES.md, geometry.json |
| Approach polylines with node coordinates and plan lengths: Scona NB 345.9 m and 103.8 m, Scona SB (ways 1415752722, 693125057, 472624621/22, 112188681), Connors EB 219.1 m and 269.7 m, Connors toward river 67.5 m and 73.5 m, loops and ramps. Lane counts per way. | geometry.json `approaches`, `ramps` |
| Neighbouring bridge-tagged ways (not B065): Connors over ramp (34388891, 42.7 m); 98 Ave WB (22916470, 76.3 m, 3 lanes, width tag 11.1); 98 Ave EB (106711204, 81.1 m, 2 lanes); ramp (106711230, 81.3 m). | geometry.json `decks[1-4]` |
| Horizontal distance from B065 midpoint to the south end of the SB Low Level deck: 404.2 m. To the 98 Ave WB midpoint from the truss node: 138.1 m. | NOTES.md "What reads from the air" |
| Rough look of the area: concrete overpass beyond the truss, roads under and beside it, loops, treed hill behind. | photos `overpass-beyond-south-end.jpg`, `interchange-and-hill.jpg` |

**Conflicts inside the folder**
- B126 crosses "Scona Road" (inventory) or "Connors Road" (tender, league page). NOTES.md reports both. Only matters for 98 Ave.
- Tender start 15 Jan 2024 vs inventory start 2025. Reported, not resolved.
- NOTES.md says the Scona span is "on the south slope" and 404 m from the truss. The photos from the north show an overpass "immediately beyond the truss" (138 m). The notes say that one is 98 Ave, so no true conflict, but a viewer will mix them up.
- Heights: maxheight 4.3, 4.6, 6.1 are on other Connors ways. The notes say not to use them. I will not.

## Build spec I would use from this alone

Derived from geometry.json. Heading and offsets are my calculation.

**Placement**
- Origin: centre 53.533941, -113.483610.
- Deck axis: node 1 to node 2 is about 43.3 m north and 25.9 m east. Length 50.4 m checks. True bearing about 031 degrees (direction of travel, downhill). Model axis along that line. Mirror it for the 211 degree view.
- Elevation: unknown. The deck sits on a slope. Use the sim's terrain height at the centre as the base and set deck height as a variable. No value is in the folder.

**Components (all dimensions are assumptions, flagged)**
1. Deck slab, 50.4 m long. Width unknown. Two lanes plus shoulders, I would guess 10 to 12 m as a placeholder. Thickness unknown. Placeholder only.
2. Parapets or barriers on both sides. Type unknown.
3. Abutments at both ends. Form unknown.
4. Piers: count unknown. Placeholder is none (single span), because the way is one straight segment. The notes say that is not a span count.
5. Approach road surface: use the polylines above, but at one grade the roads cannot pass over each other. Needs elevations.
6. Lane markings: 2 lanes, one-way. Edge lines. Nothing in photos shows this span's markings.

**Materials and colours**
- Deck type is unknown. The photos show concrete decks at the valley floor (98 Ave). Concrete grey is likely for the structure but is not confirmed for B065. Asphalt dark grey (tag: asphalt).
- Photo `overpass-beyond-south-end.jpg`: light grey concrete, steel-sided deck edge. Photo `interchange-and-hill.jpg`: concrete bridge with pale grey fascia and dark rail. Neither is B065 per the notes.

**LOD ideas**
- At 1,000 to 3,500 ft AGL, a 50 m deck is a thin grey bar. One mesh, one road texture, no detail.
- Close fly-by: add parapets, a pier or abutment wall, and lamp posts. Lamp posts: `lit: yes` is on the Connors bridge 34388891, not on this deck.
- Do not model the 98 Ave spans here. NOTES.md assigns them to the Low Level south end.

## Gaps and conflicts (worst first)

1. **No photo of the span.** The three photos show 98 Ave or a distant view. `span-from-south-slope.jpg` is a skyline shot; the span is a tiny strip in the middle distance and the notes say it was not identified as B065. I cannot read type, piers, rails, or colour from any of them.
2. **No deck elevation or clearance.** No vertical datum, deck, soffit or road elevation. Without it I cannot set height above Connors Rd or the terrain. This is the biggest geometry risk for terrain clipping.
3. **No deck type, pier or abutment data.** Slab, girder, or other: unknown. The look at close range is a guess.
4. **No width.** Lane count is 2 but lane width, shoulders, barriers and sidewalks are missing.
5. **No grade or crossfall.** The span is on a slope. Plan lengths only.
6. **Rehab status unknown.** The 2024/2025 work may have changed railings or deck.
7. **Identification risk.** The 98 Ave overpass is the one seen from the north. A later pass could model the wrong bridge.
8. **Terrain interaction not addressed.** The notes do not say whether the sim terrain, or the existing Low Level model, overlaps this area.
9. **Night lighting, collision, road surface type** not addressed.

## Handoff requests

| # | Request | Blocking? |
| --- | --- | --- |
| 1 | A ground-level or oblique photo of B065 itself, from Connors Road (looking at the soffit and abutments) and along Scona Road (deck, rail, markings). Say the direction and the date. Check they are not the 98 Ave spans. | Blocking |
| 2 | Deck elevation, soffit elevation, and Connors road elevation under the span, in metres ASL, with datum. Sources: City of Edmonton LiDAR / DEM, or the sim's terrain at the site. Also the terrain elevation at both Scona end nodes. | Blocking |
| 3 | Deck width, lane width, shoulder and barrier type for B065. A City inspection sheet or drawing, or a scaled photo. | Blocking |
| 4 | Deck type, span count, pier and abutment form for B065. | Blocking for close-up, nice-to-have for 1,000 ft+ |
| 5 | Longitudinal grade on the span and approaches (from item 2). | Nice-to-have |
| 6 | Was the 2024/2025 rehab built? What changed (rails, deck, paint)? Check City project page or a recent photo. | Nice-to-have |
| 7 | Colour reference for the concrete and rails under daylight. A close photo, not a distant one. | Nice-to-have |
| 8 | Terrain question: in the sim, does terrain at this location sit above the deck (clipping) or below? Check in sim with a placed test box. Also check overlap with the 98 Ave / Low Level south-end model. | Blocking before placing |
| 9 | Night lighting: are there lamp posts on the deck? Photo or street-view check. Tag `lit` is on neighbouring ways only. | Nice-to-have |
| 10 | Decide whether roads on the approaches need collision and a drivable surface or are decoration only. | Nice-to-have |
| 11 | Confirm which bridges the project should include: the notes say N260 also covers 98 Ave spans and Connors over the ramp. Confirm who models those, so none are doubled or dropped. | Nice-to-have |
