# W85 Fox Drive, Campbell Bridge — sources

Photos in `photos\` are openly licensed (CC BY-SA). A file that was useful but not openly licensed, or that is CC BY-NC, is listed under "Not downloaded" with the URL only.

## Measurements

| Source | What it supplies | Licence / access |
| --- | --- | --- |
| [Edmonton Nature Centres Foundation, Whitemud Ravine Nature Reserve – North of Whitemud Drive (PDF)](https://encf.org/wp-content/uploads/2020/04/Walk-II-21.pdf) | Campbell Bridge named for Duncan L. Campbell, who farmed the area and built the first bridge over the creek. Present bridge built by the City in 1969. | ENCF walk sheet. Text used. |
| [Edmonton Nature Centres Foundation, Brookside Loop (PDF)](https://encf.org/wp-content/uploads/2022/03/Walk-II-22.pdf) | Walk under Campbell Bridge from Fort Edmonton Park Road. Washrooms in the Alfred Savage Centre south of Campbell Bridge. No span, width, or height. | ENCF walk sheet. Text used. |
| [edmonton.name, Whitemud Park](https://edmonton.name/en/whitemud-park-edmonton) | Repeats the 1969 City-built present structure and the Duncan L. Campbell naming. Places the bridge at the north edge of the park. Creek empties into the North Saskatchewan just east of Quesnell. | Third-party park page. Text used only where it matches the ENCF sheet. |
| [Wikipedia, Fox Drive](https://en.wikipedia.org/wiki/Fox_Drive) | Fox Drive, 2.2 km, 70 km/h, from Whitemud Drive at the southern approaches to Quesnell, then across Whitemud Creek on Campbell Bridge after Fort Edmonton Park Road. Caption on the 2012 photograph names this crossing. The 2.2 km is the road, not the span. | CC BY-SA. Text only. The photograph is saved below. |
| [Naming Edmonton, Fox Drive](https://namingedmonton.ca/naming-edmonton-a-digital-gazetteer/fox-drive/) | Road named for Thomas Fox. Designation year 1968. No Campbell Bridge entry was found. | City of Edmonton gazetteer. Text used for the road name only. |
| [Canada Gazette Part I, Q2 2008 index (PDF)](https://gazette.gc.ca/rp-pr/p1/2008/g1-142q2.pdf) | Indexes a notice: City of Edmonton, rehabilitation of the Campbell Bridge over Whitemud Creek. Page 1059 in that quarter. The index does not describe the work. | Government of Canada. Text used. The notice itself was not retrieved. |
| [HistoricPlaces.ca](https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=3031) | No Campbell Bridge record was found. The High Level Bridge record was used only to keep this creek span apart from that truss. | Parks Canada register. |
| [Structurae](https://structurae.net/en/structures) | No Edmonton Campbell Bridge / Fox Drive page was found. Other Campbell bridges on that site are different structures. | Structurae. |
| `docs/edmonton-bridges/bridge-geometry.json`, retrieved 2026-10-14 | OpenStreetMap ways. South carriageway 25475831, three lanes, 70 km/h, `width=11.1`, `bridge:name=Campbell Bridge`. North carriageway 25475833 and 944470767. North cycleway 27265227. South footway 582712471. The extract also stores footway 25475768 and path 840389481, which are other crossings. No elevations. Way node counts match the live OpenStreetMap ways on the same day. | ODbL. Geometry only; see `geometry.json`. |

No Government of Alberta bridge sheet with a deck elevation or a creek clearance was found. HistoricBridges.org has no Campbell Bridge Edmonton page in the sources checked. The City as Museum Project was searched by name and returned no measurement. PIEVC 2008 names a 2004 Earth Tech report, *The Quesnell Bridge and Whitemud Bridge Over Fox Drive*. That second structure is the freeway over Fox Drive. It is not this creek span.

## Photos saved

| File | Shows | Source | Licence |
| --- | --- | --- | --- |
| `deck-looking-east-2012.jpg` | 2 August 2012, from Fort Edmonton Park Road looking east. Fox Drive deck, metal railing, lamp posts, a 70 km/h sign, the far tree line. Wikipedia captions it as the Campbell Bridge over Whitemud Creek. The soffit and the piers are not in the frame. Full file, 2,560 × 1,920. | [Commons, Johntwrl](https://commons.wikimedia.org/wiki/File:Fox_Drive_20120802_01.jpg) | CC BY-SA 3.0 |

## Not downloaded

Openly licensed, skipped because the bridge is not the subject:

- [2008-05-19 Whitemud Creek 002](https://commons.wikimedia.org/wiki/File:2008-05-19_Whitemud_Creek_002.jpg), Johntwrl, 18 May 2008, CC BY-SA 3.0. Caption: just south of where Fox Drive crosses the creek. The deck is not in the frame.
- Other files in [Category:Whitemud Creek (Alberta)](https://commons.wikimedia.org/wiki/Category:Whitemud_Creek_(Alberta)). Park, ravine, and Henday views. This deck is not isolated in those frames.

CC BY-NC, or no open licence found. URL only:

- City of Edmonton Whitemud Park page photographs. No open photo licence stated.
- No openly licensed underside, pier elevation, or aerial was found. City 2019 Pictometry clips in `aerial/` are measuring reference only (licence not confirmed) and are not listed here as redistributable photos.

## Added 2026-10-15 (Tier 2 review)

| Source | What it supplies | Licence / access |
| --- | --- | --- |
| Web search (2026-10-15): "Campbell Bridge Fox Drive Whitemud Creek Edmonton spans length rehabilitation" | Nothing on spans, type, piers or the 2008 rehabilitation. Wikipedia Fox Drive only. | None found. |
| `elevation/profiles.csv`, `scenery-edmonton-bridges/tools/lidar_pil.py` | 25 m LiDAR profiles on every mapped way. Creek bed about 618.4 m at 50 m along the south way; banks 627.9 m at the ends. | Derived from the gitignored 2018 clips. |
| 2019 orthophoto measurements (`aerial/`, 0.2 m/px) | Overall deck width (about 33.5 m), joint lines, deck length about 85 m between the visible joints. Used for measuring only. | City 2019 Pictometry, licence not confirmed. |
