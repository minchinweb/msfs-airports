# Hangar 19 photos (General Aviation Centre, 77 Airport Rd)

Added 2026-10-22. Hangar 19 is the General Aviation Centre (confirmed by comparing the Commons photos with Street View, see below).

| File | Source | What it shows |
|---|---|---|
| `EDMONTON_MUNI_11094203585_.jpg` | Wikimedia Commons, 2013-03-24, CC BY 2.0 | Landside front: two-storey red-brown brick, a round tan stair tower with a grey band in the middle, an arched sign "GENERAL AVIATION CENTRE" with a blue airliner above the centre, glazed ground floor with glass doors |
| `EDMONTON_MUNI_11094283326_.jpg` | Wikimedia Commons, 2013-03-24, CC BY 2.0 | The same complex, pink-tan stucco curved entrance with red columns, "77 Airport Rd." in steel letters, "PASSENGER LOUNGE" arrow sign at the left |
| `airport-rd-north-07-streetview-201206.png` | Google Street View, 62 Airport Rd NW, 2012-06 | Esso building at the left, the brick building with the tower behind the sign pylon, low commercial wing to its right |
| `h19-landside-08-streetview-201206.png` | Google Street View, 63 Airport Rd NW, 2012-06 | Brick building with a tower in the centre, a low tan strip with glazed shop fronts to its right; Esso building at the far left |
| `h19-nw-entrance-streetview-201206.png` | Google Street View, 802 Airport Rd NW, 2012-06 (user, 2026-10-22) | The NW end: Esso building, chain-link gate, brick stub wall with an Esso oval, the round entrance facing roughly NW, the NW wing's windows; a big tree in front of the round end |

Street View is copyright Google (reference only, do not redistribute); the Street View photos are also listed in `SOURCES-streetview.md`. The address in a Street View header is the nearest address to the camera.

## Why this is Hangar 19
- Address 77 sits between 69 and the Esso building (83) in the Street View address order along Airport Rd, which is where Hangar 19 stands (SE of the Esso building).
- Street View 07 and 08 (camera at 62 and 63) show, to the right of the Esso building, a two-storey brick building with a tower flanked by a low tan wing with glazed shop-front bays. That is the `hangar19()` layout (brick centre with a tower, two low tan wings).
- OSM has no address for it: the current data has no 77 Airport Rd, only 101 (terminal) and 131.

## Other sources used for the 2026-10-22 model
- **Airside:** the last seconds of the Hangar 18 video (`../hangar18-photos/woodys_11395521785_video.mp4`, from about 9 s; the pan runs NW past Hangar 18). Hangar 19's airside is a two-storey red-brown brick wall with an upper window band and a grey glazed panel, and a one-storey stucco front on the SE part; the arched sign shows over the roof (a second GENERAL AVIATION CENTRE board on the airside wall, user 2026-10-22). Beyond it are the Esso building (tan, dark ribbon, door at its NW end) and the terminal.
- **Plan:** Esri Wayback 2014-02-20 (release 10, only zoom 17 is served here, 0.71 m/px; measuring only, not saved). Rotated front-down, it shows an 83 x 32 m outline: a tall block (long roof shadow) over the NW half and the full depth, an open courtyard with trees in front of it, a one-storey wing in two roof sections to the SE, a short wing NW of the courtyard ending in a round pavilion about 25 m across (the curved "77 Airport Rd." entrance of `EDMONTON_MUNI_11094283326_.jpg`). The 2017 imagery shows the site cleared.
- Street View 07/08, enlarged: the blue "19" roundel sits high at the NW end of the brick block's landside face; a taller round brick stair tower with grey-teal glazing below it stands at the courtyard's SE corner, and a glazed slot at its NW corner; the SE wing has a darker taupe fascia with stepped raised panels and fascia signs over shop fronts with white mullions.
- **Trees** (2026-10-22): crowns in the 2014 aerial (four in the courtyard, a big one in front of the round entrance, a row along Airport Rd), matching the Commons courtyard photo and Street View. They are placed as stock MSFS 2024 trees (birch and poplar from `fs24-asobo-modellib-vegetation`); the GUIDs were read from that package's `bglindex.bout` in the sim's `StreamedPackages` folder (`H19_TREES` in `tools/hangars.py`).
