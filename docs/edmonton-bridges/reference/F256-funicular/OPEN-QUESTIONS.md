# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

The 2018 LiDAR (nominally 12 May) may predate the finished funicular, so structure heights here may show it unfinished; the terrain figures below do not depend on it.

1. **Which length is the as-built length along the rails: Open, needs source.** The horizontal run of the mapped track is 63.1 m.
2. **As-built vertical rise: Answered for the terrain.** Ground at the top of the track 663.04 m and at the bottom 638.46 m, a 24.6 m drop over 63 m, agreeing with the 2015 25 m drop. That is about 21 degrees against the recorded 23.5 degrees, so the track and the ground are not exactly parallel (the track stands on a beam above the ground at the bottom).
3. **Elevation ASL of the track ends and the lookout deck: Partly.** Ground ends as above; the footbridge top reads 637.74 m (DSM median) and about 12 m above its edge ground at the 95th percentile.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
