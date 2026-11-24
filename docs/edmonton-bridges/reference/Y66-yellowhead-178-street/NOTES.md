# Y66 Yellowhead / 178 Street: modeling brief

Edmonton. Yellowhead Trail (Alberta Highway 16) at 178 Street NW, on the west side of the city. Centre used by the project: 53.572, -113.631. This is a Yellowhead helicopter-route point. It is a freeway with two one-way carriageways, running east and west.

This is not Y65 (Yellowhead / 184 Street, 53.573, -113.639). It is not Y67 (Yellowhead / 170 Street, 53.573, -113.615). No figure here comes from either folder.

**The main finding: no source checked shows a 178 Street crossing of Yellowhead.** The Alberta bridge export has no structure that carries 178 Street over Yellowhead, or Yellowhead over 178 Street. The only Alberta structures on Yellowhead at this point cross the CNR railway. Their name is "180 ST." The OpenStreetMap bridge ways in the Y66 object sit on those same two structures. So the Y66 deck geometry may be the CNR overpass, not a 178 Street grade separation. The 178 Street road itself is not in the Y66 object. Check the site before modeling any 178 Street deck.

All figures below are cited. Where two sources disagree, both are given. Nothing is averaged. Nothing is invented by adding or subtracting citations.

## Bridge

**Type.** Not stated in the Alberta record. The record gives three spans, a concrete pier cap and shaft, a deck code of PCONC, and a skew of -60 degrees. It does not name the superstructure type (AB, STRU_ID 40882 and 40883). No Structurae or HistoricPlaces entry was found.

**Spans.** 41.5 m, 52 m, and 41.5 m, from the Alberta record for each carriageway (AB, STRU_ID 40882 and 40883). Those are the same three spans for both. The record has the spans for the CNR overpass, not for a 178 Street crossing.

**Length.** Nominal bridge length 135 m. Theoretical bridge length 156.2 m for the eastbound structure and 156.1 m for the westbound structure (AB). The nominal and theoretical lengths are both published. They are not reconciled here. The 135 m is the length the record calls nominal. The 156 m figures are the record's theoretical length. Neither is checked against a drawing.

**Plan lengths (OSM, not structural).** The mapped bridge ways are 135.7 m, 152.9 m, and 142.1 m long (OSM, `geometry.json`). They are plan lengths between mapped nodes. They are not structural lengths.

**Pier count and type.** Three spans imply two interior supports. The record does not state a pier count. It gives a concrete pier cap and a concrete pier shaft (AB). It does not give a pier shape. The pier shape field is blank for these two records.

**Girder or arch or truss depth.** Not published.

**Clearance.** The record gives a theoretical vertical clearance under the structure of 7.2 m, and a theoretical horizontal clearance of 7.5 m (AB, both carriageways). The clearance is under the bridge, over the CNR track. The export does not label units. Y65 read the same field as metres. This brief reads it the same way. The clearance is not a clearance to the road below. No such road is recorded.

**Sidewalks.** None recorded. The export has no sidewalk width for either record.

**Widening or rehabilitation.** The record gives first in service 1981 (AB, both). Its status date is 1 January 1981. No rehabilitation is recorded in the export. No City or news source found for this structure says otherwise. The 2026 City work at 184 Street is a different structure (see Y65).

## Approaches

No source gives a gradient, an elevation change, or a point where either carriageway meets natural grade. That is unpublished for this site.

The OSM approaches are plan geometry only. They are mapped Yellowhead ways that touch the bridge ends. Their lengths are mapped way lengths. They are not climbs to grade.

**West end.** Two approach ways touch the west end of the bridge ways. One is 45.0 m long and has 4 lanes (OSM 61431875). A 3-lane way runs 723.3 m further west (OSM 60064980). Its far node is not a grade point.

**East end.** Two approach ways touch the east end. One is 37.2 m long and has 3 lanes (OSM 23226554). One is 221.4 m long and has 4 lanes (OSM 61513652).

**Ramps.** The extract has two motorway-link ways that touch the bridge ends, at 449.8 m and 49.5 m plan length (OSM 186928079 and 273839600). They are plan geometry only.

**Carriageways.** The OSM one-way node order puts the 3-lane bridge way running east and the 4-lane bridge way running west. No published source confirms the direction.

**Where each carriageway meets grade.** Not published.

## Deck

**Elevation above sea level, and datum.** Not published. Nothing in the sources gives a deck elevation for this structure.

**Elevation above the road underneath.** Not applicable. The road under the Yellowhead bridge at this point is the CNR railway. The record gives 7.2 m vertical clearance under the structure (AB). The Alberta "DECK_HEIGHT" field reads 10.4 m for both records (AB). The export does not label its units or datum. It is not converted here. It is not a geodetic deck elevation.

**Thickness.** Not published. The record gives no deck depth.

**Width of each carriageway.** The Alberta record gives a gross deck width of 14.5 m and a total clear roadway of 13 m for each of the two structures (AB, 40882 and 40883). The OSM tags give 11.1 m for the three-lane way and 14.6 m for the four-lane way (OSM). The OSM widths are mapper tags. They are not published structural widths. They disagree with the Alberta record. Both are given.

**Width of the whole crossing.** Two carriageways, each 14.5 m gross (AB). Total width across both carriageways is not in the record.

**Lanes.** OSM tags are 3 lanes for one carriageway and 4 lanes for the other. The Alberta record does not give lanes. OSM is the only lane source. It is not confirmed.

**Sidewalk or path.** None recorded (AB).

**Crossfall and longitudinal grade.** Not published.

## Still missing

- Whether 178 Street crosses Yellowhead here, and whether it is over or under. No source found shows it. The Alberta export has no record for this.
- The 178 Street deck, if there is one. The OSM object for Y66 has no 178 Street way.
- Deck elevation above sea level, datum, and grade line.
- Superstructure type, pier count, and pier shape.
- Carriageway and total widths from a published source. The OSM widths disagree with the Alberta gross width.
- Approach gradients and where each road meets grade.
- Any photograph of the structure with an open licence.
