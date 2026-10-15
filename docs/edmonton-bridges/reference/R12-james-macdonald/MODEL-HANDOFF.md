# R12 James MacDonald Bridge: model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Reviewed from this folder only (NOTES.md, SOURCES.md, geometry.json, 7 photos). Nothing outside it was used.

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 613.7 m (2,014 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 613.73 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Main deck height** (`road_deck`, DSM median): 631.52 m, 17.79 m above the river. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** no usable night photo found (see `../../DATA-SOURCES.md`).
- **Street-level photos:** 5 daytime Mapillary frames in `street/` (CC BY-SA, credits in `street/SOURCES.md`). They show railings, barriers, lamp posts, lane and sidewalk layout and approach shape from the road; not the underside or truss depth. Check them before treating those items below as open.

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions.** Plan shape, approach layout and general look are good. Every vertical number is missing: deck elevation, clearance, girder depth, pier height, span count. I can build a believable massing for 1,000-3,500 ft viewing. I cannot make it fit the sim terrain without a deck or river elevation. That one item is blocking for placement. The rest can be estimated from photo proportions.

## What the folder gives me

Plan geometry (geometry.json, OSM, retrieved 2026-10-14):

- Westbound deck centreline, way 25455305: 14 nodes, 381.4 m, 3 lanes, one-way, asphalt, width tag 11.1, layer 1. Runs east end to west end. Northern line.
- Eastbound deck centreline, way 25455308: 15 nodes, 375.6 m, same tags. Southern line.
- Bridge outline, way 626069071: closed polygon, 20 nodes, tagged `bridge:structure=beam`. South edge 371.4 m, north edge 381.6 m. West end 29.9 m wide. East end a 37.3 m edge plus a 2.9 m jog.
- Mapped centreline spacing 12.1 m to 19.1 m, average 13.9 m (NOTES.md).
- North sidewalk, way 673730078: concrete footway, 367.4 m, 10 nodes, 9.2 to 14.7 m north of the westbound line (NOTES.md). Live tags read `sidewalk:right=separate` on the westbound way. No sidewalk on the south side.
- Chain endpoints (from geometry.json nodes): west end near 53.5352, -113.4912. East end near 53.5361, -113.4857. Project centre 53.536, -113.488.
- Approaches (geometry.json):
  - West, 97 Avenue. Westbound way 25455281: 4 lanes, width tag 14.8, 184.9 m, 6 nodes. Eastbound way 432373966: 3 lanes, width tag 11.1, 154.8 m, 5 nodes. Far nodes near 53.5344, -113.4937.
  - East, 98 Avenue. Westbound way 926792878: 3 lanes, 68.9 m, 2 nodes, far node 53.5363, -113.4847. Eastbound way 106711215: 3 lanes, 33.1 m, then ways 926792877 (2 lanes, 40.6 m) and 926792876 (2-lane link, 40.4 m).
  - East ramp, way 106711220: 1 lane, 308.1 m, 20 nodes, curves south off the eastbound deck.
  - Paths: west footway 1264715853 (195.1 m), steps 226985622 (20 m), east footway 673730077 (3.3 m).
- Total length as stated: 359.7 m (Wikipedia, Wikidata) and 359.66 m (Structurae).
- Type: haunched concrete girder (Alberta aesthetics study, 2005). Opened Oct 1971 (Structurae: 4 Oct. Wikipedia and Wikidata: 11 Oct).
- Six lanes plus pedestrians (Wikipedia infobox, uncited). 60 km/h (OSM).
- Rehabilitation 2007-08: new railings, repaved deck, strengthened girders, repaired piers, new bearings (Journal, Lorac). Railing design not described.
- Do not model the three unbuilt spans south of the bridge (NOTES.md).

Photo facts:

- `elevation-from-south.jpg` (3 Jun 2008): girder soffit curves up between piers. One pier is a twin pair of square shafts. The other is a single wide shaft. Deck edge has a slim parapet and light poles with a single curved arm. Colours: mid-grey concrete, dark grey asphalt, grey railing.
- `underside-from-river.jpg` (6 Aug 2011): several parallel girders, deeper at the pier, with cross-frames between. Pier is a wall shaft with a rectangular opening near the water and a cap under the girders. A red band at the base of the shaft. Fascia has a metal railing on a concrete parapet. Light poles stand at the deck edge. Concrete is light grey, weathered, with horizontal form lines.
- `girder-behind-low-level.jpg` (24 Aug 2009): this bridge is the upper deck. Deep haunch at the piers, thin at midspan. Two plain rectangular wall piers in the channel, light grey, unadorned. Deck edge is a straight horizontal band with a railing.
- `oblique-and-east-ramps.jpg` (2010): bridge curves gently in plan. On the south bank the deck is carried by tall round/square shafts that step down the slope. The abutment bank has rock riprap. The road splits into the east interchange ramps. Light poles run along both edges.
- `east-approach-toward-muttart.jpg` (15 Feb 2009): shows 5 to 6 pier columns in the frame as the deck curves into the Cloverdale interchange. Ramps are on embankments with a guardrail. Green highway signs on the ramp. Light poles with curved arms. Concrete grey, asphalt dark grey. Pile of riprap under the first span.
- `underside-over-park.jpg` (25 May 2017): a ribbed soffit (many narrow parallel ribs) and wide square pier walls with chamfered, recessed panels. Per NOTES.md this is the park span, not the river span.
- `cloverdale-98-avenue.jpg`: 98 Avenue at grade in Cloverdale. Three lanes, painted yellow double centre line, concrete sidewalk on both sides. No bridge in frame.

## Conflicts inside the folder

- **Length.** 359.7 m and 359.66 m (stated) against 381.4 m and 375.6 m (OSM centrelines) and 371.4 / 381.6 m (outline edges). NOTES.md says these are different extents. I will build from OSM lines for plan, and treat 359.7 m as the structure length, as the notes advise.
- **Opening date.** 4 Oct 1971 (Structurae) against 11 Oct 1971 (Wikipedia, Wikidata). No model impact.
- **Lanes.** Six present (infobox) against five westbound (freeway design). NOTES.md says use six.
- **Width.** Each carriageway width tag is 11.1. Centreline spacing is 13.9 m average. Outline is 29.9 m at the west end. If both carriageways are 11.1 m wide on 13.9 m centres, the gap between them is about 2.8 m, and the total is about 25 m. That leaves roughly 2.5 m each side inside the 29.9 m outline. The sidewalk offset (9.2 to 14.7 m from the westbound centreline) goes beyond the outline's roughly 8 m half-margin on that side. My arithmetic. The OSM geometry is not self-consistent.
- **Westbound approach.** West 97 Avenue leaves the deck as 4 lanes, 14.8 m, from a 3-lane deck. The eastbound arrives as 3 lanes. Likely a mapper widening for a turn lane.
- **Pier count.** NOTES.md says 2 shafts in the 2008 frame and a count was not taken. The 2010 and 2009 frames show more pier columns on the south approach. The count is not reconciled.
- **Photo 'underside-over-park'.** NOTES.md calls it the park span. The Journal's two "approach bridges" are not located. Do not use the ribbed soffit for the river span.

## Build spec I would use from this alone

Placement and orientation:

- Origin at the midpoint of the two deck centrelines at the river span (about 53.5356, -113.4885). Place the deck along the OSM polylines, not one straight line. The plan curves gently.
- Overall heading from west end to east end is about 074 degrees true (east-northeast). Reverse is about 254. My calculation from the first and last nodes of way 25455305.
- Deck length: follow the polyline, about 375 to 381 m. Add approach structures to the OSM way lengths above only where the photos show a bridge or embankment.
- Elevation: unknown. Place the deck by reading the sim terrain at the river. Treat all heights below as proportions to be confirmed.

Components:

1. **Two carriageway slabs.** Each 11.1 m wide, 3 lanes, following way 25455305 and way 25455308. Gap between them from the 13.9 m average spacing, varying 12.1 to 19.1 m. Single deck mesh with a median strip, joined at ends. Asphalt dark grey. White/yellow lane markings in the texture, yellow double line at the centre where the carriageways merge on the approaches.
2. **Haunched girder soffit.** Parallel concrete girders under the deck. Deeper at piers, shallower at midspan. The proportion on the 2009 and 2011 photos is roughly 1.5 to 2 times deeper at the pier than at midspan (visual estimate, not measured). Cross-frames between girders at LOD0 only.
3. **Piers.** Concrete wall shafts, rectangular, with a cap under the girders. One pier line is a twin pair of shafts, one line is a single wide shaft (elevation-from-south). South-bank approach piers are taller shafts stepping down the slope. Pier count for the river is two lines (photos). Approach count unconfirmed.
4. **Abutments and slopes.** Rock riprap slopes at both ends (oblique, 2010).
5. **Railing and parapet.** Low concrete parapet with a metal railing on both fascia edges. Grey. Detail is thin at distance, so a texture strip with a simple 3D rail at LOD0 is enough.
6. **North sidewalk.** Concrete, on the north fascia only. Width unknown. Use a placeholder of the OSM geometry offset, not 9 to 14 m.
7. **Light poles.** Single curved arm, galvanised or pale grey. Both edges. Spacing not given. Guess from photos at an interval of about 3 pole lengths and mark as a guess.
8. **Approach roads.** 97 Avenue west, 98 Avenue east, and the 308 m east ramp, as ribbons following the OSM ways. Ramp embankments and a guardrail on the east interchange.
9. **Colours.** Concrete light grey, slightly warm, weathered. Asphalt dark grey. Railing mid-grey. Red band on the base of the pier shaft (2011 photo). Green highway signs on the east ramps.

LOD ideas:

- Far (above 2,500 ft): one deck ribbon, two pier lines, textured soffit band. No railings in geometry.
- Mid (1,000 to 2,500 ft): add haunch profile, pier caps, parapet, poles.
- Close fly-by: cross-frames, bearings, pier opening, sidewalk, riprap.

Sim interaction:

- Collision and road surface: treat the deck and ramps as drivable road surface only if the sim needs it (not stated in the folder).
- Night lighting: not covered. Poles exist along both edges. Lamp type not given.

## Gaps and conflicts, ranked by harm to the model

1. **No deck elevation or river level, no vertical datum.** The deck cannot be set to the sim terrain. Photos give no scale.
2. **No span count or span lengths.** Pier positions along the deck are guesses.
3. **No girder depth, pier height, or pier plan size.** All proportions are visual estimates.
4. **Deck width unresolved.** 11.1 per carriageway, 13.9 spacing, 29.9 and 37.3 outline, sidewalk offset to 14.7. They do not agree.
5. **No approach grade or elevation change.** 97 Avenue and 98 Avenue climbs cannot be shaped. The 7.5 percent figure is not located.
6. **Girder cross-section unnamed.** I-girder or box not stated. The 2011 photo suggests separate girders. Only one frame shows it.
7. **No close photo of the deck top or the Rossdale approach.** Railing and parapet detail are from distant frames. Railing may have changed in 2008.
8. **Sidewalk width and pole spacing missing.**
9. **Sim terrain and water interaction not covered anywhere in the folder.**
10. **Night lighting and collision not covered.**

## Handoff requests

Blocking:

1. **Deck elevation above sea level, with vertical datum, at the river span and at both abutments.** Source: Alberta bridge sheet, City of Edmonton survey, or a LiDAR/DEM read at the deck line. Without this the model cannot be placed.
2. **River water-surface elevation at the bridge.** Needed to set pier base and decide how much shaft shows. Say which source (gauge conversion, DEM, or sim water level).

Nice-to-have (would change the look):

3. **Span count and span lengths, and pier positions along the deck.** From a drawing, a plan view, or a top-down aerial. A single aerial would give pier positions.
4. **Girder depth at pier and at midspan, and pier shaft plan size.** From a side elevation photo with a known scale object, or a drawing.
5. **Total deck width, carriageway width, median width, sidewalk width.** Settle the 11.1 / 13.9 / 29.9 / 37.3 / 14.7 conflict.
6. **Close photos.** (a) deck top looking along the river span, (b) railing and parapet from the side at 2 to 5 m distance, (c) pier cap and bearings from below, (d) Rossdale approach, (e) both abutments.
7. **Approach grades.** Elevation at the bridge end and at natural grade for 97 Avenue (west) and 98 Avenue (east).
8. **Which structures are the "two approach bridges" in the 1971 Journal recap.** Decide whether the east ramp and the south-bank piers are separate bridges.
9. **Light pole height, spacing, arm and lamp type.** Needed for night lighting.
10. **Sim checks (done in the sim, not research).** Does the sim terrain or water mesh clip into the piers? Is the river a flat water polygon with a fixed level? Can the pier base be buried below it? Check `maxheight` or clearance expectations for boats, and whether the deck and ramps should carry collision and road-surface material.
11. **Colour reference.** One calibrated, evenly lit photo of the concrete and railing in daylight. The folder photos vary in exposure.
