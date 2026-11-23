# R21 Clover Bar Bridge — modeling brief

Edmonton. One of the two Highway 16 / Yellowhead Trail decks across the North Saskatchewan River at the VFR checkpoint Bridges (VCBRG). Project files this as Clover Bar Bridge (R21). Inventory: Highway 16 eastbound, three lanes, 1953. Centre used by the project: 53.572, -113.372.

The OpenStreetMap way in this object, 61431758, is tagged `bridge:name=Beverly Bridge`. It is Yellowhead Trail NW, motorway, three lanes, oneway, ref 16. Node order is from 53.571378, -113.369538 to 53.572724, -113.374409, southeast to northwest. The OpenStreetMap outline in this object, way 642360970, is tagged `name=Clover Bar Bridge` and `bridge:structure=beam`. Both names are on the map. This folder does not invent which mapped deck is which named structure.

Wikipedia and Naming Edmonton call Clover Bar the original 1953 span, north of the 1972 girder, and westbound. The Wikipedia list of crossings, and this project's inventory, call Clover Bar eastbound and Beverly westbound. Both wordings are published.

This is not R20 Beverly Bridge, centre 53.571, -113.373. It is not R22 Clover Bar Railway Bridge, centre 53.573, -113.372. It is not H50 Henday / Yellowhead east, 53.568, -113.345. It is not Y75 Yellowhead / 17 Street, 53.570, -113.363. It is not Y78 Yellowhead / Clover Bar Road, 53.570, -113.271. Do not copy those span lengths, widths, or pier notes here. The 504 m and 504.44 m lengths, and the 42 m and 42.06 m heights, are published for the railway. They are not used here. The 321.5 m OpenStreetMap centreline in the R20 folder is a different way. It is not copied here.

Numbers below are cited. Where two sources disagree, both are given. A blank in the "Still missing" list has no published figure in the sources checked. Nothing here was filled in by adding one citation to another. Way 61431758 has no `width` tag and no `maxheight` tag in the extract. A mapper tag is not a deck elevation.

## Bridge

**Type.** Alberta Transportation bridge record, file 02032, CLOVERBAR BRIDGE (B292), Highway 16 over the North Saskatchewan River. Status IN SERVICE, first in service 2001, last inspected 2025-09-14 (https://www.transportation.alberta.ca/PlanningTools/Data/Bridge/Structure-Export.csv). The record gives concrete piers and caps, pile-founded abutments and a polymer-modified asphalt wearing surface. It does not give a superstructure type. A girder is not stated by the record. The model's plate-girder deck is an assumption, consistent with the 2001 date and 70 m spans. The 1953 truss is not the present bridge; see Opening.

Conflict, one note: Wikipedia calls the original Clover Bar a truss completed in 1953. Structurae lists a 1952 Clover Bar Highway Bridge with no type. The 1999 EIA says 1952/3. Same file 02032, record CLOVERBAR BR, is that old structure: REMOVED, first in service 1952, 7 spans, 11 m gross deck. The 1953 date belongs to the removed truss. The 1952 and 1953 dates are not averaged, and neither is used for the present bridge.

**Spans.** Five spans: 55, 70, 70, 70 and 55 m, maximum 70 m (record, file 02032). The span set is symmetric, so the interior piers sit at 55, 125, 195 and 265 m from either abutment. The removed structure's seven spans (record CLOVERBAR BR) are not used.

**Length.** Nominal bridge length 320 m (record, file 02032). The model deck runs 320 m between abutments, centred on the middle of OSM way 61431758 (355.1 m), trimmed 17.55 m at each end. The OSM outline perimeter (723.6 m) and its 344.5 m length are mapped extents, not the structural length.

**Truss or girders.** Not stated by the record. The present bridge is a 2001 structure with 70 m spans. The 12 May 2015 photograph shows a girder highway in front of the railway truss, not a truss. The model is a five-line plate-girder deck, 2.8 m deep. Girder depth and line count are assumed, not published.

**Piers.** Concrete shafts and caps, four interior piers (record, file 02032). Pier plan size, height and abutment size are not in the record. Wall-type piers under a cap are assumed, as before. The cap now spans the 17.5 m gross deck. Pier stations come from the record, not from the photograph.

**Clearance above the river.** Not published. No navigation clearance is published. No elevation above sea level is published for the deck, the soffit, or the water. Environment Canada gauge 05DF001 is at the Low Level Bridge and uses a local assumed datum. No source used here converts a clearance at this crossing from that gauge.

**Opening.** First in service 2001 (record, file 02032, IN SERVICE). Truck News, 6 April 2001, lists a three-lane Clover Bar Bridge for westbound traffic among that season's projects, which fits the 2001 date. The 1952 and 1953 dates above are for the removed truss.

**Rehabilitation that shows.** The record's 2001 date matches Truck News 2001 (construction of a three-lane Clover Bar Bridge for westbound traffic). What else changed on the silhouette is not described. The City's 2025–2026 project is named Beverly Bridge. That work is in the R20 folder. It is not copied here.

## Approaches

No source gives the present gradient, the elevation change, or the point where either road meets natural grade. The OpenStreetMap ways below are complete ways: each one has the same node count as the live way on 14 October 2026. A complete way is still only the mapped polyline. Its far node is not a surveyed grade point. Lengths are horizontal WGS84. They are plan geometry only.

**Northwest.** Way 61432008 is Yellowhead Trail NW, three lanes, oneway, 100 km/h, 150.6 m. Node order runs away from the deck, from the northwest end of way 61431758 to 53.573296, -113.376474. Live tags also have `turn:lanes=||through;slight_right`. The extract does not store that tag. The far node is not a surveyed grade point.

**Southeast.** Way 61430196 is Yellowhead Trail NW, three lanes, oneway, 100 km/h, 401.5 m. Node order runs toward the deck, from 53.57044, -113.363695 to the southeast end of way 61431758. The far node is toward Y75, not a grade point on this climb.

Way 1271013522 is a track, 258.9 m. It was dropped. Ways 32832524 and 61431778 are the other carriageway's approaches. They were dropped.

No openly licensed frame was found that shows either road meeting grade. Mapillary frames in `street/` are dashcam views from the mapped Yellowhead ways. They show asphalt, lamps, and barriers. They do not show the underside or girder depth. They were not scaled.

2018 LiDAR, CGVD2013, along way 61432008: DSM median 635.98 m. Along way 61430196: DSM median 637.61 m. Those are first-return surface heights on the mapped centrelines. They are not a published gradient, and they are not a climb to grade.

## Deck

**Elevation.** 2018 LiDAR, CGVD2013. DSM median along way 61431758: **634.10 m** (p10 632.91 m, p90 635.11 m, 117 samples). River surface in this clip: **610.07 m**, valid. Median 24.03 m above that river surface. DTM at the project centre (53.572, -113.372): **609.99 m**. That centre sits over the channel, so the DTM there is the water, not a bank. DSM is first-return; traffic and railings can add up to 1 m. Rise is DSM minus the river surface, not a published clear height. Subtract deck depth if a clearance is stated. No published geodetic deck elevation was found to set beside these figures. These LiDAR numbers were sampled on this folder's clips. They were not copied from R20.

**Thickness.** Not published. The depth from the wearing surface to the soffit is not published.

**Width.** Record, file 02032: gross deck width 17.5 m, total clear roadway 16.6 m. The model centres the 17.5 m gross deck on the middle of the OSM outline (way 642360970, 17.2 m across at the NW end and 17.1 m at the SE end). The 0.9 m between gross and clear is the edges, split 0.45 m each side (assumed). Carriageway 11.1 m and shoulders 2.75 m each side are assumed: the way has no width tag and the record gives no lane width. The 11.1 m is not taken from the R20 way's width tag. Lane width is missing. Shoulder width is missing.

**Lanes.** Three, one-way (OpenStreetMap way 61431758; Truck News 2001 for a three-lane Clover Bar Bridge). The way is tagged 100 km/h. Node order on the bridge way is southeast to northwest. A live read of the same way on 14 October 2026 also has `lit=yes`, `hgv=designated`, `hazmat=designated`, `NHS=yes`, and language variants of Yellowhead / Trans-Canada. The extract does not store those tags. The tags are not a deck elevation.

**Sidewalks.** The City describes a south-side sidewalk on the structure it names Beverly Bridge. That sentence is in the R20 folder. A sidewalk on this deck is not published. OpenStreetMap does not map a bridge-tagged sidewalk on way 61431758. The 2011 photograph shows a blue metal railing on the highway next to the railway. Width was not measured from that frame.

**Crossfall.** Not published. Longitudinal grade on the span is not published.

## Still missing

- Deck elevation above sea level from a published source, and the vertical datum. Soffit elevation.
- Clearance from the roadway or the soffit down to the river, and a navigation clearance.
- A source that states the superstructure type. Girder depth and the number of girder lines.
- Pier plan size and pier heights. Abutment size.
- Deck thickness, and the depth from the wearing surface to the soffit.
- Lane width and shoulder width. The record gives only the 16.6 m total clear roadway.
- Sidewalk presence and width on this deck. The 0.9 m between gross and clear is not split by a source.
- Crossfall as a slope. Longitudinal grade on the spans.
- Where each Yellowhead approach meets natural grade, and the length, gradient, and elevation change of each climb.
- A published statement that settles which mapped carriageway is Beverly and which is Clover Bar. File 02032 gives no direction, and the names on the road way and on the outline do not match each other.
- An openly licensed underside photograph, a labelled elevation of this deck alone, and an openly licensed aerial.

## Tier 2 review (2026-10-15)

Review result: buildable with assumptions; spans, piers and girders are still not published. Added:

- `elevation/profiles.csv` by `scenery-edmonton-bridges/tools/lidar_pil.py`. Deck first returns rise steadily from 632.5 m (SE end) to 635.3 m (NW end); bare earth meets the soffit about 22 m from the SE way end and about 10 m from the NW way end, the outline runs about 11 m past each.
- Outline lateral extent about the way (reversed, NW to SE): -6.4 m south to +10.8 m north.
- The 12 May 2015 photograph shows tan wall-type piers with taper under the far (north) deck, but that deck is hidden behind R20's in the frame, so no pier station can be read; the model copies R20's fractions and flags them as assumed.
- The 2011 photograph from this deck shows a blue 3-rail steel railing on the north edge. The street frames show a low concrete median barrier and davit lamps with curved arms.
- No published span or pier data was found by web search.
