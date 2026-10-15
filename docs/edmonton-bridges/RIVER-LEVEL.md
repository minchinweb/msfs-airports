# North Saskatchewan River level at Edmonton

Written 2026-10-14. This is the answer to the "deck ASL and water ASL are null" blocker in the `MODEL-HANDOFF.md` files. Short version: **use the LiDAR river surface in `ELEVATION.md` as the water height (about 613.7 m at the Low Level, falling downstream, 614.9 m at the High Level). The gauge record below says how far that number moves with the season.**

## Where the data is, and a correction

The hint was "the sewer system outfalls through the City". The City's outfall layer (`data.edmonton.ca` `gpxt-s37s` "Drainage_Outfall", and the map view `efaq-9jrb`) holds only outfall **locations** (type, year built, road, neighbourhood). It has no invert elevations and no river readings, so it is no use here. The river gauge belongs to Water Survey of Canada (federal), reported by Alberta Environment and Protected Areas on rivers.alberta.ca.

| Item | Value |
| --- | --- |
| Station | 05DF001 North Saskatchewan River at Edmonton |
| Position | 53.53721, -113.48550 (the Low Level Bridge, so right at R13 and next to R12 and R14) |
| Operator | Water Survey of Canada |
| Vertical datum | "Assumed datum": the stage is height above a local gauge zero, not above sea level |
| Open API (no key) | `https://api.weather.gc.ca/collections/hydrometric-daily-mean/items?STATION_NUMBER=05DF001`, also `hydrometric-realtime` (5 minute, last 30 days), `hydrometric-annual-peaks`, `hydrometric-monthly-mean` |

Saved in `data/gauge/`:

- `05DF001-daily-mean.csv`: 41,519 daily rows, 1911-05-01 to 2024-12-31. **Discharge is there for the whole record; stage (water level) only for 2012-01-01 onwards (4,647 days).** Before 2012 the open API has no daily stage.
- `peaks.json`: the annual maximum and minimum levels and discharges (109 records).
- `05DF001-station.json`: station metadata as the API returns it.

The Water Survey's own site (`wateroffice.ec.gc.ca`, station 05DF001) and the HYDAT database carry the datum history and gauge-zero elevation. I could not retrieve those from here. The conversion below is derived from LiDAR instead and should be replaced if William can get the HYDAT datum.

## Stage to elevation

The 2018 City LiDAR holds the river surface. Nominal acquisition date is 2018-05-12 (the STAC date for `AB-Edmonton-1m`; the real flight days are not published and could be some weeks either side). The gauge read **3.825 m** that day (309 m3/s). At the gauge the LiDAR river surface is **613.74 m** (CGVD2013). So:

    gauge zero is about 609.92 m CGVD2013   (613.74 - 3.825)
    water surface ASL at the Low Level = 609.92 + stage

Uncertainty: the stage ran 3.74 to 4.19 m between 27 April and 20 May 2018, so the zero is good to about 0.2 m, until the flight date is pinned down.

Both the stage and the LiDAR surface are at the Low Level, where the gauge is. Elsewhere add the river's slope, which the LiDAR gives for the same 2018 day:

| Reach | LiDAR river surface (2018) | Note |
| --- | --- | --- |
| Groat Bridge R8 | 616.3 m | |
| High Level R10 and Menzies R9 | 614.9 m | |
| Walterdale R11 | 614.2 m | |
| Low Level R13, James MacDonald R12 | 613.7 m | gauge is here |
| Tawatinâ R14 | 613.3 m | |
| Dawson R15 | 612.8 m | |

To get a water height at another stage, add `(stage - 3.825)` to the figure for the reach. All figures are metres. Divide by 0.3048 for feet (613.74 m is 2,013.6 ft).

## What the river does (2012 to 2024 daily stage)

| Statistic | Stage m | Water surface at the Low Level m (zero + stage) |
| --- | --- | --- |
| Lowest day (2022-11-08) | 2.58 | 612.5 |
| 10th percentile | 3.08 | 613.0 |
| Median | 3.59 | 613.5 |
| 90th percentile | 4.35 | 614.3 |
| Highest day (2013-06-23, flood) | 9.03 (9.26 instantaneous) | 618.9 (619.2) |

Median stage by month: Jan 3.74, Feb 3.72, Mar 3.78, Apr 3.62, May 3.55, Jun 3.84, Jul 3.73, Aug 3.52, Sep 3.26, Oct 3.10, Nov 3.19, Dec 3.93 (winter values include ice effects). The 90th percentile for June is 5.13, July 4.95: the summer rises are real, but the river sits within about half a metre of the median most of the time. A typical summer-day water height is therefore the 2018 LiDAR value, minus or plus 0.3 m. Errors of that size are small against decks 15 to 48 m above the river.

Highest annual instantaneous peaks (2012 on): 2013-06-23 9.26 (flood), 2020-04-21 8.38, 2023-06-22 6.77, 2016-08-24 6.75, 2022-06-17 6.70, 2018-04-21 6.61. Lowest instantaneous: 2017-09-03 2.50.

Use for modelling: the bridge decks are what matter and they are fixed, so a water height within half a metre is fine. If the sim's river is not flat at this value (MSFS water follows its own terrain mesh), measure the sim's river where each bridge sits and set the deck as `LiDAR deck minus LiDAR river` above the sim's own water. See `ELEVATION.md` for those clearances (for example the High Level upper deck reads 47.54 m above the river, matching the handoff's 47.55 m).

## What is still open

1. **Gauge zero and its datum from HYDAT.** The derived 609.92 m rests on a nominal flight date.
2. **LiDAR flight dates.** The 2018 City LiDAR was flown in spring 2018, but the dates are not in the STAC record. The City's metadata page or the RFP 939448 documents may say.
3. **Vertical datum of the sim.** The LiDAR is CGVD2013 (orthometric). MSFS reports heights against its own geoid model; the offset in Alberta is probably under 1 m, which is small beside the deck clearances, but it was not checked against the sim. A check: compare the CYXD runway LiDAR height with the airport's reference altitude in the CYXD project.
4. **Pre-2012 stage.** Only discharge is open. Historical stage for the 1915 and 1986 floods, should it ever matter for a historic package, is in the 1987 Alberta publication "Analysis of North Saskatchewan River floods at Edmonton" (open.alberta.ca). Not needed for the present-day package.
