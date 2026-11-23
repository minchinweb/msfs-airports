# H27 and H28 sources

Photos in `photos\` are empty. No openly licensed photograph of the H27 interchange or the H28 arches was found that shows the structures. Candidates are under "Not downloaded". The folder was created so the layout matches the other reference folders.

## Measurements

| Source | What it supplies | Licence / access |
| --- | --- | --- |
| [Canadian Consulting Engineer, "Three Crossings On Henday" (2008)](https://www.canadianconsultingengineer.com/features/three-crossings-on-henday/) | The only source with dimensions for both H27 and H28. Blackmud Creek: three cast-in-place concrete, deck-stiffened, open-spandrel arches, completed September 2005. Each structure 76 m long, 15-degree skew, 40 m middle span, about 18 m cantilevers each side. Roadway 17 m above the creek bed, 45-degree skew. Embankments 16 m high each side, supported partly by the arch thrust. Two ribs per structure, each 40 m span by 7.5 m rise, 7.0 m wide, 0.4 m thick. Deck slab 1.5 m deep, five cells per bridge, cantilever up to 4 m from the girders. Creek realigned. Calgary Trail interchange: Alberta's first three-level interchange; four grade-separated trellis-beam structures; skew 50 to 80 degrees on two; 44 m spans against about 22 m minimum; beams spaced 8 m, not 6 m; beams 600 mm wide at bottom, 1,000 mm at the top-flange underside, flange 1,300 mm; integral abutments; no piers next to the roadway. Owner Alberta Infrastructure & Transportation. Contractors PCL Maxam (Blackmud Creek) and Graham Industrial Services (trellis beams). Design Associated Engineering. Also gives the Whitemud Creek arch (300 m wide, 18 m deep ravine, 20 m span, 7 m walls) which is not used here. | Text used. Verbatim sentences checked against the article text through the fetch tool on two passes. Article date given as 1 January 2008 by the fetch tool. |
| [Wikipedia, Alberta Highway 216 (Anthony Henday Drive)](https://en.wikipedia.org/wiki/Alberta_Highway_216) | Henday has two three-level interchanges. The Calgary Trail / Gateway Boulevard one was the first in Alberta. Several bridges use a trellis-beam design "in which many perpendicular girders are used to carry the upper roadway at a high degree of skew". "Three arch bridges over Blackmud Creek" (cites the CCE article). Interchange is the start of the ring, with exits 78A and 78B. The route text says "Three westbound lanes continue across Blackmud Creek past 111 Street to 119 Street", with no citation on that sentence. No lengths in the infobox for these structures; the infobox length is for the whole ring (77.954 km). | CC BY-SA. Text used. Recorded, not averaged, for the lane count. |
| [Wikipedia, Blackmud Creek](https://en.wikipedia.org/wiki/Blackmud_Creek) | Says only "The creek continues north under Anthony Henday Drive." No structure data. | CC BY-SA. Text used for the creek course only. |
| [Balakrishnan, TAC paper on trellis beam bridges and highly skewed flyovers](https://tac-atc.ca/wp-content/uploads/Balakrishnan.pdf) | Search summaries say the concept was used at the Calgary Trail / Anthony Henday interchange and cite a 2005 TAC paper. Design team listed as Associated Engineering. The PDF was returned as binary data and was not read. Its content for H27 is not confirmed here. | TAC. Not read. |
| `docs/edmonton-bridges/bridge-geometry.json`, retrieved 2026-10-14 | OpenStreetMap ways for both deck centres. Bridge ways and connected approaches, ramps and cross roads. Plan lengths computed from the nodes. No elevations. | ODbL. Geometry only. See geometry.json. |
| [Commons category, Anthony Henday Drive](https://commons.wikimedia.org/wiki/Category:Anthony_Henday_Drive) | 18 files, none of the Blackmud arches or the Calgary Trail interchange structures. | Commons. Listing only. |
| [Commons category, Calgary Trail & Gateway Boulevard](https://commons.wikimedia.org/wiki/Category:Calgary_Trail_%26_Gateway_Boulevard) | 13 files, sign gantries and street photos. None of the structures. | Commons. Listing only. |

No Alberta Transportation Structure-Export.csv row was found for Blackmud Creek or the Henday interchange. The search tool did not reach the file. Not checked: the City of Edmonton structure inventory, HistoricPlaces.ca, Edmonton City as Museum Project, Environment Canada gauge 05DF001 (the gauge is at the Low Level Bridge and uses a local assumed datum; no reading is converted here), and Structurae (a search found no Blackmud Creek or Calgary Trail record).

## Photos saved

None. No open-licence frame shows the H28 arches or the H27 trellis flyovers in a usable way.

## Not downloaded

Candidate Commons files on the Henday and Gateway Boulevard interchange area, all by the same photographer. They are sign and road photographs, and no frame in the descriptions shows the structures.

- [File:AB2nRoad-AB216split-2km (33443092490).jpg](https://commons.wikimedia.org/wiki/File:AB2nRoad-AB216split-2km_(33443092490).jpg), Gateway Boulevard SW near Gateway Park, approaching Ellerslie Road. 5 March 2017. Coordinates 53.41035, -113.4977. CC BY-SA 2.0. Original 2,400 x 1,600 px. A sign gantry; the interchange is not described in frame. Not downloaded.
- [File:AB216rampFromAB2n-TCH16eLloydminsterSign (33786910646).jpg](https://commons.wikimedia.org/wiki/File:AB216rampFromAB2n-TCH16eLloydminsterSign_(33786910646).jpg), northbound along the exit ramp from Gateway Boulevard NW to Anthony Henday Drive. 5 March 2017. Coordinates 53.43029, -113.49238. CC BY-SA 2.0. Original 2,400 x 1,600 px. This is a ramp near the H27 interchange, about 0.7 km north of the Blackmud arches. The sign is the subject. Not downloaded.
- [File:GatewayCityCentre (33698725391).jpg](https://commons.wikimedia.org/wiki/Category:Anthony_Henday_Drive), Gateway Boulevard SW northbound near Ellerslie Boulevard. File page not fetched. Description given by search only. Not downloaded.
- [Commons, Henday Whitemud Creek.jpg](https://commons.wikimedia.org/wiki/Category:Anthony_Henday_Drive). Whitemud Creek, a different structure. Not checked beyond its file name. Not used.
- [Commons, Blackmud Creek Edmonton.jpg](https://commons.wikimedia.org/wiki/Category:Blackmud_Creek). Creek view from Twin Brooks, not a structure. Licence not checked. Not used.

Not open licence, or none stated: the CCE article has no photographs saved here. No photograph of the arches was found in the search results.

No openly licensed underside, elevation, or aerial of the H28 arches was found. The CCE article may have one, but its licence is not stated, and it was not saved.

## Added 2026-11-23 (model build)

- OpenStreetMap API (`api.openstreetmap.org/api/0.6/map`, box -113.522, 53.426 to -113.478, 53.446), read 2026-11-23, ODbL. The road, stream and railway ways are in `geometry.json` under `osm_added_2026_11_23`.
- City of Edmonton 2019 orthophoto and the 2018 1 m DSM and DTM, refetched with `fetch-site-data.py H27` to cover H28 as well. Gitignored. The samples the model uses are in `elevation/h27-samples.json` and `elevation/h28-samples.json`.
- Mapillary, 15 frames in `street/` (CC BY-SA 4.0; creators and links in `street/SOURCES.md`). They show the trellis beams and MSE walls, the hammerhead piers of the curved 2 South flyover, the Henday decks over Calgary Trail, and the barriers.
