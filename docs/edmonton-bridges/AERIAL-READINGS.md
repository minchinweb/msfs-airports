# Pier, span and hanger stations read from the aerial

Written 2026-10-14. Method: `aerial-strip.py` straightens the 2019 City orthophoto along a mapped way and draws chainage ticks (7.5 px per metre at zoom 1.5), so pier tabs, cutwaters and joints can be read to about plus or minus 1 to 1.5 m. Chainage is metres along the OSM way from its first node. The aerial is rectified to the ground, so tall features (arch ribs, truss tops) are displaced sideways and are not measured; stations along the line are reliable.

| Site | Way | Reading | Piers or stations (chainage m) | Compared with |
| --- | --- | --- | --- | --- |
| R8 Groat | 22916458 | Pier cap tabs on the east edge | 32.7, 78.0, 122.4, 167.3, 212.4, 257.3; spacing 44.9 m; abutments inferred near -12 and 302 | Seven spans of 44.9 m = 314 m, matches the published 315 and 315.5 m; the mapped way (291.5 m) is about 12 m short at each end |
| R13 Low Level | 31882107 | Cutwater noses on the west edge | 52.4, 105.3, 158.4; truss ends near 0 and 212 | Four equal spans of 53 m (the 2008 paper), not 51.8 m; three piers under the 1900 span |
| R15 Dawson | 22916476 | Cutwaters on the south edge | 44.5, 87.9, 131.1, 207.0; abutments near 1 and 237.6 | Spans 43.3, 43.4, 43.2, 75.9, 30.5 m: matches the published 43.3 x 3, 76.2, 30.5 |
| R11 Walterdale | 175326660 | Hanger posts and deck joints | 16 hangers per plane, first near 49, last near 204 (10.3 m mean); joints near 14 and 246; arch feet near 32 and 229 | 16 hangers at 10 m confirmed; joints 232 m apart against the 230 m abutment centrelines |

**Not readable from the aerial:** R12 (a girder deck, piers hidden), R9 (curved box deck, the strip method assumes a straight line), the tall truss and arch geometry (truss depth, rib spacing, crown), and shaft heights. Those need drawings or photos.

The R8 reading works because the 2019 aerial caught the deck half rebuilt; other bridges with a solid deck do not show piers.
