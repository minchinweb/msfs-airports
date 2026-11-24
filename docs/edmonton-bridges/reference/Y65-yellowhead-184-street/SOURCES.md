# Y65 Yellowhead / 184 Street: sources

Street-level photos are in `street/`. See `street/SOURCES.md`.

## Measurements

| Tag | Source | What it supplies | Access |
| --- | --- | --- | --- |
| [AB] | [Alberta Transportation, Structure-Export.csv](https://www.transportation.alberta.ca/PlanningTools/Data/Bridge/Structure-Export.csv), retrieved 2026-11-23 | Records STRU_ID 146057 / file 85130 (184 STREET - YELLOWHEAD TRAIL, B291): two spans 45 m and 42 m, nominal length 87 m, span type WG, concrete deck, rectangular pier shaft, gross deck width 27.2 m, total clear roadway 18.8 m, left sidewalk 2500 (read as mm), ACP PM wearing surface, first in service 2004, over Highway 16 control section 17 at 0.784 and 0.790 km, export point 53.572236, -113.639383. Also records file 85131 (B294, 184 Street over the CNR at 118 Avenue, skew 26 degrees), which is a different structure. | Open government data, direct download. The http address returns 301, so the https address was used. Units are not labelled in the file. |
| [OSM] | `docs/edmonton-bridges/bridge-geometry.json`, Y65 object, OpenStreetMap, retrieved 2026-10-14 | Deck ways 25531561 (northbound), 31680388 (southbound) and cycleway 234183148. Approaches 25531566, 31686096, 472626783, 1553048483. Cycleways 234183141, 234183149. Ramps 25531590, 25531594. Road beneath 60064980, 279661272. Tags lanes=2, maxspeed=60, layer=1. | ODbL. Geometry and mapper tags only. |
| [WP] | [Wikipedia, Yellowhead Trail](https://en.wikipedia.org/wiki/Yellowhead_Trail) | 184 Street interchange: partial cloverleaf, exit 379. Interchanges opened at 184 Street in 2004. Cites Alberta Transportation TIMS, Existing Structures in the Provincial Highway Corridor, 28 Sept 2012, p. 186, for the date. Says Yellowhead "passes underneath 184 Street and over the Canadian National Railway". That wording disagrees with [AB] and [CITY], so it is recorded and not used for direction. | CC BY-SA. Text fetched. |
| [CITY] | [City of Edmonton, 184 Street Bridge over the Yellowhead Freeway](https://www.edmonton.ca/projects_plans/roads/184-street-bridge-yellowhead-trail-rehab) | Project title puts 184 Street over Yellowhead. The summary in search results says the rehabilitation was scheduled to start in August 2026 to extend service life and improve safety. | City of Edmonton. The page returned HTTP 502 on both fetches on 2026-11-23, so only search-result text is used. |
| [CTV-A] | [CTV News, 184 Street Bridge over Yellowhead Trail to close for 3 months](https://www.ctvnews.ca/edmonton/article/184-street-bridge-over-yellowhead-trail-to-close-for-3-months/) | Published 7 Aug 2026. Headline: closure for 3 months. Article body was not returned. Search summary says the ramps stayed open and that this was the first renovation since the bridge opened in the early 2000s. Those two points come from the summary, not the body. | CTV. Headline and byline only. |
| [CTV-B] | [CTV News video, 184 street bridge opens ahead of schedule](https://www.ctvnews.ca/edmonton/video/2026/10/16/184-street-bridge-opens-ahead-of-schedule/) | Dated 16 Oct 2026. Says the bridge is open two weeks ahead of schedule. No dimensions, lanes or work scope. | CTV. Text fetched. |

No Alberta Transportation bridge sheet, Structurae entry, or HistoricPlaces record was found for file 85130. Searches returned none. The City of Edmonton Archives and the Edmonton City as Museum Project returned nothing on this bridge in search.

The brief asked for the Environment Canada gauge 05DF001. It is not used here. Nothing in the sources converts a gauge reading to a deck elevation for this bridge.

## Photos

No open-licence photograph of this structure was found. `photos/` is empty for this reason.

Search on Wikimedia Commons, Flickr (CC filter) and general search returned nothing for 184 Street over Yellowhead. The only nearby CC image found was the Anthony Henday interchange over Yellowhead, which is a different structure and was not downloaded.

### Not downloaded

None. No candidate image was found.

## Street photos

Four Mapillary images are saved in `street/`. Their licence is unconfirmed, and none shows the structure. See `street/SOURCES.md`.
