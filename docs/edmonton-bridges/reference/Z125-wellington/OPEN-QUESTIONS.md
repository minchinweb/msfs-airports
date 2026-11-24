# Open questions, merged 2026-10-14

The "Ask before building" list in another session's review (`CURSOR-HANDOFF.md`, commit c5f3a92, removed 2026-11-23; its "Do not invent" list is kept at the end of this file) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

The 2018 LiDAR shows the old 1932 arch structure, not the finished replacement. No Mapillary frame exists within 250 m.

1. **Which option was built and whether it stands now: Open, needs source.**
2. **Built span length: Open, needs source.** The raised run of the old structure is 57 to 70 m.
3. **Deck elevation ASL, datum: Partly.** The old deck top is 664.36 m, and the ravine floor under it is 653.0 to 661.1 m, so the deck was 9.1 m (median) and up to 11.4 m above ground. The new deck may differ.
4. **As-built width: Open, needs source.** The old structure reads 17 to 19 m raised width.
5. **Girder depth: Open, needs source.**

## Do not invent

From the review, unchanged. It was written before the LiDAR, so where it forbids a deck, ground or water elevation, use the measured CGVD2013 values above; still do not take an elevation from a published or mapped figure. Keep conflicting published figures separate and unaveraged, and do not turn a mapped plan length into a structural length.

Which girder was built, steel or NU2400. A published span length. Do not use 72.3 m or 70.5 m as the structural span. Deck elevation and clearance to the ravine. A girder-design width. The 4.2 m and 2.8 m are the 2023 update. The 23.78 m is the April 2024 preliminary width, later described as due to be reduced. Do not use 16.6 m, the width tag 12.4, or the right-of-way 30.6 m as the girder width. Girder depth. Do not add piers to the finished span.

Where a photo is missing, check `street/` and `night/` first.
