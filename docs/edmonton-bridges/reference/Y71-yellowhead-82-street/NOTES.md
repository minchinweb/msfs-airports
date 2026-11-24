# Y71 Yellowhead / 82 Street: modeling brief

Edmonton. A single-span concrete overpass carries 82 Street over Yellowhead Trail (Alberta Highway 16). Alberta record 41170 names it 82 STREET - YELLOWHEAD TRAIL (B224). The record says it went into service in 1988. The City of Edmonton owns and manages it.

Centre used: the Alberta record point, 53.582152, -113.467305. It is not the PRIORITY.md estimate, 53.578, -113.462. That estimate is 579 m south-east of the record. The cached Y71 object in bridge-geometry.json was centred on the estimate. Its bridge ways are Capital Line light rail and a disused rail yard about 1.3 km away. So the cache does not describe this crossing. Geometry in this folder comes from a live OpenStreetMap extract centred on the record point.

Which road is on top: 82 Street. The record name reads "82 STREET OVER YELLOWHEAD TRAIL AT EDMONTON". Its LOCATED_OVER field is Highway 16, control section 17, km 12.425 (L1) and 12.429 (R1). Its LOCATED_ON road field is blank. The name and the over-field agree. In OpenStreetMap the Yellowhead carriageways beneath are tagged layer -1 and tunnel=yes. Those tags mark an underpass here, not a tunnel.

Lanes run north-south on 82 Street, with one carriageway each way. Yellowhead runs east-west under it, one carriageway each way. The Alberta export does not give lane counts.

This is not Y70 (Yellowhead / 97 Street, record 41052, 53.5813, -113.4921). It is not Y72 (Yellowhead / Wayne Gretzky Drive), which is further east. It is not the CNR rail overpass on 82 Street, record 41690, about 165 m north of this point. That is a rail structure, not this one, and nothing here is modelled from it. The Alberta export has no other in-service structure within 400 m of the point. Four PROPOSED records (2086649, 2086650, 2086652, 2086654) are planned sign or tube structures. None is built, and none is used.

## Bridge

**Type.** Single-span structure, recorded as MAJOR BRIDGE. Precast concrete deck with a concrete wearing surface (Alberta record 41170: DECK_MATERIAL "Precast CONCRETE", WEAR_SURFACE_TYPE "CONCRETE; CLASS B"). The export gives span-type code CXP. The code is not labelled, so it is not interpreted here.

**Spans.** One span. 34.2 m (LENGTH_SPAN_1, NOMINAL_BRIDGE_LENGTH and MAX_SPAN_LENGTH all read 34.2). The theoretical bridge length field is blank. No other span length is published.

**Length.** 34.2 m nominal (Alberta record 41170). That is the only published length. It is not the length of the 82 Street deck along the road.

**Depth.** Girder or slab depth is not published.

**Piers.** None. The structure has one span, and the export has no pier fields. Abutment foundation fields are blank in the export.

**Clearance.** Theoretical vertical clearance under the structure: 5.2 m (THEOR_VCL_UNDER_STRUCTURE). Theoretical horizontal clearance under: 5.2 m (THEOR_HCL_UNDER_STRUCTURE). The measured clearance fields are blank. These are theoretical figures. OSM maxheight=5.2 on the eastbound underpass way (80402688) gives the same number. That matches a published figure. It is not a surveyed clearance.

**Sidewalks.** Left and right sidewalk width fields are blank in the export. No sidewalk width is published.

**Widening or rehabilitation.** None recorded. The export gives in-service year 1988, sufficiency 50.2, condition 72.2 and last inspection 5 July 2024. Wikipedia's Yellowhead Trail article says interchanges opened at 82 Street in 1988. No later rebuild is recorded in the sources checked. The City's Yellowhead Trail Freeway Conversion page lists 82 Street as an existing interchange inside the conversion limits. It describes no change to the 82 Street structure.

## Approaches

Nothing is published about the approach gradients, the elevation change, or where either road meets natural grade. The OSM ways below are plan geometry only.

**82 Street, south of the deck.** Northbound way 46894306: 69.5 m, lanes tagged 4 with a left-turn lane. Southbound way 440558308: 67.6 m, lanes tagged 3. Both run from the deck to a far node about 80 m from the record point.

**82 Street, north of the deck.** Northbound: way 472538989 (50.0 m), then way 472538993 (100.7 m). The far node of 472538993 is about 179 m from the record point. Southbound: way 472538995 (75.8 m), then 1513039275 (36.9 m), then 472538997 (163.9 m). The far node of 472538997 is about 305 m from the record point. Lanes tagged 3 to 5. The maxheight=4.2 tags on 1513039275 and 472538997 are mapper tags. They are not published clearances.

**Yellowhead, both sides of the underpass.** Eastbound at grade west of the underpass: way 1285856992, 333.4 m. Westbound at grade west: way 61480209, 690.8 m, which runs well past the 150 m footprint. Eastbound at grade east: way 61345250, 414.2 m. Westbound at grade east: way 1289101911, 318.4 m. Each is a whole way. None is a grade point.

**Carriageway split.** The two 82 Street carriageways are about 11 m apart on the OSM centrelines at the crossing. That is plan separation, not a deck width.

## Deck

**Elevation above sea level.** Not published. No vertical datum is given in the export.

**Elevation above the road underneath.** 5.2 m theoretical vertical clearance under the structure (Alberta record 41170). The measured value is blank.

**Thickness.** Not published. The export gives no slab or girder depth.

**Width.** The export gives TOTAL_CLEAR_ROADWAY 24.1 m, with a range of "> 10 m". It also gives GROSS_DECK_WIDTH 84. The export does not label that unit, so it is not converted. Width of each carriageway is not published.

**Lanes.** OSM tags the 82 Street ways lanes=3 in each direction. That is a mapper tag, not a published lane count.

**Sidewalks or paths.** Not in the export. The OSM ways tagged as sidewalk or footway near the crossing are at grade. They are listed in geometry.json under paths, and none is tagged as part of the bridge.

**Crossfall.** Not published.

**Longitudinal grade.** Not published. The export has a grade field, STRUCTURE_GRADE_PERCENT, and it is blank.

**Plan lengths of the crossing pieces.** The northbound pieces are 21.8 m and 19.9 m, a total of 41.7 m. The southbound pieces are 21.1 m and 21.0 m, a total of 42.1 m. These are plan lengths along the OSM ways. They are not the 34.2 m span.

## Still missing

- Deck elevation above sea level and the vertical datum.
- Measured clearance under the structure. The export gives only the theoretical 5.2 m.
- Girder or slab depth, bearing type, and any cross section.
- Abutment and pier details. The export fields are blank.
- Sidewalk and lane widths, crossfall, and longitudinal grade.
- Approach gradients, the elevation change, and where each road meets grade.
- Rehabilitation or widening records for this structure.
- Open-licence photographs of the elevation, the underside, or the piers. None found. See SOURCES.md.
- Not searched in this pass: Structurae, engineering papers, Edmonton City as Museum, and City bridge inspection or design records.
- Skew. The export's SKEW_DEGREES field is blank.
