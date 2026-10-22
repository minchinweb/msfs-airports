# CYXD departures 1941–1978: primary sources + reconstruction

Follow-up to the three notes in this folder. Those concluded that no 1940–1980 departure plate is online. That still holds: **no published departure procedure for Edmonton Municipal/Industrial from 1940–1980 turned up.** In that era Canada handled IFR departures with ATC clearances built on the radio range, and later the NDB, the airways and radar. Graphic SIDs came later. This note collects the era-specific primary data I *did* find. With it you can build departures that match the real geometry.

Everything under "Documented" was read off a scan (links at the bottom). Everything under "Reconstruction" is my inference and is labelled as such.

---

## Era A: radio-range era (1941 – late 1940s)

### Documented

**Aerodrome (RCAF/DoT *Pilots Manual of Aerodromes and Seaplane Bases*, Vol. 2, p. 90, c. 1942)**
- Lat 53°34′N, Long 113°31′W, **Var 25°E**, elevation **2185 ft**
- Runways (all hard-surfaced, 200 ft wide): **3-21** 4500 ft · **11-29** 5700 ft · **15-33** 5700 ft
- "Aerodrome 3.35 miles from R.R. at 61° magnetic"
- "Radio Range 266 KC/S, Identification XD"

**Edmonton radio range (US CAA *Air Navigation Radio Aids*, 1941, p. P-52, "Canadian Radio Facilities")**

| Item | Value |
|---|---|
| Call / freq / ident | VFE · 266 kc · **XD** |
| Range courses (mag) | **173 – A – 240 – N – 340 – A – 95 – N** |
| Station → field | **61° mag, 3.3 mi** |
| Field elevation | 2185 ft |

The 1945 CAA *Flight Information Bulletin* (Cut Bank 5 sheet table) repeats this: XD 266, station-to-field 61°/3.3 mi, class SBRAPZ-DTX, tower 278 kc and 126.18 Mc. The broadcast cycle lists Whitecourt, Edmonton, Penhold and Vermilion.

**Airways / control (US CAA *Airman's Guide*, 1946, p. 149: Edmonton ATC area, effective 1 Oct 1946)**
Edmonton ATC Centre controlled:
- **Green 1** (25 mi W of Cranbrook to 25 mi E of Medicine Hat)
- **Amber 2** (US border to 25 mi W of Watson Lake)
- **Red 6** (Edmonton range to 25 mi E of Edmonton range)
- **all of Red 7**
- traffic within 25 mi of the Lethbridge, Calgary and Edmonton ranges

**Other 1947 facilities (*Airman's Guide* 1947):** An Edmonton GCA radar operated during IFR. The source doesn't say which aerodrome it served. There was also a VHF/DF.

### What the numbers mean (worked out, check me)

The CAA tabulation lists each leg as the **magnetic course flown toward the station**. The check: the field bears 061°M from the station, and that matches the 240° inbound leg (060° outbound) to within 1°. That fits the DoT practice of putting one on-course leg over the airport.

With 25°E variation:

| Leg | Inbound course | Leg lies (from station) | Points toward | Airway |
|---|---|---|---|---|
| North | 173°M | 353°M / **018°T** | Athabasca–Fort McMurray (023°T) | probably Red 7 *(unconfirmed)* |
| East | 240°M | 060°M / **085°T** | **passes over the airfield**; Vermilion (096°T) | Red 6 |
| South | 340°M | 160°M / **185°T** | Penhold 187°T, Calgary 186°T | Amber 2 south |
| WNW | 095°M | 275°M / **300°T** | Whitecourt 296°T, Grande Prairie 300°T | Amber 2 north (Staging Route) |

Quadrants, as I read the table: A between the N and E legs, N between E and S, A between S and WNW, N between WNW and N.

Approximate station position: from your scenery ARP (53.57249, −113.52043), 2.87 NM on 266°T. That gives **N53°34.1′ W113°36.0′**, about 2.9 NM west of the field. This is computed, not surveyed.

### Reconstruction: IFR departure, radio-range era
Not a published procedure. This is how a 1940s ATC clearance would plausibly have used the geometry above.

- **Eastbound (Red 6):** The field sits on the east leg, 2.9 NM from the station. After take-off, intercept the **east leg outbound 060°M** and climb to the assigned altitude.
- **Northwest (Amber 2 to Whitecourt/Grande Prairie/Fort St John):** After take-off, join the east leg **inbound 240°M** and fly to **XD**. Report over the station, then go **outbound on the WNW leg, 275°M**.
- **South (Amber 2 to Penhold/Calgary):** Go to XD as above, then outbound on the **south leg, 160°M**.
- **North:** Go to XD, then outbound on the **north leg, 353°M**.
- Altitudes: the clearance would assign a cruising altitude and probably a "cross XD at or above". Field elevation is 2185 ft, so something like 4000–6000 ft is plausible. **I made these numbers up; no source gives them.**

### Later changes to XD (partly unresolved)
- **1978:** The airport is "157° 3.8 NM from XD NDB". With 23°E variation, that puts XD on the **runway 16 extended centreline, 3.8 NM north of the 16 threshold**. That's where your scenery's XD NDB is (53.6436, −113.5130). The ident and 266 frequency survived, but the site moved.
- Flying the Beams places an XD radio-range site at **N53°39′15″ W113°32′17″**, about 5 NM north of the field. It's taken from a "former DoT radio site" marked on a 1961 topo map. It may be a post-war range site, but I couldn't confirm the dates.

---

## Era B: Edmonton Industrial, 1970s

### Documented (*On Track: the Pilot's Air Travel Guide*, 1st annual edition, 1978, "Edmonton Muni")
- **Var 23°E.** Elevation 2200 ft. All runways 200 ft wide.
- Runways: **03/21** 4451 ft (concrete; area marked "Closed" near the 03 end) · **11/29** 5868 ft (concrete) · **16/34** 5700 ft (asphalt)
- **All thresholds displaced.** My reading of the table: the landing distance on one runway equals the take-off distance on the reciprocal.

  | Landing | ft | Take-off |
  |---|---|---|
  | 03 | 3814 | 21 |
  | 11 | 5068 | 29 |
  | 16 | 5190 | 34 |
  | 21 | 4319 | 03 |
  | 29 | 4681 | 11 |
  | 34 | 5160 | 16 |

- **Right-hand circuits: RWY 21, 29, 34**
- Rotating beacon, windsock. **VASIS RWY 11, 16, 29.** High-intensity runway and approach lights. Approach lights non-standard, 2000 ft.
- **NOISE ABATEMENT, unless otherwise directed:**
  - a) **RWY 16-34 to be used during calm conditions** (no wind)
  - b) **RWY 11 take-off: aircraft gross weight restricted to 12,500 lb**
  - c) RWY 29 landing weight 30,000 lb maximum between 04–14Z (DT 03–13Z)
- "**Consult Edmonton Special Procedures Chart**". This was the local VFR procedures chart. I didn't find a copy online.
- Fuel/FBOs: Brooker-Wheaton (Hangar 8), Aero Aviation Centre (Hangar 12, private advisory "Aer Radio" 119.1), Esso Aviation. Customs available on request.

**City context**
- 1973: the City and MOT agreed which carriers would serve Industrial vs International with aircraft over 12,500 lb. That's the same weight threshold as the RWY 11 take-off rule. (Council minutes, 13 Aug 1973)
- 1984: the Municipal Airport Noise Policy Study asked Transport Canada to amend the *Canada Air Pilot – West* to make **RWY 30 the preferential noise-abatement departure runway** (12 for arrivals). It also asked for formal noise-abatement take-off procedures to be added to the CAP. That suggests no preferential departure runway or noise take-off procedure was in the CAP before then, beyond the 1978-style rules above. (Council minutes, 9 Oct 1984)

### Reconstruction: 1970s IFR departure (vector style)
Again, not a published procedure. It's built from the documented rules plus geography. Magnetic headings use 23°E and your scenery's true headings: 11/29 = 115°/295°M, 16/34 = 157°/337°M, 03/21 = 035°/215°M.

- Clearance: "...via radar vectors, climb runway heading, maintain [altitude], departure frequency [x]". The late-era Edmonton Terminal departure frequency in your data is 119.5. **I couldn't confirm it for the 1970s.**
- **RWY 29:** The natural IFR departure runway for anything over 12,500 lb when the wind allows, because 11 is weight-restricted. Climb on runway heading (≈295°M), then vectors.
- **RWY 34 / 16:** Used in calm wind. A 34 departure points at **CFB Edmonton (Namao), only 6 NM away on 018°T**. Expect an early ATC turn or a restriction. That's my inference; it isn't documented.
- **RWY 11:** Light aircraft only (≤12,500 lb). It climbs out toward downtown.
- **VFR departures:** The circuit pattern keeps traffic **north of 11/29, east of 16/34 and northwest of 03/21**, so plan turn-outs to those sides.
- **If no SID or vector is assigned:** the modern Canadian default is to climb runway heading to 400 ft AGL before turning, then on course. **The exact 1970s wording may differ.**

---

## Model notes that bear on departures (your scenery XML)

- Runway numbers for the target era: **3-21 / 11-29 / 15-33** in the 1940s; **03/21 / 11/29 / 16/34** in the 1970s. The scenery currently uses 04/22, 12/30, 16/34, which match the 16°E variation of the 2000s.
- In the scenery, the 04/22 circuits are on the **southeast** side (primary RIGHT, secondary LEFT). In 1978 they were on the **northwest** side (03 left-hand, 21 right-hand). 12/30 and 16/34 already match 1978.

---

## Still not found / where to look next
- HathiTrust full-text search can find Canada Air Pilot and DoD terminal volumes, but it sits behind a human-verification page I couldn't pass. Worth running yourself, e.g. `"Edmonton Industrial"`, `"Edmonton Municipal" range`.
- Library and Archives Canada: *Canada Air Pilot* volumes from the 1950s–70s, and the *Edmonton Special Procedures Chart*.
- City of Edmonton Archives: RG-11-4 (Commissioners: Transportation, 1926–1971) and RG-50-4 (Engineer's Dept. reports, to 1982) may hold DoT/MOT correspondence about procedures.
- Old Jeppesen Edmonton Industrial pages on eBay or from retired pilots. The Alberta Aviation Museum is on the old field.

## Images
- [`../aerials/c1942-RCAF-415.011-2AOS-16EFTS.jpg`](../aerials/c1942-RCAF-415.011-2AOS-16EFTS.jpg): oblique aerial of the wartime field, looking north-ish over the three runways with the BCATP schools (No. 2 AOS / No. 16 EFTS) and hangar lines. National Defence image #415.011, via rcaf.info (shared there by Mike Anglin).
- [`rcaf-manual-of-aerodromes-edmonton-p90.jpg`](rcaf-manual-of-aerodromes-edmonton-p90.jpg): RCAF/DoT *Pilots Manual of Aerodromes and Seaplane Bases*, Vol. 2, p. 90. Location map plus runway diagram (3-21, 11-29, 15-33), the wind tee and beacon positions, and the radio range note. Via rcaf.info. Already in `docs/cyxd`; the extra copy was the same page.
- [`rcaf-on-track-1978-page1.jpg`](rcaf-on-track-1978-page1.jpg): *On Track* (1978), page 1. Noise abatement block: calm-wind use of 16-34, 12,500 lb take-off cap on runway 11, 30,000 lb landing cap on runway 29. Via rcaf.info.
- [`rcaf-on-track-1978-edmonton-muni-2.jpg`](rcaf-on-track-1978-edmonton-muni-2.jpg): *On Track* (1978), page 2. Aerial photo plus aerodrome diagram showing taxiways, displaced thresholds, tower, the XD bearing line (157° / 3.8 NM), and variation 23°E. Via rcaf.info. Already in `docs/cyxd`.
- [`../charts/procedures-2010/cfs-b230.png`](../charts/procedures-2010/cfs-b230.png), [`../charts/procedures-2010/cfs-b231.png`](../charts/procedures-2010/cfs-b231.png), and [`../charts/procedures-2010/2008-CFS-CYXD-B230-B231.pdf`](../charts/procedures-2010/2008-CFS-CYXD-B230-B231.pdf): Canada Flight Supplement pages B230–B231, effective 20 November 2008–15 January 2009. B231 is the preferential-runway departure (climb runway heading to 3,200 / 4,500 / 4,000 ft ASL). Extracted from the IVAO copy of CFS_AD_E.pdf. The page footer on B231 reads issue 159, 20 November 2008. The full directory PDF is `../charts/procedures-2010/CFS_AD_E-ivao.pdf`.

No image of the Edmonton Special Procedures Chart was found. The 11 February 2010 City FOUR departure and the approach plates are in `../procedures-2010.md`, with the images under `../charts/procedures-2010/`. The IVAO CAP 3 link for CYXD (`charts.www.ivao.ca`) no longer resolves, and it is not in the Wayback Machine.

These are copyrighted, Crown, or NAV CANADA pages, kept here for personal reference only. Don't ship them in the package.

## Sources
- RCAF Station Edmonton Municipal, rcaf.info (images of the c.1942 RCAF manual page and the 1978 *On Track* pages): https://rcaf.info/rcaf-stations/alberta-rcaf-stations/rcaf-station-edmonton-municipal/
- US CAA, *Air Navigation Radio Aids* (1941), p. P-52: https://books.google.ca/books?id=cuRGAQAAIAAJ&pg=RA9-SL16-PA52
- US CAA, *Flight Information Bulletin* (1945), Cut Bank 5 sheet: https://books.google.ca/books?id=sfBGAQAAIAAJ&pg=RA8-PA6
- US CAA, *Airman's Guide* (1946), p. 149: https://books.google.ca/books?id=fGMkiDRAWhUC&pg=RA4-PA149
- US CAA, *Airman's Guide* (1947), GCA note: https://books.google.ca/books?id=YCGGjPalI7cC&pg=RA16-PA49
- Flying the Beams, LF radio range map (Edmonton XD entry): https://flyingthebeams.com/map
- City of Edmonton Archives, Council Meeting No. 24, 13 Aug 1973: https://cityarchives.edmonton.ca/meeting-no-24-64
- City of Edmonton Archives, Council Meeting No. 23, 9 Oct 1984: https://cityarchives.edmonton.ca/meeting-no-23-74
