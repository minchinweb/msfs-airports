# Hangar 15 (Centennial Flight Centre) - review 2026-11-03

Street View screenshots in this folder: see `SOURCES-streetview.md`. Model: `hangar15()` and `hangar15_wing()` in `airport-cyxd/tools/gen_buildings.py`. Positions below are in the Hangar 18 frame (u = bearing 138, v = bearing 48, origin 53.568498, -113.519742), the frame `gen_parking.py` uses.

## Sources used
| Source | What it gives |
|---|---|
| OSM way 325232647 (Overpass, as of 2016-01-01) | Footprint of hangar plus wing: hangar u 226.2-281.8, v -23.4-19.6 (43 x 55.6 m); wing v 19.6-36.5, running 5.3 m past the NW gable (u 220.9); NE face 0.7 m further back SE of u 259.5; a small porch at u 223-224.5. Also way 325234438, a small building SW of the SE corner (u 274-293, v -28 to -47). |
| Esri Wayback 2017-05-03 (release 784, z18/z19; not saved) | Post-demolition slab scar: u 227.5-281, NE edge v 35.5, agrees with OSM. The scar's SW edge is at v -17.5, 6 m short of OSM; the landside office strip probably had its own slab. OSM kept. Airport Rd fence at about v -47. |
| Esri Wayback 2014-02-20 (release 10, z17) | Roof u 216-279 with the wing's junction shadow at v 18-19.5. Coarse; used only as a check. |
| Commons `EDMONTON_MUNI_AIRPORT_(15256173388)` (Oct 2014, in `../aerials/`) | From the south: the **main door is in the SE gable** (the "south" face), confirmed. Four grey leaves from about 0.8 m off the NE corner, 22.4 m wide, with a dark glazing strip at about 3.9-4.9 m; plain wall to the SW. The wing's SE end, beside the door, is a **dark-navy door face** under a light parapet band. Gable rise about 3 m. |
| `../aerials/city-edmonton-archives-1982-ET-28-899.jpg`, `-1980ca-ET-28-895.jpg` | Runway face of the wing: low white (later pale-blue) wing, taller middle section with four tall glazed bays between white piers. |
| `../west-lineup-photos/flickr_woodhead_13858722704.jpg` (2014, NAIT parkade) | Runway face: the raised middle section, a round disc just SE of it (the **"15" roundel**; the old model read it as a porthole), one window toward the NW end. |
| `h15-01-streetview-201206.png` (17 Airport Rd), `h15-h16-00-streetview-201206.png` (25 Airport Rd), Commons `EDMONTON_MUNI_(11094252276)` (winter 2013, in `../hangar17-tower-photos/`) | Landside (SW) wall and the NW gable; see below. |
| Commons `EDMONTON_MUNI_(11094254636)` "Centennial flight center hanger" (2013-03-24, not saved) | Interior only (white walls, red trim, steel roof trusses). |

Other Commons files in "Hangars at Edmonton City Centre Airport" and "Edmonton City Centre Airport" were checked (about 35); none shows Hangar 15's runway face closer than the line-up photo.

## Heights
Eave about **9.5 m** (it was 7.6): scaled on the glazed door under the first awning and on a pickup parked at the wall in the 17 Airport Rd view. Grey base 2.6 m (27 % of the wall in the same view). Wing 6.5 m, middle section 8 m: from the 1982 oblique (middle/ends 1.22) and the 2014 line-up photo (hangar wall showing above the wing). The Oct 2014 view makes the wing's SE end look nearly as tall as the hangar eave (0.9); not followed.

## Landside (SW) wall, s = metres from the NW corner
Three views tied by a perspective fit; about +/-1 m up to s 16, +/-3 m beyond.
- **"15" roundel**: high (centre about 8 m), just past the NW corner (s 1.1), about 1.4 m across. It was at s 11, 6.5 m up.
- Ground floor: window s 1.1-2.7; light-grey service door s 3.9-5.8 (about 3.2 m high); **three glazed entrances under blue awnings** at s 11, 27 and 45; windows under the upper ones at s 15.3, 21.5 and 31.5.
- Upper floor: small windows at s 7.3, 15.3, 21.5, 31.5, 39.3 and 46.
- Nothing visible between s 47 and the SE corner.

## NW gable (facing the Shell hangar), s = metres from the SW (landside) corner
- **Cessna board**: a white sign about 1.8 x 2.2 m, high (centre about 7.2 m) at s 7.8, i.e. on the gable just round the corner from the "15" roundel (confirmed by the user). The artwork is too small to read; the texture (`make_signs.py`, `cessna()`) is a generic emblem over "CESSNA".
- Two small upper windows at s 2.5 and 4.8; a floodlight at the corner; a small window (s 6.9) and a side door with a little canopy (s 11) low down.
- A **low grey annex**, 4.4 m high, s 18-32.6, with a door near its NE end. Its depth is not visible; 4.5 m assumed. Not in OSM.

## Runway (NE) face of the wing (u along the wing)
- Raised middle u 244.3-259.5 (8 m, four tall glazed bays, white piers); the "15" disc at u about 262, 4.2 m up; a window at u 235-237; an entry porch at u 223-224.5 (OSM).
- The extra disc on the low SE section (old model) and the "porthole" are gone: they were the same roundel.

## Roundels, summary
Landside: SW wall, high, just past the NW corner. Runway side: the wing's NE face, just SE of the raised section. The disc kept high on the SW part of the SE door gable is **unconfirmed**: every airside view has the museum's roof in front of that spot.

## Fence and car parks
- Fence (user, 2026-11-03: the gap only): chain-link across the gap between the Shell hangar's SE wall and Hangar 15's NW gable at v 12.5, with a 6 m vehicle gate in the middle (in `hangars.py`, with the other fence runs). No photo shows this run; the line is chosen, not traced.
- Car parks (`CAR_PARKS` in `gen_parking.py`): a row against the landside wall in two parts (the middle entrance left clear), an outer row by the lot edge (25 Airport Rd shows both), and the east column between the hangars now stops at the annex.
