# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Arch crown height: Partly.** The highest DSM return above the river along the road centreline is 52.8 m (river 614.13 m), consistent with the published 54 to 55 m above the river. Crown above the arch foot and above the roadway are still two separate unreconciled figures.
2. **Rib spacing at crown and feet: Open, measurable** on the aerial (the ribs show in plan); not done.
3. **Deck elevation ASL, datum, 13.3 m label: Answered for the deck.** Deck top median 629.05 m; river 614.21 m, so 14.7 m above the river over the whole raised run. The 13.3 m mid-span label is a lower number, which fits a roadway-to-soffit reading with a deck about 1.4 m deep; unconfirmed.
4. **Where the 230 m abutment centrelines sit on the 260.7 m way: Partly.** The raised structure is 248.6 m of that way, including approach fill. The centrelines themselves are not resolved.
5. **Strut count, 6. delta-pier count, 8. first-hanger distance: Open, measurable** on the aerial; not done.
7. **Longitudinal grade and where 105 Street and Walterdale Hill meet grade: Partly.** Ground profiles along the approach ways are in `elevation/profiles.csv`.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
