# T127 Davies guideway and P157 Davies station: Tier 2 handoff

Built 2026-11-23. `scenery-edmonton-bridges/tools/site_t127.py`. Model `br_t127_davies` (about 18,800 polys, 2 chunks), placed at 53.5003, -113.4486, datum 670.00 m. Package built with the sim closed (exit 0, `_RPTErrors.xml` empty). **Not seen in the sim.**

## Data collected this session

- `elevation/t127-samples.json` (committed): the 2018 bare earth on the mid line of the two tracks and the highest first return within 6 m of it, every metre. Written by `python -I -c "import sys; sys.path.insert(0, 'scenery-edmonton-bridges/tools'); import site_t127; site_t127.sample()"` (needs numpy, Pillow and the gitignored clips, fetched with `fetch-site-data.py T127`).
- `geometry.json` `osm_added_2026_11_23`: the station building (way 735311921: building:levels 4, roof:shape round, layer 2), the LRT platform (1157283680), the bus station area (561325376), and the 13 road and railway ways that cross under the guideway. Read from the OSM API on 2026-11-23.
- `street/`: 4 more Mapillary frames, chosen for the piers. Mapillary has nothing here after 2019. All frames are 2018, before the girders went up. They show the Y piers standing in rows along 75 Street, Wagner Road and the railway. The 2023 Commons photos in `photos/` remain the only views of the finished station.

## What the 2018 LiDAR shows

The flight caught most piers standing without their girders. They are spikes in the first return 6 to 14 m above the bare earth: about 35 to 40 m apart on the line and about 22 m apart through the station. The model uses 30 of them. A spike counts as a pier unless either:

- it stands more than 1.5 m above the median of the spikes within 60 m (cranes); or
- it sits well below a taller spike within 45 m (piers still being built, around 885 to 925 m).

The 2019 aerial shows no piers yet between about 950 and 1,060 m. That gap and both ends are filled at even spacing (spans of 40 m at most), kept 8 m clear of the crossing roads and railways.

The aerial also shows:

- the precast U-trough girders, one per track, with spare girders lying on site;
- the station's steel frame going up on the OSM footprint;
- a pair of girders about 10 m wide overall.

## What is in the model

Stations are metres along the track mid line from the south end (75 Street, 53.4956), 1,491 m in all.

| Part | Where | Notes |
| --- | --- | --- |
| Retained fill, south | 0 to 89 m | Rail rises from 1.0 m above the ground at the OSM bridge end. Panel walls, track bed, upstands as on the girders. |
| U girders on piers | 89 to 461 m, 554 to 1,345 m | One per track: 4.9 m over the webs, 2.2 m deep, webs 1.2 m above the rail. Plinths and rails (1.435 m gauge). |
| Y piers | where the tracks are side by side | Shaft 1.2 x 1.8 m, forking at about half height into two arms, one under each girder. |
| Column piers | where the tracks spread (about 300 to 690 m, the station) | One round column under a cap, two columns where the tracks are more than 12 m apart. |
| Station P157 | 461 to 554 m (OSM building), tracks 13 m apart | See below. |
| Retained fill, north | 1,345 to 1,491 m | Down to 1.0 m above the ground at the OSM bridge end near Argyll Road / 83 Street. |
| Overhead-line masts | every 50 m outside both girders | Cantilever arm over each track. No contact wire. |

Station, on the OSM footprint (93 m x 20.6 m):

- centre platform 0.35 m above the rail, with yellow edge strips and a glazed lift and stair enclosure;
- white panel belly from the pier caps up to the track bed;
- white band to 1.3 m above the rail, then a glazed band leaning out to the eaves at 5 m;
- barrel roof, crest 8.5 m above the rail: white outside, timber soffit, 6 m overhang at both ends, open ends for the trains;
- ground floor of glass rooms and a solid service block, set back under the belly, with columns along the edges.

Levels:

- rail at the station 686.72 m, ground 671.98 m (platform about 15 m up);
- rail 680.1 m at the south end, highest 687.5 m at about 250 m, 679.0 m over Argyll Road.

Clearance under the girders, from the 2018 bare earth:

- 6.4 m over Argyll Road;
- 7.4 m over the CP Strathcona Industrial Lead (238 m);
- 8.6 m over the CN Scotford Subdivision (1,047 m);
- 9 m over 75 Street (338 to 366 m);
- 11 m over Davies Road and Wagner Road.

## Park and ride (added 2026-11-23)

The two ETS park-and-ride lots in OSM: way 1138132749, south-west of the station, 30,100 m2; and way 1138133499, north of it, 12,800 m2. Their 18 parking aisles and the ways that cut into them are in `geometry.json` `osm_added_2026_11_23` `park_and_ride`.

- **Cars.** Done as at CYXD (`airport-cyxd/tools/gen_parking.py`): 135 `<CarParking>` rows the sim fills with its own parked cars, written by `gen_bridges.py` between the `car parks` markers in `edmonton-bridges.xml`. Each row is 5.5 m deep, one per side of each aisle segment, beside a 6.5 m aisle. The rows are cut back from the footways, cycleways, service roads, grass islands and bus platforms. They come to about 1,490 stalls at 2.6 m; Wikipedia gives 1,300. There is no `carsHeading`, which fails the BGL compiler; the sim lines the cars up with each row's long edge.
- **Pavement.** This package has no airport, so it cannot use CYXD's Apron pavement. Instead, the lots are a flat asphalt surface in the model, 0.05 m above a flatten polygon at each lot's level. The levels are the median 2018 bare earth inside each lot: 676.49 m and 674.72 m. The 2018 ground was still a building site, so the true graded level may differ by about 1 m.

Sim checks:
- whether the cars appear (the model's exclusion polygon now covers the lots; if it also removes `CarParking` cars, the rows need cutting out of it);
- whether the cars face square to the aisles;
- whether the edges of the flattened lots step against the roads round them.

## Assumed (flagged in the module docstring)

- Rail top 1.2 m above the LiDAR pier top.
- U girder sizes.
- Track centres at least 5.1 m apart: OSM has 4.3 m, which the aerial's 10 m girder pair cannot fit.
- Y pier and cap sizes. The fork height.
- The two ends: rail 1.0 m above the ground where the OSM bridge ways end, and fill until the rail is 4.5 m up.
- All station heights: ground floor to the caps, the glazed band, the roof crest and overhang.
- The mast spacing.

The Railway Age and City start points (69A Avenue or 83 Street) are not used. The OSM bridge ends are.

No signals, signs, lamps, contact wire, art glass, stair towers, bus canopies or park and ride.

## Sim checks for William

- **The sim's own Davies station.** OSM maps it as a 4-level building on layer 2. The sim may draw its own box or photogrammetry there. The exclusion polygon (the plan footprint plus 4 m) should remove it.
- **The ends.** The fill ends meet the at-grade track, which the sim does not draw, with a blunt end.
- **Station from the air.** The glazed band uses the CYXD dark glass swatch, so it reads darker than in the photos.
- **Long final, runway 30.** The station is meant to be readable from about 2 km to the side.

## Rebuilding

`python -I scenery-edmonton-bridges/tools/gen_bridges.py t127` (numpy, Pillow, shapely). It reads only `geometry.json` and `elevation/t127-samples.json`.
