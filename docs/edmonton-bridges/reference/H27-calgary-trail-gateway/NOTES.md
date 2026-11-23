# H27 and H28 modeling brief: Henday / Calgary Trail / Gateway Boulevard and the Blackmud Creek arches

Edmonton. Anthony Henday Drive (Highway 216) runs east and west here, on the south side of the city. It is the southwest ring road. The H27 interchange sits at Calgary Trail (Highway 2) and Gateway Boulevard. The H28 arches are immediately west of it, over Blackmud Creek. This is one task. The arches without the interchange, or the interchange without the arches, leaves a hole in the landmark on a north departure from CYEG.

Centres used by the project: H27 at 53.437, -113.491. H28 at 53.437, -113.496. The combined centre is 53.437, -113.4935.

**Correction (2026-11-23, model build):** H28 is at **53.4348, -113.5134**, not -113.496. Blackmud Creek crosses under the Henday about 1.5 km west of H27 (OSM ways 25477513, 25477514, and the ramp pair 25477544 and 115754686). The ways at -113.496 listed below under H28 are H27 trellis and girder decks over the West Edmonton Mall ramp. See HANDOFF-T2.md.

This is not H29 Henday at 111 Street (53.435, -113.514), and it is not T134 the Blackmud Creek LRT span (53.4409, -113.5185). It is not W88 Whitemud / Calgary Trail (53.4804, -113.4938), which is a separate interchange about 4.5 km north. The 2005 interchange and the 2005 arches are the subject. Present-day package only.

Numbers below are cited. Where sources disagree, both are given. Nothing is averaged. No height is built by adding or subtracting citations.

## Interchange

**Type.** Alberta's first three-level interchange (Canadian Consulting Engineer, 2008, "Three Crossings On Henday"; Wikipedia, citing the same article). Wikipedia says Henday has two three-level interchanges and does not name the second.

**Flyovers.** Four grade-separated trellis-beam structures, at varying high skew. On two of them the skew runs from 50 to 80 degrees, south to north (CCE 2008). The beams are post-tensioned, according to a search summary of the CCE article; the verbatim fetch did not confirm this. The beams are spaced at 8 m, up from a normal 6 m (CCE 2008). Each span is 44 m, against a minimum of about 22 m (CCE 2008). The beams are 600 mm wide at the bottom, 1,000 mm at the underside of the top flange, and the top flange is 1,300 mm wide (CCE 2008).

**Supports.** Integral abutments. No piers next to the roadway (CCE 2008).

**Span lengths and total length.** Not published. The 44 m is the trellis span. No overall length for the interchange flyovers is published in the sources checked.

**Bridge ways.** The inventory row says twelve bridge ways. The OSM extract for the H27 object shows four deck ways close to the centre (see geometry.json). The rest are ramps and cross roads. The twelve is not reproduced. The four decks are: two Henday ways (eastbound 100.2 m and westbound 110.2 m, plan length), one one-lane eastbound link (101.4 m), and one two-lane westbound link to Calgary Trail (99.2 m). These are plan lengths only.

**Layer and clearance.** Not published. The OSM layer tags (1) are mapper tags and are not clearances.

## Blackmud Creek arches

**Type.** Three cast-in-place concrete, deck-stiffened, open-spandrel arch bridges (CCE 2008; Wikipedia, same citation). One bridge carries each direction of the two-lane divided Henday. The third carries a ramp from the Calgary Trail interchange (CCE 2008). Wikipedia calls them "three arch bridges over Blackmud Creek" and gives no dimensions.

**Completion.** Completed September 2005 (CCE 2008). The inventory says opened 2005. That is the same year, and the source says completed.

**Structure length and spans.** Each structure is 76 m long (CCE 2008: "Each 76-m long bridge structure has a 15-degree skew"). Each has a 40 m middle span, with about 18 m side cantilevers on each side (CCE 2008). 18 + 40 + 18 = 76. The creek was realigned to shorten the spans (CCE 2008). The creek distance is not given.

**Arch ribs.** Two ribs per structure. Each rib spans 40 m with a 7.5 m rise, is 7.0 m wide, and is 0.4 m thick (CCE 2008).

**Piers.** No piers are mentioned in the arch description. The arches stand on the embankments. Pier count is not published.

**Deck slab.** A 1.5 m deep cellular slab with five cells per bridge, and a cantilevered top slab reaching up to 4 m out from the main girders (CCE 2008).

**Skew.** The roadway runs at 45 degrees to the creek. Each structure has a 15-degree skew (CCE 2008). The two skew values are for different things. Both are given.

## Bridge

**Deck above the creek.** The roadway is 17 m above the creek bed (CCE 2008). This is the figure in the freeway-bridges.md row, "about 17 m". Elevation above sea level is not published. A creek bed elevation is not published.

**Embankments.** The arch thrust partly supports 16 m high embankments on each side (CCE 2008). The 16 m is the embankment height. It is not the deck height.

**Clearance under.** The 17 m above the creek bed is the deck height. No vehicle clearance under the arches is published.

**Girder or arch depth.** The arch rise is 7.5 m per rib (CCE 2008). The slab is 1.5 m deep. The total depth from the top of the deck to the soffit of the arch is not published.

**Rehabilitation.** None found in the sources checked.

## Approaches

Plan geometry only. The extract gives no gradients. OSM approach polylines are plan lines and are not grade points.

**Henday, east of the interchange.** Several approach ways, from 39.5 m to 354.0 m plan length (geometry.json). The west end of the H27 flyovers runs into H27 approach and link ways. Gradient and the point where each road meets grade are not published.

**Henday, between the interchange and the arches.** Two approach ways sit in the creek gap, one on each carriageway (41985704, 118.4 m; 41985557, 65.7 m). They are tagged approach, not bridge. The arch structures may be in those ways. OSM does not say. The two CCE structure lengths (76 m each) do not match a single OSM way.

**Henday, west of the arches.** Two approach ways run west from the arches: 707.6 m and 390.5 m, both clipped at the edge of the download box. Gradient is not published.

**Calgary Trail and Gateway Boulevard.** The cross roads and the Calgary Trail 2 South ramp are in geometry.json under cross_roads. They are plan only. Calgary Trail and Gateway Boulevard are Highway 2 and carry the ring's start (Alberta Transportation starts the ring here and measures mileage clockwise, as Wikipedia states). Their profile through the interchange is not published.

**Gradient.** Not published for any approach.

## Deck

**Elevation.** Above sea level: not published. Datum: not published.

**Thickness.** Slab 1.5 m deep (CCE 2008).

**Width of each carriageway.** Not published. Two lanes each way is the CCE description ("one for each of the two-lane divided highways") and the OSM lane tag.

**Width of the crossing.** Not published as an overall figure. The CCE article says the deck slab is cast to the roadway width of the flyover. The width is not given.

**Lanes.** Two each way on the Blackmud decks (OSM lanes=2). The Wikipedia text says "three westbound lanes continue across Blackmud Creek past 111 Street to 119 Street". That sentence is about the route past 111 Street and does not give a lane count for the arches. The source disagrees with the OSM and CCE two-lane count. Both are recorded. The two-lane figure is used for the arch decks. The three-lane figure is recorded but not used.

**Sidewalk or path.** None mapped on the Blackmud decks. The OSM extract has no footway on the arch structures. The CCE article describes a pedestrian path inside the Whitemud Creek arch, which is a different structure. It is not used here.

**Crossfall.** Not published.

**Longitudinal grade.** Not published.

## Still missing

- Deck elevation above sea level, and the vertical datum.
- Creek bed elevation, and the creek width at the arches.
- Pier count for the H27 flyovers and the H28 arches (the arch article describes none).
- Carriageway and lane widths for each structure.
- Overall lengths of the H27 trellis flyovers and each span length beyond the 44 m trellis span.
- Crossfall and longitudinal grade on each structure.
- Gradients of the approaches, and where each road meets grade.
- Which OSM ways are the three arch structures. The OSM extract does not settle whether ways 41986110 and 22915670 are the Blackmud ramp. OSM way 22915670 (316.4 m, north to south) is the best candidate; it is not confirmed.
- The Alberta Transportation structure inventory for Highway 216 at Blackmud Creek and at the interchange. The Structure-Export file was searched for and not found through the search tool.
- The Balakrishnan TAC paper on trellis-beam bridges. It is a PDF, and the fetch tool returned binary data. Its content was not read.
- The engineering paper cited in the CCE article. Not located.
- An openly licensed photograph of the arches, the deck, the piers, or the approaches. See SOURCES.md.
