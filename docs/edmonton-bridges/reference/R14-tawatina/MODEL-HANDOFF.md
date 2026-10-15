# R14 Tawatina Bridge - model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Reviewed using only this folder: NOTES.md, SOURCES.md, geometry.json, and all 9 photos.

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 613.4 m (2,012 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 613.26 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Main deck height** (`lrt_track_west`, DSM median): 628.19 m, 14.93 m above the river. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** no usable night photo found (see `../../DATA-SOURCES.md`).

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions.** Plan position, span layout, widths, girder depth, pylon form, stay layout, path form, materials and colours are all covered well enough to build the river bridge and the south guideway. There is no deck elevation, no datum and no pylon survey. The model can be built at correct plan position and proportion. Its absolute height above the river is a guess until someone supplies elevation.

## What the folder gives me

Each item says where it came from.

**Plan and placement**
- Centre 53.5401, -113.4772 (NOTES.md; geometry.json `centre`).
- Tracks run almost due north-south. West track lon goes -113.477159 to -113.477171 over the river piece, about 0.8 m of drift over 160 m. Heading is about 180 deg true (geometry.json, my arithmetic).
- Bridge-tagged length 471.5 m (west) and 473.5 m (east), from 53.541573 to 53.5374 (NOTES.md; geometry.json `dimensions`).
- River bridge 260 m, three spans: 100 m, 110 m, 50 m (NOTES.md; thesis, American Bridge, Wikipedia, IABSE).
- The OSM ways split exactly where the spans fall. Way 636427023 is 100.4 m, from 53.541573 to 53.540671. Way 1221895803 is 160.5 m, from 53.540671 to 53.539229 (geometry.json). That 160.5 m equals 110 m plus 50 m.
- So the north river pier, which carries the pylons, is at about lat 53.540671 (derived).
- The south river pier is 110 m further south, about lat 53.53968 (NOTES.md says "may sit 110 m south"; latitude is my arithmetic).
- The south-bank pier is at about lat 53.539229, 160 m from the north pier (NOTES.md; geometry.json).
- South elevated run: 210.6 m (west) and 212.7 m (east), still bridge-tagged, from 53.539229 to 53.5374 (geometry.json).
- That run goes straight (lon about -113.4772) to about 53.5386. It then bends south-west. The last nodes are 53.537415, -113.477787 (west) and 53.537395, -113.477728 (east), a bearing of about 218 deg (geometry.json; bearing is my arithmetic).
- The guideway ends at the Muttart ramp. The bridge tag stops at 53.5374. The stop is at 53.53621, -113.48000 (NOTES.md).
- Track spacing is not stated. OSM nodes give about 3.7 m to 5.4 m centre to centre (my arithmetic, noisy). The thesis load lanes are offset 2,250 mm from the deck centre, which implies about 4.5 m. I would use 4.5 m. This is an inference.
- Path (way 732161091) runs 53.539384 to 53.541098, 190.8 m, lon -113.477135 to -113.477119, centred under the box (geometry.json). It sits 47.5 m north of the north pier and about 143 m south of it (my arithmetic).
- Path stops about 17 m short of the south-bank pier node (my arithmetic). It does not continue over the south guideway (NOTES.md; geometry.json).
- 98 Avenue carriageways pass under the guideway near 53.5378, -113.4775 to -113.4778 (geometry.json `cross_roads`).

**Cross-section and structure**
- Box girder: trapezoidal, 3.5 m deep, 11 m wide, concrete (NOTES.md; thesis, Structurae). Sides slope at most 1:2 (agreement).
- Pylons: two, on the north river pier, no member joining them above the deck (NOTES.md; agreement 2-11.5.3).
- Pylon height above deck: 24 m to 30 m required. Contractor says 30 m (NOTES.md; geometry.json).
- Pylon width at deck is at most 4 m in elevation. Taper is at most 1 in 60 (NOTES.md).
- Stays: 7 per leg per side in the thesis and American Bridge; 14 or 28 in other counts (NOTES.md). Angles 17.4 to 26.2 deg from horizontal (thesis).
- Pier base is at most 8.5 m wide above the pile cap. The path passes through an opening in each river pier (NOTES.md).
- Path: 8 m wide, deck 0.40 m thick. Asphalt centre at least 3.0 m wide. Wood planks at least 1.8 m each side. Steel hangers in two lines (NOTES.md; Structurae; pedestrian-deck-through-pier.jpg).
- Lookouts bulge outward at each pier. The curve starts at least 20 m from the pier face. Seating is at least 7 m2 per side (NOTES.md; pedestrian-deck-lookout.jpg).
- Two tracks, gauge 1,435 mm. Overhead line. Six catenary poles on the river span per TransEd (NOTES.md).
- Segment lengths are listed in NOTES.md. They are only useful for joint lines.

**Conflicts inside the folder**
- Pylon count: 2 (agreement, photos) against 1 (Structurae, thesis "one tower"). Photos show two legs on one pier. Use 2.
- River pier count: 2 (agreement, Wikipedia) against 1 (Structurae). Use 2.
- Stay count: 7 per leg, 14 total, or 28 (NOTES.md). Photos show about 7 stays per fan per leg. Use 7.
- Pylon height: 24 to 30 m range against "30 m" (American Bridge, which does not name the datum).
- Walkway width: 7.8 m minimum, about 7 m in the 2013 concept (3.0 + 2x2.0), 8 m built. Use 8 m.
- Headroom under the box: 3.6 m and 3.0 m at piers (2013), 3.5 m general minimum (agreement). The folder gives no as-built value.
- Guideway length south of the river: 380 m minus 260 m is 120 m in the 2013 reference design. The OSM bridge tag gives about 211 m. NOTES.md explains why. Use OSM.
- Structurae calls the bridge "two-span" while listing three span lengths. Use 3.

## Build spec I would use from this alone

Units are metres. Local origin is the north river pier at lat 53.540671, lon -113.47713 (deck centreline). The model Y axis (forward) points true south at 180 deg. These are my choices.

**1. Main box girder, river span, 260 m**
- Trapezoid, 11 m top width, 3.5 m deep. The lower width is not given. I would assume the webs slope at 1:2, so the soffit is about 7 m wide (assumption from the agreement's 1:2 limit; photos agree with a visibly narrower soffit).
- Straight in plan. Constant depth. Parapets and railings on top.
- Colour: light concrete grey, slightly warm, weathered streaks (both-decks-from-north-bank.jpg, elevation-pylons-both-decks.jpg).

**2. Pylon pier and pylons**
- One Y-shaped pier at the north river pier, monolithic with the box, 8.5 m wide at most above the pile cap. Path opening through it.
- Two pylon legs, one at each deck edge, each at most 4 m wide at deck level, rising 24 to 30 m. I would use 28 m as a middle value. This is an assumption.
- In upper-deck-tracks.png the legs lean outward across the deck. In the elevation photos they lean and taper toward the top. Use a lateral outward lean and a slight taper.
- Anchor plates show as a row of square boxes on the inner face (both-decks-from-north-bank.jpg, elevation-pylons-both-decks.jpg).
- Colour: concrete grey, same as the box.

**3. Stays**
- 7 per leg on each side of each pylon, so 14 per pylon and 28 total. Two planes, outside the outer rails.
- White or very light grey sheaths about 0.2 m diameter. I read this from the photos, not from a source. Dark steel anchor collars at the deck edge.
- Anchors on the deck edge outside the rails, spaced along the span. Angles 17.4 to 26.2 deg (thesis).
- Back stays go north, forward stays go south. Both fan out as shown in elevation-pylons-both-decks.jpg.

**4. South river pier and south-bank pier**
- Concrete piers of the same family as the pylon pier, without pylons. Path openings in both.
- South river pier at 110 m south of the pylon pier. South-bank pier at 260 m, at lat about 53.539229.

**5. Pedestrian deck**
- 8 m wide, 0.40 m thick, 190.8 m long, hung on steel rods from the soffit. The rods run in two lines, galvanized grey, with bracket bases at the deck edge (pedestrian-deck-through-pier.jpg, pedestrian-deck-north-end.jpg).
- Surface: asphalt centre (dark grey), wood side planks (light brown, weathering grey in pedestrian-deck-lookout.jpg).
- Railing: galvanized steel with curved-top balusters, light grey.
- At each river pier the deck bulges into a lookout with benches (dark metal). The curve starts 20 m from the pier face (agreement).
- Hanger length is not given. I would use about 4 to 5 m by eye. This is an assumption.
- Soffit shows colourful art medallions (pedestrian-deck-north-end.jpg, pedestrian-deck-through-pier.jpg). Use a small decal or ignore it.

**6. Track bed on top**
- Two tracks at about 4.5 m spacing. Concrete direct-fixation slab, no ballast. Grating walkway between and beside tracks, dark grey.
- Dark railings at both edges. Catenary poles in the centre between the tracks (upper-deck-tracks.png), grey galvanized. A support-pole count of 6 on the river span is from TransEd, but the photo shows more poles in its view, so I would not trust 6. Wire catenary as thin lines.
- A train is optional. Not needed.

**7. South guideway, about 210 m**
- Concrete box girder, constant depth to the ramp. In plan it is straight to about lat 53.5386, then curves south-west by about 38 deg to lat 53.5374.
- Supported on Y or inverted-V concrete piers (Grierson hill photo, upper-deck-tracks.png shows a V pier at the far end). At least 35 m between piers (agreement). Pier count and spacing are not known. I would place piers at about 40 m spacing. This is an assumption.
- Over 98 Avenue the girder may be shallower. Not known.
- Ends at a vertical face at the start of the ramp. The ramp itself runs to Muttart stop (not in this folder; see P152).

**8. North end**
- Bridge tag ends at lat 53.541573. The tunnel portal is about 43 m further north (geometry.json). The folder says not to model the tunnel.
- Add a short abutment block and a plain tunnel-mouth stub. Its look is not in the folder.

**Elevation and sim placement**
- Plan position is solid. Elevation is not.
- I would set the deck by reading the sim terrain and the photos, using the pier-height ratio from elevation-and-south-girder-grierson-hill.jpg. That is a guess. The 2013 water levels (615.60 m, EL 615.9) have no datum and no relation to a deck level.
- Model the pier bases to run below the water or terrain surface, with a skirt, so a clipped base never shows a gap.

**LOD plan**
- LOD0 (under 500 m): everything above. Stays as cylinders or thin quads.
- LOD1 (500 to 1,500 m): box, pylons, 14 stays per side as lines or thin quads, path as a flat strip. Drop hangers, benches and balusters.
- LOD2 (1,500 ft AGL and above): a single extruded box with a thin path strip, two pylons, and the stays as one textured plane each. Drop the art soffit and the catenary.
- Collision: the box top, if the sim needs a surface. Not covered by the folder.

## Gaps and conflicts, worst first

1. **No deck elevation, no datum, no clearance over the river.** The folder has two design water levels without a datum and a 10 m window that is not tied to the path or the box. Wrong height shows from every angle.
2. **Pylon height is a range of 24 m to 30 m.** About 20 percent of the visual size. It also sets the stay lengths.
3. **No lower-box width or section drawing.** Soffit width and web slope are inferred. Only top width (11 m) and depth (3.5 m) are given.
4. **Gap between the box soffit and the path is missing.** It sets hanger length and how much daylight shows between the decks. The folder has 3.0, 3.5 and 3.6 m figures for headroom, none of them as-built.
5. **South guideway has no pier count, spacing, heights or deck level.** Only plan and a total length from OSM. Over 98 Avenue the girder may change depth.
6. **Pier shape is only read from photos.** No dimensions apart from the 8.5 m base width.
7. **Track spacing and crossfall are not given.** Spacing inferred from OSM and the thesis lane offset.
8. **Stay count conflict (7, 14, 28).** Use the photos. Low impact.
9. **North end has no photo of the portal or abutment.** Folder says none found.
10. **No photo of the finished 98 Avenue crossing at close range.** Folder says none found.
11. **Soffit lighting and night appearance are not covered.** The photos show small round fittings in the soffit (pedestrian-deck-north-end.jpg) and path lamps in the park. Nothing says what the bridge looks like lit.
12. **Catenary pole count (6 versus photo).** Low impact.

## Handoff requests

**Blocking**
1. Deck elevation. Find the LRT rail level and the path level in metres above sea level with a named datum, at the north pier, the south river pier and the south end of the guideway. Try Alberta bridge records, TransEd or City drawings, or survey data. If none exist, give the sim-terrain ground height at the north pier and a measured pier-to-deck height from a photo with a known scale.
2. Pylon height. Find a surveyed or drawn height above deck. A photo with a person or train for scale, taken square-on, would do.
3. Sim terrain and water at the site. Check whether the sim terrain, the river and the shore cover the pier bases. Say whether the piers will be clipped by the river mesh, and whether any ground edit or exclusion polygon is needed. Check where the valley floor and park sit relative to the guideway.
4. Section through the box. Find a drawing or a photo from directly below or from the end that shows soffit width, web slope and parapet height.

**Nice to have**
5. Gap from the soffit to the path deck and the hanger length. A square-on photo with a scale object would do.
6. South guideway piers. Count them, give spacing and heights, and say whether the girder gets shallower over 98 Avenue. A side photo from 98 Avenue or the park would answer it.
7. Track spacing. A top-down photo or the rail layout from a design drawing.
8. North abutment and tunnel portal photo or drawing, to model the stub honestly.
9. Colour references. Take swatches from a daylight photo of the concrete, the white stay sheaths and the galvanized steel. Say if the stays are white or silver.
10. Night lighting. Does the bridge have deck, path or soffit lighting? Any aviation or accent lights? Photos at night would show it.
11. Collision and road-surface needs. Say whether the sim needs collision on the deck or on the path, and whether anything should be walkable. This is a decision for the user, not a research item.
12. Catenary. Count the poles on the river span and check the photo against the six in the TransEd note.
13. Soffit art. A photo plus a size would let me add a decal. Low priority.
