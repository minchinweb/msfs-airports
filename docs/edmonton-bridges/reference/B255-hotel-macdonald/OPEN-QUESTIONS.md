# Open questions, merged 2026-10-14

The "Ask before building" list in another session's review (`CURSOR-HANDOFF.md`, commit c5f3a92, removed 2026-11-23; its "Do not invent" list is kept at the end of this file) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Grade to ridge and grade to the tallest turret: Partly answered.** The tallest point is 714.95 m, 48.1 m above the edge ground (666.83 m), at 53.540318, -113.489602, which agrees with the published 47.7 m (156 ft), so that figure is to the tallest point. A second peak reads 45.3 m (53.540053, -113.489756) and a cluster of at least four more reads 41.7 to 43.8 m. Across the footprint 66 percent is higher than 30 m, 35 percent higher than 35 m and 11 percent higher than 40 m, so the main steep roof ridge is about 35 to 38 m above grade (plus or minus 2 m) and the turrets and towers 42 to 48 m. The ridge is read from the area distribution, not from a surveyed line.
2. **Grade at 100 Street, ridge elevation, datum: Answered.** Ground at the building edge 666.83 m (665.0 to 667.31 m), CGVD2013. This replaces the earlier note in `BLOCKERS.md` that put the ground at 614 to 640 m.
3. **Whether the Bing ring is the footprint to build: Open, measurable** (compare the DSM roof edge with the ring); not done. The ring area is 2,426 m2.
4. **Turret count and roof masses: Open, needs source.** The 1 m DSM gives the peak heights above but cannot separate turrets from chimneys and dormers; the designation does not give a count.
5. **Copper colour as a specification: Open, needs source.** The night photo shows a floodlit warm facade only.

## Do not invent

From the review, unchanged. It was written before the LiDAR, so where it forbids a deck, ground or water elevation, use the measured CGVD2013 values above; still do not take an elevation from a published or mapped figure. Keep conflicting published figures separate and unaveraged, and do not turn a mapped plan length into a structural length.

A height from grade to the ridge, and a height from grade to the top of the tallest turret. Wikipedia's 47.7 m (156 ft) does not say which point it reaches. Emporis states 155.51 ft architectural and 167.49 ft tip, and does not say ridge or turret. The OpenStreetMap `height=47` tag was not used. A published plan length and width. A surveyed outline. A turret count. The present colour of the copper. The survey compilation says the roof was blackened with age. The 8 October 2011 frame shows green. Those were not averaged. Elevation of the ridge, of the grade at 100 Street, and the datum.

Where a photo is missing, check `street/` and `night/` first.
