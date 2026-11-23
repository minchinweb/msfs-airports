# R6 Quesnell Bridge: Tier 2 handoff

Built 2026-10-15: `scenery-edmonton-bridges/tools/site_r6.py` (helpers in `t2lib.py`), model `br_r6_quesnell` (about 19,000 polys, two chunks placed at the same point), placed at 53.506262, -113.566653, datum altitude 618.30 m. Built with `build.bat bridges` (exit 0, `_RPTErrors.xml` empty). **Not seen in the sim.** Checked against the 2019 orthophoto (`tools/overlay.py r6 R6-quesnell`): the deck footprint, the median and the east path sit on the aerial deck; the south end widening for the Fox Drive merge matches. `elevation/profiles.csv` did not exist; it is now written by `tools/lidar_pil.py`.

## What is in the model

Eight-lane concrete girder deck (14 girder lines, haunched over the supports of the continuous spans, steel-grey diaphragms every 8 m), asphalt with dashed white lane lines, yellow median edge lines and white edge lines, concrete median barrier, west parapet with a steel rail, concrete barrier and a 4.2 m shared path on the east with a three-rail steel railing, the south merge lane widening from the Fox Drive ramp (3.9 m over the first 102 m), five piers each with two round shafts, a concrete cap beam and two steel cap extensions with inclined struts, abutments, lamps (west edge, double-arm median).

## Sourced

- Plan: OSM west carriageway 22916674 and east ways 22916673, 944470769, 297284104; the axis runs midway between them, south to north, 315.7 m.
- Deck level: quadratic through the 2018 LiDAR first returns on the west way (18.3 m above the datum at the south end, 20.7 m at the north), lowered 0.1 m.
- Spans 50 / 54.9 x 3 / 53.3 + 46.6 m, five piers with two shafts each, cast-in-place deck, parabolic precast girders (PIEVC 2008, IABSE 2008); ten steel cap extensions, two per pier (CISC Alberta 2011 award page, fetched 2026-10-15; it gives no dimensions).
- Overall width (-25.4 to +22.0 m about the axis), median barrier position, the 4.2 m east path (City 2018) and the merge lane: measured on the 2019 aerial at 0.2 m/px.
- 2015 photograph: cap extensions, round shafts, plain concrete finish, steel cross-frames.

## Assumed (flagged)

- Span order: the papers list the 50 m simple span first; it is placed at the south end. The two papers do not say which bank holds it. Pier stations 50, 105, 160, 215 and 268 m from the south end follow from that.
- Shaft spacing (13 m between shafts), diameter 2.5 m, cap beam 2.0 m deep, cap extension geometry.
- Girder count (14), depths (1.9 m mid-span, 3.4 m at supports, 2.4 m on the simple span), slab 0.3 m, lane widths, railing details.
- Datum 618.30 m (common with W85); the clip river surface is 618.44 m.
- Abutments are plain back walls to the LiDAR ground; the south end passes over a park road in the aerial that is not modelled. Approach roads, signs, traffic and the Fox Drive ramp are not modelled.

## Remains

- PIEVC 2008 Exhibit 2-4 (report p. 2-11) was read on 2026-11-23. Its spans (50.10, 54.90 x 3, 53.30, 46.60 m) match the model, and so do the five piers. It does not say which bank holds the 50 m span, so the span order is still assumed. The McBride-Ragan 1967 contract drawings (not found as an open file) would settle it.
- Model differences left as they are (not in the change rule): the model joins spans 3 and 4 over the fourth pier, where PIEVC has a break between the 164.7 m group and the 53.3 + 46.6 m group. The model draws 14 girder lines; PIEVC says ten before the widening. The model's caps use steel extensions (CISC 2011); PIEVC's caps are post-tensioned (Exhibit 2-5).
- The `site_r6.py` docstring says 315.7 m. The spans sum to 314.6 m, so the axis is scaled about 0.3 % longer than the spans. This is the existing scaling and was not changed.
- Night lighting, textures, transparency: none, as for Tier 1.

## Sim-side checks for William

- Deck against the sim terrain at both abutments (north end deck about 639.0 m ASL over ground at about 634.7 m; south end deck 636.5 m over ground at 626 to 634 m).
- That the sim roads meet the deck ends at those heights; the sim may carry its own Quesnell or none.
- The datum: compare 618.30 m with the sim river surface; the piers reach 5 m below it.
- That the shafts show only on the bank slopes and in the water, not floating, on the south bank where the ground rises steeply.
