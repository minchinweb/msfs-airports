# R21 Clover Bar Bridge — sources

Photos in `photos\` are openly licensed (CC BY-SA). A file that was useful but not openly licensed is listed under "Not downloaded" with the URL only. Neighbouring structures appear in both saved frames; the table says which structure is which.

## Measurements

| Source | What it supplies | Licence / access |
| --- | --- | --- |
| [Wikipedia, Clover Bar Bridge](https://en.wikipedia.org/wiki/Clover_Bar_Bridge) | Original truss completed summer 1953, named Clover Bar, connected Beverly to Strathcona County. Steel girder built just to the south in 1972, named Beverly, eastbound; Clover Bar westbound in that article. Infobox: north span 1953, south span 1972. Combined 61,402 AADT (2024). Cites Edmonton Journal 18 August 2012 ("Aug. 18, 1953: Premier Manning first to drive of Clover Bar Bridge") and Aubrey, *Naming Edmonton*, p. 22. Railway 504 m / 42 m not used here. | CC BY-SA. Text only. |
| [Wikipedia, List of crossings of the North Saskatchewan River](https://en.wikipedia.org/wiki/List_of_crossings_of_the_North_Saskatchewan_River) | Clover Bar Bridge: 3 lanes eastbound, 1953, 53.572, -113.372. Beverly Bridge: 3 lanes westbound, 1972. Those directions are the opposite of the Wikipedia Clover Bar Bridge article and of Naming Edmonton. | CC BY-SA. Text only. |
| [Naming Edmonton, Beverly Bridge](https://namingedmonton.ca/naming-edmonton-a-digital-gazetteer/beverly-bridge/) | Clover Bar Bridge handles westbound traffic. Beverly, 1972, eastbound. Railway 1907, Grand Trunk Pacific. | City of Edmonton gazetteer (Aubrey 2004). Text used. |
| [Structurae, Clover Bar Highway Bridge](https://structurae.net/en/structures/clover-bar-highway-bridge) | Completion 1952. Motorway bridge. Coordinates 53°34'15.37"N 113°22'23.59"W. No span, width, or height on the public page. | Structurae. Text used. No technical data. |
| [Library of Congress, Clover Bar Bridge (Edmonton, Alta.)](https://id.loc.gov/authorities/subjects/sh99014674.html) | Quotes Gibbs & Brown, *Clover Bar Bridge replacement: environmental impact assessment*, 1999: existing Clover Bar Bridge constructed 1952/3 as a two-lane, two-way bridge; replacement needed for six-lane Yellowhead Trail. City site, 8 November 1999: functional planning study completed, subject to council. | LCSH. Text used. |
| [Truck News, 6 April 2001](https://www.trucknews.com/transportation/headaches-in-store-for-edmonton-drivers/1000000465/) | That construction season includes "a three-lane Clover Bar Bridge for westbound traffic on Yellowhead Trail." | Truck News. Text used. |
| [HistoricPlaces.ca](https://www.historicplaces.ca/en/rep-reg/place-lieu.aspx?id=3031) | No Clover Bar highway record was found. The High Level Bridge record was used only to keep this deck apart from that truss. | Parks Canada register. |
| `docs/edmonton-bridges/bridge-geometry.json`, retrieved 2026-10-14 | OpenStreetMap ways. Way 61431758 tagged `bridge:name=Beverly Bridge`, three lanes, 100 km/h, no width tag. Outline 642360970 tagged `name=Clover Bar Bridge`, `bridge:structure=beam`. Approach polylines. Outline 642360969 dropped (R20). Way node counts match the live OpenStreetMap ways on the same day. | ODbL. Geometry only; see `geometry.json`. |

The City's 2025–2026 rehabilitation is named Beverly Bridge. It is cited in `reference/R20-beverly/SOURCES.md`. It is not used here as this deck's project. No Government of Alberta bridge sheet with a deck elevation or a navigation clearance was found for this deck.

## Photos saved

| File | Shows | Source | Licence |
| --- | --- | --- | --- |
| `elevation-from-southwest-2015.jpg` | Elevation, 12 May 2015, facing northeast. A girder highway with four concrete piers in the channel sits in front of the Clover Bar Railway Bridge. The frame does not label which highway is Clover Bar and which is Beverly. Full file, 4,224 × 2,376. | [Commons, Kmw2700](https://commons.wikimedia.org/wiki/File:Clover_Bar_Bridges_(railway_and_highway_-_HWY_16)_-_Edmonton_-_CA_-_May_2015.JPG) | CC BY-SA 4.0 |
| `rail-from-highway-deck-2011.jpg` | 9 August 2011. Asphalt and a blue metal railing in the foreground, taken from a highway deck immediately next to the railway. The Clover Bar Railway Bridge is beyond the railing: steel deck truss, concrete piers, CN locomotives. The railway sits north of both highway decks. Full file, 4,000 × 3,000. | [Commons, Robert Blyth](https://commons.wikimedia.org/wiki/File:Crossing_the_N._Saskatchewan_river_(6057934376).jpg) | CC BY-SA 2.0 |

## Not downloaded

Openly licensed, skipped as a weaker view or because the bridge is not the subject:

- [IMGP7578 (15396172873)](https://commons.wikimedia.org/wiki/File:IMGP7578_(15396172873).jpg) and [IMGP7586 (16015833605)](https://commons.wikimedia.org/wiki/File:IMGP7586_(16015833605).jpg), KMW2700, 6 December 2014, CC BY-SA 2.0. River ice and a dirt track. The decks are not in the frame.

CC BY-NC, or no open licence found. URL only:

- City of Edmonton photographs of the neighbouring Beverly rehab. No open photo licence stated.
- [Flickr, Drew De Bruyn, Clover Bar Bridge, Edmonton](https://www.flickr.com/photos/123908288@N05/14921839525), 24 July 2014. All rights reserved. Railway caption, not saved.
- The 1999 EIA was not found as an open file.
- No openly licensed underside or aerial was found. City 2019 Pictometry clips in `aerial/` are measuring reference only (licence not confirmed).

## Tier 2 additions (2026-10-15)

| Source | What it supplies | Licence / access |
| --- | --- | --- |
| `elevation/profiles.csv` | 25 m profiles of bare earth and first returns along each mapped way, computed from the 2018 clips in this folder with `scenery-edmonton-bridges/tools/lidar_pil.py` | Derived from the NRCan HRDEM 2018 clips (Open Government Licence - Canada) |
| The 2019 orthophoto in `aerial/` | Pier stations and bent stations (R22), end joints and plan check for all three | City of Edmonton Pictometry clip, measuring reference only, gitignored |
| The photographs in `photos/` | Pier layout and shape, deck depth, railing colour (R20 and R22), truss depth (R22), read at scale from the known deck or locomotive length | As in the table above |
| Web search (Wikipedia, Structurae, City and Alberta project pages, news) | No span, pier, girder or drawing data found | |
