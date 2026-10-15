# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Deck elevation ASL, datum, river level: Answered.** Track deck top 638.27 m (east) and 638.16 m (west), including rails and catenary; river 614.92 m, so 23.4 m above the river. The portal ends and ground are in `elevation/profiles.csv`.
2. **Span lengths and pier positions: Partly.** The raised structure measures 567 m on each track (chainage 86 to 653 m on the east track, 20 to 587 m on the west), between the 530 m seven-span box and the 685 m mapped way. Individual span and pier stations are open, measurable (pier caps on the aerial); not done.
3. **Soffit to walkway distance, which part is the three river spans: Open, needs source.** The DSM cannot see the walkway under the deck.
4. **Open view of the University tunnel mouth: Open, needs source.** The Mapillary frames for this site were not reviewed.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
