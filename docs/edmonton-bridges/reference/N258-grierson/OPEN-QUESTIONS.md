# Open questions, merged 2026-10-14

The "Ask before building" list in another session's review (`CURSOR-HANDOFF.md`, commit c5f3a92, removed 2026-11-23; its "Do not invent" list is kept at the end of this file) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Deck elevation ASL and datum: Answered.** Deck top 630.92 m; ground under it 624.5 to 627.5 m.
2. **Clearance under the deck: Answered.** The deck top is 6.1 m (median) above the road below. Less a deck depth of 1 to 2 m this leaves roughly 4 to 5 m of clearance, consistent with the McDougall Hill `maxheight` tags (5.0 and 5.2 m).
3. **Structure length: Partly.** The raised run is 36.1 m of the 59.0 m mapped centreline.
4. **Deck width: Answered.** Raised width 11.5 m (plus or minus 1 m), two lanes with curbs and rails.
5. **Span count, pier count, abutment form: Partly.** A large concrete column with a steel guardrail wrapped around its base shows in Mapillary frame 5, so there are pier columns; the count is open.
6. **Vertical profile and grade points: Partly.** Profiles in `elevation/profiles.csv`.
7. **A view of this deck over McDougall Hill Road: Partly.** Mapillary frames 2 to 4 show the elevated deck and its flat soffit from the valley.

## Do not invent

From the review, unchanged. It was written before the LiDAR, so where it forbids a deck, ground or water elevation, use the measured CGVD2013 values above; still do not take an elevation from a published or mapped figure. Keep conflicting published figures separate and unaveraged, and do not turn a mapped plan length into a structural length.

Span count. A published structure length. Pier count, pier height, and abutment form. Clearance under the deck. The tags `maxheight=5.2` and `5.0` are on McDougall Hill Road. They are not this clearance and not a deck elevation. Deck elevation, soffit elevation, and the datum. Width and lane width. Longitudinal grade, and the grade point at either end. A model that joins the two roads at one level is the wrong interchange.

Where a photo is missing, check `street/` and `night/` first.
