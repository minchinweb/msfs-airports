# Elevation (2018 LiDAR, CGVD2013)

Files: `dtm-2018-1m.tif` (bare earth), `dsm-2018-1m.tif` (surface incl. bridges, buildings, trees). EPSG:3979, 1 m, float32 metres, nodata -32767. Source: NRCan HRDEM `AB-Edmonton-1m` (City of Edmonton 2018 LiDAR), Open Government Licence - Canada.

River surface in this clip: **613.65 m** (2,013.3 ft), NOT valid (the clip has too little river; ignore).
Lowest DTM pixel: 613.60 m.

| Part | Samples | DSM p10 | DSM median | DSM p90 | Median above river |
| --- | --- | --- | --- | --- | --- |
| west_platform | 73 | 621.69 | 621.94 | 622.20 | 8.29 (vs a non-river value) |
| east_platform | 73 | 621.95 | 622.65 | 624.01 | 9.00 (vs a non-river value) |
