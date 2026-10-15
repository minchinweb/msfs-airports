# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Heights above the water for the decks, wheelhouse, canopy: Partly.** The boat was in the 2018 LiDAR: its footprint (567 m2) has a median surface of 620.09 m and a highest point of 623.64 m, against water at 613.66 m, so about 6.4 m (median) and 10.0 m (highest) above the water. Which part is the highest point (wheelhouse, canopy, wheel gear) is not known. Freeboard and the deck line need a photo with a scale.
2. **Waterline or dock ASL, datum: Answered.** Water 613.66 m (2018, nominal 12 May); the stage at another date is `RIVER-LEVEL.md` zero 609.92 m plus the stage, as a reach correction of about minus 0.1 m from the Low Level.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
