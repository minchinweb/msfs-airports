# CYXD open questions and to-do list

Reviewed 2026-10-22. Current state is in `STATUS.md`; links are in `reference-links.md`. The old `_Next.txt` scratch file is retired (deleted); every link and task from it is in `reference-links.md`, a folder's `SOURCES.md`, or below.

## Questions for the user (they change what gets built)

| # | Question | If answered | Status |
|---|---|---|---|
| 1 | **Gable and door directions of Hangars 4-8.** Assumed: doors and gables on the west (apron) side for 5-8, north for Hangar 4 (reworked to the photos since; still not seen in the sim). | Check in the sim against `hangar4-photos/` to `hangar8-photos/`; change `heading` or builder in `HANGARS`. | open |
| 2 | **Is the white barrel-vault building in the 1956 Northwest Industries photo Hangar 11?** Compared against the 2013 annex photos: fairly solid. | If wrong, rework `hangar11`. | assumed yes |
| 3 | **Was Western GMC in Hangar 6?** The two edmonton.ca images could not be fetched. | Could add GMC lettering to Hangar 6. | open, low priority |
| 4 | **Is Ingenium CAVM-05641 really in Edmonton?** | Use as reference only if it is. | open, not fetched |
| 5 | **Hangar 18 footprint** was hand-traced (not in OSM). | Edit the row in `HANGARS`. | accepted unless told otherwise |
| 6 | **Which signs want real text** (Aviation Museum, Shell, Northwest Industries, Esso, Law Office and the Flying Club are done as textures; the rest are bars)? | Add as texture or letter geometry. | open |
| 7 | **Hangar 9** has no photo and no footprint (the old "Hangar 9" photos are Hangar 8; the model was deleted). Where was it? Nothing on the east line fits (4, 5, 6, 7, 8, 11 with only pavement between). | Add a new model if a spot and photo turn up. | open |
| 8 | **Hudson General hangar number** (`hudson-general-photos/`, provisional folder) and **which building** the TCA "Hanger 2" photo (`hangar2-photos/`) shows. | Refile the photos. | open |

## Not built or not applied yet

1. Hangar 15: adjust the face to the west line-up photo (`west-lineup-photos/flickr_woodhead_13858722704.jpg`).
2. Hangar 16: the box-out at the Aerocentre's SE end and the second stepped-back block are not built; lettering is a bar (see `hangar16-photos/SOURCES.md`).
3. Wind sock: move it to the position seen in the PWA 737 video (YouTube q5-woik2XsQ; Reddit 1ffvw4j). Watch the same videos for building layout and the taxi sign style.
4. A static Pacific Western 737 on the apron.
5. Hangar 14 displays: the black AIR MUSEUM sign is built (position estimated) but not the older blue board; the searchlight and the east-side and airside displays (CF-100, HS.125, Silver Star: OSM nodes near 53.5657, -113.5163) are not.
6. The 1930s first hangar (stucco arch, tower and wing) as its own model; the 1938 hangar is already split off. For the 1938 hangar's door textures use the Fort Edmonton Park replica wedding photos (link in `reference-links.md`).
7. The blue-grey gabled hall at the SE end of OSM 230718900 (formerly part of Hangar 40's way).
8. Not to build (reference only): the 1950s terminal / Administration Building (postcards, 1950 photo); the 1978 sketch buildings until measured.
9. Trans-Canada Air Lines 1938 logo (Ingenium CAVM-17996) for any TCA livery or sign work.
10. Search `Category:Hangars at Edmonton City Centre Airport` on Commons for more photos.
11. **Cement Plant** (the VFR checkpoint VCCMT, N53 35.00 W113 36.00, in `procedures-2010.md`), as a distant landmark. About 5.7 km west-north-west of the tower, so a skyline model, not an airfield building. The west line-up photo shows it on the horizon (silhouette only; use aerials and LiDAR for footprint and heights).
12. The hotels (Edmonton Inn, Chateau Louis) are not modelled; the Chateau Nova hotel is 2005, out of era but present in OSM.
13. **Flashing red obstruction lights** (added 2026-10-22) on the downtown Edmonton buildings near the approach paths and on the nearby NAIT buildings. Not started: pick the buildings under or beside the approaches (from LiDAR or OSM heights), then place flashing red beacons on their roofs.

## Research gaps

- **When did runway 04/22 (03/21) stop operating?** Only bounded: operating in the 1978 On Track guide, gone from the operating set by Edmonton Airports' 1995 plan, absent from the 6 June 2012 aerial. A dated CFS or air photo from 1979-1994 would settle it. Detail: `runway-04-22-closure.md`. It matters for how 04/22 markings, lights and thresholds are modelled.

## Deferred

- **Building south of Hangar 11** (the large grey building, `street-view-review.md`): still shows in the sim as the sim's own generated building; no exclusion or model yet. User deferred it.
- **Hangar 39 in its Pacific Western era:** no period photos of its face found (`hangar39-pwa/README.md`); only the 2014 pale-blue scheme is documented.
- **Front doors of Hangar 3 and the dark-blue hangar north of it:** the apron is held. Hangar 3's airside wall is generic (no photo); the dark-blue hangar's door is assumed to face south; the nearest pavement is 52-107 m away. Needs which wall carries the main doors and where the pavement should join (`HOLD` in `gen_aprons.py`).
- **Aprons for the 1938 hangar and the second ("orange") hangar** along Kingsway: their ENE doors face open ground 107-114 m from pavement, with the terminal, garage and Hangar 20 between. Should they get an apron at all (1930s-1982 buildings), which route would join it, and are the doors on the ENE end? The second hangar is in `HOLD`; the 1938 hangar is not in the table.

## Where did the 1930s first hangar stand? (not known)

Candidate zones are marked on `footprints/first-hangar-candidates.png` (and `-west.png`). Evidence:
- EA-10-1044 shows the first hangar beside the 1938 hangar, its tower and wing on the side facing it. The PC013987 postcard shows a second, larger barrel-vault hangar with a pale two-storey wing and a tower NW of the 1938 hangar. The 1937 plan (amended 1943, `aerials/ualberta-archive-org-1937-WCWdb_2534-general-plan.pdf`) shows one hangar by the circular drive ("No. 3") and two against the west boundary road (121 St): **No. 2 to the north** (3 hazard lights on the roof) and **No. 1 to the south** (labelled "Control Tower"), each with a curved concrete apron; "Compass Swinging Base" and the wind tee lie east of them.
- Positions from the 1944 aerial (which does not fit one transform, so each is anchored locally, +-50 m): the 1938 hangar 53.56988, -113.52510 (built); the second hangar 53.56945, -113.52610 (built, shifted NE); the 1937 plan's No. 2 (red) about 53.573858, -113.530096, 42 x 57 m, door end south; No. 1 (green) about 53.573053, -113.530172, 32 x 34 m, door end north. Both were smaller predecessors on the ground now under Hangars 38 / 39 and are not built. Hangars 38 and 39 are unchanged.
- EA-160-1441 (1933) shows a hangar with a tower beside a road; Hangar No. 1 with its tower is the likely match for the stucco "first hangar". Not proven. Whether the double-tower barrel hangar in EA-10-1044 is No. 2 or the No. 3 by the circular drive is also unsettled.
- To settle it: a georeferenced 1930s-40s aerial, or the 1937 plan scaled against Kingsway.
