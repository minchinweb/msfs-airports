# B262 Holyrood Gardens Tower — modeling brief

Edmonton. A residential tower in the Holyrood Gardens redevelopment, on the east side of 85 Street NW, at the junction with Connors Road. Connors Road becomes 90 Avenue at that junction, so both names mean the same corner. The tower is beside the Holyrood LRT stop. It is a building, not a bridge. It has no Look or Where score.

The City's permit records name it building 1, at 9009 85 Street NW. That is the address the permits give. Its geocode is 53.52652, -113.45658. The earlier PRIORITY.md centre, 53.528012, -113.456611, was the centroid of the OSM Holyrood Gardens landuse polygon, not the tower. The entry is updated to the permit point.

It is not the Holyrood LRT stop (P154). It is not the ambulance station (B263), Sir William Place (B275), the house at 9538 85 Street (B266), or St. Luke's Anglican (B280). It is not Strathearn Heights (B261). Nothing here is copied from those.

Numbers are cited. Where sources disagree, both are given. Nothing was averaged. Height was not built up from storey counts.

## Building

**City permit records (checked 2026-11-23).** These settle the storey count and the unit count. They do not give a height in metres.

- Development permit file 298214168-002, 19 June 2019: four apartment buildings, 725 dwellings, underground parkade.
- File 298214168-065, 29 April 2020: dwellings increased from 725 to 760.
- Building permit, 11 September 2020: "To construct BLDG 1 a 26 storey apartment building on existing parkade - Holyrood Gardens." 284 units, construction value $58,975,500. Its floor area field reads 8001.88. That cannot be a gross floor area for 26 storeys, so do not use it. The permit has no occupancy date.
- File 298214168-092, 3 April 2023 (building 1): the 8 dwellings on the 26th floor become amenity areas, and one main-floor dwelling goes. Dwellings fall from 284 to 275. So building 1 has 26 floors, with 275 dwellings after this revision.
- File 298214168-098, 29 February 2024: building 2 is cut from 12 storeys to 6, with dwellings from 143 to 84. Building 2 is not the tower. Its occupancy date is 5 November 2025.
- File 298214168-135, 4 February 2026: the landscape plan is split into phases. Phase 1 is building 1. The permit does not give a completion date.

A 26-floor building at about 3.3 m a floor is about 86 m. That is the DC2 ceiling. The arithmetic is a check only, not a source. Storeys above ground, and whether the parkade counts, are not stated.

**Storeys and height.** Three figures are published, and they do not agree.

- The City's Direct Control provision DC2 (Area 2, Holyrood) sets a maximum height of 86.0 m for building type E. The tower is building type E in that provision. The table row reads "E ... 86.0 m". The tower is probably type E, but no source states that. This is the zoning ceiling, not the built height.
- An early plan, in one report summarised by the search, describes one tower up to 20 storeys at the 85 Street and 90 Avenue circle. The report is not named. The Edmonton Journal, 10 July 2018 ("New design OK'd for Holyrood Gardens") is a related result, and its page was not opened.
- A later report describes a 22-storey tower near a row of bungalows.
- A SkyriseCities forum thread titled "East Junction | 86m | 25s | Regency Developments | DER + Associates" gives 86 m and 25 storeys. That is a forum listing, not a City record. It was not confirmed as this tower.

The DC2 height ceiling (86.0 m) and the forum figure (86 m) agree on height. The storey counts from the press and forum (20, 22, 25) do not. The City's own record of 26 floors (2023 revision) supersedes them. The record gives no height in metres, so 86 m remains a ceiling, not a built height.

**Form, as the zoning sets it.** DC2 says:

- Storeys of building types D and E above 22.0 m in height have a maximum floor plate of 750 m².
- Building type E shall contribute to the City's skyline, using articulation and features that reduce the massing. The provision lists sculpting and variation of form as options.
- Buildings taller than 22.0 m need 35.0 m of separation, except that the distance between building type E and the most southern building type D in Area 2-B is 20.0 m.

These are rules, not the built form. No elevation, plan size or floor plate for the built tower was found.

**Footprint.** OpenStreetMap has no tower footprint. It has one landuse polygon for the whole site (way 556925041), which is kept as site context in `geometry.json`. No plan size, base width, or pier-free dimension is given here.

**Podium and roof.** Not found in the sources checked.

## Site

The site is the east side of 85 Street NW, from about 90 Avenue to 93 Avenue. The 2018 rezoning plan puts phase one there: four buildings with about 760 units. The OSM landuse strip for the whole site runs from about 53.5254 to 53.5306 in latitude. That is about 580 m long and about 85 m wide. The strip includes the whole site, not only the tower.

Building 1's permit geocode (53.52652, -113.45658) is in the upper part of that range, near the Connors Road junction. The earlier PRIORITY.md note that the old centre sat 311 m from Connors Road is not consistent with this junction, and should be treated as wrong.

The Holyrood LRT stop (P154, 53.52751, -113.45740) is about 120 m north-west of building 1's geocode.

The Mapillary frames in `street/` are from July and August 2018. They show the site before construction. Low-rise blocks, a brick institutional building, and roadwork cones sit on the road. They show the pre-construction site, not the tower.

## Ground

No elevation above sea level was published in the sources checked. The 2018 LiDAR clip for this site was not made in this session. The `elevation/` folder is not created yet. Do not add a value from another site.

## Status

Excavation began in March 2020, according to SkyriseCities. Phase one was expected to finish around 2022, according to an older report. No 2025 or 2026 status was confirmed. The current construction state is unknown. Before modelling, check the City's development permit record for this address and whether the tower stands.

## Still missing

- Current construction status, with a date: built, under construction, or not started.
- Height in metres. The City permit gives 26 floors and 275 dwellings, but no metres. The approved drawings or the development permit's approved plans would give a height. The City's online development application search, by file 298214168, may list them. Not opened this session.
- Built status. The permit has no occupancy date for building 1. The landscape phase 1 approval of 4 February 2026 suggests it is not finished. Confirm from the permit record or a photo.
- The tower footprint. OSM has none. The permit's floor-area figure is not usable.
- The exact centre. The permit geocode is a point for the building, not a surveyed footprint. Survey it against the 2019 aerial.
- Ground elevation and datum. The LiDAR clip is not made.
- Open-licence photographs of the tower. None were searched or saved in this session.
- Neighbouring building footprints. The Overpass query for buildings within 250 m failed on two mirrors.

## 2026-11-23 model (supersedes the footprint and centre notes above)

OpenStreetMap does map the building, in two ways added in 2023 (read through the OSM API map call; Overpass was down):

- Way 1209666933, "The Beacon Apartments at East Junction", 9009 85 Street NW, `building=apartments`, `building:levels=6`: the whole outline, an L of about 47 x 30 m, edges square to the compass.
- Way 1221215089, `building:part`, `building:levels=26`, `height=86`: its west square, 30.7 m (east-west) by 30.0 m (north-south), 922 m2, on 85 Street. The 6 levels on the outline belong to the east wing, 16.3 x 21.5 m.

The building is at the south end of the site, centre 53.52574, -113.45657. The permit geocode (53.52652, -113.45658) is an address point 87 m north of it. `geometry.json` now carries both ways and the new centre.

The 922 m2 square is more than the DC2 floor plate cap of 750 m2 above 22 m, so the OSM line is taken as the balcony edge: the model's shaft is 1.5 m inside it on the street, south and north faces, and 3.5 m inside at the back (about 694 m2).

Ground, 2018 DTM (pre-construction): 664.56 to 665.12 m inside the footprint, median 664.86 m; 664.45 to 665.15 m in the 8 m ring round it. The model datum is 664.56 m and grade is taken as 0.3 m above it.

Form: from the developer's rendering of the tower (DER + Associates, signed 13 November 2018, image 23492-124185 on the SkyriseCities project page; looked at only, not saved: it is not openly licensed). It shows a shaft in three vertical masses: grey panel each side of a taller white-framed pale-glass centre. The centre's frame stands proud of the roof with a yellow panel inside. It also shows blue vertical stripes in the joints, white balcony slabs with glass rails stacked round the corners, small yellow accent panels, a two-storey podium with brick bays, and a six-storey white wing with yellow and blue accents. The rendering says 25 storeys; the 2023 permit says 26. The tower's top is set at 86.0 m above grade (OSM, DC2 ceiling). The other mass heights (82 and 79.5 m), the floor heights, the mass split, and the balcony and accent positions are assumed. The full list is in the module docstring.

Not done: night lighting, and the other Holyrood Gardens buildings (not in OSM). Check in the sim: the exclusion polygon removes the sim's own autogen copy of the OSM building, the model sits on the ground, and the colours read like the rendering.
