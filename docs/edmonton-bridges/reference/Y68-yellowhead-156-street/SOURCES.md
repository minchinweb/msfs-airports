# Y68 Yellowhead / 156 Street: sources

Street-level photos are in `street/`. See `street/SOURCES.md`.

## Measurements

| Tag | Source | What it supplies | Access |
| --- | --- | --- | --- |
| [AB] | [Alberta Transportation, Structure-Export.csv](https://www.transportation.alberta.ca/PlanningTools/Data/Bridge/Structure-Export.csv), retrieved 2026-11-23 | **STRU_ID 148330**, file 85162, "156 STREET - YHT GRADE SEPARATION ( B324 )". Location "156 ST AND YELLOWHEAD TRAIL (HWY 16) GRADE SEPARATION IN EDMONTON". Located on 156 St. Located over Highway 16 at R1 km 4.162 and L1 km 4.153. Two spans, 33.5 and 30.0. Nominal length 63.5. Gross deck width 30.8. Total clear roadway 21.3. Measured vertical clearance under the structure 5.3. Theoretical vertical, theoretical horizontal and measured horizontal clearances blank. Deck height blank. Pier cap and pier shaft concrete. Abutment foundation blank. Span type code WG (no label in the file). Wearing surface polymer modified ACP. Major bridge, in service, first in service 2007. Estimated AADT 30,600. Sufficiency 52.9, condition 61.1, last inspection 4 July 2025. Owned and managed by the City of Edmonton. Latitude 53.5789116080445, longitude -113.590698399705. Units not labelled in the file. |
| [AB] | same file | **STRU_ID 148332**, file 85163, "156 STREET - CNR (NORTH OF YELLOWHEAD TR.) ( B325 )". 156 Street over the CN rail line, one span of 39.24, nominal 39.24, gross width 32.5, total clear roadway 25.2, in service 2006, about 207 m north of this structure's record point. **A separate structure.** Not used for any Y68 figure. | Same. |
| [AB] | same file | Records named "CITY ID" (2086739 to 2086746, 2086873) with status PROPOSED, and the 156 Street and 123 Avenue CITY ID records. None is built. None used. | Same. |
| [AB] | same file | Searched every record with "156 ST" in its name or location, and every record within 600 m of the STRU 148330 point. Only 148330 and 148332 are built. The 14 "156 ST" hits are the two built structures, one at Whitemud Drive (STRU 40253, 70.4 m, over Whitemud, not this one), and the proposed records above. | Same. |
| [OSM] | OpenStreetMap API 0.6 map call, bbox -113.6040,53.5752,-113.5775,53.5826, retrieved 2026-11-23 | Deck ways 25532547 (northbound, three lanes, bridge=yes, layer=1, 64.5 m plan) and 38071214 (southbound, two lanes, bridge=yes, layer=1, 64.0 m plan). Footprint 1137993242 (bridge:structure=beam, closed). Footway 1529521611 (bridge=yes, layer=1, 65.0 m). Road beneath 937503510, 937503512, 1379042187 (Yellowhead Trail NW, Highway 16). Ramps and approaches as listed in `geometry.json`. Mapper tags only. ODbL. | ODbL. Geometry and mapper tags only. |
| [OSM] | `docs/edmonton-bridges/bridge-geometry.json`, Y68 object, retrieved 2026-10-14 | The object lists no bridge ways within 700 m of its estimated centre 53.578, -113.596, and an empty connected list. The live extract on 2026-11-23 has the ways above. Way 25532547 was last edited 2024-05-14 (version 12), so its bridge tags predate the 2026-10-14 query. The earlier empty result was not a missing OSM feature. Not edited. | Repo file. |
| [WP] | [Wikipedia, Yellowhead Trail](https://en.wikipedia.org/wiki/Yellowhead_Trail), text fetched 2026-11-23 | "Interchanges were opened at 184 Street in 2004 and 156 Street in 2007." Cites Alberta Transportation TIMS, p. 186. The table row for "156 Street - St. Albert" says "Partial cloverleaf interchange" with no citation. The text says "After an interchange at 156 Street, a pair of one-way service roads begins". Does not say which road passes over at 156 Street. No dimensions. CC BY-SA. | Text only. |
| [WP-mirror] | Search snippet quoting a mirror of Yellowhead Trail (Edmonton), 2026-11-23 | A planned-upgrade chart lists "156 Street, folded diamond interchange". This conflicts with the Wikipedia table's "partial cloverleaf". Mirror only. Not used beyond noting the conflict. | Search snippets only. |
| [City] | [City of Edmonton, Yellowhead Trail 156 Street to St. Albert Trail](https://www.edmonton.ca/projects_plans/yellowhead-trail-156Street-to-StAlbertTrail) | HTTP 502 on fetch, 2026-11-23. Also the alternate edmonton.ca/yellowhead156streettostalberttrail returned HTTP 502. Not read. | Not available. |
| [Search] | Search summary, 2026-11-23 | Says Yellowhead Trail 156 Street to St. Albert Trail freeway conversion was built 2021 to 2023, complete by winter 2024. No dimensions for the 156 Street bridge. Not checked against the City page. | Search snippets only. |

No Structurae entry, HistoricPlaces record, or Alberta bridge sheet with a deck elevation or a navigation clearance was found for STRU 148330. No Government of Alberta sheet giving the deck elevation was found. The brief's Environment Canada gauge 05DF001 is not relevant here: this crossing has no river.

## Photos

No open-licence photograph of this structure was found. `photos/` is empty for this reason.

Wikimedia Commons searches on 2026-11-23 for "156 Street Edmonton", "Yellowhead Trail Edmonton overpass", and "156 St Yellowhead" returned no image of this crossing. Category queries for "Yellowhead Trail (Edmonton)", "Yellowhead Trail NW" and "156 Street (Edmonton)" returned no category of this crossing. The Yellowhead Trail category members are an east interchange subcategory (Anthony Henday), Beverly and Clover Bar bridges, and unrelated road signs.

## Street photos

Four Mapillary images are saved in `street/`. Their licence is unconfirmed. Two show the 156 Street roadway on or beside the deck, and two show the approaches. None shows the Yellowhead roadway underneath. See `street/SOURCES.md`.
