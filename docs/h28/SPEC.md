# H28 / CEQ4: Whetstone International (Del Bonita) spec

Draft started 2026-10-27. Status: **open questions are marked `DECISION`**. Nothing is built yet.

Planned project: `airport-h28/airport-H28-del-bonita-whetstone-intl.xml`, package `cardboardgt-airport-h28-whetstone`, source `airport-h28/PackageSources/Scenery/airport-h28/H28.xml`. Handoff notes will go in `docs/h28/STATUS.md`.

## Facts gathered so far

| Item | Value | Source |
|---|---|---|
| Name | Whetstone International (Del Bonita/Whetstone Intl) | FAA, Wikipedia |
| Identifiers | FAA LID **H28**; Transport Canada **CEQ4**; no ICAO or IATA code | Wikipedia |
| Owner and operator | State of Montana, MDT Aeronautics Division | AirNav |
| Elevation | 4,336 ft (1,321.6 m) | AirNav, OurAirports |
| Runway | 07/25, turf, 4,440 x 65 ft (FAA); CFS also quoted as 4,401 ft | AirNav, Wikipedia |
| Markings | thresholds: double cones; edges: white cones every 200 ft | AirNav (FAA) |
| Fences | 4 ft fences, 44 ft left and right of centreline, full runway length | AirNav (FAA) |
| Obstruction | Rwy 7: power line 31 ft high with **red marker balls**, 205 ft from the threshold, 70 ft right of centreline | AirNav (FAA) |
| Lighting | none (MDT conditions list) | MDT |
| Pattern | left traffic, both runways | AirNav |
| CTAF | 122.8 | AirNav |
| Wind indicator | yes; no segmented circle | AirNav |
| Other | unattended, no fuel, no snow removal, gopher holes; customs both ways (CBSA airport of entry, 15 pax max); tiedowns on both sides of the border | AirNav, Wikipedia, MDT |
| Instrument procedures | none | AirNav |
| Nearby navaids | CTB VOR/DME 113.35 (309 R, 31.6 nm); YQL VOR/DME 115.7 (176 R, 38.4 nm) | AirNav |
| Magnetic variation | 18 E on the FAA record (1985 epoch); about 13-14 E today (to be checked) | AirNav |

### Where things are (WGS84)

| Feature | Lat, lon | Note |
|---|---|---|
| FAA ARP ("estimated") | 48.99999, -112.79258 | **1.2 km west of the runway midpoint, west of the highway.** Likely the source of the misplaced in-sim marker. |
| Wikipedia coordinates | 48.99861, -112.77639 | close to the OSM runway midpoint |
| OSM runway line (from OurAirports, not surveyed) | 48.99867, -112.78789 to 48.99868, -112.76697 | 1,530 m long, more than the published 1,353 m; endpoints are not trustworthy, but it puts the runway on a true heading of about 090 along the border |
| Canadian port (CBSA) building | 48.9995-48.9996, -112.7880 | OSM |
| US port (CBP) building | 48.9964-48.9966, -112.7889 | OSM; replaced in 2012 (ARRA-funded, daytime-only port) |
| Other small buildings | around 48.9993, -112.7878 and 49.0000, -112.7877; two stables about 48.9958, -112.7893 | OSM |

| Canada-US boundary (OSM way 82787728) | 48.99856-48.99858 from -112.7915 to -112.7602 | almost exactly an east-west line across the whole field |

**The runway straddles the border, and must keep doing so.** One description says the runway's southern edge is 10 ft inside the US and the rest (about 55 ft) is in Canada. With a 65 ft (20 m) runway, the centreline is about 7 m north of the boundary: about 48.99863 N using the OSM boundary. The OSM runway line (48.99867) agrees to about 5 m. Tie-downs are on both sides of the line.

The runway runs east from the highway (MT 213 / AB 62), so the port of entry sits just off the 07 threshold. Approaching runway 07, you pass over the port and the 31 ft power line.

**To do before building:** measure the strip, the mowed area and the threshold ends on recent imagery (Esri World Imagery was down on 2026-10-27; retry, or use Google Earth, or measure in DevMode against the sim's own aerial). The runway in our XML must match **the sim's aerial**, because that is what the user sees.

### The default in-sim airport (MSFS 2024)

Read from Little Navmap 3.0.18's MSFS 2024 database (`%APPDATA%\ABarthel\little_navmap_db\little_navmap_msfs24.sqlite`, loaded 2025-11-22 through SimConnect; reload the scenery library in Little Navmap for fresher data):

| Item | Default sim value | Compared with real |
|---|---|---|
| Airport ident and name | `H28`, "Whetstone Intl"; no CEQ4 entry | |
| ARP (the marker) | 48.99999, -112.79258 | the FAA "estimated" ARP, 1.2 km west of the runway midpoint: **confirms the marker problem** |
| Magnetic variation | 12.5 E | |
| Runway | **08/26** (the sim renumbered it from the heading and variation), grass, 5,229 x 68 ft (1,594 x 20.7 m), true heading 89.97 | real 07/25, 4,440 x 65 ft: about 240 m too long |
| Runway ends | 08: 48.998676, -112.788063; 26: 48.998684, -112.766197 | |
| Runway midpoint | 48.998680, -112.777130 | 12 m north of the OSM boundary, so the south edge is about 2 m north of it; real is 10 ft (3 m) south. Check on the aerial |
| Elevation | runway 4,346.5 ft, starts 4,336.0 ft | published 4,336 ft |
| Start positions | 08: 48.998676, -112.787613; 26: 48.998684, -112.766647 (about 33 m in from each end) | |
| Parking, taxi paths, lights, VASI | none | real field has tiedowns on both sides |

The MSFS 2020 default (Little Navmap's 2020 database, 2023-09-16) had the same runway, plus a CTAF/UNICOM 122.8 entry and one apron. The 2024 default has neither, so our airport adds the 122.8 `Com`. Run `python -I tools/sim_airport.py H28` (add `--sim msfs` for 2020) to repeat this.

So the default runway's centreline and heading are usable, but its ends need trimming to the real 1,353 m (to be decided against the aerial: the extra length may be at one end or split). The number needs forcing back to 07/25.

ADE (`D:\MSFS\Airport Design Editor`, ADE2020 Alpha 21) is MSFS 2020 only and its development has stopped. It can't read MSFS 2024's `sr_v2` airport BGLs, so it isn't a route to the default data.

## 1. Replace the existing field and fix the marker

The in-sim marker (the world-map pin and the airport reference point) comes from the `<Airport lat lon>` attributes. Our `Airport` record, with ident `H28`, overrides the default one.

Plan:
- `Airport` lat/lon at the runway midpoint (the published ARP is wrong for this purpose). `alt` 1321.6 m. `airportTestRadius` about 2,000 m, so it covers the port.
- One `Runway` that straddles the border: southern edge about 3 m (10 ft) south of the boundary, the rest north of it. Check against the sim's aerial (the cleared border vista and the fences should show). Surface grass/turf, 1,353 x 20 m, true heading measured from the aerial (about 090), `number="07"`, `primaryPattern` and `secondaryPattern` LEFT. Keep 07/25 even though today's variation would make it 08/26, since that is what the charts say. Set the `magvar` attribute to today's value and check in the sim that the runway still reads 07/25.
- `RunwayStart` at both ends, a short taxi path to tie-down spots on each side of the border, and a windsock.
- `excludeVegetationAround` on the runway, plus a vegetation-exclusion polygon over the strip. The trees the user lands in are at the misplaced marker, west of the highway, so they stay. A start position on the runway puts the user on the turf.

Decided (2026-10-27): only the marker is misplaced; the default runway already sits on the aerial's strip. Our runway should match the default one's position (read it in DevMode before replacing it), and the fix is mainly the `Airport` lat/lon.

## 2. Two identifiers (H28 and CEQ4)

An MSFS `Airport` record has one `ident`. Options:

| Option | Pros | Cons |
|---|---|---|
| A. One airport, ident `H28`, name `Whetstone Intl (CEQ4)` | Clean: one runway, one set of AI and ATC data. CEQ4 shows in the name and the airport card. | Typing CEQ4 in the world-map search may not find it (the search does match names, untested). |
| B. Two `Airport` records, `H28` and `CEQ4`, sharing the same runway geometry | Both idents work in the flight planner, the EFB and FSE job matching. | Two overlapping runways: risk of z-fighting, doubled windsocks and parking, AI traffic spawning twice, ATC confusion. Needs a trick (for example the CEQ4 runway with `transparent` and no markings, and no parking). |
| C. `H28` real, `CEQ4` a minimal record with no runway, only a start position | CEQ4 is searchable and flight-plannable. | The sim may reject or hide an airport with no runway; untested. |

Also to check: whether the base sim already has a separate CEQ4 entry. If it does, it needs to be overridden too, or two markers will sit side by side.

Decided (2026-10-27): **option A**, ident `H28`, name `Whetstone Intl (CEQ4)`. The user found no CEQ4 entry in the sim (2026-10-27), so only H28 needs overriding. Still to check: whether a world-map search for "CEQ4" finds the name.

## 3. Making the field stand out from the farm fields

What the real field has, which we model regardless:
- white edge cones every 200 ft (about 22 per side) and double cones at each threshold;
- the two 4 ft fences 44 ft each side of the centreline, full length (a strong linear cue from the air);
- the power line with red marker balls off the 07 end (built with the port-of-entry scenery, see item 5);
- a windsock.

Ways to make the turf read differently:

| Option | Effect | Cost and risk |
|---|---|---|
| Mowed-grass ground polygon over the strip and its mowed apron (Apron or ground polygon with a short-grass material, as CYXD's grass polygons) | Even, lighter green; looks maintained in every season | Low. Only covers our area, so the contrast depends on the aerial around it. |
| Mowing-stripe texture (custom material, light and dark bands lengthwise) | Very visible from pattern altitude; reads as "mowed" | Medium: one custom texture; risk of looking artificial up close. |
| Repaint the **surrounding** fields (tilled black or tall grain) with large ground polygons | Biggest contrast | High: static all year (it would look tilled in July and under snow), covers real cropland, and fights the sim's seasonal ground. Not recommended. |
| Raised turf edge (a row of taller grass meshes along the fences) | Adds a "hedge" line | Medium; mostly redundant with the fences. |

Decided (2026-10-27): realistic cones, fences and windsock (the power line comes with item 5), plus a mowed short-grass polygon with subtle lengthwise mowing stripes. The surrounding fields are left alone.

## 4. Navigation aids

Real field: no lights, no VGSI, no navaids. Options:

| Option | Realism | Use |
|---|---|---|
| None beyond the windsock (as real) | Exact | Day VFR only, as in real life |
| PAPI-2 or PAPI-4 at one or both ends, solar-style | Fictional | Helps a steep or short approach over the power line and port |
| Pilot-controlled low-intensity edge lights on 122.8 | Fictional | Makes the field usable at night; the sim's ATC also treats it as lit |
| Threshold reflectors only | Plausible for a remote field | Shows up in landing lights only |

The port lights (item 5) give a night landmark either way.

Decided (2026-10-27): the real-field items (windsock, cones, fences; the marker-ball power line comes with item 5), plus a **fictional PAPI** and **threshold/edge reflectors**. No edge lights. PAPI on **runway 07 only**, where the power line and the port are the obstacles. Plan PAPI-2 at about 3.5 deg so the on-path aircraft clears the 31 ft line at 205 ft (to be checked against the 7:1 clearance slope); runway 25 has an open approach over fields.

## 5. Del Bonita border crossing

Two ports about 300 m apart on the highway, each with a main building, inspection canopy and booths, parking, and outbuildings (OSM shows small buildings on both sides and two stables south of the US port). The crossing is open daytime only (09:00-17:00 CBP; CBSA lists longer summer hours), but the canopy and pole lights are security lighting and stay on all night.

Plan:
- Measure footprints from OSM and imagery; heights and colours from Street View (photos and `SOURCES.md` in `docs/h28/port-photos/`, the same layout as CYXD).
- Build glTF models with the CYXD generator approach (flat colour palette, `LibraryObject` placements, building exclusion polygons).
- Night: emissive canopy undersides and windows, plus light sources on the canopies and on pole lights around the plazas. The goal is a bright cluster visible from 10-15 nm on a dark prairie.
- Day: the canopies and roofs read as a VFR landmark marking the 07 end.

Decided (2026-10-27): **massing plus lights** now: correct footprints, heights and roof colours, canopies, emissive windows, canopy and pole lights. **Future item:** facade textures from Street View photos (signage, cladding).

**Power line (part of this scenery work):** model the power line off the runway 07 end along with the port buildings. Take its course (pole positions) from OSM `power=line` / `power=minor_line` ways; the Overpass servers timed out on 2026-10-27, so fetch it when this work starts, and fall back to imagery if OSM doesn't have it. Check it against the FAA remark: 31 ft high, red marker balls, crossing 205 ft from the threshold and 70 ft right of the centreline (7:1 clearance slope). Poles and wires as glTF models (or library objects if a suitable one exists), with the marker balls on the span nearest the runway. The PAPI angle (item 4) is set to clear it.

## 6. What an RNAV approach would look like here

None exists in real life. FAA criteria would make one hard: a 65 ft turf runway with no lights limits it to day-only, circling or straight-in LNAV with high minimums, and the final segment of 25 crosses Canadian airspace and the Canadian half of the field. Montana references to read before designing one: Cut Bank (KCTB), Shelby (KSBX), Conrad (S01), Big Timber (6S0).

A typical small-field GPS approach (T-design / TAA):
- Three IAFs: one on the extended centreline and one 4-6 nm either side, joining an IF 5-6 nm farther out on the centreline (hold-in-lieu of a procedure turn at the IF).
- FAF about 5 nm from the threshold, crossed at about 1,500 ft AGL (about 5,900 ft MSL here), 3.0 deg path.
- MAP at the threshold. LNAV MDA about 400-500 ft above field (about 4,800 ft MSL), 1 sm visibility; circling higher.
- Missed approach: climb on runway heading, then direct to a holding fix (often the IAF on the centreline).
- Notes typical for such a field: "Procedure NA at night", "Circling NA north of runway" (or similar, to keep circling on one side of the border), altimeter from Cut Bank.

Decided (2026-10-27): implement **both**, as fictional approaches, so the user can compare them in the sim:
- **RNAV (GPS) RWY 25**, straight-in LNAV: final course along the extended centreline from the east (along the border), FAF about 5 nm, MAP at the threshold, MDA about 400-500 ft above field.
- **RNAV (GPS)-A**, circling only: final course offset from both runways, MAP over the field, circling minimums about 600-700 ft above field, "circling NA north of runway". Untested: whether the MSFS approach XML accepts an approach with no runway, and how the planner shows it. Build it after RWY 25 and check it on its own.
- Fix names invented (five-letter, not matching any real fix), as with CYXD's RNAV 12 Y and 30 Y. Before choosing fixes and altitudes, read the Cut Bank, Shelby, Conrad and Big Timber plates.

## 7. Arrivals and departures

Real fields of this size have no SIDs or STARs. If an approach exists, the FAA also publishes a takeoff minimums / obstacle departure procedure (ODP), usually a short text like "Rwy 7: climb heading 070 to 4,800 before turning." MSFS has no slot for a text ODP; it would have to be a `<Departure>` like CYXD's CITY4.

Decided (2026-10-27): **no SIDs or STARs**, even if an approach is added.

## Sources

- AirNav H28: https://www.airnav.com/airport/H28
- Wikipedia, Whetstone International Airport: https://en.wikipedia.org/wiki/Whetstone_International_Airport
- Wikipedia, Del Bonita Border Crossing: https://en.wikipedia.org/wiki/Del_Bonita_Border_Crossing
- OurAirports H28: https://ourairports.com/airports/H28/
- MDT State Owned Airport Conditions: https://mdt.mt.gov/other/webdata/external/aero/State_Owned_Airport_Conditions.pdf
- CBSA office, Whetstone International Airport (Del Bonita): https://www.cbsa-asfc.gc.ca/do-rb/offices-bureaux/656-eng.html
- CBP hours (Land Line): https://landline.media/feds-announce-updated-hours-at-four-ports-of-entry-on-northern-border/
- OpenStreetMap (Overpass query, 2026-10-27): runway way 232480144, aerodrome way 1208466528, port buildings ways 1147679784, 1147679785, 1151192789
