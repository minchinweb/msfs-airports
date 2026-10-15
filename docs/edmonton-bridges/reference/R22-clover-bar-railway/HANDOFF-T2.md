# R22 Clover Bar Railway Bridge: Tier 2 handoff

Built 2026-10-15: `scenery-edmonton-bridges/tools/site_r22.py` (helpers in `t2lib.py`), model `br_r22_clover_bar_railway` (8,882 polys, one chunk), placed at the mid-point of way 23426591 with datum altitude 610.00 m. Built with `build.bat bridges` (exit 0, `_RPTErrors.xml` empty). **Not seen in the sim.** Checked against the 2019 orthophoto (`tools/overlay.py r22 R22-clover-bar-railway`): the track line follows the rails and the river pier stations sit on the tan cutwaters in the photo.

## What is in the model

Four steel deck-truss spans (55, 69, 69, 75 m, Pratt, 14.5 m deep, planes 4.6 m apart, floor beams, stringers, plan bracing), four tan concrete river piers with cutwaters tapering to the truss bearings, steel trestle towers and plate-girder spans on both approaches (six towers), ties, rails, plank walkways with handrails on both sides, concrete abutments. Length 505 m (published 504 m).

## Sourced

- Plan: OSM way 23426591 (513 m, reversed to run NW to SE); outline way 654886208 (7.1 to 7.9 m wide).
- Rail top 651.4 m ASL (2018 LiDAR median 651.45; 41.5 m above the river datum, published 42 m). Abutments at 5 and 510 m where the bare earth meets the deck.
- Single track, steel truss on concrete piers (Structurae, Forth Junction, 2011 and 2015 photographs), approach piers up to about 29 m (Edmonton Bulletin 1906, 95 ft).
- River pier stations 141, 210, 279, 354 m and trestle bents at 23.5, 55, 86, 401, 433, 465 m, read from the aerial (3.3 px per metre, plus or minus 3 m).

## Assumed (flagged)

- Truss depth 14.5 m (from the 2011 photograph against the 4.7 m locomotive; a Pratt layout with counters is the generic stand-in for the double-intersection panels in the photograph), panel counts, plane spacing, plate-girder depths (3.0 to 3.8 m), tower shape, pier taper and size, walkway.
- The 2011 photograph is oblique: truss depth is good to about plus or minus 2 m.
- Piers are drawn square to the track; in the aerial they are aligned with the river, about 24 degrees off.

## Remains

Span lengths and drawings; the 1932 OSM construction year is unexplained; textures, night lighting.

## Sim-side checks for William

Rail top 651.4 m ASL against the sim at both ends; piers reach the river bed; the datum; the towers on the slopes against the sim terrain (the 2018 bare earth sets the tower footings, 8 to 30 m below the deck).
