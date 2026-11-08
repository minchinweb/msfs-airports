# Street View photos (landside), added 2026-10-18

Screenshots from Google Street View (copyright Google; reference only, do not redistribute). They came from `docs/cyxd/_unsorted photos`; the original screenshot name and its index (0-81, sorted by name) are in the last columns. The address is the one in the Street View header, i.e. the nearest address to the camera, not necessarily to the subject.

| File | Address | Date | What it shows | Original | Idx |
|---|---|---|---|---|---|
| h40-29-streetview-201004.png | 12039 121 St NW | 2010-04 | Hangar 40: white ribbed metal building with a brick-red office block, red awnings and a "40" roundel on a taller white block | Screenshot 2026-10-17 200249.png | 29 |
| h40-30-streetview-201004.png | 12043 121 St NW | 2010-04 | Hangar 40: white ribbed metal building with a brick-red office block, red awnings and a "40" roundel on a taller white block | Screenshot 2026-10-17 200316.png | 30 |
| h40-31-streetview-201004.png | 12043 121 St NW | 2010-04 | Hangar 40: white ribbed metal building with a brick-red office block, red awnings and a "40" roundel on a taller white block | Screenshot 2026-10-17 200335.png | 31 |
| h40-32-streetview-201206.png | 12043 121 St NW | 2012-06 | Hangar 40: white ribbed metal building with a brick-red office block, red awnings and a "40" roundel on a taller white block | Screenshot 2026-10-17 200405.png | 32 |

## Also Hangar 40 (2026-10-21)
| File | Source | What it shows |
|---|---|---|
| `flickr_woodhead_13207130405.jpg` | Flickr woodhead 13207130405 (moved from `canadian-helicopters-photos/`; the user confirmed it is Hangar 40, Canadian Helicopters) | Two-storey red-brick office wing with a red fascia, a glass-block entrance with a white gabled canopy, a red awning, next to a grey ribbed hangar wall. Matches the brick office in photos 29-31 |

## Review, 2026-11-03

Aerials: Esri Wayback release 784 (2017-05, zoom 19) and release 10 (2014-02, zoom 17) agree to about 1 m. By 2026 the site is cleared.

- **Plan:** there are three masses side by side, all on one NE (airside) face. From the NW they are: a flat-roofed white block (white membrane roof, 29.0 m wide, 36.7 m deep); the brick office (12.7 m wide, its front flush with the white block's); and a gabled hall with a pale-blue roof (31.0 m wide, 51.4 m deep). The hall's ridge runs SW-NE, and its SW gable end stands 14.7 m forward of the office. Photo 29 shows that end's side wall beside the entrance, with the "40" roundel just inside its NW corner. The old model had two equal gabled halls 46 m deep, with the SE one only 3.5 m forward.
- **Office front** (Flickr, photo 29): from the SE end, a glass-block panel, the door under the white gabled canopy, then a glass-block panel under a red awning, more brick, and a second red awning over glass blocks by the white block. It has three first-floor windows and a red fascia.
- **White block:** photo 31 shows two window pairs and doors on its SW face, and doors with small canopies and a high louvre on its NW face. The roof units and stacks are from the 2017 aerial.
- **Flags:** the Canadian flag flies on a pole over the office, and the Alberta flag on a bracket at the white block's front (photo 29).
- **Car park:** the oval lot on 121 St between Hangars 40 and 38 (user), west of Hangar 39, gets four columns placed on the painted stalls from the 2017 aerial (`gen_parking.py`). In 2014 it had buses parked across it. Not built: the row along the hall's SE side facing Hangar 39 (2014).
- **Fence (2026-11-07):** the fenced lot of photo 31 is the lot NW of the white block (cars in 2010, empty in 2017). Its fence against the yard and the helicopter apron is in `cyxd_west_fence` (`display_aircraft.py`), and so is Hangar 39's yard fence along Hangar 40's hall.
- **Airside:** the 2017 aerial shows four yellow painted helicopter pads, each an outer ring with an inner one. Three small ones (about 8 m radius) stand in a column off the white block's NW corner, 16, 37 and 57 m out from the door wall. A big one (about 12 m) is 45 m out in front of the office. They are now four helicopter stands (P11-P14).
  - **Removed:** the two medium stands at the doors and the jet stand 64 m out. The jet stand sat between both connectors with its wings reaching into each.
  - **Connections:** the column joins a hand-placed 8 m heli lane in `CYXD.xml`, from node 120 on taxiway A toward the white block, so no connector crosses another pad. The big pad joins taxiway A at node 122.
  - **Apron:** the pavement runs about 16 m past the white block's NW wall. `gen_parking.py` now adds an apron strip there, because the generated door apron stopped at the wall line and left the pads on grass.
  - **Unchanged:** taxiway A (30 m, on the old pavement strip NE of the apron) matches the aerial and is left alone.
- **Landside roundel:** the elevation render shows "40" reversed only because `elev.py` draws the raw glTF, before the sim's X flip. Hangar 20's "20", already checked in the sim, renders as "05" in the same tool.
