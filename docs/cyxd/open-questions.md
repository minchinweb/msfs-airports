# CYXD open questions and to-do list

Kept here so it can be queried later. Dated 2026-10-13. This file and `reference-links.md` replace the old `_Next Steps.txt` scratch file, which can be deleted: every link and note from it is in `reference-links.md` or a folder's `SOURCES.md`, and every task is below.

## Questions for the user (they change what gets built)

| # | Question | If answered | Status |
|---|---|---|---|
| 1 | **Where was Hangar 9?** The east line runs 4, 5, 6, 7, then 8, then 11, with only pavement and parking between them in the 2014 imagery and the 2016 OSM data. The model `cyxd_hangar9` is built but not placed. | Set `HANGAR9_PLACEMENT = (lat, lon, heading)` in `airport-cyxd/tools/hangars.py`, regenerate, rebuild. | open |
| 2 | **Is Hangar 38 the SW building and 39 the NW building** of the 121 St group? Chosen from photo angles (`hangar39-photos/SOURCES.md`). | If backwards, swap the two rows in `HANGARS` in `hangars.py`. | open |
| 3 | **Gable and door directions of Hangars 4-8.** Assumed: doors and gables on the west (apron) side for 5-8, north for Hangar 4. User said only that both gables in the 6/7 photo run to the left of the picture, orientation unknown. | Check in the sim against the photos in `hangar4-photos/` to `hangar8-photos/`; change `heading` or builder in `HANGARS`. | open |
| 4 | **Which end of Hangar 8 has the tall block** (with the "8" roundel)? Assumed. | As above. | open |
| 5 | **Is the white barrel-vault building in the 1956 Northwest Industries photo Hangar 11?** User was "pretty sure"; it was modelled that way (it fits the arch shadow and the annex). | If wrong, rework `hangar11`. | assumed yes |
| 6 | **Was Western GMC in Hangar 6?** User's note ended in a question mark; the two edmonton.ca images could not be fetched. | Could add GMC lettering to Hangar 6 if confirmed. | open, low priority |
| 7 | **Is Ingenium CAVM-05641 really in Edmonton?** The photo claims to be; unconfirmed. | Use as reference only if it is. | open, not fetched |
| 8 | **Hangar 18 footprint** was hand-traced (not in OSM). Accept it, or give a better outline? | Edit the row in `HANGARS`. | accepted unless told otherwise |
| 9 | **Signs and lettering** on the new hangars are only suggested with plain bars. Which ones want real text (Aviation Museum, Shell, Northwest Industries)? | Add as texture or letter geometry. | open |
| 10 | **Status line.** The `/statusline` request never got an answer on what it should show. | | open |

## Not built or not applied yet

1. Hangar 15: adjust the face to the west line-up photo (`west-lineup-photos/flickr_woodhead_13858722704.jpg`).
2. Hangar 16 rebuilt 2026-10-17 (five-bay Aerocentre with the angled entrance, repositioned Shell hangar, north block, landside wing, new Shell pecten); still to check in the sim: the front offset between the Aerocentre and the hangar, and the SE-end box-out (not built). See `hangar16-photos/SOURCES.md`.
3. Wind sock: move it to the position seen in the PWA 737 video (YouTube q5-woik2XsQ; Reddit 1ffvw4j). Watch the same videos for building layout and the taxi sign style.
4. A static Pacific Western 737 on the apron.
5. Hangar 14 static displays: the aircraft mounted in front of the museum and the displays on its east side. Bomarc and searchlight photos are in `hangar14-photos/`.
6. Split `cyxd_hangar_1938_landmark` into the 1930s first hangar and the 1938 hangar (`first-hangar-photos/SOURCES.md`). For the 1938 hangar's door and door-window textures use the Fort Edmonton Park replica wedding photos (link in `reference-links.md`).
7. General Aviation Centre (77 Airport Road, west side), Canadian Helicopters hangar, and the large red-roofed complex at the north-west. Photos are saved.
8. Not to build (reference only): the old terminal building.
9. Trans-Canada Air Lines 1938 logo (Ingenium CAVM-17996) for any TCA livery or sign work.
10. Search `Category:Hangars at Edmonton City Centre Airport` on Commons for more photos.

## Research gaps

- **When did runway 04/22 (03/21) stop operating?** Only bounded: still operating in the 1978 On Track guide, gone from the operating set by Edmonton Airports' 1995 plan, and absent from the 6 June 2012 aerial. No NOTAM or council minute found. A dated CFS or air photo from 1979-1994 would settle it. Detail and what was searched: `runway-04-22-closure.md`. Matters for how the 04/22 markings, lights and displaced thresholds are modelled (STATUS.md, "Open questions: Runway 04 alignment").

## Unverified

- None of the ten new hangars has been viewed in the sim. The package builds clean (exit 0, empty `_RPTErrors.xml`). Restart the sim and check them.
- Nothing from this work is committed.
