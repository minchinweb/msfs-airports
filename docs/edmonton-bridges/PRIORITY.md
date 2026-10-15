# Edmonton bridges: master priority

Last updated: 2026-10-14. Handoff checklist for `scenery-edmonton-bridges`. Work the empty boxes from the top. A later session should not re-rank from scratch; the scores below are the reason for the order. An empty box is unbuilt. Section 1 was modeled on 2026-10-14 (see `MODEL-NOTES.md`; built and compiled, not yet seen in the sim).

This file covers every structure in `bridges.md`, `freeway-bridges.md`, and `lrt.md`, plus the bridges that exist only as crosses on `edmonton-bridges-map.png` (the Yellowhead row beside CYXD, and the Mill Creek trestle). Codes match `draw-map.py`. A number is used once, whatever the letter. Bridge codes use 1–136. Above-ground stops are P137–P189 and at-grade track sections are K190–K253, both listed in `lrt.md`. B254 is the Muttart Conservatory. B255 is the Fairmont Hotel Macdonald. F256 is the 100 Street funicular. V257 is the Edmonton Queen. N258 is the Grierson Hill Bridge, N259 is Rossdale Road over McDougall Hill, and N260 is the Low Level south roadworks. An Alberta bridge file number such as B065 is not one of these codes. Centres are the inventory centres, not abutment surveys. Deck geometry for the plotted road and river bridges is already in `bridge-geometry.json`. LRT centreline geometry is in `lrt-tracks.json`.

**Elevation blocker answered (2026-10-14).** Deck and river heights from the 2018 LiDAR are in `ELEVATION.md`; the gauge, its datum and the river's seasonal range are in `RIVER-LEVEL.md`; aerials, DEM clips and night photos are in each `reference/<site>/` folder and described in `DATA-SOURCES.md`. Each `MODEL-HANDOFF.md` now has an Update block with the site's numbers. What still blocks is ranked in `BLOCKERS.md`.

The package is the present-day city. Do not rebuild a demolished span. The historic CYXD airport is a separate package; these bridges are what a flight in the current sim sees around it.

## How a bridge scored

Two scores, each 1–5. Order is Look + Where. A neighbour that would leave a hole in the same glance is pulled into the same box even if its own score is lower.

**Look** is the silhouette at 1,000–3,500 ft AGL.

| Look | What earns it |
| --- | --- |
| 5 | A shape you can name: steel truss, tied arch, extradosed pylons, open-spandrel or network arch, a guideway about a kilometre long, a three-level flyover. |
| 4 | A long or wide deck that holds together as one object: an eight-lane river bridge, a triple crossing, a system interchange. |
| 3 | A deck that reads against the valley, a ravine, or a rail yard. A footbridge only if it sits in open valley. |
| 2 | An ordinary freeway girder, a short LRT span, a small footbridge. |
| 1 | A diamond or partial cloverleaf over an arterial, and not on a published route. At 2,000 ft it is a speck. A cloverleaf that is a named checkpoint is a 3: the loops are the landmark. |

**Where** is how often it is in the windscreen on a VFR flight among CYXD, CYED, CYEG, CZVL, CFB6, and CEZ3. The CYXD thresholds used for the offsets are the ones in `airport-cyxd` scenery:

| Runway | Threshold | The airplane is coming from |
| --- | --- | --- |
| 34 | 53.5664, -113.5128 | South, over the downtown valley. Extended centerline is longitude -113.513. |
| 30 | 53.5684, -113.5143 | Southeast, up the east side of the valley. |
| 16 | 53.5780, -113.5128 | North, across the Yellowhead. |
| 04 | 53.5723, -113.5266 | Southwest, across the Groat ravine, and further out toward West Edmonton Mall. |

| Where | What earns it |
| --- | --- |
| 5 | On a CYXD final inside 5 km and within 0.8 km of the extended centerline, the access bridge on one of the six fields, or a named checkpoint on the Edmonton VFR terminal chart. |
| 4 | On a CYXD final inside 8 km and within 2 km of the centerline, or an interchange on a published helicopter route. The City Centre heli chart flies those at 3,000 ft ASL, about 800 ft above the field, so the exchange is the picture. |
| 3 | On a VFR line between the fields (Henday, Yellowhead, Whitemud, QE2, Sherwood Park Freeway, Manning) and big enough to see at enroute altitude. |
| 2 | On that line only as a speck, or a modest structure inside the ring and off the finals. |
| 1 | Off those lines. A flight has to go looking. |

The plates are `docs/cyxd/charts/procedures-2010/vfr-vtpc.png` (checkpoints and coordinates on `vfr-vtpc-cont.png`, transcribed in `docs/cyxd/procedures-2010.md`) and `heli-vtpc.png`. The named fixes that are bridges or exchanges: **Bridges** (VCBRG, the Beverly / Clover Bar crossing), **Quesnell Bridge** (VCQSN), **Bremner Cloverleaf** (VCBCL, Highway 16 / Highway 21), **Sherwood Park Cloverleaf** (VCSWP, Sherwood Park Freeway / Henday). **Shopping Mall** (VCSHP) is West Edmonton Mall, already on the T131 box. **City Limits** (VCCTY) sits between the west Henday interchanges and is not its own bridge. Cement Plant, Big Lake, and the other town checkpoints are not bridges.

The helicopter chart itself names routes rather than interchanges. All of them are 3,000 ft ASL. The northwest route follows Yellowhead Trail, so the exchanges along that trail are the fixes. The south route passes Molson's, Hawrelak Park, and the University Hospital, which is the downtown valley and the Groat stack. The west route is 111 Avenue and has no freeway bridge. A dotted northeast route leaves the top of the sheet.

Other factors, applied on the line rather than as a third number:

- **Hole in the scene.** High Level without Menzies, one Low Level span without the other, an LRT bridge without the road bridge it stands beside.
- **Already open, versus still rising.** T131–T135 are under construction in 2026. Model the finished bridge. Do not invent a half-built stage. An open bridge of the same score comes first.
- **One model, many placements.** A truss, an arch, and a guideway are each custom. Diamonds and ordinary freeway girders share one overpass model. Do not sculpt them one by one.
- **Stock scenery.** Before building tier 1, look at what the sim already draws. A wrong High Level outranks a missing diamond. A generic deck already in the sim is not a reason to skip a tier 1 bridge.
- **Not a bridge.** At-grade stations, the 23 Avenue underpass, and unfunded alignments are listed so they are not lost. They are not bridge tasks.
- **CYXD footprint.** Do not place anything whose centre falls inside the polygon named `CYXD Airport Area` in `airport-cyxd/PackageSources/Scenery/airport-cyxd/CYXD.xml`. That polygon is the airport package's ground, from about 53.563 to 53.582 and -113.530 to -113.505. Two stations are inside it: NAIT / Blatchford Market and Blatchford Gate. No bridge centre is. The airport package owns that ground.

## 1. Downtown valley

One scene. Runway 34 looks straight down this valley. Runway 30 looks up the east side of it. Do the whole tier before anything in tier 2.

- [x] **R10 High Level** and **R9 Dudley B. Menzies**, one task. 53.531, -113.511 and 53.531, -113.512. Look 5, Where 5. Steel truss, about 777 m, deck about 46 m above the river, streetcar on the upper deck. Menzies is the Capital Line deck hard against it. The mapped elevated run is longer than the river span: about 685 m per track, from the downtown portal at 53.5327, -113.5108 to the University tunnel at 53.5273, -113.5156. Both sit about 0.2 km off the runway 34 centerline, 3.9 km south of the threshold. Custom. The truss is lit at night. Leaving either one out is a hole.

- [x] **R11 Walterdale**. 53.529, -113.502. Look 5, Where 5. Tied arch, two 56 m arches, no piers in the river. About 0.8 km east of the runway 34 centerline, 4.1 km out. Custom. This is the 2017 structure. The 1913 truss was demolished in 2017; do not model it.

- [x] **R14 Tawatinâ**, including the elevated guideway south of the river. 53.5401, -113.4772. Look 5, Where 5. Extradosed concrete box, pylons 24–30 m above the deck, pedestrian deck hung underneath. About 0.4 km off the runway 30 centerline, 4.0 km out. The mapped bridge ways continue south to about 53.5374, over 98 Avenue and down to the Muttart ramp (about 470 m per track from 53.5416). That south run is part of this box, not a second bridge. Custom. The Muttart stop, P152 (53.53621, -113.48000), is the platform slab and low canopy at the bottom of this ramp. Build it with the bridge, and build B254, the Muttart Conservatory, with the stop. The pyramids and the support greenhouses are B254. They are the landmark in this picture. The briefs are in `reference/P152-muttart/` and `reference/P152-muttart/B254-conservatory/`. On the south bank between this bridge and the Low Level, the Edmonton Queen is docked at Rafter's Landing. The code is V257. The brief is in `reference/V257-river-queen/`.

- [x] **R15 Dawson**. 53.549, -113.467. Look 5, Where 4. Truss. About 0.8 km off the runway 30 centerline, 3.7 km out. Custom. Not the same truss as the High Level; do not reuse that model.

- [x] **R13 Low Level** and **R12 James MacDonald**, one task. 53.538, -113.487 and 53.536, -113.488. Look 4 and 3, Where 4. Two Low Level spans side by side (1900 and 1948) plus the 1971 girder. About 1.0–1.2 km off the runway 30 centerline. Do all three decks. One span alone reads as a mistake. With the north end, include the Grierson Hill Bridge (also the Grierson/McDougall Overpass), Grierson Hill Road over McDougall Hill Road, centre 53.538564, -113.488789. It is not a Low Level deck. The code is N258. The brief is in `reference/N258-grierson/`. On the same north bank, include the 100 Street funicular, with the Frederick G. Todd Lookout and the pedestrian bridge over Grierson Hill Road. The mapped footbridge centre is 53.539305, -113.487472. The code is F256. The brief is in `reference/F256-funicular/`. Above that funicular, include B255, the Fairmont Hotel Macdonald. The published spelling is Macdonald. Outline centre 53.540305, -113.489500. The brief is in `reference/B255-hotel-macdonald/`. Include the Rossdale Road Bridge over McDougall Hill Road, also called the Rossdale/McDougall Overpass. The 2013 news name is Rossdale Road Bridge over MacDougall Drive. Way 37120045, centre 53.537724, -113.493132. The code is N259. The brief is in `reference/N259-rossdale-mcdougall/`. On the south bank, the roadworks are N260. Omit the Scona Road Bridge (B065), Scona Road over Connors Road, centre 53.533941, -113.483610. It sits on the wooded slope. Model the 98 Avenue spans at the valley floor with this south end. Eastbound is City bridge B126. The brief is in `reference/N260-scona-connors/`. On the south bank between this bridge and the Tawatinâ, include the Edmonton Queen docked at Rafter's Landing, mapped pier centre 53.5395342, -113.4818826. The code is V257. The brief is in `reference/V257-river-queen/`.

## 2. Landmarks on a VFR line

The first four boxes are named fixes on the Edmonton VFR terminal chart. Then the open landmarks, then the two structures still rising. Each is custom, except where the line says the loops can share a cloverleaf model.

- [x] **R20 Beverly**, **R21 Clover Bar**, and **R22 Clover Bar Railway**, one task. 53.571, -113.373 / 53.572, -113.372 / 53.573, -113.372. Look 4, Where 5. This crossing is the VFR checkpoint **Bridges** (VCBRG, N53° 34.30′ W113° 22.30′). Three decks. Do all three. It is not on a runway centerline.

- [ ] **R6 Quesnell**. 53.507, -113.567. Look 4, Where 5. The VFR checkpoint **Quesnell Bridge** (VCQSN, N53° 30.25′ W113° 34.00′). Whitemud Drive, eight lanes. About 3.4 km off the runway 34 long final at 6.6 km. Wide deck, not a truss. With it, place **W85 Fox Drive (Campbell Bridge)**, 53.5032, -113.5610, the creek span beside it. W85 was left off the freeway list.

- [ ] **Y79 Bremner Cloverleaf**. 53.5702, -113.2461. Look 3, Where 5. Highway 16 / Highway 21. The VFR checkpoint **Bremner Cloverleaf** (VCBCL, N53° 34.30′ W113° 14.70′). It was on the cross list. The loops are the landmark, so this is not a diamond speck. Model the cloverleaf.

- [ ] **H52 Sherwood Park Cloverleaf**. 53.513, -113.344. Look 3, Where 5. Sherwood Park Freeway / Henday. The VFR checkpoint **Sherwood Park Cloverleaf** (VCSWP, N53° 31.00′ W113° 20.50′). The freeway's own bridges through the interchange. Model the interchange, not a single girder.

- [ ] **H39 Henday / Yellowhead west**. 53.574, -113.662. Look 4, Where 4. System interchange, ten bridge ways. The northwest helicopter route follows Yellowhead Trail at 3,000 ft ASL and meets the ring here. A CZVL arrival comes down the same side. **City Limits** (VCCTY, N53° 33.00′ W113° 39.00′) sits between this interchange and **H38 Henday / Stony Plain Road** (53.540, -113.659); place H38 in this box. Flyovers are the part that reads. Ramps can be the shared girder.

- [ ] **H27 Henday / Calgary Trail / Gateway Boulevard** and **H28 Blackmud Creek arches**, one task. 53.437, -113.491 and 53.437, -113.496. Look 5, Where 4. Three-level interchange, trellis beams at a high skew, twelve bridge ways. The arches are three cast-in-place open-spandrel spans immediately west of it (two Henday carriageways and a ramp), deck about 17 m above the creek, opened 2005. This is the landmark on a north departure from CYEG. The arches without the interchange, or the interchange without the arches, leaves a hole.

- [ ] **T127 Davies Elevated Guideway** and **Davies station**, one task. Centre 53.5003, -113.4486. Station 53.49988, -113.44415. Look 5, Where 3. About 1.49 km per track, from 53.5049, -113.4549 to 53.4956, -113.4423. It clears Argyll Road, the CP and CN tracks, and 75 Street. The 2019 count was 38 spans. Piers through the station are circular; elsewhere the top of the pier is a split shaft. Station is three storeys on the deck, centre platform, curved roof, 1,300-stall park and ride. About 2 km off the runway 30 extended centerline at 8 km, so it is in the side window of a long final and it is large enough to read. First LRT model. Full pier and girder limits are in `lrt.md`.

- [ ] **H30 Whitemud Creek arch**. Estimated centre 53.448, -113.560 (`draw-map.py`; OpenStreetMap gave this mainline no bridge centre). Look 5, Where 3. Semi-circular arch on the southwest Henday, between 111 Street and Rabbit Hill Road, over a ravine about 300 m wide and 18 m deep. Survey the centre before placing. Custom. Do not use the Blackmud arch model unchanged; confirm the span count against a photo first.

- [ ] **H50 Henday / Yellowhead east**. 53.568, -113.345. Look 4, Where 4. Hybrid interchange: braided ramps, a railway through the middle, third-level flyovers. It sits on Yellowhead between the Bridges checkpoint and Bremner Cloverleaf, and it is the junction for a CFB6 or CYED arrival that has come down Manning Drive. Custom flyovers; the ramps can be the shared girder.

- [ ] **T135 Anthony Henday LRT bridge, Heritage Valley**. 53.4354, -113.5237. Look 5, Where 3. Under construction. Two steel network arches on a 49° skew, plus two concrete-girder approach spans, one rectangular median pier. Piling was underway in March 2026 and arch steel was arriving in June 2026. Model the finished arches. This is the bridge a south departure toward CYEG will see. Place it with H27/H28, not as a separate art style. Clearance and pier rules are in `lrt.md`.

- [ ] **T131 87 Avenue elevated guideway**, with the **West Edmonton Mall** and **Misericordia** stations. Guideway 53.5205, -113.618. Stations 53.5206, -113.624 and 53.5197, -113.613. Look 5, Where 5. Under construction through 2028. Nearly 2 km on 46 Y-shaped piers, between 178 Street and 165 Street. The mall is the VFR checkpoint **Shopping Mall** (VCSHP, N53° 31.50′ W113° 37.00′), and the guideway is on it, about 1.4 km off the runway 04 long final at 8 km. Model the finished guideway and the two elevated stations. Do this after the open landmarks above. With it, place **T132** (53.5224, -113.6584, the LRT span on the south side of the existing 87 Avenue bridge) and **H37 Henday / 87 Avenue** (53.5228, -113.6592). H37 was left off as a partial cloverleaf. T132 stands beside that road bridge, so the road bridge is part of this box.

## 3. Yellowhead exchanges on the published routes

The northwest helicopter route is Yellowhead Trail at 3,000 ft ASL, about 800 ft above the field. The VFR chart then carries the same highway east through **Bridges** to **Bremner Cloverleaf**, and west to the Henday. At that height these are not specks. One interchange model, in this order, before the ordinary decks in the next section. Centres marked estimated come from the street grid in `draw-map.py` and were not in the written freeway tables. Survey those before placing. None of these centres fall inside the CYXD airport polygon.

West from the field, the helicopter route, until H39:

- [ ] **Y69 Yellowhead / St. Albert Trail**. Estimated 53.578, -113.548. About 2.3 km west of the runway 16 centerline.
- [ ] **Y68 Yellowhead / 156 Street**. Estimated 53.578, -113.596.
- [ ] **Y67 Yellowhead / 170 Street**. 53.573, -113.615. Surveyed.
- [ ] **Y66 Yellowhead / 178 Street**. 53.572, -113.631. Surveyed. Was on the include list.
- [ ] **Y65 Yellowhead / 184 Street**. 53.573, -113.639. Surveyed.

East from the field, toward Bridges and then on to Bremner. H50 and Y79 are already in tier 2.

- [ ] **Y70 Yellowhead / 97 Street**. Estimated 53.578, -113.489. About 1.6 km east of the runway 16 centerline. Not H45, which is 97 Street at the north Henday.
- [ ] **Y71 Yellowhead / 82 Street**. Estimated 53.578, -113.462.
- [ ] **Y72 Yellowhead / Wayne Gretzky Drive**. Estimated 53.578, -113.450. C123 Grant Moellmann, just south, is in the Capilano box. This is the interchange.
- [ ] **Y73 Yellowhead / 50 Street**. Estimated 53.576, -113.405.
- [ ] **Y74 Yellowhead / Victoria Trail**. Estimated 53.574, -113.388.
- [ ] **Y75 Yellowhead / 17 Street**. 53.5700, -113.3631. Just east of the Bridges checkpoint.
- [ ] **Y76 Yellowhead at Broadmoor Boulevard / Sherwood Drive**. 53.570, -113.333. Just east of H50.
- [ ] **Y77 Yellowhead / Sherwood Drive**. 53.5703, -113.2954. Not Y76.
- [ ] **Y78 Yellowhead / Clover Bar Road**. 53.570, -113.271. Two lanes each way, between H50 and Bremner.

## 4. Completes a scene, or an ordinary deck on a final

Shared girders are fine here, except where the line says custom. Several of these were plotted as crosses. They outrank the remaining diamonds because they sit on a CYXD final or they finish a tier 2 scene.

- [ ] **R8 Groat** and the ravine decks north and south of it, one task. Groat Bridge 53.537, -113.539 (Look 3, Where 4, about 1.7 km off the runway 34 centerline). The daytime south helicopter route passes Hawrelak Park and the University Hospital, so this stack is on that route. On the runway 04 short final, 1.2–2.0 km off the centerline at 2.5–3 km: **G116 Hawrelak access** (53.5322, -113.5383), **G117 102 Avenue** (53.5430, -113.5403), **Z125 Wellington** (53.5431, -113.5481), **T133 Stony Plain Road** (53.5478, -113.5458), **G119 107 Avenue** (53.5510, -113.5498). G117, Z125, G118, G119, and G116 were left off the freeway list. **G118 is the old Stony Plain Road span, demolished in 2023. Do not model it.** T133 is the replacement: a single span of at least 46 m, no piers, road and Valley Line together, still under construction. Model the finished T133. The river-span brief is in `reference/R8-groat/`. The ravine briefs are in `reference/G116-hawrelak/`, `reference/G117-102-avenue/`, `reference/Z125-wellington/`, `reference/T133-stony-plain/`, and `reference/G119-107-avenue/`.

- [ ] **R16 Capilano** and the decks on the same road. Capilano 53.556, -113.439 (Look 3, Where 3, about 2.6 km off the runway 30 centerline). Pulled up from the cross list: **C120 106 Avenue** (53.5493, -113.4387, the south approach), **C121 Ada Boulevard** (53.5602, -113.4427), **C122 112 Avenue** (53.5629, -113.4465), **C123 Grant Moellmann** (53.5754, -113.4530). Moellmann is the long span over the rail yard just south of the Yellowhead, about 2.3 km off the runway 22 final at 3.3 km. Give Moellmann its own length. The others can be the shared girder.

- [ ] **H47 Manning / Henday**. 53.631, -113.381. Look 3, Where 4. East departure from CYED and the inbound line from CFB6. More Henday bridges continue at 53.625, -113.372 and 53.624, -113.369; those decks are part of this interchange, not extra landmarks.

- [ ] **H54 Highway 14 / Henday**. 53.449, -113.336. Look 3, Where 4. Layer 2 flyover. The ring crossing on the way in from Cooking Lake.

- [ ] **H53 Henday / Whitemud east**. 53.4829, -113.3427. Look 3, Where 3. The CEZ3 section of `freeway-bridges.md` includes this interchange and the layer 2 Whitemud flyover at 53.482, -113.364. The cross list also plots H53. Treat the flyover as in scope. **W91 Whitemud / 17 Street** (53.482, -113.364) is the flyover just west of it; place W91 in this box. W91 is not the south-ring Henday crossing at 17 Street (that one is H55, still in tier 6).

- [ ] **R2 Constable Travis Jordan** and **R3 Constable Brett Ryan**, one task. Both centres 53.460, -113.615. Look 3, Where 3. Southwest Henday twin over the river. Eastbound and westbound are separate spans. Do both.

- [ ] **R23 Henday northeast river**. 53.608, -113.354. Look 3, Where 3. Two spans, seven lanes, on the ring between CYED and the Yellowhead. No separate memorial name. Do both spans.

- [ ] **H36 Henday / Whitemud west**. 53.512, -113.659. Look 3, Where 3. West-side system interchange. A single ramp bridge at 53.519, -113.657 is the braid up to 87 Avenue; it belongs in this box. H37, the 87 Avenue crossing just north, is already in the T131 box.

- [ ] **W88 Whitemud / Calgary Trail**. 53.4804, -113.4938. Look 3, Where 3. Left off the freeway list. This is Whitemud's own Calgary Trail interchange, not H27. About 1.4 km off the runway 34 long final at 9.5 km. Place it as an interchange, not as a diamond speck.

- [ ] **S104 Sherwood Park Freeway at 82 Avenue and Argyll Road**. 53.5180, -113.4735. Look 3, Where 3. Left off. OpenStreetMap calls the viaduct Mill Creek Bridge. About 1.9 km off the runway 30 final at 6 km. This is not the wooden Mill Creek trestle (Z124, last section).

- [ ] **W87 Rainbow Valley**. 53.483, -113.555. Look 3, Where 3. Whitemud over Rainbow Valley Road and Whitemud Creek, between the west Henday interchange and Quesnell. Place it in the same Whitemud Creek pass as R6 and W85.

- [ ] **Q96 QE2 / Airport Road**. 53.309, -113.549. Look 2, Where 5. The airport access bridge east of the CYEG terminal. A shared girder. It is on this tier because a flight to CYEG cannot miss it, not because the deck is interesting.

- [ ] **H45 Henday / 97 Street**. 53.647, -113.491. Look 2, Where 4. Partial cloverleaf, exit 39, about 1.3 km off the runway 16 long final at 7.7 km. The line from CYXD up to Namao. Shared girder.

## 5. Included corridors, shared girder

One overpass model, placed in this order. None of these is a landmark. They are already on an include list, on a line between the fields, and they should exist before any later diamond. The Yellowhead exchanges are in section 3, not here.

- [ ] **T129 Capital Line over Whitemud**. 53.4828, -113.5165. Look 2, Where 3. Mapped deck about 83 m. About 50 m off the runway 34 extended centerline at 9 km. It reads as the freeway crossing, not as a landmark. Place it with the south Whitemud work.
- [ ] **T130 Capital Line over 118 Avenue**. 53.5704, -113.4586. Look 2, Where 3. Mapped deck about 62 m, beside Coliseum, about 2.6 km off runway 22 at 2.7 km. East of the field.
- [ ] **T128 Whitemud Drive LRT bridge** and **W89 Whitemud / 66 Street**, one task. T128 is 53.4852, -113.4422, mapped deck about 67 m, one median pier. W89 is 53.4852, -113.4427, the road bridge it stands beside. W89 was left off the freeway list. Do not place the LRT span in empty air.
- [ ] **T134 Blackmud Creek LRT bridge**. 53.4409, -113.5185. Look 2, Where 3. Under construction. West of the 111 Street road bridges, profile within 300 mm of them. Those road bridges are not in the inventory. Place the LRT span. If the sim has no creek crossing here, survey the road bridges before adding them; do not invent the span count.
- [ ] **H29 Henday at 111 Street**. 53.435, -113.514. Three lanes each way, west of the Blackmud arches.
- [ ] **H33 Henday / Wedgewood Creek**. 53.471, -113.647. Two three-lane Henday bridges, no cross road, about 2 km west of R2/R3.
- [ ] **H41 Henday / 137 Avenue**. 53.600, -113.632 and 53.602, -113.628. First ring bridges on a southeast line from CZVL.
- [ ] **H43 North Henday / Campbell Road**. 53.633, -113.566. Two lanes each way. A CZVL to CYED flight along the ring.
- [ ] **S106 Sherwood Park Freeway / 34 Street and 67 Street**. 53.517, -113.386 and 53.516, -113.431. Two decks, one box.
- [ ] **Q94 QE2 / 50 Avenue and Black Gold Drive**. Map centre 53.261, -113.563. North deck crosses 50 Avenue at 53.265, -113.564. South deck crosses Black Gold Drive at 53.258, -113.562. **Q95 and Q93 are these two decks. Do not model them again from the cross list.**
- [ ] **Q98 QE2 / Leduc rail line**. 53.380, -113.520. The freeway bridge between CYEG and the ring. No cross road.

Footbridges. Thin decks. Do them after the road spans in the same valley, not before.

- [ ] **R7 Hawrelak / Buena Vista footbridge**. 53.523, -113.547. Look 2, Where 3. Central valley, west of the High Level, in the runway 34 picture only as a line on the water.
- [ ] **R4 Terwillegar Park footbridge**. 53.481, -113.598. Look 3, Where 2. Southwest valley.
- [ ] **R5 Fort Edmonton footbridge**. 53.495, -113.590. Look 3, Where 2. Southwest valley, by Fort Edmonton.
- [ ] **R17 Capilano footbridge**. 53.563, -113.419. Look 2, Where 2.
- [ ] **R18 Ainsworth Dyer footbridge**. 53.554, -113.398. Look 2, Where 2.
- [ ] **R19 Rundle Park footbridge**. 53.563, -113.379. Look 2, Where 2.
- [ ] **R25 Highway 15, Fort Saskatchewan**. 53.706, -113.235. Look 2, Where 2. The 1957 span and the 2022 twin, on Manning Drive toward CFB6. Do both spans. Not M112, which is the 99 Avenue overpass in town.
- [ ] **R24 Beaver Hills footbridge**. 53.628, -113.322. Look 2, Where 1. East of the Henday, opened August 2025.
- [ ] **R1 Devon Bridge**. 53.370, -113.752. Look 2, Where 1. Highway 60 twin, upstream of the city.
- [ ] **R26 CN bridge west of Scotford**. 53.761, -113.171. Look 2, Where 1. Year not in the crossing list.

## 6. Every other excluded bridge

Look 1. Where 2 if the road is still a line between the six fields or just beyond a field. Where 1 if it is only there for a flight that keeps going. One shared overpass, after section 5. Do not reopen the inventory and do not promote one of these on silhouette. The Yellowhead exchanges are not in this section: they are on the helicopter route and the VFR chart, and they are in section 3. Centres are the plotted deck centres.

A few names in the cross tables already have a box above. They are repeated here so a later session does not model them twice. These lines are not boxes.

- H37 Henday / 87 Avenue — with T131
- H53 Henday / Whitemud east — section 4
- W85 Fox Drive, Campbell Bridge — with R6
- W88 Whitemud / Calgary Trail — section 4
- W89 Whitemud / 66 Street — with T128
- W91 Whitemud / 17 Street — with H53
- S104 SPF / 82 Avenue and Argyll — section 4
- G116, G117, Z125, G119, C120, C121, C122, C123 — with R8 or R16
- G118 Stony Plain Road at Groat — demolished, replaced by T133
- Q93 and Q95 — the two decks of Q94
- Y65, Y66, Y67, Y68, Y69, Y70, Y71, Y72, Y73, Y74, Y75, Y76, Y77, Y78 — section 3
- Y79 Bremner Cloverleaf — section 2
- H38 Henday / Stony Plain Road — with H39
- H39 Henday / Yellowhead west — section 2
- H52 Sherwood Park Cloverleaf — section 2
- R20, R21, R22 — section 2, the Bridges checkpoint

### Henday diamonds, Where 2

- [ ] **H31 Terwillegar Drive**. 53.4442, -113.6002. Exit 8. The rest of Terwillegar Drive is still traffic lights.
- [ ] **H32 184 Street**. 53.4666, -113.6311. Signed Cameron Heights Drive / Maskêkosihk Trail.
- [ ] **H34 Lessard Road**. 53.4800, -113.6584.
- [ ] **H35 Callingwood Road / 62 Avenue**. 53.4943, -113.6591.
- [ ] **H40 Ray Gibbon Drive**. 53.5914, -113.6462. Toward St. Albert, before H41.
- [ ] **H42 St. Albert Trail**. 53.6169, -113.6004. Highway 2.
- [ ] **H44 127 Street**. 53.6390, -113.5453.
- [ ] **H46 66 Street**. 53.6465, -113.4390. Exit 43, between H45 and Manning Drive.
- [ ] **H48 153 Avenue**. 53.6173, -113.3593.
- [ ] **H49 130 Avenue**. 53.5873, -113.3453. Signed Aurum Road.
- [ ] **H51 Baseline Road / 101 Avenue**. 53.5404, -113.3426.
- [ ] **H55 17 Street**. 53.4385, -113.3691. South ring. Not W91 and not S107.
- [ ] **H56 50 Street**. 53.4356, -113.4180. South ring. Not W90 and not S105.
- [ ] **H57 91 Street**. 53.4375, -113.4668. Just east of H27.

Not plotted, so there is nothing to place: Rabbit Hill Road (Henday exit 6; the deck was not in the map boxes), 135 Street (right-in/right-out), and the old right-in/right-out connections at 119 Street, 127 Street on the southwest, and 109/111 Avenue.

### Whitemud, Where 2

- [ ] **W81 178 Street**. 53.5121, -113.6300.
- [ ] **W82 170 Street**. 53.5122, -113.6153.
- [ ] **W83 159 Street**. 53.5119, -113.5967.
- [ ] **W84 156 Street**. 53.5121, -113.5904.
- [ ] **W86 53 Avenue**. 53.4904, -113.5720. South of Quesnell.
- [ ] **W90 50 Street**. 53.4873, -113.4182.

### QE2 between the airport and the ring, and just south of CYEG, Where 2

- [ ] **Q97 Highway 19**. 53.3379, -113.5489. Highway 19 is the bridge. Highway 628 is the same interchange east of the QE2. Not Q96.
- [ ] **Q99 41 Avenue SW**. 53.3963, -113.5122. North of Q98.
- [ ] **Q100 Ellerslie Road**. 53.4248, -113.4931. A second Ellerslie bridge just west is the creek, not the highway. Do not add that creek span from this line.
- [ ] **Q101 23 Avenue**. 53.4535, -113.4922.

### Sherwood Park Freeway and the Yellowhead just east of the river, Where 2

- [ ] **S105 50 Street**. 53.5143, -113.4185.
- [ ] **S107 17 Street**. 53.5172, -113.3691. Not H55 and not W91.
- [ ] **Z126 50 Street rail overpass**. 53.5181, -113.4184. The tagged 50 Street bridge just north of the freeway. Not a second rail deck.
- [ ] **L113 Highway 14 / Highway 21**. 53.4468, -113.2461. Highway 21 is the bridge.
- [ ] **M112 Highway 15 / 99 Avenue**. 53.7022, -113.2270. Fort Saskatchewan. Not R25.
- [ ] **D114 Highway 28 / 195 Avenue**. 53.6579, -113.4986. 195 Avenue over Highway 28 on 97 Street, south of CYED.

### Only if the flight keeps going, Where 1

Highway 16 and 16A west of the Henday, then the crossings past Namao, Leduc, and Gibbons.

- [ ] **Y64 Highway 16 / Winterburn Road**. 53.5703, -113.6891.
- [ ] **A111 Highway 16A / Winterburn Road**. 53.5412, -113.6887.
- [ ] **Y63 Highway 16 / Highway 60**. 53.5699, -113.7633.
- [ ] **A110 Highway 16A / Highway 60**. 53.5413, -113.7626.
- [ ] **Y62 Highway 16 / Highway 44**. 53.5703, -113.8091. Highway 44 is the bridge.
- [ ] **A109 Highway 16A rail crossing**. 53.5434, -113.8347. On the Edson Subdivision.
- [ ] **Y61 Highway 16 / Century Road**. 53.5698, -113.8854.
- [ ] **Y60 Highway 16 / Jennifer Heil Way**. 53.5696, -113.9338. Campsite Road is the same interchange.
- [ ] **Y59 Highway 16 / Highway 779**. 53.5696, -114.0003. Signed 779, not 775.
- [ ] **A108 Highway 16A / Highway 779**. 53.5413, -114.0019. 48 Street.
- [ ] **Y58 Highway 16 / Highway 43**. 53.5702, -114.2214. West of Stony Plain.
- [ ] **Q102 Highway 2 / Highway 37**. 53.7159, -113.5533. Highway 37 is the bridge. A second Highway 37 bridge further west is not this crossing.
- [ ] **Q103 Highway 2 / Highway 642**. 53.8018, -113.6612. West of Morinville. Highway 2 is the bridge, over 100 Avenue.
- [ ] **Q92 Highway 2 / Township Road 490**. 53.1922, -113.5982. South of Leduc.
- [ ] **D115 Highway 28 / Highway 28A**. 53.8443, -113.3220. North of Gibbons. Northbound flyover at the trumpet. The southbound loop is the other bridge a few metres away; do both if this box is ever opened.
- [ ] **Y80 Highway 16 / Highway 824**. 53.5700, -113.1479. Range Road 222, east of CFB6.

There is no separate Highway 16 / 16A interchange to add. The east end of 16A is H38, already with H39. The west end is Y58.

## 7. Stations

Not bridge models. A canopy is a later pass. Elevated stations are already inside a bridge box above; the line here is so they are not also built as a freestanding station.

The order is how close the platform sits to a CYXD final. Kingsway and NAIT are on the airport side of the downtown picture. They still wait, because a platform does not rank with a truss.

### On a guideway already in this list

- [ ] **P157 Davies** — with T127. Do not open a second task.
- [ ] **P163 West Edmonton Mall** and **P164 Misericordia** — with T131.

### Open, at grade, near CYXD

NAIT / Blatchford Market (P147) and Blatchford Gate (P148) are inside the CYXD airport polygon. They are in the do-not-model section.

- [ ] **P146 Kingsway / Royal Alex**. 53.55803, -113.50147. About 0.2 km off the runway 30 centerline, 1.4 km south of the threshold. South of the airport polygon.
- [ ] **P139 Coliseum**. 53.57068, -113.45838. On T130.
- [ ] **P140 Stadium**. 53.55995, -113.47071.

### Open, at grade, on the runway 30 side of downtown

These are the street stops a runway 30 arrival flies past. P152 is the platform at the bottom of the R14 ramp, and B254 sits with that stop. Build both with the bridge. The briefs are in `reference/P152-muttart/` and `reference/P152-muttart/B254-conservatory/`.

- [ ] **P149 102 Street**. 53.54317, -113.49524.
- [ ] **P150 Churchill**. 53.54377, -113.48904. Valley Line stop is at street level. Capital and Metro platforms are underground. One surface stop.
- [ ] **P151 Quarters**. 53.54440, -113.48405.
- [ ] **P152 Muttart**. 53.53621, -113.48000. At grade, at the bottom of the south ramp off R14. Side platforms and a low canopy, plus B254 beside the stop. Build both with the R14 box. Briefs: `reference/P152-muttart/` and `reference/P152-muttart/B254-conservatory/`.

### Open, at grade, the rest

- [ ] **P137 Clareview**. 53.60177, -113.41142. The yard west of the Kathleen Andrews Transit Garage is the only thing here that reads from the air, and it is track, not a station building.
- [ ] **P138 Belvedere**. 53.58805, -113.43348.
- [ ] **P141 Health Sciences / Jubilee**. 53.52006, -113.52589.
- [ ] **P142 McKernan / Belgravia**. 53.51308, -113.52619.
- [ ] **P143 South Campus / Fort Edmonton Park**. 53.50287, -113.52842.
- [ ] **P144 Southgate**. 53.48576, -113.51678. Just north of T129.
- [ ] **P145 Century Park**. 53.45731, -113.51637.
- [ ] **P153 Strathearn**. 53.53171, -113.46231.
- [ ] **P154 Holyrood**. 53.52751, -113.45740.
- [ ] **P155 Bonnie Doon**. 53.51981, -113.45538.
- [ ] **P156 Avonmore**. 53.51046, -113.45508. North of T127.
- [ ] **P158 Millbourne / Woodvale**. 53.47469, -113.43896. South of T128.
- [ ] **P159 Grey Nuns**. 53.46243, -113.43451.
- [ ] **P160 Mill Woods**. 53.45839, -113.43097.

Underground, and not a scenery object: Central, Bay/Enterprise Square, Corona, Government Centre, University, and MacEwan. Churchill's Capital and Metro platforms are in that set.

### Under construction, at grade

Valley Line West and Capital Line South phase 1. No platform until the guideways in tier 2 exist. Centres are estimated on the mapped centreline.

- [ ] **P161 Lewis Farms**. 53.5228, -113.6679. West of T132.
- [ ] **P162 Aldergrove / Belmead**. 53.5213, -113.648.
- [ ] **P165 Meadowlark**. 53.5198, -113.5965.
- [ ] **P166 Glenwood / Sherwood**. 53.528, -113.591.
- [ ] **P167 Jasper Place**. 53.5412, -113.5902.
- [ ] **P168 Stony Plain Road / 149 Street**. 53.5413, -113.5799.
- [ ] **P169 Grovenor / 142 Street**. 53.5432, -113.5641.
- [ ] **P170 Glenora**. 53.5468, -113.5495.
- [ ] **P171 124 Street**. 53.5463, -113.5311.
- [ ] **P172 Brewery / 120 Street**. 53.5462, -113.523.
- [ ] **P173 The Yards / 116 Street**. 53.5462, -113.514.
- [ ] **P174 MacEwan Arts / 112 Street**. 53.5462, -113.5064.
- [ ] **P175 NorQuest**. 53.5430, -113.4991.
- [ ] **P176 Alex Decoteau**. 53.5431, -113.497.
- [ ] **P177 Twin Brooks**. 53.4468, -113.5167.
- [ ] **P178 Heritage Valley North**. 53.42512, -113.54559. End of Capital Line South phase 1.
- [ ] **Llew Lawrence maintenance facility**. South of T135. Yard, not a station. Leave it until T135 exists.

## 8. Do not model

These were scored and rejected. They are not boxes. A later session should not pull one back up without a new fact (funding, a built span, or a photo that shows the trestle reading from the air).

- **P147 NAIT / Blatchford Market** (53.56695, -113.50909) and **P148 Blatchford Gate** (53.57695, -113.51041). Both centres fall inside the `CYXD Airport Area` polygon. Placing them would sit on the airport package. The airport package owns that ground, including a canopy.
- **T136 Walker Bridge**. Estimated 53.586, -113.515. Design only, unfunded in 2026. The centre is north of the airport polygon, so the footprint rule is not what keeps it off. If it is funded it jumps to section 2: it would sit about 0.2 km off the runway 16 centerline, 1 km north, over the Yellowhead and the CN Walker Yard. Until then there is no span, pier count, or clearance to build.
- **G118**, the old Stony Plain Road bridge. Demolished 2023. T133 replaces it.
- The **1913 Walterdale truss**. Demolished 2017. R11 replaces it.
- **23 Avenue** on Capital Line South. An underpass, not a viaduct.
- **Kâhasinîskâk Bridge**. Pedestrian bridge over Connors Road, built with Valley Line Southeast. Not an LRT deck. No centre in the inventory; do not invent one.
- **Capital Line Northeast** (Clareview to Gorman). No viaduct. Unfunded.
- **Capital Line South phase 2** (Heritage Valley North to Desrochers). The grade separation at Ellerslie Road has not been chosen. No bridge was found.
- **Anything past Desrochers toward CYEG.** A City Plan test reused two stop names. It did not produce a corridor or a structure.
- **Metro Line Northwest** stations (P183 132 Avenue, P184 137 Avenue, P185 145 Avenue, P186 Castle Downs, P187 127 Street, P188 137 Street, P189 Campbell Road). Street level, preliminary design only. The only elevated structure on that line is T136.
- **P182 Gorman**. 53.6218, -113.3704, estimated. Unfunded. No viaduct.
- The proposed way south of Mill Woods in `lrt-tracks.json`. Not one of the four extensions. Not drawn.
- **Z124 Mill Creek trestle**. Plotted at 53.512, -113.470. It is in the ravine. From pattern altitude it sits in the trees. It does not outrank a bridge that reads against the sky or the river. It is not S104. Ravine bridges were left as a separate set; do not grow that set from this file.
- Crossovers, sidings, and yards (Clareview / Kathleen Andrews, Valley Line shops, tunnel storage, Gerry Wright operations facility, Lewis Farms storage) as scenery of their own. The Clareview yard is the one exception worth a look, and only after Clareview's station box is actually open.
