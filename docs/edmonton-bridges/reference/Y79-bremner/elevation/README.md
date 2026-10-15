# Elevation (2018 LiDAR, CGVD2013)

Files: `dtm-2018-1m.tif` (bare earth), `dsm-2018-1m.tif` (surface incl. bridges, buildings, trees). EPSG:3979, 1 m, float32 metres, nodata -32767. Source: NRCan HRDEM `NRCAN-Edmonton_2018-1m` (City of Edmonton 2018 LiDAR), Open Government Licence - Canada. `fetch-site-data.py` first wrote the `AB-Edmonton-1m` window; that cropped city tile is nodata at this interchange. The clips were rewritten from the same 2018 flight's fuller `NRCAN-Edmonton_2018-1m` COGs.

This clip is the Highway 16 / Highway 21 prairie interchange. It does not hold a river reach. Do not use a modal low DTM as water.

Lowest DTM pixel: 663.10 m.
DTM ground at the project centre (53.5702, -113.2461): **669.77 m**.

| Part | Samples | DSM p10 | DSM median | DSM p90 |
| --- | --- | --- | --- | --- |
| east_overpass | 29 | 677.21 | 677.27 | 677.31 |
| west_overpass | 30 | 677.62 | 677.70 | 677.72 |
| north_west_road | 269 | 675.80 | 676.98 | 677.36 |
| north_east_road | 28 | 677.18 | 677.25 | 677.73 |
| south_east_road | 41 | 676.88 | 676.98 | 677.13 |
| south_west_road | 33 | 677.16 | 677.30 | 677.52 |
| northeast_loop | 87 | 670.64 | 673.78 | 677.03 |
| southeast_loop | 131 | 670.10 | 673.27 | 677.18 |

Stubs `north_east_stub` and `south_east_stub` had fewer than six DSM samples and were not tabulated. DSM is first-return; traffic and railings can add up to 1 m. Rise against the centre DTM is not a published clear height. Subtract deck depth if a clearance is stated.
