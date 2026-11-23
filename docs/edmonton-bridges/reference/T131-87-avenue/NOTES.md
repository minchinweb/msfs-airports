# T131 87 Avenue elevated guideway — modeling brief

Edmonton. The Valley Line West LRT elevated guideway on 87 Avenue, with two elevated stations: West Edmonton Mall (P163) and Misericordia (P164). Guideway centre used by the project: 53.5205, -113.618.

Under construction. The newest dated source opened is the Marigold release of 8 October 2025. Segment erection was complete by the end of 2025 (Parsons). Phase 2 to Lewis Farms is expected in 2028 (Wikipedia). A summer 2026 City update exists, but it was not opened (see SOURCES.md). Model the finished guideway. Do not model a half-built stage.

Trains run east and west along 87 Avenue, from Lewis Farms in the west to 102 Avenue in the east. The guideway carries both tracks. The mapped ways are two, one for each direction. They are the same alignment. The guideway runs over 87 Avenue, the centre of the road.

This is not the Valley Line Southeast (T127, Davies). It is not the Anthony Henday LRT span (T132), which is on the same road at the Henday. It is not the 87 Avenue road bridge over the Henday. Do not copy the Valley Line Southeast span or pier notes here. The Valley Line West is a different contract and a different structure.

The mall is the VFR checkpoint Shopping Mall (VCSHP). PRIORITY.md says the guideway lies about 1.4 km off the runway 04 long final at 8 km. That approach figure was not checked in this pass.

## Guideway

**Type.** Precast segmental box girder with constant depth (Parsons, opened). The contract was built primarily in simple spans (Parsons). Two tracks, dual track (Marigold, Parsons).

**Spans.** Span count is not published in any source opened. Span lengths are not published. Parsons says simple spans. The project inventory (lrt.md) does not give a span count either.

**Segments.** Each pair of piers has six to 15 segments between them (Marigold, 8 October 2025). The segments are 60 tonnes each (Marigold; Global News). Global News reports 224 precast segments installed in just under 180 days. That count is for the season, not a span count.

**Length.** The published lengths differ. Marigold and Parsons give about 2 km, between 182 Street and 163 Street (Marigold, 8 October 2025; Global News, the same day). A City page reached by search gives 2.3 km between the same streets. That page did not open, so it is not used. The project inventory (lrt.md) gives the guideway as the stretch between 178 Street and 165 Street. Both sets of limits are kept. They were not averaged.

The OpenStreetMap construction ways give a plan length of 1,736.6 m for track A and 1,734.2 m for track B, between the 178 Street and 165 Street points. Those are horizontal plan lengths along the mapped nodes. They are not structural lengths. The two tracks are separate ways, so 1.74 km is one track, not the pair. The 2 km figure and the 1.74 km plan figure are both kept. The gap may be the approaches beyond the named streets. No source says so.

**Girder depth.** Not published.

**Piers.** 46 Y-shaped piers hold up the guideway (Marigold, 8 October 2025). The 46 count matches the project inventory. Pier shape is Y (Marigold). Pier height is not published in any source opened. A search summary gave 6.0 m to 12.7 m, from an ELLISDON page that no longer loads. It is not used.

The inventory lists preliminary pier numbers: piers 02 to 16 near 176 to 180 Street, pier 24 west of 172 Street, and piers 38 to 40 near 165 Street. These are preliminary contract numbers. They are not checked.

**Clearance under 87 Avenue.** The project inventory gives a minimum of 5.5 m over 165, 169, 170, 175 and 178 Street, and over the mall and hospital driveways. It gives 3.0 m over pedestrian crossings. These are inventory figures, not published design figures, and the inventory has no date. No published source opened gives a clearance.

**Road and rail beneath.** 87 Avenue runs under the guideway. The road carries two lanes each way. The City reduces it to one lane each way between 161 Street and Anthony Henday Drive until the end of 2026 (search summary only; the City page did not open).

**Station structure on the deck.** Both stations are elevated, on the guideway (Marigold; Wikipedia; inventory). See the Stations section.

## Stations

**West Edmonton Mall (P163).** Elevated, side platform (lrt.md; Wikipedia gives "Elevated" in its stop table). Centre 53.5206, -113.624. The inventory says it sits at the mall transit centre.

- Platform length, width and height above the guideway: not published in any source opened.
- Canopy: not published.
- On the guideway: yes. It is an elevated station on the T131 structure.

**Misericordia (P164).** Elevated, side platform (lrt.md; Wikipedia). Centre 53.5197, -113.613. The inventory says it sits at the hospital.

- Platform length, width and height: not published in any source opened.
- Canopy: not published.
- On the guideway: yes.

The two stations have no footprint in the OpenStreetMap extract. The extract has no station polygons for either.

## Approaches

**178 Street (west).** The mapped guideway starts at 178 Street, at 53.5213, -113.6310 (lrt.md; the OSM node on route 13 is 53.521301, -113.631003). The City and Marigold give 182 Street as the west end. Gradient at the west approach: not published. Elevation change: not published. Point where the guideway meets grade: not published. The inventory says the approach fill above 1 m is on piles. That is not a published figure.

**165 Street (east).** The mapped guideway ends at 165 Street, at 53.5195, -113.605 (lrt.md; the OSM node is 53.51951, -113.605091). The City and Marigold give 163 Street. Gradient at the east approach: not published. Elevation change: not published. Point where the guideway meets grade: not published.

The OpenStreetMap ways end at the same points as the inventory, not at grade. A plan line is not a climb to grade. Do not read a gradient from the plan lines.

## Deck

**Elevation above sea level.** Not published. No vertical datum is published. The OpenStreetMap ways have no elevation.

**Elevation above the road beneath.** Not published.

**Deck thickness.** Not published.

**Track centres.** Not published.

**Noise or safety screens.** Not published in any source opened.

## Neighbours

**T132, Anthony Henday LRT span (53.5224, -113.6584).** The sources support a centre and an inventory row (lrt.md): one median pier in line with the road bridge pier, at least 10 m clear of the existing bridge, design clearance 5.7 m, and a 6.0 m option if the deck is a slab. The OpenStreetMap route 13 passes through that area, but the ways are construction ways with no bridge tag. Only the inventory row supports T132's pier and clearance. The sources support adding T132 as its own code with its own nodes. They do not support copying T131's figures to it. It is not in geometry.json, because this folder covers T131 only.

**H37, Henday / 87 Avenue (53.5228, -113.6592).** No inventory row in lrt.md, freeway-bridges.md or bridges.md was found. PRIORITY.md places it in the T131 box and says it is a partial cloverleaf. No source checked gives H37 geometry, deck elevation or ramp data. The sources do not support including H37 yet. It needs a road-side source first.

## Still missing

- Span count and span lengths. Check Schedule 5 Part 4 (the City's project agreement), which has a section on this guideway.
- Girder depth.
- Pier height and pier cross-section. The 6.0 to 12.7 m range is a search summary only.
- Clearance over 87 Avenue as published, and deck elevation above sea level and the datum.
- Platform length, width and height above the guideway, for both stations. Canopy for both stations. Check the City station pages (transforming.edmonton.ca, elevated stations), the WEM fact sheet and the booklet. All returned 502 when opened.
- Gradient and elevation change for each approach. Where each end meets grade.
- Track centres, deck thickness, noise or safety screens.
- Which length is right, 2 km or 2.3 km, and whether the guideway runs from 182 Street or 178 Street. Read the City page once it is back.
- Blackfalds as the casting yard for the segments. It is in lrt.md but no source opened or searched gives it.
- Alberta Transportation Structure-Export.csv for any structure over 87 Avenue on the alignment. No copy was found.
- Open-licence photographs of the piers, the guideway, both stations and the approaches. None found. See SOURCES.md.
