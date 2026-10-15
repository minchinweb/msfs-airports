# B254 Muttart Conservatory — model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Reviewed from this folder only: NOTES.md, SOURCES.md, geometry.json, five photos.
Figures marked "(my arithmetic)" are my own sums from geometry.json nodes. They are not in the folder as numbers.

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 622.0 m (2,041 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 622.03 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../../RIVER-LEVEL.md`.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** no usable night photo found (see `../../../DATA-SOURCES.md`).
- **Street-level photos:** 4 daytime Mapillary frames in `street/` (CC BY-SA, credits in `street/SOURCES.md`). They show railings, barriers, lamp posts, lane and sidewalk layout and approach shape from the road; not the underside or truss depth. Check them before treating those items below as open.

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions.** The four pyramids can be built now: positions, heights, floor areas, layout and look are all in the folder. The base side, the berm and ground heights, and every dimension of the support greenhouses are missing. Those need stated assumptions or more research.

## What the folder gives me

### Layout and position (geometry.json)
- Pyramid centres (lat, lon):
  - Tropical 53.5355282, -113.4772852 (way 714340898).
  - Temperate 53.5348974, -113.4772917 (way 714340901).
  - Arid 53.5352093, -113.4767941 (way 714340899).
  - Feature 53.5352144, -113.4777726 (way 714340900).
  - Centre skylight 53.5352114, -113.4772875 (way 714340902).
- Names are OSM name tags. Edify (SOURCES.md) agrees: temperate is south, feature is west.
- Offsets from the skylight centre (my arithmetic): tropical about 35 m north, temperate about 35 m south, arid about 33 m east, feature about 32 m west. The N-S pair and the E-W pair each sit on a line within 1 m of true north or true east. The group is a cross, not a row.
- Main entrance node 1940805166 at 53.5354051, -113.4769722. It is on the east side (geometry.json "entrance"; NOTES.md "Plan").
- Stop node 53.53621, -113.48000. The pyramid group is about 208 m from it, measured to the skylight (map_distance_to_stop_m 207.7). The nearest greenhouse point is 28.4 m from it (geometry.json).
- Whole-complex centre 53.5354324, -113.4783154. This is area-weighted. It sits toward the greenhouse ring, so it is not the pyramid centre.

### Heights (NOTES.md, SOURCES.md)
- Tropical and temperate: 24 m floor to apex. Sources: Journal, student slide, Guinness. Guinness writes 78 ft 8 in. Monumentous writes 79 ft.
- Arid and feature: 18 m (59 ft). Sources: Journal, Guinness. The City says 59 ft for arid only.
- Centre skylight: no published height. OSM tag height=4 only.
- Entrance addition and its black granite pyramid (RPK, 2009) are a different object. No dimensions beyond a 233 m² facility size.
- OSM roof:height tags: 20 on the large pair, 14 on the small pair. The folder says not to subtract. I follow that.

### Floor areas (NOTES.md)
- Large pair: 660 m² (Journal, slide, Wikipedia, Williams, Guinness).
- Small pair: 381 m² (Journal, slide, Guinness) or 410 m² (Wikipedia, Williams). Conflict, see below.
- Centre court atrium: 1,319 m². Student slide only.
- Support greenhouse complex: 3,700 m². Slide and brochure.
- Greenhouse count: six (slide, Williams) or nine (Edify). Conflict.

### Footprint outlines (geometry.json)
- Each pyramid has a node ring. All four rings read as diamonds, with corners pointing N, E, S and W. Tropical: N-S extent 40.8 m, E-W extent 40.8 m (my arithmetic). Arid: both about 31.6 m (my arithmetic).
- Tropical NE face edge is 28.6 m. Other edges are uneven (edge_m), so the rings are not clean squares.
- Skylight ring: four sides of 5.5 and 5.8 m, a small diamond.
- Grass-roof part (way 714340904): flat, around the entrance, 66.2 m perimeter.
- East ring (way 1287216689, 411.1 m perimeter) shares nodes with the four pyramid rings. It traces the outer edge of the pyramid group.
- West ring (way 1287216690, 442.5 m perimeter) is the greenhouse envelope. It is one irregular polygon, not individual houses. Its nodes span roughly lat 53.5349 to 53.5361 and lon -113.4799 to -113.4779.
- Two tiny untagged rings (ways 322972875 and 322972340, 25.7 m and 32.6 m perimeter) sit south of the greenhouse ring. Unknown purpose.

### Look (photos)
- Glass and colour (`valley.jpg`, `group.jpg`, `elevation.jpg`):
  - Sunlit faces read pale silver or lavender-white.
  - Shaded faces read blue-green or teal. Dark green plants and dark interior frame show through (right pyramid, `elevation.jpg`).
  - Mullions and hip ridges are pale white or grey.
- Pane grid: square or near-square panes in a regular grid on every face (`elevation.jpg`, `group.jpg`). I count roughly a dozen pane rows on a large face. That count is a rough read, not a measurement.
- Cap: a dark louvered band just under each apex, with a small glass cap above it (`elevation.jpg`, `group.jpg`). Louver panels look amber or gold where lit in `group.jpg`.
- Base: a pale sill band with horizontal vents at the glass line. The pyramids rise out of the berm top (`elevation.jpg`).
- Berms: mown green grass mounds around the pyramids. Concrete portals with glass guard rails and stepped stone or concrete retaining blocks cut into them (`elevation.jpg`, left and right).
- Skylight: a small glass pyramid, low between the four. Seen at the centre of `elevation.jpg`.
- Greenhouses (`greenhouses-from-pyramids.jpg`, `greenhouses-from-stop.jpg`):
  - Long low pitched glass roofs with pale frames.
  - A grey concrete retaining wall, a squat grey concrete service block with rooftop equipment, and a tall concrete tower with a square opening.
  - They read as one flat glass roofscape, not as pyramids.
- Stop: low dark-brown slab roof with a pink sculpture on top, west of the greenhouses (`greenhouses-from-stop.jpg`). That is P152, not this model.

## Build spec I would use from this alone

### Coordinate frame
- Origin: centre skylight, 53.5352114, -113.4772875. Axes aligned to true north and east. Use 111,319 m per degree of latitude and about 66,150 m per degree of longitude here (my arithmetic).
- Place each part at its offset (E, N) from the origin:
  - Tropical (0, +35).
  - Temperate (0, -35).
  - Arid (+33, 0).
  - Feature (-32, 0).
  - Skylight (0, 0).
- Heading: pyramid base edges at 45 degrees to the axes, corners to N, E, S, W. This follows the node rings. It is not stated in any text.

### Components

| Part | Shape | Height | Base | Notes |
|---|---|---|---|---|
| Tropical, temperate | square pyramid, 4 faces | 24 m | assumption: about 25.7 m side if 660 m² is the base, about 28.6 m if the ring edge is. Pick one and note it. | Apex centred on the ring centre |
| Arid, feature | square pyramid | 18 m | assumption: about 19.5 m side if 381 m² is the base. For 410 m² use about 20.2 m. | Same cap and grid detail |
| Centre skylight | small pyramid | 4 m (OSM tag, assumption) | 5.5 by 5.8 m ring | Low, hardly visible from the air |
| Berms and grass roof | terrain mound under and around the four | not known | follow the east ring outline | See gaps. Needs a height. |
| Entrance portals | concrete box with glass rails | not known | east side, near the entrance node | Small. Detail only for close fly-bys. |
| Support greenhouses | extruded block with a gable or barrel roof, glass | not known | west ring polygon | Single mass. Pitch and height unknown. |
| Service block and tower (near the greenhouses) | grey boxes | not known | no footprint | Only seen in `greenhouses-from-pyramids.jpg`. Optional. |

- The base side figures above come from a square assumed from the photos and the areas. The folder says no source gives the base. The ring diamonds are 25 to 30 percent larger by area than the published floor areas (my arithmetic: about 830 m² against 660 m² on tropical, about 500 m² against 381 m² on arid). I would build to the published areas and flag that.
- Cap detail: a dark louver band about the top 15 percent of the height (my read from `elevation.jpg`, not measured), then a small glass tip.

### Materials and colours
- Glass: reflective, tinted blue-green. High specular so sunlit faces go pale silver. Moderate transparency. Dark green interior fill behind it so the faces are not empty.
- Frame and mullions: pale grey-white, thin. Draw them in the texture at LOD1 and below.
- Louver band: dark grey, with an amber highlight.
- Sill and portals: pale concrete.
- Berm: mown grass, medium green.
- Greenhouse roofs: glass with pale frames. At altitude they read as white-silver.
- Greenhouse walls and retaining walls: mid-grey concrete.

### LOD
- At 1,000 to 3,500 ft AGL, a pane grid is below pixel size. A textured four-face pyramid with a mullion grid texture and a louver band is enough. A separate cap quad is cheap.
- Close fly-by LOD: real mullion geometry on the ridges and the sill, portals, glass rails, and visible interior floor.
- Greenhouses: one or two low-poly roof blocks with a texture. No individual bays.

### Placement in the sim
- Place at the skylight coordinate. Heading 0 in the true-north frame above.
- Ground and berm elevation is not given. I would place the model at ground level and let the sim terrain set the base. That depends on the berm height. See gaps.
- Keep the greenhouse mass in a second glTF or a second node. Its footprint is 100 m or more from the pyramids and it can be placed separately.

## Gaps and conflicts

Ranked by how much each would hurt the model.

1. **Berm height and glass-line height are unknown.** The 24 m and 18 m heights are floor to apex. The photos show the sill well above the surrounding grass, with the berm cut away at the portals. I cannot tell how much of the 24 m shows above the valley floor. This changes the silhouette in the 2018 and 2010 photographs and makes the apex height above terrain a guess. No elevations, no datum (geometry.json "dimensions" all null).
2. **No base side.** I have to build from areas. The ring diamonds and the published areas disagree by 25 to 30 percent (my arithmetic). A wrong base changes the roof slope on every pyramid. Photo proportions are not reliable for a check because `group.jpg` and `elevation.jpg` are wide stitched images and `valley.jpg` is far away.
3. **Support greenhouses have no height, pitch, bay count, ridge direction or individual outlines.** The count is six or nine. The west ring is one envelope. The photos show roofs but no bearing, so I cannot say which way the ridges run. The roofs are the largest ground footprint in the scene, next to the pyramids.
4. **Small-pair area conflict.** 381 m² (Journal, slide, Guinness) against 410 m² (Wikipedia, Williams). The City says 4,200 ft² for arid (about 390 m², my arithmetic), Guinness says 4,100 ft², Wikipedia says 4,400 ft². All published. About a 7 percent difference in area, so about a 3.5 percent difference in side length. Low risk.
5. **Layout wording conflict.** The student slide puts tropical and temperate on one diagonal and arid and show on the other. OSM puts tropical north, temperate south, arid east, feature west. These can both be true if "diagonal" means a 45 degree frame. I treat OSM as the layout. The folder did not redraw the slide.
6. **Photo bearings are not given.** I cannot cross-check the layout against `elevation.jpg` and `group.jpg` without the camera heading. In `elevation.jpg` the two large pyramids frame two small ones, which is plausible for a view along the E-W line, but that is my reading.
7. **Skylight is thin.** 4 m is a mapper tag. Sides come from the same ring. The 1,319 m² centre court figure is from one student slide and conflicts with the 5.5 by 5.8 m skylight only if the court were glazed, which the folder does not say.
8. **Mullion spacing, pane size, glass colour and frame material.** Read only from photos. Edify says the arid girders are painted, and does not give a colour. Texture work is possible but approximate.
9. **Entrance portals, grass-roof part and the 2009 black granite pyramid.** The granite pyramid is named but has no position or size. The grass-roof part has a footprint and no height.
10. **Folder housekeeping.** SOURCES.md says "all three saved files" but five photos are listed and present. Wikipedia's coordinate (53.53522, -113.47650) is about 55 m east of the skylight and was not used. The address says Street or Avenue. None of these changes the build.
11. **No collision, night lighting or interior data.** Nothing in the folder says whether the pyramids are lit at night, or what the glass looks like from outside after dark.

## Handoff requests

**Blocking**
1. Berm and sill heights. Find a section, a surveyed profile or an elevation drawing, or a LiDAR or DEM sample: ground elevation (with datum) at the centre of each pyramid, at the sill line, on the berm crest, and on the surrounding valley floor. Even four spot heights would do. Also say how far the glass line stands above the berm crest. (Gap 1.)
2. Pyramid base side. Find a Hemingway drawing, a City facility plan, or a photo taken square-on with a known scale object (a person, a door) at the base of one large and one small pyramid. State the side or the diagonal in metres. (Gap 2.)
3. Support greenhouse envelope. Find the ridge direction, roof pitch, eave and ridge heights, and bay count. Say whether it is six or nine houses and mark their outlines on the west ring. Any plan, roof survey or two clear oblique photos with a scale object would do. (Gap 3.)

**Nice to have**
4. Camera bearing and position for each of the five photos, so I can check the layout and orientation. (Gap 6.)
5. One square-on photo of a large pyramid face and one of a small face, taken from a hill or a drone-height view, with no tree cover. I want the pane count, the louver band height as a share of total height, and the sill detail. (Gap 8.)
6. Aerial, satellite or Street View capture of the whole complex from above. A top-down image would settle the diamond orientation and the area disagreement with the rings, and show the greenhouse roof ridges. No openly licensed aerial was found, so a looked-at-only reference, with the source named, is fine. (Gaps 2, 3.)
7. Glass colour and reflectance. A colour-checked photo in overcast light and one at low sun. (Gap 8.)
8. Skylight height and size, and where the 1,319 m² court lies. A City or Journal figure. (Gap 7.)
9. Entrance: position and footprint of the 2009 black granite pyramid and the portals. Sizes and a photo of each. (Gap 9.)
10. Night appearance. Does the complex glow, and are the pyramids or the berms lit? Any dusk or night photo. (Gap 11.)
11. Collision: ask whether the model needs collision or can be visual only. I would assume visual only unless told otherwise.
12. Ground interaction: say how the sim terrain and the parking and park around the conservatory are handled. In particular, whether a flat or sculpted ground mesh must be included for the berms, and whether trees around the pyramids (seen in `valley.jpg` and `group.jpg`) are in the sim's own vegetation or need adding. (Gap 1.)
