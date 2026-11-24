# Y69 Yellowhead / St. Albert Trail: modeling brief

Edmonton. A City-owned two-span concrete bridge carrying St. Albert Trail over Yellowhead Trail (Alberta Highway 16) at the interchange on the west side of the city. Alberta records first service in 1982. The St. Albert Trail deck is the top road. Yellowhead Trail runs east-west underneath.

Centre used: 53.580893, -113.556664. This is the Alberta record point for STRU 40995. It is not the PRIORITY estimate of 53.578, -113.548. That estimate is about 0.66 km south-east of the record point. The cached Y69 object in `bridge-geometry.json` has no bridge ways, so it was only used to search. The record point was found in the Alberta CSV by name and by location.

Not Y68 (Yellowhead / 156 Street, to the west). Not Y70 (Yellowhead / 97 Street, to the east). The CNR overpass STRU 40108 (B096) is about 0.33 km north-north-west and crosses local roads, not Yellowhead. The pedestrian bridge STRU 233733 (B403) crosses Yellowhead at this point, but it is a separate record. It is listed under paths in `geometry.json`, not as a deck.

Which road is on top: St. Albert Trail. Alberta STRU 40995 is named "ST. ALBERT TRAIL OVER YELLOWHEAD TRAIL INTERCHANGE AT EDMONTON", and it is over Highway 16 at km 6.466. Wikipedia's Yellowhead Trail article says the expressway "passes underneath St. Albert Trail". The Alberta record lists the road on top as a local road, not Highway 2. Highway 2 leaves Yellowhead at this interchange and runs north into St. Albert.

## Bridge

**Type.** Alberta gives span type code RM. The file does not label the code. No source describes the superstructure type. Deck material is precast concrete with a high-performance concrete wearing surface. Piers and pier caps are concrete. Abutments sit on pile foundations.

**Spans and length.** Two spans of 23 m each (Alberta). Nominal bridge length 46 m. Maximum span 23 m. Skew -24 degrees (Alberta). OSM carriageway ways are 39.2 m and 34.7 m long in plan. These are centreline plan lengths, not the structural length. The two figures are not reconciled.

**Girder, arch or truss depth.** Not published.

**Piers.** Two spans imply one interior support. Alberta does not give a pier count or pier type. It gives concrete pier cap and concrete pier shaft materials only.

**Clearance.** Alberta gives a theoretical vertical clearance under the structure of 5.4 m. The measured vertical clearance field is blank. Alberta gives a theoretical horizontal clearance under the structure of 5.4 m. OSM tags maxheight=5.3 on the Yellowhead motorway ways beneath. That is a mapper tag on the road, not a surveyed clearance. The Alberta value 5.4 m and the OSM tag 5.3 m are both recorded. They are not averaged.

**Sidewalks.** Not published for this structure. Alberta gives a gross deck width of 29.5 m and a total clear roadway of 21.5 m. The split between roadway, median, barrier, and sidewalk is not given.

**Widening or rehabilitation.** No rehabilitation date is given in any source reached. Alberta shows a sufficiency of 46.6, a condition of 61.1, and last inspection on 3 October 2025. Alberta lists an estimated replacement year of 2041. A search snippet quoting a City of Edmonton page for the 156 Street to St. Albert Trail segment mentions "retaining walls under the St. Albert Trail bridge". The City page itself returned HTTP 502. The later St. Albert Trail to 97 Street project shows an all-directional interchange at St. Albert Trail in its 2023 draft. No source reached says whether this bridge is replaced.

## Approaches

Both ends are the St. Albert Trail. Each end is listed separately in `geometry.json`. The OSM approach ways are plan geometry only. OSM does not record gradient or elevation.

**South end.** The at-grade St. Albert Trail approach runs north into the deck. Plan lengths for the short legs are 5.1 m, 12.7 m, 25.9 m, 29.4 m and 31.9 m. A primary_link ramp and a trunk_link ramp also meet this end. Gradient and elevation change: not published.

**North end.** The St. Albert Trail continues north from the deck. The first legs are 11.8 m and 15.8 m. A 152.1 m primary way runs north from there. Gradient and elevation change: not published.

**Carriageways.** OSM maps St. Albert Trail as two one-way carriageways on the deck, each with its own approach. The split on the approaches is in `geometry.json`. The deck carriageways are one-way and carry the two directions.

**Road labels.** Some Yellowhead ways in OSM carry ref=2. Alberta and the other tags give Highway 16. The ref is recorded as mapped and not corrected.

**Where each road meets grade.** Not published.

## Deck

**Elevation above sea level, datum.** Not published. No source gives the deck or road elevation at this point.

**Elevation above the road underneath.** Alberta theoretical vertical clearance 5.4 m. OSM maxheight 5.3 m on the Yellowhead ways (a mapper tag). No surveyed figure found.

**Thickness.** Not published.

**Width.** Gross deck width 29.5 m (Alberta). Total clear roadway 21.5 m (Alberta). Width of each carriageway: not published. OSM tags 4 lanes on each deck carriageway (mapper tag).

**Lanes.** Two carriageways, one-way each, as mapped in OSM. The number of lanes per carriageway is a mapper tag only.

**Sidewalk or path.** The pedestrian and cycle bridge STRU 233733 (B403) crosses Yellowhead at this point. It is 2010 construction, two 23 m spans, nominal 46 m, gross width 4 m, total clear roadway 3.7 m. OSM has it as a 46.9 m cycleway bridge, concrete, bridge=yes, layer 1. Its position relative to the St. Albert Trail deck is not stated in the sources. Its width is not part of the St. Albert Trail deck width.

**Crossfall.** Not published.

**Longitudinal grade.** Not published.

## Still missing

- Deck and road elevations above sea level, and the datum.
- Girder or superstructure depth and type.
- Pier count, pier type, and pier dimensions.
- Gradient and elevation change on each approach.
- Carriageway widths and the split of the 29.5 m gross width.
- Sidewalk and median widths.
- Crossfall and longitudinal grade.
- Any rehabilitation or widening date for this structure.
- Whether the bridge is replaced in the St. Albert Trail to 97 Street project. The City pages returned HTTP 502.
- Open-licence photographs of the structure, the piers, the deck, or the approaches. None was found on Wikimedia Commons in the searches. See SOURCES.md.
- Structurae, HistoricPlaces, and Edmonton City as Museum records for this structure. The searches returned none.
- A Mapillary frame that shows the bridge. The three usable frames are within 60 m and show the approaches only. See `street/SOURCES.md`.
