# R8 Groat Bridge: model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Reviewed from this folder only (NOTES.md, SOURCES.md, geometry.json, 6 photos).

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 616.2 m (2,022 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 616.31 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Main deck height** (`road_deck`, DSM median): 631.83 m, 15.52 m above the river. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** no usable night photo found (see `../../DATA-SOURCES.md`).

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions.** Plan position, heading, lane layout, east path and the material story are solid. Deck elevation, span lengths, pier count, girder depth and widths are all unpublished. A convincing silhouette for 1,000-3,500 ft is buildable. A close fly-by model is not dimensionally trustworthy. Deck elevation must come from the sim terrain probe, not from this folder.

## What the folder gives me

Plan (geometry.json, NOTES.md):
- Centre used by project: 53.537, -113.539 (NOTES.md). The mid-point of the mapped carriageways is about 53.53683, -113.53884 (my arithmetic from the node pairs). The "centre" is about 25 m off that. Use the node pairs, not the centre.
- East carriageway, northbound, way 22916458: (53.535607, -113.539669) to (53.538001, -113.537884). 291.5 m. 2 lanes, asphalt, layer 2.
- West carriageway, southbound, way 191843040: (53.538044, -113.538008) to (53.535654, -113.539794). 291.1 m. 2 lanes, asphalt, layer 2.
- Centreline separation: 9.8 m south, 9.5 m north (geometry.json).
- Plan bearing 23.9 deg east of north (NOTES.md). I rechecked it from both node pairs. It matches.
- East shared-use path, way 27265608: (53.535589, -113.53963) to (53.537976, -113.537834). Centreline 3.3 m east of the east road at the south end, 4.3 m at the north end.
- Outline ring, way 626069075, 11 nodes, `bridge:structure=beam`. North-end edge 22.1 m. Perimeter 627.4 m.
- Approach ways (47.8 m, 42.4 m south; 23.1 m north, plus longer continuations) are plan only. No grade (geometry.json).

Structure (NOTES.md, SOURCES.md):
- Girder bridge, 7 spans along the bridge, built 1955. Superstructure replaced 2018-2020. Piers kept.
- New superstructure: haunched steel plate girders, cast-in-place concrete deck, asphalt wearing surface (Graham). Girders weathering steel (DIALOG).
- Old superstructure: 6 cast-in-place concrete girder lines, rocking piers (Graham case study). Photos 2008, 2009, 2012, 2015 show the old one.
- Piers: concrete, mostly reused. New concrete collar at the base of 3 piers. Which three is unknown.
- Lanes: 4 (2 + 2). Posted 60 km/h. East path 4.2 m wide (was 2.4 m). A west walk exists in some form. Its width is not published.
- Length: 315.5 m (Wikipedia, Structurae), 315 m (City Archives), 1,000 ft (Graham page), 330 m (Graham case study), 291.5 m and 291.1 m (mapped centrelines).

From the photos (my reading):
- `deck-northbound-2023.jpg`: new deck at road level. Asphalt dark grey, white dashed lane lines, yellow edge line on the left. Solid light-grey concrete barrier on the west edge. A lower sloped concrete barrier between the lanes and the path. The path is pale concrete with a broom or groove finish. A galvanised steel pole railing with vertical pickets on the east edge, painted or weathered dark grey. A galvanised sign gantry with two signs and a lane-control light box. Curved-arm street lamps. One lamp is on the path-side barrier and one is tall and mid-road behind the gantry.
- `elevation-2026.jpg`: new superstructure, slim, shallow fascia, soft haunches over piers. Light concrete grey. Five piers in view, slender and round-looking, light grey. Interior span spacing looks equal.
- `elevation-2008.jpg`, `elevation-2012.jpg`, `elevation-from-river-2015.jpg`, `piers-2009.jpg`: old cream-beige concrete haunched girders. Stocky grey-beige piers. Dark band or stain at the waterline. Old lamps with banners, roughly at the pier lines in 2015.

## Build spec I would use from this alone

Everything marked (A) is an assumption, not from the folder.

Placement and orientation:
- Build one straight bridge along the bearing 23.9 deg east of north. Deck centreline runs from about (53.535630, -113.539732) south to (53.538022, -113.537946) north (mean of the two carriageway ends). Length along the line about 291 m for the roadway. (A) Make the structure 315.5 m with abutment and end wall extending beyond the road node ends, because both Wikipedia and Structurae agree on 315.5 m.
- Origin at the mid-point, about 53.53683, -113.53884. Local +Y along the bridge to the north-north-east. The glTF forward axis must be set to match the sim's convention.
- Deck elevation: unknown. (A) Place by probing the sim terrain/water at the two ends and the river surface. Keep the deck level or on a gentle crest (grade unpublished).

Components:
1. Deck slab. Two carriageways, 2 lanes each, separated by a gap with a median barrier. Centreline spacing 9.5-9.8 m. (A) Lane width about 3.5 m. Thickness unknown. Model a slab with a shallow fascia.
2. Median barrier. The two carriageways are tied by one deck (the 2023 photo shows a continuous deck). (A) Show a low concrete median barrier.
3. West parapet. Solid concrete barrier, light grey. (A) About 1 m high.
4. East path, 4.2 m wide, pale concrete. Centreline 3.3 to 4.3 m east of the east road centreline, so the path slowly diverges from the road by 1 m. Model it parallel and accept the error.
5. East barrier between road and path. Sloped concrete, lower than the west parapet.
6. East railing. Steel pickets, dark grey galvanised.
7. Overall width: (A) about 22 m. This is the mapped north-end edge of 22.1 m. A rough sum (west lane half, 9.7 m separation, path 4.2 m plus offset) gives about 20 m, so 22 m is plausible.
8. Girders. Haunched, deepest at piers, shallow at midspan, as in `elevation-2026.jpg`. Four to six lines would be hidden anyway. Model the fascia and soffit only. Depth not published. (A) Take proportions from the 2026 photo.
9. Piers. (A) Five in-channel piers plus one on each bank gives 6 supports, which matches 7 spans (the folder says 7 spans, not the pier count). Concrete, light grey. Dark band at the base. For 3 of them, add a wider concrete collar at the base (which three unknown, so pick the in-channel ones).
10. Abutments. End walls. Size unknown.
11. Sign gantry. Galvanised steel box frame with two green signs. Position along the deck unknown.
12. Street lamps. Curved single arm. (A) One per pier line.

Dimensions read from photos (ratios only, perspective error likely):
- Visible deck-to-water gap on the piers is about 0.25 to 0.3 of the adjacent span spacing in `elevation-2026.jpg` and `elevation-from-river-2015.jpg`. No absolute value in the folder. If the average span were 315.5 / 7 = 45 m (A, equal spans, not endorsed by the folder), that is about 11 to 14 m. Treat as a placeholder to be replaced by a measured value.
- Interior spans look equal in `elevation-2008.jpg` and `elevation-2026.jpg`. End spans are not visible in any frame.

Materials and colours:
- Deck: asphalt, dark neutral grey. White dashed lines, yellow left edge (2023 photo).
- Fascia, parapet, barriers, piers: light cool grey concrete (2026, 2023 photos).
- East path: pale concrete, a little lighter than the road.
- Railing, gantry: galvanised silver-grey, with dark grey weathered railing.
- Pier bases: dark stain band at the waterline.
- Do not use cream-beige. That is the removed 1955 superstructure.

LOD ideas:
- LOD0 (over 1.5 km): one box deck, one box fascia with haunch fakes, six simple piers. No railings. Colour baked.
- LOD1 (300 m to 1.5 km): add barriers, path, railing as a textured strip, haunch geometry, collars.
- LOD2 (close): pickets, lamps, gantry, lane-line texture, abutments.
- Keep road surface as a flat textured plane. Lane markings in the texture.

## Gaps and conflicts, ranked by harm to the model

1. **Deck elevation, soffit and clearance above the river are missing.** Without them the bridge floats or buries. The pier height cannot be set. Nothing in the folder converts to sim altitude. (geometry.json `deck_elevation_asl_m: null`.)
2. **Span lengths and pier count are missing.** Pier positions and rhythm are the most visible feature from the air. I inferred 5 in-channel piers from the 2008, 2012 and 2026 photos. 7 spans imply 6 supports. Not confirmed in any file.
3. **Length conflict.** 315.5 m, 315 m, 1,000 ft (about 305 m), 330 m, and the mapped 291.5/291.1 m. The folder explains they may be different extents and does not resolve them. A 25-40 m error moves the abutments off the banks.
4. **Girder colour conflict.** DIALOG says weathering steel. The 2026 photo (six years after opening) shows pale grey, not rust-brown. Either the fascia hides the girders, the girders are coated, or the photo is not showing steel. Colour choice depends on this.
5. **Pier shape unresolved.** The 2008/2009/2015 piers look broad and stocky with a dark base band. The 2026 piers look slender and round. The folder gives no plan size and no collar photo. This could be the viewing angle or the three collars.
6. **Deck width and cross-section missing.** Carriageway, lane, shoulder, west walk, overall, thickness and crossfall are all unpublished. 22.1 m is a mapped ring edge, not a structural width. The path offset (3.3 to 4.3 m) changes along the span, which suggests the deck is skewed or the mapping is loose.
7. **West walk contradiction.** Global News says "sidewalks" (plural). Other sources only describe the east path. Whether a west walk exists, and its width, is unknown. The 2023 photo shows a solid parapet on the west edge and no walk beside it, so I model none.
8. **Path surface conflict.** Graham says HPC. OSM says asphalt. The 2023 photo shows pale concrete. I use concrete.
9. **Minor conflicts in lane and speed tags.** way 25601745 is one lane and 50 km/h while its neighbours are two lanes and 60. Way 25601730 is one lane. The folder says no source states a lane drop. These are approach ways, not the model.
10. **"Two spans side by side" versus "seven spans."** Explained in NOTES.md (two carriageways versus seven spans). Resolved, but note it for anyone who reads Wikipedia.
11. **Abutments, end walls, bearings, wing walls missing.** Bridge ends will be guessed.
12. **Photos are mostly side elevations from far away.** No underside view, no close pier detail, no end view, no approach photo showing the grade.

## Handoff requests

Blocking:
1. **Deck elevation and river surface elevation.** Ask for one number set: deck top at both ends and mid-span, soffit at the piers, normal water level, all with a stated datum, ideally as ASL metres. If no published source, say the researcher should sample the sim's own terrain at the bridge ends and the river and record the numbers. Blocking.
2. **Pier count and positions along the bridge.** A researcher with the City bridge file, a drawing, or a clear aerial photo should give the distance from the south end to each pier and to each abutment. Aerial or satellite imagery would do. Blocking.
3. **Real end points of the structure.** One measured length, end to end, abutment to abutment, with a note on what the 291.5 m node lines exclude. Blocking.
4. **Sim terrain and water interaction.** Check in the sim whether the terrain mesh and the river surface cover the pier bases (the piers stand in water, as in all six photos). Report whether the water is flat at a fixed level and whether the mesh clips or floods the piers. Ask whether the sim already has a Groat Bridge (photogrammetry or generated bridge) that needs to be excluded or hidden. Blocking.
5. **Girder and fascia colour after 2020.** One close or mid-range colour photo of the underside or the fascia, taken after 2020, in daylight, to settle weathering steel versus grey. Blocking for a close-range model, nice-to-have above 1,000 ft.

Nice-to-have:
6. **Cross-section.** A deck cross-section drawing or measured widths (lane, median, parapet, path, overall) and the crossfall. Nice-to-have. Without it I use 22 m total and 3.5 m lanes.
7. **Girder depth and haunch profile.** A side elevation with a scale reference, or a figure from the DIALOG or Graham design drawings. Nice-to-have.
8. **Pier photos after 2020.** One close photo of the pier shaft from a boat or the bank, showing a collar. Plan size and which piers have collars. Nice-to-have.
9. **End views.** A photo along the deck from each end, and one from below at the abutment. Nice-to-have.
10. **West walk.** A photo or measurement of the west edge to confirm there is no walk. Nice-to-have.
11. **Lamp spacing and type.** Count of lamps along one side, position of the sign gantry along the deck. Nice-to-have.
12. **Night lighting.** `lit=yes` appears only in the live OSM read (NOTES.md). No colour (sodium or LED) is recorded. A night photo would settle the lamp colour. Nice-to-have.
13. **Road surface and collision.** Decide whether the model carries a road surface the sim can drive on, and whether the sim's own road layer already runs over this bridge. If it does, hide it or match it. Nice-to-have unless the user wants ground traffic.
14. **Grade at the approaches.** Where each road meets natural grade and the elevation change. The folder says no source was found. A sim terrain sample would do. Nice-to-have, but it decides how long the approach ramps must be.
