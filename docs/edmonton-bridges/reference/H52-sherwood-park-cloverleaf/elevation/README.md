# Elevation (2018 LiDAR, CGVD2013)

Files: `dtm-2018-1m.tif` (bare earth), `dsm-2018-1m.tif` (surface incl. bridges, buildings, trees). EPSG:3979, 1 m, float32 metres, nodata -32767. Source: NRCan HRDEM `NRCAN-Edmonton_2018-1m` (City of Edmonton 2018 LiDAR), Open Government Licence - Canada. `fetch-site-data.py` first wrote the `AB-Edmonton-1m` window; that cropped city tile is nodata at this interchange. The clips were rewritten from the same 2018 flight's fuller `NRCAN-Edmonton_2018-1m` COGs.

This clip is the Sherwood Park Freeway / Henday prairie interchange. It does not hold a river reach. Do not use a modal low DTM as water.

Lowest DTM pixel: 689.50 m.
DTM ground at the project centre (53.513, -113.344): **707.76 m**.

| Part | Samples | DSM p10 | DSM median | DSM p90 |
| --- | --- | --- | --- | --- |
| eastbound_overpass | 49 | 717.29 | 717.86 | 717.99 |
| westbound_overpass | 46 | 717.40 | 717.86 | 717.93 |
| en_ramp1_over_henday | 47 | 719.39 | 721.40 | 722.95 |
| en_ramp2_over_freeway | 29 | 724.62 | 724.84 | 724.96 |
| west_eastbound_stub | 7 | 716.74 | 716.91 | 717.09 |
| west_eastbound_road | 211 | 699.20 | 706.43 | 715.30 |
| west_westbound_road | 25 | 716.04 | 716.62 | 717.16 |
| east_westbound_road | 218 | 712.56 | 713.62 | 717.52 |
| east_eastbound_road | 176 | 712.65 | 713.54 | 717.73 |
| south_to_westbound_ramp | 345 | 708.69 | 710.85 | 717.02 |
| southwest_loop | 116 | 708.57 | 711.80 | 715.65 |
| north_to_loop | 57 | 708.31 | 708.43 | 717.35 |

DSM is first-return; traffic and railings can add up to 1 m. Rise against the centre DTM is not a published clear height. Subtract deck depth if a clearance is stated.
