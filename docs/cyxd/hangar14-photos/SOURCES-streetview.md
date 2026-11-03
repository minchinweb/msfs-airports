# Street View photos (landside), added 2026-10-18

Screenshots from Google Street View (copyright Google; reference only, do not redistribute). They came from `docs/cyxd/_unsorted photos`; the original screenshot name and its index (0-81, sorted by name) are in the last columns. The address is the one in the Street View header, i.e. the nearest address to the camera, not necessarily to the subject.

| File | Address | Date | What it shows | Original | Idx |
|---|---|---|---|---|---|
| pedestal-aircraft-73-streetview-202406.png | 11294 Kingsway NW | 2024-06 | Aircraft on pedestals beside Kingsway in front of the Alberta Aviation Museum | Screenshot 2026-10-17 201902.png | 73 |
| pedestal-aircraft-74-streetview-201210.png | 11294 Kingsway NW | 2012-10 | Aircraft on pedestals beside Kingsway in front of the Alberta Aviation Museum | Screenshot 2026-10-17 201920.png | 74 |
| pedestal-aircraft-75-streetview-201206.png | 11340 Kingsway NW | 2012-06 | Aircraft on pedestals beside Kingsway in front of the Alberta Aviation Museum | Screenshot 2026-10-17 201943.png | 75 |
| pedestal-aircraft-76-streetview-201408.png | 11340 Kingsway NW | 2014-08 | Aircraft on pedestals beside Kingsway in front of the Alberta Aviation Museum | Screenshot 2026-10-17 201958.png | 76 |
| pedestal-aircraft-77-streetview-201408.png | 11342 Kingsway NW | 2014-08 | Aircraft on pedestals beside Kingsway in front of the Alberta Aviation Museum | Screenshot 2026-10-17 202018.png | 77 |
| bomarc-sign-78-streetview-201906.png | 11416 Kingsway NW | 2019-06 | White Bomarc missile on a base, blue AIR MUSEUM sign, floatplane on a pole beyond | Screenshot 2026-10-17 202036.png | 78 |
| h14-kingsway-79-streetview-201906.png | 11416 Kingsway NW | 2019-06 | Hangar 14 long Kingsway side: white siding, regular window grid, big arched glazed doors at the end (80) | Screenshot 2026-10-17 202054.png | 79 |
| h14-kingsway-80-streetview-201207.png | 11416 Kingsway NW | 2012-07 | Hangar 14 long Kingsway side: white siding, regular window grid, big arched glazed doors at the end (80) | Screenshot 2026-10-17 202111.png | 80 |
| h14-kingsway-81-streetview-201207.png | 11436 Kingsway NW | 2012-07 | Hangar 14 long Kingsway side: white siding, regular window grid, big arched glazed doors at the end (80) | Screenshot 2026-10-17 202130.png | 81 |

## Frontage set, added 2026-10-21 (`frontage/`)
Fourteen more Street View screenshots (Kingsway NW, May 2023, Jun 2024 and Oct 2022; original names kept): the Bomarc 60447 (pedestal, rail, roundels, flag on the fins), the Norseman CF-HPY (cream-yellow, mint cowl and wingtips, silver floats, green C-shaped pylon, green cut-out fir trees), the Voodoo 101060 (side, three-quarter and underside, blue C-shaped pole) and the memorial (stone block with plaque on a round pad, three flagpoles). There are three display aircraft, not four: the "white jet" in photo 78 is the Voodoo seen past the Norseman. Order from the north: AIR MUSEUM sign, Bomarc, Norseman, memorial, Voodoo.
Models: `airport-cyxd/tools/display_aircraft.py`, placed at the OSM nodes (`historic=aircraft` / `monument`).

## Review, 2026-11-03

Aerials: Esri Wayback release 43291 (2026-10, zoom 19) and release 784 (2017-05, zoom 19), measured in the airport frame (x east, y north). The 2017 image sits about 1.5 m east and 1.5 m north of the 2026 one; the 2026 one matches the OSM display nodes (the memorial to 0.5 m), so traces use it.

- **Footprint:** the roof is 82 m east-west, not 90.8 m (OSM): west wing strip 6.2-6.9 m, hall 69-69.5 m, east lean-to 5.4-6.7 m. North-south is 99.5 m (OSM 100). The user agreed to narrow the model; the south-face bays are scaled from the old 80.8 m hall. The model's centre (hall + wing) is now x 215.6, y -751.7.
- **Ladder:** the roof ladder is on the wing's west wall, about 4.5 m from the south corner, from the lean-to ledge to above the eave (frontage/210410).
- **Flags:** the memorial flies the Canadian flag on the Kingsway (SW) side, the Alberta flag on the NW and the RCAF ensign on the E (user; poles placed from 211225 and 211249). The Voodoo's fin carries the Canadian flag (211150, confirmed). The Bomarc's tail fin carries a Canadian Red Ensign, upright with the canton at the top outer corner (210410, 210624, the Commons photo); the user's "northern plane". The Norseman CF-HPY shows no flag. Roundels on the Bomarc and the Voodoo have the red maple-leaf centre. Textures: `tools/assets/flags_sign.png` (`make_signs.flags`).
- **Fir trees** (round the Norseman): each is a tall square pyramid of four green sheet-metal panels with tiered edges, about 1.2 m square and 4 m tall, on four short splayed legs (210501, 211207, 211358 show two panels meeting on a hip). They were single flat boards; `display_aircraft.fir_tree` now builds the four panels.
- **Fence** (`display_aircraft.FENCE_RUNS`, traced on the aerials): the north yard's north fence at y -672.6 from x 189 to 273, a cut NE corner, the east fence at x 281 outside the aircraft strip down to Kingsway, then the perimeter fence turning SE along Kingsway (only 20 m built). The west-yard fence runs from the north yard's NW corner SW along the neighbouring lot, then SE to the museum's west wall by its SW corner. A 3.6 m tie joins Hangar 15's south corner (which the 2017 slab scar puts just north of the fence) to the north fence. The museum, its yards and the front lot are all landside.
- **Car parks:** eight rows from the painted stalls on the 2026 aerial (single west column, double column, the columns either side of the planted median, a double column, the long column inside the east fence). The 2011 Commons photo shows an older layout with cars nose-in on a grass-edged row by the building.
