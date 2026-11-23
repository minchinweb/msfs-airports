# H27 Calgary Trail / Gateway and H28 Blackmud Creek arches: Tier 2 handoff

Built 2026-11-23. `scenery-edmonton-bridges/tools/site_h27.py` and `site_h28.py`, both on the shared `tools/henday.py`. Models: `br_h27_calgary_trail` (about 26,000 polys, 2 chunks), placed at 53.4365, -113.4910, datum 680.00 m; and `br_h28_blackmud_arches` (about 3,300 polys, 1 chunk), placed at 53.4349, -113.5134, datum 660.00 m. Package built with the sim closed (exit 0, `_RPTErrors.xml` empty). **Not seen in the sim.**

## H28 is not where the brief put it

NOTES.md placed H28 at 53.437, -113.496, "immediately west" of H27. The 2019 aerial and the LiDAR show no creek there. The OSM bridge ways at -113.496 (41985530, 41985559, 41985706, 41985746, 41986110) are H27's own decks. 41985530 and 41985559 are two of the four CCE trellis structures: striped beam shadows in the aerial, over the West Edmonton Mall ramp. Blackmud Creek (OSM stream 490629227) passes under the Henday 1.5 km further west, at **53.4348, -113.5134**, about 500 m east of 111 Street. The LiDAR shows three raised decks there, which matches CCE's three 76 m structures:

- the ramp structure, carrying ways 25477544 (the collector from the Calgary Trail interchange) and 115754686;
- Henday westbound, 25477513;
- Henday eastbound, 25477514.

Each is 76 to 78 m in OSM. The deck stands 15.8 to 16.5 m above the creek bed (LiDAR); CCE gives 17 m. `geometry.json` keeps the brief's lists unchanged and adds `osm_added_2026_11_23`, every road, stream and railway way in 53.4285..53.4420, -113.5215..-113.4800, read from the OSM API on 2026-11-23. `PRIORITY.md` has the corrected centre.

## Data collected this session

- `geometry.json` `osm_added_2026_11_23`, 155 ways. The aerial and LiDAR clips were refetched (`fetch-site-data.py H27`) so they cover both sites: aerial 0.49 m/px, DEM 4338 x 3149 m. All are gitignored.
- `elevation/h27-samples.json` and `h28-samples.json` (committed): first return, bare earth, embankment crown and side ground every 2 m along each deck chain, plus the bare earth at every crossing. Written by `python -I -c "import sys; sys.path.insert(0, 'scenery-edmonton-bridges/tools'); import site_h27, site_h28; site_h27.sample(); site_h28.sample()"`, which needs numpy, Pillow and the clips.
- `street/`: 15 Mapillary frames, three aimed at each structure (`street/SOURCES.md`, CC BY-SA 4.0). They show:
  - trellis beams on tall MSE panel walls, under the Henday over the West Edmonton Mall ramp;
  - the curved 2 South flyover on single-column hammerhead piers;
  - the Henday over Calgary Trail on piers with a wide cap;
  - concrete barriers on every deck.

  No frame shows the Blackmud arches from below.

## What is in the models

H27, 19 decks (`DECKS` in `site_h27.py`):

- **Girder decks**:
  - Henday WB and EB and both links over Calgary Trail / Gateway;
  - the three Henday decks and the exit beside the flyover at -113.495;
  - the 2 South flyover (third level, 314 m, ten hammerhead piers);
  - the loop ramp over Calgary Trail / Gateway;
  - link 22927649;
  - five decks over the Leduc Subdivision railway at the east edge.
- **Trellis structures (4)**: the Henday WB and EB over the West Edmonton Mall ramp (41985530, 41985559), the West Edmonton Mall ramp over Calgary Trail SW (22949436), and the 2 South ramp over the West Edmonton Mall ramp (22924959). They have beams square to the road underneath, 44 m long and 8 m apart, with a 1.3 m top flange, on two MSE walls 44 m apart (CCE 2008). The deck covers only the stretch between the walls. The beam layout lies on the striped shadows in the aerial.
- **Approaches** from every deck end, up to 150 m along the connecting OSM ways:
  - the road follows the first-return level at up to 6 %;
  - where it stands more than 1.5 m above the bare earth, the sides are vertical concrete walls (MSE fill; the DTM leaves it out);
  - elsewhere the sides are 4:1 grass slopes, capped at 6 m of drop;
  - between two decks on one road, each side draws to the midpoint.

H28, three arch structures (CCE 2008):

- 40 m arch centred on the creek crossing, 7.5 m rise, crown at the soffit of the 1.5 m deck slab;
- 18 m of deck cantilevered on past each springing;
- two ribs per structure, 7.0 m wide and 0.4 m thick;
- spandrel cross walls every 5 m;
- springing lines skewed 15 degrees, turned towards the creek.

| Deck (OSM) | Kind | Length m | Top start / mid / end (m ASL) | Width m | Piers (m from start) / beams / arch centre |
| --- | --- | --- | --- | --- | --- |
| 22924969 link WB | girder | 106 | 692.03 / 693.28 / 694.43 | 12.4 | 25, 54, 80 |
| 22924966 Henday WB | girder | 106 | 691.73 / 691.56 / 691.35 | 12.4 | 21.8, 51.6, 78.8 |
| 22924964 Henday EB | girder | 104 | 691.22 / 691.36 / 691.52 | 12.4 | 26.1, 52.1, 84.1 |
| 22916449 link EB | girder | 106 | 691.01 / 691.20 / 691.21 | 8.7 | 27.2, 54.5, 86.2 |
| 41985530 Henday WB | trellis | 114 | 690.15 / 689.91 / 689.45 | 12.4 | 14 beams |
| 41985559 Henday EB | trellis | 72 | 690.03 / 690.22 / 690.38 | 12.4 | 9 beams |
| 41985706 Henday WB | girder | 54 | 690.79 / 690.69 / 690.61 | 12.4 | 21 |
| 41986110 exit | girder | 54 | 690.79 / 690.69 / 691.50 | 8.7 | 34 |
| 41985746 Henday EB | girder | 58 | 690.58 / 690.64 / 690.73 | 12.4 | 23 |
| 22915670 2 South flyover | girder | 314 | 698.78 / 699.36 / 695.15 | 12.4 | 18, 48, 64, 106, 145, 175, 205, 232, 260, 287 |
| 22916446 loop | girder | 90 | 690.02 / 690.64 / 690.89 | 8.7 | 43.7, 60.8 |
| 22949436 WEM ramp | trellis | 130 | 690.11 / 689.76 / 689.27 | 12.4 | 16 beams |
| 22924959 2 South ramp | trellis | 203 | 690.91 / 690.91 / 690.13 | 19.8 | 25 beams |
| 22927649 link | girder | 62 | 690.75 / 690.75 / 690.65 | 12.4 | 33 |
| 60093990, 22916432, 22916426, 115758014, 22916422 (railway) | girder | 62-68 | 692.2 to 692.7 | 8.7-12.4 | one each, between the railway and Parsons Road |
| 25477513 Henday WB | arch | 76 (run 82) | 681.60 / 681.72 / 682.10 | 16.1 | creek at 42.4 |
| 25477514 Henday EB | arch | 76 (run 80) | 682.59 / 682.33 / 682.16 | 16.1 | creek at 38.0 |
| 25477544 + 115754686 ramp | arch | 76 (run 80) | 680.98 / 681.14 / 681.38 | 16.1 | creek at 40.0 |

Creek bed at the arches: 665.7 to 665.9 m (2018 bare earth).

## Assumed (flagged in the module docstrings)

- **Deck widths** from the OSM lane count: 3.7 m lanes, 3.0 m and 1.0 m shoulders, 0.5 m barriers.
- **H28 ramp deck**: three lanes' width, centred 3.9 m left of 25477544.
- **Depths**: 1.8 m girders, 2.0 m trellis beams.
- **Pier sizes**: hammerhead up to 10.5 m deck width, otherwise two or three columns under a cap.
- **Pier stations**: in each gap of more than 14 m between the roads underneath, then more until no span exceeds 46 m, kept 7 m clear of the roads.
- **H28**: rib positions (a quarter of the deck width each side), spandrel spacing, footings, and the sign of the skew.
- **Grass slopes**: 4:1. There are no lamps, signs or gantries.

## Sim checks for William

- Whether the sim draws its own decks here and doubles up, and whether the grass slopes and walled approaches z-fight with the sim's terrain (the H39 question again).
- **H28**: the creek valley under the arches. The sim's terrain may fill it, which would bury the ribs. If it does, a flatten polygon (`terrain.py`) at creek level is the fix.
- Clearance under the girder decks over Calgary Trail / Gateway (about 8 m from the LiDAR) and under the trellis beams.

## Rebuilding

`python -I scenery-edmonton-bridges/tools/gen_bridges.py h27 h28` (numpy, Pillow, shapely). It reads only `geometry.json` and the two sample files.
