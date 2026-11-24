# Open questions, merged 2026-10-14

The "Ask before building" list in another session's review (`CURSOR-HANDOFF.md`, commit c5f3a92, removed 2026-11-23; its "Do not invent" list is kept at the end of this file) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

The 2018 LiDAR (nominally 12 May) may predate the finished funicular, so structure heights here may show it unfinished; the terrain figures below do not depend on it.

1. **Which length is the as-built length along the rails: Open, needs source.** The horizontal run of the mapped track is 63.1 m.
2. **As-built vertical rise: Answered for the terrain.** Ground at the top of the track 663.04 m and at the bottom 638.46 m, a 24.6 m drop over 63 m, agreeing with the 2015 25 m drop. That is about 21 degrees against the recorded 23.5 degrees, so the track and the ground are not exactly parallel (the track stands on a beam above the ground at the bottom).
3. **Elevation ASL of the track ends and the lookout deck: Partly.** Ground ends as above; the footbridge top reads 637.74 m (DSM median) and about 12 m above its edge ground at the 95th percentile.

## Do not invent

From the review, unchanged. It was written before the LiDAR, so where it forbids a deck, ground or water elevation, use the measured CGVD2013 values above; still do not take an elevation from a published or mapped figure. Keep conflicting published figures separate and unaveraged, and do not turn a mapped plan length into a structural length.

An as-built vertical rise. The 25 m drop is a 2015 pre-construction figure. The 50 m figure is the valley, not the track. The 66.0 m at 23.5 degrees was not converted into a rise. Which published track length is the as-built length along the rails. The Journal states 55 m. The award submission states 66.0 m along the grade. The mapped line is 64.0 m horizontal. Do not add the three spans, and do not match them to the mapped edges. Do not draw the promenade. The Journal states a 200 m walkway. The City states about 260 m for the whole walk. The 55.3 m gap between the mapped track and the mapped bridge is neither of those. Pier height. Do not use the City's approximate 6 m as a deck elevation.

Where a photo is missing, check `street/` and `night/` first.
