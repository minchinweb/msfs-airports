# R20 Beverly Bridge: Tier 2 handoff

Built 2026-10-15: `scenery-edmonton-bridges/tools/site_r20.py` (helpers in `t2lib.py`), model `br_r20_beverly` (3,850 polys, one chunk), placed at the mid-point of way 61430014 with datum altitude 610.00 m. Built with `build.bat bridges` (exit 0, `_RPTErrors.xml` empty). **Not seen in the sim.** Checked against the 2019 orthophoto (`tools/overlay.py r20 R20-beverly`): the deck footprint sits on the deck and the end joints line up.

## What is in the model

Steel plate-girder highway deck (five girder lines, diaphragms every 7.5 m), concrete slab with asphalt top, three lanes with dashed white lane lines, yellow left edge line, white right edge line, four concrete piers, abutments, blue 3-rail steel railing on the south edge over a raised footway, concrete parapet with a blue rail on the north (inner) edge, davit lamps every 36 m on the south side.

## Sourced

- Plan: OSM way 61430014 (321.5 m, NW to SE) as the axis; deck lateral extent from the OSM outline, way 642360969 (-8.8 m south to +10.5 m north of the way, 19.3 m).
- Deck level: a quadratic through the 2018 LiDAR first returns on the way, vehicles dropped, lowered 0.1 m (22.1 m above the river at mid-span, 23.0 m at the SE end). `elevation/profiles.csv` was missing for this site; it is now written by `tools/lidar_pil.py` (Pillow only, no rasterio).
- Three lanes, 11.1 m carriageway (OSM `width` tag), the 1972 girder with a south-side sidewalk (City rehab page), blue steel railing (2011 photograph), abutments at the ends where the 2018 bare earth meets the soffit.
- River datum 610.00 m: the three Bridges clips give 610.14, 610.07 and 609.84; one common value is used so the three decks share a datum.

## Assumed (flagged)

- Pier stations (54, 129, 207, 280 m) and shape (single wide column under the first two, twin columns under the last two, cap beams) are read from the 12 May 2015 photograph (`photos/elevation-from-southwest-2015.jpg`) at about 5.7 px per metre; plus or minus 10 m.
- Girder depth 3.0 m, slab 0.3 m, girder spacing, diaphragms, railing details, sidewalk width 2.0 m, lamp spacing.
- Which mapped carriageway is "Beverly" (the project inventory and Wikipedia contradict each other); the south 1972 girder deck is taken as R20 because the 2015 photograph shows column piers under the nearer (south) deck.
- Cars, signs and the NW and SE approach roads are not modelled.

## Remains

- A span layout or bridge sheet from the City or Alberta Transportation would replace the photo-read piers.
- Night lighting, textures, transparency: none, as for Tier 1.

## Sim-side checks for William

- Deck against the sim terrain at both abutments (the sim bank may sit higher than the 2018 LiDAR).
- That the roads the sim draws meet the deck ends at about 632.8 m (NW end) and 633.1 m (SE end) ASL.
- The datum: compare 610.00 m with the sim river surface here.
- The piers reach the water bed (they extend to 6 m below the datum).
