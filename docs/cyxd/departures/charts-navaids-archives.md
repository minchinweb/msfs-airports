# Charts, navaids, archives — CYXD

## Navaids (community + OurAirports + sim databases)

| Ident | Type | Freq | Role |
| --- | --- | --- | --- |
| Edmonton range (historical) | 4-course radio range | LF | 1930s–50s airways; one leg over a runway |
| XD | NDB | 266 kHz | Edmonton NDB; OurAirports associates with CYXD; ~N of field |
| ZXD | NDB | 201 kHz | Blatchford locator; ~4–5 NM south; used for NDB 16/34 |
| IXD | ILS/DME | 109.50 | RWY 34; DME ch 032X “EDMONTON MUNI” on-field (airports-worldwide) |
| YEG | VOR-DME | 117.60 | Edmonton International — **not** a CYXD departure navaid until post-1960 enroute |

Nav Canada NAVAID Modernization lists **Edmonton (XD) NDB** for later decommission (after CYXD closed). ZET/ZZD/ZAB are International-area NDBs.

## Airways

- **Amber 2:** Edmonton–north (Staging Route / Yukon / Alaska). Documented in use from Municipal and Namao in the 1950s.
- **Alpha 7** and **Bravo 3** (1984): named in the CASB occurrence report 84-H40006 ([`casb-84-h40006-wapiti-402-alpha7-1984.pdf`](casb-84-h40006-wapiti-402-alpha7-1984.pdf), Wapiti Aviation PA-31-350 C-GXUC, 19 Oct 1984). Wapiti 402 left Edmonton Municipal at 19:10 local, IFR for Peace River via **Alpha 7**, runway 34, **Municipal One** departure, radar-vectored climb to 8,000 ft, abeam the Swan Hills NDB when it asked to descend to High Prairie (MEA 7,000 ft on that stretch of the airway). So Alpha 7 runs north-west from Edmonton towards Swan Hills and Peace River, and the Municipal One departure was still in use in 1984. Pages 1-6 were read (the report is in French and English; the annex A route figure was not checked). Bravo 3 is from the user's reading of the report and has not been checked against the text here.
- Later **Victor** low-altitude structure replaced ranges; first-fix after a radar/on-course departure would be whatever was on the flight plan (e.g. toward YEG, YYC, YMM, YQU). No published “first fix always X” for CYXD.

## Archival catalogues (plates not digitized in this pass)

- Library and Archives Canada: VFR terminal / aeronautical chart fonds (e.g. VTA series from 1970s; Edmonton sheet exists in the national chart program). Radio Facility Charts and Canada Air Pilot are the series that would hold 1960s–80s DPs.
- Internet Archive: 1929 Municipal Airport postcard aerial — no procedure chart. No CAP volume for Edmonton Municipal found on Archive.org in this search.
- Open Government / NRCan atlas samples mention Canada Air Pilot approach/landing charts as a national series (~90 maps historically) — Edmonton Municipal would have been in that set when it was the city’s IFR airport.
- Yumpu: CAP 3, 11 Feb 2010, includes **NDB RWY 16 (GNSS)** for Edmonton City Centre; remaining pages not fetchable (403).

## Runway geometry (late/closed field)

| RWY | True hdg (PilotNav) | Length | Notes |
| --- | --- | --- | --- |
| 12 | 142° | ~5868 ft | Displaced threshold in some databases |
| 30 | 322° | ~5868 ft | |
| 16 | 184° | 5700 ft | Closed 2010 |
| 34 | 364°/000° | 5700 ft | ILS; closed 2010 |

Elevation ~2200–2202 ft. Mag var ~16–17°E in 2006–2010 CAP.

## What can **not** be inferred from IAPs

Missed-approach tracks (typically climb to NDB and hold) are **not** the SID. Do not reverse an IAP and call it a departure without the CAP departure page.

## Physical next steps for the modeller

1. Alberta Aviation Museum / City of Edmonton archives — operations manuals, noise bylaws, old CAP pages.
2. LAC search: “Canada Air Pilot” + Edmonton; “Radio Facility Chart” Edmonton.
3. Purchase or borrow a pre-2013 CAP 3 (library, retired pilots, Nav Canada product archive).
4. If a DAFIF/ARINC 424 cycle from ~2005–2012 is available (military/sim), grep `CYXD4` / `CITY FOUR`.
