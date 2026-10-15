# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Deck elevation ASL and where 97 Avenue and 98 Avenue meet grade: Answered for the deck, Partly for the approaches.** Road deck top 631.63 m (westbound) and 631.10 m (eastbound); river 613.73 m, so 17.4 m above the river; the profiles of both approaches are in `elevation/profiles.csv`.
2. **Span lengths, pier stations, shaft size: Open, measurable** (piers in the channel show on the aerial); not done. The raised structure measures about 340 m on both decks.
3. **Girder depth at pier and midspan: Open, needs source.**
4. **Which structures are the 1971 approach bridges: Open, needs source.**
5. **Overall width: Answered.** The raised width is about 26 to 27 m (plus or minus 1 m) for the six lanes. The street frames 2, 3 and 5 show a grey concrete parapet about 1 m high topped by a tan open railing (about 1.4 to 1.5 m overall) and twin-arm lamps along the centre of the deck.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
