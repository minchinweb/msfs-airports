# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Deck elevation ASL and datum: Answered.** Road deck top 631.82 m (southbound 631.79 m); east path 632.5 m; river 616.31 m, so 15.5 m above the river. Ground at the ends is 626.0 to 626.1 m.
2. **Seven span lengths, pier count: Answered from the 2019 aerial, plus or minus 1.5 m; pier height still needs a source.** Six river piers show as cap tabs along the east edge at chainage 32.7, 78.0, 122.4, 167.3, 212.4 and 257.3 m on the east carriageway way (22916458, from its south node), a steady 44.9 m apart. That is seven spans of about 44.9 m, 314 m in all, matching the published 315 and 315.5 m. The mapped way (291.5 m) is therefore short by about 12 m at each end: the south abutment lies near chainage minus 12 m and the north abutment near 302 m (seen at about 293 to 303 m). The 2019 aerial caught the deck in mid-rebuild (the west half open), which is why the caps show. The raised structure measures 287 m between the 3 m-rise points. See `AERIAL-READINGS.md`.
3. **Girder depth and haunch depth: Open, needs source.**
4. **Overall width: Answered.** Raised width 19.0 m (plus or minus 1 m), which agrees with a 4.2 m path plus two two-lane carriageways. The 22.1 m north-end edge is unresolved.
5. **West-side walk after 2020: Open, needs source.**
6. **What each published length includes: Partly** (see 2).
7. **Where the Mayfair and Glenora roads meet grade: Partly.** Profiles in `elevation/profiles.csv`.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
