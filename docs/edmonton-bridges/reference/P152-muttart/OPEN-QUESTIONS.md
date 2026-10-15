# Open questions, merged 2026-10-14

The "Ask before building" list in `CURSOR-HANDOFF.md` (another session's review, commit c5f3a92) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

1. **Platform elevation ASL and datum: Partly.** 2018 ground at the platform sites is 622.05 to 622.44 m (the LiDAR predates the stop, so this is the ground it was built on); platform DSM medians 621.9 m (west) and 622.7 m (east) are ground, not platform. Take about 622 m as the platform level, at grade. Unverified against the as-built.
2. **Canopy roof plan: Open, needs source.** The 2019 aerial predates the stop.
3. **2013 storage track on the north-west side: Open, needs source.**
4. **Join with the ramp: Partly.** The R14 ramp ways end at the platform edge: 53.536207, -113.480002 and 53.536104, -113.4801. William's decision stands (R14 owns the ramp).
5. **Sim:** the heading check (49 degrees true, within 2 degrees).

The review's "Do not invent" list still applies: keep the conflicting published figures separate and unaveraged, as the review set out, and do not turn a mapped plan length into a structural length. Where its "Photos" section says none are saved, check `street/` and `night/` first.
