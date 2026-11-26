# Edmonton buildings 100 m and taller (reference for obstruction lighting)

Source: [List of tallest buildings in Edmonton, Wikipedia](https://en.wikipedia.org/wiki/List_of_tallest_buildings_in_Edmonton?useskin=vector), fetched 2026-11-26. The page ranks completed buildings at least 100 m (328 ft) tall "as of 2026", including spires and architectural details, excluding antenna masts. Its lead says "As of 2025, Edmonton has 25 buildings taller than 100 m", so the page's own date is inconsistent.

The fetch was truncated. Only ranks 1 to 3 are checked against the page text. Ranks 4 to 25, their coordinates, and the under-construction and proposed lists came from a summary of the rest of the page and are **unverified**. Check them against the page before relying on them, especially the coordinates and heights used in a `buildings.csv`.

Heights are the page's metres, with feet as given. Nothing was converted. Coordinates are as the page gives them (WGS 84). The page lists neighbourhoods, not street addresses.

## Completed, 100 m and taller

| Rank | Name | Height (m) | Feet | Floors | Year | Area | Lat, Long | Checked |
|---|---|---|---|---|---|---|---|---|
| 1 | Stantec Tower | 248.9 | 817 | 66 | 2019 | Downtown | 53.54500, -113.49611 | page text |
| 2 | JW Marriott Edmonton | 191 | 627 | 56 | 2019 | Downtown | 53.545750, -113.496083 | page text |
| 3 | Epcor Tower | 149.4 | 490 | 28 | 2011 | Downtown | 53.547472, -113.492889 | page text |
| 4 | National Bank Centre (fmr. Manulife Place) | 146.4 | 480 | 36 | 1983 | Downtown | 53.542667, -113.494389 | summary |
| 5 | Encore Tower | 137.7 | 452 | 43 | 2020 | Downtown | 53.54278, -113.49806 | summary |
| 6 | TELUS House (ATB Place) | 134.4 | 441 | 33 | 1971 | Downtown | 53.540083, -113.491417 | summary |
| 7 | 10104 103 Ave (Bell Tower) | 129.9 | 426 | 32 | 1982 | Downtown | 53.544972, -113.494306 | summary |
| 8 | Edmonton Tower | 129.84 | 426.0 | 29 | 2016 | Downtown | 53.545694, -113.494639 | summary |
| 9 | Commerce Place | 124.97 | 410.0 | 30 | 1990 | Downtown | 53.541972, -113.495111 | summary |
| 10 | Edmonton House | 121.1 | 397 | 45 | 1971 | Downtown | 53.538444, -113.495056 | summary |
| 11 | The Pearl | 121 | 397 | 36 | 2014 | Wihkwentowin | 53.540639, -113.528667 | summary |
| 12 | The Parks I | 121 | 397 | 35 | 2025 | Downtown | 53.541528, -113.506306 | summary |
| 13 | Canadian Western Bank Place | 120.6 | 396 | 30 | 1980 | Downtown | 53.540583, -113.498000 | summary |
| 14 | MNP Tower | 117.6 | 386 | 27 | 1978 | Downtown | 53.545167, -113.492917 | summary |
| 15 | TD Tower | 116.7 | 383 | 27 | 1976 | Downtown | 53.543500, -113.493028 | summary |
| 16 | Rice Howard 1 | 113.2 | 371 | 28 | 1982 | Downtown | 53.541583, -113.492611 | summary |
| 17 | Icon II | 112.3 | 368 | 35 | 2010 | Downtown | 53.541832, -113.49984 | summary |
| 18 | CN Tower | 110.9 | 364 | 26 | 1966 | Downtown | 53.546944, -113.491389 | summary |
| 19 | Enbridge Centre | 110.6 | 363 | 25 | 2016 | Downtown | 53.542417, -113.493028 | summary |
| 20 | Ultima | 107.9 | 354 | 32 | 2016 | Downtown | 53.544000, -113.497861 | summary |
| 21 | Citizen on Jasper (CNIB Tower) | 107.9 | 354 | 32 | 2023 | Wihkwentowin | 53.54139, -113.52917 | summary |
| 22 | Sun Life Place | 107.7 | 353 | 25 | 1978 | Downtown | 53.542194, -113.487917 | summary |
| 23 | Fox Two | 107.3 | 352 | 33 | 2017 | Downtown | 53.543306, -113.499750 | summary |
| 24 | Hendrix | 103.6 | 340 | 29 | 2016 | Wihkwentowin | 53.535222, -113.511639 | summary |
| 25 | 102A Tower | 102.9 | 338 | 23 | 1974 | Downtown | 53.544083, -113.492528 | summary |

Conflicts: the summary's "other buildings" table gives Stantec Tower as 250.9 m and JW Marriott as 192.15 m, against the page's 248.9 m and 191 m. The lead gives Stantec as 816 ft, the rank table as 817 ft. The verbatim figures are used here.

## Under construction (summary only)

- Falcon Two: 146 m (479 ft), 30 floors, expected 2027, 53.53861, -113.50139.

## Approved or proposed (summary only, no coordinates, not on the completed list)

Alldritt Tower 280.0 m (80 floors, approved 2017); 9955 Jasper 184 m (58 floors, approved 2018); Massey Harris Ferguson Tower 3 150.0 m (48 floors, approved 2015); The Parks Tower 2 147.0 m (45 floors); Falcon One 140.0 m (30 floors, approved 2018); Massey Harris Ferguson Tower 1 140.0 m (45 floors, approved 2015); Massey Harris Ferguson Tower 2 135.0 m (42 floors, approved 2015); The Shift Tower 1 113.08 m (38 floors, proposed 2018); The Shift Tower 2 106.68 m (35 floors, proposed 2018); The Clancey 103 m (28 floors, approved 2019).

## Use for obstruction lighting

- All 25 completed buildings are at least 102.9 m. Under CARs 601.23(1)(b), a building above 90 m within 6 km of the field is an obstacle. Downtown and Wihkwentowin are both within about 6 km of CYXD (downtown about 3 km), so every building on the completed list meets that test.
- For `tools/obstacle_surfaces.py`, a `buildings.csv` needs the top height in AMSL and the ground elevation. Neither is on this page. Use the summary's coordinates only after checking them.
