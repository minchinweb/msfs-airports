# Y79 Bremner Cloverleaf: Tier 2 handoff

Built 2026-10-15: `scenery-edmonton-bridges/tools/site_y79.py` (helpers in `t2lib.py`: `girder_deck` gained a `girder_sw` colour argument, default unchanged), model `br_y79_bremner` (about 7,300 polys, one chunk), placed at 53.5702, -113.2461 with datum altitude 670.00 m. Built with `build.bat bridges` (exit 0, `_RPTErrors.xml` empty). **Not seen in the sim.**

## Review: was there enough?

Yes for a landmark-grade interchange, with a smaller kit of facts than the river sites:

- The 2019 City orthophoto in `aerial/` is **entirely black** (the interchange is in Strathcona County, outside the City imagery). `tools/overlay.py` is therefore useless here. The plan check was done against the 2018 LiDAR first-return image instead (rendered in the local frame, model asphalt outlined): loops, outer ramps, both Highway 21 carriageways and both decks sit on the bright road bands.
- `geometry.json` held only the decks, approaches and the two loops. The other ramps were listed in NOTES.md as "still missing". They are now in `geometry.json` under `ramps_added_2026_10_15` (Overpass read, ODbL).
- No deck-depth or abutment data, no usable photograph of the underside. Girder depth was derived instead (below).

## What is in the model

- Two overpasses, built like the R20 to R22 decks (`girder_deck`): N-1 east/northbound (concrete girders, 5 lines, grey) and S-6 west/southbound (rust-coloured weathering steel, 6 lines), slab with asphalt, lane lines, concrete median parapet with blue rail, blue outer railing, lamps, abutments, round-column piers with cap beams.
- Highway 21 approaches 300 m each side of both decks as raised road on 4:1 grass slopes, narrowing from the deck width to 12 m over 60 m and sinking into the terrain at the far end (120 m fade).
- Both loops (NE 32834983, SE 32835223), the four outer ramps (32834795, 153737435, 153737436 with 1264725793 and 91930051, 1259559957 and 1259559962, 32830192) and the short stubs: 8.6 m roadway, yellow left edge line, white right edge line, grass slopes. Where a ramp is lower than 0.8 m above its side ground the road sinks into the terrain (nothing is drawn at grade, where the sim already draws Highway 16 and the ramp). The ramps are LiDAR-limited: parts of 32830192 and 153737436 are outside the clip and end with a 40 m fade.
- Not modelled: Highway 16 itself (two carriageways at about 670 m under the decks; the sim draws it), guardrail, signs, sign gantries (ZE, ZS, ZN, ZW), service roads.

## Sourced

- Plan: OSM ways listed in the `site_y79.py` docstring.
- Heights: 2018 LiDAR. Ramps and approaches are on embankment (loops up to 7 m, ground about 670.5 m), so the road surface is the bare-earth crown (max DTM within 3 m of the centreline), sampled to `elevation/y79-samples.json` by `python -I` (see below). Deck levels: first-return median along each deck (east 677.27 m, west 677.70 m) less 0.12 m; the approaches are pinned to the deck at each abutment (correction faded over 90 m), so deck ends and approach road are flush (max joint step 0 by construction).
- N-1: 3 spans 29, 16.2, 29 m; 15 girders (read here as 5 lines x 3 spans, which fits 14.3 m of deck); clear roadway 14.2 m; eight columns, two piers; chip seal 50 mm. S-6: 2 spans 38.65 m; weathering steel; clear roadway 16.6 m; one pier on five bearing piles; ACP 90 mm. Both in `NOTES.md`.
- Girder + slab depth: the published 5.3 m posted clearance (5.5 m required on S-6) over Highway 16 at 670.0 to 670.3 m puts the soffit at about 675.6 m, so deck top 677.15 m gives about 1.57 m (N-1: 1.30 m girder, 0.27 m slab) and about 2.15 m (S-6: 1.85 m + 0.30 m).

## Assumed (flagged)

- Abutment and pier stations along the OSM line: N-1 abutments 0.65 m and 74.85 m (the 74.2 m total centred on the Highway 16 median centre), piers at 29.65 m and 45.85 m; S-6 abutments 11.35 m and 88.65 m, pier at 50 m. The OSM decks are 86.2 m and 91.0 m, so the structures are shorter than the mapped lines.
- S-6 girder line count (6), column sizes (0.9 m and 1.0 m diameter, 4 and 5 columns), cap beams, lamp positions, ramp roadway width 8.6 m (lane plus shoulders; Mapillary frames show a wide paved shoulder), approach width 12 m, 4:1 slopes, the grass colour.
- Edge-line colours follow the street frames (yellow left, white right).
- The 2009 plan for a "modified four-leaf clover" is not modelled (the interchange as it stands, with the two loops).

## Seams

- Deck ends to approach road: same height at the abutment by construction, same asphalt colour, approach width equals the deck clear roadway at the abutment.
- Ramp starts and ends at the mainline nodes: the ramp and mainline heights agree to within 0.1 m at every shared node (checked numerically; both use the same LiDAR crown and the same 0.1 m lowering). Colours are asphalt over asphalt and grass over grass, so any overlap is invisible.
- Slopes end with a 12 m taper at the abutments so no floating end wall sticks out. One chunk, so no chunk seams.

## Remains

- Sim check of the slopes: they are drawn at the 2018 LiDAR levels and coincide with the sim terrain where the sim already has the embankments.
- Overpass drawings (Alberta file 75760) would replace the assumed abutment and pier stations.
- Tier 1 style textures, night lighting: none.

## Rebuilding

The LiDAR clips are gitignored. The samples are committed (`elevation/y79-samples.json`). To regenerate them from the clips: `python -I -c "import sys; sys.path.insert(0, 'scenery-edmonton-bridges/tools'); import site_y79; site_y79.sample()"`.

## Sim-side checks for William

- Highway 21 deck ends at about 677.0 to 677.6 m ASL; the sim road should meet the approach fill at the same height.
- Whether the green slopes show through or z-fight with the sim terrain along the loops (they are lowered 0.1 m and sink below 0.8 m height, so should be hidden at grade).
- Whether the sim draws a deck or an overpass of its own here; if so, it will double up with this model.
- Highway 16 must still pass under the decks at about 670 m (nothing here blocks it).
