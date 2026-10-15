# T133 Stony Plain Road replacement — modeling brief

Stony Plain Road and the Valley Line West over Groat Road. Centre used by the project: 53.5478, -113.5458. Model the finished bridge.

## What it is

The finished bridge is one span, with the road and the light-rail tracks on the same deck.

G118 is the old span. It was demolished from 29 December 2022 to 3 January 2023 (Marigold). The City's project history says the demolition took six days, in late December 2022 and early January 2023. The old span is not to be modeled. No G118 folder was written. Alberta file B055, Stony Plain Road over Groat Road, year 1954, row prints GF 3. That is the demolished bridge. The other numbers on that row were not used as the new span length.

Way 25601841 is still tagged bridge:name Groat, Stony Plain Road NW. Its horizontal length is 60.7 m. That mapped length is not the new structural span length.

This is not the river span. Do not reuse the river span's lengths, the east path width, or the pier notes. The 4.2 m sidewalks below are this bridge's own requirement.

## Bridge

**Type.** Single span, no piers. The Valley Line West project agreement, Schedule 5 Part 4, section 4-3.2, requires a span length of a minimum of 46 m (4-3.2.2.1.A), integral abutments and no deck joints (4-3.2.8.A), a full-depth cast-in-place concrete deck (4-3.2.9.A), and a trackway slab built separately from the bridge deck and the approach slabs, reinforced across the interface (4-3.2.12.A). Those are requirements, not as-built measurements.

The site location study and the EIA final report, section 4.3, describe the reference design as a single-span steel haunched girder, on concrete abutments on piles. Steel girders were set from 7 p.m. on 10 August 2023 to 6 a.m. on 14 August 2023 (Marigold). The City's 2023 third-quarter dashboard records the girders as installed in August 2023. Transforming Edmonton says each girder weighed 78,000 kg, and names a Liebherr LTM1400-7.1. It does not say the installed girders are haunched, and it does not give a girder count. Haunched is the reference design. Girder depth is not published. The same page says an unloaded light-rail vehicle is about 64,000 kg. That is the vehicle, not the girder.

**Spans.** One. No piers. The 46 m is a minimum. It is not an as-built length.

The EIA says the replacement is slightly shorter than the existing bridge by about 8 m, because the abutments change. That sentence is a comparison. It is not a length. It was not subtracted from 60.7 m or from any Alberta figure.

**Clearance.** Section 4-3.2.2.1.B requires a minimum vertical clearance of 6 m over Groat Road. That is a minimum. It is not a deck elevation, and it is not exactly 6 m. The EIA says the vertical clearance under the replacement remains the same as the existing bridge, and it does not give that height. A wildlife note in the EIA says the old west abutment bench offered about 4.0 m under the old girders. That 4.0 m is the old bench. It is not the road clearance and not the new bridge.

Schedule 5 Part 3 has a separate sentence about a 6 m wide service road between Woodbend Place and Sylvancroft Lane. That 6 m is not this clearance and not this span.

**Width.** The site location study says the reference design is 25.4 m wide, against an existing 18.4 m. The same study says two centre LRT tracks, two outside vehicle lanes, and two 4.2 m sidewalks. The agreement says a north sidewalk of minimum 4.2 m and a south shared-use path of minimum 4.2 m (4-3.2.4). Both wordings are kept. The 4.2 m figures are this bridge. They are not the river bridge's east path.

Section 3-2.11.8.B of Schedule 5 Part 3: across this bridge, the lane width between the lip of gutter next to the trackway and the face of barrier next to the sidewalk or shared-use path is a minimum of 4.0 m.

**What opened.** The City's project history says the road and bridge reopened to vehicles and pedestrians on 30 November 2024, with the tracks in the middle, one lane each way, and a shared-use path. That sentence does not mention the north sidewalk. Marigold's pages say one vehicle lane each direction, LRT tracks, a sidewalk, and a shared-use path on the south side. A 2026 mid-season update says pedestrian rail is installed, LRV barrier railing is installed, and most of the track slab is complete between the bridge and Grovenor / 142 Street. The line is not in service. No City opening date for the LRT was found in the pages read.

**Other agreement figures.** All of these are requirements. Exposed abutment seat height no greater than 1.2 m (4-3.2.8.B). Concrete slope protection is not required unless the geotechnical design requires it (4-3.2.8.C). ACP wearing surface minimum 80 mm (4-3.2.3.C). Waterproofing to Alberta Transportation drawings S1838-17, S1839-17, and S1840-17. High-performance concrete for the decks, trackway slabs, curbs, barriers, sidewalks, abutment roof slabs, approach slabs, sleeper slabs, diaphragms, and the upper 300 mm of the backwalls. TL-4 single-slope concrete barrier with a steel bicycle railing; top of steel rail to top of concrete a minimum of 0.37 m; bicycle railing on both outside edges (4-3.2.10). Minimum longitudinal grade 0.5 percent. Travel lanes a minimum transverse grade of 2 percent away from the centre unless superelevated. Sidewalk and shared-use path slope 2 percent toward the roadway (4-3.2.11). Water is not discharged onto Groat Road or the headslopes. Existing foundations abandoned (4-3.2.7). The existing retaining wall on the west side of Groat Road is not modified. The existing sidewalk is expanded over the area of the old piers. A wildlife crossing bench sits at mid-height of each abutment headslope, with no added fill, on 300 mm of compacted clay (4-3.2.15). The agreement spells "Stoney Plain" once, in the instrumentation sentence. The heading is Stony Plain.

The EIA also estimates a 28 m MSE wall at the southeast end, about half of it inside the bylaw boundary. The east abutment is shifted slightly south. The horizontal alignment is slightly curved. The vertical profile remains the same. No elevation is given for that profile.

## Approaches

The ways are stored on the G118 object in bridge-geometry.json. The code in geometry.json is T133. lrt-tracks.json routes 13 and 14 are the full Valley Line West construction centrelines, each about 14.1 km. They pass near this centre. They are not a span, and their node lists are not in geometry.json.

Mapped lines on the bridge tag. These horizontal lengths are not the structural span:

- Way 25601841, north carriageway, Stony Plain Road NW, two lanes, one-way, 60.7 m. Node order east to west. Do not use 60.7 m as the new span length.
- Way 1352501168, south carriageway, two lanes, one-way, 57.3 m. Node order west to east.
- Way 1160377622, Valley Line, railway=construction, 58.2 m, west to east, between the road ways.
- Way 1222393198, Valley Line, railway=construction, 58.2 m, east to west.
- Way 1229761596, footway, concrete, 58.4 m, north of the north carriageway.
- Way 1229761594, cycleway, concrete, 57.5 m, south of the south carriageway.

The City says one vehicle lane each way. The map says two lanes on each road way. Both are kept.

A live read of the Valley Line ways also has gauge=1435, voltage=750, electrified=contact_line, frequency=0, opening_date=2028, and check_date=2023-11-04. Those are mapper tags. opening_date=2028 is not a City date. The check date is before the 30 November 2024 road reopening. A live read of the road ways also has hgv=no. That tag is not a clearance and not a deck elevation.

Road ways leaving the bridge tag include way 1352501163, one lane, one-way, 134.4 m; way 1248168351, four lanes, one-way, 67.1 m; way 1081194111, four lanes, one-way, width tag 12.2, 19.3 m; and way 692115845, one lane, one-way, width tag 4, 988.3 m. The width tags are not published widths. The 988.3 m way is Stony Plain Road continuing. Its far node is not grade. The Valley Line ways stored as approaches are 1,599.9 m, 1,602.0 m, 2,603.7 m, and 2,608.0 m. They are the line leaving the bridge. They are not the span.

Groat Road underneath includes way 521661798, 122.6 m; way 1102766309, 99.3 m; way 521661800, 274.8 m; and way 37749243, 1,124.7 m. No maxheight tag is stored on these four. No published clearance other than the 6 m minimum was found.

## Deck

**Elevation.** Not published. The 6 m figure is the minimum clearance over Groat Road. Gauge 05DF001 was not converted.

**Cross section to model.** One span. Integral abutments. Cast-in-place deck. Separate track slab in the middle. One vehicle lane each way, as the City describes the reopened bridge, with the map still tagging two lanes on each carriageway. North sidewalk and south shared-use path, each a minimum of 4.2 m in the agreement. Reference-design overall width 25.4 m.

## Still missing

- An as-built span length. The 46 m is a minimum. The mapped 60.7 m is not that length. The "about 8 m" is not a length.
- Deck elevation. The 6 m is a minimum clearance, and the EIA says the old clearance was kept without stating it.
- Girder depth, girder count, and whether the installed girders are haunched.
- As-built width. 25.4 m and 18.4 m are the reference design and the old bridge.
- A City date for LRT opening. The mapper tag 2028 was not used.
- An openly licensed elevation or deck photograph.
