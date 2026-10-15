# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Deck elevation ASL for ways 22916470, 106711204 and 106711230: Answered.** Westbound avenue deck 631.46 m (ground under 624.1 to 628.6 m); eastbound B126 deck 633.10 m (624.4 to 629.9 m); eastbound ramp 632.74 m (624.6 to 629.9 m). Deck top is 6.9, 8.4 and 7.9 m (median) above the ground under; the Scona Road bridge (B065) is 631.57 m, 5.4 m above ground.
2. **Published width for each deck: Partly.** Raised widths (plus or minus 1 m): westbound 20.0 m, eastbound 21.5 m, ramp 22.0 m; these include neighbouring decks at the same level, so the three are not separated. The 11.1 m tag is not confirmed.
3. **B126 wording (Scona or Connors): Open, needs source.**
4. Mapillary frames 4 and 5 (on the deck) show a concrete parapet about 0.9 to 1 m high with a metal top rail, no sidewalk, and curved lamps on tall poles at the outside edge.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
