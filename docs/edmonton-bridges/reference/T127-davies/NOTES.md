# T127 Davies Elevated Guideway and Davies station (P157) — modeling brief

Edmonton. The Valley Line Southeast LRT elevated guideway over Davies Industrial, with the Davies station (P157) on its deck. Centre used by the project: 53.5003, -113.4486. Station centre: 53.49988, -113.44415. The line opened to passengers on 4 November 2023.

Two tracks, each on its own elevated way. Trains run north and south along the deck, between Avonmore (P156) to the north and Millbourne/Woodvale (P158) to the south. This is the first LRT model in the package. Davies is the only elevated stop on the Valley Line Southeast.

This is not the Whitemud Drive LRT bridge (T128, 53.4852, -113.4422). It is not the Capital Line over Whitemud (T129). The Capital Line and the Valley Line Southeast are different lines. Do not copy the Capital Line's span lengths or pier notes here. The Kâhasinîskâk pedestrian bridge is not this structure. The 98 Avenue guideway is not this structure either. The Valley Line West is a different contract.

Numbers below are cited. Where two sources disagree, both are given. Where only the project inventory (`lrt.md`) gives a number, it is marked as such. Nothing here was filled in by adding one citation to another. Nothing was scaled from a photograph.

## Guideway

**Type.** Elevated guideway for light rail, two tracks. The published sources describe the Davies span as an elevated concrete guideway. They do not give a girder type for Davies. The project inventory gives a girder depth of at most 2.5 m, and at most 4.5 m over 75 Street where there is no pier between the curbs. No public source checked gives a girder depth.

**Spans.** The 2019 progress count was 38 spans (`lrt.md`, project inventory). No public source checked gives the Davies span count, and no span lengths were published. The project inventory says piers are at least 20 m apart. No public source checked gives that spacing.

**Length.** Plan length in WGS84, one track: 1,491.3 m (way 4) and 1,485.9 m (way 5). The extract's stored values are 1,493 m and 1,488 m. Both are kept. These are horizontal lengths along the mapped nodes. They are not structural lengths. The two tracks are separate ways, so 1.49 km is one track, not the pair.

**Piers.** Pier count is not published. Line-wide, Wikipedia gives 45 piers on the Valley Line Southeast, citing press reports. Those reports say 30 of 45 piers were cracked in 2022. That is a line-wide figure. It is not a Davies count.

Pier shape is not settled by the sources checked. The project inventory says the piers are circular through the station and a split shaft with a triangular opening elsewhere. A 2017 construction photograph on Wikimedia Commons shows a V- or Y-shaped concrete pier with a split top at this site. That matches the split-shaft description, but it is one photograph and it does not give a size.

One search snippet gave pier heights of 6.0 m to 12.7 m for "the piers" of this line. The page was not opened, and it does not say which piers. It is not used in `geometry.json`.

**Clearances.** The guideway lifts trains over the CP and CN rail lines. The City says the rail lines cross perpendicular to the LRT tracks north and south of the station. The guideway also crosses Argyll Road. No clearance over Argyll Road, the rail lines, or 75 Street is published in the sources checked. The project inventory gives a minimum of 6.5 m over 75 Street. No public source checked gives that figure.

**Station on the deck.** Davies station sits on the elevated guideway. Wikipedia lists the structure type as elevated, the centre-loading platform, and two tracks. The Davies Transit Centre sits alongside: a bus centre with 15 bus bays, and a park and ride.

## Approaches

**North end.** The north end of both tracks is at 53.504944, -113.454872 (way 4) and 53.504932, -113.454936 (way 5). Surface ways continue north from there. They pass Avonmore (P156) at about 615 m of plan length from the bridge end. The project inventory gives K213 as 612 m from P156 to T127.

The start of the elevated section is given two ways. The City's Taking Shape update 4 (as read through a search summary) says the elevated section starts at 83 Street and Argyll Road. Railway Age (as read through a search summary) says it starts at 69A Avenue, over Argyll Road. The page for Railway Age could not be opened. Both are kept.

No gradient is published for the north approach. No elevation change is published. The point where the guideway meets grade is not published. The project inventory says the ramps are at most 5 m from grade to top of rail at both ends. No source checked gives that figure. The surface ways in `lrt-tracks.json` are plan lines only. They are not a climb to grade.

**South end.** The south end of both tracks is at 53.495637, -113.442378 (way 4) and 53.495638, -113.442445 (way 5). Surface ways continue south toward T128. The surface ways from the south end are 1,129 m and 1,129 m long in plan. The project inventory gives K214 as 1,130 m from T127 to T128. The City's Taking Shape update 4 (as read through a search summary) says the guideway returns to ground on 75 Street before McIntyre Road.

No gradient is published for the south approach. No elevation change is published. The point where the guideway meets grade is not published.

## Deck and station

**Elevation.** No deck elevation above sea level is published. No vertical datum is published. The project inventory gives no elevation either. No elevation is in `geometry.json`.

**Above the road or rail.** No height above Argyll Road, the CP or CN rail lines, or 75 Street is published in the sources checked.

**Deck thickness and track centres.** Not published in the sources checked.

**Platform.** Two tracks, centre-loading (Wikipedia infobox, without a citation). Platform width, length and height are not published. The platform footprint is not in the OSM extract, which has only the station node. No platform footprint was added.

**Canopy and roof.** The station roof is wood. Wikipedia says the wood roof uses 15,498 individual timber pieces, prepared and treated in Edmonton. It cites a 2020 TransEd update that was archived and was not opened here. The 2023 platform photograph shows curved arch ribs under a timber-faced soffit. The project inventory calls the ribs steel arch ribs at least 5 m apart with a radius at most 12.5 m. No public source checked confirms those rib figures. The roof height above the platform is not published.

**Park and ride.** 1,300 stalls. Wikipedia gives this figure. A search summary of the Edmonton FAQ gives the same figure, and the page itself was not opened. Opened with the transit centre on 4 September 2022 (Wikipedia, no citation in that line). The bus centre has 15 bus bays (Wikipedia, citing the Davies Transit Centre map).

**Station storeys and size.** The project inventory says three storeys on the deck, about 1,200 m² across three levels. No public source checked gives a storey count or a floor area.

**Architect.** DIALOG (Wikipedia infobox, citing the DIALOG page).

## Still missing

- Span count and span lengths, checked against a public source. The 38 is a project progress count.
- Girder type and depth for the Davies span.
- Pier count, pier heights and pier cross-section at Davies, including the circular piers through the station.
- Deck elevation above sea level and the datum. Soffit elevation.
- Clearance over Argyll Road, the CP and CN rail lines, and 75 Street.
- Gradient and elevation change for each approach. The point where each end meets grade.
- Platform length, width and height. Track centres.
- Canopy or roof height above the platform. Roof rib spacing and radius.
- Station storey count and floor area.
- Which start point is right for the elevated section: 83 Street and Argyll Road, or 69A Avenue.
