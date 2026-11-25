# B276 The Church of Jesus Christ of Latter-day Saints — modelling brief

9010 85 Street NW, Strathearn, Edmonton. A church on the west side of 85 Street NW, just north of the Connors Road junction. Holyrood Gardens (B262) is across the road on the east side. It is a building, not a bridge, and has no Look or Where score.

Numbers are cited. Where a source is missing, the gap is stated, not filled.

## Building

**Footprint.** One OSM way, 322965284, 31 nodes, `building=church`. No `building:part`, no height, no levels. The plan is stepped, so it has several wings. It spans about 77 m east-west and 64 m north-south. The perimeter is about 282 m.

The OSM outline is the only footprint source. The aerial shows an irregular plan with the spire block near the middle; the OSM outline is used as the authority.

**Masses**, as seen in the 2019 aerial and the 2018 street frames (no measured heights):

1. **Spire tower.** A tall, thin brick tower with a light spire, near the middle of the front (east) wing. It is the tallest element in the street frames.
2. **Chapel / auditorium block.** A grey-panelled block with tall vertical pilasters, on the north-west side of the spire. It is the taller of the main blocks.
3. **Long brick wing.** A one-storey-looking brick wing with horizontal windows and the church name in raised letters on its east face, running along the road.
4. **Lower flat-roofed wings and entrance canopy.** Lower roofs on the south and back of the plan, and a canopy at the front entrance. The aerial shows a flat roof with a pale membrane, so there are no pitched roofs.

**Heights.** Measured 2026-11-24 from the 2018 DSM minus the grade (665.45 m), on a 2 m grid aligned with the building: wings 3 m, cultural hall 7 m (8 m on its north edge), chapel 7 to 8 m, spire peak 14.8 m. Proportions in the 2024 photo agree (chapel about 2.4 times the wing). The needle above the spire is too thin for the LiDAR; scaled from the photos it is about 3.6 m.

**Materials, as seen.** Brown brick on the wings and spire, grey vertical-panel cladding on the chapel block. Roofs look flat and light on the aerial. Not checked against a close photo.

## Site

- Church parcel: OSM way 594346540, `landuse=religious`, 24 nodes. Context only.
- Centre: 53.525858, -113.458448 (OSM outline centre; PRIORITY.md value).
- 85 Street NW centreline: OSM way 182082894. It lies about 20 to 25 m east of the church's east face.
- The church faces 85 Street. Its front lot is on the east side, between the building and the road.

## Parking

OSM has no parking on the church parcel. The nearest mapped lots are 110 m and 175 m south (private surface lots, OSM ways 1389212268 and 1389212267).

**Lot layout from the 2015 proposed site plan** (Gowling and Gibb Architects, sheet SD1.0, October 2015, scale 1:300). The plan is a reference-only drawing in `drawings-reference-only/`. It is traced into `geometry.json` under `parking_plan_2015`.

Georeferencing: the plan's north is to the left and east is up, about 6 px per metre. The church outline (OSM), 85 Street, the LRT and 92 Avenue all line up with the plan once that is applied. The lots are traced by eye, to about 10 m.

The plan shows 171 stalls in total: 5 barrier-free and 166 typical. It notes 22 stalls impacted by the project.

| Plan lot | Rows on the sheet | Where |
| --- | --- | --- |
| West lot | 6, 10, 12, 13, 14A | The large lot on the north-west, off 92 Avenue. Two banks of stalls with a central aisle. |
| North strip | 16 | A narrow strip of stalls between the north lawn and the building's west side. |
| South strip | 10 | Stalls along the south-west parcel edge, below the north strip. |
| South diagonal banks | 15, 20 | Two diagonal banks on the south-west side of the building, on either side of an aisle. |
| East curve lot | 8, 11, 15 | Perpendicular stalls along the curved drive on the east side. |

Mapping from the earlier aerial guesses: the aerial "north" point falls in the west lot, the aerial "west" point in the south diagonal banks, and the aerial "SE" point at the east curve lot's west edge.

**Trees and planting on the 2015 plan.** The sheet has no legend. Starburst symbols are read as conifers, and clusters of circles as deciduous shrubs or small trees. Sizes are estimates. These are proposals; current planting may differ. The plan shows:
- Three conifer starbursts on the north lawn by 85 Street.
- A row of four conifers on the west edge of the west lot, with a deciduous cluster at its north-west corner.
- A column of shrubs or small trees down the middle of the west lot.
- Two large round trees: one south-west of the west lot, one on the north-west lawn beside the building.
- Shrub beds along the building walls, with starbursts in the east bed and a starburst planter on the south-east lawn.
- A starburst pair in the south-west strip.

Points for each tree and shrub bed are in `geometry.json` under `trees_and_planting_2015_proposed`.

The 2024 owner's photo (`photos/2024-10-27-church-front-parking.jpg`) shows conifers and deciduous trees along the lot edges and in the front lawn. Check the trees on the aerial and in photos before placing them.

## Ground

- DTM 2018 (City LiDAR), median under the footprint: **665.45 m**. Range 665.11 to 665.64 m.
- DTM in an 8 m ring round the footprint: median 665.31 m, range 664.36 to 665.61 m.
- So the ground is flat to within about 0.3 m around the building. Set grade at 665.45 m above the same datum.
- The B262 model uses a datum of 664.56 m with grade 664.86 m (its footprint median). This church's grade is 665.45 m, about 0.6 m higher. Both come from the same 2018 LiDAR.

## Owner's photos (2026-11-24)

Five photos from the owner, in `photos/` (see `photos/SOURCES.md`). They show the front, the entrance sign "9010 - 85 ST.", the spire lit at night, the brick wing with the name lettering, and a courtyard. Use the night and front photos to check the masses and the entrance. The 2015 site plan is in `drawings-reference-only/`, marked reference only, because it is copyrighted.

## Street frames

Five 2018 frames in `street/`, from the road. Two of them are the B262 frames, which show the church from across the street:

- `mly-348860486834010.jpg` (2018-07-31): the only church-front view in the five. Shows the spire, the brick wing with lettering, the front lot with barriers and accessible bays.
- `mly-1106115126546811.jpg`, `mly-558906988431879.jpg`, `mly-861848634686402.jpg`: the 3-storey apartment block on the south side of the church approach, and a tall residential tower on the left. The church is not in these frames.
- `mly-288695449637417.jpg` (2018-08-10): 85 Street looking north, with the downtown skyline on the horizon. The church is not in this frame.

Also useful from the B262 folder: `B262-holyrood-gardens/street/mly-1242525472871579.jpg` (2018-08-13) and `mly-182877776943992.jpg` (2018-08-08). The first shows the church's grey chapel block and a spire-side tree line on the right of the street, with Holyrood's pre-construction site on the left. The second shows the spire far up 85 Street from the south. Both are pre-construction and 2018.

## Still missing

- The needle height (estimated from the photos), and window counts and positions.
- Whether the spire is a separate mass. The OSM outline does not split it.
- Parking lot extents, and whether the north lot is part of the church parcel.
- Night frames. None were downloaded.

## Holyrood Gardens check (B262)

The B262 street frames are not all useful here, but two of them show the church. They are listed above under Street frames. The B262 brief says the tower sits "on 85 Street". The OSM geometry does not agree: the 85 Street centreline (about -113.4576) lies about 40 m west of the tower's west face (about -113.4569). The tower is set back from the road. This does not change the church, but it should be checked before the B262 model is changed.

## Model (2026-11-24)

`scenery-edmonton-bridges/tools/site_b276.py`, model `br_b276_lds_church`, placed at the outline centre with heading 0.

- **Datum and grade.** Datum 665.11 m, the lowest DTM cell under the footprint. Grade is 0.34 m above it.
- **Building frame.** The walls run 30.6° off the compass. The model works in u (toward 85 Street, bearing 59.4) and v (bearing 329.4). The front, which faces the curved lot and Connors Road, is at -v.
- **Masses.**
  - The whole outline, to 3.3 m: buff brick, a brown fascia, and window bands between brick piers.
  - The cultural hall, u -24.5 to 5 and v -4.5 to 17, to 7.2 m.
  - The chapel, u -18.5 to -3 and v -18.8 to -4.5, with its front bay out to v -25, to 7.8 m. The bay's face has beige panels, white pilasters and brick corner piers.
  - The spire: three brick fins with stepped tops, 15 m, with a needle to 18.6 m. It stands at u 3.9 to 6.1 and v -17.9 to -15.3, where the DSM peak is.
  - The entrance: glazing and a flat canopy.
  - The lettering panel at the east end of the front, 0.5 m higher than the wing.
- **Night.** These follow the 2026 night photo, except the wall packs.
  - Emissive at night only: the spire (floodlit), the chapel face (wall-washed), the lobby, the canopy soffit, and about half the windows.
  - 17 `ASOBO_street_light` lights: two canopy downlights, two uplights at the spire, three uplights on the chapel face, and ten wall packs. The wall packs are on the walls facing the lots and walks; their number and places are assumed.
- **Car parks.** Sim `CarParking` polygons:
  - The plan's north lot, west lot and strips. The north strip is cut back to its paved west end.
  - Two rows along the curved front drive. The inner row follows the cars on the 2019 aerial. The outer row is 12.5 m further out, from the stall lines in the 2024 photo. The plan draws this lot about 5 m too far out, so its polygon is not used.
- **Trees.** 27 stock MSFS trees at the 2018 DSM crowns on the parcel. Species:
  - Pine stands in for the spruces: the north lot's north row, the trees by 85 Street, and those west of and in front of the chapel.
  - Cypress for the columnar tree at the chapel's east corner.
  - Birch or poplar for the broadleaf trees.

  The shrub island and the plan's shrub beds are left out. The stock trees are not scaled, so their size against the 6 to 19 m crowns is unchecked.
- **Exclusions.** The model footprint plus 4 m, as for every site. A second polygon over the parcel (OSM way 594346540) removes the sim's own trees and buildings there.
- **Status.** Built with exit 0. Not seen in the sim.
