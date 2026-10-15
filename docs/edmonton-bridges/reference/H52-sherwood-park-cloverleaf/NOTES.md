# H52 Sherwood Park Cloverleaf — modeling brief

Strathcona County, on the east edge of Edmonton, at the Sherwood Park Freeway / Anthony Henday Drive interchange. Centre used by the project: 53.513, -113.344. The VFR checkpoint Sherwood Park Cloverleaf is VCSWP, N53° 31.00′ W113° 20.50′. Carries Sherwood Park Freeway (unsigned Highway 100) over Henday (Highway 216). Eastbound on the freeway is three lanes. Westbound is four lanes. Henday runs under the freeway decks, three lanes each way.

OpenStreetMap way 34572698 is the eastbound overpass. Node order is from 53.512944, -113.345151 to 53.512583, -113.343008, west to east, so the one-way is eastbound toward Wye Road. Way 232709695 is the westbound overpass. Node order is from 53.51289, -113.342988 to 53.513219, -113.344994, east to west, so the one-way is westbound toward Edmonton.

The 2010 VFR plate names this checkpoint a cloverleaf. Wikipedia, citing the 2012 provincial structures list, says the cloverleaf at the freeway's east end was completed in 1965. The present-day package is the 2016 combination interchange. Wikipedia: a two-lane semi-directional flyover carries eastbound Sherwood Park Freeway to northbound Henday; the other three left turns are loop ramps. Do not model the demolished 1965 decks.

This is not H50 Henday / Yellowhead east, centre 53.568, -113.345. That is the three-level systems interchange with flyovers. The Commons aerial of Anthony Henday Drive over Yellowhead Trail is that junction. Do not copy it here. This is not H53 Henday / Whitemud east, 53.4829, -113.3427. This is not H54 Highway 14 / Henday, 53.449, -113.336. This is not S107 Sherwood Park Freeway / 17 Street, 53.5172, -113.3691. That is 17 Street over the freeway, rebuilt in the same northeast Henday contract. This is not W91 Whitemud / 17 Street. This is not Y79 Bremner Cloverleaf, 53.5702, -113.2461. Do not copy those span lengths, widths, or pier notes here. This is not the demolished 76 Avenue interchange. This is not the CNR overpass on Sherwood Park Freeway. This is not a single girder. The freeway decks, the flyover, and the loops are the landmark.

Numbers below are cited. Where two sources disagree, both are given. A blank in the "Still missing" list has no published figure in the sources checked. Nothing here was filled in by adding one citation to another. OpenStreetMap `maxheight=5.7` on Henday and `maxheight=5.8` on a north-side ramp are mapper tags. They are not deck elevations.

## Bridge

**Type.** Four separate grade-separation decks. Alberta Transportation file 75543.

E-7, Sherwood Park Freeway (EBL) over AHD (Hwy 216) (NBL and SBL). Inventory: WG, MAJOR BRIDGE, GS 2, year 2016, on 100:02 R1 3.367.

W-8, Sherwood Park Freeway (WBL) over AHD (Hwy 216) (NBL and SBL). Inventory: WG, MAJOR BRIDGE, GS 2, year 2016, on 100:02 L1 3.369.

EN1-9, Sherwood Park Freeway EN Ramp 1 over AHD (Hwy 216) (NBL and SBL). Inventory: WG, MAJOR BRIDGE, GF 2, year 2016, on Ramp 82-3 G.

EN2-10, Sherwood Park Freeway EN Ramp 2 over Sherwood Park Freeway (NBL and SBL). Inventory: NU, MAJOR BRIDGE, GF 2, year 2016, on Ramp 82-3 G.

The OpenStreetMap freeway ways have no `bridge:structure` tag. The two extra Overpass decks are tagged `source=AB Transportation`.

The January 2013 inspections under the same file number are E-1 and W-2, town name Salisbury Interchange, year built 1965. Those are the demolished cloverleaf decks. Do not use their span lengths on the 2016 structures.

**Spans.** No 2016 BIM inspection PDF was found (75543-7, 75543-8, 75543-9, and 75543-10 returned HTTP 404). The inventory rows print two spans on each of the four 2016 decks. E-7 prints 16.1, 65.5, and 128.5. W-8 prints 19.8, 65.5, and 128.5. EN1-9 prints 13.9, 63.0, and 123.5. EN2-10 prints 13.9, 36.5, and 71.5. Other numbers on those rows were not assigned. They were not added here and they were not averaged.

The demolished E-1 and W-2 inspections of 14 January 2013 both state FC, four spans, lengths 12.2 m, 19.8 m, 19.8 m, and 12.2 m. Those lengths are the 1965 decks. They are not the 2016 decks.

**Length.** No source other than those inventory figures states a length between abutments. The OpenStreetMap eastbound centreline, way 34572698, is 147.4 m. The westbound centreline, way 232709695, is 137.7 m. The south flyover centreline, way 103485448, is 147.0 m. The east ramp-bridge centreline, way 103485443, is 90.0 m. Use those lines for the plan shape. The mapped lengths and the inventory figures are different extents.

**Girders.** E-7, W-8, and EN1-9 are typed WG. EN2-10 is typed NU. Girder depth is not published. A girder-line count for the 2016 decks is not published. The demolished 1965 inspections state 40 girders on each of E-1 and W-2. That count is not the 2016 count. Depth was not read from any photograph. No openly licensed elevation was found.

Alberta, 21 February 2014: crews were installing girders for a new overpass that will go over Anthony Henday Drive at the new Sherwood Park Freeway interchange. That sentence does not give a girder count or a depth.

**Piers.** Not published for the 2016 decks. The 2013 inspections of the demolished decks type the piers PIER-COLUMN, with concrete abutments. Those notes are the 1965 structures. Pier height is not published. A footing plan size is not published.

**Clearance over Henday.** Alberta's vertical-clearances table: Sherwood Park Fwy east of Edmonton, on Highway 216, north 5.3 m, south 5.3 m. The demolished E-1 and W-2 inspections required posting under 216 L1 5.3 m and 216 R1 5.3 m, and posted 5.3 m. The table still states 5.3 m. It is a clearance under the overpass. It is not a deck elevation.

OpenStreetMap way 430222934 (Henday, dropped from this geometry) tags `maxheight=5.7`. Way 1286998212 tags `maxheight=5.8`. No published source found states 5.7 m or 5.8 m for this overpass. The vertical-clearances table's "Sherwood Pk Fwy / 17th Street" line is 5.3 m east and 5.0 m west. That is S107. It is not this deck. The "Sherwood Pk Fwy / 76th Avenue" line is 5.6 m east and 5.3 m west. That interchange was removed.

**Opening and widening.** Wikipedia, citing Strathcona County: construction of Sherwood Park Freeway began in 1964; the freeway and the interchange at Highway 14 opened in 1968. The same article, citing the 2012 structures list, says the cloverleaf at the east end was completed in 1965. The 1965 year and the 1968 opening are both published. They were not averaged. The 2013 inspections print year built 1965 and town name Salisbury Interchange, coordinates −113:20:42, 53:30:47.

The 1965 decks were demolished for the northeast Henday rebuild. Alberta project overview, 2013 work: traffic was shifted to the eastbound bridge to accommodate demolition of the westbound bridge over Anthony Henday Drive; 76 Avenue access to Sherwood Park Freeway was closed permanently. Looking ahead to fall 2016: a new free-flow overpass with collector roads, longer ramps, and a new flyover; first bridge opens to the public in summer 2014. Alberta, 21 February 2014: when completed in fall 2016, the new interchange will add a third lane in each direction, safer collector lanes, and a new free-flow overpass for eastbound to northbound traffic. Wikipedia: westbound between Henday and 17 Street widened to four lanes; eastbound now three lanes, up from two each way. The 2014 "third lane in each direction," the Wikipedia three-and-four lane split, and the OpenStreetMap three-and-four lane tags are all published. They were not reconciled into a new count.

CBC, 1 October 2016: the northeast Henday, Manning Drive to Whitemud Drive, opened that Saturday; 27 km; $1.81 billion; nine interchanges; 47 bridge structures. The P3 value-for-money report lists Sherwood Park Freeway / Wye Road among the interchange locations.

Present-day package: model the 2016 combination interchange, including the flyover and the loops that stand now. Do not invent a half-built 2013–2016 stage. Do not rebuild the 1965 cloverleaf.

**Rehabilitation that shows.** No post-2016 rehabilitation of these four decks was found. The 2018 LiDAR is after the 2016 opening. Sign structures ZN, ZE, ZS, and ZW under file 75543 are not decks.

## Approaches

No source gives the present gradient, the elevation change, or the point where either road meets natural grade. The OpenStreetMap ways below from the extract are complete ways: each one has the same node count as the live way on 14 October 2026. A complete way is still only the mapped polyline. Its far node is not a surveyed grade point. Lengths are horizontal WGS84. They are plan geometry only.

**West.** Eastbound onto the eastbound overpass. Way 995106404 is Sherwood Park Freeway, three lanes, 80 km/h, one-way, asphalt, 19.9 m. Node order runs toward the deck. Way 373938261 continues it west, two lanes, 80 km/h, one-way, 639.2 m, to 53.514557, -113.354732. The extract calls 373938261 a cross road because it does not share a node with a bridge=yes way. It is the same road. It heads toward S107. It is not that deck.

Westbound off the westbound overpass. Way 995106405 is Sherwood Park Freeway, four lanes, 70 km/h, one-way, asphalt, 73.1 m. Node order runs away from the deck, from the west end of way 232709695.

**East.** Westbound onto the westbound overpass. Way 32834429 is Wye Road, three lanes, 70 km/h, one-way, 683.0 m. Node order runs toward the deck, from 53.512194, -113.332806. The extract calls it a cross road because the name is Wye Road. Wikipedia: 800 m east of Henday the Highway 100 and Sherwood Park Freeway names end and the road continues as Wye Road.

Eastbound off the eastbound overpass. Way 373938269 is Wye Road, three lanes, 80 km/h, one-way, 559.7 m, to 53.512059, -113.334656. The extract role is cross_road. It is the same through road.

**Loops and ramps in this object.** Way 32834242 is the southwest loop, one lane, destination Sherwood Park, 395.2 m, onto the west stub of the eastbound overpass. Way 1286998212 is the two-lane link onto that loop, destination East; Sherwood Park, 171.8 m, maxheight tag 5.8. Way 103485446 is the motorway link from 53.507251, -113.343351, destination West; Edmonton; Sherwood Park Freeway, 1,090.2 m, onto the east end of the westbound overpass. None of those three is tagged `bridge=yes`.

A live Overpass and OSM map read of the box 53.507, −113.355, 53.519, −113.333 on 14 October 2026 also returned motorway_link ways 38001208 (destination Anthony; Henday Drive, destination:ref 216 South), 103485440 (destination West; Edmonton, junction:ref 61A), 103485444 (destination Anthony Henday Drive, destination:ref 216 North), 103485445 (destination East; Sherwood Park; Wye Road), and 1262002013 (destination East; Sherwood Park, junction:ref 61B). They are not in the extract. They were not copied into `geometry.json`.

**Henday underneath.** Way 430222934 is Anthony Henday Drive, 2,402.6 m, three lanes, 100 km/h, ref 216, maxheight tag 5.7. It was dropped. It runs toward H50 and H53. Alberta exit 61; signed 61A west and 61B east (AARoads / Wikipedia Highway 216). Posted 100 km/h on that way.

Five Mapillary frames sit 7 m to 31 m from this geometry: `street/mly-843101787615160.jpg` (30 December 2023), `street/mly-1278512605876288.jpg` (9 September 2020), `street/mly-380419036641919.jpg` (17 August 2018), `street/mly-4264480636917312.jpg` (21 October 2018), and `street/mly-303368634611381.jpg` (2 August 2018). They show asphalt, lane markings, barriers, and lamp posts. They do not show the underside or girder depth. They were not scaled.

2018 LiDAR, CGVD2013. West eastbound road, way 373938261, DSM median **706.43 m**. West westbound road, way 995106405, **716.62 m**. East westbound road, way 32834429, **713.62 m**. East eastbound road, way 373938269, **713.54 m**. Southwest loop, way 32834242, **711.80 m**. South-to-westbound ramp, way 103485446, **710.85 m**. Those are first-return surface heights on the mapped centrelines. They are not a published gradient, and they are not a climb to grade.

## Deck

**Elevation.** 2018 LiDAR, CGVD2013. DSM median along the eastbound overpass, way 34572698: **717.86 m** (p10 717.29 m, p90 717.99 m, 49 samples). Along the westbound overpass, way 232709695: **717.86 m** (p10 717.40 m, p90 717.93 m, 46 samples). Along the south flyover, way 103485448: **721.40 m** (p10 719.39 m, p90 722.95 m, 47 samples). Along the east ramp bridge, way 103485443: **724.84 m** (p10 724.62 m, p90 724.96 m, 29 samples). Those medians were not averaged. DTM at the project centre (53.513, -113.344): **707.76 m**. That centre sits in the interchange, over Henday, so the DTM there is the ground under the overpasses, not a river. DSM is first-return; traffic and railings can add up to 1 m. Rise is DSM minus that DTM, not a published clear height. Subtract deck depth if a clearance is stated. No published geodetic deck elevation was found to set beside these figures. The clip does not hold a river reach. Gauge 05DF001 was not converted.

**Thickness.** Not published for the 2016 decks. The demolished 1965 inspections state conventional chip seal 50 mm on 70 mm fibre-reinforced concrete. That sandwich is the old deck. The depth from the wearing surface to the soffit is not published on either generation. Girder depth is not published.

**Width.** No 2016 inspection clear-roadway figure was found. The inventory rows print 16.1 on E-7 and 19.8 on W-8. Those prints were not assigned to a named width here. The demolished E-1 and W-2 inspections both state clear roadway 15.8 m, roadway width 12.500 m, skew 16 deg RHF. Those are the 1965 decks. Lane width is missing. Shoulder width is missing. The two freeway overpass centrelines are 32.3 m apart at the west end and 34.2 m apart at the east end. Those are distances between mapped centrelines. They are not a published width.

**Lanes.** Three eastbound and four westbound on the freeway overpasses, one-way, asphalt (Wikipedia; OpenStreetMap). Eastbound tagged 80 km/h. Westbound tagged 70 km/h. The two extra Overpass decks are tagged two lanes. Henday underneath is three lanes each way, 100 km/h. The 2013 inspections of the demolished decks list sidewalk as none. No path ways are tagged on these overpasses.

**Crossfall.** Not published. Longitudinal grade on the spans is not published. The demolished inspections call the alignment a typical grade separation with on and off ramps and a crest curve. That wording is the 1965 decks.

Wikipedia, citing Alberta 2019 traffic statistics: about 40,000 vehicles a day between Henday and 17 Street in 2019. The 2013 inspections print AADT 33,860 (2011). Both figures are published. They were not averaged.

## Still missing

- Deck elevation above sea level from a published source, and the vertical datum. Soffit elevation.
- Girder depth on any of the four 2016 decks.
- A girder-line count for the 2016 decks. The 40-girder count is the demolished 1965 inspections.
- 2016 BIM inspection PDFs (span-by-span lengths, pier type, wearing-surface thickness, posted clearances on the new decks). 75543-7 through 75543-10 were not on the inspections server.
- Pier heights, footing plan sizes, and a published pier type for the 2016 decks.
- Lane width and shoulder width. What the inventory 16.1 and 19.8 prints measure.
- Crossfall as a slope. Longitudinal grade on the spans.
- Where each Sherwood Park Freeway and Wye Road approach meets natural grade, and the length, gradient, and elevation change of each climb.
- Geometry in this folder for the other OSM loops and outer ramps (ways 38001208, 103485440, 103485444, 103485445, 1262002013).
- An openly licensed elevation, underside, or aerial. City 2019 Pictometry clips in `aerial/` are measuring reference only (licence not confirmed).

## Added 2026-10-15

The 2019 City orthophoto covers only the west half of the interchange (west of the Henday and the loops on the west side); the east half is blank. The model plan matches the photo where it exists: both west loops, the flyover over Henday, and the freeway decks. Henday pavement under the decks is about 708.6 to 709.6 m (DTM), deck tops about 717.6 m (freeway) and 721.0 m / 724.6 m (flyover). The OSM freeway and Wye Road ways run as two parallel carriageways 14 m to 32 m apart. See HANDOFF-T2.md.
