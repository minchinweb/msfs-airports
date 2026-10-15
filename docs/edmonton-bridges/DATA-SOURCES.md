# Bridges: aerials, elevation and night references

Written 2026-10-14. What was collected for the 21 reference folders in `reference/`, where it came from, how to refresh it, and what is still missing. Companion files: `RIVER-LEVEL.md` (gauge and water height) and `ELEVATION.md` (per-bridge deck and river heights).

## Per-folder layout

Each `reference/<site>/` now has:

- `aerial/ortho-2019.jpg` and `.json`: City of Edmonton 2019 orthophoto, north up, EPSG:3776 (NAD83(CSRS) / 3TM 114). The `.json` has the bounds and pixel size so a pixel can be placed: `x = xmin + (col+0.5)*pixel_m`, `y = ymax - (row+0.5)*pixel_m`. Pixel size is 0.2 m (up to 0.7 m for T133, whose outline spans 5 km).
- `elevation/dtm-2018-1m.tif`, `dsm-2018-1m.tif`, `README.md`: 2018 LiDAR clips and the per-deck numbers. EPSG:3979 (Canada Atlas Lambert), 1 m, metres CGVD2013.
- `night/*.jpg` and `SOURCES.md` (only 7 sites, see below).

Clip extent is the OSM geometry in `geometry.json` plus 120 m, at least 500 m across. `P152-muttart/B254-conservatory/` has its own copy.

## Aerial photos

- Source: `https://gis.edmonton.ca/site1/rest/services/Imagery_Public/2019_RGB_Pictometry/ImageServer` (`exportImage`, public, no key). The same folder holds `2018_RGB_Pictometry` (same 7.5 cm native pixel, matches the LiDAR year) and `2020_Spring_RGB_Pictometry_Tiled` (map tiles, bare-tree spring view, useful for outlines under summer leaf). Native pixel is 7.5 cm; the clips here are 0.2 m. Rerun at 0.075 by editing `RES` in the script.
- The images are true-vertical (the High Level sample shows no lean) and sharp enough to count truss panels, piers and lane markings. For modelling use them as a plan reference: bridge outline, pier positions, approach geometry, building footprints.
- Method: the CYXD project used Esri Wayback tiles (`docs/cyxd/hangar-footprints.md`). These City images are far finer than Esri's 0.18 to 0.7 m and are dated, so they replace Wayback here.
- Gotcha: the City site sits behind Cloudflare, which refuses Python's default user agent with HTTP 403 and "error code: 1010". The script sends a plain curl-style user agent. Nothing else was needed.
- **Licence not confirmed.** The City service page states none for the Pictometry layers (the LiDAR layers say Open Government Licence - Canada). Treat the images as measuring reference only and do not redistribute them, the same rule `hangar-footprints.md` set for the Esri tiles. If the repo is ever published, check or drop `aerial/` first.
- Refresh: `python fetch-site-data.py [site ...]` in an environment with `rasterio pyproj numpy pillow`. Sites are named by folder substring (`R10`, `T133`). It rewrites the aerial and the DEM clips.

## LiDAR and elevation

- Source: NRCan CanElevation HRDEM, STAC `https://datacube.services.geo.ca/stac/api`, collection `hrdem-lidar`, item `AB-Edmonton-1m` (cloud-optimised GeoTIFFs at `canelevation-dem.s3.ca-central-1.amazonaws.com/hrdem-lidar/AB-Edmonton-1m-dtm.tif` and `-dsm.tif`; the NRCan copy `NRCAN-Edmonton_2018-1m` is the same flight). 1 m, CGVD2013, nominal date 2018-05-12. Open Government Licence - Canada. The City also serves it as `Imagery_Public/2018_DTM_Lidar_1m` and `2018_DSM_Lidar_1m`.
- A newer 1 m mosaic tile `3_4-mosaic-1m` (2024-10-19) also covers the city. It was not used because the 2018 flight is a single consistent project with known gauge stage.
- The full files are about 9 GB each. The scripts read only the needed windows over HTTP range requests; nothing large is stored.
- Results, with checks: `ELEVATION.md`. The High Level upper deck reads 47.54 m above the river against the handoff's 47.55 m, which supports both the LiDAR and the handoff's datum.
- Limits: the DSM sees only the first return, so a deck under another deck (High Level lower road, Menzies walkways under the rail deck, Tawatinâ lower path) reads as the upper one. A sparse return over a river is smooth and can scatter by 0.1 m. Catenary, vehicles and railings add up to a metre on the DSM; the spread is in `data/elevation-summary.json`.
- `analyze-elevation.py` regenerates `ELEVATION.md`, the per-site `elevation/README.md` files and `data/elevation-summary.json`.

## Night lighting

`night/` exists for seven sites. All images are from Wikimedia Commons under CC licences, 1800 px copies, with author, date, licence and page link in each `SOURCES.md`, plus a paragraph on what the lighting looks like. Run `python fetch-night-photos.py` (standard library only) to refetch.

| Site | Night photos | Gist |
| --- | --- | --- |
| R10 High Level | 8 | Cool blue-white LED line along the upper chord, piers floodlit in the same colour (colour changes by event). |
| R9 Menzies | 3 | White LED edge line along the LRT deck, same pier floods. |
| R11 Walterdale | 2 | White arch edges, warm street lamps. |
| R13 Low Level | 3 | 2006: warm amber outline along the old truss, orange street lamps. Old photos. |
| F256 Funicular | 4 | White vertical LED bars in the railings, warm under-bench light. |
| P152 Muttart | 1 | Blue/violet pyramid ridge lines. |
| B255 Hotel Macdonald | 1 | Warm floodlit facade. |

**Not found: night photos for R12 James MacDonald, R14 Tawatinâ, R15 Dawson, R8 Groat, G116, G117, G119, T133, Z125, N258, N259, N260, V257.** Searches of Commons and the web gave daytime or dusk images only (a Dawson dusk frame shows no deck lighting). Leads that are not freely licensed: LocationScout's Tawatinâ page (copyrighted), Tom Arban's Walterdale press-kit photos (the City's `v2com-newswire` release), the City's "Light the bridge" page photo. For the plain road bridges the lighting is presumably ordinary roadway lamps on posts, but no photo here confirms the lamp colour (the High Level and Low Level frames show orange sodium street lamps on the approaches, so older lamps are orange and any newer LED retrofit is not documented).
- Dawson (a truss) is the likeliest to have photos on Flickr or from the City's Edmonton Archives; neither was searched in depth.
- Colour temperatures in the table above are read by eye from long-exposure photos, which shift colour. Verify against a source with stated colour (the City's lighting specification for the High Level is described by Lumenpulse and in Construction Canada's article "Historic bridge gets a bright new look").

## Not done

- No 2018 or 2020 aerials were saved, only 2019. The 2018 service matches the LiDAR year; fetch it with the same script if the date matters.
- Heights are not yet in the individual `MODEL-HANDOFF.md` files. A modeller should read `ELEVATION.md` and `RIVER-LEVEL.md` first. Items there that were listed as blocking (deck ASL, water ASL, datum) are now answered, with the caveats above.
- Nothing is committed: about 270 MB of images and rasters were added (aerials about 100 MB, DEM clips about 150 MB, night photos about 13 MB). If that is too much for the repo, keep only the scripts and `data/`, since the clips regenerate in a few minutes.
