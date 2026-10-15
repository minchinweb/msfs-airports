# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

The 2018 LiDAR shows the old bridge, before the Valley Line West deck and the 2023 girders.

1. **As-built span between abutment faces: Open, needs source.** The old raised structure is 47.9 m (road) and 51.7 m (second road way), consistent with the 46 m minimum.
2. **Deck elevation ASL and datum: Partly.** The old deck top is 665.9 m, and Groat Road under it is 656.0 to 662.9 m. The old deck was 8.0 m (median) above the road, so about 6 m of clearance after the deck, consistent with the 6 m kept clearance. The new deck may differ.
3. **As-built width: Partly.** The old raised width is 17.2 to 18.0 m, agreeing with the 18.4 m existing bridge; the 25.4 m reference design is unbuilt in this data.
4. **Soffit depth and haunch: Open, needs source.** Mapillary frame 5 (2018) shows a tan concrete post-and-rail parapet with a steel guardrail inside it, the same rail type as G117; no soffit.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
