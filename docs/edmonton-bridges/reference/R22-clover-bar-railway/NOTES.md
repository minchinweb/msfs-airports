# R22 Clover Bar Railway Bridge — modeling brief

Edmonton. Steel deck-truss railway across the North Saskatchewan River at the VFR checkpoint Bridges (VCBRG), north of the two Highway 16 decks. Inventory: CN, 1908. Centre used by the project: 53.573, -113.372. OpenStreetMap names the line Wainwright Subdivision. Operator tags: Canadian National Railway and VIA Rail.

The R22 object in `bridge-geometry.json` attached a Yellowhead road way. Those ways are not this span. This folder uses OpenStreetMap way 23426591, the rail centreline on the river, and way 654886208, the named outline Clover Bar Railway Bridge.

This is not R20 Beverly Bridge, centre 53.571, -113.373. It is not R21 Clover Bar Bridge, centre 53.572, -113.372. It is not H50 Henday / Yellowhead east, 53.568, -113.345. It is not Y75 Yellowhead / 17 Street, 53.570, -113.363. It is not Y78 Yellowhead / Clover Bar Road, 53.570, -113.271. Do not copy those span lengths, widths, or pier notes here. The Highway 16 mapped centrelines 321.5 m and 355.1 m are different ways. They are not used here.

Numbers below are cited. Where two sources disagree, both are given. A blank in the "Still missing" list has no published figure in the sources checked. Nothing here was filled in by adding one citation to another. OpenStreetMap `maxspeed=40 mph` is a mapper tag on the rail way. It is not a deck elevation.

## Bridge

**Type.** Structurae calls it a steel deck truss, railroad bridge, in use, completed 1908. Forth Junction: iron truss with concrete piers and trestle towers, Grand Trunk Pacific, 1907–08, still in use by CN. Wikipedia: iron and concrete truss, Grand Trunk Pacific, 1907–1908, CN main line. The OpenStreetMap outline, way 654886208, tags `bridge:structure=truss` and `bridge=cantilever`. The rail way, 23426591, tags `bridge=cantilever` and has no `bridge:structure` tag. The 9 August 2011 photograph shows a steel deck truss, a train on top of the truss, and concrete piers. The 12 May 2015 photograph shows the same truss behind the highway girder, with a freight train on it.

The OpenStreetMap outline tags `construction_year=1932`. Published completion is 1908. Naming Edmonton gives 1907 for the railway. The Edmonton Bulletin, quoted by the River Valley Atlas, reports the bridge finished on 26 December 1908. All of those dates are published. They were not averaged. A published description of 1932 work on the silhouette was not found.

**Spans.** Individual span lengths are not published. They were not made by dividing 504 m. The 2011 photograph shows repeated truss panels between concrete piers. A panel count was not published. A count was not taken from the photograph.

**Length.** Forth Junction: 504 m (1,655 ft). Wikipedia: 504 m (1,654 ft). Structurae: 504.44 m. The Edmonton Bulletin, 30 October 1907, quoted by the River Valley Atlas, called it over a quarter of a mile. Those figures were not averaged. The OpenStreetMap rail centreline, way 23426591, is 513.3 m. Use 504 m or 504.44 m as the published length. Use the OpenStreetMap line for the plan shape. The mapped length and the published lengths are different extents.

The mapped outline, way 654886208, is a closed ring. Its perimeter is 1,040.5 m. That perimeter is not a span length. The long sides are 511.7 m and 513.8 m (257.8 m plus 256.0 m, with a node on that side).

**Truss.** Steel (Structurae). Iron in Forth Junction and in Wikipedia. Both wordings are published. Truss depth is not published. Depth was not read from the photographs.

**Piers.** Concrete piers (Forth Junction; the 2011 and 2015 photographs). Forth Junction also names trestle towers. The Edmonton Bulletin, 24 December 1906, quoted by the River Valley Atlas, says ninety-five foot high piers. That is a pier height in construction. It is not the 42 m height published for the bridge. The two figures were not added or subtracted. The Bulletin of 14 October 1907, quoted in the same atlas, reports one abutment, seven pedestals, and one pier finished, and three cofferdams for the remaining piers. That is a construction progress note. It is not a finished pier count. A finished pier count was not published. A count was not taken from the photographs.

Talbot, 1912, caption: shore supports need deep foundations because of friable soil. The 1912 plate shows a shore-end cut under construction, with timber falsework. That plate is this bridge during construction. The finished deck is the 1908 structure still in use, not a demolished span.

**Clearance / height.** Structurae: 42.06 m above valley floor or water. Forth Junction: 42 m (138 ft). Wikipedia: 42 m (138 ft). The public pages do not name a geodetic datum for that height. They were not averaged. No navigation clearance is published. No elevation above sea level is published for the deck, the soffit, or the water. Environment Canada gauge 05DF001 is at the Low Level Bridge and uses a local assumed datum. No source used here converts a clearance at this crossing from that gauge. The 95 ft pier figure is not that 42 m height.

**Rehabilitation that shows.** Still in use (Structurae; Forth Junction; Wikipedia; CN train in 2011). A published rehabilitation that changed the truss outline was not found.

## Approaches

No source gives the present gradient, the elevation change, or the point where either rail meets natural grade. The OpenStreetMap ways below are complete ways. A far node is not a surveyed grade point. Lengths are horizontal WGS84. They are plan geometry only.

**Northwest.** Way 23426590 is Wainwright Subdivision, not tagged bridge, 562.8 m. Node order runs away from the span, from 53.573943, -113.374596 to 53.575857, -113.382477.

**Southeast.** Way 1308613066 is Wainwright Subdivision, not tagged bridge, 1,168.7 m. Node order runs toward the span, ending at 53.572198, -113.367408, the southeast end of way 23426591. That way is long. It is not the climb to grade.

Way 37841289 is another CN railway east of the southeast end. It was dropped. The Yellowhead ways the extract attached were dropped.

The 1912 plate shows the shore-end earthworks during construction. No gradient was measured from it. Mapillary frames in `street/` are dashcam views near this geometry, from the adjacent highway. They do not show the rail underside. They were not scaled.

2018 LiDAR, CGVD2013, along way 23426590: DSM median 651.66 m. Along way 1308613066: DSM median 656.78 m. Those are first-return surface heights on the mapped centrelines. They are not a published gradient, and they are not a climb to grade.

## Deck

**Elevation.** 2018 LiDAR, CGVD2013. DSM median along way 23426591: **651.45 m** (p10 651.35 m, p90 651.54 m, 169 samples). River surface in this clip: **609.84 m**, valid. Median 41.61 m above that river surface. DTM at the project centre (53.573, -113.372): **609.96 m**. That centre sits over the channel, so the DTM there is the water, not a bank. DSM is first-return; rails and a train can add up to 1 m. Rise is DSM minus the river surface, not a published clear height. Subtract deck depth if a clearance is stated.

Structurae states 42.06 m above valley floor or water. Forth Junction states 42 m (138 ft). Wikipedia states 42 m (138 ft). The 41.61 m LiDAR rise and those published heights are both given. They were not averaged. No published geodetic deck elevation was found. The 42 m figures are not a deck ASL.

**Thickness.** Not published. The depth from rail to soffit is not published.

**Width.** No published width. The mapped outline is 7.9 m across at the northwest end and 7.1 m across at the southeast end. Those are the OpenStreetMap outline, not a published structural width. The 2011 photograph shows a single track on the truss. A track count was not published. Gauge tag 1435 mm. Electrified: no.

**Rail.** One mapped centreline. Operator Canadian National Railway and VIA Rail. Usage main. Name Wainwright Subdivision. `maxspeed=40 mph` is the mapper tag. No published source found states 40 mph as a structural clearance.

**Walkway.** Not published. OpenStreetMap does not map a sidewalk on this span.

**Crossfall.** Not published. Longitudinal grade on the span is not published.

## Still missing

- Deck elevation above sea level from a published source, and the vertical datum. Soffit elevation.
- A geodetic datum for the 42 m / 42.06 m height. A navigation clearance.
- Published span count and span lengths. Truss depth. Panel count.
- Finished pier count, and the plan size of the piers, pedestals, trestle towers, and abutments.
- Deck thickness, and the depth from rail to soffit.
- Published structural width and track count.
- What the OpenStreetMap `construction_year=1932` tag records.
- Crossfall as a slope. Longitudinal grade on the spans.
- Where each rail approach meets natural grade, and the length, gradient, and elevation change of each climb.
- An openly licensed aerial. Underside is visible in the 2011 and 2015 side elevations; a close soffit still is missing.

## Tier 2 review (2026-10-15)

Review result: buildable with assumptions (the best-documented of the three: published length and height, two good photographs, visible piers in the aerial). Added:

- `elevation/profiles.csv` by `scenery-edmonton-bridges/tools/lidar_pil.py`. Rail first returns 651.3 to 651.7 m along the whole structure (flat); bare earth meets the deck at about 5 m (NW) and 510 m (SE) along the NW to SE axis (504 to 505 m, equal to the published 504 m); water from about 130 to 343 m, with the slopes either side up to 30 m below the deck.
- River piers read from the 2019 aerial (tan cutwaters visible in the water, 3.3 px per metre): 141, 210, 279 m, plus a bank pier at 354 m, from the NW end of the axis. Steel trestle bents (X-braced towers) at about 23.5, 55 and 86 m on the NW slope and 401, 433 and 465 m on the SE slope (aerial shadows, spacing about 31 m). Truss spans 141-210 and 210-279 (69 m), 279-354 (75 m), 86-141 (55 m).
- The 2011 photograph (locomotive 4.7 m high) gives a truss depth near 14 m between the piers: deck-level top chord, bottom chord resting on the pier tops, sloping end posts, X-braced verticals, tan tapered piers. Piers rise about 25 m from the water.
- The 1912 plate (shore cut with falsework) is construction only and gave nothing to scale.
