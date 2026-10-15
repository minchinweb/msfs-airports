# P152 Muttart LRT stop: model handoff review

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Scope: the stop only. B254-conservatory was not read.

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 622.0 m (2,041 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface:** this clip holds no river reach, so no water figure applies. For a ravine or rail crossing use the ground heights above and below.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** 1 photos in `night/` with a lighting description in `night/SOURCES.md`.
- **Street-level photos:** 5 daytime Mapillary frames in `street/` (CC BY-SA, credits in `street/SOURCES.md`). They show railings, barriers, lamp posts, lane and sidewalk layout and approach shape from the road; not the underside or truss depth. Check them before treating those items below as open.

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions.** Plan position, heading and platform length are solid. Platform width, height, elevation, ramp shape and canopy size are not measured. I would build a simple, low-detail stop and take heights from requirement limits and photo proportions. Nothing here blocks a 1,000-3,500 ft model. Close fly-bys will look generic.

## What the folder gives me

| Fact | Value | Source |
| --- | --- | --- |
| Type | At-grade, two side platforms, two tracks, under catenary | NOTES.md (Platform) |
| Project centre | 53.53621, -113.48000 (the stop node) | geometry.json `centre`, `extract_stop` |
| West platform ring | OSM way 1157283683, 7 nodes, long sides 103.8 m | geometry.json `platforms[0]` |
| East platform ring | OSM way 1157283685, 7 nodes, long sides 103.6 m | geometry.json `platforms[1]` |
| Platform min length | at least 90 m (requirement) | NOTES.md, SOURCES.md (Sched 5 Part 5) |
| Platform min width | at least 4.0 m (requirement, side-loading) | NOTES.md |
| Platform height | at most 360 mm above closest rail (maximum, not as-built) | NOTES.md |
| Train floor | 0.3 m off ground; 50 mm vertical, 75 mm horizontal gap limits | NOTES.md |
| Cross-fall | 1.25% to 2.50%, down and away from track (requirement) | NOTES.md |
| Canopy | Metal roof, wood soffit, curved section, one steel column row at the non-track edge, at least 3000 mm on centre | NOTES.md |
| Canopy underside | at most 3.8 m above platform | NOTES.md |
| Canopy area | at least 125 m2 per platform | NOTES.md |
| Shelters | at least four glass shelters per platform, each at least 6.5 m2, short side at least 1.6 m (requirement) | NOTES.md |
| Catenary pole | max 4.5 m above platform top on a platform. Photo shows poles between the tracks | NOTES.md, platform.jpg |
| Track | Gauge 1,435 mm. Concrete slab between platforms, rails set in the slab | NOTES.md, platform.jpg |
| Ramp to north | Agreement max 6 m, adjacent grade to top of rail. Mapped run to bridge tag: 199.1 m (west track), 213.1 m (east track) | NOTES.md |
| Ramp finish | Landscaped earth, tree screening, textured ramp walls (requirement) | NOTES.md |
| Ramp grades | -5.600% and -0.275% on a 2013 reference drawing, "approximate", from the R14 notes | NOTES.md |
| Retaining walls | 2013 concept: 5 walls, 120-230 m long, 2.5-6 m high | NOTES.md |
| South | Crossover 39 m south of the stop. Track climbs Connors Hill parallel to Connors Road | NOTES.md, geometry.json `excluded` |
| Art | "Best Fronds" leaf sculpture, 2 sections on diagonal canopies, each 30 ft long x 4 ft high | NOTES.md; pink leaf shape on roof in shelter.jpg |
| Vehicle | Bombardier Flexity low-floor, ETS livery, 2-car train at most 90 m | NOTES.md, train.jpg |

### Derived from geometry.json (my arithmetic, not stated in the folder)

- Long axis bearing of both rings is about 49 deg true (SW end to NE end). West ring SW node 53.5361554, -113.4801367 to NE node 53.536772, -113.4789592. East ring 53.5360782, -113.4800218 to 53.5366913, -113.4788446. Both give 48.6-48.8 deg. Reverse bearing about 229 deg.
- Corresponding corners of the two rings are about 11.5 m apart, measured perpendicular to the axis. The east ring is on the SE side.
- Each ring's short end (for example nodes 2 to 4 of the west ring) is about 3.8 m. The NOTES say not to add short sides into a width. I use ~3.8 m only as a plan-view hint. It is below the 4.0 m requirement, so it is unreliable.
- Photo platform.jpg is described as looking north, but the axis is about 49 deg. Treat "north" as "up the ramp, toward the NE".

### Conflicts and tensions inside the folder

- Mapped platform length (103.8 / 103.6 m) vs the 90 m minimum. Not a true conflict, but the actual length is unknown. NOTES keeps both.
- Ring short side ~3.8 m (derived) vs the 4.0 m minimum width. Mapping tolerance, probably.
- Tactile edge, ramp and "direct fixation" (2013) vs concrete slab seen in photo: NOTES says do not treat as the same detail.
- 6 m ramp maximum vs 2.5-6 m walls: different statements, not merged. Fine, but I cannot pick a ramp height.
- Photo platform.jpg shows the opposite (right) platform canopy with a different, flatter profile than the left. Not discussed in NOTES.
- Wikipedia coordinate 53.53639, -113.47944 differs from the project centre. Centre is the south stop position. OSM station node 53.5364394, -113.4795032 lies between the two stops. The model origin should be the platform midpoint, not the project centre (see below).

## Build spec I would use from this alone

### Origin and placement

- The project centre is the south end of the platforms. The platforms run about 103 m to the NE, so the stop midpoint is near the OSM station node 53.5364394, -113.4795032. I would place the model origin there.
- Heading: long axis 49 deg true. Build the model with its long axis on +Z (or X) and rotate by 49 deg when placing. Direction check is needed because the sign convention matters.
- Elevation: not given. The model must sit on the sim terrain or be placed by an altitude the terrain tool reads. No MSL value, no datum.
- Model the ramp to the NE as terrain-conforming fill only if the researcher gives heights. Otherwise leave the ramp to the bridge model (R14).

### Components

1. **Two platform slabs.** Each 103.7 m long (use mapped value). Width 4.0 m minimum, say 4.0-4.5 m (assumption). Height above rail head 0.3 m (assumption from low-floor train floor 0.3 m and the 360 mm maximum). Centres about 11.5 m apart (derived). Material: warm beige-tan concrete, slightly pink-orange on the vertical face (platform.jpg, train.jpg, shelter.jpg).
2. **Tactile strip.** About 0.6 m wide yellow strip along the track edge, full length (visible in platform.jpg, train.jpg). Width is a visual estimate. A thin yellow texture strip, no geometry.
3. **Track slab.** Concrete slab between and beside the platforms. Light grey, with two steel rails per track at 1,435 mm gauge. Rails are a thin strip or a texture at 1,000+ ft.
4. **Canopy, each platform.** Curved metal roof over a wood-tone soffit (warm orange-brown). Dark brown/black fascia, dark steel columns at the rear edge, at least 3 m on centre. Underside about 3.8 m max above platform. Roof not continuous over the whole length. Photo platform.jpg shows several separate canopy bays with gaps. Bay count and lengths unknown. I would use three to four bays per platform (assumption) and meet the 125 m2 minimum.
5. **Glass shelters, each platform.** Four per platform minimum (requirement). Glass box with silver frames under the canopy, about 6.5 m2 each (requirement). Height about 2.5-3 m (visual estimate).
6. **Catenary poles.** Galvanized grey steel, round, standing between the two tracks, with cantilever arms (platform.jpg). Spacing unknown. Height unknown, but taller than the canopy. Contact wire as a thin line only. Optional at far LOD.
7. **Lamp standards.** Black curved-arm poles on the platforms (train.jpg) and on the plaza (shelter.jpg). Optional.
8. **Plaza and walls (south or west side).** Light grey concrete plaza with a patterned surface, low concrete retaining wall, stone-faced wall and a galvanized railing (shelter.jpg). Optional, because the extent is unknown.
9. **Leaf sculpture.** Pink, on two diagonal canopies (shelter.jpg). Small pink shape on the roof. Optional, close-view only.
10. **Train.** Not part of the model. Flexity is blue/white, ETS. Skip unless the project has a shared tram asset.

### LOD ideas

- LOD0 (close, under 300 m): everything above, rails, tactile strip, glass, poles.
- LOD1 (300-1,500 m): slabs, canopy bays as boxes with curved top, shelters as glass boxes, poles as sticks, no wires.
- LOD2 (beyond 1,500 m): two long thin slabs plus roof-colour bays on one mesh. Nothing smaller than ~1 m.
- At 1,000-3,500 ft the stop is a pair of narrow beige strips with brown roof patches in trees. I would not spend effort beyond LOD1.

### Materials and colours (read from photos, not sampled)

- Platform concrete: warm tan, slight salmon tint on the vertical face.
- Track slab: neutral light grey.
- Tactile strip: bright yellow with dot pattern.
- Soffit: orange-brown wood. Roof fascia and columns: dark brown to black. Roof top: dark brown-grey metal (train.jpg, shelter.jpg).
- Glass: clear, silver-grey frames.
- Poles: galvanized grey. Rails: bright steel.
- Night: platforms are tagged `lit=yes` in OSM (geometry.json). Soffit lights and a lit sign are visible in platform.jpg. Emissive strip under the canopy is plausible. No colour temperature is given.

### Collision

Not given. I would set no collision on the stop (the platforms are at ground level). I would not collide the track.

## Gaps and conflicts, ranked by harm to the model

1. **No elevation and no terrain relation.** No MSL height, no datum, no ground profile. The stop is at the bottom of a valley ramp. Placement on sim terrain could float or sink. Highest risk.
2. **Ramp geometry missing.** No length, grade or height at the stop. This is what reads from the air (NOTES), and it is tied to R14. The only numbers are a 6 m maximum, a 2013 concept, and mapped runs of 199.1 / 213.1 m.
3. **Platform width and height unknown.** Width not measured (derived ~3.8 m vs 4.0 m minimum). Height assumed from a 360 mm maximum and the 0.3 m train floor.
4. **Canopy layout unknown.** Bay count, bay length, canopy width and roof height not given. Photos show several separate canopy bays, with different profiles on the two platforms. Plan layout cannot be built from numbers.
5. **Origin ambiguity.** The centre is the south stop node, not the platform midpoint. The sign of the heading and which platform is "west" depend on the geometry nodes. Researcher should confirm.
6. **No aerial.** No overhead image. Roof colour from above, plaza extent, tree cover and the relation to the glasshouses are unknown.
7. **Pole count and spacing unknown.**
8. **Stair, crossover, storage track unknown.** The required stair at the north end of the west platform is not shown. The 39 m crossover is south. Whether the storage track was built is unknown.
9. **Photo quality.** Four thumbnails, 1,920 px. ramp.jpg is a 2020 construction view and misleads on appearance. shelter.jpg shows the stop before opening (fencing, bare mulch).
10. **No texture-grade photos.** Photos are oblique, shaded and not rectified.

## Handoff requests

| # | Request | Blocking? |
| --- | --- | --- |
| 1 | Ground elevation (MSL, with datum) at the south stop node and the NE end of the platforms. Source: Alberta LiDAR DEM or the City's open data. Also elevation at the foot of the ramp and at the bridge end. | Blocking |
| 2 | Terrain profile along the track from the stop up to the bridge end: heights at 25 m steps. This sets the ramp fill. | Blocking for any ramp modelling. Nice-to-have if the ramp belongs to R14. |
| 3 | Confirm which model (this one or R14) owns the ramp, retaining walls and fill. State the join point in lat/lon. | Blocking (to avoid duplicated or missing ramp) |
| 4 | Platform width, measured on a dimensioned drawing or by scaling a rectified image (any known object, such as a 1.435 m track gauge). | Nice-to-have |
| 5 | Platform height above rail: one photo showing a tape or a person at the platform edge. | Nice-to-have |
| 6 | Canopy plan: number of bays, bay lengths and gaps along each platform, canopy width, roof height at the high and low edge. Source: a straight-on side photo from the track bed or an aerial. | Nice-to-have |
| 7 | An aerial or satellite view of the stop (any licence for reference only is fine, but note it). Roof colours from above, plaza extent. | Nice-to-have, strongly preferred |
| 8 | Side elevation photo of each platform from the opposite platform, square on. Colour reference for soffit, fascia, concrete. | Nice-to-have |
| 9 | Catenary pole spacing and height. One photo with the pole and a person, or a count from an aerial. | Nice-to-have |
| 10 | Count of shelters per platform. Count from photo or aerial. | Nice-to-have |
| 11 | Heading check: confirm the platform axis against a map. My derived 49 deg true should agree within 2 deg. | Quick check, blocking if skipped |
| 12 | Night appearance: a night photo of the stop, to judge lamp colour and soffit lighting. | Nice-to-have |
| 13 | Collision: confirm whether the sim needs the platforms to be walkable or collidable (for helicopter landings or ground vehicles). Default: none. | Nice-to-have |
| 14 | Whether the sim already draws the Valley Line tracks here (default scenery or another project file). If yes, avoid a duplicate track slab. | Blocking (duplication risk) |
| 15 | Whether the 2013 storage track and the stair were built. One photo of the NW side of the west platform. | Nice-to-have |
