# Y66 Yellowhead / 178 Street: sources

Street-level photos are in `street/`. See `street/SOURCES.md`.

## Measurements

| Tag | Source | What it supplies | Access |
| --- | --- | --- | --- |
| [AB] | [Alberta Transportation, Structure-Export.csv](https://www.transportation.alberta.ca/PlanningTools/Data/Bridge/Structure-Export.csv), retrieved 2026-11-23 | Two records for the Yellowhead bridges over the CNR at about this point. STRU_ID 40882 (file 78728, "YHT EB - CNR (180 ST.) (B188)") and STRU_ID 40883 (file 78728, "YELLOWHEAD TRAIL WB - CNR (180 ST.) (B189)"). Both: located on Highway 16, control section 17, at km 1.241 (EB) and 1.303 (WB). Located over the CNR railway. Three spans 41.5 m, 52 m, 41.5 m. Nominal length 135 m. Theoretical length 156.2 m (EB) and 156.1 m (WB). Skew -60 degrees. Gross deck width 14.5 m. Total clear roadway 13 m. Theoretical vertical clearance under structure 7.2 m, horizontal 7.5 m. Deck height 10.4 m as written, units not labelled. Pier cap and shaft concrete. Deck code PCONC. In service 1981. Estimated AADT 36352 (EB) and 30680 (WB). Coordinates for EB 53.571903, -113.632487, and for WB 53.572104, -113.631565. | Open government data, direct download. Units are not labelled in the file. The record does not name a 178 Street crossing. |
| [AB] | same file | Structure 146057 (file 85130, "184 STREET - YELLOWHEAD TRAIL (B291)"), over Highway 16 at 0.784 and 0.790 km. Not this structure. Recorded in [Y65 SOURCES.md](../Y65-yellowhead-184-street/SOURCES.md). | Same. |
| [AB] | same file | Structure 41607 (file 82066, "178 STREET - WHITEMUD DRIVE"), 178 Street over Whitemud Drive at about 53.512, -113.630. Not this structure. | Same. |
| [AB] | same file | Searched every record with 178 Street or Yellowhead in its name or location, and every record within about 700 m of 53.572, -113.631. No record has 178 Street over Yellowhead, or Yellowhead over 178 Street. Other records near this point are proposed tube structures on Yellowhead (STRU 2086644, 2086643, 2086731, 2086725, 2086727, 2086732, 2086733). Their status is PROPOSED. | Same. |
| [OSM] | `docs/edmonton-bridges/bridge-geometry.json`, Y66 object, OpenStreetMap, retrieved 2026-10-14 | Bridge ways 23226555 (3 lanes, width tag 11.1), 61513664 (4 lanes, width tag 14.6), and 273839599 (motorway link, bridge). Approaches 23226554, 60064980, 61431875, 61513652. Ramps 186928079, 273839600. Cross-road ways 25531583, 279661272, 279661273 (dropped; see `geometry.json`). No way named 178 Street is in the object. | ODbL. Geometry and mapper tags only. |
| [WP] | [Wikipedia, Yellowhead Trail](https://en.wikipedia.org/wiki/Yellowhead_Trail), text fetched 2026-11-23 | Lists 184 Street, 170 Street and 156 Street as interchanges. Says Yellowhead "passes underneath 184 Street and over the Canadian National Railway". Says the road "intersects 170 Street at another diamond interchange". Does not mention 178 Street or 180 Street as an interchange. Exit numbers differ between the article fetch and its mirrors, so none are used here. | CC BY-SA. Text only. |
| [WP-mirror] | Search results quoting mirrors of the same Wikipedia article, 2026-11-23 | Interchange list from west to east, including 184 Street, 170 Street, 156 Street and 82 Street. No 178 Street. Exit numbers conflict with the article fetch. Not used for measurements. | Search snippets only. |
| [CITY-184] | [City of Edmonton, 184 Street Bridge over the Yellowhead Freeway](https://www.edmonton.ca/projects_plans/roads/184-street-bridge-yellowhead-trail-rehab) | Search summary only. The page is about 184 Street, not 178 Street. | City of Edmonton. The page was not fetched in full. |
| [CITY-FC] | [City of Edmonton, Yellowhead Trail freeway conversion](https://www.edmonton.ca/projects_plans/roads/yellowhead-trail-freeway-conversion) | Search summary only. Mentions 127 Street, 121 Street and 66 Street. Does not mention 178 Street. The page and the Dec 2016 graphic map PDF returned HTTP 502 on fetch on 2026-11-23. | City of Edmonton. Not used for measurements. |

No Structurae entry, HistoricPlaces record, or Alberta bridge sheet with a deck elevation was found for STRU 40882 or 40883. The Edmonton City as Museum Project and City Archives were not searched for this point. A web search for "178 Street" with "Yellowhead" returned no matching overpass.

The brief asked for the Environment Canada gauge 05DF001. It is not used here. Nothing in the sources converts a gauge reading to a deck elevation for this structure.

## Photos

No open-licence photograph of this structure was found. `photos/` is empty for this reason.

Wikimedia Commons, searched within 800 m of the centre and by text for Yellowhead Trail with overpass, bridge, or 178 Street, returned no image of the crossing. One CC BY-SA 2.0 image, "Yellowhead Highway (E town) (11343119934).jpg" (KMW2700, 4288 x 3216), came up in the text search. Its location is not confirmed as this structure, and it was not downloaded. The search also returned many public-domain PDFs of Alberta publications, which do not show this structure.

### Not downloaded

- [Yellowhead Highway (E town) (11343119934)](https://commons.wikimedia.org/wiki/File:Yellowhead_Highway_(E_town)_(11343119934).jpg). CC BY-SA 2.0. Location not confirmed as this structure.

## Street photos

Four Mapillary images are saved in `street/`. Their licence is unconfirmed. They show the Yellowhead freeway, and none clearly shows the 178 Street crossing. See `street/SOURCES.md`.
