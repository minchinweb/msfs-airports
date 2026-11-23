# R20 Beverly Bridge — modeling brief

Edmonton. One of the two Highway 16 / Yellowhead Trail decks across the North Saskatchewan River at the VFR checkpoint Bridges (VCBRG). Project files this as Beverly Bridge (R20). Inventory: Highway 16 westbound, three lanes, opened 1972. Centre used by the project: 53.571, -113.373.

The OpenStreetMap way in this object, 61430014, is tagged `bridge:name=Clover Bar Bridge`. It is Yellowhead Trail NW, motorway, three lanes, oneway, ref 16. Node order is from 53.571685, -113.375267 to 53.570196, -113.371099, northwest to southeast. The OpenStreetMap outline in this object, way 642360969, is tagged `name=Beverly Bridge` and `bridge:structure=beam`. Both names are on the map. This folder does not invent which mapped deck is which named structure.

Wikipedia and Naming Edmonton call the 1972 steel girder Beverly, place it south of the 1953 span, and give it eastbound Yellowhead traffic. The same Wikipedia article, and Naming Edmonton, give Clover Bar westbound traffic. The Wikipedia list of crossings, and this project's inventory, call Beverly westbound and Clover Bar eastbound. Both wordings are published.

This is not R21 Clover Bar Bridge, centre 53.572, -113.372. It is not R22 Clover Bar Railway Bridge, centre 53.573, -113.372. It is not H50 Henday / Yellowhead east, 53.568, -113.345. It is not Y75 Yellowhead / 17 Street, 53.570, -113.363. It is not Y78 Yellowhead / Clover Bar Road, 53.570, -113.271. Do not copy those span lengths, widths, or pier notes here. The 504 m and 504.44 m lengths, and the 42 m and 42.06 m heights, are published for the railway. They are not used here.

Numbers below are cited. Where two sources disagree, both are given. A blank in the "Still missing" list has no published figure in the sources checked. Nothing here was filled in by adding one citation to another. OpenStreetMap `width=11.1` is a mapper tag on the road way. It is not a published structural width. There is no `maxheight` tag on this way. A mapper tag is not a deck elevation.

## Bridge

**Type.** The City's 2025–2026 rehabilitation of a structure it names Beverly Bridge describes a concrete deck and steel girders. Wikipedia calls the 1972 south span a steel girder and names it Beverly. The OpenStreetMap outline, way 642360969, tags `bridge:structure=beam`. Way 61430014 has no `bridge:structure` tag.

Wikipedia calls the original 1953 north span a truss and names it Clover Bar. That sentence is about the other highway deck. The 12 May 2015 photograph, taken facing northeast, shows a girder highway in front of the railway truss. Four concrete piers stand in the channel under the nearer highway. A second highway deck is not labelled in that frame. A count of spans was not published. A count was not taken from the photograph.

**Spans.** Alberta Transportation bridge record, file 77132 (BEVERLY BRDG, B143, Highway 16 over the North Saskatchewan River, in service 1972). Source: https://www.transportation.alberta.ca/PlanningTools/Data/Bridge/Structure-Export.csv (extract retrieved 2026-11-23; last inspected 2023-08-16). Five spans: 54.9, 70.1, 70.1, 70.1 and 54.9 m. Max span 70.1 m. The set is symmetric, so the interior piers sit at 54.9, 125.0, 195.1 and 265.2 m from either abutment. The 2015 photo-read pier stations (54, 129, 207, 280 m) are replaced by these.

**Length.** Nominal bridge length 320.1 m (file 77132, as above). The model deck runs between the abutments at exactly 320.1 m, centred on the middle of the OSM way. Structurae's Clover Bar Highway Bridge page has no technical data. The OpenStreetMap road centreline, way 61430014, is 322.0 m on the model's frame (earlier notes gave 321.5 m, a different measure), so 0.97 m is trimmed at each end. The mapped outline, way 642360969, is a closed ring. Its perimeter is 719.6 m. That perimeter is not a span length. The long sides of the outline are 339.3 m and 341.7 m (197.8 m plus 143.9 m, with a node on that side). The outline is the mapped footprint. Structural length is the 320.1 m from file 77132.

**Girders.** Steel girders (City rehab; Wikipedia for the 1972 Beverly span). Girder depth is not published. The number of girder lines is not published. Depth was not read from the 2015 photograph.

**Piers.** Four concrete piers, five spans (file 77132). Concrete shafts and caps; abutments on pile foundations (file 77132). Shaft shape is not in the record: the model keeps the 2015 photo read (single wide columns under the first two piers, twin columns under the last two), which is still assumed. The 2015 photograph shows four shafts under the nearer highway, wider toward the water, which agrees with the record's count. The City's 2025 work on the structure it names Beverly Bridge includes abutment repair. Abutment size is not published. Bearing types are described only as repaired.

**Clearance above the river.** Not published. No navigation clearance is published. No elevation above sea level is published for the deck, the soffit, or the water. Environment Canada gauge 05DF001 is at the Low Level Bridge and uses a local assumed datum. No source used here converts a clearance at this crossing from that gauge.

**Rehabilitation that shows.** The City's Beverly Bridge project, 2025–2026, repairs the concrete deck and the steel girders, replaces pavement and traffic barriers, and repairs bearings and abutments. Stage 1, south side of that bridge, finished in November 2025: deck repair, waterproofing, paving, girder, bearing and abutment repair, and upgraded street lighting. Three lanes returned for the winter. Stage 2, north side, from April 2026: two lanes, 60 km/h in the zone, asphalt milling and paving, barrier replacement, girder repairs, through the end of October 2026. The sidewalk on the south side of that bridge stays open. Alberta Major Projects states $16.7 million and names the 1972 bridge. The City does not describe a new girder outline or a new pier shape. The 2015 photograph is older than this work. Mapillary frames from 2018 are older than this work.

The Library of Congress subject record quotes a 1999 environmental impact assessment: the existing Clover Bar Bridge was constructed in 1952/3 as a two-lane, two-way bridge, and replacement was needed for six-lane Yellowhead Trail. Truck News, 6 April 2001, lists construction of a three-lane Clover Bar Bridge for westbound traffic among that season's projects. Those sentences name Clover Bar. They are not copied here as this deck's history.

## Approaches

No source gives the present gradient, the elevation change, or the point where either road meets natural grade. The OpenStreetMap ways below are complete ways: each one has the same node count as the live way on 14 October 2026. A complete way is still only the mapped polyline. Its far node is not a surveyed grade point. Lengths are horizontal WGS84. They are plan geometry only.

**Northwest.** Way 61431778 is Yellowhead Trail NW, three lanes, oneway, 100 km/h, width tag 11.1, 131.1 m. Node order runs toward the deck, from 53.572318, -113.376939 to the northwest end of way 61430014. The extract role is approach.

**Southeast.** Way 32832524 is Yellowhead Trail NW, three lanes, oneway, 100 km/h, width tag 11.1, 452.7 m. Node order runs away from the deck, from the southeast end of way 61430014 to 53.569092, -113.364628. That far node is toward Y75, not a grade point on this climb.

Way 1271013522 is a track, 258.9 m, at the northwest end. It was dropped. It is a valley trail, not the Yellowhead climb.

No openly licensed frame was found that shows either road meeting grade. Two Mapillary frames sit 2 m and 4 m from this geometry, on the mapped Yellowhead ways: `street/mly-379523593476007.jpg` (7 August 2014) and `street/mly-789596358644544.jpg` (20 October 2018). They show asphalt, lane markings, and a green overpass ahead. They are not a view of the river span. They do not show the underside or girder depth. They were not scaled.

2018 LiDAR, CGVD2013, along way 61431778: DSM median 633.72 m. Along way 32832524: DSM median 638.62 m. Those are first-return surface heights on the mapped centrelines. They are not a published gradient, and they are not a climb to grade.

## Deck

**Elevation.** 2018 LiDAR, CGVD2013. DSM median along way 61430014: **632.42 m** (p10 632.20 m, p90 632.99 m, 106 samples). River surface in this clip: **610.14 m**, valid. Median 22.28 m above that river surface. DTM at the project centre (53.571, -113.373): **610.10 m**. That centre sits over the channel, so the DTM there is the water, not a bank. DSM is first-return; traffic and railings can add up to 1 m. Rise is DSM minus the river surface, not a published clear height. Subtract deck depth if a clearance is stated. No published geodetic deck elevation was found to set beside these figures. The 2018 surface is older than the 2025–2026 deck work.

**Thickness.** The City names a concrete deck, waterproofing, and new pavement on the structure it calls Beverly Bridge. No thickness is given for the concrete, the waterproofing, or the asphalt. The depth from the wearing surface to the soffit is not published.

**Width.** Alberta file 77132: gross deck width 19.2 m, total clear roadway 16.8 m. The model uses these as the authority:

- Gross 19.2 m, centred on the middle of the OSM outline (way 642360969, 19.3 m across, mid-line 0.85 m north of the way): -8.75 m (south) to +10.45 m (north) about the way.
- Clear roadway 16.8 m = carriageway 11.1 m plus two 2.85 m shoulders. The 11.1 m is the OSM `width=11.1` tag, read as three 3.7 m lanes (lane width is assumed, not published). The shoulders are assumed.
- The 2.4 m left over (gross less clear) is split between the edges: 1.8 m on the south side for the sidewalk (City, south side; the width is assumed) and 0.6 m on the north side for the parapet (assumed).

So the 16.8 m clear roadway and the 19.2 m gross both hold in the model. Lane, shoulder and sidewalk widths are not published; only the totals are.

**Lanes.** Three, one-way, asphalt (City; OpenStreetMap way 61430014). The way is tagged 100 km/h. The City uses the same 100 km/h, reduced to 60 km/h in the 2026 construction zone. Node order on the bridge way is northwest to southeast. A live read of the same way on 14 October 2026 also has `lit=yes`, `hgv=designated`, `hazmat=designated`, `placement=right_of:2`, `NHS=yes`, and language variants of Yellowhead / Trans-Canada. The extract does not store those tags. No published source found states a clearance that matches those tags. The tags are not a deck elevation.

**Sidewalks.** The City says the sidewalk on the south side of Beverly Bridge stays open during the 2026 work. The sidewalk width is not published; the model uses 1.8 m (assumed, see Width). OpenStreetMap does not map a bridge-tagged sidewalk on way 61430014. There is no `sidewalk` tag on that way. The 9 August 2011 photograph, taken from a highway deck toward the railway, shows a blue metal railing and an asphalt wearing surface in the foreground. Width was not measured from that frame. The frame does not label which of the two highway decks the photographer stood on.

**Crossfall.** Not published. Longitudinal grade on the span is not published.

## Still missing

- Deck elevation above sea level from a published source, and the vertical datum. Soffit elevation.
- Clearance from the roadway or the soffit down to the river, and a navigation clearance.
- Girder depth. Number of girder lines.
- Pier heights, the plan size and shape of the piers and the abutments (the record gives materials only; the shaft shape is still the 2015 photo read).
- Deck thickness, and the depth from the wearing surface to the soffit.
- Lane width and shoulder width (the record gives only the 16.8 m clear roadway; the 3.7 m lanes and 2.85 m shoulders are assumed). Sidewalk width (1.8 m assumed). Do not treat the OSM `width=11.1` tag as a structural width; it is consistent with three 3.7 m lanes.
- A mapped sidewalk way on this deck.
- Crossfall as a slope. Longitudinal grade on the spans.
- Where each Yellowhead approach meets natural grade, and the length, gradient, and elevation change of each climb.
- A published statement that settles which mapped carriageway is Beverly and which is Clover Bar. The names on the road way and on the outline do not match each other.
- An openly licensed underside photograph, a labelled elevation of this deck alone, and an openly licensed aerial.
- Whether the 2025–2026 barrier replacement changed the railing in the 2011 photograph. The City does not describe the new barrier.

## Tier 2 review (2026-10-15)

Review result: buildable with assumptions. Missing from the published record, still: span count and lengths, pier and girder details, deck thickness. What was added from the existing files:

- `elevation/profiles.csv` (25 m steps along every mapped way), written by `scenery-edmonton-bridges/tools/lidar_pil.py`. Deck first returns run 632.2 m (mid-span) to 633.0 m (SE end), a shallow sag; bare earth is 3.7 m below the deck at the NW end and about 4 m at the SE end, so the abutments sit at the way ends.
- Outline lateral extent about the way: -8.8 m (south) to +10.5 m (north). The south excess over the 11.1 m carriageway matches the City's south-side sidewalk.
- The 12 May 2015 photograph (nearer deck, the south one) shows slender concrete columns under a thin constant-depth girder deck: single wide columns at about 54 m and 129 m, twin columns at about 207 m and 280 m from the NW end (scale from the 321.5 m deck length, plus or minus 10 m); column height above the water about 20 m, deck plus girders about 3 m deep. The deck shows a blue steel railing.
- Web searches for span lengths, a bridge file or a drawing (Structurae, Wikipedia, City and Alberta project pages, news) found none.

## Update 2026-11-23: Alberta file 77132

The Alberta Transportation record (https://www.transportation.alberta.ca/PlanningTools/Data/Bridge/Structure-Export.csv, inspected 2023-08-16) gives five spans of 54.9, 70.1, 70.1, 70.1 and 54.9 m, nominal 320.1 m, gross width 19.2 m, clear roadway 16.8 m, concrete piers and caps, pile-founded abutments and a polymer-modified asphalt wearing surface. The span and width statements above are now sourced from it. The 2015 photo-read pier stations (54, 129, 207, 280 m) were replaced by 54.9, 125.0, 195.1 and 265.2 m from the first abutment. The record is symmetric, so the stations are the same from either end; the model's 0 m is the NW end of the OSM way and the deck starts at 0.97 m on that axis.

The same extract has file 02032, CLOVERBAR BRIDGE (B292), in service 2001 on Highway 16 over the same river: five spans 55, 70, 70, 70, 55 m, nominal 320 m, gross 17.5 m, clear roadway 16.6 m, last inspected 2025-09-14. R21 is not changed here, but its own width and span notes should be checked against that record.
