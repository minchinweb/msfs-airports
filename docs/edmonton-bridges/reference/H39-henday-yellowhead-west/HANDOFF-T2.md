# H39 Henday / Yellowhead west: Tier 2 handoff

Built 2026-10-15: `scenery-edmonton-bridges/tools/site_h39.py` (shares `t2lib.girder_deck`, `bridgelib`; `road_fill` is the H52 one with a general neighbour clip). Model `br_h39_henday_yellowhead` (about 26,400 polys, 2 chunks), placed at 53.574, -113.662 with datum altitude 680.00 m. **Not seen in the sim.**

## Review: was there enough?

Yes. The folder was complete (not cut off): NOTES.md, SOURCES.md, geometry.json with all ten decks and the Henday approaches, the 2019 orthophoto and the 2018 DSM/DTM clips (they cover the whole interchange and about 600 m beyond), five Mapillary frames. Missing and collected: the flyover and loop ramp chains and the Yellowhead carriageways (they were not in `geometry.json`, which is why the NOTES listed them as missing). 34 ways were read from the OSM API (box 53.566, -113.672, 53.582, -113.650) and stored under `ramps_added_2026_10_15`. `elevation/README.md` was never written; the DSM/DTM samples are now in `elevation/h39-samples.json`. Still missing and not findable: overpass drawings (girder depth, abutment and pier stations), WG girder-line counts.

H38 (Henday / Stony Plain Road, 53.540) has no reference folder, is 3.7 km south and a separate seven-bridge interchange, so it was **not built**.

## What is in the model

- Ten decks, each on abutment walls with the shared `girder_deck`: N-1 (6 lines) and S-6 (6 lines) Henday over Yellowhead, parapets on the median side; NW-7 and SE-8 (one lane, 8.3 m, one column per pier); WS1-9 and EN1-12 (single span, no pier); WS3-11 (two spans, two columns) and EN3-14 (two spans, concrete girders); WS2-10 and EN2-13 (three spans, two piers of two columns, concrete girders, over the three roadways west of / east of Henday). WG decks have weathering-steel (rust) girders, NU decks concrete.
- Ten chains drawn as raised road on 4:1 grass slopes, with edge lines: both Henday carriageways (600 m each side of the deck), the NW and SE ramp chains, the WS chain (Yellowhead westbound over the EN ramp, Henday NB / SB and Yellowhead, down to Henday southbound), the EN chain (from the west over the WS ramp, Henday and Yellowhead to Henday northbound), and four more ramps. Ramps are drawn over their full mapped length inside the LiDAR clip; a road lower than 0.8 m above its side ground sinks below the terrain (the sim already draws at-grade ends).
- Slopes are cut short (and closed with a vertical grass skirt) where another road at a similar level runs alongside, so parallel embankments do not run through each other.
- Not modelled: Yellowhead Trail itself (the sim draws it), MSE walls, guardrail, signs, sign gantries, ramp lamps.

## Sourced

- Plan: OSM ways (listed in the `site_h39.py` docstring and `geometry.json`). Checked on the 2019 aerial at four crops: every road, loop, deck and flyover sits on its photo band (`tools/overlay.py` style overlay).
- Heights: 2018 LiDAR. Deck tops from a robust quadratic fit to the first returns along each deck, minus 0.12 m; roads from the bare-earth crown minus 0.1 m. Deck tops: N-1 691.5, S-6 692.1, NW-7 691.2, SE-8 693.1, WS1 693.8, WS2 701.9, WS3 696.3, EN1 697.9, EN2 701.5, EN3 691.7 m ASL.
- Inspections (Alberta file 85047): spans, clear roadway widths, column counts, girder type, five NU girders; clearances (5.5 to 5.8 m over Yellowhead, 9.0 m and 7.7 m over Henday). Girder depth = soffit height from the published clearance over the pavement under the deck, capped (2.9 m on the 64 m span, 1.95 m on the NU decks); results 1.56 to 2.9 m.

## Assumed (flagged)

- Where each structure sits in its OSM line: the first pier at the midpoint of the crossings with the road under (the two Yellowhead carriageways, or the first two roads under WS2 / EN2), then the inspection spans. EN3-14 and WS2-10 then fit their OSM decks to 2.5 m; the other decks come out 5 to 30 m shorter than their mapped lines (the lines include embankment).
- Girder line counts of the WG decks (6, 6, 4, 4, 5, 5, 5), column radius (0.5 to 1.0 m), cap beams, deck lanes (3, 3, 1 ...), ramp roadway width 8.6 m, approach width 14.5 m for Henday, taper to the deck width over 60 m, 4:1 slopes, grass colour, lamps only on N-1 and S-6.
- Roads end where the LiDAR clip ends (rotated rectangle, 40 m fade); the Henday carriageways end 600 m from the decks with a 120 m fade.

## Seams (checked numerically)

- Deck ends: the approach profile is pinned to the deck at each abutment, step 0.000 m on all ten decks; the chains with three decks (WS) interpolate between the pins, so WS1 / WS2 / WS3 and their ramps are flush.
- Ramp-to-ramp junctions inside the model (en / w_s, en / ne_n, ne_e / nw, ne_n / ws, w_s / ws, sb_w / se): heights agree to within 0.03 m. Ramp starts on the Henday carriageways lie outside the 600 m drawn approach, so they end on their own embankment (grass and asphalt colours only).
- One BMesh, split into two chunks on polygon boundaries; asphalt, grass, concrete and rust are the same palette entries in both, so no colour change between chunks.

## Sim checks for William

- Deck tops (above) against the sim road where the sim draws Henday and the ramps; the sim may already draw its own decks here and double up.
- Whether the green slopes z-fight with sim terrain along the loops and along the Henday embankment, and whether the Henday approaches (600 m) join the sim road without a step at the 120 m fade.
- Yellowhead must pass clear under the decks (about 5.5 m between pavement and soffit) and Henday must pass clear under WS2-10 and EN2-13 (about 9 m).
- The ramp ends along Yellowhead (the NW loop and SE ramp merges) lie on the sim's road at grade; they should be hidden by the sink rule.

## Rebuilding

`python -I -c "import sys; sys.path.insert(0, 'scenery-edmonton-bridges/tools'); import site_h39; site_h39.sample()"`, then `python -I scenery-edmonton-bridges/tools/gen_bridges.py h39`. The LiDAR clips are gitignored (`_refetch_lidar.py` in this folder re-cuts them); the samples are committed.
