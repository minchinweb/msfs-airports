# Open questions, merged 2026-10-14

The "Ask before building" list in another session's review (`CURSOR-HANDOFF.md`, commit c5f3a92, removed 2026-11-23; its "Do not invent" list is kept at the end of this file) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Geodetic elevation of each end of each deck: Answered.** East (1900) deck top 631.69 m, west (1949) deck 632.10 m; river 613.74 m, so 17.2 m above the river; the DTM at the ends is in `elevation/profiles.csv`. The gauge zero is 609.92 m (`RIVER-LEVEL.md`).
2. **Truss depth of each span: Open, measurable** (chord offsets in the DSM or the aerial); not done.
3. **Pier height and a pier count for the 1949 span: Open, needs source.** The deck is 17.2 m above the river; the pier is that less the truss and deck depth.
4. **Southbound span lengths one by one: Open, needs source.** The raised structure measures 209.7 m (west deck) and 211.0 m (east deck), against the mapped 212.6 m and 213.9 m and the published 211.7 m and 213.1 m.
5. **Which 1900 bay length (53 m or 51.8 m): Answered, 53 m.** Pier cutwater noses show on the west edge at chainage 52.4, 105.3 and 158.4 m on the east deck way (31882107, from its south-east node), 53 m apart, with the truss ends at about 0 and 212 m: four equal spans of 53 m (212 m), and three piers for the 1900 span. See `AERIAL-READINGS.md`. Truss depth and panel counts are still not measured.
6. **Deck frames exist** (filed under V257, read in `STREET-READINGS.md`): two truss colours (rust-brown and pale sea-green), a low concrete curb with a steel W-beam rail on both sides, a pale green lattice fence on the east sidewalk, no lamps on the deck. They do not date the lighting.

## Do not invent

From the review, unchanged. It was written before the LiDAR, so where it forbids a deck, ground or water elevation, use the measured CGVD2013 values above; still do not take an elevation from a published or mapped figure. Keep conflicting published figures separate and unaveraged, and do not turn a mapped plan length into a structural length.

Deck elevation above sea level, and the datum, for both spans. Clearance to the river, and a navigation clearance. The 13 m figure is the 1915 flood above low water. Truss depth, for both spans. Southbound span lengths one by one. Pier heights, for both spans, and a pier count for the southbound span alone. Longitudinal grade. Where McDougall Hill, Connors Road, Rossdale Road, and Scona Road meet grade. Keep 53 m and 51.8 m apart.

Where a photo is missing, check `street/` and `night/` first.
