# CYXD Street View photo review (2026-10-18, corrected 2026-10-21, reviewed 2026-10-22)

82 Google Street View screenshots (landside, 2007-2024) are filed in per-building folders. Each folder has a `SOURCES-streetview.md` with the file name, the Street View address, the date and what the photo shows. The Street View address is the nearest address to the camera, not to the subject.

User corrections (2026-10-21) are already applied below: the old `canadian-helicopters-photos/` is Hangar 40; the old "Hangar 9" photos are Hangar 8; the old `hangar37-photos/` are Hangar 38; Hangar 20 is the Esso building; Hangar 39 is the pale-blue double hall (OSM 230718901), with Hangar 40 at its NW end. Building status is in `STATUS.md`; footprints in `hangar-footprints.md`.

## Which photo is which building
| Folder | Photos | Building | Confidence |
|---|---|---|---|
| `hangar3-photos/` | 38-45 | Hangar 3: pale blue ribbed, red/blue stripe under the eaves, big cream roller door with a window band, green-teal window columns, "3" roundel, tan block annex (3 109 St NW) | high (roundel legible) |
| `hangar3-photos/` | 33-37 | Dark-blue gabled hangar with a white gable end, north of Hangar 3 (5 109 St NW) | **unnumbered**, built as is |
| `hangar4-photos/` | 46, 47 | Hangar 4 ("4" roundel) | high |
| `hangar5-photos/` | 48-51 | Hangar 5 ("5" roundel, dark-glass office on the landside) | high |
| `hangar6-7-photos/` | 52, 53 | Hangar 6 (white, small roundel) | medium (roundel too small to read) |
| `hangar6-7-photos/` | 54-56 | Hangar 7 ("7" roundel, window awnings, crest sign) | high |
| `hangar8-photos/` | 57, 59-61 | Hangar 8 ("8" roundel on the tall end block, LAW OFFICE AVIATION sign) | high |
| `hangar11-photos/` | 58, 62-67 | Hangar 11 barrel vault and its white clapboard annex | high |
| `south-of-hangar11-photos/` | 68-70 | Large grey flat-topped metal building south of Hangar 11 (11520 109 St) | **unidentified** (Hangar 12 or 13?) |
| `south-of-hangar11-photos/` | 71, 72 | Tan brick building "11630-109 St" | **unidentified** |
| `hangar14-photos/` | 73-78 | Aircraft and a Bomarc on pedestals along Kingsway | high |
| `hangar14-photos/` | 79-81 | Hangar 14 (museum) long Kingsway side | high |
| `hangar15-photos/` | 0, 1 | Hangar 15 ("15" roundel) and the teal Hangar 16 | high |
| `hangar18-photos/` | 2-6 | Edmonton Flying Club ("18" roundel, club sign) | high for 2-4; 5, 6 are the north end of the group |
| `hangar21-terminal-photos/` | 13, 14 | Old terminal, now Amiskwaciy Academy (1003 / 1012 Airport Rd) | high |
| `hangar22-photos/` | 15 | Parking garage (8603 Flying Club Rd) | high |
| `hangar22-photos/` | 16 | Garage from Airport Rd (145 Airport Rd) | medium |
| `hangar21-terminal-photos/` | 17, 18 | Terminal from Airport Rd | medium |
| `hangar38-photos/` | 19-25 | Hangar 38 (olive-mustard, "38" roundel) | high |
| `hangar39-photos/` | 26-28 | Hangar 39 (pale blue, tall) | high that it is the blue hangar; no roundel in these views |
| `hangar40-photos/` | 29-32 | Hangar 40 ("40" roundel, white with brick office) | high |
| `hangar19-photos/` (7, 8), `hangar20-photos/` (9-11), `hangar22-photos/` (12) | 7-12 | Hangar 19 landside, i.e. the General Aviation Centre at 77 Airport Rd (7, 8); the Esso building (Hangar 20) on Airport Rd (9-11); looking along Airport Rd toward the terminal and its garage (12) | per the user |

## Still unidentified
The large grey flat-topped building south of Hangar 11 (deferred, see `open-questions.md`) and the tan brick building at 11630 109 St. Hangar 9 has no photo.

## Aircraft on pedestals in front of the Alberta Aviation Museum
Three aircraft, not four (the "white jet" past the Norseman in photo 78 is the Voodoo): from the north the Bomarc 60447, the Norseman CF-HPY on a green pylon, a memorial, and the CF-101B Voodoo 101060 on a blue pole. Identified from the museum's collection pages and OSM; the 2026-10-21 photos (`hangar14-photos/frontage/`) cover all of them from several sides. Built as `cyxd_h14_bomarc`, `_norseman`, `_memorial`, `_voodoo` (`tools/display_aircraft.py`, placed at the OSM nodes). Markings are roundels and flag only; pole heights and tilt angles are estimates.

## Old terminal (Hangar 21) and stands
Photos 13 and 14 are the old terminal (OSM way 230718907, 101 Airport Rd). The 2014 Esri imagery shows pale pavement strips at four jetway positions (`footprints/terminal21-stands-overlay.png`). Since then the stands, gates and jetways were rebuilt (`STATUS.md`, Parking); only the terminal, the garage and the NE-face gates 1-4 remain. Jetway origin convention (object heading = parking heading, root 25 m ahead) is unverified in the sim.
