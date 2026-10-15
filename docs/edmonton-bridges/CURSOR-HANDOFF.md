# Cursor handoff — model from the reference briefs

> **Partly superseded 2026-10-14.** This review was written from each folder alone, before the LiDAR, aerial, river-gauge, street-photo and plate-reading work. Its statement that no site has a deck elevation is no longer true. Each site's "Ask before building" list has been re-checked item by item in `reference/<site>/OPEN-QUESTIONS.md` (Answered, Partly, Open, Sim). Its "Do not invent" lists and unreconciled figures still apply. Read the per-site file first.

Last updated: 2026-10-14. Package: `scenery-edmonton-bridges`. Nothing in this package has been modeled. The coded briefs named in `PRIORITY.md` have all been reviewed.

Each section is one site, reviewed from that site's own `NOTES.md`, `SOURCES.md`, `geometry.json`, and `photos/` only. A number that is not in that folder was not supplied here. A photograph was not scaled. Do not start the glTF for a site until its "Ask before building" list is answered.

The product is the silhouette at about 1,000–3,500 ft AGL. Plan placement uses the nodes in that site's `geometry.json` (EPSG:4326, latitude then longitude). A `plan_length_m` is the horizontal length of that OpenStreetMap way. It is not a structural length. No site in this file has a deck elevation above sea level, so none of them can be seated vertically from the brief alone.

Reviewed in the order in `PRIORITY.md`. Uncoded duplicate folders were not reviewed. The coded folders named in `PRIORITY.md` are the briefs.

## R10 High Level

Folder: `reference/R10-high-level/`. Not enough to build and place.

The plan footprint is in `geometry.json` (outline way 461598489, road way 22915822, streetcar way 463555601, project centre 53.531, -113.511). The altitude is not. `deck_elevation_asl_m` and `mean_water_elevation_asl_m` are null.

**Can draw now.** Two-deck steel truss. Lower deck is the road. Upper deck is one centre streetcar track. Length to use is 777.24 m (2,550 ft). Do not use the other published length, 2,478 ft. Of 28 spans, 18 are itemized: 3 centre Pratt spans of 87.78 m (288 ft) on four concrete river piers; 2 north Warren spans of 39.62 m (130 ft); 7 south Pratt spans of 29.26 m (96 ft); 6 south tower spans of 14.33 m (47 ft) on steel legs. Main-span truss depth is 15.24 m (50 ft), both decks inside that depth. Each deck is 11.89 m (39 ft) wide. The decks are 6.10 m (20 ft) apart. The base of the rail deck is 47.55 m (156 ft) above mean river water. That is not a height above sea level. Those 18 spans sum to 633.38 m. They do not fill 777.24 m.

**Do not invent.** Deck elevation above sea level, the datum, or the elevation of the mean-water surface used for the 156 ft figure. A single as-built river-pier height (the folder records about 125 ft, nearly 100 ft, and a 1910 proposal of 138 ft). Present north and south approach gradients, lengths, elevation changes, and where each meets grade. The 1914 and 1910 figures predate the 1931 and 1971 approach rebuilds. Lengths for the 10 spans the designation does not itemize. Do not assign the unitemized remainder. Do not swap the decks. Do not build the old three-track upper deck. Do not build the Dudley B. Menzies Bridge. Pier count also disagrees (32 concrete piers and pedestals, or four river piers plus 62 smaller piers). The designation already gives four river piers and south tower spans on steel legs. Do not choose the other count.

**Ask before building.**

1. Rail-deck elevation above sea level and the vertical datum, or the mean-water elevation in that same datum. Closest figure: 47.55 m above mean water. Both ASL fields in `geometry.json` are null.
2. Lengths and order of all 28 spans, including the 10 not itemized, reconciled with the 1914 plate. Closest material: the 18 itemized spans, and `photos/elevation-drawing-railway-age.png`.
3. One as-built river-pier height and the two points it is measured between. Closest figures are the three disagreeing heights. `photos/underside-pier-from-menzies.jpg` and `photos/elevation-with-streetcar.jpg` show the shafts.
4. Present north and south approach gradients, lengths, elevation changes, and the elevation where each meets grade. Closest material: the horizontal approach ways in `geometry.json`. The approach photos and the 1914 plate predate the rebuilds.
5. Whether the outer steel is the 11.89 m deck width or the recorded 43 ft overall width. Closest statement is the width section of `NOTES.md`. There is no cross-section drawing in the folder.

**Photos.** Elevation, river piers, both decks, and the south towers are in the folder. `photos/upper-deck-tracks-historical.jpg` and the approach photos are the historical arrangement. No present-day photograph of either road approach after 1931 and 1971. No present-day view along the single upper track. No photograph ties the deck to a geodetic benchmark.

## R9 Dudley B. Menzies

Folder: `reference/R9-menzies/`. Enough to fix the plan path and the box cross-section. Not enough to seat the model, place the piers, or mark where the box becomes the abutment spans.

The nodes for way 533052900 lay the deck in plan. East track way 700467672 is 685.1 m. West track way 37834327 is 682.3 m. Centre 53.531, -113.512. Use 530 m only for the seven-span box. Do not stretch that box to 685 m. No deck elevation above sea level and no datum. `deck_elevation_asl_m`, `height_above_river_m`, `clearance_above_river_m`, and `vertical_datum` are null. The 23 m figure is the University station platform below the road. It is not a deck elevation.

**Can draw now.** Present-day curved concrete segmental box, two direct-fixation tracks, blue edge railings, centreline catenary. Box about 4.5 m deep by 4.5 m wide. Top deck about 10 m wide. Seven continuous box spans, three of them the river spans, plus two slab-and-girder spans at the north abutment and four slab spans at the south abutment. A concrete walkway with blue hangers under the three river spans. Piers are single round columns with a wide cap. The north end meets a concrete headwall. Do not model the High Level truss.

**Do not invent.** Length of each box span, and the lengths of the two north abutment spans and the four south abutment spans. Do not make those lengths by subtracting 530 m from 600 m or from 685 m. Pier count, pier height, and pier spacing. Clearance above the river, and the deck elevation above the river and above sea level, with the datum. Gradient and elevation change on each portal side. The University tunnel mouth. The vertical distance from the walkway to the box soffit.

**Ask before building.**

1. Deck elevation above sea level, with the datum, at the north portal, over the river, and at the south portal, and the river elevation in that same datum. Closest figure: the null elevation fields. `photos/north-portal.jpg` shows the deck still up at the headwall.
2. The seven box-span lengths and the two north and four south abutment lengths, in order along the mapped tracks, or a plan of pier centres. Closest figure: the span counts, and `photos/pier-column-and-walkway.jpg` for one column and cap.
3. The vertical distance from the box soffit down to the walkway, and which part of the mapped run is the three river spans. Closest figure: the walkway photos. Way 424285379 is 296.4 m and is not that survey.
4. An open view of the University tunnel mouth. Closest figure: `photos/north-portal.jpg` is the downtown mouth.

**Photos.** Side elevation, one pier, the track deck, the hung walkway, and the downtown portal are in the folder. Absent: the University tunnel mouth, the four south abutment spans, an end-on box section, a full pier line, and an aerial of the whole crossing.

## R11 Walterdale

Folder: `reference/R11-walterdale/`. Not enough to build and seat the 2017 arch.

The road, west sidewalk, and east-path nodes lay the crossing in plan. Centre 53.529, -113.502. Road way 175326660 is 260.7 m, south to north. Use 230 m for the structural deck between abutment centrelines, and 206 m for the arch span from bank to bank. `deck_elevation_asl_m` and `midspan_height_above_water_datum` are null. The only water-related height is 13.3 m at mid-span. The mean-water elevation is not in the folder, so that label cannot become a height above sea level.

**Can draw now.** The 2017 twin through-arch on 105 Street. The erection ties were removed. The deck has no tie. Do not model the 1913 truss. Each rib is a curved steel box, about 2.5 m by 2.5 m at the base to 1.4 m by 1.4 m at the crown, inclined 13.5° from vertical, leaning toward the other rib. No pier in the channel. Traffic deck 22.4 m wide, three northbound lanes. The west sidewalk is inside that width and inside the hanger plane. The road hangs on two planes of 16 hangers at 10 m centres. The east shared-use path is a separate trapezoidal box, 1.4 m deep, clear width 8 m at the banks and 4.2 m near mid-span. The City's "up to 9 m" at the ends is also on record. Its plan is way 451293733. Four concrete support legs show at the arch feet. The thrust blocks are buried. The steel reads white to light grey.

**Do not invent.** A single arch rise. The folder records 56 m above the thrust blocks, 43 m and 40 m above the deck or roadway, and 55 m and 54 m above the river. One source also says 54 m measured from the deck. Rib-to-rib spacing at the crown and at the feet. Where the 230 m between abutment centrelines sits on the 260.7 m mapped way. Strut count. Delta-pier count. Longitudinal grade, and where the north and south roads meet grade. The station of the first road hanger. Deck elevation above sea level, the datum, and whether 13.3 m is to the roadway or the soffit. The arch curve cannot be closed from these figures.

**Ask before building.**

1. One as-built crown height above the roadway, and the same crown above the arch foot. Closest figures: 56 m above the thrust blocks, 43 m above the deck, 40 m above the roadway, and 54 m and 55 m above the river.
2. Rib-to-rib centre spacing at the crown and at the feet. The 13.5° lean has no base width. Closest views: `photos/elevation-from-south-bank.jpg` and `photos/struts-from-north-bank.jpg`.
3. Deck elevation above sea level, with the datum, at mid-span and at each abutment, the water elevation used for the 13.3 m label, and whether 13.3 m is to the roadway or the soffit. Closest figure: 13.3 m, datum blank.
4. Where the 230 m abutment centrelines fall on way 175326660. The mapped bridge way is 260.7 m.
5. Strut count and spacing. Closest statement: a strut count is not given. Closest views: `photos/struts-from-north-bank.jpg`, `photos/arch-and-hangers-southwest.jpg`, `photos/deck-and-south-approach.jpg`.
6. Delta-pier count and their stations along the path. Closest statement: near the water's edge, number unpublished.
7. Longitudinal grade of the span, and the gradient, length, elevation change, and grade point of 105 Street north and Walterdale Hill south. North way 471835847 is 112.3 m and clipped. South ways 931254808 and 1516540140 are 31.3 m and 19.0 m and clipped.
8. The distance from the abutment centreline to the first road hanger. Closest figure: 16 hangers per plane at 10 m centres.

**Photos.** Full side elevation, the open channel, the separated east path, the soffit, one support leg, and both ends of the deck are in the folder. Absent: a dimensioned elevation, an aerial, a pier schedule, a cross-section, and either climb to the point where the road meets grade.

## R14 Tawatinâ

Folder: `reference/R14-tawatina/`. The river-span outline and the plan centreline are in the folder. The model cannot be seated, and the south-guideway piers are not defined.

Both Valley Line tracks, the hung path, and the approach polylines are node lists. EPSG:4326, latitude then longitude, plan only. The south elevated guideway follows the bridge-tagged corridor from the river piece at 53.539229 to the bridge-tag ends near 53.5374. `upper_deck_elevation_m`, `lower_deck_elevation_m`, and `vertical_datum` are null. The folder records water levels 615.60 m and EL 615.9 and a 10 m clearance window, and it did not turn those into a deck elevation.

**Can draw now.** A 260 m extradosed concrete box in three spans: 100 m north, 110 m south, and a 50 m side span. The box is trapezoidal, 11 m wide and 3.5 m from top of deck to soffit. Two tracks at 1,435 mm gauge. Two pylons stand on the north river pier only, with no member joining them above the deck. The south river pier matches that pier only up to the superstructure. Two river piers, and the path passes through an opening in each. Deck-level leg width is limited to 4 m, and the taper to 1 in 60. Those are limits, not a surveyed height. Seven stays lie in each of two outer planes, between 17.4° and 26.2° from horizontal. The lower deck is an 8 m wide, 0.40 m deep steel path. Its bridge-tagged centreline is 190.8 m and it does not continue over 98 Avenue. The south deck ribbon can follow the nodes at the 11 m upper-deck width. Do not model the Muttart stop, the conservatory, the Edmonton Queen, or the north tunnel.

**Do not invent.** Surveyed pylon height. The requirement is 24 m to 30 m from the top of deck, and the contractor says 30 m pylons. The 30 m figure does not restate the datum. LRT deck elevation and pedestrian deck elevation, in any datum. As-built clearance over the river. As-built length, span lengths, and pier count of the south guideway. The mapped runs south of the river piece are 210.6 m and 212.7 m. Those are bridge-tag lengths, not pier spacing. The 2013 drawing's three 40 m spans are marked approximate. As-built gap between the girder soffit and the pedestrian deck. As-built south ramp length, gradient, and elevation change, and the surveyed point where the ramp meets grade. The 199.1 m and 213.1 m clips reach the mapped stop and are not that point.

**Ask before building.**

1. Surveyed pylon height from the top of deck. Closest figure: 24 m minimum and 30 m maximum from the top of deck, and American Bridge's "30-metre pylons."
2. LRT deck elevations at the north and south bridge-tag nodes, and the pedestrian deck elevation, in one named datum. Closest figures: 615.60 m and EL 615.9, datum unnamed, and the 10 m window. A 2013 river-profile label reads −1.90%.
3. As-built pier count and span lengths from the end of the 50 m side span to the end of the elevated structure. Closest figures: 210.6 m and 212.7 m of bridge-tagged track south of 53.539229, and the 2013 approximate 40 m labels.
4. Built gradient of the south ramp and the surveyed point where it meets grade. Closest figures: 2013 labels −5.600% and −0.275%, and the clips to the mapped stop.

**Photos.** Side elevation, both pylons, both decks, the river pier, the hung path, and the upper tracks are in the folder. The south-guideway photo is the April 2020 falsework. The view from the stop is 10 August 2020, while the stop was still track slab. Absent: a finished close view of the guideway over 98 Avenue, a finished north tunnel portal, and a present-day view of where the south ramp meets grade. No photo carries an elevation or a scale.

## P152 Muttart stop

Folder: `reference/P152-muttart/`. The two side-platform slabs can be laid in plan. The model cannot be seated. The canopy roof plan is not in the folder.

West platform way 1157283683 has long sides of 103.8 m. East platform way 1157283685 has long sides of 103.6 m. The concrete slab is the gap between those rings. Centre 53.53621, -113.48000 is the south stop node, not a platform outline. Wikipedia's 53.53639, -113.47944 was not used. `platform_elevation_m` and `vertical_datum` are null. Phone GPS altitudes in the photograph files were not used. The 90 m figure is a minimum for the longest train. It is not a measurement of this platform.

**Can draw now.** Two side platforms at grade, two tracks in a concrete slab between them. The canopy reads as a curved metal roof, a wood soffit, and glass shelters. No canopy ring is in `geometry.json`, so the roof has no outline to trace. Do not model the pyramids, the greenhouses, or the Tawatinâ bridge.

**Do not invent.** Platform elevation above sea level, and the vertical datum. A surveyed platform length that reconciles the 90 m minimum with the mapped 103.8 m and 103.6 m sides. The canopy footprint. The agreement states at least 125 m² under canopy on each side platform, an underside at most 3.8 m above the platform, and columns at least 3,000 mm on centre. Those are requirements. Best Fronds is two sections, each 30 feet long and 4 feet high. Those feet are the artwork. Whether the storage track conceived in 2013 on the northwest side was built. That siding was not found as its own way.

**Ask before building.**

1. Platform elevation above sea level and the vertical datum. Closest figure: both fields are null. The 6 m ramp figure is a maximum from adjacent grade to top of rail.
2. The as-built roof plan on each platform, the part of each ring that is covered. Closest views: `photos/platform.jpg`, `photos/shelter.jpg`, and `photos/train.jpg`. No length was read from them.
3. Whether the 2013 storage track on the northwest side was built. Closest figure: `photos/platform.jpg` shows two tracks in the slab.

**Photos.** The finished platform and canopy are in `photos/platform.jpg`, `photos/shelter.jpg`, and `photos/train.jpg`. `photos/ramp.jpg` is 10 August 2020, before the canopy. Absent: a present-day view of the finished stop at the bottom of the ramp, an aerial, and the stair from grade to the north access of the west platform.

## B254 Muttart Conservatory

Folder: `reference/P152-muttart/B254-conservatory/`. The four pyramids and the greenhouse ring can be laid in plan, and floor-to-apex heights are published. The air silhouette cannot be closed, and the model cannot be seated.

The four rings are in `geometry.json`: tropical north (way 714340898), temperate south (way 714340901), arid east (way 714340899), feature west (way 714340900). File centre 53.5354324, -113.4783154 is the area-weighted centre of the four outer rings. Wikipedia's coordinate was not used. `ground_elevation_m` and `vertical_datum` are null. No elevations are stored.

**Can draw now.** Four glass pyramids in a symmetrical group, connected by a central court. Larger pair, tropical and temperate: floor to apex 24 m. Guinness writes 24 m (78 ft 8 in). Monumentous states 79 feet. Those were not averaged. Smaller pair, arid and feature: 18 m. Guinness writes 18 m (59 ft). The City and Monumentous state 59 feet for the arid pyramid. The support-greenhouse plan is the western outer ring, way 1287216690, a row of low pitched glass roofs on pale frames. The eastern ring is the garden that contains the main entrance. The two small south rings are not display pyramids. The glass reads as a square pane grid, light mullions, a louvered band under the apex, and reflective glass, rising from grass berms. Do not model the stop or the bridge.

**Do not invent.** A published base side. No source says the base is square. The mapped edges are unequal. Apex coordinates. Ground elevation, the vertical datum, berm height, and the height of the sill at the glass line. The 24 m and 18 m figures are floor to apex. They were not turned into a slope length. A published height and size of the centre skylight. The OpenStreetMap height tag of 4 is not a published height. A published height and roof pitch for the support houses. Six and nine are both published as a count of houses. The 2009 entrance is a fifth pyramid of black granite, facility size 233 m². That area is not a base side.

**Ask before building.**

1. A published base side for the large pair and the small pair, and whether each base is square. Closest figures: the unequal `edge_m` lists, and the floor areas in `NOTES.md`. `photos/group.jpg` and `photos/elevation.jpg` were not scaled.
2. The apex position in plan. Closest figures: the ring centres. Those centres are not apex coordinates.
3. Ground elevation above sea level, with the datum, plus berm height and the height of the sill at the glass line. Closest figures: the null elevation fields, and the berms in `photos/elevation.jpg` and `photos/group.jpg`.
4. Support-house height, roof pitch, and whether the row is six houses or nine. Closest figures: west-ring way 1287216690, and `photos/greenhouses-from-pyramids.jpg`. The 3,700 m² figure is the area of that complex.

**Photos.** All four pyramids, the berms, and the greenhouse row are in the folder. Absent: an aerial, a site-plan photograph, one frame in which the pyramids and the stop are both identifiable, a frame of the centre skylight, and a view of the greenhouse roofs from above.

## V257 Edmonton Queen

Folder: `reference/V257-river-queen/`. The hull, its plan size, and its map position are in the folder. The aerial silhouette cannot be finished, and the model cannot be seated.

Transport Canada states length 51.78 m and beam 12.00 m. The 16 June 2018 FAQ states 51.79 m and 12.01 m. The auction sheet states 169.91 ft and 39.4 ft. The Journal states 51 metres. Wikipedia's article text states 52 metres. Those citations were left uncombined. Pier way 67563569, centre 53.5395342, -113.4818826, is the stored centre. Vessel way 1373511013, centroid 53.5396064, -113.4819983, is where the hull belongs. The longest span between vessel corners is 53.5 m. That span is not the registered length. No elevations are stored.

**Can draw now.** One hull, official number 817706, registry name EDMONTON QUEEN (THE), docked on the south bank at Rafter's Landing. Two stern wheels, Journal diameter 16 feet. Two decks: enclosed lower deck, open upper deck under a blue canopy, wheelhouse at the forward end of the upper deck. Paint from the photographs: white house, blue hull, red stripe, blue canopy, red wheels. The side elevations show no tall stack. When docked, the bow points west toward the Low Level. Do not model the neighbouring bridges.

**Do not invent.** Freeboard. The height of the lower deck, the upper deck, and the wheelhouse above the water. The height of the canopy. An air draft. The 10 m Valley Line window is not a height of this boat. Do not use the mapped pier edges or the vessel edge lengths as the hull or the dock. Do not average the length citations or the beam citations.

**Ask before building.**

1. A published height above the water for the deck line, the lower deck, the upper deck, the wheelhouse, and the canopy. Closest view: `photos/elevation.jpg`, the 28 September 2008 side elevation. No height was read from it.
2. An elevation above sea level for the waterline or the dock, with the datum named. Closest figure: the pier centre and the vessel nodes, with no elevations stored.

**Photos.** Full side, stern quarter, one wheel, and the mooring are in the folder. The newest saved view is 18 June 2018. Absent: an overhead, a bow-on view, a 2024–2026 photograph, and a frame with the boat, the Low Level, and the Tawatinâ together.

## R15 Dawson

Folder: `reference/R15-dawson/`. The plan and the five span lengths are in the folder. The model cannot be seated, and the side silhouette must not be invented.

Road way 22916476 is a straight line, 237.1 m, from Riverdale to Forest Heights. Outline way 642360972 has long sides of 236.2 m and ends of 14.4 m. Use 236.5 m between abutment walls. A total length of 236.6 m is also published. Those were not averaged. Centre 53.549, -113.467. `deck_elevation_asl_m` is null. The OpenStreetMap `maxheight=4.5` tag is not a deck elevation.

**Can draw now.** A single-deck, five-span riveted steel through-truss. Spans west to east: 43.3 m, 43.3 m, 43.3 m, 76.2 m, and 30.5 m. The 76.2 m span is the navigation span. That figure is a length. The elevation reads as three lower polygonal spans, one higher polygonal span, and one shorter, lower span. HistoricBridges names three Camelback spans, one 14-panel Pennsylvania span, and one small Pratt span. The 14-panel count is for the Pennsylvania span only. Two asphalt lanes, clear width 8.1 m. Two wood sidewalks outside the trusses, each 2.65 m clear after 2010. Four concrete piers in the channel, wider toward the water, and an abutment at each bank. The steel reads blue. Do not reuse the High Level model. The 2010 work kept the truss outline. The 2026 work does not describe a new truss or a new pier shape.

**Do not invent.** Deck elevation above sea level, the datum, and soffit elevation. Clearance to the river, and a navigation clearance. Truss depth. Panel counts for the three Camelback spans and the east Pratt span. Pier heights. Longitudinal grade. Where each approach meets grade, and the length, gradient, and elevation change of each climb. What the Wikipedia and Structurae 12.5 m width measures. Do not treat 7 m, 8.1 m, 12.5 m, or 14.4 m as an out-to-out structural width.

**Ask before building.**

1. A deck elevation in metres above sea level, with the datum, at each abutment. Closest material: `deck_elevation_asl_m` is null. The small pier and water figures on the 1912 general arrangement were not legible and were not transcribed.
2. Truss depth, and panel counts for the three Camelback spans and the east Pratt span. Closest material: the Pennsylvania span is 14 panels and 76.2 m. `photos/elevation-five-spans.jpg` and `photos/elevation-and-east-bank.jpg` must not be scaled.
3. Pier shaft height. Closest material: the same two elevation photos, and `pier_height_m` is null.
4. What the published 12.5 m width measures, or an out-to-out width. Closest material: clear width 8.1 m, sidewalk clear width 2.65 m, mapped ends 14.4 m.
5. Where each approach meets natural grade, and the elevation change of that climb, if the approaches are part of the model. Closest material: the approach polylines, and `photos/east-approach-curve.jpg`, which does not show the bridge.

**Photos.** Both elevation files show all five spans and the pier shafts. The sidewalk photo is 2016, before the June 2026 barrier replacement. The east portal is 2008, before the 2010 widening. Absent: a Riverdale approach photograph, a present-day vehicle deck, a close pier, an underside, and an aerial.

## R13 Low Level

Folder: `reference/R13-low-level/`. Both spans can be laid in plan. The model cannot be seated. Truss depth, pier height, and the 1949 span lengths one by one are missing.

Centre 53.538, -113.487. The 1900 span is the downstream east deck, northbound, way 31882107, plan line 213.9 m. Published structure length 213.1 m. The 1949 span is the upstream west deck, southbound, way 22916473, centreline 212.6 m. Wikipedia's infobox states 211.7 m. Those lengths stay unreconciled. Outline way 462866197 encloses both decks. The ends are 23.4 m on the north and 23.5 m on the south. Gauge 05DF001 at this bridge uses an assumed datum. No deck elevation above sea level is in the folder.

**Can draw now.** Both spans, side by side. The May 2026 decommissioning has not happened. The 1900 span is a riveted steel Pratt through truss with horizontal chords. HistoricBridges states 7 panels on the page whose structure length is 213.1 m. The 2008 paper states four equal spans of 53 m. HistoricBridges states a main span of 170.0 feet (51.8 m) and four main spans. Keep those as separate figures. After 1980 the northbound truss centrelines are 7,925 mm apart. Three concrete piers on timber piles, wider toward the water, and an abutment at each bank. The sidewalk is on the east side, outside the truss. Two asphalt lanes run northbound. The 1949 span was built to resemble it, and the photographs show a second horizontal-chord through truss. Two asphalt lanes run southbound. Each span has one sidewalk, and none between them. Do not model James MacDonald, Grierson Hill, the funicular, the hotel, Rossdale Road, or the south roadworks.

**Do not invent.** Deck elevation above sea level, and the datum, for both spans. Clearance to the river, and a navigation clearance. The 13 m figure is the 1915 flood above low water. Truss depth, for both spans. Southbound span lengths one by one. Pier heights, for both spans, and a pier count for the southbound span alone. Longitudinal grade. Where McDougall Hill, Connors Road, Rossdale Road, and Scona Road meet grade. Keep 53 m and 51.8 m apart.

**Ask before building.**

1. Geodetic elevation of each end of each deck, with the datum. Closest material: no elevation on the nodes. Gauge 05DF001 is an assumed datum. The 13 m line is the 1915 flood above low water.
2. Truss depth of each span. Closest views: `photos/elevation-aligned-spans.jpg` and `photos/elevation-toward-downtown.jpg`. The depth is not published.
3. Pier height for each span, and a pier count for the 1949 span alone. Closest figure: three concrete piers for the 1900 span. `photos/underside-and-pier.jpg` shows two faces side by side and does not number the west span.
4. Southbound span lengths one by one. Closest figures: the uncited infobox total 211.7 m, and way 22916473 at 212.6 m. Those are totals.
5. Which published 1900 bay length sets the pier stations: four equal spans of 53 m, or a main span of 51.8 m. Both are already in `NOTES.md`.

**Photos.** Side elevations, both portals, the outer sidewalks, and pier shafts are in the folder. The side elevations hide the second span. No kept photo shows three northbound piers. No kept photo follows an approach to grade. The only kept view after the December 2025 repairs is `photos/underside-and-pier.jpg`.

## R12 James MacDonald

Folder: `reference/R12-james-macdonald/`. The present-day deck footprint can be laid in plan. The model cannot be seated. Span lengths, haunch depths, pier stations, and the two 1971 approach bridges are unpublished.

Outline way 626069071: west end 29.9 m, east end a 37.3 m edge and a 2.9 m jog, north edge 381.6 m, south edge 371.4 m. Westbound way 25455305 is 381.4 m, three lanes. Eastbound way 25455308 is 375.6 m, three lanes. Six lanes in all. Centre 53.536, -113.488. Wikipedia's 359.7 m and Structurae's 359.66 m are totals and different extents. They were not averaged. No deck elevation and no datum.

**Can draw now.** The 1971 haunched concrete girder, in plan. The underside photo shows several girders side by side, deeper at the pier than toward midspan, with cross-frames. That soffit is not a closed box. The north footway is a 367.4 m centreline. Its width is not published, so it stays a line. Approach and ramp centrelines can be drawn in plan only, including the Cloverdale one-lane ramp, way 106711220, 308.1 m. Do not model the Low Level trusses. The three unbuilt spans south of this one stay out.

**Do not invent.** Deck elevation above sea level, the datum, and soffit elevation. Span count and span lengths. Girder depth at the pier and at midspan. Pier count, pier heights, and the plan size of the shafts. Where the two approach bridges in the Journal's 2007 recap are. Longitudinal grade. Where 97 Avenue at Rossdale and 98 Avenue at Cloverdale meet grade. Do not scale the photographs. A count was not taken from them.

**Ask before building.**

1. A geodetic deck elevation and its datum, plus the elevation where 97 Avenue and 98 Avenue meet natural grade. Closest material: plan nodes only. The 7.5 percent figure on 98 Avenue is unconverted and unlocated.
2. Span lengths or pier stations, and the plan size of the shafts. Closest view: `photos/elevation-from-south.jpg` shows two channel shafts, with the abutments outside the frame.
3. Girder depth at the pier and at midspan. Closest view: `photos/underside-from-river.jpg`, which was not measured.
4. Which structures the Journal's two 1971 approach bridges are. Closest views: `photos/underside-over-park.jpg` and `photos/east-approach-toward-muttart.jpg`.

**Photos.** The south-bank elevation, the soffit, a channel pier, and the Cloverdale end are in the folder. Absent: a close river-span deck, a close Rossdale approach, and a north-bank elevation.

## N258 Grierson Hill

Folder: `reference/N258-grierson/`. The road centreline can be laid in plan. The deck outline is not in the folder, and the model cannot be seated.

Way 106711211 is two stored nodes, 59.0 m. The live coordinates of the same nodes are 59.1 m. Use the stored nodes. Do not average them, and do not use either length as the built length. Centre 53.538564, -113.488789. Two lanes, two-way, asphalt, `layer=1`. `width_m`, `deck_elevation_asl_m`, `soffit_elevation_asl_m`, and `vertical_datum` are null. The deck crosses McDougall Hill Road ways 1433098757 and 303665641. Those ways have no nodes in this file.

**Can draw now.** The 2012 replacement: deck demolished and rebuilt, then paved, with a new guardrail, on pier columns, carrying Grierson Hill Road over McDougall Hill Road. Approach centrelines exist in plan only. Do not build the Low Level decks, the hillside footbridge, the cloverleaf links, or the MacDonald Drive pedestrian underpass. Do not build this outline from `photos/from-funicular.jpg`. The pier in that frame is the 2016 footbridge.

**Do not invent.** Span count. A published structure length. Pier count, pier height, and abutment form. Clearance under the deck. The tags `maxheight=5.2` and `5.0` are on McDougall Hill Road. They are not this clearance and not a deck elevation. Deck elevation, soffit elevation, and the datum. Width and lane width. Longitudinal grade, and the grade point at either end. A model that joins the two roads at one level is the wrong interchange.

**Ask before building.**

1. A deck elevation above sea level, with the datum. Closest item: both fields are null. The 2018 landslide elevations were not used.
2. A published clearance under this deck, or a pier height. Closest item: the McDougall Hill `maxheight` tags, which the folder says are not this clearance.
3. A published structure length, or a statement that the deck ends are the two stored nodes. Closest item: the 59.0 m and 59.1 m centreline lengths.
4. The deck width. Closest item: two lanes, and `width_m` null.
5. The number of spans or piers, and the abutment form at each end. Closest item: the 2012 news words for columns and pillars, with no count.
6. The vertical profile of Grierson Hill Road on the span, and the elevation where each approach meets the ground. Closest item: the approach polylines. The northeast far node is a junction. The southwest far node is the Rossdale Road intersection.
7. One drawing or photo that shows this deck over McDougall Hill Road, or the City 2025 orthophoto tile 33183E593382N named in `SOURCES.md`. Closest saved figure: `photos/from-funicular.jpg`.

**Photos.** One file, `photos/from-funicular.jpg`, 15 December 2017. It shows the funicular stairs, a kinked wood-deck footbridge, and the Low Level truss. This deck's elevation, piers, soffit, and approaches are absent.

## F256 Funicular

Folder: `reference/F256-funicular/`. The funicular, the lookout, and the Grierson Hill Road footbridge can be laid in plan. They cannot be seated. The as-built rail rise and the rail length are unresolved. The footbridge span is not in this folder's photos.

The track is a straight line from 53.5396888, -113.4896381 to 53.5394103, -113.4887917, horizontal length 64.0 m, way 490235928. The stored centre 53.539305, -113.487472 is the footbridge outline, not the track. The footbridge ring is way 1271848915, perimeter 191.0 m. The kinked centreline is way 533867748, 91.0 m. `deck_elevation_asl_m` and `vertical_datum` are null. Do not model the Grierson Hill road bridge or the hotel.

**Can draw now.** One glass cabin on two rails on a steel beam, with the stair beside the rails and a canopy at the top. The recorded grade is 23.5 degrees from horizontal. The published footbridge spans are a 50.0 m main span, a 19.4 m span, and a 19.0 m cantilever. The south end cantilevers past the elevator shaft. The lookout is that railed river-end deck, with a glass elevator shaft. Its stated cantilever is 19 m, and its stated height is 19 m above the river bank. The named supports are one concrete pier and that shaft. The urban stair width stays the published range, 4.5 m to 7.5 m.

**Do not invent.** An as-built vertical rise. The 25 m drop is a 2015 pre-construction figure. The 50 m figure is the valley, not the track. The 66.0 m at 23.5 degrees was not converted into a rise. Which published track length is the as-built length along the rails. The Journal states 55 m. The award submission states 66.0 m along the grade. The mapped line is 64.0 m horizontal. Do not add the three spans, and do not match them to the mapped edges. Do not draw the promenade. The Journal states a 200 m walkway. The City states about 260 m for the whole walk. The 55.3 m gap between the mapped track and the mapped bridge is neither of those. Pier height. Do not use the City's approximate 6 m as a deck elevation.

**Ask before building.**

1. Which length is the as-built length along the rails. Closest figures: 55 m, 66.0 m along the grade, and 64.0 m horizontal.
2. The as-built vertical rise of the track. Closest figures: the 2015 25 m drop, the 50 m valley figure, and 66.0 m at 23.5 degrees, which this folder did not convert.
3. An elevation above sea level, with the datum, for the track ends and the lookout deck. Closest figures: the City's approximate 6 m above the roadway, and the lookout's 19 m above the river bank.

**Photos.** The rails, one glass cabin, the stair, the upper canopy, and the lookout shaft are in the folder. `photos/lookout-and-truss.jpg` is 8 August 2017, during construction. The footbridge span, the kink, and the pier are absent from this folder's photos. The 15 December 2017 view of that span is in the Grierson folder and was not copied here.

## B255 Hotel Macdonald

Folder: `reference/B255-hotel-macdonald/`. The mapped footprint can be laid in plan. The château mass, the steep copper roof, and the turrets are named. The model cannot be seated. Grade-to-ridge and grade-to-turret are blank.

Way 198826612 is a closed ring of 34 corners, centre 53.540305, -113.489500, perimeter 247.2 m. It is tagged `source=Bing`. The 71.4 m north–south span and the 70.3 m east–west span are the node box. They are not wing length and width. `height_grade_to_ridge_m`, `height_grade_to_tallest_turret_m`, `deck_elevation_asl_m`, and `vertical_datum` are null. Do not model the funicular. The 1953 wing is gone.

**Can draw now.** An L-shaped Canadian château: perpendicular wings, a recessed diagonal entrance, rear façades toward the river, Indiana limestone walls, a steep dormered copper roof, high chimneys, projecting towers, a turret roof, and finials. The survey codes also name a high gable, hip dormers, a cupola or lantern, and a balustrade, still without metres. A vertical outline cannot be built from this folder.

**Do not invent.** A height from grade to the ridge, and a height from grade to the top of the tallest turret. Wikipedia's 47.7 m (156 ft) does not say which point it reaches. Emporis states 155.51 ft architectural and 167.49 ft tip, and does not say ridge or turret. The OpenStreetMap `height=47` tag was not used. A published plan length and width. A surveyed outline. A turret count. The present colour of the copper. The survey compilation says the roof was blackened with age. The 8 October 2011 frame shows green. Those were not averaged. Elevation of the ridge, of the grade at 100 Street, and the datum.

**Ask before building.**

1. A height from grade to the ridge, and a height from grade to the top of the tallest turret, each named. Closest figures: Wikipedia 47.7 m, point unnamed; Emporis 155.51 ft architectural and 167.49 ft tip.
2. The elevation of grade at 100 Street, or of the ridge, with the vertical datum. Closest figure: both fields null.
3. Whether the Bing ring is the footprint to build, or a surveyed outline. Closest figure: the 34-corner ring and the 247.2 m perimeter. The designation says L-shaped and gives no metres.
4. A published turret count, and which roof masses are the turret and the projecting towers. Closest figure: the designation names them, and no count was taken off the photographs.
5. The present copper colour as a specification. Closest figures, left unaveraged: "blackened with age," green slopes in `photos/roof-and-turrets.jpg`, and dark roofs in `photos/river-face.jpg`.

**Photos.** The river face, the south face, and the street-corner roof with a conical green turret are in the folder. No photograph is a plan or an overhead roof.

## N259 Rossdale / McDougall

Folder: `reference/N259-rossdale-mcdougall/`. The plan centrelines are in the folder. The model cannot be seated. The deck width and the gap under the deck are not.

Way 37120045 is the westbound deck centreline, three nodes, 49.1 m, northeast to southwest. That length is the mapped way, not a published structure length. Centre 53.537724, -113.493132 is the midpoint along that way, not a surveyed centre. Approach ways 36610268 (85.1 m), 37120044 (40.0 m), 321190619 (24.4 m), and 321190620 (19.5 m) are in the file. McDougall Hill way 636183922 has no nodes here. `deck_elevation_asl_m`, `soffit_elevation_asl_m`, `vertical_datum`, and `width_m` are null. Do not model a Low Level deck or the Grierson Hill Bridge.

**Can draw now.** A concrete grade separation carrying Rossdale Road over McDougall Hill Road. The June 2013 work was a rehabilitation: hydro-blasting a cast-in-place deck, new curbs, and abutment repairs. The only photo is 6 September 2008, older than that work. It shows a concrete span over a lower road. No height was read from it.

**Do not invent.** Deck elevation, soffit elevation, and the datum. Clearance under the deck. The tag `maxheight=4.5` on way 636183922 is not that clearance and not a deck elevation. Width and lane width. Pier count and pier height. Span count. The mapped centreline is two segments, 49.1 m. That is not a published span count. Gradient, elevation change, and where either approach meets grade.

**Ask before building.**

1. The deck elevation above sea level and the vertical datum. Closest figure: both fields are null. `photos/from-west.jpg` was not measured.
2. The deck width. Closest figure: way 37120045 has no width tag.
3. A published clearance under this deck, or a pier height. Closest figure: `maxheight=4.5`, which this folder says is not the clearance.
4. Whether the opening is abutments only or has intermediate piers. Closest figure: Alberco records abutment repairs and no count. The 2008 frame was not used to count piers.
5. The elevation change along ways 36610268 and 37120044, and the point where each meets grade. Closest figure: those nodes, with each far node not a surveyed grade point.
6. The node list of McDougall Hill way 636183922 if the lower road is part of the same scene. Closest figure: the excluded entry, way id and 165.5 m, no coordinates.
7. A present-day elevation or aerial of this span. Closest figure: `photos/from-west.jpg`, older than the June 2013 work.

**Photos.** One file, `photos/from-west.jpg`, 6 September 2008. The span is small, in the lower right of a downtown skyline. Absent: an elevation that isolates the span, a pier view, a deck view, an approach view, and an aerial.

## N260 Scona / Connors

Folder: `reference/N260-scona-connors/`. The three 98 Avenue valley-floor decks can be laid in plan. They cannot be seated. The file centre is the omitted slope span. Do not use it for these decks.

Westbound 98 Avenue, way 22916470: 76.3 m, three lanes, no City number. Eastbound 98 Avenue, way 106711204: City bridge B126, year built 1971, 81.1 m, two lanes. Unnamed eastbound ramp, way 106711230: 81.3 m, two lanes. It is not B126. The file centre 53.533941, -113.483610 and the 50.4 m length are way 22959547, the Scona Road Bridge (B065), on the wooded slope. Omit it. Omit the Low Level trusses. Connors Road over a ramp, way 34388891, is a third bridge and is not one of these decks. `deck_elevation_asl_m`, `soffit_elevation_asl_m`, and `vertical_datum` are null.

**Can draw now.** Three separate concrete decks on those centrelines, the overpass immediately beyond the Low Level truss. The midpoint of way 22916470 is 138.1 m from that truss node. No girder or slab designation was published for B126. Do not build the westbound span or the ramp as B126.

**Do not invent.** Deck elevation, soffit elevation, and the datum. The mapper tags `maxheight=4.3` and `4.6` are under these spans. They are not a deck elevation. What the 11.1 m width tag on way 22916470 measures. The other two ways have no width tag. Do not treat 11.1 m as the structural width. Which road the City means under B126. The inventory says Scona Road. The tender listing and the league page say Connors Road. Way 106711204 crosses a way named Connors Road NW. A City number and a year for the westbound span. Do not scale the photographs.

**Ask before building.**

1. A deck elevation above sea level, with the datum, for ways 22916470, 106711204, and 106711230. Closest figure: the null elevation fields, and the 4.3 and 4.6 tags that the folder says are not elevations.
2. A published width for each of those three decks. Closest figure: the 11.1 m tag on way 22916470, which the folder says is unpublished, and the lane tags 3, 2, and 2.
3. Which published wording to build under B126. Closest figure: the inventory says Scona Road. The tender, the league page, and way 106711204 say Connors Road.

**Photos.** `photos/overpass-beyond-south-end.jpg` (30 May 2007) and `photos/interchange-and-hill.jpg` (7 April 2008) show the concrete crossing beyond the truss. `photos/span-from-south-slope.jpg` (10 February 2025) was not identified as one of these spans. Absent: a pier or soffit of the 98 Avenue spans, a deck view that separates the three spans, and an identified present-day view.

## R8 Groat

Folder: `reference/R8-groat/`. The river span can be laid in plan. It cannot be seated, and the elevation outline cannot be fixed.

Outline way 626069075, perimeter 627.4 m. That perimeter is the ring, not a span length. East carriageway way 22916458, northbound, two lanes, 291.5 m. West carriageway way 191843040, southbound, two lanes, 291.1 m. East cycleway way 27265608, 291.1 m. Centre 53.537, -113.539. Published lengths, left unaveraged: Wikipedia and Structurae 315.5 m, City Archives 315 m, Graham's project page 1,000 feet, Graham's case study 330 m. `deck_elevation_asl_m` and `deck_elevation_datum` are null. Do not model G116, G117, Z125, T133, G119, or the demolished G118.

**Can draw now.** One river girder bridge: seven spans, two side-by-side carriageways of two lanes. The 2020 superstructure is haunched weathering-steel plate girders with a cast-in-place deck and an asphalt wearing surface. The east shared-use path is 4.2 m, outside the northbound lanes, with a concrete barrier on the traffic side and a metal railing on the outside. South end is River Valley Mayfair. North end is River Valley Glenora. This model is the river span only. Do not build the pre-2020 concrete haunch. The 2008, 2009, 2012, and 2015 photos show the soffit that was removed.

**Do not invent.** Deck elevation, the datum, soffit elevation, and height above the river. The seven span lengths, a pier count, and pier height. Girder depth and haunch depth. Carriageway width, overall width, lane width, and shoulder width. What the mapped 22.1 m north-end edge corresponds to. A west-side sidewalk width. Longitudinal grade. Where the Mayfair road and the Glenora road meet grade. Do not divide a total length by seven. Do not treat the 9.8 m and 9.5 m centreline separations, or the 22.1 m edge, as a published structural width.

**Ask before building.**

1. Deck elevation above sea level, with the datum. Closest record: both elevation fields are null. `photos/elevation-2026.jpg` shows the deck line, and depth was not read from it.
2. The seven span lengths, a pier count, and pier height. Closest record: `span_lengths_m` and `pier_count` are null. `photos/elevation-2026.jpg` shows shafts in the channel, and a count was not taken.
3. Girder depth and haunch depth of the 2020 steel girders. Closest frame: `photos/elevation-2026.jpg`. The older frames are the removed concrete soffit.
4. Overall width, and what the mapped 22.1 m north-end edge is. Closest record: the 4.2 m east path, which is only one strip.
5. Whether a west-side walk exists after 2020, and its width. Closest frame: `photos/deck-northbound-2023.jpg`, which shows the east path.
6. What each published length includes, so 315.5 m, 315 m, 1,000 feet, and 330 m are not substituted for the mapped ways.
7. Where the Mayfair and Glenora roads meet natural grade, with length, gradient, and elevation change, plus the longitudinal grade on the spans. The 350 m figure on the exit sign is the sign, not an approach length.

**Photos.** `photos/elevation-2026.jpg` is the present elevation. `photos/deck-northbound-2023.jpg` is the northbound deck and the east path. The older frames are the removed superstructure. Absent: a close present pier view, a west-carriageway view, and either road meeting grade.

## G116 Hawrelak

Folder: `reference/G116-hawrelak/`. The centrelines can be laid in plan. The model cannot be given an outline or seated. `photos/` is empty.

Centre 53.5322, -113.5383. Bridge-tagged ways, each with its own horizontal length: 106605009 (57.0 m), 106605261 (56.4 m), 106605020 (39.1 m), 160418786 (50.5 m), 474575069 (8.4 m), 474575072 (7.8 m), 501599774 (14.4 m), 474575066 (4.5 m). They are two-lane and one-way. Cycleway way 160418783 is 61.0 m. `deck_elevation_asl_m` is null. The structure those lines belong to is the Mayfair Bridge, Alberta file 76535, year 1966. The inventory row prints GS 3, read as three spans. That printed 3 was not turned into three lengths. Do not add the mapped lines into a structure length. Do not model the river span. The Journal of Commerce "approximately 300 metres" and 1955 are the river bridge. Do not model G118.

**Can draw now.** The park-road and ramp centrelines, tagged bridge and layer 1. The 2018–2021 work is recorded as a rehabilitation. That is a history. It is not an edge, a depth, or a pier line.

**Do not invent.** Published span lengths, and a total length. Deck elevation, soffit elevation, and clearance over Groat Road. The 5.3 tag was not confirmed and is not a clearance. Deck width. The 1.5 m cycleway tag was not confirmed. What the 2018 rehabilitation changed on the silhouette.

**Ask before building.**

1. A deck elevation above sea level with the datum named, plus the clearance over Groat Road or a soffit elevation on that datum. Closest text: "Elevation. Not published." and `maxheight` 5.3, which the folder rejects as clearance.
2. A published outer deck width. Closest text: the cycleway width tag `1.5 m`, which no published source states.
3. Published span lengths, or a plan that places the pier lines for the printed three spans. Closest text: "PJ MAJOR BRIDGE GS 3."
4. Whether the 2018 rehabilitation moved the fascia depth or the pier lines. Closest text: the rehabilitation notes, which do not describe the outline. No elevation photograph was saved.
5. Elevations or a gradient at the ends of the bridge-tagged ways. Closest text: "No gradient is published," and each far node is not a surveyed grade point.

**Photos.** None saved. Graham, Journal, and Global News photographs were not downloaded. The 1919 Commons frame is the streetcar trestle, not this 1966 bridge.

## G117 102 Avenue

Folder: `reference/G117-102-avenue/`. The centreline can be laid in plan. The model cannot be seated. The 22 m figure is ravine depth.

Way 25601853 is two nodes, west to east, 111.9 m. Centre 53.5430, -113.5403. Alberta file B408, the 2016 flyover: one clear span, steel girders, integral concrete abutments, no intermediate piers. The design paper's 113 m length, 83 m main span, and 15.6 m abutment length stay separate. They were not added together. `deck_elevation_asl_m` is null. Do not model the river span, the demolished 1910 trestle, Wellington, or the Groat Road bridge over Victoria Park Road.

**Can draw now.** Four asphalt lanes, a bike lane separated by a concrete barrier, sidewalks, and a metal railing, on that centreline. North footway 120.9 m, south footway 112.1 m, protected bike lane 111.7 m, all without a published width. The only girder depth on file is ENR's roughly 4.2 m at the ends.

**Do not invent.** A deck width. The 13.6 tag, and the approach tags 15 and 14, are not published widths. Do not add or average 113 m, 83 m, 15.6 m, 111.9 m, and ENR's roughly 100 m. Do not assign Alberta's printed 83.3, 18.2, and 68.3. Do not station the 15.6 m abutments on the 111.9 m line by arithmetic. Do not draw a haunch. The EIA caption says steel-haunched. The design abstract does not. Do not use 22 m as a deck elevation or as clearance. Do not scale the three deck photos.

**Ask before building.**

1. The deck elevation above sea level, with datum, at both ends of way 25601853. Closest figures: the null field, ravine depth 22 m, and gauge 05DF001, which was not converted.
2. A published overall deck width, fascia to fascia. Closest figure: width tag 13.6, which this folder says was not confirmed.
3. Girder depth along the span, or an openly licensed side elevation that shows the soffit. Closest figure: ENR's roughly 4.2 m at the ends, and the unresolved "steel-haunched" caption.
4. Where the 83 m steel span and each 15.6 m abutment sit on the 111.9 m centreline, as positions. Closest figures: those lengths kept separate.

**Photos.** All three saved files are 9 September 2016 deck views: lanes, the separated bike lane, the sidewalk, and the railing. A side elevation, the soffit, the abutments, and the approaches are absent.

## Z125 Wellington

Folder: `reference/Z125-wellington/`. The mapped plan can be laid down. The present-day girder cannot be built or seated. `photos/` is empty.

Outline way 1227946189, edges 70.5 m, 16.6 m, 70.5 m, and 16.6 m. The perimeter, 174.2 m, is not a span. Centreline way 37749246 is 72.3 m, west to east. Centre 53.5431, -113.5481. `deck_elevation_asl_m` and `clearance_to_ravine_m` are null. On 14 October 2026 the mapped road is `highway=construction` and `access=private`. That is a closure line, not a girder. Do not model G117, the river span, T133, or G118. The 1932 three-span arch is the structure being replaced.

**Can draw now.** The mapped ring and the centreline, in plan. In words, the finished arrangement is one clear span with the piers eliminated. The City page names a shared pathway on the north, a sidewalk on the south, wider lanes, barriers, handrails, and decorative streetlights. No width in that sentence is a buildable cross-section.

**Do not invent.** Which girder was built, steel or NU2400. A published span length. Do not use 72.3 m or 70.5 m as the structural span. Deck elevation and clearance to the ravine. A girder-design width. The 4.2 m and 2.8 m are the 2023 update. The 23.78 m is the April 2024 preliminary width, later described as due to be reduced. Do not use 16.6 m, the width tag 12.4, or the right-of-way 30.6 m as the girder width. Girder depth. Do not add piers to the finished span.

**Ask before building.**

1. Which option was built, clear-span steel or NU2400, and whether that girder is standing on 14 October 2026 or the site is still the closed replacement. Closest text: the finished-type notes. No award is named.
2. A published structural span length of the built girder. Closest figures: 72.3 m centreline and 70.5 m outline sides, both stated not to be a structural length.
3. The deck elevation above sea level, with the datum. Closest record: the null field, and gauge 05DF001, which was not converted.
4. The as-built out-to-out width after the August 2024 reduction. Closest figures: 23.78 m preliminary, right-of-way 30.6 m, path widths 4.2 m and 2.8 m, width tag 12.4, and outline short sides 16.6 m.
5. The girder depth of the built option. Closest text: the still-missing line. No depth is given.

**Photos.** None saved. City photographs of shoring, a crack, rebar, and the 2024 condition were left as URLs. The April 2024 drawing was not extracted. The 1919 streetcar frame is a different bridge.

## T133 Stony Plain Road

Folder: `reference/T133-stony-plain/`. The mapped corridor can be laid in plan. The finished bridge cannot be built or seated. `photos/` is empty.

Centre 53.5478, -113.5458. Six bridge-tagged polylines: north footway, north carriageway, two Valley Line tracks between the carriageways, south carriageway, and south cycleway. Those horizontal lengths are not the structural span. `span_count` is 1. `pier_count` is 0. `deck_elevation_asl_m` is null. Model the finished bridge. Do not model G118 or the river span. Do not build a pier.

**Can draw now.** The part order, in words: integral abutments, a cast-in-place deck, a separate track slab in the middle, two centre tracks, vehicle lanes, a north sidewalk, and a south shared-use path. Groat Road is the road underneath. The City's reopened section is one vehicle lane each way. The map tags two lanes on each carriageway. Both are kept. The 46 m span, the 25.4 m width, and the 4.2 m sidewalk and path are a minimum or a reference design, not as-built edges.

**Do not invent.** An as-built span length. The 46 m is a minimum. The mapped 60.7 m is not that length. The "about 8 m" is not a length. Deck elevation. The 6 m is a minimum clearance, and the EIA says the old clearance was kept without stating it. Girder depth, and whether the installed girders are haunched. Haunched is the reference design. The installed girders are not confirmed as haunched. As-built width. 25.4 m and 18.4 m are the reference design and the old bridge. Do not use the old 4.0 m bench as the road clearance. Do not draw the southeast MSE wall as a measured 28 m. That is an EIA estimate.

**Ask before building.**

1. As-built span between abutment faces. Closest figure: `minimum_span_length_m` 46, and the mapped way lengths, which are not the span.
2. Deck elevation in metres above sea level, with the datum. Closest figure: the null field, and the 6 m minimum clearance, which is not an elevation. Gauge 05DF001 was not converted.
3. As-built overall width. Closest figure: reference design 25.4 m against an existing 18.4 m.
4. Soffit depth, and whether the girders set in August 2023 are haunched. Closest figure: the site location study's "single-span steel haunched girder." No elevation view was saved.

**Photos.** None saved. Demolition, construction, and the 31 July 2018 EIA plate of the old bridge with piers were not downloaded. The 30 November 2024 road reopening is text, not a photograph.

## G119 107 Avenue

Folder: `reference/G119-107-avenue/`. The Glenora Overpass can be laid in plan from the mapped outline ring. The model cannot be seated. Span lengths were not split from the printed count of 3. `photos/` is empty.

Alberta file B097, a 1967 beam grade separation, two carriageways of 107 Avenue NW over Groat Road. Outline way 1510405388, edges 73.7 m, 38.7 m, 73.7 m, and 38.6 m, perimeter 224.7 m. Those edges are the fascia in plan. They are not a published width and not a span. South carriageway way 22928017, eastbound, two lanes, 75.8 m. North carriageway way 158414123, westbound, two lanes, 75.3 m. Centre 53.5510, -113.5498. `deck_elevation_asl_m` is null. Do not model the river span or Stony Plain Road. Do not divide the 73.7 m edges by 3.

**Can draw now.** The closed ring, both carriageways, and both sidewalks, in plan. The printed span count is 3. That count is not three lengths. No girder depth is in the folder, so the solid under the deck cannot be built.

**Do not invent.** Published span lengths and a total length. Deck elevation and clearance over Groat Road. The 4.8 and 4.9 tags were not confirmed. `clearance_over_groat_road_m` is null. Do not copy river-span lengths or river-pier notes. The 2021 and 2022 rehabilitation notes do not describe a new silhouette.

**Ask before building.**

1. A surveyed deck elevation above sea level and the vertical datum. Closest record: the null field, and gauge 05DF001, which was not converted. The 4.8 and 4.9 tags are not that number.
2. The three span lengths, or the plan positions of the piers. Closest record: the printed count is 3, and `span_lengths_m` is null.
3. A published clearance over Groat Road if the opening is part of the model. Closest record: the unconfirmed maxheight tags on ways 98093800 and 157319879.
4. One present-day elevation view that shows the fascia depth, or a stated fascia depth. Closest record: no elevation was saved. The 1919 streetcar trestle frame is not this deck.

**Photos.** None saved. The elevation, the piers, the deck, and the approaches are all absent.

## Across the set

Every site above can be laid in plan from its own `geometry.json`. None has a deck elevation above sea level with a datum, so none can be seated. Do not start a glTF until that site's "Ask before building" list is answered. Uncoded duplicate folders (`hotel-macdonald`, `B2-hotel-macdonald`, `funicular`, `grierson`, `rossdale-mcdougall`, `scona-connors`, `river-queen`, `muttart`, `P16-muttart`) were not reviewed. The coded folders named in `PRIORITY.md` are the briefs.
