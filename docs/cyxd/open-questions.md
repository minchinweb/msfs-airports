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
5. Hangar 14 static displays: Bomarc, Norseman, memorial and Voodoo in front of the museum are modelled (`tools/display_aircraft.py`; not yet built or seen in the sim). Still open: the black AIR MUSEUM sign, the searchlight, and the displays on the east side and airside (CF-100, HS.125, Silver Star: OSM nodes near 53.5657, -113.5163).
6. Split `cyxd_hangar_1938_landmark` into the 1930s first hangar and the 1938 hangar (`hangar1930-photos/SOURCES.md`). For the 1938 hangar's door and door-window textures use the Fort Edmonton Park replica wedding photos (link in `reference-links.md`).
7. General Aviation Centre (77 Airport Road, west side), Canadian Helicopters hangar, and the large red-roofed complex at the north-west (the last is built since 2026-10-21 as the north hangar complex, see STATUS.md; the other two were built earlier). Photos are saved.
8. Not to build (reference only): the old terminal building.
9. Trans-Canada Air Lines 1938 logo (Ingenium CAVM-17996) for any TCA livery or sign work.
10. Search `Category:Hangars at Edmonton City Centre Airport` on Commons for more photos.
11. **Cement Plant** (the VFR checkpoint VCCMT, N53 35.00 W113 36.00, in `procedures-2010.md`), as a distant landmark building. About 5.7 km west-north-west of the control tower, so it is a skyline model, not an airfield building. The west line-up photo `west-lineup-photos/flickr_woodhead_13858722704.jpg` shows it on the horizon (the user's red box in the marked copy): a cluster of tall grey silos and kiln/preheater towers on the ridge, with a white dome at its left. Use the photo for the silhouette only; for the footprint and heights use aerials and LiDAR. Not built yet.

## Research gaps

- **When did runway 04/22 (03/21) stop operating?** Only bounded: still operating in the 1978 On Track guide, gone from the operating set by Edmonton Airports' 1995 plan, and absent from the 6 June 2012 aerial. No NOTAM or council minute found. A dated CFS or air photo from 1979-1994 would settle it. Detail and what was searched: `runway-04-22-closure.md`. Matters for how the 04/22 markings, lights and displaced thresholds are modelled (STATUS.md, "Open questions: Runway 04 alignment").

## Unverified

- None of the ten new hangars has been viewed in the sim. The package builds clean (exit 0, empty `_RPTErrors.xml`). Restart the sim and check them.
- Nothing from this work is committed.

## Deferred (2026-10-21)

- **Building south of Hangar 11** (the large grey building, `street-view-review.md`): still shows in the sim as the sim's own generated building. Put on deferral by the user; no exclusion or model yet.
- **Hangar 39 in its Pacific Western Airlines era**: the search for period photos of its face found none (see `hangar39-pwa/README.md`); only the 2014 pale-blue scheme is documented, and the PWA link rests on the 2014 captions.

## Where did the 1930s first hangar stand? (2026-10-21, not known)
Map of the two candidate zones: `footprints/first-hangar-candidates.png` (2017 imagery, the built 1938 hangar in red). Evidence: EA-10-1044 shows the first hangar beside the 1938 hangar, the first hangar's tower and wing on the side facing it; the PC013987 postcard shows a second, larger barrel-vault hangar with a pale two-storey wing and a tower NW of the 1938 hangar (zone B); the 1937 plan (amended 1943) shows only one hangar by the circular drive ("No. 3", concrete apron). No measurement exists. Needs a georeferenced 1930s-40s aerial or the 1937 plan scaled against Kingsway.

### Update (2026-10-21): hangars placed on the 1944 aerial
The user's coloured boxes on `RG-18-AA-208-27-ac` (blue = built 1938 hangar, orange = second postcard hangar, red and green = unplaced) were converted to lat/lon by a north-up similarity fit: runway 12/30 x 04/22 intersection at pixel (845, 815) of the 2000 px-wide display, 2.11 m/px (from the 16/34 centreline, east 639 m away), registered on the runway centrelines in `CYXD.xml`. Checks: the 1944 terminal/administration site lands within about 15 m of the old terminal (Hangar 21); the green and red boxes land within about 15-35 m of Hangars 38 and 39, so the fit is good to roughly +-35 m.
- **Blue (1938 hangar): the built model was about 133 m too far south.** Moved north (SHIFTS in `gen_buildings.py`) to 53.57075, -113.52550.
- **Orange (second hangar, still standing in 1982, ET-28-900): about 53.570368, -113.526563**, 100 m from Kingsway (Airport Rd), 85 m SW of the 1938 hangar. Not built. It sits under the later Hangar 18 / 19 complex (worth checking whether the Flying Club's green hangar is a re-clad descendant).
- **Red 53.574136, -113.529222 and green 53.573309, -113.529480** are the sites of Hangars 39 and 38. Hangars already stood there in 1944, so they are old buildings later re-faced. EA-160-1441 (1933) shows a hangar with a tower beside a road, which fits the west-boundary road (121 St) there; first-hangar candidate.
- Map: `footprints/first-hangar-candidates.png` (replaces the earlier A / B map).

### Correction (2026-10-21, later): the 1944 aerial does not fit one similarity transform
`RG-18-AA-208-27-ac` is not a clean north-up vertical: the grid streets in it tilt about 5.7 deg, Kingsway about 10.5 deg, and a fit on the runway X and the 118 Ave / Kingsway / 121 St junction disagrees by about 90 m. The "133 m north" move of the 1938 hangar (previous entry) came from the runway-X fit and is withdrawn. Positions are now anchored locally:
- **Blue (1938 hangar):** from the junction (603, 951 on the 2000 px display) with 5.7-10.5 deg and 2.0-2.3 m/px, 53.5698-53.5700, -113.5251 to -113.5253. The model sits at 53.56988, -113.52510 (37 m N, 27 m E of the first placement), uncertainty about +-50 m.
- **Orange (second hangar):** 53.56945, -113.52610 (+-50 m), about 85 m WSW of the 1938 hangar, by Kingsway.
- **Red and green (user: square with the road, south door of red onto 120 Ave extended, green south of it):** placed on the street grid, not the transform. Anchors: 120 Ave = lat 53.57353 (OSM), 121 St centreline = lon -113.53064 at that latitude (read off the 2017 imagery, NOT the OSM node interpolation, which was 48 m out), west wall 15 m east of the centreline. Sizes read off the 1944 roofs at about 2.1 m/px: red 42 m E-W x 57 m N-S, centre 53.573858, -113.530096, door end south (heading 180), south wall 8 m north of the avenue line; green about 32 x 34 m, centre 53.573053, -113.530172, door end north (heading 0), about 36 m south of the avenue line, so between 120 Ave and 119 Ave. Both overlap the built Hangar 38 (which straddles 120 Ave), so they were smaller predecessors on the same ground. Not built.
- Map: `footprints/first-hangar-candidates.png` (and `-west.png`, a crop of the 121 St end).

### Which hangars were red and green? (2026-10-21)
The 1937 plan (amended to 1943, `aerials/ualberta-archive-org-1937-WCWdb_2534-general-plan.pdf`; crop `footprints/plan1937-west-boundary-hangars-1-2.png`) shows two hangars against the west boundary road (121 St), with a curved concrete apron on their east side: **No. 2 to the north (= red)**, labelled "3 hazard lights on roof of hangar", and **No. 1 to the south (= green)**, labelled "Control Tower", each with its own concrete apron. "Compass Swinging Base" and the wind tee lie east of them. That matches the red / green layout from the 1944 aerial and the 120 Ave position. So red = Hangar No. 2, green = Hangar No. 1 (with the control tower), both on the plan's numbering. Not proven: whether either is the 1930s "first hangar" with the crenellated tower (EA-160-1441, 1933, shows a hangar with a tower beside a road; Hangar No. 1 with its tower is the likely match), and whether the double-tower barrel hangar in EA-10-1044 is No. 2 or the one by the circular drive (No. 3 on the plan). The current positions of both are recorded in the entries above. Hangars 38 and 39 are unchanged.

### Northwest Industries: Hangar 11 or the second ("orange") hangar? (2026-10-21)
Compared the 1956 photo (`hangar11-photos/flickr_woodysworld1_11393738936.jpg`) with Hangar 11's surviving annex (2013 photos) and with the orange hangar (postcard PC013987, ET-28-900). The 1956 building has a three-storey white block with ribbon windows and a control cab, a steel fire-escape ladder at the block's end, a low one-storey annex with a dark pitched roof in front, and a white barrel hall behind. Hangar 11 in 2013 has the three-storey white clapboard annex with ribbon windows, the steel fire-escape ladder, and a lower one-storey white annex plus a small shed in front. The postcard hangar instead has a two-storey flat-roofed wing and brick towers at the hall's ends, and the 1982 photo shows no cab or sign. Verdict: Northwest Industries = Hangar 11 (fairly solid); the orange hangar is a different building, owner unknown. Hangar 11's model and signs are unchanged.

### Front doors of Hangar 3 and the dark-blue hangar north of it (2026-10-22)
Apron to their doors is deferred (user: ignore for now). Hangar 3's airside (west) wall is generic in the model (no photo) and its cream roller doors may be on the landside; the dark-blue hangar's roller door is assumed to face south. With either wall on the airside, the nearest pavement is 52-107 m away, so a strip would cross open ground. `tools/gen_aprons.py` lists both in `HOLD`. Needs: which wall carries the main doors, and where the pavement should join.

### Aprons for the 1938 hangar and the other "old" hangar along Kingsway (2026-10-22)
The 1938 barrel-vault hangar (`cyxd_hangar_1938_landmark`) and the second hangar ("orange", `cyxd_hangar_second`) stand along Kingsway Ave and have no apron at their fronts: their ENE doors face open ground 107-114 m from the nearest pavement (apron 5 / the terminal strip), with the terminal, garage and Hangar 20 in between. Questions: (1) should either get a paved apron at all (they are 1930s-1982 buildings; the 1944 aerial and postcard PC013987 may show an apron or just grass), (2) if so, which route joins it to the terminal apron or the taxiway, (3) are the doors really on the ENE end. `tools/gen_aprons.py` lists the second hangar in `HOLD`; the 1938 hangar is not in its table.
