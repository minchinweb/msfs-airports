# H28 / CEQ4 Whetstone International: status

Project: `airport-h28/airport-H28-del-bonita-whetstone-intl.xml` (package `cardboardgt-airport-h28-whetstone`, v0.0.1). Spec and decisions: `SPEC.md`. Build: `.\build.bat h28` (sim closed; see CLAUDE.md build notes).

## Built (2026-10-27, builds OK, not yet seen in the sim)
- `Airport` H28, name "Whetstone Intl (CEQ4)", marker moved to the runway midpoint (48.99868, -112.77713), magvar 12.5, test radius 2,000 m.
- One runway numbered 07 (the sim would call it 08/26), true heading 89.97, 1,353 m x 20 m, centred on the sim default runway's midpoint (so 120 m trimmed from each end of the default 1,594 m). Surface `{322DE917-E25D-4AD8-BFBB-4D5F4D259413}`, which the user found in the Project Editor and thinks is striped grass.
- Starts about 30 m in from each end; 122.8 CTAF.
- Four small GA tie-downs, two north and two south of the runway about 100 m from the west end, with grass taxi paths (`drawSurface` false) and a windsock on the north side.

## Not done yet
- Check in the sim: that the runway reads 07/25 and matches the aerial strip, and that the grass surface looks right (plain vs striped).
- Runway position and length were not measured against imagery (the spec's to-do); the border straddle is only as good as the sim default (centreline 48.99868, about 12 m north of the OSM boundary).
- Vegetation-exclusion polygon (only the runway's `excludeVegetationAround` is set), threshold double cones, edge cones, fences, mowed polygon.
- PAPI on 07, threshold reflectors; the port of entry buildings and lights; the power line; RNAV 25 and RNAV-A.
- A world-map search for "CEQ4".
