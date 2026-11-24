# Open questions, merged 2026-10-14

The "Ask before building" list in another session's review (`CURSOR-HANDOFF.md`, commit c5f3a92, removed 2026-11-23; its "Do not invent" list is kept at the end of this file) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Rail-deck elevation ASL, datum, water level: Answered.** Upper (rail) deck top 662.45 m; river 614.91 m; 47.54 m above the river, against the handoff's 47.55 m (156 ft). The plate's July 1906 water is about 0.8 m below the 2018 river.
2. **All 28 span lengths: Partly.** Read from the 1914 plate (printed and scaled, see `NOTES.md`): all river, north and south spans and the six tower bents are now in the notes; the plate sums to 2,558 ft against the documented 2,550 ft. The Soullier Avenue dimension label is unreadable (65 ft scaled, not printed). Measured raised run on the upper deck is 753.7 m of the 777.24 m length (`MEASUREMENTS.md`: the run ends where the deck is within 3 m of ground).
3. **River-pier height: Answered to about 3 ft.** Pier 24/23: about 140 ft (42.5 m) head to footing, about 98 ft (29.8 m) above the July 1906 water, footing 42 ft below it. Matches the 138 ft (1910) and Herzog's "nearly 100 ft"; the "about 125 ft" is not supported. Tower bent heights are in `NOTES.md`.
4. **Approach gradients, lengths, grade points: Partly.** The plate prints grades of 0.74 percent and 5.45 percent for 1914. Present ground profiles along the approach ways are in `elevation/profiles.csv` (25 m steps, DTM and DSM). The 1931 and 1971 rebuilds are not drawn.
5. **Outer steel 11.89 m or 43 ft: Partly.** LiDAR raised width at deck level 11.0 m (plus or minus 1 m), agreeing with the 11.89 m deck; the 43 ft overall width is not tested.
6. **Sim:** the High Level was treated in the sim as a solid ridge, so the terrain under the span needs lowering or cutting (`BLOCKERS.md` section 3).

## Do not invent

From the review, unchanged. It was written before the LiDAR, so where it forbids a deck, ground or water elevation, use the measured CGVD2013 values above; still do not take an elevation from a published or mapped figure. Keep conflicting published figures separate and unaveraged, and do not turn a mapped plan length into a structural length.

Deck elevation above sea level, the datum, or the elevation of the mean-water surface used for the 156 ft figure. A single as-built river-pier height (the folder records about 125 ft, nearly 100 ft, and a 1910 proposal of 138 ft). Present north and south approach gradients, lengths, elevation changes, and where each meets grade. The 1914 and 1910 figures predate the 1931 and 1971 approach rebuilds. Lengths for the 10 spans the designation does not itemize. Do not assign the unitemized remainder. Do not swap the decks. Do not build the old three-track upper deck. Do not build the Dudley B. Menzies Bridge. Pier count also disagrees (32 concrete piers and pedestals, or four river piers plus 62 smaller piers). The designation already gives four river piers and south tower spans on steel legs. Do not choose the other count.

Where a photo is missing, check `street/` and `night/` first.
