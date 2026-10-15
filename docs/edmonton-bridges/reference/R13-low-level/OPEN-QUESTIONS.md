# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Geodetic elevation of each end of each deck: Answered.** East (1900) deck top 631.69 m, west (1949) deck 632.10 m; river 613.74 m, so 17.2 m above the river; the DTM at the ends is in `elevation/profiles.csv`. The gauge zero is 609.92 m (`RIVER-LEVEL.md`).
2. **Truss depth of each span: Open, measurable** (chord offsets in the DSM or the aerial); not done.
3. **Pier height and a pier count for the 1949 span: Open, needs source.** The deck is 17.2 m above the river; the pier is that less the truss and deck depth.
4. **Southbound span lengths one by one: Open, needs source.** The raised structure measures 209.7 m (west deck) and 211.0 m (east deck), against the mapped 212.6 m and 213.9 m and the published 211.7 m and 213.1 m.
5. **Which 1900 bay length (53 m or 51.8 m): Open, measurable** from pier positions on the aerial; not done.
6. The Mapillary frames show only approaches and ramps; they do not date the lighting.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
