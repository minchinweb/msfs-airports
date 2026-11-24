# Y70 Yellowhead / 97 Street: sources

No open-licence photograph of this structure was found, so `photos/` is empty. Street-level photos are in `street/`. See `street/SOURCES.md`.

## Measurements

| Tag | Source | What it supplies | Access |
| --- | --- | --- | --- |
| [AB] | [Alberta Transportation, Structure-Export.csv](https://www.transportation.alberta.ca/PlanningTools/Data/Bridge/Structure-Export.csv), retrieved 2026-11-23 | **STRU_ID 41052**, file 79365 structure 1, "97 STREET OVER YELLOWHEAD TRAIL INTERCHANGE AT EDMONTON", structure name 97 STREET - YELLOWHEAD TRAIL (B186). In service 1982. Located on local road (97 Street), over Highway 16 (control section 17) at L1 km 10.768 and R1 km 10.770. One span, 27.9 m. Nominal length 27.9. Theoretical bridge length 30. Maximum span 27.9. Skew 4. Total clear roadway 29.3. Gross deck width 64. Span-type code PJ (not labelled). Theoretical and measured vertical clearance blank. Pile foundation, concrete abutments. Precast concrete deck, high-density concrete wearing surface. Sufficiency 42.3, condition 44.4, last inspection 9 October 2025. Load ratings 28, 49, 62 (units not labelled). Estimated AADTS 37,100 (2023). Owned and managed by the City of Edmonton. Longitude -113.492106, latitude 53.581278. | Same file. Text and numbers used. |
| [AB] | same file | **STRU_ID 39678**, file 74850, CNR over 97 Street, "CNR / 97ST (B071)". Rail on top. Four spans, 41.4 nominal. About 260 m north of the Y70 record point. **Not this structure.** Used only to tell the two apart. | Same. |
| [AB] | same file | **STRU_ID 41618**, file 82076, "CNR / 97ST S (B070)", CNR over 97 Street, same location as 39678, four spans, 41.4 nominal. **Not this structure.** | Same. |
| [AB] | same file | **STRU_ID 41170**, "82 STREET - YELLOWHEAD TRAIL (B224)", about 1.6 km east. Used only to rule out Y71. | Same. |
| [AB] | same file | **STRU_ID 85093 series** ("11.1 - 97 ST OVER ANTHONY HENDAY DRIVE", H45) and other 97 St records to the north and south. Not this point. Not used. | Same. |
| [AB] | same file | Searched every record with 97 ST, 97 STREET, YELLOWHEAD, HWY 16 or HIGHWAY 16 in its name, location, or road field, and every record within 2.5 km of the Y70 estimate and the record point. The only in-service structure over Yellowhead at 97 Street is 41052. Proposed records 2086636, 2086637, 2086641, 2086642 (97 Street and Yellowhead, PROPOSED, no structure) are not built. None used. | Same. |
| [OSM] | OpenStreetMap API 0.6 map call, bbox -113.5070,53.5740,-113.4770,53.5900, retrieved 2026-11-23 | Deck way 472577432 (24.6 m plan, 97 Street NW, lanes 7, sidewalks separate). Approach ways 472577429, 476073031, 472577426, 62232309. Road beneath: Yellowhead Trail NW ways 22916204 and 80403108 (layer -1, tunnel=yes, lanes 3). Interchange ramps (24 motorway_link ways within 150 m). Footways at the ramp terminals. The ways are complete, not clipped at the bbox. No way at this crossing carries `bridge=yes`. The only `bridge=yes` way in the extract is a footbridge 379 m away (way 198706326, access no). Mapper tags only. ODbL. | ODbL. Geometry and mapper tags only. |
| [OSM] | `docs/edmonton-bridges/bridge-geometry.json`, Y70 object, retrieved 2026-10-14 | Object centre 53.578, -113.489 (estimated from the street grid). bridge_ways empty, connected empty, note "Estimated from the street grid. No tagged bridge within 700 m." That note is correct for the estimate: the footbridge is about 730 m from it. The live extract also shows the deck is not bridge-tagged, so the empty list is not a sign of a bad cache. But the cached object held no road ways at all. Refetched live. The cache was not edited. | Repo file. |
| [WP] | [Wikipedia, Yellowhead Trail](https://en.wikipedia.org/wiki/Yellowhead_Trail), fetched 2026-11-23 | "Interchanges opened at 118 Avenue / Victoria Trail in 1978, 97 Street and St. Albert Trail in 1982, and 170 Street in 1983." Cites [5][9]. "The expressway passes underneath St. Albert Trail and past Canadian National's Walker Yard to 97 Street." Interchange table row: "97 Street to Highway 28 north", "Single-point urban interchange; to Royal Alexandra Hospital". No citation on that row. No dimensions or bridge details. CC BY-SA. | Text only. |
| [WP] | Wikipedia, 97 Street (Edmonton), search snippet only, 2026-11-23 | Says 97 Street runs north of Yellowhead Trail as Highway 28. Not fetched. | Snippet only. |
| [City] | [City of Edmonton, St. Albert Trail to 97 Street](https://www.edmonton.ca/projects_plans/st-albert-trail-to-97-street) | HTTP 502 on fetch, 2026-11-23, twice. The search summary says the segment is under construction and targeted to finish in 2027. No 97 Street overpass dimensions in the summary. Not read directly. | Not available. |
| [City] | [City of Edmonton, 97 Street to 82 Street](https://www.edmonton.ca/projects_plans/97-street-to-82-street) | HTTP 502 on fetch, 2026-11-23. A search snippet says traffic signals and direct access at 89 Street were removed under the conversion. Not read directly. | Not available. |
| [Search] | Search summaries, 2026-11-23 | Global News (2021) and Daily Hive (June 2025) both give 2027 as the completion year for the St. Albert Trail to 97 Street segment. CTV gives about $500 million for the segment. No bridge dimensions in any snippet. Search snippets only. | Search only. |
| [Structurae] | Search, 2026-11-23 | No Structurae or engineering record for this interchange was found. | Search only. |
| [HistoricPlaces] | Not checked | No search hit. Not fetched. | Not available. |
| [Commons] | Wikimedia Commons API, category members for Yellowhead Trail, 2026-11-23 | No file of this interchange. See Photos. | Commons API. |

No Government of Alberta bridge sheet with a deck elevation or a navigation clearance was found. The Alberta record gives no deck elevation and no vertical clearance. The Environment Canada gauge 05DF001 is not relevant here: this is a road over a road.

## Photos

No open-licence photograph of this structure was found. The Commons API returned one category of Yellowhead Trail files. None of them shows this interchange.

Checked and not used:

- [File:YellowheadTrail.jpg](https://commons.wikimedia.org/wiki/File:YellowheadTrail.jpg), SriMesh, 21 August 2008, CC BY-SA 3.0. Yellowhead sign marker and 125 Avenue, between 50 Street and 66 Street. Not this interchange.
- [File:Edmonton (26827908070).jpg](https://commons.wikimedia.org/wiki/File:Edmonton_(26827908070).jpg), CC BY 2.0, 18 May 2016. Listed under Yellowhead Trail. Its description is a general Edmonton view. Not viewed, not downloaded.

## Street photos

Four Mapillary images in `street/`. The licence is unconfirmed. See `street/SOURCES.md`. One of them, the Yellowhead underpass image, is taken 19 m from the record point and appears to be inside the Yellowhead underpass beneath this deck. The other three are on 97 Street north of the structure.
