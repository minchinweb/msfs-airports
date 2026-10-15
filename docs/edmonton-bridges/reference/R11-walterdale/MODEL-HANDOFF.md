# R11 Walterdale Bridge: model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 614.2 m (2,015 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 614.21 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Main deck height** (`road_deck`, DSM median): 628.93 m, 14.72 m above the river. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** 2 photos in `night/` with a lighting description in `night/SOURCES.md`.
- **Street-level photos:** 4 daytime Mapillary frames in `street/` (CC BY-SA, credits in `street/SOURCES.md`). They show railings, barriers, lamp posts, lane and sidewalk layout and approach shape from the road; not the underside or truss depth. Check them before treating those items below as open.
- **Open questions:** the other session's review (`CURSOR-HANDOFF.md`) re-checked against this data, item by item, in `OPEN-QUESTIONS.md`. Read it before the blocking items below.

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions.** The plan shape, span, arch form, hanger layout, deck width and colours are all usable. The vertical position (deck elevation above sea level) is missing, and the arch rise has four conflicting figures. Neither blocks a 1,000-3,500 ft model, but the elevation must be fixed before placement.

## What the folder gives me

Source tags: N = NOTES.md, S = SOURCES.md, G = geometry.json, P = photo.

**Plan and placement**
- Centre 53.529, -113.502, EPSG:4326 [lat, lon] (G, N).
- Road deck centreline, OSM way 175326660, south to north: 53.527264,-113.502281 / 53.529377,-113.501183 / 53.529505,-113.501139 (G). Plan length 260.7 m.
- Heading from the end nodes (my arithmetic, not in the folder): about 17 deg east of north. It is near straight (three nodes). The 2012 study's "15 deg skew eastward" (N, S) is consistent with this but is a planning figure.
- West sidewalk, way 709287392, 26 nodes, 266.8 m (G).
- East shared-use path, way 451293733, 22 nodes, 275.4 m, runs north to south, curved in plan, bowing east of the road (G, P deck-and-south-approach, P elevation-from-south-bank).
- North approach road, way 471835847, 112.3 m, 5 lanes (G). South approach, ways 931254808 + 1516540140, 31.3 m + 19.0 m, 3 lanes (G).
- Direction: northbound one-way, 3 lanes, 50 km/h (G, N). Sidewalk on the west, path on the east (N, P).

**Structure**
- Structural length 230 m between abutment centrelines; arch span 206 m bank to bank (N, S: 2014 paper, 2019 award, Pedelta, DIALOG).
- Twin through-arch, thrust arch, no tie, no pier in the river (N, P elevation-from-high-level, P underside-no-river-pier).
- Ribs: steel box, 2.5 x 2.5 m at base tapering to 1.4 x 1.4 m at crown. Plate 100 mm to 75 mm. 21 segments per rib. Curved between splices, not faceted (N).
- Ribs lean inward, 13.5 deg from vertical (N; Lima says about 14).
- Struts between the ribs above the roadway; count not given (N). Photos show roughly 8 to 9 per arch pair, tapered and "fish-belly" shaped, thick at the ribs and thin in the middle (P north-end-toward-downtown, P struts-from-north-bank, P arch-and-hangers-southwest). The count is my reading of the photos only.
- Hangers: road deck 2 planes x 16 = 32, 10 m centres (N, G). Shared-use path plane: 16 (Pedelta) or 14 (City 2016). Hanger is a cable in a pipe, fixed at the top, adjustable at the bottom (N).
- Thrust blocks: 4, buried. Above grade is a concrete support leg, inclined, with a row of anchor bars (N, P thrust-block-support-leg). Footing 9 x 10.5 m (2019 award); other sources differ.
- Gap between road deck and path: 8 m to 2 m, narrowest at mid-span (N: Lima).
- Delta piers (V-shaped, concrete) carry the path near the banks, on the riprap, not in the channel. Count not given (N, P elevation-from-south-bank, P underside-no-river-pier).
- Abutments: concrete wall with bearings, gabion walls stepping down to the bank (N, P abutment-flood-markers).

**Deck**
- Traffic deck 22.4 m wide (Pedelta, ACCIONA Australia); 22.5 m in the ACCIONA article. Includes 3 lanes, 2 shoulders, barriers and the west sidewalk (N).
- Path girder: trapezoidal steel box, 1.4 m deep (N). Clear width 8 m at the banks, 4.2 m near mid-span (N); City says up to 9 m at the ends.
- Bench along the middle 50 percent of the path, west side, solid back (N).
- Road deck build-up: concrete slab on steel stringers and floor beams, box edge girders, asphalt on membrane (N, P underside-no-river-pier).
- Mid-span height above water 13.3 m (N, S: 2013 yearbook diagram), datum and reference point unknown.

**Conflicts inside the folder**
- Arch rise: 56 m above thrust blocks; 43 m above deck (yearbook, Lima, ACCIONA AU); 40 m above roadway (2019 award); 54 m above river (City 2015/2016, Pedelta); 55 m above river (Lima, ACCIONA AU); ACCIONA article also says 54 m from the deck. Deck-to-crown ranges 40 to 54 m.
- Deck width 22.4 vs 22.5 m. Minor.
- Path hangers 16 vs 14. Minor.
- Path width at ends 8 m clear vs 9 m. Minor.
- Thrust block 600 m3 / 20 m below road vs 400 m3 / 15 m. Buried, irrelevant to the model.
- ACCIONA AU puts walkway and path on swapped sides. Folder uses the designer's layout. Photos agree with the designer: path east, curving away.
- OSM road way 260.7 m vs structural 230 m. The folder says the extra is likely pavement past the abutments. Unconfirmed.
- OSM tags path and sidewalk as concrete; design says polymer asphalt on the path.
- OSM tags the north way as 5 lanes and the south ways as 3 lanes, but the City says Walterdale Hill was narrowed to 2 lanes from 109 Street north. Approach lane counts are unreliable.

## Build spec I would use from this alone

**Coordinate frame.** Local origin at the road centreline mid-node region near 53.529, -113.502. Axis along the deck at about 17 deg east of north. Take the road-deck way nodes as the plan line; derive plan offsets of the path and sidewalk from their own ways, not from nominal widths.

**Components**
1. Road deck: 22.4 m wide ribbon along the way, 230 m long between abutment centrelines. Slab plus asphalt top, concrete parapet band on each edge, white-painted steel edge girder below (P hangers-over-open-river). Thickness: ASSUME about 1.5 to 2 m total depth visible edge girder (not in the folder; scale from P hangers-over-open-river and P underside-no-river-pier). Flag as an assumption.
2. West sidewalk: inside the hanger plane, on the road deck edge, width ASSUMED (not published).
3. East shared-use path: separate curved box girder following way 451293733. Width tapers 8 m at banks to 4.2 m mid-span. Girder 1.4 m deep. Light colour steel soffit, railing along both edges (P deck-and-south-approach, P underside-no-river-pier). Joins road level at both ends.
4. Arch ribs: two, each 21 curved segments, box 2.5 m tapering to 1.4 m, leaning inward 13.5 deg. Span 206 m. Crown height: ASSUME 43 m above deck unless the researcher resolves it (see gaps). Lean means feet are wider apart than the crown; set rib-to-rib spacing from the plan photo, because no centre-to-centre figure exists.
5. Struts: about 8 to 9 tapered struts between ribs, above the roadway only. Number ASSUMED from photos.
6. Hangers: 16 per plane x 2 road planes at 10 m centres, plus 14 or 16 on the path plane. Thin cylinders, about 0.15 to 0.2 m diameter (ASSUMED; no diameter in the folder). Silver-white. Hangers are near vertical in the side elevation (P elevation-from-high-level) and look crossed only because of oblique view.
7. Support legs and thrust-block caps: four inclined concrete legs, about 10 m across (N: "10 m across", ambiguous), arch box lands on a row of black-capped anchor bars (P thrust-block-support-leg). Buried part not modelled.
8. Delta piers: V-shaped concrete piers on the riprap bank, under the path girder (P elevation-from-south-bank, P underside-no-river-pier). Two visible at each end in P elevation-from-south-bank; count not published.
9. Abutment walls: concrete block under each deck end with bearings, light grey, with horizontal flood-line bands and "1915" / "1986" text (optional) (P abutment-flood-markers). Gabion walls beside them.
10. Light poles: slim curved poles along the road, inside the hanger plane (P hangers-over-open-river, P arch-and-hangers-southwest).
11. Approach ramps: short stubs of road at both ends, merging into the sim's road network. Lengths not published; use the OSM ways as the limit.

**Materials and colours (from photos)**
- Arch ribs, struts, deck edge girders: bright white to very light grey paint, smooth (all elevation photos).
- Hangers: silver-white, matte-metallic pipe (P hangers-over-open-river).
- Underside steel and path soffit: pale grey-green/grey (P underside-no-river-pier).
- Concrete (legs, abutments, delta piers, parapet): mid-light grey, slightly warm (P abutment-flood-markers, P thrust-block-support-leg).
- Anchor caps: black (P thrust-block-support-leg).
- Railings: light metal, vertical pickets (P deck-and-south-approach).
- Road: dark grey asphalt, painted lane lines visible (P deck-and-south-approach).
- Ground at the banks: riprap (grey boulders) and gabion (wire-mesh stone) (P underside-no-river-pier, P abutment-flood-markers).

**LOD**
- LOD0 (over 2 km): two ribs as swept boxes, deck slab, path ribbon, hangers as a textured plane or thin lines. Under 5k triangles.
- LOD1 (500 m to 2 km): add struts, delta piers, legs, parapets, individual hangers.
- LOD2 (under 500 m): add railings, light poles, bearings, flood text, anchor bars, soffit beams.
- Hangers need alpha-card or very low poly cylinders from altitude; they are thin (see P elevation-from-high-level).

**Placement**
- Heading: align the deck to the OSM way (about 17 deg east of north). Verify against imagery in-sim.
- Elevation: not available. The folder has no ASL deck height, no datum, no water level. Use the sim's terrain/water height at the site as the basis, with deck about 13.3 m above water at mid-span (ASSUMPTION: the diagram label may be to the roadway or the soffit).
- Arch feet at bank level; abutments set into the bank on both sides; the north bank is higher than the south (N: DIALOG), amount unknown.

## Gaps and conflicts, ranked by harm to the model

1. **No deck elevation or water level (ASL, datum).** Placement can be off by metres, and the bridge can float or sink relative to the sim's terrain. Highest risk.
2. **Arch rise conflict (40, 43, 54, 55, 56 m).** Spread of up to about 14 m in the crown height. Visible silhouette from any altitude.
3. **No rib-to-rib spacing at the crown or at the feet.** The inward lean (13.5 deg) is known but the base spacing is not. Controls the whole look of the arch.
4. **Deck thickness, edge girder depth, parapet height, crossfall, grade missing.** Affects the side silhouette and the approach joins. Approach gradients also unknown, so the ends may not meet the sim's roads.
5. **Strut count and spacing, and delta-pier count, not published.** Visible in close fly-bys.
6. **Approach lengths and where the roads meet grade.** OSM ways are clipped, and lane counts are unreliable.
7. **Path width taper is only given at two points (8/4.2 m).** Use the OSM polyline for the plan curve; the intermediate widths are unknown.
8. **Lane, shoulder and sidewalk widths missing.** Only needed for the lane markings in close views.
9. **Hanger diameter, hanger count on the path (14 vs 16), light pole spacing.** Small.
10. **No aerial or orthophoto.** There is no top-down check of rib spacing, path curve or plaza shapes.
11. **Photos are ground-level, mostly sunlit.** No night or lit view, except P struts-from-north-bank, which shows a faint lit-rib edge.

## Handoff requests

Each is something a researcher can act on. B = blocking, N = nice-to-have.

1. **B.** Find a deck elevation above sea level (and datum) for the road at mid-span and at each abutment, or a surveyed river water level at this site. Likely sources: Alberta Transportation bridge file, City of Edmonton drawings, LiDAR / DEM. Also state whether the 13.3 m is to the roadway or the soffit.
2. **B.** Pick one arch rise: find a drawing or elevation with the crown height above the deck and above the arch foot. Check which of 43 / 40 / 54 m is from deck to crown. A dimensioned side elevation would settle it.
3. **B.** Find the rib-to-rib centre spacing at the crown and at the feet (a plan or section drawing, or a measurable top-down image).
4. **B.** Ask how the sim's terrain and water interact: check in-sim whether water height at the site is above the arch feet or delta piers, and whether terrain at the banks is high enough to hide the legs and abutments. Whether the sim's default Edmonton photogrammetry already has this bridge (and needs to be excluded) must be checked in the sim, not from this folder.
5. **N.** An openly licensed aerial or satellite view, straight down, of the bridge and plazas. It confirms plan heading, path curve, the ends and the approach shape.
6. **N.** Photos needed: (a) straight side elevation with a known-size object, (b) end-on elevation along the deck axis showing rib lean and strut spacing, (c) close shot of the road section with lane lines, barrier, sidewalk and hanger plane, (d) the path and bench, (e) light poles and railings close up, (f) the support leg from the front (water side), (g) the bridge at night.
7. **N.** A count of struts and delta piers, from a drawing or by counting in a clear photo (an end-on or elevation image in full resolution).
8. **N.** Deck thickness, edge girder depth, parapet height, crossfall. A section drawing from the 2014 paper or the award PDF figures (not extracted; S says so) is the likely source. Extract those drawings.
9. **N.** Approach grade: gradient and length for 105 Street north and Walterdale Hill south, or elevations at the clipped OSM end nodes.
10. **N.** Colour reference: a calibrated colour or paint spec for the white steel (e.g. RAL) and the concrete. Folder only has photographs under varying light.
11. **N.** Night lighting: whether the arches are lit (P struts-from-north-bank suggests rib-edge lighting), light colour, and pole positions, for emissive materials.
12. **N.** Collision and road surface: whether the sim needs a drivable road surface for ground traffic or only a visual model, and whether the lanes and the path need separate collision. The folder cannot answer this.
13. **N.** Lane, shoulder and west sidewalk widths.
