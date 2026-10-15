# Edmonton bridges status

Last updated: 2026-10-14. Package: `scenery-edmonton-bridges/` (project `scenery-edmonton-bridges.xml`, definition `PackageDefinitions/cardboardgt-scenery-edmonton-bridges.xml`, version 0.1.0).

## What this is

Version 0.2.0 holds the Tier 1 downtown valley: 15 models and 16 placements (R10, R9, R11, R15, R13, R12, R14, P152, B254, B255, F256, V257, N258, N259, N260). Flat-colour glTF built by `scenery-edmonton-bridges/tools/gen_bridges.py` from the reference data; what is sourced and what is assumed is in `docs/edmonton-bridges/MODEL-NOTES.md`. Compiled, not yet seen in the sim. `PackageOrderHint` is `CUSTOM_WORLD_SCENERY` because these are city objects, not an airport.

## Build

From the repo root: `build.bat bridges` (PowerShell: `cmd /c ".\build.bat bridges"`). Short name `bridges` matches the folder `scenery-edmonton-bridges`. See `CLAUDE.md` for the SDK path override.

Built on 2026-10-14 with the sim closed (the 0.1.0 text follows; 0.2.0 compiled the same way, with a `ModelLib` asset group added). `_PackageInt/_RPTErrors.xml` is empty and `Packages/cardboardgt-scenery-edmonton-bridges/Scenery/cardboardgt/edmonton-bridges/edmonton-bridges.bgl` was written (56 bytes, nothing placed). `fspackagetool` did not write `layout.json`; one was added from the built files so the package folder has an index. Both `Packages/` and `_PackageInt/` are gitignored.

## What to model

Three inventories. `docs/edmonton-bridges/bridges.md` is the North Saskatchewan crossings from Devon to Scotford. `docs/edmonton-bridges/freeway-bridges.md` is the freeway structures on VFR lines among CYXD, CYED, CYEG, CZVL, CFB6, and CEZ3. `docs/edmonton-bridges/lrt.md` is the above-ground LRT stations, viaducts, and extension bridges. The freeway list names the cross road on the QE2, Yellowhead, Henday, Whitemud, and Sherwood Park Freeway decks, and records the Henday, Whitemud, Terwillegar, Groat, and Capilano bridges left off. Highway 16 west of the Henday, Highway 21, and the other crossings added on 14 October are plotted as crosses and still left off the include list. Deck, approach, ramp, and cross-road geometry for every plotted road and river bridge is in `bridge-geometry.json`. Above-ground LRT centreline geometry, including construction and unfunded alignments, is in `lrt-tracks.json`. The build order is `docs/edmonton-bridges/PRIORITY.md`. It ranks every included and excluded bridge, viaduct, and station by how it reads from the air, whether it falls on a VFR approach, and whether it is a named fix on the Edmonton VFR terminal chart or the City Centre helicopter chart. First box is the High Level Bridge and the Dudley B. Menzies Bridge together. Reference briefs for R8–R15, the Groat ravine decks G116, G117, Z125, T133, and G119, P152 and B254, N258, N259, N260, F256, and V257 are in `docs/edmonton-bridges/reference/`. Numbers are unique across every prefix. Bridge codes use 1–136. Stops are P137–P189, at-grade track is K190–K253, and the later codes are listed in `lrt.md` and `bridges.md`. The prompt for the next reference subagent is `docs/edmonton-bridges/reference-prompt.md`. Fill the braces and send one structure at a time. The named checkpoints Bridges, Quesnell, Bremner Cloverleaf, and Sherwood Park Cloverleaf come next. Do not place anything inside the `CYXD Airport Area` polygon; NAIT and Blatchford Gate are inside it.

## Next

1. Open the sim and look: terrain clipping at piers, the datum, the High Level ridge (`MODEL-NOTES.md`, last section). Then fix what shows, by changing the site modules and rerunning `tools/gen_bridges.py`.
2. `build.bat bridges` (clear `gamingservicesui` and `gamelaunchhelper` first if it says NO BUILD), then `python -I scenery-edmonton-bridges/tools/make_layout.py` if `Packages/.../layout.json` is missing.
3. Next boxes in `PRIORITY.md`: section 2 landmarks, starting with the Bridges checkpoint (R20, R21, R22) and Quesnell (R6). The T133, Z125, G116, G117 and G119 ravine decks of the R8 task are not built.
4. Night lighting and transparent glass are not done for any model.
