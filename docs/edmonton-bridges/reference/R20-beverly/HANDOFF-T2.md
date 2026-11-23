# R20 Beverly Bridge: Tier 2 handoff

Built 2026-10-15 with the photo-read piers and 11.1 m carriageway. Updated 2026-11-23 to Alberta Transportation file 77132 (spans, pier stations, width). Module `scenery-edmonton-bridges/tools/site_r20.py` (helpers in `t2lib.py`), model `br_r20_beverly` (3,858 polys, one chunk; was 3,850), placed at the mid-point of way 61430014 with datum altitude 610.00 m (unchanged). The 2026-11-23 model was generated with `gen_bridges.py r20`; **it has not been built with `build.bat bridges` or seen in the sim.** Overlay check (`tools/overlay.py r20 R20-beverly`): the deck footprint sits on the south deck from abutment to abutment, and both end joints line up. The piers are under the deck, so the top-down overlay cannot check their stations.

## What is in the model

Steel plate-girder highway deck (five girder lines, diaphragms every 7.5 m) on abutments, 320.1 m between abutments. Concrete slab with asphalt top; a 19.2 m gross deck: 1.8 m south sidewalk, 16.8 m clear roadway (three 3.7 m lanes in an 11.1 m carriageway, with 2.85 m shoulders), 0.6 m north parapet. Dashed white lane lines, yellow left edge line, white right edge line. Four concrete piers under five spans (54.9, 70.1, 70.1, 70.1, 54.9 m), abutments, blue 3-rail steel railing on the south edge over the raised footway, concrete parapet with a blue rail on the north (inner) edge, davit lamps every 36 m on the south side.

## Sourced

- Spans, nominal length, max span, gross width 19.2 m, clear roadway 16.8 m, concrete piers and caps, pile-founded abutments, polymer-modified asphalt wearing surface: Alberta Transportation file 77132 (BEVERLY BRDG, B143), from https://www.transportation.alberta.ca/PlanningTools/Data/Bridge/Structure-Export.csv, last inspected 2023-08-16.
- Pier stations, from the first abutment: 54.9, 125.0, 195.1 and 265.2 m. The record is symmetric, so the same stations hold from the other end. The model's 0 m is the NW end of the OSM way, and the deck starts 0.97 m along it (the OSM axis is 322.0 m, and the 320.1 m deck is centred on it).
- Plan: OSM way 61430014 as the axis (NW to SE). Deck lateral centre: the middle of the OSM outline, way 642360969 (-8.8 m south to +10.5 m north of the way, 19.3 m across), giving -8.75 m to +10.45 m for the 19.2 m gross.
- Deck level: a quadratic through the 2018 LiDAR first returns on the way, vehicles dropped, lowered 0.1 m (22.1 m above the river at mid-span, 23.0 m at the SE end). `elevation/profiles.csv` is written by `tools/lidar_pil.py` (Pillow only, no rasterio).
- Carriageway 11.1 m (OSM `width` tag, read as 3 x 3.7 m lanes), the 1972 girder with a south-side sidewalk (City rehab page), blue steel railing (2011 photograph), abutments at the ends where the 2018 bare earth meets the soffit.
- River datum 610.00 m: the three Bridges clips give 610.14, 610.07 and 609.84; one common value is used so the three decks share a datum.

## Assumed (flagged)

- Lane width 3.7 m, shoulders 2.85 m each side (these make the 16.8 m clear roadway), sidewalk 1.8 m, north parapet 0.6 m. The record gives only the totals.
- Pier shape: single wide column under the first two piers, twin columns under the last two, cap beams, all as read from the 12 May 2015 photograph (`photos/elevation-from-southwest-2015.jpg`). The record says concrete shafts and caps, not the shape.
- Girder depth 3.0 m, slab 0.3 m, girder spacing, diaphragms, railing details, lamp spacing.
- Which mapped carriageway is "Beverly" (the project inventory and Wikipedia contradict each other); the south 1972 girder deck is taken as R20. Alberta file 77132 names the 1972 deck BEVERLY BRDG, but gives only "E boundary of Edmonton" as its location.
- Cars, signs and the NW and SE approach roads are not modelled.

## Replaced (2026-11-23)

- Pier stations 54, 129, 207 and 280 m (from the 2015 photo, plus or minus 10 m) are replaced by the record's 54.9, 125.0, 195.1 and 265.2 m from the first abutment.
- Lateral extent of the deck: the 11.1 m carriageway centred on the way, with sidewalk 2.0 m, lateral -8.8 to +10.5 m, and 19.3 m total, is replaced by a 19.2 m gross deck (-8.75 to +10.45 m) with a clear roadway of 16.8 m and a 1.8 m sidewalk.
- Deck length: the full 322.0 m OSM axis is replaced by the 320.1 m between abutments.
- `t2lib.girder_deck` gained a `t_c` argument (carriageway centre, default 0). The R21 and R22 models do not pass it, so their output is unchanged.

## Remains

- Night lighting, textures, transparency: none, as for Tier 1.
- Girder depth, pier shaft shape and plan size, abutment size, and deck thickness are still not in any source checked.

## Sim-side checks for William

- Deck heights at both abutments against the sim terrain (the sim bank may sit higher than the 2018 LiDAR).
- That the roads the sim draws meet the deck ends (about 632.8 m NW and 633.1 m SE ASL before the 0.97 m trim; the ends are now 0.97 m further in).
- The datum: compare 610.00 m with the sim river surface here.
- The piers reach the water bed (they extend to 6 m below the datum) and sit at the stations above.
