# Open questions, merged 2026-10-14

The "Ask before building" list in another session's review (`CURSOR-HANDOFF.md`, commit c5f3a92, removed 2026-11-23; its "Do not invent" list is kept at the end of this file) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Deck elevation ASL and datum: Answered.** Deck top 636.23 m; ground under it 630.4 to 633.0 m.
2. **Deck width: Answered.** Raised width 13.0 m (plus or minus 1 m). Mapillary frame 1 (on the deck) shows three lanes, steel rails on posts at both edges, no sidewalk and no lamps on the deck.
3. **Clearance under the deck: Answered.** Deck top 5.7 m (median) above the road below; less 1 to 2 m of deck leaves roughly 4 m, consistent with the 4.5 m `maxheight` tag.
4. **Abutments only or intermediate piers: Open, needs source.** The raised run is 31.3 m; nothing in the frames shows a pier.
5. **Elevation change along the approach ways: Partly.** The north-east approach (way 36610268, 84 m) climbs from 632.9 to 635.85 m, about 3.5 percent; the rest are in `elevation/profiles.csv`.
6. **McDougall Hill way 636183922 node list: Answered.** Fetched from OpenStreetMap on 2026-10-14 and saved as `mcdougall-hill-way-636183922.json` (15 nodes, west 53.537844, -113.493275 to east 53.537822, -113.491135; two-lane one-way expressway, `maxheight` 4.5, lit, no sidewalk).
7. **A present-day view: Partly.** Four Mapillary frames, 2018 to 2024, after the 2013 rehabilitation.

## Do not invent

From the review, unchanged. It was written before the LiDAR, so where it forbids a deck, ground or water elevation, use the measured CGVD2013 values above; still do not take an elevation from a published or mapped figure. Keep conflicting published figures separate and unaveraged, and do not turn a mapped plan length into a structural length.

Deck elevation, soffit elevation, and the datum. Clearance under the deck. The tag `maxheight=4.5` on way 636183922 is not that clearance and not a deck elevation. Width and lane width. Pier count and pier height. Span count. The mapped centreline is two segments, 49.1 m. That is not a published span count. Gradient, elevation change, and where either approach meets grade.

Where a photo is missing, check `street/` and `night/` first.
