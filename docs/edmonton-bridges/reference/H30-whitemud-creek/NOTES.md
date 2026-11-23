# H30 Whitemud Creek arch: modelling brief

Edmonton. A semi-circular arch on the southwest Anthony Henday Drive (Alberta Highway 216), over Whitemud Creek. Built 2005. It is a wildlife and pedestrian crossing beneath the highway, not a river bridge. Surveyed centre: 53.4286, -113.5630. The estimate in `draw-map.py` was 53.448, -113.560. The surveyed centre is 2,169 m from that estimate: about 2,160 m south and 199 m west. The estimate sat in a residential and park area with no road in the 2019 aerial. The Henday is about 2.2 km south of it.

Each direction of the highway is a separate one-way carriageway here. Eastbound runs west to east. Westbound runs east to west. The two carriageways are close together at the arch, roughly 40 m apart in the OSM geometry.

This is not H28 Blackmud Creek (53.437, -113.496). Blackmud is three open-spandrel arches with a 40 m middle span and a deck 17 m above the creek. None of those figures apply here. This is not H27 or H28 unchanged, and it is not a copy of the Blackmud model.

Numbers below are cited. Where sources disagree, both are given. A blank in "Still missing" has no published figure in the sources checked. Nothing here was filled in by adding one citation to another.

## Bridge

**Type.** Semi-circular arch, one span. The Canadian Consulting Engineer article says "a unique semi-circular arch spanning 20 metres," supported on "7 metre high walls" (Canadian Consulting Engineer, "Three Crossings on Henday"). discoverAPEGA gives the same 20 m span. The article gives no rise for the arch. Rise is missing.

**Spans.** One arch span of 20 m, by both sources above. Span count is one. The sources do not describe a second span or a multi-span structure. The 2019 aerial shows the arch ends on both sides of the highway. It does not show a second span. Neither source is a structural drawing. Treat "one span, 20 m" as the published figure, not a checked dimension.

**What the arch carries.** Two sources disagree in wording.
- The CCE article says the highway is above the arch and the path is inside it. It says "the pedestrian-bike path is raised within the arch, 7 metres above the creek."
- discoverAPEGA says the arch sits "beneath the highway on the city's southside," and that the arch "carries both a wildlife pathway and a pedestrian walkway."
- A search summary said the arch carries the Henday over the creek. That summary is not the article text. The primary text says the highway is above the arch.

The two sources agree the highway is above and the creek and path are below. Neither says which carriageway or lane is over which part of the arch.

The user confirmed on 2026-11-23 that the highway is carried over the ravine. That is the user's observation, not a published source. It settles the direction of the wording above: the highway is the deck and the arch is below it.

**Arch depth, soffit, deck above the creek.** The path is 7 m above the creek (CCE, discoverAPEGA). The highway deck above the arch is not given in either source. The highway deck height above the creek is missing.

**Piers and abutments.** The CCE article says the arch is supported on 7 m high walls. It gives no pier count and no footing. The walls are the nearest to a support description.

**Clearance.** Missing. No vertical clearance under the highway is published.

**Sidewalks.** The arch carries a pedestrian-bike path. Its width is not published.

**Rehabilitation.** Completed 2005 (CCE, discoverAPEGA). The CCE article says the crossing was built on a former coal-mining area, so foundations were difficult. It gives no later widening or rehabilitation. None is listed in the sources checked.

**Oculus.** discoverAPEGA says "a giant oculus opens the centre of the arch." The 2019 City aerial shows a round dark opening in the median between the two carriageways, on the arch centreline. That reading fits the oculus. The size of the opening is not published.

## Approaches

The OSM extract gives both carriageways as separate ways, chained through the bridge pieces. Plan lengths are horizontal WGS84 lengths along the mapped nodes. They are not grade or climb figures.

**Eastbound, west side.** Way 1289815290 (1,011.6 m, then way 542172228 at 589.1 m, then way 1577455879 at 171.2 m) reaches the west end of the eastbound bridge piece. Way 1289815290 and way 758869440 carry OSM `maxheight=5.5`. That is a mapper tag. It is not a clearance measurement and is not used here.

**Eastbound, east side.** Way 1388870988 (458.0 m) starts at the east end of the eastbound bridge piece. It continues east toward 111 Street. The OSM extract does not show where the east approach meets grade.

**Westbound, east side.** The westbound east approach is not in the OSM extract. The westbound bridge piece's east end is at 53.428792, -113.562691. No way starts there in the extract.

**Westbound, west side.** Way 1577455880 (447.0 m) leads west from the westbound bridge piece, then way 758869440 (1,097.6 m) leads northwest toward Rabbit Hill Road.

**Grade.** No source gives the present gradient, the elevation change, or the point where either carriageway meets natural grade. The ways are tagged `highway=motorway`, `lanes=3`, `maxspeed=100`, `width=11.1` on most segments. Those are mapper tags, not design figures.

## Deck

**Elevation.** Missing above sea level. The datum is missing.

**Elevation above the creek.** The path is 7 m above the creek (CCE, discoverAPEGA). The highway deck above the creek is missing.

**Thickness.** Missing.

**Width.** The OSM tag `width=11.1` on the eastbound and westbound motorway ways is a mapper tag. It is not a published carriageway width. Lane count is 3 per direction in OSM. No published lane count is given.

**Crossfall and longitudinal grade.** Missing.

## Still missing

- The highway deck type and depth over the arch. Whether it is a deck on the arch or fill on the arch. The sources say "beneath the highway," not how the highway is carried. The user confirms the highway is carried over the ravine; the structural form of that carrying is still unpublished.
- Arch rise and soffit height.
- Clearance under the highway.
- Deck elevation above sea level, with the datum.
- Height of the highway deck above the creek.
- Ravine width and depth as measured. The CCE article gives 300 m wide and 18 m deep. OSM does not map the ravine width, and the 2019 aerial does not show a 300 m valley at this scale. The two figures are not reconciled.
- Pier or wall count and footing detail.
- Path width.
- Westbound east approach ways.
- Gradients and grade points on each approach.
- Inventory record for this structure in Alberta Transportation's TIMS export. The Structure-Export.csv was not reached.
- A photo that confirms the span count. No open-licence photo was downloaded. See SOURCES.md.
- A control survey of the centre. The centre is from the OSM geometry and the 2019 aerial, not a survey.
