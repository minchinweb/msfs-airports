# R12 James MacDonald Bridge — modeling brief

Edmonton. Haunched concrete girder across the North Saskatchewan River. Opened in October 1971. Centre used by the project: 53.536, -113.488. Carries 97 Avenue and 98 Avenue, six lanes.

This is not the Low Level Bridge. The Low Level is the two through-truss spans immediately downstream: the 1900 northbound span and the 1948/1949 southbound span. Their decks, piers, and truss geometry are in `docs/edmonton-bridges/reference/R13-low-level/`. Where a photograph here shows those trusses, the concrete girder is this bridge and the trusses are the other one.

No source checked here describes a bridge that this girder replaced. The present structure is the 1971 girder. Wikipedia says three further spans were planned south of this one, for the downtown freeway loop, and were not built. Do not model those spans.

Numbers below are cited. Where two sources disagree, both are given. A blank in the "Still missing" list has no published figure in the sources checked. Nothing here was filled in by adding one citation to another. OpenStreetMap `width` tags are mapper tags. They are not deck elevations. No `maxheight` tag is stored on these ways.

## Bridge

**Type.** Girder (Structurae). The Alberta Transportation bridge-aesthetics study, April 2005, captions this bridge "Nicely proportioned haunched girders," and on the river-crossing page says haunched girders were used for the Edmonton bridge. The Edmonton Journal's recap of the 2007 work says the plan was to strengthen concrete girders. Haunched, and concrete, are both published. The study does not say box girder or I-girder. The 6 August 2011 photograph shows several concrete girders side by side, with cross-frames in the gaps, deeper at the pier than toward midspan. That soffit is not a closed box. A published name for the cross-section, beyond haunched concrete girder, was not found.

The bullet in the same study that says "Increased depth at middle of main span" sits with the Puerto Vallarta pedestrian bridge. It was not used here.

**Spans.** A span count is not published. Span lengths are not published. The 3 June 2008 photograph shows two concrete pier shafts in the channel. The abutments are outside that frame. A count was not taken from the photographs.

**Length.** Wikipedia's infobox states 359.7 m (1,180 feet). The article text does not cite a measurement for that length. Structurae states 359.66 m. The 359.7 m and the 359.66 m are both published. They were not averaged.

The OpenStreetMap westbound centreline, way 25455305, is 381.4 m. The eastbound centreline, way 25455308, is 375.6 m. Use the OpenStreetMap lines for the plan shape. The mapped length and the stated structure length are different extents.

**Which carriageway is which.** The extract has two road centrelines, both tagged `bridge:name=James MacDonald Bridge`, three lanes, one-way, asphalt, width 11.1. Way 25455305 runs from the east end to the west end, so the traffic is westbound. Its nodes lie north of way 25455308. Way 25455308 runs from the west end to the east end, so the traffic is eastbound. It is the southern centreline.

The horizontal distance between those two centrelines runs from 12.1 m to 19.1 m, and the average along the eastbound nodes is 13.9 m. That is the mapped spacing. It is not a published width of either carriageway, and it is not the width of the whole crossing.

One outline encloses both, way 626069071, tagged `bridge:structure=beam`. The beam tag is a mapper tag. A published source does not say the two directions are separate bridges. The Journal's "two approach bridges" are named with this bridge as 1971 works. The extract does not contain a second river span.

**Piers.** Pier count, pier height, and a foundation are not published. The photographs show concrete wall shafts. The 6 August 2011 photograph shows an opening through the shaft near the water, and the girders bearing on the cap. A published name for that pier was not found.

**Clearance above the river.** Not published. No navigation clearance is published. No elevation above sea level is published for the deck, the soffit, or the water. The red mark on the pier in the 2011 photograph was not measured.

Environment Canada gauge 05DF001 is at the Low Level Bridge and uses a local assumed datum. No source used here converts a gauge reading, or a clearance, into a geodetic deck elevation for this bridge.

**Rehabilitation that shows.** The Journal's recap: James MacDonald and two approach bridges, built in 1971. The 2007 plan was to repave the deck, replace the railings, strengthen the concrete girders, and repair the piers. The work was planned for March to November 2007 and was finished in January 2008. The Journal gives the estimate as $12.5 million and the final cost as $16.5 million. A CBC report of 12 October 2006 had put the same work at $8 million to $10 million. Those figures were not averaged. The Journal does not describe a new girder outline or a new pier shape. It does not describe the new railing.

Lorac Construction's page says the City had the bearings and their housings rehabilitated on the underside, with a snooper truck. The page gives no date and no dimension. It does not describe a new soffit.

The photographs saved here are dated June 2008 or later, so they are after the January 2008 reopening. A photograph of the railing from before the closure was not saved.

## Approaches

Wikipedia puts Cloverdale at the east end and Rossdale at the west end. The east end is the south bank. The west end is the north bank. OpenStreetMap names the west-end roads 97 Avenue NW and the east-end roads 98 Avenue NW. Wikidata says the bridge carries 97/98/101 Avenue. 101 Avenue is not the name on any way in this extract.

The two avenues are not one road with two names. 97 Avenue is the Rossdale end. 98 Avenue is the Cloverdale end. A second way named 98 Avenue NW lies west of the Rossdale end and does not meet the deck. That way is not the Cloverdale road.

No source gives the elevation change, or the point where either road meets natural grade. The Southeast LRT route-selection report says 98 Avenue has 7.5 percent grades, in the section on using this bridge for LRT, and that those grades are too steep for LRT. It does not say which block, and it does not give an elevation change. The 7.5 percent was not turned into a height. It is not a grade on the river span.

The OpenStreetMap ways below match the live node counts on 14 October 2026. A complete way is still only the mapped polyline. Its far node is not a surveyed grade point.

**West, Rossdale, 97 Avenue.** The two carriageways do not share one approach way.

Westbound. Way 25455281 leaves the deck: four lanes, width tag 14.8, 184.9 m. Node order is away from the bridge. The deck it leaves is tagged three lanes and width 11.1.

Eastbound. Way 432373966 comes onto the deck: three lanes, sidewalk tagged no, width tag 11.1, 154.8 m. Node order is toward the bridge.

The two ways are not the same length, and they are not the same lane count. 100 Street NW, way 302605553, passes this end and does not share a node with the deck. It is a cross street.

**East, Cloverdale, 98 Avenue.** The carriageways do not share one approach way. Wikipedia describes the interchange on this bank as the remnant of the freeway plan: ramps laid out as temporary connectors, and still there. The February 2009 photograph looks from downtown toward the Muttart and shows this end, the curving roads, and concrete piers. The river span is at the left of that frame. The June 2008 photograph is 98 Avenue in Cloverdale, as its description states. The girder is not in that frame. No gradient was read from either photograph.

Westbound. Way 926792878 comes onto the deck: three lanes, width tag 11.1, 68.9 m. Node order is toward the bridge.

Eastbound. Way 106711215 leaves the deck: three lanes, width tag 11.1, 33.1 m. Node order is away from the bridge. Way 926792877 continues 98 Avenue from there: two lanes, 40.6 m. The lane count on the mapped road drops from three to two. Way 926792876 is a two-lane link off the same node, 40.4 m. It is not named 98 Avenue.

Way 106711220 is a one-lane ramp off the eastbound deck, 308.1 m. Node order is away from the bridge. A live read on 14 October 2026 tags `destination:street` as South Scona Road. That tag is not in the extract. The ramp is not a second river span.

99A Street NW meets the mapped outline at this end. It does not meet either road centreline. It is a cross street.

## Deck

**Elevation.** Missing above sea level, and the vertical datum is missing. Soffit elevation is missing. Gauge 05DF001 was not converted.

**Thickness.** Not published. The Edmonton Sun, 26 May 2012, says the 2007–08 work was to have left an asphalt surface and instead left milled concrete. OpenStreetMap tags both carriageways `surface=asphalt`. Both are published. Neither is a thickness.

**Width.** A published width of one carriageway, and of the whole crossing, was not found. Wikipedia's infobox leaves width blank. Each road centreline is tagged `width=11.1`. The westbound 97 Avenue way off the deck is tagged `width=14.8`. No published source found states 11.1 m or 14.8 m.

The mapped outline is 29.9 m across the west end. The east end is a 37.3 m edge and a 2.9 m jog. That is the OpenStreetMap outline, not a published structural width. The 13.9 m figure is the average spacing of the two centrelines. It is not a width either.

**Lanes.** Six in the project list and in the Wikipedia infobox: motor vehicles, and pedestrians. The infobox does not cite a count for the six. Each OpenStreetMap carriageway is tagged three lanes, 60 km/h. Three westbound on the north centreline, three eastbound on the south centreline.

Wikipedia also says this span was designed to carry the five westbound collector lanes of the south leg of the downtown freeway loop, and cites Alberta Roads for that sentence. The five and the six are both in the article. The five was not used as the present lane count.

The infobox daily traffic is 50,095 in 2023, cited to a Google spreadsheet titled AAWDT. That spreadsheet was not opened.

**Sidewalks.** One mapped sidewalk, on the north side, outside the westbound carriageway. Way 673730078 is tagged a concrete footway, 367.4 m. It lies north of way 25455305. The offset from that centreline runs from 9.2 m to 14.7 m. That offset is the mapped plan distance. It is not a sidewalk width.

A live read of way 25455305 on 14 October 2026 tags `sidewalk:left=no` and `sidewalk:right=separate`. The way runs east to west, so the right side is the north side. The eastbound way, 25455308, has no sidewalk tag on that read. The extract did not store the sidewalk tags. No published source found states which side the sidewalk is on, or its width. The concrete tag is the mapper tag.

Way 1264715853 continues the concrete walk off the Rossdale end. Steps, way 226985622, leave the same node. A short footway, way 673730077, sits at the Cloverdale end of the bridge walk. Those are paths off the sidewalk. They are not the avenue climbs.

**Crossfall and grade.** Not published for the span. The 7.5 percent figure is the LRT report's grade for 98 Avenue. It is not a crossfall, and it was not placed on the span.

**maxheight.** No `maxheight` tag is stored on the bridge ways, the avenue ways, or the ramp in the extract. The live read on 14 October 2026 did not add one. There is no mapper clearance here to mistake for a deck elevation.

## Still missing

- Deck elevation above sea level, and the vertical datum. Soffit elevation.
- Clearance from the roadway or the soffit down to the river, and a navigation clearance. The red mark on the pier in the 2011 photograph was not measured. Gauge 05DF001 is an assumed datum at the Low Level Bridge.
- Span count and span lengths. The 359.7 m and the 359.66 m are totals. The two pier shafts in the 2008 frame are not a published count.
- Girder depth, at the pier and at midspan. A published name for the section beyond haunched concrete girder. The 2011 photograph shows separate girders and cross-frames. It was not measured.
- Pier count, pier heights, and the plan size of the shafts and the foundations. A published name for the opening through the pier in the 2011 photograph.
- Where the two approach bridges in the Journal's 2007 recap are, and whether they are the Cloverdale ramp and the park span or another structure. The extract has one river outline.
- Deck thickness. The Sun's milled concrete and the OpenStreetMap asphalt tag are surfaces. They are not a thickness.
- A published width of each carriageway and of the whole crossing. What the OpenStreetMap tags `width=11.1` and `width=14.8` measure. The 13.9 m figure is the mapped centreline spacing. The 29.9 m and 37.3 m figures are the mapped outline.
- Lane width. The Wikipedia sentence that says five westbound collector lanes is the freeway design. It is not a present lane width.
- Sidewalk width. A published confirmation of the north side. The live tags `sidewalk:left=no` and `sidewalk:right=separate` are mapper tags, and the extract did not store them.
- Crossfall. Longitudinal grade on the span. The 7.5 percent figure is 98 Avenue in the LRT report, and that report does not locate the block or give the elevation change.
- Where 97 Avenue at Rossdale and 98 Avenue at Cloverdale meet natural grade, and the length, gradient, and elevation change of each climb. The OpenStreetMap lengths are plan lengths of the mapped ways. The westbound road leaves the deck tagged four lanes, and the eastbound road arrives tagged three lanes. The eastbound road leaves the Cloverdale end tagged three lanes and the next 98 Avenue way is tagged two lanes.
- Whether the January 2008 railing replacement changed the fascia railing in the 2011 photograph. The Journal does not describe the new railing.
- An openly licensed close photograph of the river-span deck, and an openly licensed close photograph of the Rossdale approach. The Cloverdale approach is the February 2009 frame. The girder is not in the June 2008 frame of 98 Avenue.
