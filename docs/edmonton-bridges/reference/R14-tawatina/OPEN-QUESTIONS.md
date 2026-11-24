# Open questions, merged 2026-10-14

The "Ask before building" list in another session's review (`CURSOR-HANDOFF.md`, commit c5f3a92, removed 2026-11-23; its "Do not invent" list is kept at the end of this file) re-checked against the data added since: LiDAR heights and measurements (`elevation/README.md`, `elevation/MEASUREMENTS.md`, `../../MEASUREMENTS.md`), the 2019 aerial, Mapillary street frames (`street/`, read in `../../STREET-READINGS.md` for ten sites) and the river gauge (`../../RIVER-LEVEL.md`). Status words: **Answered** (a value is now held), **Partly** (a value or bound is held, a gap remains), **Open, measurable** (can be done from files we hold, not done yet), **Open, needs source** (a document, photo or survey is needed), **Sim** (only William can test it).

Elevations are CGVD2013 metres from the 2018 LiDAR. Deck tops are first returns (rails, traffic and catenary can add up to 1 m) and the sim's datum is not yet checked. "Rise" is deck top above the ground or water under it, not the clear height: take off the deck depth (1 to 2.5 m).

The 2018 LiDAR and the 2019 aerial **predate the bridge**. The 2019 aerial shows the Valley Line trench and ramp as bare earthworks south of 98 Avenue, and the 2018 DSM at mid-bridge reads ground, not a deck. The 2024 mosaic returns the same values there. **The R14 deck row in `ELEVATION.md` (628.19 m, 14.93 m above the river) is not a deck and should not be used.** The river surface at the site, 613.26 m, is valid.

1. **Pylon height: Open, needs source.** Not in the data. 24 to 30 m above the deck remains the figure.
2. **LRT and pedestrian deck elevations: Open, needs source.** Only the folder's 615.60 m and EL 615.9 (datum unnamed) stand. Ground at the south end of the bridge is about 619 to 622 m in 2018.
3. **Pier count and span lengths south of the 50 m side span: Open, needs source.**
4. **South ramp gradient and where it meets grade: Partly.** William decided the bridge (R14) owns the ramp and runs it to the edge of the station (P152). The ramp ways are 1280982479 (196 m, ends at 53.536207, -113.480002) and 1280982480 (210 m, starts at 53.536104, -113.4801); those two nodes are the join with P152's platforms. 2018 ground along them rises from about 619.1 m at the bridge end to about 622.0 m at the platform; that ground is pre-construction, so the finished grade is not read. The 2013 labels (minus 5.600 percent and minus 0.275 percent) remain the only graded figures. The 2019 aerial shows the ramp as a cut running south-west from the portal beside 98 Avenue.

## Do not invent

From the review, unchanged. It was written before the LiDAR, so where it forbids a deck, ground or water elevation, use the measured CGVD2013 values above; still do not take an elevation from a published or mapped figure. Keep conflicting published figures separate and unaveraged, and do not turn a mapped plan length into a structural length.

Surveyed pylon height. The requirement is 24 m to 30 m from the top of deck, and the contractor says 30 m pylons. The 30 m figure does not restate the datum. LRT deck elevation and pedestrian deck elevation, in any datum. As-built clearance over the river. As-built length, span lengths, and pier count of the south guideway. The mapped runs south of the river piece are 210.6 m and 212.7 m. Those are bridge-tag lengths, not pier spacing. The 2013 drawing's three 40 m spans are marked approximate. As-built gap between the girder soffit and the pedestrian deck. As-built south ramp length, gradient, and elevation change, and the surveyed point where the ramp meets grade. The 199.1 m and 213.1 m clips reach the mapped stop and are not that point.

Where a photo is missing, check `street/` and `night/` first.
5. **Street frames:** a finished-stop frame (`1965015420835933`) shows the track at grade beside the road with a sloped retaining wall and tall catenary poles; two older frames show the dark steel pedestrian truss on concrete V-shaped pier heads at the south end. See `STREET-READINGS.md`.
