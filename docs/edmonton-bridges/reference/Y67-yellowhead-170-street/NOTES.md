# Y67 Yellowhead / 170 Street: modeling brief

Edmonton. Yellowhead Trail (Alberta Highway 16) passes under 170 Street NW at the Yellowhead interchange in west Edmonton. The interchange is a diamond (Wikipedia, citing Google Maps, retrieved 25 October 2017). The project centre is 53.573, -113.615 (latitude, longitude). The OpenStreetMap object centre is 53.5733, -113.6153, and that is the point plotted on the map. The surveyed point on the helicopter route is the same crossing.

This is not Y66, Yellowhead / 178 Street, at 53.572, -113.631. It is not Y68, Yellowhead / 156 Street, at 53.578, -113.596, which is estimated. The 170 Street bridges over the CN rail yard, 260 m north of this centre, are a different structure. Do not reuse the notes for those.

## Bridge

**Which road is on top.** 170 Street is on top. Yellowhead Trail is underneath. Two sources say so directly. The Alberta record STRU_ID 41091 (file 79483, "170 STREET - YHT (B185)") is a structure on a local road that passes over Highway 16 at R1 km 2.415 and L1 km 2.406. The file does not say what R1 and L1 mean beyond the lane labels. OpenStreetMap has 170 Street bridge ways at layer 1 over the Yellowhead motorway. Two one-way carriageways carry 170 Street over the highway. The west carriageway runs southbound and the east carriageway runs northbound (OpenStreetMap one-way tags and node order). The Alberta description reads "HIGHWAY 2 OVER YELLOWHEAD TRAIL AT 170 STREET". The same record says the carried road is a local road, owned by the City of Edmonton. The word "Highway 2" conflicts with that. Nothing in the sources resolves it. The structure's name and location both say 170 Street.

**Type.** Concrete, two spans. Alberta's span-type code is FM. The file gives no label for FM, so this brief does not name the type. Pier caps are concrete (PCONC). Deck is precast concrete. Wearing surface is concrete, high density. No girder or truss depth is published.

**Spans.** Two spans, 31.0 m and 35.6 m (Alberta record 41091). The nominal length is 66.6 m. The maximum span is 35.6 m. The Alberta file gives no pier count and no abutment type.

**Length.** Nominal 66.6 m (Alberta record 41091). The OpenStreetMap deck ways are 68.6 m (west carriageway, way 22916254) and 68.8 m (east carriageway, way 153737331). Those are plan lengths along the mapped nodes, not structural lengths. The 2.0 m difference from the nominal length is not explained by any source. Use 66.6 m for the structure.

**Pier count and type.** Not published. The Alberta pier cap is concrete. The pier shaft material field is blank. The abutment fields are blank. Two spans would normally have one support between the abutments. The file does not say that.

**Clearance.** Theoretical vertical clearance under the structure is 5.8 m (Alberta record 41091). Theoretical horizontal clearance under the structure is 5.8 m. The file does not label the units. The neighbouring notes read these figures as metres. Measured clearance is blank. Treat 5.8 m as a theoretical figure from the inventory. It is not a survey.

**Sidewalks.** The Alberta record has no sidewalk widths. OpenStreetMap has one footway tagged bridge=yes on the Yellowhead deck, on the east side, concrete surface. Plan length 66.9 m (way 1543946733). It is not tagged with a width.

**Widening or rehabilitation.** The Alberta record shows no rehabilitation. Its inspection date is 10 July 2025. Sufficiency is 34.5 and condition is 38.9 (Alberta record 41091). The estimated replacement year is 2033. The estimated replacement cost is $14.1 million (Alberta record 41091). Two 2017 news items describe deck work on 170 Street near Yellowhead. The Global News item (22 June 2017) says the overpass at Yellowhead Trail was closed for a concrete deck pour. The CTV item (17 April 2017) says rehabilitation was starting on "170 St bridge north of Yellowhead". The CTV headline does not name the bridge that was rehabilitated. Neither item gives a dimension. The PCL page describes the northbound 170 Street bridge over CN's Bissel Yard, 160 m long, built 1983. That is the rail bridge. Its deck figures (150 mm structural deck, 50 mm topping pours) do not describe this crossing.

## Approaches

No source publishes a gradient, an elevation change, or the point where either road meets grade. The OpenStreetMap approach ways below are plan geometry only.

**South, the Yellowhead underpass.** Two short one-way links leave the south end of the deck, one per carriageway. The west link, way 472597643, is 27.2 m long, southbound, three lanes. The east link, way 472597648, is 27.7 m long, northbound, four lanes. Further south, 170 Street continues as ways 472597645 (70.5 m) and 472597646 (97.3 m). The extract calls those two cross roads. They are the same road. Ramps join the interchange in several places (eight motorway links are listed in `geometry.json`).

**North, toward the rail bridge.** Two one-way links leave the north end of the deck, one per carriageway. The west link, way 127496991, is 29.5 m long, southbound. The east link, way 502009507, is 29.7 m long, northbound. Beyond that the road continues to the CN rail overpass. The rail overpass is a separate structure. Ways 241143868 and 472597650 are short links between the two structures. Those are not part of Y67.

## Deck

**Elevation.** Missing above sea level, and the vertical datum is missing. No deck elevation is published for this crossing. The Environment Canada gauge 05DF001 is at the Low Level Bridge and uses a local assumed datum. Nothing here converts it.

**Thickness.** Not published. No deck or slab thickness is in the Alberta record.

**Elevation above the road.** Theoretical vertical clearance is 5.8 m (Alberta record 41091). That is the only published figure. Deck height above the road is blank in the record.

**Width.** Gross deck width is 37.8 m. Total clear roadway is 33.0 m (Alberta record 41091). Those are the inventory figures for the whole structure. OpenStreetMap carriageway width tags are 14.6 m on both deck ways. Those are mapper tags, not published widths. The two carriageways are about 16 m apart on the plan.

**Lanes.** OpenStreetMap lanes tags: three lanes on the southbound carriageway (way 22916254) and four on the northbound (way 153737331). That is seven lanes in all. The Alberta record gives no lane count or lane width.

**Sidewalk or path.** One bridge-tagged footway on the east side (way 1543946733). The Alberta record gives no sidewalk widths.

**Crossfall.** Not published.

**Longitudinal grade.** Not published.

## Still missing

- Deck elevation above sea level and the vertical datum. Soffit elevation.
- Deck height above the road beneath, as a measured figure. The 5.8 m is the only theoretical clearance.
- Units of the Alberta clearance and width fields. The file labels no units.
- Pier count, pier shaft and abutment types. Pier heights and footing sizes.
- Girder or beam depth. The meaning of span type FM.
- Deck or slab thickness.
- Sidewalk widths on each side. Lane widths. Shoulder widths.
- Crossfall as a slope. Longitudinal grade.
- Where each approach meets natural grade. The gradient and elevation change of each approach.
- The date of the 2017 deck pour and whether it was on this structure or the rail bridge. The Global News and CTV items do not settle it.
- Confirmation of the "HIGHWAY 2" wording in the Alberta description.
- An openly licensed photograph of the structure, its piers, or its approaches.
- A Structurae entry, HistoricPlaces record, or City Archives entry for this crossing. Searches found none.
