# B262 Holyrood Gardens Tower — sources

No open-licence photographs were saved for this folder. The `photos/` folder is empty. A photo search was not run this session.

Street-level frames are in `street/`, with their own SOURCES.md.

## Sources

| Source | What it supplies | Licence / access |
| --- | --- | --- |
| [City of Edmonton, DC2 Site-specific Development Control Provision, Area 2](https://webdocs.edmonton.ca/ZoningBylaw/DC2/1000/DC2.1001_(Area_2).htm) | Building type E maximum height 86.0 m. Floor plate of 750 m² above 22.0 m for types D and E. 35.0 m separation for buildings over 22.0 m, 20.0 m between type E and the most southern type D in Area 2-B. Signature articulation for type E. | City of Edmonton zoning bylaw. Text read. Table read from the page text. |
| [City of Edmonton, DC 20757](https://zoningbylaw.edmonton.ca/dc-20757) | The same Direct Control provision in the current bylaw. Listed in the search results. Not opened. | City of Edmonton. Not read. |
| [Edmonton Journal, 10 July 2018, "New design OK'd for Holyrood Gardens"](https://www.pressreader.com/canada/edmonton-journal/20180710/281492162079384) | Revised design approved, 2018. Listed in search results. Not opened. The 20-storey early-plan figure came from an unnamed report in a search summary, not from this article. | Edmonton Journal. Not read. |
| [SkyriseCities, "excavation begins holyrood gardens", March 2020](https://edmonton.skyrisecities.com/news/2020/03/excavation-begins-holyrood-gardens) | Excavation began in 2020. Listed in search results. Not opened. | SkyriseCities. Summary only. |
| [SkyriseCities, Holyrood Gardens Redevelopment project page](https://edmonton.skyrisecities.com/database/projects/holyrood-gardens-redevelopment.23492) | Project listing. Search summary says 86 m and 25 storeys and lists the project as under construction. Not verified against the City. | SkyriseCities. Summary only. |
| [SkyriseCities forum, "East Junction | 86m | 25s | Regency Developments | DER + Associates"](https://edmonton.skyrisecities.com/forum/threads/east-junction-86m-25s-regency-developments-der-associates.26188/page-2) | Forum thread title gives 86 m and 25 storeys for a Regency project. Not confirmed as the Holyrood tower. A search summary also cites a forum estimate that the tallest tower is about 70 m. | SkyriseCities forum. Title only. |
| [CTV News, Holyrood development breaking ground](https://edmonton.ctvnews.ca/while-other-projects-hit-pause-holyrood-development-breaking-ground-1.5008897?cache=yes) | Regency broke ground on the first phase. Four-tower phase one, more than 700 units, due around 2022. Summary only. | CTV News. Summary only. |
| [Holyrood Community Association, "Rezoning Submitted for Holyrood Gardens Site"](https://holyroodcommunity.org/?p=983) | Rezoning application. Listed in search results. Not opened. | Community association. Not read. |
| [REW, Holyrood Gardens by Regency Developments](https://www.rew.ca/developments/5675/holyrood-gardens-edmonton-ab) | Developer listing. Listed in search results. Not opened. | REW. Not read. |
| [City of Edmonton engagement page, Holyrood Gardens](https://engaged.edmonton.ca/HolyroodGardens?page=3) | Public engagement history. Listed in search results. Not opened. | City of Edmonton. Not read. |
| [City of Edmonton Open Data, Development Permits (2ccn-pwtu)](https://data.edmonton.ca/d/2ccn-pwtu) | Development permit file 298214168 for the Holyrood Gardens site: 2019 approval of four buildings and 725 dwellings; 2020 increase to 760; 2023 building 1 revision to 26 floors and 275 dwellings; 2024 building 2 cut to 6 storeys and 84 dwellings; 2026 landscape phasing. Building 1 is at 9009 85 Street NW, geocode 53.52652, -113.45658. Queried 2026-11-23 through the Socrata API. | City of Edmonton open data. Records read. |
| [City of Edmonton Open Data, General Building Permits (24uj-dj8v)](https://data.edmonton.ca/d/24uj-dj8v) | Building permit issued 11 September 2020: "BLDG 1 a 26 storey apartment building on existing parkade - Holyrood Gardens", 284 units, construction value $58,975,500, no occupancy date. Building 2 permit: 6 storeys, 84 units, occupancy granted 5 November 2025. Queried 2026-11-23. | City of Edmonton open data. Records read. |
| [OpenStreetMap ways 1209666933](https://www.openstreetmap.org/way/1209666933) and [1221215089](https://www.openstreetmap.org/way/1221215089) | The building outline ("The Beacon Apartments at East Junction", 9009 85 Street NW, 6 levels) and the tower part (26 levels, height 86). Read 2026-11-23 through the OSM API. | ODbL. Geometry and tags in `geometry.json`. |
| SkyriseCities project page, rendering 23492-124185 (DER + Associates, 13 Nov 2018) and 23492-124184 (street view along 85 Street) | Tower form and colours used for the model (see NOTES.md). The page itself returned 403; read through the Wayback Machine copy of 31 Oct 2026, which gives 7 buildings, 1,200 units, maximum 86.00 m and 25 storeys, building units 284, 143, 200, 133, 440, developer Regency, builder Pagnotta, architect DER + Associates Architecture, status under construction. | Copyright the developer/architect. Viewed only, not saved here. |
| [OpenStreetMap way 556925041, Holyrood Gardens](https://www.openstreetmap.org/way/556925041) | Landuse residential, apartments, name Holyrood Gardens. 19 nodes. The whole site polygon, not a tower footprint. | ODbL. Geometry and tags only. See `geometry.json`. |
| Mapillary, images in the bounding box in `street/` | Street-level frames, July and August 2018. | See `street/SOURCES.md`. |

## What the search did not settle

- Storey count: resolved by the City permit record, 26 floors (2023 revision). The press and forum figures (20, 22, 25) are superseded.
- Height: 86.0 m zoning ceiling (City DC2 table). A 70 m figure appears in a forum summary. No built height in metres in any record checked.
- Current construction status: the permit has no occupancy date for building 1. Not confirmed.
- Tower location: 9009 85 Street NW, the junction with Connors Road (which becomes 90 Avenue). The permit records name it. The press and DC2 descriptions use "85 Street and 90 Avenue".
