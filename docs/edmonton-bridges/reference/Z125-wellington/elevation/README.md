# Elevation (2018 LiDAR, CGVD2013)

Files: `dtm-2018-1m.tif` (bare earth), `dsm-2018-1m.tif` (surface incl. bridges, buildings, trees). EPSG:3979, 1 m, float32 metres, nodata -32767. Source: NRCan HRDEM `AB-Edmonton-1m` (City of Edmonton 2018 LiDAR), Open Government Licence - Canada.

River surface in this clip: **637.95 m** (2,093.0 ft), NOT valid (the clip has too little river; ignore).
Lowest DTM pixel: 623.30 m.

| Part | Samples | DSM p10 | DSM median | DSM p90 | Median above river |
| --- | --- | --- | --- | --- | --- |
| road_deck | 24 | 664.31 | 664.35 | 664.39 | 26.40 (vs a non-river value) |
| north_shared_path | 25 | 664.69 | 665.44 | 666.44 | 27.49 (vs a non-river value) |
| south_construction_way | 22 | 665.20 | 665.57 | 672.16 | 27.62 (vs a non-river value) |
| outline | 57 | 663.44 | 665.70 | 670.63 | 27.75 (vs a non-river value) |
| approach | 36 | 664.42 | 664.60 | 665.49 | 26.65 (vs a non-river value) |
