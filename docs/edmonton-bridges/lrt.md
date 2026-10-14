# Edmonton LRT: above-ground stations and viaducts

Last updated: 2026-10-14. Third scope, beside the river crossings in `bridges.md` and the freeway bridges in `freeway-bridges.md`. This one is the light-rail structures that read from the air: viaducts, LRT bridges, and the stations that are not in a tunnel. The above-ground track is saved in `lrt-tracks.json` so it can be followed later if the rails themselves are modelled.

OpenStreetMap centres were pulled 2026-10-14. A station centre is the mapped platform node. An extension centre marked estimated is a point on the mapped centreline at the named cross street, not a surveyed platform. Two tracks are mapped separately, so a length in that file is one track, not the pair.

Capital Line and Metro Line are high-floor (Siemens U2 and SD-160, high platforms). Valley Line is low-floor (Flexity, curb-height platforms). All three run under catenary. The Dudley B. Menzies Bridge (R9) and the Tawatinâ Bridge (R14) are already on the river list. They are not given a second code here.

## Above-ground stations in service

Underground, and not plotted: Central, Bay/Enterprise Square, Corona, Government Centre, University, and MacEwan. Churchill is plotted once. The Capital and Metro platforms are underground; the Valley Line stop is at street level on the same square.

### Capital Line

High-floor. Clareview to Century Park. The downtown section and University are in tunnel. The line is elevated only on R9, over Whitemud Drive (T129), and over 118 Avenue (T130).

| Station | Centre | Notes |
| --- | --- | --- |
| Clareview | 53.60177, -113.41142 | Northeast terminus. At grade. The yard west of the Kathleen Andrews Transit Garage is the `service=yard` track in the geometry file. |
| Belvedere | 53.58805, -113.43348 | At grade, in the rail corridor. |
| Coliseum | 53.57068, -113.45838 | At grade, beside the 118 Avenue flyover (T130). |
| Stadium | 53.55995, -113.47071 | At grade, east of Commonwealth Stadium. |
| Health Sciences/Jubilee | 53.52006, -113.52589 | First above-ground station south of the University tunnel. |
| McKernan/Belgravia | 53.51308, -113.52619 | At grade. |
| South Campus/Fort Edmonton Park | 53.50287, -113.52842 | At grade. |
| Southgate | 53.48576, -113.51678 | At grade, just north of the Whitemud flyover (T129). |
| Century Park | 53.45731, -113.51637 | South terminus. At grade on the west side of 111 Street. |

### Metro Line

Shares the Capital Line from Churchill to Health Sciences. Above ground it is the northwest leg.

| Station | Centre | Notes |
| --- | --- | --- |
| Kingsway/Royal Alex | 53.55803, -113.50147 | At grade. |
| NAIT/Blatchford Market | 53.56695, -113.50909 | At grade. Opened 20 January 2024, replacing the temporary NAIT stop. Platforms can take five-car trains. Solar canopy. |
| Blatchford Gate | 53.57695, -113.51041 | Built with phase 1. Not in passenger service until the city's ridership test is met. |

### Valley Line Southeast

Low-floor. 102 Street to Mill Woods, opened 4 November 2023. Eleven stops are at street level. Davies is the elevated station. A short tunnel with no station sits north of the Tawatinâ Bridge.

| Stop or station | Centre | Notes |
| --- | --- | --- |
| 102 Street | 53.54317, -113.49524 | At grade, downtown terminus until Valley Line West opens. |
| Churchill | 53.54377, -113.48904 | Valley Line stop at street level. Underground Capital/Metro platforms at the same place. |
| Quarters | 53.54440, -113.48405 | At grade. |
| Muttart | 53.53621, -113.48000 | At grade, at the bottom of the ramp off the south end of R14. |
| Strathearn | 53.53171, -113.46231 | At grade. |
| Holyrood | 53.52751, -113.45740 | At grade. |
| Bonnie Doon | 53.51981, -113.45538 | At grade. |
| Avonmore | 53.51046, -113.45508 | At grade. North of the Davies viaduct. |
| Davies | 53.49988, -113.44415 | Elevated. The only open elevated station. Three storeys, centre platform, 1,300-stall park and ride, bus terminal around the piers. |
| Millbourne/Woodvale | 53.47469, -113.43896 | At grade, south of the Whitemud LRT bridge (T128). |
| Grey Nuns | 53.46243, -113.43451 | At grade. |
| Mill Woods | 53.45839, -113.43097 | Southeast terminus. At grade. |

## Viaducts and LRT bridges

| Code | Structure | Centre | State | What to model |
| --- | --- | --- | --- | --- |
| T127 | Davies Elevated Guideway | 53.5003, -113.4486 | Open | About 1.49 km per track on the mapped bridge ways, from 53.5049, -113.4549 (near 69A Avenue / 83 Street) to 53.4956, -113.4423 (75 Street, north of McIntyre Road). It clears Argyll Road, the CP and CN tracks, and 75 Street so trains do not wait for freight. The 2019 progress count was 38 spans. Piers are at least 20 m apart. Through the station they are circular. Elsewhere the top 4.7 m of the pier is a split shaft with a triangular opening: shaft thickness at most 0.9 m, top width at most 4.5 m, lower shaft tapering between 12:1 and 15:1. Girder depth at most 2.5 m, or up to 4.5 m over 75 Street if there is no pier between the curbs. Minimum clearance over 75 Street is 6.5 m. Ramps at both ends are at most 5 m from grade to top of rail. Davies Station sits on this deck: about 1,200 m² on three levels, platform on top, curved roof on steel arch ribs at least 5 m apart with a radius at most 12.5 m, heavy-timber soffit, clerestory, glass enclosure. No catenary poles on the platform. |
| T128 | Whitemud Drive LRT bridge | 53.4852, -113.4422 | Open | Valley Line on 66 Street, beside the existing road bridge over Whitemud Drive. Mapped deck about 67 m. One pier, in the median, in line with the road bridge pier. Abutments at least 25 m from the median centreline. Headslopes in line with the road bridge. |
| T129 | Capital Line over Whitemud Drive | 53.4828, -113.5165 | Open | High-floor line between Southgate and Century Park. Mapped deck about 83 m, layer above the freeway. Two tracks. |
| T130 | Capital Line over 118 Avenue | 53.5704, -113.4586 | Open | Beside Coliseum. Mapped deck about 62 m, layer above 118 Avenue. |
| T131 | 87 Avenue elevated guideway | 53.5205, -113.618 | Under construction | Valley Line West, between the Misericordia and West Edmonton Mall stations, along the centre of 87 Avenue. The city describes a guideway of nearly 2 km on 46 Y-shaped piers. The piers carry 60-tonne precast segments cast in Blackfalds; the last segment was set with a 400-tonne gantry. The contract's preliminary pier numbers run from the west (P02–P16 near 176–180 Street, P24 west of 172 Street, P38–P40 near 165 Street). Minimum clearance is 5.5 m over 165, 169, 170, 175, and 178 Street and over the mall and hospital driveways, and 3.0 m over pedestrian crossings. Where the approach fill is higher than 1 m, the track slab is on piles. The mapped centreline along 87 Avenue from 178 Street (53.5213, -113.6310) to 165 Street (53.5195, -113.605) is the horizontal alignment. |
| T132 | Anthony Henday LRT bridge, Lewis Estates | 53.5224, -113.6584 | Under construction | Valley Line West, on the south side of the existing 87 Avenue bridge over the Henday. At least 10 m clear of that bridge. One pier, in the median, in line with the road bridge pier. Abutment faces in line with the existing abutment seats. Steel girders were up in 2024; in the second quarter of 2026 the track was going down on the west approach. Design clearance is 5.7 m, or 0.2 m more than the adjacent Henday structures, and 6.0 m if the deck is a slab. Approach fills higher than 1 m sit on piled approach spans. Lewis Farms, the western terminus, is at grade just west of here. |
| T133 | Stony Plain Road bridge | 53.5478, -113.5458 | Under construction | New bridge where Stony Plain Road crosses Groat Road. Same place as G118, which is the old span and is still drawn as a cross. The old bridge was demolished in 2023. The replacement is a single span with no piers, at least 46 m, 6 m over Groat Road, integral abutments, and a separate track slab on a cast-in-place deck. It carries the road and the Valley Line. |
| T134 | Blackmud Creek LRT bridge | 53.4409, -113.5185 | Under construction | Capital Line South, west of the 111 Street road bridges. At least 5 m clear of those bridges. Pier finish matches the road bridge. Profile within 300 mm of the road bridge. A 4.2 m shared-use path is on the west side. Piling was done in 2025; girders were expected in 2026. The centre is the mapped centreline in the ravine, not an abutment survey. |
| T135 | Anthony Henday LRT bridge, Heritage Valley | 53.4354, -113.5237 | Under construction | Capital Line South, south of Twin Brooks, crossing the Henday on a 49° skew. Two steel network arches with a post-tensioned concrete deck over the highway, plus two concrete-girder approach spans. Inclined hangers. One rectangular median pier with chamfered corners and a hammerhead cap; the piers at the end of the arch spans are either that shape or a two-column bent. Arch ribs are shop-painted steel. Clearance over the mainline and ramps is at least 6.2 m, including 0.1 m tolerance and 0.2 m for a future overlay. Deck drainage is taken off at the approach piers, not dropped on the Henday. Piling was underway in March 2026, and arch steel was being delivered in June 2026. This is the bridge that will show on a south departure toward CYEG. |
| T136 | Walker Bridge | 53.586, -113.515 | Design only | Metro Line Northwest. Elevated crossing of Yellowhead Trail and the CN Walker Yard, chosen over a tunnel in the 2019 preliminary design. It is also the walking and cycling link. No span, pier count, or clearance has been published. The mapped proposal leaves Blatchford at 53.579, -113.510 and is back at street level by about 53.588, -113.517. The centre above is the middle of that grade-separated run. Unfunded in 2026. Council asked in 2026 for cheaper options, including bus rapid transit, because the Yellowhead and yard crossing dominates the cost. |

R9 is the Capital Line river bridge. The mapped bridge ways run about 685 m per track, from 53.5327, -113.5108 at the downtown portal to 53.5273, -113.5156 at the University tunnel, so the elevated section is longer than the river span alone. R14 is the Valley Line river bridge, an extradosed concrete box with pylons 24–30 m above the deck and a pedestrian deck hung underneath. The mapped bridge ways continue south to about 53.5374, which is the elevated guideway over 98 Avenue down to the Muttart ramp. That south run is part of the same bridge ways as R14, about 470 m per track from 53.5416 to 53.5374.

Not LRT decks: the Kâhasinîskâk Bridge is the pedestrian bridge over Connors Road built with Valley Line Southeast. The 23 Avenue crossing on Capital Line South is an underpass, not a viaduct.

## Extensions

Status is the city's July 2026 construction update. "Preliminary design only" means drawings to about 30 percent and no builder.

### Valley Line West, downtown to Lewis Farms

Under construction since 2022. Major construction is scheduled through 2028, then testing. Opening date is still to be set. Fourteen street-level stops and two elevated stations. In the second quarter of 2026 the elevated stations were in structural steel, the Henday bridge had track on the west approach, and 87 Avenue from 159 Street to the Henday was still down to one lane each way.

The mapped construction centreline is about 14.1 km per track, from Lewis Farms at 53.5228, -113.6679 to 102 Avenue at 53.5431, -113.4953. Centres below are on that line. They are estimated.

| Stop or station | Type | Centre | Notes |
| --- | --- | --- | --- |
| Lewis Farms | At grade, centre platform | 53.5228, -113.6679 | Western terminus, west of the Henday. Park and ride and the storage facility. |
| Aldergrove/Belmead | At grade, side platform | 53.5213, -113.648 | 87 Avenue between the Henday and the elevated guideway. |
| West Edmonton Mall | Elevated, side platform | 53.5206, -113.624 | On T131, at the mall transit centre. |
| Misericordia | Elevated, side platform | 53.5197, -113.613 | On T131, at the hospital. |
| Meadowlark | At grade, side platform | 53.5198, -113.5965 | Where the line leaves 87 Avenue. |
| Glenwood/Sherwood | At grade, split side platform | 53.528, -113.591 | On the climb from 87 Avenue toward Stony Plain Road. |
| Jasper Place | At grade | 53.5412, -113.5902 | Stony Plain Road. |
| Stony Plain Road/149 Street | At grade | 53.5413, -113.5799 | |
| Grovenor/142 Street | At grade | 53.5432, -113.5641 | |
| Glenora | At grade | 53.5468, -113.5495 | West of the Groat crossing. |
| Stony Plain Road bridge | Bridge, not a stop | 53.5478, -113.5458 | T133. |
| 124 Street | At grade | 53.5463, -113.5311 | East of Groat Road. |
| Brewery/120 Street | At grade | 53.5462, -113.523 | On the mapped line between 124 Street and 112 Street. |
| The Yards/116 Street | At grade | 53.5462, -113.514 | Same stretch. |
| MacEwan Arts/112 Street | At grade | 53.5462, -113.5064 | The line turns south onto 102 Avenue here. |
| NorQuest | At grade, side platform | 53.5430, -113.4991 | 102 Avenue. Platform integrated with the sidewalk. |
| Alex Decoteau | At grade, side platform | 53.5431, -113.497 | 102 Avenue, west of the open 102 Street stop. |

### Capital Line South, Century Park to Heritage Valley, and the airport

Phase 1 is under construction (2025–2029): 4.5 km, high-floor, along the west side of 111 Street from Century Park to Heritage Valley North, just north of Ellerslie Road. It does not cross Ellerslie Road. The contract is about $1.4 billion. The mapped construction centreline is 4.7 km per track and ends at 53.42512, -113.54559.

| Place | Type | Centre | Notes |
| --- | --- | --- | --- |
| 23 Avenue | Underpass | 53.453, -113.517 | The line goes under the intersection. Not a bridge. |
| Twin Brooks | At grade | 53.4468, -113.5167 | Neighbourhood station, smaller than Century Park. Estimated on the centreline. |
| Blackmud Creek | Bridge | 53.4409, -113.5185 | T134. |
| Anthony Henday Drive | Bridge | 53.4354, -113.5237 | T135. The Heritage Valley crossing. |
| Heritage Valley North | At grade | 53.42512, -113.54559 | End of phase 1. Connects to the Heritage Valley transit centre and park and ride. |
| Llew Lawrence maintenance facility | Yard | south of the Henday | Storage and maintenance. South of T135. |

Phase 2 is preliminary design, approved by council in 2020, and not funded. About 3.5 km from Heritage Valley North across Ellerslie Road to Desrochers, north of 41 Avenue SW. The grade separation at Ellerslie Road has not been chosen. No bridge was found on this section. The mapped proposed centreline is 3.4 km. Estimated stations on that line:

| Station | Centre | Notes |
| --- | --- | --- |
| 20 Avenue SW | 53.4198, -113.5448 | At the future South Edmonton Hospital site. |
| Heritage Valley | 53.4102, -113.5455 | Not Heritage Valley North. |
| Desrochers | 53.3953, -113.5414 | End of the approved Capital Line. North of 41 Avenue SW. |

There is no LRT alignment from Desrochers to CYEG. The airport is about 9 km further south. A City Plan mass-transit test ("City III") ran the Capital Line through to the airport and reused two regional-rail stop names, Township Road 510 and Highway 19. That test did not produce a corridor, a structure, or a funded project. Nothing is drawn past Desrochers.

### Capital Line Northeast, Clareview to Gorman

Preliminary engineering was finished in 2010 and is still unfunded. The city's July 2026 table lists it as preliminary design only. The project is 2.9 km, mostly in the existing CN right of way, with street-level crossings at 144 Avenue and 153 Avenue. There is no viaduct. The station is in the Gorman area, north of 153 Avenue and east of the CN tracks. ("Gorman", not a separate northern name.)

The mapped proposed way is 4.2 km, from 53.6037, -113.4085 just north of Clareview to 53.6298, -113.3694. That is longer than 2.9 km because the way continues past the station toward the north city limit. The station dot is the point on that way north of the 153 Avenue crossing: 53.6218, -113.3704, estimated. The 153 Avenue crossing on the same way is 53.6157, -113.3889.

### Metro Line Northwest, Blatchford to Campbell Road and St. Albert

Phase 1 (NAIT to Blatchford) is built. Phase 2 (Blatchford to Castle Downs, 4.2 km) has land-purchase funding only. Phase 3 (Castle Downs to Campbell Road) is preliminary design. The July 2026 table lists both as preliminary design only. The line is mostly at street level. The one elevated structure is T136, over the Yellowhead and the CN Walker Yard.

The mapped proposed centreline is 9.3 km, from Blatchford Gate at 53.5788, -113.5104 to Campbell Road at 53.6153, -113.5949. It runs north on 113A Street, then west on 153 Avenue. Estimated stations on that line, from the city's 2025 booklet:

| Station | Centre | Notes |
| --- | --- | --- |
| 132 Avenue | 53.596, -113.517 | On 113A Street. Avenue latitude is estimated. |
| 137 Avenue | 53.602, -113.517 | On 113A Street. |
| 145 Avenue | 53.610, -113.517 | On 113A Street. |
| Castle Downs | 53.6160, -113.5269 | 153 Avenue. End of phase 2. |
| 127 Street | 53.6166, -113.5450 | Along 153 Avenue. |
| 137 Street | 53.6145, -113.5660 | Along 153 Avenue. |
| Campbell Road | 53.6153, -113.5949 | Nakî transit centre and park and ride. End of the Edmonton project. This is the connection toward St. Albert. |

The Edmonton line stops at Campbell Road. A 2016 council report says St. Albert's transportation plan shows a further station near the Sturgeon Community Hospital. No alignment, span, or station coordinate for that extension was found, so nothing is drawn west of Campbell Road.

## Also mapped, not on this list

OpenStreetMap has a proposed way of about 4.3 km south from Mill Woods (53.4585, -113.4291) to 53.4252, -113.4179, toward Ellerslie Road. It has no station names and it is not one of the four extensions above. It is in `lrt-tracks.json` and it is not drawn.

The geometry file also keeps crossovers, sidings, and yards (Clareview / Kathleen Andrews, the Valley Line shops, and the tunnel storage tracks). Those are not drawn. The Gerry Wright operations facility is at the Valley Line shops near Whitemud Drive and 75 Street. Valley Line West adds a second building there and the Lewis Farms storage facility.

Sources: OpenStreetMap light-rail, construction, and proposed ways, 2026-10-14; City of Edmonton, [Valley Line West](https://www.edmonton.ca/projects_plans/transit/valley-line-west), [project history](https://www.edmonton.ca/projects_plans/transit/project-history), and the 2026 Q2 dashboard; Valley Line Southeast and Valley Line West project-agreement Schedule 5 (structures, facilities, and the Davies urban-design requirements); TransEd, Valley Line Southeast FAQ; [Davies station](https://en.wikipedia.org/wiki/Davies_station); City of Edmonton, Capital Line South fact sheet, phase 1 booklet, and Schedule 5 structures (Blackmud Creek and the Heritage Valley network arches); City of Edmonton, Capital Line Northeast and Metro Line Northwest pages, and the Metro Line NW booklet (2025 update); City of Edmonton, 2026 mid-season LRT construction update (July 2026); City Plan mass-transit scenario analysis (the airport test); Edmonton council report on the Metro Line Yellowhead / Walker Yard crossing (bridge preferred to a tunnel).
