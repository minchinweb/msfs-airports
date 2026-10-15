# R21 Clover Bar Bridge: Tier 2 handoff

Built 2026-10-15: `scenery-edmonton-bridges/tools/site_r21.py` (helpers in `t2lib.py`), model `br_r21_clover_bar` (4,004 polys, one chunk), placed at the mid-point of way 61431758 with datum altitude 610.00 m. Built with `build.bat bridges` (exit 0, `_RPTErrors.xml` empty). **Not seen in the sim.** Checked against the 2019 orthophoto (`tools/overlay.py r21 R21-clover-bar`): footprint and end joints match.

## What is in the model

Plate-girder highway deck, three lanes with lane lines (travel is the opposite way to the axis: yellow edge line on the south), four tan wall piers with round noses under cap beams, abutments, concrete parapet with blue rail on the south (inner) edge, blue 3-rail steel railing on the north edge, davit lamps every 36 m on the north side. The axis is the OSM way reversed so it runs NW to SE like R20.

## Sourced

- Plan: OSM way 61431758 (355.1 m); deck extent from the OSM outline, way 642360970 (344.5 m long, -6.4 m south to +10.8 m north of the way).
- Deck level: a quadratic through the 2018 LiDAR first returns, lowered 0.1 m: 22.5 m above the river at the SE end rising to 25.3 m at the NW end. `elevation/profiles.csv` is new (`tools/lidar_pil.py`).
- Three lanes (OSM, Truck News 2001); the 2011 photograph taken from this deck shows the blue steel railing; the 2015 photograph shows wall-type tan piers under the far (north) deck.
- Same 610.00 m datum as R20 and R22.

## Assumed (flagged)

- **Pier stations.** The far deck is hidden behind R20 in the 2015 photograph, so they are the same fractions of the span as the R20 reading (0.17, 0.40, 0.64, 0.87 between LiDAR ground crossings at 10.8 and 333.8 m): 65, 140, 219 and 292 m. Wall plan 1.6 m by 9.2 m with round noses; cap 2.6 m by 11.2 m. Plus or minus 15 m.
- Girder depth 2.8 m, no sidewalk, 11.1 m carriageway centred on the way (no width tag on this way), lamps.
- That the present deck is the 1953 structure (or its 2001 three-lane rebuild) with plate girders: not stated by any source; the 2015 photograph shows a girder deck, not a truss.
- Which carriageway is "Clover Bar": see R20 handoff.

## Remains

Same list as R20: a bridge sheet for spans, piers, girders; night lighting; textures.

## Sim-side checks for William

Deck against sim terrain at both ends (NW end deck 635.3 m ASL where the 2018 bare earth is 634.1 m, so the abutment is nearly buried); road ends meeting the deck; datum against the sim river; seam with R20 and R22 is none, they are separate structures about 100 m apart in plan, same datum.
