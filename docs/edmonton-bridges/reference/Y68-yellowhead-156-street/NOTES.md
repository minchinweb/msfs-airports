# Y68 Yellowhead / 156 Street: modeling brief

Edmonton. A grade separation where 156 Street NW passes over Yellowhead Trail (Alberta Highway 16). Opened in 2007 (Alberta Transportation inventory, STRU_ID 148330). The road on top is 156 Street. Yellowhead Trail runs underneath, east-west, on the west side of the city. Highway 16 is the road below, not the road above.

Centre used: 53.5789116, -113.5906984, from the Alberta inventory point for this structure. The PRIORITY.md and bridge-geometry.json estimate of 53.578, -113.596 is about 364 m west of it and was not used. The estimate came from the street grid. The inventory point is a government record, and the OSM deck way 25532547 starts within about 1 m of it. So the record point is the better centre. It is still an inventory point, not a survey. Its coordinates are not labelled with a datum.

This is not Y67 (Yellowhead / 170 Street), the exchange to the west. It is not Y69 (Yellowhead / St. Albert Trail), the exchange to the east. It is not the CN rail overpass on 156 Street, which is a separate structure about 200 m north (STRU_ID 148332). Nothing here comes from another folder.

The name and the record agree. The Alberta record for STRU_ID 148330 reads "156 ST AND YELLOWHEAD TRAIL (HWY 16) GRADE SEPARATION", with 156 Street carried and Highway 16 over. That is a grade separation with 156 Street on top.

Numbers below are cited. Where sources disagree, both are given. Nothing is averaged. OSM `maxheight` and `width` tags are mapper tags, not deck elevations.

## Bridge

**Type.** Two-span bridge. The Alberta record gives span type code "WG", with no label in the file. It gives the wearing surface as polymer modified asphalt (Alberta Transportation, Structure-Export.csv, STRU_ID 148330). The record does not name the superstructure material or the girder type. Girder depth is not published.

**Spans.** 33.5 m and 30.0 m (Alberta, STRU_ID 148330). Units are not labelled in the file. They are treated as metres here, because the OSM carriageway plan lengths (64.0 m and 64.5 m) match a 63.5 m total. Only two spans are listed. The record has blanks for spans 3 to 5.

**Length.** Nominal bridge length 63.5 m (Alberta). The OSM carriageway plan lengths are 64.5 m (northbound, way 25532547) and 64.0 m (southbound, way 38071214). These are horizontal lengths along the mapped centrelines. They are not structural lengths. Both are published as found. They were not averaged.

**Girder or arch depth.** Not published.

**Piers.** The Alberta record gives pier cap and pier shaft both as concrete. A two-span bridge has one interior support line. That count is inferred from the span count, not stated in the record. The record gives no pier footing, pier height, or pier width.

**Abutments.** Abutment foundation type and material are blank in the Alberta record.

**Clearance under.** Measured vertical clearance under the structure: 5.3 m (Alberta, MEAS_VCL_UNDER_STRUCTURE). Theoretical vertical and horizontal clearances are blank in the record. OSM tags the two Yellowhead carriageways under the bridge with `maxheight=5.6` (ways 937503510 and 937503512). OSM tags a ramp at about the same point with `maxheight=5.3` (way 61241727, from CanVec). Those are mapper tags. The published figure is the 5.3 m measured in the inventory. The OSM 5.6 m was not used in its place.

**Sidewalks.** Not stated in the Alberta record. OSM has a footway tagged `bridge=yes` on the west side of the southbound carriageway (way 1529521611, 65.0 m). It is a mapper tag. The Alberta record does not confirm a sidewalk.

**Rehabilitation.** No rehabilitation is recorded in the sources checked. The Alberta record shows the structure in service since 2007, last inspected 4 July 2025, with sufficiency 52.9 and condition 61.1 (Alberta). The Wikipedia article describes the 156 Street interchange as opened in 2007 and gives no later rebuild for this bridge. The City freeway-conversion project covers the Yellowhead segment from 156 Street to St. Albert Trail. The City pages for that project returned HTTP 502 on 2026-11-23, so their text was not read. Whether the 156 Street bridge itself was rebuilt in that project is not confirmed.

## Approaches

**North end of each deck, toward the CN rail overpass.** The northbound carriageway (way 25532547) rises from the south. Its approach chain is six OSM ways from about 53.5753 N to the deck start, with plan lengths 108.5, 70.7, 72.3, 10.9, 66.3 and 74.8 m (ways 1282837620 to 38110082). The chain is three lanes in places and four in others, and the OSM lane tags differ between ways. A plan length is not a grade distance. No gradient is published for either end.

**North, between the deck and the CN overpass.** Three short OSM ways (25532551, 61333603, 38071215) carry 156 Street north from the Yellowhead deck toward the CN rail overpass. They total about 142 m of plan length. They end at the CN structure, which is a separate record (STRU_ID 148332, 39.24 m, built 2006). They are not part of the Yellowhead grade separation.

**South end of the southbound deck.** The southbound carriageway (way 38071214) continues south through four ways (472627675, 472627674, 1339751354, 38071213), with plan lengths 64.4, 70.9, 11.0 and 356.7 m. The last way ends at about 53.5744 N, at its own last node. That is not a grade point. The OSM extract box did not cut this chain.

**Gradient and elevation change.** Not published. The Alberta record gives no approach grade, no deck height above the road below (DECK_HEIGHT is blank), and no approach grade point. No source found gives the change in elevation between the 156 Street grade and the Yellowhead roadway. No source found gives where either road meets natural grade. Nothing here adds or subtracts a citation to estimate one.

**Approach roadway width.** Blank in the Alberta record (APPROACH_ROADWAY_WIDTH). The OSM approaches carry no width tags.

## Deck

**Elevation.** Not published. The Alberta record has no deck elevation above sea level, and no datum. No Alberta bridge sheet with an elevation was found. Environment Canada gauge 05DF001 is at the Low Level Bridge and is not relevant to this crossing. No conversion from that gauge was made.

**Thickness.** Not published. The Alberta record gives the wearing surface type (polymer modified asphalt), not its depth.

**Width.** Gross deck width 30.8 m (Alberta, STRU_ID 148330). Total clear roadway 21.3 m (Alberta). Those are the published figures for the whole crossing. The two OSM carriageway ways carry no width tags. Their footprint, way 1137993242, is about 42 m east-west and about 74 m north-south from its nodes. That is an OSM outline, not a published width.

**Lanes.** OSM tags the northbound deck as three lanes (way 25532547) and the southbound deck as two lanes (way 38071214). The Alberta record gives no lane count. The two counts are both OSM mapper tags. The total is not confirmed by a published source.

**Carriageways.** The two carriageways are one-way and separate. Node order on the northbound way runs south to north. Node order on the southbound way runs north to south. Both lie on the same alignment about 28 m apart, from the stored nodes.

**Sidewalk or path.** One footway on the west side of the southbound carriageway (way 1529521611, 65.0 m). The Alberta record does not give a sidewalk width. The side of the northbound carriageway has no mapped footway on the deck.

**Crossfall.** Not published.

**Longitudinal grade.** Not published.

## Still missing

- Deck elevation above sea level and the vertical datum. No soffit or road elevation.
- Girder or arch depth, and the girder type. The Alberta record gives only the span type code "WG".
- Pier count and pier height. The Alberta record gives the span count but not the pier count separately.
- Approach gradients and the points where each approach meets grade.
- Sidewalk width. Sidewalk presence is mapped in OSM only.
- Lane count, lane width and shoulder width from a published source.
- Whether the 156 Street deck was widened or rebuilt in the City freeway-conversion work. The City pages were not readable on 2026-11-23.
- Open-licence photographs of the structure. None were found on Wikimedia Commons (see SOURCES.md).
- Wikipedia gives the interchange type as "partial cloverleaf" in its table, uncited. A mirrored copy of Wikipedia gives "folded diamond". The two are not reconciled.
