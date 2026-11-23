# R21 Clover Bar Bridge: Tier 2 handoff

Built 2026-10-15 as a placeholder: four piers, a 344 m deck from the OSM outline, 17.2 m wide. Rebuilt 2026-11-23 to the Alberta record (file 02032, `Structure-Export.csv`, inspected 2025-09-14): `scenery-edmonton-bridges/tools/site_r21.py` (helpers in `t2lib.py`, unchanged this time), model `br_r21_clover_bar` (3,728 polys, one chunk), placed at the mid-point of way 61431758 with datum altitude 610.00 m. Built with `build.bat bridges` (exit 0, `_RPTErrors.xml` empty). The palette was restored after the generator run. **Not seen in the sim.**

## What is in the model

Five-span plate-girder highway deck, 320 m between abutments: spans 55, 70, 70, 70, 55 m, with interior piers at 55, 125, 195 and 265 m from the NW abutment. Gross deck 17.5 m, clear roadway 16.6 m, centred on the middle of the OSM outline. Three lanes with lane lines, four tan wall piers with round noses under cap beams 17.5 m across, abutments, concrete parapet with blue rail on the south (inner) edge, blue 3-rail steel railing on the north edge, davit lamps every 36 m on the north side. Axis is the OSM way reversed so it runs NW to SE, s = 0 at the NW end of way 61431758, as in R20. Deck top is still the quadratic through the 2018 LiDAR first returns.

## Sourced

- Spans 55/70/70/70/55 m, nominal 320 m, max span 70 m, gross deck 17.5 m, clear roadway 16.6 m, concrete piers and caps, pile abutments: Alberta file 02032 (B292), IN SERVICE, first in service 2001.
- Plan: OSM way 61431758 (355.1 m); deck lateral centre from the OSM outline, way 642360970.
- Deck level: quadratic through the 2018 LiDAR first returns, lowered 0.1 m (`elevation/profiles.csv`, `tools/lidar_pil.py`).
- Three lanes (OSM, Truck News 2001); the 2011 photograph taken from this deck shows the blue steel railing.
- Same 610.00 m datum as R20 and R22.

## Assumed (flagged)

- **Superstructure.** The record gives no superstructure type. Plate girder, five lines, 2.8 m deep is assumed. The 2001 date and 70 m spans are consistent with girders; the 2015 photograph shows a girder deck.
- **Pier shape.** Wall piers (1.6 m by 9.2 m, round noses) under a 2.6 m cap, from the 2015 photograph. The far deck is hidden behind R20 there, so the shape is an assumption. Pier stations are now from the record. The old fraction-based stations (65, 140, 219, 292 m) are gone.
- **Piers on the deck centre.** Piers are under the deck centre line (t_c, 2.2 m north of the way), not the way itself.
- **Lanes.** 11.1 m carriageway, three 3.7 m lanes. No width tag on the way; no lane width in the record.
- **Shoulders and edges.** 2.75 m shoulders each side of the clear roadway; 0.45 m edges each side of the gross deck.
- No sidewalk (the record gives no sidewalk; the 0.9 m between gross and clear is taken as edges).
- Lamps, blue railing and parapet placement, as before.
- Which carriageway is "Clover Bar": see R20 handoff. File 02032 gives no direction.

## Remains

Same list as R20: a bridge sheet for superstructure and pier dimensions, night lighting, textures.

## Sim-side checks for William

Deck against sim terrain at both abutments (the deck now ends 17.55 m inside the OSM way at each end, so the approach roads meet the deck over that gap: check they reach the abutments); datum against the sim river; the piers reach the water bed; seam with R20 and R22 is none, they are separate structures about 100 m apart in plan, same datum.
