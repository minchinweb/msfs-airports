# H52 Sherwood Park Cloverleaf: Tier 2 handoff

Built 2026-10-15: `scenery-edmonton-bridges/tools/site_h52.py` (helpers in `t2lib.py`: `girder_deck` gained a `lanes` argument, default 3, unchanged for older sites). Model `br_h52_sherwood_park` (about 16,400 polys, 2 chunks), placed at 53.513, -113.344 with datum altitude 700.00 m. **Not seen in the sim.**

## Review: was there enough?

Yes, at the Y79 standard. The 2018 LiDAR clips cover every way. Missing and collected: the loops and ramps other than the two in `geometry.json`, and the two Henday carriageways (needed for the pier stations and the clearance). Overpass was down (HTTP 502/500), so they came from the OSM API map call, now in `geometry.json` under `ramps_added_2026_10_15`. Still missing and not findable: the 2016 inspections (404), so girder depth, widths and span split are derived or assumed.

## What is in the model

- E-7 (eastbound, 3 lanes) and W-8 (westbound, 4 lanes): welded-girder decks over Henday, one pier on the Henday median (4 and 5 columns, cap beam), abutments 65.5 m and 63.0 m either side of it along the travel direction.
- EN1-9 (flyover over Henday) and EN2-10 (flyover over the freeway, concrete girders), both on one flyover chain from the freeway west of Henday, up over Henday, over the freeway east of it, to northbound Henday.
- Freeway and Wye Road approaches (up to 1 km each side, 4:1 grass slopes, inner slopes cut short and skirted so the two carriageways do not run through each other), the flyover chain, four loops (SW, NW, NE, and the SW loop chain), collector ramps.
- Not modelled: Henday itself (the sim draws it), at-grade Henday collector links, guardrail, signs, sign gantries.

## Sourced / assumed

- Sourced: plan (OSM), levels (2018 LiDAR: deck first-return fit less 0.12 m; road = bare-earth crown less 0.1 m), 5.3 m clearance over Henday.
- Girder depth: soffit = road under + 5.4 m. E-7 3.23 m, W-8 3.29 m, EN1 3.4 m (capped), EN2 2.1 m (capped, concrete).
- **Assumed:** the inventory prints read as widths 16.1 / 19.8 / 13.9 / 13.9 m, total lengths 128.5 / 128.5 / 123.5 / 71.5 m, longer span 65.5 / 65.5 / 63.0 / 36.5 m (west or first span the longer); piers on the median centre; girder lines 6 / 7 / 5 / 5; column radius; steel girders grey; ramp roadway 8.6 m (11.6 m two lanes); approach width from the lane tags; lamps.

## Checks

- Plan against the 2019 aerial (west half): roads, both west loops, flyover and decks sit on the photo (`tools/overlay.py`). The east half of the photo is blank.
- Seams: deck ends pin the approach to the deck height by construction; every ramp-to-mainline joint is within 0.3 m (checked numerically); asphalt joins asphalt and grass joins grass, and chunks split on polygon boundaries.

## Sim checks for William

- Deck tops about 717.6 m (freeway), 721.0 m and 724.6 m (flyovers): the sim road should meet the approach fill.
- Whether the green slopes z-fight with sim terrain along the loops and the Henday cut, or double up with any deck the sim already draws.
- Henday must still pass clear under the decks (about 5.4 m between pavement and soffit).

## Rebuilding

`python -I -c "import sys; sys.path.insert(0, 'scenery-edmonton-bridges/tools'); import site_h52; site_h52.sample()"`, then `gen_bridges.py h52`.
