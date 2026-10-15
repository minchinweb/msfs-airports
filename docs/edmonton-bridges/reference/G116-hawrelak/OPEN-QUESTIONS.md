# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Deck elevation ASL and clearance over Groat Road: Answered.** Deck top about 635.2 to 635.3 m (cycleway 635.6 m); Groat Road below is about 628.4 to 628.9 m. The deck is 5.8 to 6.4 m above the road, so roughly 4.5 to 5 m of clearance after the deck; the unconfirmed `maxheight` 5.3 m is consistent.
2. **Outer deck width: Partly.** The raised width at deck level is 34 to 37 m, but that is every ramp and the cycleway side by side. A single ramp is two lanes with a concrete median barrier on its left and a curb on its right; no sidewalk (Mapillary frames 1, 3, 4).
3. **Span lengths or pier lines for the printed three spans: Partly.** The raised run is 40.6 to 51.7 m along each way; the split into three spans is open.
4. **What the 2018 rehabilitation changed: Open, needs source.** The 2018 Mapillary frames (2, 3, 5) show the ramp in a work zone.
5. **Ends of the bridge-tagged ways: Partly.** Profiles in `elevation/profiles.csv`.

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
