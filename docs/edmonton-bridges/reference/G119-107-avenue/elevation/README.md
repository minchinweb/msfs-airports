# Elevation (2018 LiDAR, CGVD2013)

Files: `dtm-2018-1m.tif` (bare earth), `dsm-2018-1m.tif` (surface incl. bridges, buildings, trees). EPSG:3979, 1 m, float32 metres, nodata -32767. Source: NRCan HRDEM `AB-Edmonton-1m` (City of Edmonton 2018 LiDAR), Open Government Licence - Canada.

River surface in this clip: **661.86 m** (2,171.5 ft), NOT valid (the clip has too little river; ignore).
Lowest DTM pixel: 653.22 m.

| Part | Samples | DSM p10 | DSM median | DSM p90 | Median above river |
| --- | --- | --- | --- | --- | --- |
| road_deck | 25 | 667.84 | 667.94 | 668.11 | 6.08 (vs a non-river value) |
| sidewalk | 25 | 668.19 | 668.52 | 668.72 | 6.66 (vs a non-river value) |
| road_deck | 25 | 667.87 | 668.00 | 668.09 | 6.14 (vs a non-river value) |
| sidewalk | 25 | 668.11 | 668.34 | 668.66 | 6.48 (vs a non-river value) |
| outline | 73 | 667.32 | 668.14 | 668.64 | 6.28 (vs a non-river value) |
| approach_road | 8 | 667.76 | 667.78 | 667.79 | 5.92 (vs a non-river value) |
| approach_road | 8 | 667.81 | 667.82 | 668.97 | 5.96 (vs a non-river value) |
| under_groat_road | 195 | 661.71 | 662.46 | 667.55 | 0.60 (vs a non-river value) |
| under_groat_road | 195 | 660.86 | 661.96 | 666.57 | 0.10 (vs a non-river value) |
