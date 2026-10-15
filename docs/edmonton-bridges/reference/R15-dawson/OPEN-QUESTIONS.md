# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Deck elevation ASL at each abutment: Answered.** Road deck top 631.31 m median (sidewalks 627.8 to 628.6 m); river 612.83 m, so 18.2 m above the river over the raised run. Ground at each end is in `elevation/profiles.csv`.
2. **Truss depth and panel counts: Open, measurable** (the top chord and panels show on the aerial); not done.
3. **Pier shaft height: Open, needs source.** The deck is 18.2 m above the river; the shaft is that less the bearing and truss floor depth, which are unknown.
4. **What the 12.5 m width measures: Open, needs source.** The LiDAR raised width (6.5 m) is not usable on a through truss. The Mapillary frame (2024) shows the approach, a concrete parapet with a steel rail and a footway of about 1.5 to 2 m, not the truss.
5. **Where each approach meets grade: Partly.** Profiles in `elevation/profiles.csv`.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
