# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Deck elevation ASL at both ends: Answered.** Deck top 662.52 m; the ravine floor under it is 638.9 m, so the deck is 14.4 m above ground at the median and 23.6 m at the deepest point, consistent with the 22 m ravine depth.
2. **Overall deck width: Answered.** Raised width 24.0 m (plus or minus 1 m) at deck level: four lanes, a bike lane, two sidewalks and rails. The 13.6 m tag is not that. Mapillary frame 2 shows a tan concrete post-and-rail parapet with a steel guardrail along the curb.
3. **Girder depth: Open, needs source.** Mapillary shows only the road surface.
4. **Where the 83 m steel span and abutments sit: Open, needs source.** The raised structure is 102.4 m of the 111.9 m mapped line, consistent with integral abutments.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
