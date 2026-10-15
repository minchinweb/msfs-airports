# G116 Hawrelak access (Mayfair Bridge) - model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

Reviewed from this folder only: NOTES.md, SOURCES.md, geometry.json. The folder has no photos.

## Verdict

**Blocked** for a faithful model. The folder gives a plan outline from OSM and nothing else. There is no photo, no deck elevation, no clearance, no width, no girder or pier type, and no colour. A generic grey placeholder deck could be built, but every dimension except plan position would be a guess.

## What the folder gives me

| Fact | Value | Source |
| --- | --- | --- |
| Identity | Emily Murphy Park Road over Groat Road. Also "Mayfair Bridge". Not the river span (R8). | NOTES.md "What it is" |
| Alberta file | 76535, MAYFAIR BRG, built 1966 | NOTES.md, SOURCES.md, geometry.json `dimensions` |
| Span count | 3. This is a read of a printed "GS 3" by column pattern, not a stated fact. | NOTES.md "Type" |
| Work | Rehabilitation 2018 (Journal) to 2021 (Al-Terra). Not replaced. What changed is unknown. | NOTES.md "Work that shows" |
| Centre | 53.5322, -113.5383 | NOTES.md, geometry.json |
| Deck plan | Bridge-tagged ways, layer 1, two lanes, one-way, 50 km/h, asphalt or paved. Node lists in geometry.json. | geometry.json `decks` |
| Cycleway on bridge | Way 160418783, concrete, 61.0 m, three nodes, width tag "1.5 m" (unconfirmed) | geometry.json |
| Road under | Groat Road NW, secondary, 2 lanes, one-way, 60 km/h, asphalt, no sidewalk, foot=no. Ways 648645164 (918.2 m) and 944414125 (607.8 m). | geometry.json `approaches` |
| maxheight tag | 5.3 on way 648645164. Not a clearance. | NOTES.md "Clearance" |
| Ramps and approaches | Ways 106605008 (238.3 m), 106605090 (154.4 m); park-road pieces 59.4, 36.6, 36.1, 31.7 m. Plan lengths only. | NOTES.md "Approaches" |
| Deck elevation, clearance, width, span lengths | All null | geometry.json `dimensions` |

Conflicts inside the folder:
- Deck year: 1966 (Alberta row) versus a 2018-2021 rehabilitation. Not a true conflict, but the look is the rehabilitated look and nothing describes it.
- Rehabilitation completion: 2018 (Journal, Graham single season) versus 2021 (Al-Terra). Al-Terra's date probably covers the whole contract.
- Naming: Global News reverses the roads ("Victoria Park Road bridge over Groat Road"). NOTES.md already flags this.
- Way 160418783 (cycleway, 61.0 m) is in `decks`. Ways 160418782 (31.4 m) and 201157172 (51.9 m) are `excluded` with the same width tag. It is unclear whether the cycleway runs on the deck on both sides or only one.
- Centre point vs deck: the stated centre sits about 40 m from the plotted deck middle. Small, but use the node lists, not the centre.

## Build spec I would use from this alone

Everything marked (derived) is my arithmetic on geometry.json nodes. Everything marked (assumed) is not in the folder.

**Placement and heading**
- Deck runs east-west (derived). The cycleway goes from 53.532394, -113.53855 to 53.53237, -113.537632. Plan length 61.0 m (given), about 61 m by my calculation.
- Groat Road passes under at roughly north-south (derived from way 648645164 nodes near 53.5322-53.5324, lon about -113.5381). The crossing is near square (derived, rough).
- North-south extent of the mapped deck: park-road carriageway at about lat 53.53214 to the cycleway at about lat 53.53237. That is about 25 m centre to centre (derived). The two one-way carriageways diverge, so the plan is a wedge or a Y, not a plain rectangle.
- Carriageway paths (use the node lists for the lines): south carriageway ways 106605009 + 106605020 + 501599774; north carriageway ways 106605261 + 160418786; cycleway 160418783 along the north edge; short stubs 474575066, 474575069, 474575072 at the ends.

**Components**
1. Deck slab following the carriageway and cycleway lines (width assumed: 2 lanes of about 3.5 m per mapped way; not in the folder).
2. Three spans (count from the printed 3; lengths unknown). Two intermediate supports or piers (assumed from a 3-span read).
3. Girders under the deck (type unknown).
4. Railings or parapets on both outer edges and between the carriageway and cycleway if separated (type unknown).
5. Approach ramps leading off the bridge ends. Plan lengths are given; heights are not.
6. Abutments and any embankment (not described).

**Elevation**
- No deck AGL or ASL. Groat Road is a cut under the deck, so deck height above Groat Road is the one number I need. I would set it to an assumed typical road clearance only as a placeholder, and mark it as an assumption. The 5.3 tag must not be used.

**Materials and colour**
- Deck: asphalt (given). Cycleway: concrete (given). Everything else: no colour read from any source. I would use neutral concrete grey as a placeholder.

**LOD ideas**
- Far LOD (1,000-3,500 ft AGL): deck ribbon and cycleway ribbon, flat grey, with a darker strip for the carriageways. The plan geometry is good enough for this.
- Near LOD: add girders, piers, parapets. Not buildable from this folder.

## Gaps and conflicts (worst first)

1. No deck elevation or clearance over Groat Road. The bridge only reads as a bridge if the deck sits above the road. Hurts most.
2. No photograph at all. Girder type, pier shape, railing, and the rehabilitated look are all unknown.
3. No deck width, lane width, shoulder or sidewalk width. The 1.5 m cycleway width is an unconfirmed OSM tag.
4. No span lengths. The count of 3 is an inference from a column pattern.
5. Mapped plan is a ramp pair plus stubs, not a single deck outline. I cannot tell which parts are on structure and which are on embankment.
6. No colour or texture reference.
7. No terrain information: the cut that Groat Road runs in, side slopes, and whether the sim terrain will already be shaped to the road.
8. No lighting, collision or road-surface information.

## Handoff requests

| # | Request | Blocking? |
| --- | --- | --- |
| 1 | Find deck elevation ASL and Groat Road surface elevation ASL at the crossing (survey, City of Edmonton drawing, LiDAR DEM/DSM). The difference gives the clearance. | Blocking |
| 2 | Get a photo from Groat Road looking along the road at the underside: girder count and type, pier or column shape, abutment style. Note the date (post-2021 preferred). | Blocking |
| 3 | Get a photo from the deck: parapet or railing type and height, whether the cycleway is separated from the carriageway, kerb and median detail. | Blocking |
| 4 | Get an overhead or oblique image of the crossing to confirm which mapped segments are on structure and where the two carriageways split. | Blocking |
| 5 | Measure deck width, lane width, shoulder and cycleway width (city drawing, rehabilitation tender, or a scaled aerial). | Blocking |
| 6 | Find span lengths and the pier locations in plan (tender drawings, Alberta bridge inventory sheet for file 76535). | Blocking for the near LOD; nice-to-have for the far LOD |
| 7 | Say what the 2018 rehabilitation changed on the visible silhouette (new railings, new deck, girder repair). | Nice-to-have |
| 8 | Record concrete and parapet colour from the photos and any steel colour. | Nice-to-have |
| 9 | Say whether the sim terrain or the existing OSM-based road in the sim will cut Groat Road under the deck. If not, I must model the road cut (and flatten or exclude terrain) myself. Say how much. | Blocking for placement; check in the sim |
| 10 | Say whether street lights stand on the bridge, and whether Groat Road is lit under it. | Nice-to-have |
| 11 | Say whether the bridge needs a drivable road surface and collision, or is visual only. Groat Road and Emily Murphy Park Road are already roads in the sim. | Nice-to-have, but decide before building |
| 12 | Confirm whether the cycleway is on both sides of the deck or one (compare ways 160418783, 160418782, 201157172). | Nice-to-have |
