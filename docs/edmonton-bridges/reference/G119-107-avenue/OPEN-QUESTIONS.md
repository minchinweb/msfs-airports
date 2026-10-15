# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Deck elevation ASL and datum: Answered.** Deck top 667.95 m (south) and 668.00 m (north); Groat Road below is 661.4 to 661.5 m, with the embankments to 665 m.
2. **Three span lengths or pier positions: Open, measurable** (two column piers visible in Mapillary frame 5; positions on the aerial); not done. The raised structure is 48 to 51 m.
3. **Clearance over Groat Road: Answered.** Deck top 5.9 to 6.0 m above the road, so about 4.5 m after a 1 to 1.5 m deck, consistent with the 4.8 and 4.9 tags.
4. **Fascia depth: Partly.** Mapillary frames 1, 2 and 5 show a thin flat slab, looking about 1 to 1.5 m deep, a pale parapet with an open railing, and a dark soffit on two column piers. Not measured.
5. Groat Road below has three lanes each way with a concrete median barrier. The raised width of 37.5 m is the two carriageways and two sidewalks.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
