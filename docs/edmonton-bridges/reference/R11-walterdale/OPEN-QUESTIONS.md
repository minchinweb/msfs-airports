# Open questions, merged 2026-10-14

The "Ask before building" list in another session's review (`CURSOR-HANDOFF.md`, commit c5f3a92, removed 2026-11-23; its "Do not invent" list is kept at the end of this file) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Arch crown height: Partly.** The highest DSM return above the river along the road centreline is 52.8 m (river 614.13 m), consistent with the published 54 to 55 m above the river. Crown above the arch foot and above the roadway are still two separate unreconciled figures.
2. **Rib spacing at crown and feet: Open, needs source.** The aerial cannot give it: the orthophoto is rectified to the ground, so the 40 to 50 m high ribs are displaced sideways by an unknown amount. The rib feet read at about chainage 32 m (south) and 229 m (north) on way 175326660 in plan.
3. **Deck elevation ASL, datum, 13.3 m label: Answered for the deck.** Deck top median 629.05 m; river 614.21 m, so 14.7 m above the river over the whole raised run. The 13.3 m mid-span label is a lower number, which fits a roadway-to-soffit reading with a deck about 1.4 m deep; unconfirmed.
4. **Where the 230 m abutment centrelines sit on the 260.7 m way: Partly answered.** Expansion-joint lines on the aerial fall at about chainage 14 m and 246 m, 232 m apart (plus or minus 3 m), consistent with the 230 m. The raised structure is 248.6 m of the way.
5. **Hangers: Answered. Struts, delta piers: Open.** 16 hangers per plane are counted on the aerial, 10.3 m apart on average (first near chainage 49 m, last near 204 m), matching "16 at 10 m". The first hanger is about 34 m from the south joint (plus or minus 3 m). No struts show in the aerial, but the street frames (R11 frames 3 and 4) show five to seven cross struts between the ribs; delta piers are not counted. See `AERIAL-READINGS.md`.
7. **Longitudinal grade and where 105 Street and Walterdale Hill meet grade: Partly.** Ground profiles along the approach ways are in `elevation/profiles.csv`.

## Do not invent

From the review, unchanged. It was written before the LiDAR, so where it forbids a deck, ground or water elevation, use the measured CGVD2013 values above; still do not take an elevation from a published or mapped figure. Keep conflicting published figures separate and unaveraged, and do not turn a mapped plan length into a structural length.

A single arch rise. The folder records 56 m above the thrust blocks, 43 m and 40 m above the deck or roadway, and 55 m and 54 m above the river. One source also says 54 m measured from the deck. Rib-to-rib spacing at the crown and at the feet. Where the 230 m between abutment centrelines sits on the 260.7 m mapped way. Strut count. Delta-pier count. Longitudinal grade, and where the north and south roads meet grade. The station of the first road hanger. Deck elevation above sea level, the datum, and whether 13.3 m is to the roadway or the soffit. The arch curve cannot be closed from these figures.

Where a photo is missing, check `street/` and `night/` first.
