# R14 Tawatinâ Bridge — modeling brief

Edmonton. Valley Line LRT, low-floor, under catenary. Extradosed concrete box over the North Saskatchewan River, with a shared-use path hung underneath. The path opened on 12 December 2021. The Valley Line Southeast opened on 4 November 2023. Centre used by the project: 53.5401, -113.4772. That point is the OpenStreetMap deck centre in `bridge-geometry.json` (`estimated_centre` false). Wikipedia’s coordinate, 53.540250, -113.477194, is the same bridge.

The river crossing is one structure. The elevated guideway that continues south over Henrietta Muir Edwards Park, across 98 Avenue, and down toward the Muttart ramp is the same mapped bridge, not a second bridge. Low Level and James MacDonald are upstream to the west. Dawson is downstream. They are not in this folder.

The short tunnel on the north valley wall has no station. Do not model the tunnel. Record of where the elevated structure ends is under Approaches.

Numbers below are cited. Where two sources disagree, both are given. A line in "Still missing" has no published as-built figure in the sources checked. Nothing here was filled by adding one citation to another.

## What the project notes say

Checked against the sources and against the OpenStreetMap extract of 2026-10-14.

- Centre 53.5401, -113.4772. Confirmed. It is the deck centre in `bridge-geometry.json`.
- Valley Line LRT. Confirmed. Both bridge-tagged tracks are named Valley Line.
- Opened 2021, line opened 2023. Confirmed. The shared-use path opened 12 December 2021. The line opened 4 November 2023. The concrete closure pour was 10 September 2020, before either opening.
- Extradosed concrete box. Confirmed. The project agreement requires an extradosed bridge. The thesis, Wikipedia, American Bridge, and Structurae all describe that structure. The upper deck is prestressed concrete. The lower deck is steel.
- Pylons 24–30 m above the deck. Confirmed as a requirement, not as a surveyed height. The project agreement says pylon heights, measured from the top of deck, shall be a minimum of 24 m and a maximum of 30 m. American Bridge calls them 30-metre pylons and does not restate the datum. No surveyed as-built height was found.
- Pedestrian deck hung underneath. Confirmed. Steel hangers from the box soffit. The path runs through openings in the river piers.
- Mapped bridge ways continue south to about 53.5374. Confirmed. The south ends of the bridge-tagged tracks are 53.537415, -113.477787 and 53.537395, -113.477728.
- That south run is over 98 Avenue and down to the Muttart ramp, and it is part of this bridge. Confirmed as one set of bridge-tagged ways. The project agreement gives the river bridge and the south guideway separate section titles. They are one corridor. The pedestrian deck does not continue over 98 Avenue.
- About 470 m per track from 53.5416 to 53.5374. Confirmed. The bridge-tagged tracks run from 53.541573, -113.477161 and 53.541572, -113.477077 to the south ends above. Horizontal length is 471.5 m on the west track and 473.5 m on the east track. `lrt-tracks.json` rounds the same pieces to 472 m and 474 m.

## Bridge

**River span and south guideway.** These are different lengths.

The river bridge is 260 m, in three spans: 100 m, 110 m, and 50 m. That length is in the IABSE abstract (Tarasuik and Rodgers, 2019), on the American Bridge project page (260 m, also given as 853 ft), in the Vendiola thesis (2023), on Wikipedia, and on Structurae. The longest span is 110 m. The north main span is the 100 m. The south main span is the 110 m. The side span is the 50 m continuous box. American Bridge, the thesis, Wikipedia, and the project agreement’s pier spacing all describe three spans. Structurae’s project type says "two-span" and, on the same page, lists span lengths 100 m – 110 m – 50 m. The three-span description is the one used here.

The OpenStreetMap river piece matches that 260 m. From the north bridge nodes at 53.54157 to 53.539229 the west track is 260.9 m (ways 636427023 and 1221895803) and the east track is 260.8 m (way 1221895804).

South of 53.539229 the ways stay tagged as bridge for another 210.6 m (west) and 212.7 m (east), down to 53.5374. That is the south elevated run. No as-built length of that guideway was found as a published metre figure. The 2013 environmental assessment, written as reference design and marked approximate in that report, said the river bridge and the elevated guideway across the floodplain to just north of 98 Avenue together span approximately 380 m. The same report’s elevation drawing, as extracted from the figure, labels the river spans 100 m, 110 m, and 50 m and three further spans of 40 m, and the drawing marks those 40 m spans approximate. 260 m plus three 40 m spans is 380 m. The 40 m labels are figure text, not a sentence in the report. The as-built south run in OpenStreetMap is longer than 120 m because the bridge tag continues over 98 Avenue and down the ramp, which the 2013 text treated as further structures.

**Pylons.** Two pylons, both on the north river pier, with no structural member connecting them above the deck. That is section 2-11.5.3 of the project agreement (8 February 2016). The south river pier matches the north pier only up to the superstructure, so it does not carry pylons above the deck. The thesis describes one open-shaped tower (Pier 1) with two cable planes. American Bridge says seven stay cables run through each leg of the 30-metre pylons. Structurae lists pylon number as 1. That count disagrees with the agreement’s two pylons. The agreement is the one that defines the pair, and the photographs show two legs above the one pier.

Height, measured from the top of deck: minimum 24 m, maximum 30 m (project agreement, 2-11.5.3.P). American Bridge states 30-metre pylons. That is the top of the allowed range. The page does not say "above the deck." No survey of the built height was found, so the as-built height is not filled in as a single measured number. In elevation the pylons taper, narrowest at the top. The agreement limits that taper to 1 horizontal in 60 vertical, and limits the width at deck level, viewed in elevation, to 4 m. Exposed anchors on the pylons are not permitted.

**Stays.** The counts disagree, and they can describe one saddle arrangement:

- American Bridge: seven stay cables through each leg, on a Vorpsann saddle, 40 strands in each cable. The stays act as external post-tensioning, with a large longitudinal force and a small uplift.
- Thesis: 14 stays in total, seven in each of two outer planes. Stay angles 17.4° to 26.2° from the horizontal.
- DIALOG, at the September 2020 closure: 28 stay cables. TransEd, the same week: the seventh and final set of cable stays was installed in August 2020.

Seven through-cables on each of two legs is 14 cables if each cable is counted once as it passes the saddle, and 28 ends if each side is counted. The sources are left as published. The agreement required at least five and at most ten cables on each side of each pylon, equally spaced, and not crossing a vertical plane through the outermost rails.

**Girder.** Post-tensioned trapezoidal box, 3.5 m tall and 11 m wide (thesis; Structurae upper-deck depth 3.50 m and width 11 m). The thesis says the bottom slab is thickest in the two segments next to the tower and then constant, and it gives no thickness. The agreement allowed either a constant depth of at most 3.5 m from top of deck to soffit, or a variable depth of at most 4.0 m at the two river piers tapering to at most 3.0 m at midspan. The thesis describes the 3.5 m box, not the variable option. The soffit over the path is solid, and the outside faces slope at most 1 horizontal in 2 vertical (agreement). The girder is cast monolithically with the stay tower. North abutment, Pier 2, and the end of span 3 are guided pot bearings (thesis).

The north main span was cast in 20 segments: 5.4 m next to the tower, seventeen segments of 5 m, a 4 m segment, and a 1 m closure. The south main span was 21 segments: 5.4 m, seventeen of 5 m, 4 m, 5 m, and a 1 m closure. The 50 m side span is a continuous box, not segmental in that description (thesis). American Bridge’s scope was balanced cantilever. The closure pour filled a one-metre gap on 10 September 2020 (TransEd).

**Piers.** Two piers in the river. The agreement allows a maximum of two. The north river pier is in line, east-west, with the north pier of the old Cloverdale footbridge, which this bridge replaced. A second river pier may sit 110 m south of it, in line with the old south pier. No pier is allowed between the north river pier and the north abutment. The first pier on the south bank is at least 160 m from the north river pier, which is the 100 m span plus the 110 m span plus the 50 m side span. Wikipedia’s infobox says two piers in water. Structurae lists pier number as 1, which disagrees with the agreement and with Wikipedia. The photographs show the pylon pier in the channel and a second concrete pier further along the span.

Below the shared-use path each river pier is to read as a single mass. The path passes through an opening in each pier. The base, viewed in section, is at most 8.5 m wide just above the pile cap (agreement). Piers through the park are required to be at least 35 m apart along the guideway, and the span immediately north of 98 Avenue at least 30 m. Those are minimums. An as-built pier count and spacing for the south guideway were not found. The 2013 assessment said the guideway through the park was then shown as three spans, and the 98 Avenue crossing as three spans of its own.

**Clearance over the river.** No as-built clearance, and no deck elevation above sea level, was found. Two design water levels are published, and they are not the same figure:

- 2013 assessment: a 10 m navigation window at the normal high water level of 615.60 m, the level tied there to a flow of 1000 m³/s, set off the Edmonton Queen. The text says this is slightly greater than the clearance of the Cloverdale footbridge. It does not say whether 10 m is to the pedestrian soffit, and it does not name a vertical datum.
- Project agreement, 2016: vertical clearance of the bridge, including the path, at least the clearance of the existing Cloverdale footbridge along the whole path. Piers need not meet that clearance if Transport Canada accepts them. The navigation water level for vessel collision is not less than EL 615.9. The datum is not named in that clause either.

The 10 m and the two water levels were not turned into a deck elevation.

**Clearance over 98 Avenue.** No as-built figure was found. The agreement’s general rule is 5.4 m minimum between a roadway and the underside of a transportation structure, unless a structure-specific clause says otherwise. The 98 Avenue clause does not set a different permanent clearance. It does say that during construction the clearance may temporarily be 4.0 m. The 2013 assessment said a minimum of 5.5 m, matching the 98 Avenue pedestrian bridge to the east. OpenStreetMap way 1098987149, the carriageway under this guideway, is tagged `maxheight=5.9`. That is a map tag, not a design clearance, and it is not treated as the clearance.

## Approaches

The LRT does not climb a hill on the north bank. It comes out of a tunnel. On the south it leaves the elevated structure on a ramp immediately north of Muttart stop. Gradients and elevation changes for the built approaches were not found. The grades below are labels on the 2013 reference-design drawings, which the assessment says should be treated as approximate.

**North (Louise McKinney).** The portal is on the upper slope of the north valley wall, at the northeast corner of Louise McKinney Riverfront Park (2013 assessment). It has a covered portion and an open-top portion, and one entrance for two tracks. The project agreement requires the north abutment to be monolithic with the North River Bank cut-and-cover tunnel and the tunnel approach.

In the 2026-10-14 extract the bridge tag ends at 53.541573, -113.477161 and 53.541572, -113.477077. The next 42.9 m and 43.4 m (ways 650830876 and 672849774) are tagged neither bridge nor tunnel. The tunnel tag then runs 489 m and 498 m, from 53.541958, -113.477194 and 53.541962, -113.477090 to 53.544909, -113.480895 and 53.544946, -113.480904 (`lrt-tracks.json`). There is no station on that tunnel. Quarters stop is at grade, off this tunnel. Do not model the tunnel. The elevated structure, as mapped, ends at the north bridge nodes. The mapped mouth of the tunnel is the north end of those 43 m ways. No gradient and no elevation change are published for that gap. A 2013 river-profile drawing labels one grade as −1.90%. A second grade on that drawing was not legible. It is a reference-design label.

The shared-use path, not the tracks, meets park grade on this bank. The 2013 text said the walkway would end at existing grade and join the path in the park. OpenStreetMap carries the bridge-tagged path to 53.541098, -113.477119 and then a 9.7 m cycleway off the bridge tag.

**South (Muttart ramp).** The project agreement calls the south abutment the transition from the bridge structure to the ramp, with a vertical face perpendicular to the track, immediately north of Muttart stop. The guideway depth is constant from the second pier on the south bank to that ramp, and a shallower through-girder is allowed over 98 Avenue if the vertical alignment needs it, for up to 40 m north of the north curb and on to the ramp. Whether that shallower girder was built is not stated.

The bridge tag ends at 53.5374, which is the mapped end of the elevated structure. From there to the mapped Muttart stop at 53.53621, -113.48000 the west track is 199.1 m and the east track is 213.1 m (clipped from ways 1280982479 and 1280982480). Those lengths are the mapped run to the stop. They are not a measured ramp, and they are not a surveyed point of meeting grade. The OpenStreetMap ways continue south past the stop; that continuation is not in `geometry.json`.

The 2013 98 Avenue drawing labels the descent beyond the crossing as −5.600% and then −0.275%, with the approach on fill after a pile-supported elevated approach. The same assessment said Muttart stop and its northern approach sit on a steep grade, and that five retaining walls were then conceived, 120 m to 230 m long and 2.5 m to 6 m high. Those are reference-design figures. No as-built gradient, length of climb, or elevation change was found.

The shared-use path ends on this bank in Henrietta Muir Edwards Park. It does not follow the LRT over 98 Avenue. The bridge-tagged path is 190.8 m, from 53.539384, -113.477135 to 53.541098, -113.477119. The 2013 text said the walkway would be approximately 210 m and would meet existing grade at each park. The 190.8 m is the bridge-tagged piece only.

## Deck

**LRT deck elevation.** Missing, above sea level and above the river. The vertical datum is missing. See the two water levels under Bridge. They were not converted to a rail elevation.

**Pedestrian deck elevation.** Missing on the same terms. Structurae gives the lower-deck depth as 0.40 m. That is thickness, not an elevation.

**Relationship.** The path is a separate deck, suspended below the box on steel hangers (agreement; thesis: steel rods; TransEd and DIALOG: steel shared-use path under the concrete deck). It passes straight through both river piers. At each pier the side walks shift outward into lookouts. The agreement requires those curves to start at least 20 m from the pier face, and a seating area of at least 7 m² on each side of each pier. The photographs show that bulge, the wood side decks, the asphalt centre, and the hangers in two lines.

The vertical gap between the decks is missing. The agreement requires the hanger spacing to be at least as long as the height from the path to the girder soffit, and it sets a general minimum of 3.5 m from a path up to the underside of a structure unless a specific clause says otherwise. The 2013 assessment said the walkway clearance would be 3.6 m, reduced to 3.0 m at the piers. That is headroom in the reference design, and the 3.0 m at the piers is below the later 3.5 m general minimum. Neither number is an as-built measurement of the gap.

**Widths.** Upper deck 11 m (thesis, Wikipedia, Structurae). Lower deck 8 m (thesis, Wikipedia, TransEd, DIALOG, Structurae). The agreement’s minimum functional width is 7.8 m: a centre strip at least 3.0 m, wood planks at least 1.8 m on each side, and at least 0.6 m clear from the edge of the centre strip to the hangers. DIALOG describes wood planks along each side and a smooth asphalt centre. The 2013 concept was a 3.0 m centre with about 2.0 m on each side, on a walkway about 210 m long. The built width cited after construction is 8 m.

**Tracks.** Two. Gauge 1,435 mm (Structurae). One northbound toward downtown, one southbound toward Mill Woods (Wikipedia). The thesis built its load model from the IFC drawings with lanes 3,420 mm wide, offset 2,250 mm from the centre of the deck, and it modeled the deck flat, without plinths. That offset is the lane definition in the model. It is not stated as the distance between the rails. Crossfall is not given. TransEd said six overhead-catenary poles would be installed on the bridge after the closure pour. That count is for the bridge as they described it in September 2020, which is the river span they had just connected.

**Thickness.** Upper box 3.5 m from top of deck to soffit, as above. Lower deck 0.40 m (Structurae). Slab and wall thicknesses inside the box are not given.

## Todo

The Muttart stop (53.53621, -113.48000) sits at the bottom of the south ramp. Consider building that station with this bridge rather than leaving it for the later station pass. The same note is on the R14 box in `PRIORITY.md`.

## Still missing

- Surveyed pylon height. The requirement is 24 m to 30 m from the top of deck, and the contractor says 30 m pylons.
- LRT deck elevation, and pedestrian deck elevation, in any datum.
- The name of the vertical datum for EL 615.9 and for 615.60 m.
- As-built clearance over the river.
- As-built clearance over 98 Avenue.
- As-built length, span lengths, and pier count of the south guideway, including whether the girder gets shallower over 98 Avenue.
- As-built gap between the girder soffit and the pedestrian deck.
- As-built north approach length, gradient, and elevation change. The mapped gap from the bridge tag to the tunnel tag is 43 m and is not a grade.
- As-built south ramp length, gradient, and elevation change, and the surveyed point where the ramp meets grade.
- Crossfall.
- Rail spacing as a design dimension.
- Thickness of the box slabs and webs.
- Hanger spacing and hanger length.
