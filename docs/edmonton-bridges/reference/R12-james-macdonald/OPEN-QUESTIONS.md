# Open questions, merged 2026-10-14

The "Ask before building" list in another session's review (`CURSOR-HANDOFF.md`, commit c5f3a92, removed 2026-11-23; its "Do not invent" list is kept at the end of this file) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Deck elevation ASL and where 97 Avenue and 98 Avenue meet grade: Answered for the deck, Partly for the approaches.** Road deck top 631.63 m (westbound) and 631.10 m (eastbound); river 613.73 m, so 17.4 m above the river; the profiles of both approaches are in `elevation/profiles.csv`.
2. **Span lengths, pier stations, shaft size: Open, needs source.** The aerial does not show them: the girder deck hides its piers from above (unlike R8, R13, R15), and only lamp-pole shadows and one deck joint (near chainage 350 m) show. The raised structure measures about 340 m on both decks.
3. **Girder depth at pier and midspan: Open, needs source.**
4. **Which structures are the 1971 approach bridges: Open, needs source.**
5. **Overall width: Answered.** The raised width is about 26 to 27 m (plus or minus 1 m) for the six lanes. The street frames 2, 3 and 5 show a grey concrete parapet about 1 m high topped by a tan open railing (about 1.4 to 1.5 m overall) and twin-arm lamps along the centre of the deck.

## Do not invent

From the review, unchanged. It was written before the LiDAR, so where it forbids a deck, ground or water elevation, use the measured CGVD2013 values above; still do not take an elevation from a published or mapped figure. Keep conflicting published figures separate and unaveraged, and do not turn a mapped plan length into a structural length.

Deck elevation above sea level, the datum, and soffit elevation. Span count and span lengths. Girder depth at the pier and at midspan. Pier count, pier heights, and the plan size of the shafts. Where the two approach bridges in the Journal's 2007 recap are. Longitudinal grade. Where 97 Avenue at Rossdale and 98 Avenue at Cloverdale meet grade. Do not scale the photographs. A count was not taken from them.

Where a photo is missing, check `street/` and `night/` first.
