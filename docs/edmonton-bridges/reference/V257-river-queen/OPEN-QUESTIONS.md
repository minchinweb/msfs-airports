# Open questions, merged 2026-10-14

The "Ask before building" list in another session's review (`CURSOR-HANDOFF.md`, commit c5f3a92, removed 2026-11-23; its "Do not invent" list is kept at the end of this file) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Heights above the water for the decks, wheelhouse, canopy: Partly.** The boat was in the 2018 LiDAR: its footprint (567 m2) has a median surface of 620.09 m and a highest point of 623.64 m, against water at 613.66 m, so about 6.4 m (median) and 10.0 m (highest) above the water. Which part is the highest point (wheelhouse, canopy, wheel gear) is not known. Freeboard and the deck line need a photo with a scale.
2. **Waterline or dock ASL, datum: Answered.** Water 613.66 m (2018, nominal 12 May); the stage at another date is `RIVER-LEVEL.md` zero 609.92 m plus the stage, as a reach correction of about minus 0.1 m from the Low Level.

## Do not invent

From the review, unchanged. It was written before the LiDAR, so where it forbids a deck, ground or water elevation, use the measured CGVD2013 values above; still do not take an elevation from a published or mapped figure. Keep conflicting published figures separate and unaveraged, and do not turn a mapped plan length into a structural length.

Freeboard. The height of the lower deck, the upper deck, and the wheelhouse above the water. The height of the canopy. An air draft. The 10 m Valley Line window is not a height of this boat. Do not use the mapped pier edges or the vessel edge lengths as the hull or the dock. Do not average the length citations or the beam citations.

Where a photo is missing, check `street/` and `night/` first.
