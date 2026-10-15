# Edmonton bridges status

Last updated: 2026-10-14. Package: `scenery-edmonton-bridges/` (project `scenery-edmonton-bridges.xml`, definition `PackageDefinitions/cardboardgt-scenery-edmonton-bridges.xml`, version 0.1.0).

## What this is

Scaffolding only. The scenery XML (`PackageSources/Scenery/edmonton-bridges/edmonton-bridges.xml`) is an empty `FSData` document, so the package builds and loads with nothing placed. `PackageOrderHint` is `CUSTOM_WORLD_SCENERY` because these are city objects, not an airport.

## Build

From the repo root: `build.bat bridges` (PowerShell: `cmd /c ".\build.bat bridges"`). Short name `bridges` matches the folder `scenery-edmonton-bridges`. See `CLAUDE.md` for the SDK path override.

Compiled once on 2026-10-14 with the sim closed. `_PackageInt/_RPTErrors.xml` is empty and `Packages/cardboardgt-scenery-edmonton-bridges/Scenery/cardboardgt/edmonton-bridges/edmonton-bridges.bgl` was written (56 bytes, nothing placed). `fspackagetool` did not write `layout.json`; one was added from the built files so the package folder has an index. Both `Packages/` and `_PackageInt/` are gitignored.

## What to model

Three inventories. `docs/edmonton-bridges/bridges.md` is the North Saskatchewan crossings from Devon to Scotford. `docs/edmonton-bridges/freeway-bridges.md` is the freeway structures on VFR lines among CYXD, CYED, CYEG, CZVL, CFB6, and CEZ3. `docs/edmonton-bridges/lrt.md` is the above-ground LRT stations, viaducts, and extension bridges. The freeway list names the cross road on the QE2, Yellowhead, Henday, Whitemud, and Sherwood Park Freeway decks, and records the Henday, Whitemud, Terwillegar, Groat, and Capilano bridges left off. Highway 16 west of the Henday, Highway 21, and the other crossings added on 14 October are plotted as crosses and still left off the include list. Deck, approach, ramp, and cross-road geometry for every plotted road and river bridge is in `bridge-geometry.json`. Above-ground LRT centreline geometry, including construction and unfunded alignments, is in `lrt-tracks.json`. The build order is `docs/edmonton-bridges/PRIORITY.md`. It ranks every included and excluded bridge, viaduct, and station by how it reads from the air, whether it falls on a VFR approach, and whether it is a named fix on the Edmonton VFR terminal chart or the City Centre helicopter chart. First box is the High Level Bridge and the Dudley B. Menzies Bridge together. Reference briefs for R8–R15, the Groat ravine decks G116, G117, Z125, T133, and G119, P152 and B254, N258, N259, N260, F256, and V257 are in `docs/edmonton-bridges/reference/`. Numbers are unique across every prefix. Bridge codes use 1–136. Stops are P137–P189, at-grade track is K190–K253, and the later codes are listed in `lrt.md` and `bridges.md`. The prompt for the next reference subagent is `docs/edmonton-bridges/reference-prompt.md`. Fill the braces and send one structure at a time. The named checkpoints Bridges, Quesnell, Bremner Cloverleaf, and Sherwood Park Cloverleaf come next. Do not place anything inside the `CYXD Airport Area` polygon; NAIT and Blatchford Gate are inside it.

## Next

1. Work `PRIORITY.md` from the top. Add bridge models under `PackageSources/modelLib/<model>/` (`<model>.xml` + glTF), then add a `ModelLib` asset group to the package definition. Output dir used by the other packages is `Scenery\cardboardgt\<short>\`.
2. Place them as `SceneryObject` / `LibraryObject` entries in `edmonton-bridges.xml`.
3. Bump the package version and add a release note when the first bridge is in the sim.
