# W85 Fox Drive (Campbell Bridge): Tier 2 handoff

Built 2026-10-15: `scenery-edmonton-bridges/tools/site_w85.py` (helpers in `t2lib.py`), model `br_w85_fox_drive` (about 6,500 polys, one chunk), placed at 53.503135, -113.560877, datum altitude 618.30 m. Built with `build.bat bridges` (exit 0, `_RPTErrors.xml` empty). **Not seen in the sim.** Checked against the 2019 orthophoto (`tools/overlay.py w85 W85-fox-drive`): the deck, the joint lines and the road edges line up. `elevation/profiles.csv` did not exist; it is now written by `tools/lidar_pil.py`.

## What is in the model

Concrete girder deck (12 girder lines), asphalt with three lanes each way, dashed white lines, yellow median edge lines, concrete median barrier, a south sidewalk and a north shared path with a beige steel pipe railing (2 August 2012 photograph), lamps every 33 m on both edges, abutments, two bents of six round columns with cap beams.

## Sourced

- Plan: OSM south carriageway 25475831 and north ways 25475833 + 944470767; the axis runs midway between them, west to east, 89.1 m. Carriageways about 9.4 m apart.
- Deck level: quadratic through the 2018 LiDAR first returns on the south way (9.9 to 10.1 m above the datum), lowered 0.1 m; the creek surface in the clip is 618.09 m.
- Three lanes each way, south sidewalk (way 582712471), north shared path (way 27265227) (OSM).
- Overall width -16.0 to +17.5 m about the axis: read from the 2019 aerial.
- Railing, lamp shape and the median barrier: the 2012 photograph and the two 2018 Mapillary frames.

## Assumed (flagged)

- Everything under the deck. No source gives a span count, type or pier count, and no frame shows the underside: three equal 29.7 m spans, two bents of six 1.0 m round columns, 12 concrete girders 1.5 m deep, abutments at the LiDAR ground crossing. The 2008 Gazette rehabilitation notice does not say what changed.
- Datum 618.30 m (common with R6); the creek clip says 618.09 m.
- Railing colour (beige) from one photograph. Approach roads, the park road under the deck, signs and traffic are not modelled.

## Remains

- A bridge sheet or an underside photograph (the park road runs under the west bank) would replace the assumed spans and piers.
- Night lighting, textures, transparency: none, as for Tier 1.

## Sim-side checks for William

- Deck at about 628.2 m ASL against the sim terrain and roads at both ends (the approach roads LiDAR at 627.7 to 628.9 m).
- That the bent columns reach the sim creek bed and bank (they extend to the datum minus 4 m or the ground minus 1.5 m).
- The datum against the sim creek surface.
- Seam with R6: none to check. The two structures are 430 m apart; the Fox Drive ramp between them is a ground road, not modelled.
