# R9 Dudley B. Menzies Bridge — modeling brief

Edmonton. Capital Line (Metro Line shares this track), two tracks, concrete segmental box girder, pedestrian walkway hung underneath. Centre used by the project: 53.531, -113.512. That centre is the one in `bridge-geometry.json`.

The High Level Bridge (R10) is the steel truss beside it, to the east. This file is only the Menzies deck. Do not put the High Level truss, its road, or its streetcar on this structure.

The project list says the bridge opened in 1989. That year is Government Centre station, which opened in September 1989. The bridge opened with the University extension.

Numbers below are cited. Where two sources disagree, both are given. A blank in the "Still missing" list has no published figure in the sources checked. Nothing here was filled in by subtracting one citation from another.

## Confirmed from the extract

Retrieved 2026-10-14. Lengths are horizontal, WGS84, along the nodes. They are not structural lengths.

The project's "about 685 m per track" is the two bridge-tagged Capital Line ways:

- Way 700467672, the eastern track, closer to the High Level: 685.1 m, from 53.527348, -113.515518 to 53.532641, -113.510717.
- Way 37834327, the western track: 682.3 m, from 53.532662, -113.510829 to 53.527387, -113.515571.

`lrt-tracks.json` has the same two pieces, 685 m and 682 m, kind `bridge`.

The stated downtown portal, 53.5327, -113.5108, is the 4-decimal rounding of those north ends. The western track starts 4.6 m from it. The eastern track ends 8.6 m from it. The stated University tunnel point, 53.5273, -113.5156, is the same kind of rounding of the south ends: 9.9 m and 7.6 m off. Straight-line distance between the two stated points is 679.9 m.

The tunnel tags start a few metres beyond the bridge tags. North mouths: 53.532803, -113.510756 and 53.53278, -113.51064. South mouths: 53.527334, -113.515686 and 53.527294, -113.515632. The surface stubs between bridge tag and tunnel tag are 16.4 m and 16.3 m on the north and 9.6 m on each south track. Bridge tag plus those stubs is 708.3 m on the west track and 711.0 m on the east track. That is still a horizontal plan length.

## Bridge

**What it is.** A dedicated LRT bridge. The top deck carries two tracks. A walkway for pedestrians and bicycles hangs beneath the main spans over the river. PCL-Maxam, the joint venture that built it, calls it the first concrete segmental box girder bridge in Western Canada. The City of Edmonton says the same thing as the first segmental post-tensioned bridge in Western Canada, and says that at the time of construction it had the longest spans of that type in North America. The City does not give the span length that the claim refers to.

OpenStreetMap tags the named outline as `bridge:structure=beam` and `bridge=viaduct`. That tag is the mapper's. The structure to model is the segmental box, not a steel beam.

**Length.** Three published lengths, and they are not the same extent.

- 530 m. PCL project sheet: "a 530 metre long, seven-span continuous concrete box girder", plus a two-span slab-and-girder structure at the north abutment and a four-span slab structure at the south abutment. The 530 m is the seven-span box. The six abutment spans are extra, and PCL does not give their lengths. Wikipedia's infobox repeats 530 m (1,740 ft) and does not mention the abutment spans. 1,740 ft is 530.35 m.
- 600 m. W. R. Hibbard, Don Heaton, and Darrel P. Gagnon, "Segmental Bridge for LRT Trains in Edmonton" (1990). The abstract says the bridge is 600 m long and is a precast concrete segmental box girder. The paper itself was not retrieved, so nothing else was taken from it. Structurae also lists total length 600 m, with no citation on the public page.

The mapped elevated run, 682.3 m and 685.1 m, is longer than both. Use 530 m only for the seven-span box. Do not stretch the box to 685 m, and do not invent the abutment lengths by subtracting 530 from 600 or from 685.

**Spans.** PCL: seven continuous box spans, of which three are the main river spans (the walkway is hung under those three). Then two slab-and-girder spans at the north abutment, and four slab spans at the south abutment. 7 + 2 + 4 = 13 spans in that description. Individual span lengths are not given, so pier spacing is not known. The City's "longest spans" claim does not include a number.

**Box.** PCL: the main girder is a hollow box, approximately 4.5 m deep by 4.5 m wide. Segments were precast 2.5 m long, joined with epoxy, and post-tensioned. Ducts were grouted. The webs and the bottom slab have holes for ventilation, drainage, and to equalize temperature. Structurae lists 216 precast segments, 11,300 t of concrete, 280 t of prestressing steel, and 521 t of reinforcing steel. 216 times 2.5 m is 540 m, which is near the 530 m box and is not a length. It is not used as one.

The top deck is wider than the box. PCL does not give the overhang.

**Piers.** No count, height, or spacing is published. A description posted by Tanweer Malik, and quoted by Dennis DeBruler, says the piers are single columns, lollipop-shaped, with openings the pedestrian deck passes through, and that the walkway also hangs from the soffit of the box. That is a description of the form, not a measured height. The photographs show a single round column and a wide cap, with the blue walkway hung below the box. They were not scaled.

**Clearance above the river.** Missing. No deck elevation above the river, and no navigation clearance, was found.

**Tracks.** Two. PCL: two sets of LRT trackage, direct fixation, so there is no ballast. Wikipedia's construction table, citing Colin Hatcher, *Edmonton's Light Rail Transit – The First 25 Years* (Edmonton Transit Service, 2003), says the University extension opened on 23 August 1992 as single track from the south portal, and the second track from the south portal opened on 14 May 1994. The book was not opened. Larry McLachlan's 1995 paper says the same thing in other words: the single track leaving the southern end of the bridge is why University station is so deep. Both tracks are in the current map.

**Catenary.** It is part of the silhouette. PCL: catenary poles and anchors are on the top deck and supply traction power. The night deck photograph shows those poles on the centreline between the two tracks, with the contact wire over each track. Pole height and contact-wire height are not published. The Edmonton LRT system is overhead line at 600 V DC. That voltage is not a height.

**When it opened.** University station, and this extension, opened in August 1992. The Wikipedia table gives 23 August 1992. McLachlan says August 1992. Government Centre (then Grandin) opened in September 1989, before the river crossing. The project's 1989 date is that station, not this bridge.

Cost is a separate disagreement and is not a dimension. Wikipedia cites Lawrence Herzog, "The LRT at 25", *Edmonton Real Estate Weekly* (18 December 2003), for a bridge cost of $13.3 million. That article was not retrieved. The same Wikipedia table gives the University extension, tunnels and station included, as C$79.1 million. Those are not two measurements of the same contract.

## Approaches

The LRT does not climb an earth fill onto this bridge. It leaves a tunnel on the north bank and enters a tunnel on the south bank. The elevated structure between those portals is the bridge, including the abutment spans whose lengths are missing.

McLachlan's 1995 figure labels the line in kilometres: Corona station km 9.9, Grandin (Government Centre) km 10.7, north portal km 11.0, south portal km 11.7, University station km 12.3. Those labels are printed to 0.1 km. North portal to south portal is 0.7 km on that figure, which is the same run as the mapped 682–711 m at that precision. Grandin to University is 1.6 km, which matches the Wikipedia table's 1.6 km University extension. Corona at 9.9 km matches the City's 1983 line length of 9.9 km, when Corona opened, and Grandin at 10.7 km matches that plus the 0.8 km Government Centre extension.

**North (downtown portal).** The portal is the north bank portal, below downtown, not a hole in the downtown street. Government Centre is underground, about 0.3 km of chainage north of the portal on the 1995 labels. The mapped bridge ends at 53.532662, -113.510829 and 53.532641, -113.510717. The tunnel tag starts at 53.532803, -113.510756 and 53.53278, -113.51064. The pieces in between are ways 463555599 (16.4 m) and 82699379 (16.3 m). They are tagged as surface, not as bridge and not as tunnel.

PCL's north abutment structure is two spans of slab and girder. Length, gradient, and elevation change are not given. The north-portal photograph shows the deck still elevated where it meets a concrete headwall in the slope. The tracks and the catenary run into openings in that headwall. A count of bores is not published. Where the deck would meet natural grade does not apply: the line enters the hill.

**South (University tunnel).** The mapped bridge ends at 53.527387, -113.515571 and 53.527348, -113.515518. The tunnel tag starts at 53.527334, -113.515686 and 53.527294, -113.515632. The pieces in between are ways 700467673 and 424284934, 9.6 m each.

PCL's south abutment structure is four slab spans. Length, gradient, and elevation change are not given. McLachlan: the south portal and the university tunnel were sequential excavation, and University station was cut and cover. The platform is 23 m below road level. The City says 23 m below the surface, and says the builders had to match grade with this bridge. The 23 m is the station depth, not the rise of the bridge and not the elevation of the portal. On the 1995 labels the station is 0.6 km south of the south portal. No open photograph of the tunnel mouth was found.

**Walkway approaches.** Separate from the tracks. PCL: two spiral ramps connect the pedway to the river-valley trails. Their length, radius, and gradient are not given. The winter elevation shows a curved ramp at the near end of the walkway. The extract has short cycleway stubs at each end of the mapped walkway (ways 23266026, 51.9 m, and 23266022, 28.2 m). They are not tagged as ramps, so they are not recorded here as the spirals.

## Deck

**Elevation.** Missing, both above sea level and above the river. No vertical datum is stated. The 23 m figure is the University station platform below the road, not this deck.

**Which deck.** Upper deck: two LRT tracks, direct fixation, blue railings along both edges in the photographs, catenary poles down the centre. Lower deck: the walkway, hung below the box for the three main river spans only. It does not run the whole 685 m. The photographs show it as a concrete path with a yellow centre line, blue railings, and blue frames hanging from the soffit. High Level's lower deck is its road. This walkway is not that road.

**Thickness.** Missing as a slab thickness. The 4.5 m figure is the depth of the box, top slab through bottom slab, and PCL says approximately.

**Width.** Top deck approximately 10 m (PCL). Wikipedia repeats 10 m (33 ft). The mapped outline, way 533052900, measures about 9.0 m wide through the middle of the run and about 9.5 to 10.5 m near the ends. That is a plan width of the OpenStreetMap polygon, not a second survey. The box is approximately 4.5 m wide, so the deck overhangs the box. The overhang is not given.

The lower walkway width is missing.

**Track spacing.** Not published. On the mapped centrelines the two tracks are about 4.6 to 5.4 m apart over most of the run, about 6.8 m near the north end, and the full range of node-to-node distances is 4.3 to 7.8 m. Gauge of the Edmonton LRT is 1,435 mm. That is the system gauge, not a measurement across this deck.

**Crossfall.** Missing. No superelevation is published for this bridge.

**Horizontal gap to the High Level.** Not surveyed. From the outlines in this extract, the closest the two mapped footprints come is 49.4 m, at the north end of the Menzies outline, 53.532635, -113.510686. Along the eastern track, way 700467672, the horizontal distance to the High Level outline is 165.6 m at the university end, 57.9 to 67.9 m through the middle of the run, and 51.4 m at the downtown end. They are a pair across the river, and they are not touching. Menzies is the western, lower bridge. Leaving either one out still leaves a hole, because the gap is small on the scale of the valley and the decks are one above the other in every elevation.

## Still missing

- Length of each span, and the lengths of the two north abutment spans and the four south abutment spans.
- A single length that covers the same endpoints as the mapped 682–685 m. The published 530 m and 600 m are shorter, and the sources do not say how they were measured.
- Pier count, pier height, and pier spacing.
- Clearance above the river, and the deck elevation above the river and above sea level, with the datum.
- Deck slab thickness, as distinct from the 4.5 m box depth.
- Overhang of the 10 m deck past the 4.5 m box.
- Catenary pole height and contact-wire height.
- Published track spacing. The 4.3 to 7.8 m range is the mapped centrelines only.
- Walkway width, and the vertical distance from the walkway to the box soffit.
- Crossfall.
- Gradient and elevation change on the north portal side and on the south portal side.
- The University tunnel mouth. No open photograph of it was found. The station depth of 23 m is not that elevation.
- Spiral-ramp length, radius, and gradient.
