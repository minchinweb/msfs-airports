# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Grade to ridge and grade to the tallest turret: Partly.** The DSM over the footprint peaks at 714.95 m, 48.1 m above the ground at the edge (666.83 m), which agrees with the published 47.7 m (156 ft), so that figure is probably to the tallest point. The roof's 95th percentile is 42.5 m above ground and the median 33.3 m, so the main ridge is somewhere between roughly 33 and 42 m; ridge and turret are not separated.
2. **Grade at 100 Street, ridge elevation, datum: Answered.** Ground at the building edge 666.83 m (665.0 to 667.31 m), CGVD2013. This replaces the earlier note in `BLOCKERS.md` that put the ground at 614 to 640 m.
3. **Whether the Bing ring is the footprint to build: Open, measurable** (compare the DSM roof edge with the ring); not done. The ring area is 2,426 m2.
4. **Turret count and roof masses: Open, measurable** (separate peaks in the DSM); not done.
5. **Copper colour as a specification: Open, needs source.** The night photo shows a floodlit warm facade only.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
