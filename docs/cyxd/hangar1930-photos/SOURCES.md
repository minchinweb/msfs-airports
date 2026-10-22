# CYXD first hangar (c.1929-31, Edmonton Municipal Airport) - reference photos

Saved 2026-10-10. The "first hangar" is the stucco arched-front hangar with the crenellated three-storey tower and the long office wing, as seen in 1931.

| File | Source | Credit / licence | Notes |
|---|---|---|---|
| `imperial_oil_airshow_25913346198.jpg` | https://commons.wikimedia.org/wiki/File:Imperial_Oil_Airshow_at_the_Edmonton_Municipal_Airport,_Alberta_(25913346198).jpg | Provincial Archives of Alberta BL87.1, 1931, "No restrictions" per Commons | **Best view.** Straight-on front, 1931. Biplanes parked in front of the open hangar; the tower, wing and a small outbuilding to the right; a Fokker-type monoplane (CF-AII) at right. |
| `woodys_11097736705.jpg` | https://www.flickr.com/photos/woodysworld1778/11097736705/in/album-72157638139255574 | woodysworld1778 (Flickr; licence not checked), 1024 px. Title: "EDMONTON AIRPORT 1931 --- FIRST HANGAR DIFFERENT ANGLE VIEW" | Three-quarter view from the right: tower, then the long wing, with its hip-roofed two-storey end pavilion with a dormer and a chimney. Model T cars parked in front. The windsock is limp on a mast above the hangar. |
| `woodys_11097770775.jpg` | https://www.flickr.com/photos/woodysworld1778/11097770775/in/album-72157638139255574 | woodysworld1778 (Flickr; licence not checked), 1024 px. Title: "EDMONTON AIRPORT 1931 --- THE FIRST HANGAR" | Front view from the field, with striped awnings on the tower windows. |
| `woodys_11097950423.jpg` | https://www.flickr.com/photos/woodysworld1778/11097950423/in/album-72157638139255574 | woodysworld1778 (Flickr; licence not checked), 1023 px. Title: "EDMONTON AIRPORT 1933 --- THE WINNIE MAE 1933" | Wiley Post refuelling the Winnie Mae from an Imperial Oil tanker truck, July 1933. Background from the other side: tower at the left with a flag, a long tile-roofed two-storey wing with a chimney and dormers, the arched hangar at the right end with tall openings. The tower here stands at the far end of the wing from the hangar, which is a different layout from the 1931 front views (see below). |

## What the photos show
- **Hangar:** pale stucco, front wall rising in a **segmental-arch parapet** with four diamond ornaments; a low-pitch shingled roof is visible behind it on the right, so the arch is probably a false front rather than a true barrel vault. A huge open front (almost the full width, about 6 m high) with a tall braced timber door leaf folded at each end; tall multi-pane windows in the back wall; solid piers at each end with a floodlight on top (no tower at the left end).
- **Tower:** square, three storeys plus a crenellated parapet with small pinnacles at the corners and lamps/floodlights; windows in pairs per floor, striped canvas awnings on the upper two floors and flower boxes under some windows; flag mast on top. It stands directly against the hangar's right end, flush with the front.
- **Wing:** a long low wing continues to the right (single storey with a row of windows and a low roof) ending in a taller **two-storey pavilion with a hipped tile/shingle roof, dormer and chimney** (control/observation room and club space). A small separate shed stands further right.
- **Details:** floodlights on curved gooseneck poles all along the roof edges and the tower; a windsock on a tall mast at the ridge of the hangar; all stucco walls pale cream/grey; a wire-and-post fence along the field edge in the foreground.

## Is it already in place? No (as far as I can tell)
The generator (`hangar_1938` in `tools/gen_buildings.py`, placed as `cyxd_hangar_1938_landmark`) is described as "the 1938 arched hangar + main tower + small tower + office wing". That model is a **merge of two different buildings**:
- The City of Edmonton Archives photos EA-160-1331 and EA-160-1332 (labelled 1937; the "1937 office wing" source) show the **first hangar** with its tower and wing, matching the photos above. EA-10-1044 (1930) shows it at the left, with the **later arched hangar** (a domed roof between two towers) standing to its right.
- EA-160-398 and EA-160-402 (1938; the latter under construction) show the **new hangar**: a true barrel vault between **two towers** (one at each end) and, in the scaffold photo, a long barrel-roofed block to the right.
So the main tower and the 30 x 13 m wing in our landmark model belong to the first hangar, while the barrel vault and the small tower belong to the 1938 hangar.

## Changes to make when we build it
1. **Split the landmark** into two models: (a) the first hangar, tower and wing; (b) the 1938 barrel-vault hangar flanked by its two towers. Put each at its own position (from the 1930 photo EA-10-1044 the first hangar stands to the left (west) of the 1938 one, a hangar-width or so apart) and check both against the 1944 aerial.
2. **First hangar hangar part:** stucco cream walls (not the grey `METAL` the landmark uses), arched false-front parapet with diamonds, a low roof behind it, wide open front with a folded door leaf at each end, solid end piers, no tower at the left end.
3. **Tower:** much lower than the landmark's 22 m / 5 storeys: three storeys (about 12-14 m) with a crenellated parapet and corner pinnacles, paired windows, striped awnings.
4. **Wing:** a long single-storey wing ending in a two-storey hip-roofed pavilion with a dormer and chimney, not a plain 30 x 13 m two-storey gable box.
5. **Remove the "small tower at the hangar's left front corner"** from the first-hangar model; it belongs to the 1938 hangar (two towers).
6. **Lights and windsock:** add floodlights on gooseneck poles and a windsock mast on the ridge.
7. **Era:** a pre-1931 building; check from the 1944 aerial and later photos when it was removed before deciding whether to keep it in the 1940-1985 scenery.
8. **Open questions:** the 1933 Wiley Post photo shows the tower at the far end of the wing from the hangar, which does not match the 1931 front views; it may be a later change or a different view, so check it before fixing the wing's side. Orientation (mirror) of the existing landmark was never checked in-sim.

## City of Edmonton Archives photos (added 2026-10-22)
Moved from `City of Edmonton Archive photos/`; the date is in the file name, the archive ID after it. Reference only; do not redistribute.
- `city-edmonton-archives-1930-EA-10-1044.jpg`: this hangar with its tower at the left, the later arched hangar between two towers at the right.
- `city-edmonton-archives-1932-EA-160-1688.jpg`: front of the arched hangar and tower from the field.
- `city-edmonton-archives-1933-EA-160-1441.jpg`: aerial; the hangar and tower beside the road at the edge of the field.
- `city-edmonton-archives-1935-EA-10-2770.jpg`: night view with floodlights, tower and wing at the right.
- `city-edmonton-archives-1937-EA-160-1331.jpg` and `-1332.jpg`: tower, wing and hangar front.
- `city-edmonton-archives-1939-06-02-EA-160-1798.jpg`: a crowd and an airliner in front of the hangar and tower.

## Moved from `historical-unknown-photos/` (2026-10-22)
- `flickr_woodysworld1_11394759225.jpg` (Flickr, woodysworld1778; licence not checked): view across the apron from a stucco pier, probably this hangar's tower. Biplanes CF-CBN / CF-CBX / CF-BDW and three Lockheed 10-type airliners (so 1937 or later). In the distance, a two-storey wing with a white arched hangar front at its right end, possibly the 1938 hangar (`../hangar1938-photos/`); not confirmed.
