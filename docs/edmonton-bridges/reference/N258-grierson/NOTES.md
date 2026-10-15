# N258 Grierson Hill Bridge — modeling brief

Edmonton. A short road span at the bottom of Grierson Hill, on the north bank, immediately west of the Low Level north abutment. Centre used here: 53.538564, -113.488789, the midpoint of OpenStreetMap way 106711211. The road on the deck is Grierson Hill Road NW. Two lanes, two-way, asphalt, tagged 50 km/h.

This is not one of the two Low Level river decks. The 1900 northbound deck is way 31882107. The 1948/1949 southbound deck is way 22916473. Those are the through trusses across the North Saskatchewan River. This span does not cross the river. The code is N258. It is not an R code.

It is its own bridge, and it belongs in the Low Level scene. It carries Grierson Hill Road over McDougall Hill Road. The Edmonton Sun, 12 June 2012, says the McDougall Hill road is beneath the bridge, and that work was still going on underneath on the pillars. CBC, 10 February 2012, lists pier-column repairs on this closure. The mapped centreline crosses McDougall Hill Road. It is not a culvert. The deck is short. The mapped line is 59.0 m on the nodes stored in the project extract, and 59.1 m on the live coordinates of the same two nodes. At 3,500 ft AGL that deck does not read as a river bridge. At 1,000 ft the grade separation does read, because the two roads are not at one level. A north-end model that joins them at one grade is the wrong interchange. No height was read from a photograph, and none was made by subtracting one citation from another.

Numbers below are cited. Where two sources disagree, both are given. A blank in the "Still missing" list has no published figure in the sources checked. Nothing here was filled in by adding one citation to another. OpenStreetMap `maxheight` tags are mapper tags. They are not deck elevations. This way has no `maxheight` tag and no `width` tag.

## Name

The City's 2012 project title, as Mack Male quoted it on 16 June 2012, is Grierson Hill Bridge & MacDonald Drive Pedestrian Underpass Rehabilitation. CBC's article body says Grierson Hill Bridge. The City's 2012 outline-agreements file names the Alberco contract GRIERSON/MCDOUGALL OVERPASS AND MCDONALD. Alberco's own project list says Grierson Bridge Rehabilitation. The Edmonton Sun says the Grierson bridge. CBC's headline says Grierson Bridge.

Grierson Hill Bridge and Grierson/McDougall Overpass are both published names for this span. "Grierson Bridge" is not only an OpenStreetMap tag. The tag `bridge:name=Grierson Bridge` was added to way 106711211 on 13 June 2017. The way had been tagged `bridge=yes` since 1 April 2011, without that name. The tag is kept as the mapper's name. It is the same words the Sun and the CBC headline used in 2012.

The MacDonald Drive pedestrian underpass is the other structure in that 2012 project title. It is not this span. No geometry for it was in the Low Level extract. It is not in this file.

Alberco also lists Rossdale Rd - McDougall Overpass Rehabilitation as its own project. That is the Rossdale Road Bridge over McDougall Hill Road, way 37120045. The brief is in `../N259-rossdale-mcdougall/`. It is not this span.

## Bridge

**What it crosses.** McDougall Hill Road. The Sun says that road is beneath the bridge. CBC's closure notice is for McDougall Hill north of the Low Level Bridge, for pier-column repairs, a new deck, paving, and a new guardrail. Way 106711211 crosses way 1433098757 and way 303665641 in plan. Those two ways are McDougall Hill Road NW. The deck is `layer=1`. The McDougall ways have no layer. It does not cross the river, a rail line, or a creek in the sources checked.

**Year.** A year for the overpass was not found. Grierson Hill Road was constructed between 1950 and 1963. The roadway embankment was completed in 1961 and the road was paved in 1963 (Wang, Tweedie, and Lach, 2018). Those years are the road. They were not used as the year of this deck.

The deck that is there was rebuilt in 2012. CBC, 10 February 2012, said the Grierson Hill Bridge would close from 18 February until the fall. The work listed is bridge-deck demolition and new bridge-deck construction, pier-column repairs, paving, and new guardrail construction. The expected cost was $4.5 million. The Sun, 12 June 2012, says the bridge was open nearly three months early, and that it had been supposed to stay closed until September. The same article says work was still going on underneath on the pillars. On 25 February 2012 the OpenStreetMap way was tagged `construction=tertiary`. On 3 July 2012 that tag was gone and the way was `highway=tertiary` again. Those are mapper tags. They sit inside the published closure.

**Spans.** Not published. CBC says pier columns. The Sun says pillars. Neither gives a count. An abutment form is not published.

**Length.** No published structure length was found. The project extract stores way 106711211 as two nodes, 53.538771, -113.48851 and 53.538357, -113.489068. The horizontal length of that stored line is 59.0 m. The same two nodes, read from OpenStreetMap on 14 October 2026, are 53.5387714, -113.4885102 and 53.5383572, -113.4890679. That line is 59.1 m. The 59.0 m and the 59.1 m are the same way at two coordinate precisions. They were not averaged. Neither is a published structure length. Use the stored nodes for the plan shape.

**Type.** Not published beyond the 2012 words: a bridge deck that was demolished and replaced, then paved, with a new guardrail, on pier columns. No source found says girder, slab, or beam for this span. Way 106711211 has no `bridge:structure` tag. The `beam` tag on way 1271848915 belongs to the hillside footbridge, which is a different span.

**Piers.** Pier columns, and pillars under the deck, in the 2012 accounts. A count is not published. A column size is not published. A height is not published.

**Clearance under the deck.** Not published. Way 1433098757, McDougall Hill Road onto the southbound Low Level deck, is tagged `maxheight=5.2`. Way 303665641, McDougall Hill Road off the northbound deck, is tagged `maxheight=5.0`. The R13 notes already record that no published source states 5.2 m or 5.0 m. Those tags are on the road that passes under this span. They are not a clearance under this deck, and they are not a deck elevation. This span's own way has no `maxheight` tag.

**Elevation.** Not published for the deck, the soffit, or the road underneath. The vertical datum is missing. The 2018 paper gives a shear-plane elevation and a slope height for the Grierson Hill landslide. Those figures are the landslide. They are not this deck, and they are not used here.

## The other span on the hill

Way 1271848915 is not this bridge. The R13 notes dropped it as an unnamed path bridge on the north hillside. The outline has no name. It is tagged `bridge:structure=beam` and `man_made=bridge`. Its centroid is 120.0 m from the midpoint of way 106711211. The nearest outline node is 88.5 m from this deck's nodes.

The outline crosses Grierson Hill Road on the hill, way 106711201. It does not cross way 106711211. The cycleway on that outline, way 533867748, is 91.1 m and is tagged `bridge=yes`. The outline perimeter is 191.0 m. Those lengths are that footbridge. They are not this deck.

A steel bridge that carries visitors over Grierson Hill Road was installed overnight on 17 October 2016, as part of the 100 Street funicular and the Frederick G. Todd Lookout (SkyriseCities, citing the construction). The funicular opened on 9 December 2017 (Global News). The 15 December 2017 photograph shows that footbridge: a wood deck, a kink, and a concrete pier, over a road with streetlights. The Low Level truss is in the same frame, to the right, and it is a different structure. The $24 million figure in that article is the funicular project. It is not the $4.5 million deck replacement of 2012.

The photograph and the mapped outline are the same hillside crossing: a footbridge over the hill road, uphill from this deck. It is part of the 100 Street funicular. The brief is in `../F256-funicular/`. Its geometry is not in this file.

A 1976 design drawing, Grierson Hill Bicycle and Pedestrian Bridge, drawing D2, T. Lamb, McManus & Associates, for Alberta Environment, is in the bibliography of the Valley Line environmental assessment. The pages checked do not say where it was, or that it was built. It was not assigned to either span.

## Approaches

Both approaches are Grierson Hill Road. No source gives the present gradient, the elevation change, or the point where either end meets natural grade. The OpenStreetMap ways below that come from the project extract match the live node counts on 14 October 2026. A complete way is still only the mapped polyline. Its far node is not a surveyed grade point.

**Northeast, up the hill.** Way 106711201 is Grierson Hill Road NW onto the deck. Two lanes, two-way, asphalt, 50 km/h, 158.4 m. Node order in the extract is from the upper junction down to the bridge. The far node, 53.539882, -113.487015, is a junction. It is not the top of the bank.

Three other ways meet that node. Way 106711221 is the one-lane ramp up from the Low Level north end. It is already in the R13 geometry. It is not this deck. Way 106711206 is also named Grierson Hill Road NW. It is one lane, two-way, 253.4 m, and it runs from this same junction to McDougall Hill Road at 53.538583, -113.490097. It does not use way 106711211. It is not this span. Way 697598868 is the road continuing uphill. The name on that way is Grierson Hill NW, not Grierson Hill Road NW. It is three lanes, 70.4 m, from 53.5403724, -113.4863442 down to the junction. It is not in the project extract. It was read from the OpenStreetMap API on 14 October 2026.

The same name continues. Way 451264639 is Grierson Hill NW, three lanes, 59.0 m. Way 1281336532 is Grierson Hill NW, two lanes, 47.1 m. Way 451264638 continues past that. Those lengths were read the same day. They were not copied into `geometry.json`. None of them is a surveyed grade point.

**Southwest, toward Rossdale.** Way 106711229 leaves the deck. Grierson Hill Road NW, two lanes, two-way, asphalt, 50 km/h, tagged `sidewalk=no` and `foot=no`, 29.4 m. The bridge way itself has no sidewalk tag. The sidewalk tag on this approach was not treated as a sidewalk on the deck.

The far node, 53.538154, -113.489353, is a split. Way 106711225, the cloverleaf from this node to McDougall Hill, is already in the R13 geometry. It is not this deck. Way 151895211 continues Grierson Hill Road NW. One lane, one-way, asphalt, 50 km/h, 203.8 m. Node order is from 53.537415, -113.492093 to this split, so the one-way is toward the bridge. That far node is shared with Rossdale Road NW, ways 113653301 and 302605387. It is an intersection in the valley. It is not a published point of natural grade.

## Deck

**Elevation.** Missing above sea level. The vertical datum is missing.

**Thickness.** Not published. The 2012 work demolished the bridge deck and built a new one, then paved it. No depth is given.

**Width.** Not published. Way 106711211 has no `width` tag. Lane width is missing.

**Lanes.** Two, both directions, asphalt, tagged 50 km/h. `oneway=no`. The live way on 14 October 2026 also has `hgv=designated` and `source=City of Edmonton`. Those two tags are not in the project extract. The `source` tag is a mapper tag. It is not a City drawing of the span.

**Guardrail.** CBC says new guardrail construction in 2012. The form of the rail is not described.

**Crossfall and grade.** Not published on the span.

## What reads from the air

No openly licensed aerial of this deck was found. The City's 2025 orthophoto repository has a tile that covers the coordinate. It was not extracted into `photos\`.

The 15 December 2017 photograph, from the funicular, is the open view that separates the structures. The Low Level truss is on the right. A footbridge with a wood deck crosses the hill road in the foreground. That footbridge is the 2016 span, not this one. The road under it is the hill road, with streetlights. A roadway curves up to the near end of the truss. This deck's soffit, and McDougall Hill Road under it, are not isolated in that frame. No height was read from it.

The August 2009 photograph from the McDougall Hill lookout shows a concrete overpass on columns, beyond the truss, with the Muttart pyramids and the south-bank hills behind it. That overpass is on the south bank. It is not this span. It was not saved.

From the ground accounts, the object is a replaced deck on pier columns, with McDougall Hill Road underneath, at the north end of the truss approaches. Model it with the Low Level scene as that grade separation. Do not model it as a third river truss, and do not model the hillside footbridge as this deck.

## Still missing

- A year for this overpass. The 1950–1963, 1961, and 1963 figures are Grierson Hill Road. They are not a year for the deck.
- Span count. CBC says pier columns. The Sun says pillars. Neither gives a number.
- A published structure length. The mapped centreline is 59.0 m on the stored nodes and 59.1 m on the live coordinates of those nodes.
- Deck type beyond the 2012 words: deck demolished and replaced, paving, new guardrail, pier columns. No girder, slab, or beam is published for this span. The `beam` tag is the hillside footbridge.
- Pier count, column size, and pier height. Abutment form.
- Clearance under the deck. The OpenStreetMap tags `maxheight=5.2` and `5.0` are on McDougall Hill Road. They are not that clearance, and they are not a deck elevation. No published source found states either tag.
- Deck elevation above sea level, soffit elevation, and the vertical datum.
- Width, and lane width. Way 106711211 has no `width` tag.
- Whether the deck has a sidewalk. Way 106711229 is tagged `sidewalk=no`. The bridge way has no sidewalk tag.
- Crossfall and longitudinal grade on the span.
- Gradient, elevation change, and the point where Grierson Hill Road meets natural grade, at either end. The northeast mapped end of the ways copied here is a junction, and Grierson Hill NW continues past it. The southwest mapped end is the intersection with Rossdale Road NW.
- The MacDonald Drive pedestrian underpass, named in the same 2012 project title. No geometry and no dimensions were found for it here.
- Where the 1976 Grierson Hill Bicycle and Pedestrian Bridge drawing was, and whether that drawing was built.
- An openly licensed photograph that shows this deck and McDougall Hill Road underneath it, separate from the Low Level truss and from the 2016 footbridge. An openly licensed aerial.
