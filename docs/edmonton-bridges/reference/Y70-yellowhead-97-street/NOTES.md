# Y70 Yellowhead / 97 Street: modeling brief

Edmonton. A single-span concrete overpass carries 97 Street NW over Yellowhead Trail (Alberta Highway 16). It is part of the Yellowhead interchange at 97 Street. The Alberta record gives the year in service as 1982. Wikipedia gives 1982 too, citing two sources. The lanes run east and west under the deck. 97 Street runs north and south over them.

Centre used: 53.581278, -113.492106. This is the Alberta record point (STRU_ID 41052). The Y70 estimate in PRIORITY.md and in bridge-geometry.json is 53.578, -113.489. That estimate is 418 m south-east of the record point. It was not used. The record is a found position on the structure, so it takes priority over the estimate. The cached Y70 object had no bridge or road ways at all. Its centre is marked as estimated.

This is not Y69 (St. Albert Trail), which is about 4.3 km west. It is not Y71 (82 Street), which is about 1.6 km east. It is not H45, which is the 97 Street overpass of Anthony Henday Drive at the north end of the city (Alberta record 85093). It is not the CN rail overpass over 97 Street (CNR / 97ST, records 39678 and 41618). That rail structure is about 260 m north of this point. Rail is on top there, and 97 Street is underneath.

Which road is on top: 97 Street. The Alberta record name is "97 STREET - YELLOWHEAD TRAIL (B186)". The location text is "97 STREET OVER YELLOWHEAD TRAIL INTERCHANGE AT EDMONTON". The record's own fields agree. The file puts the structure on a local road and over Highway 16, control section 17, at km 10.768 on the left lane and 10.770 on the right lane. OpenStreetMap agrees: the Yellowhead ways beneath are tagged layer -1.

## Bridge

**Type.** One-span concrete overpass. The Alberta record has one span, a span length of 27.9 m, and a span-type code of PJ. The code is not labelled in the file, so the superstructure type is not published. The record gives the deck as precast concrete with a high-density concrete wearing surface. The span is not described as a girder, arch, or truss.

**Spans.** One span. Span 27.9 m (Alberta record, LENGTH_SPAN_1, MAX_SPAN_LENGTH and NOMINAL_BRIDGE_LENGTH). Theoretical bridge length 30 m (Alberta record, THEORETICAL_BRIDGE_LENGTH). The 27.9 m and the 30 m are both published. They were not averaged. The OpenStreetMap deck way is 24.6 m long in plan (way 472577432). That is a plan length, not a structural length.

**Length.** Nominal bridge length 27.9 m (Alberta record). Theoretical length 30 m (same record). Skew 4 degrees (same record).

**Depth.** Not published. No girder, slab, or box depth is given.

**Piers.** None. The structure is one span. The record gives the abutments as pile foundations on concrete.

**Clearance.** Not published. The record's theoretical and measured vertical clearance under the structure are blank. No navigation clearance applies. No elevation above sea level is published for the deck, the soffit, or the road below.

**Sidewalks.** Not published as widths. The OpenStreetMap deck way is tagged `sidewalk:both=separate`. That tag does not give a width.

**Widening or rehabilitation.** No rehabilitation is described in the sources found. The Alberta record was last inspected on 9 October 2025. Its sufficiency rating is 42.3, its condition rating is 44.4, and its estimated remaining life is 6 to 10 years. The replacement cost is $6.1 million, with an estimated replacement year of 2036. The St. Albert Trail to 97 Street project is under construction and is targeted to finish in 2027. Its City page could not be read (HTTP 502). The sources do not say whether this structure will change.

## Approaches

**South, 97 Street.** OpenStreetMap way 472577429 is 124.7 m in plan. It runs from the south end of the deck. Its sidewalks are tagged separate. Way 476073031 continues south for 395.4 m in plan. Both ways are plan geometry only. No gradient, elevation change, or grade point is published.

**North, 97 Street.** OpenStreetMap way 472577426 is 45.6 m in plan. It starts at the north end of the deck. Way 62232309 continues north for 118.9 m. That way carries the Highway 28 reference. The sources give no gradient or grade point for either end.

**Yellowhead Trail.** The Yellowhead ways beneath the deck are 22916204 (59.5 m) and 80403108 (54.4 m, a second carriageway). The OpenStreetMap tags for both are `layer=-1` and `tunnel=yes`. Those are the mapper's underpass tags. They do not show a tunnel. The Yellowhead approaches run east and west past the ramps. Their grades are not published.

**Ramps.** Twenty-four motorway ramp ways lie within 150 m of the record point. Their plan lengths are in `geometry.json`. They belong to the interchange, not to the deck. Wikipedia's interchange table gives the 97 Street interchange as a single-point urban interchange. That row has no citation.

## Deck

**Elevation.** Not published, above sea level or above the road beneath. No vertical datum is given.

**Thickness.** Not published. The precast deck and the wearing surface are named, with no depth.

**Width.** Total clear roadway 29.3 m (Alberta record). The record also gives a gross deck width of 64 m. Both are published values. The file does not say what the 64 m covers. The two values were not reconciled. Neither is a lane or shoulder width.

**Lanes.** The OpenStreetMap tags on the deck way say 7 lanes: 3 forward, 3 backward, and 1 reversible (lanes:both_ways). No lane width is published. The Alberta record does not give lane counts.

**Sidewalks or paths.** The sidewalks are tagged separate on both sides by OpenStreetMap. Widths are not published. Four short footway and path ways sit at the ramp terminals, at grade. They are listed in `geometry.json`. They are not on the deck.

**Crossfall.** Not published.

**Longitudinal grade.** Not published.

## Still missing

- Deck elevation above sea level, and the vertical datum. Soffit elevation.
- Clearance from the road below to the soffit. The record's theoretical and measured vertical clearance are blank.
- Superstructure type and depth. The span-type code PJ is not labelled.
- Lane widths, shoulder widths, and sidewalk widths.
- What the 64 m gross deck width covers.
- Crossfall, and the longitudinal grade of the deck and both approaches.
- The gradient and grade point of each approach, north and south. The gradient and grade point of Yellowhead on each side.
- The St. Albert Trail to 97 Street City project page, which returned HTTP 502 twice. Whether this structure is changed by that project.
- A Structurae or City engineering record for this structure. None was found.
- An openly licensed photograph of the structure. None was found.
