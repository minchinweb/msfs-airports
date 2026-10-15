# V257 Edmonton River Queen: model handoff

| | |
| --- | --- |
| Reviewed by | Claude (model `claude-sonnet-5-5`), run as a general-purpose subagent for Claude Code. Dispatched by the main Claude Code session, which was working for William. |
| Review date | 2026-10-14 |
| Git commit | `bc90f82` (`bc90f82c495ab25c366da2749f43f4a003371849`, branch `agents/claude/1`). The reviewed notes, sources, geometry and photos are in that commit. This handoff file was written after it and is uncommitted. |

<!-- data-update:begin -->
## Update 2026-10-14: elevation, aerial and night data now in this folder

- **Ground at the centre point** (2018 LiDAR bare earth, CGVD2013): 613.6 m (2,013 ft). Clips in `elevation/` (`dtm-2018-1m.tif`, `dsm-2018-1m.tif`); every deck's figures are in `elevation/README.md`.
- **River surface here** (2018 LiDAR): 613.66 m. Gauge conversion and the seasonal range (about ±0.5 m) are in `../../RIVER-LEVEL.md`.
- **Main deck height** (`pier`, DSM median): 614.40 m, 0.74 m above the river. It is the first return, so it includes rails, catenary and traffic and cannot see a deck under another deck. Not a design figure.
- **Aerial:** `aerial/ortho-2019.jpg` (City 2019 orthophoto, 0.2 m, north up; bounds in `aerial/ortho-2019.json`). Gitignored, regenerate with `fetch-site-data.py`. Widths, pier positions and outlines can be measured from it; that has not been done.
- **Night lighting:** no usable night photo found (see `../../DATA-SOURCES.md`).
- **Street-level photos:** 5 daytime Mapillary frames in `street/` (CC BY-SA, credits in `street/SOURCES.md`). They show railings, barriers, lamp posts, lane and sidewalk layout and approach shape from the road; not the underside or truss depth. Check them before treating those items below as open.

Blocking items below that ask for deck or ground elevation, datum, water level or terrain heights are answered by these files; the datum is CGVD2013 and still needs a check against the sim. Items asking for widths, pier or abutment positions or an overhead view can be measured from the aerial but are not yet. Everything else below still stands. All blockers across the 21 sites are ranked in `../../BLOCKERS.md`.
<!-- data-update:end -->

## Verdict

**Ready with assumptions.**

The folder gives a firm plan footprint, heading, hull length/beam, colours and layout. It gives no heights, no water elevation, and no dock or gangway size. At 1,000 to 3,500 ft AGL a 52 m x 12 m boat is a few pixels to a few dozen pixels long. Heights can come from photo proportions, flagged as estimates. Close fly-bys would show the guesswork.

## What the folder gives me

Source tags: N = NOTES.md, S = SOURCES.md, G = geometry.json, photo file names as given.

**Identity and state**
- Steel passenger paddlewheeler, official no. 817706, IMO 8888886. A vessel, not a bridge. (N, S, G)
- Model state: docked on the south bank, between the Low Level and the Tawatinâ. Not underway. (N)
- Two decks. Enclosed lower deck, open upper deck under a blue canopy, wheelhouse at the forward end of the upper deck. (N, elevation.jpg, mooring-2018.jpg)
- Two stern paddlewheels side by side, red. 16 ft diameter (Journal figure). (N, S, stern-wheels.jpg)

**Hull size (published, in conflict)**
- Length: 51.78 m (Transport Canada), 51.79 m (FAQ 2018), 169.91 ft = 51.79 m (auction), 51 m (Journal), 52 m (Wikipedia, CBC). (N, G)
- Beam: 12.00 m (TC), 12.01 m (FAQ), 39.4 ft = 12.01 m (auction). (N, G)
- Draft: 0.73 m (FAQ), 2.4 ft = 0.73 m (auction). TC depth 2.10 m is not a draft. (N, G)

**Position and heading (OSM, mapped, not surveyed)**
- Pier centre: 53.5395342, -113.4818826. Way 67563569. Five corners. Long edges 12.5 and 12.8 m, short edges 2.2, 1.1, 1.0 m. (G)
- Vessel outline: way 1373511013, 14 corners, centroid 53.5396064, -113.4819983. Perimeter 119.4 m. Longest corner span 53.5 m. (G)
- Long axis: SW end 53.5395330, -113.4823342 to NE end 53.5397415, -113.4816061. Bearing SW to NE is 64.3 deg. (N, G)
- Bow is at the SW end, toward the Low Level (west). Stern, wheels and gangway are at the NE (east) end. (N, mooring-2018.jpg, south-bank.jpg, stern-wheels.jpg)
- Distances: pier to Low Level centre 379.2 m, to Tawatinâ centre 316.1 m. (N, G)

**Colours (photos only, no text source)**
- White house. Blue hull. Red stripe along the deck line. Blue canopy. Red wheels with grey steel rims. (N, elevation.jpg, stern-wheels.jpg)

**Other**
- Four flags on poles above the trees on the bank, near the stern. (S FAQ, elevation.jpg)
- Draw the boat as it was in 2008 to 2018. No source describes a changed outline after the 2020 to 2022 repair. (N, S)

## Build spec I would use from this alone

Items marked **[photo est.]** are my ratios from elevation.jpg and mooring-2018.jpg. They are not in the folder as numbers. Treat them as +/- 20 percent.

**Placement**
- Origin: the mapped vessel centroid 53.5396064, -113.4819983 (G). The pier centre is about 11 m SE of it. Check that offset by my own arithmetic before use.
- Model long axis at 64.3 deg true. Bow at the SW end. Bow heading is 244.3 deg true.
- The boat lies parallel to the south bank. Starboard (south) side faces the bank. The bank is on the far side in all five photos. Port (north) side faces the river.
- Water elevation: not in the folder. Must come from the sim or the bridge scenery.
- Length: use 51.8 m. Beam: 12.0 m. The OSM span of 53.5 m is about 1.7 m longer. I assume that is the stern platform and gangway foot. Do not stretch the hull to it.

**Components**
1. Hull. Steel, flush. Flat bottom, very shallow draft 0.73 m. Raked bow with a small railed foredeck. Blue below the red stripe.
2. Stern platform. The hull is full width at the stern and extends aft of the house. The wheels sit on it. Blue diagonal knee braces show under it. About 9 m of length **[photo est.]**.
3. Main (lower) deck house. White. Continuous band of windows along the side: about 2 aft of a hull door, then 8 forward. Door mid-ship **[photo: elevation.jpg]**. Stern face has 2 large windows per wheel bay and an EQ logo.
4. Upper deck. Railed, open forward. Blue canopy roof over the aft ~60 to 65 percent **[photo est.]**. Chairs and bar visible. Orange mesh fence on the forward open deck in 2008 only.
5. Wheelhouse. White box at the forward end of the upper deck. Small radar and antennas on top. A few metres back from the bow **[photo est.]**.
6. Paddlewheels x2. Each 4.9 m diameter (16 ft). Red paddle slats, grey steel rim and spokes. Side by side, mounted at the stern, mostly above the waterline with the lower arc in the water. Static in the model. Optional rotation: 18 rpm.
7. Small white vent or funnel box above the canopy at the aft end (visible in stern-wheels.jpg only). Treat as a detail.
8. Gangway. Blue covered steel truss ramp at the stern, running up the bank. Shown raised in stern-wheels.jpg and as a canopy-roofed ramp in elevation.jpg and mooring-2018.jpg. Length not given. Draw it as a ramp from the stern deck to the bank.
9. Pier and pilings. Small. A 12.5 x 2.2 m pier outline per OSM. Two or three white posts beside the stern wheel (paddlewheel.jpg).
10. Flag poles x4 on the bank.

**Heights [photo est.]**, from elevation.jpg with the registered 51.8 m length as the scale (about 28 px per metre):
- Hull blue band above water: about 1.5 to 2 m.
- Main deck to upper deck floor: about 3.5 m.
- Canopy underside to main deck: about 6.5 m.
- Canopy top above water: about 8 to 9 m.
- Wheelhouse roof above water: about 9 to 10 m. Antennas about 1 m more.
These are perspective-skewed. Do not use them for anything but a plausible silhouette.

**Materials and colours (sRGB guess from the photos)**
- Hull blue: navy in 2008 and 2018, lighter teal in 2012. Use one mid-dark blue, about #1F4E8C.
- House white, slightly off-white, #E8EAEA.
- Red stripe and paddles, #B22A2A.
- Canopy blue, #1B3F9C.
- Grey rails and wheel rims, #8A8F94.
- Window glass dark grey-blue.

**LOD**
- LOD0 (1,000 to 3,500 ft): one hull block, white house block, blue canopy slab, wheelhouse box, two red wheel discs. Under 300 triangles. No window geometry, use a texture.
- LOD1 (close): add railings as alpha cards, window insets, ramp truss, wheel spokes as cards, flags.
- Ship to MSFS as a static scenery object. The sim does not float it.

**Water and collision**
- Sit the hull bottom 0.73 m below the water plane. Hide the lower hull under the water surface.
- No collision needed for the hull at this scale. The bank is terrain.

## Gaps and conflicts

Ranked by damage to the model.

1. **No water elevation or bank elevation.** Without it the boat floats or sinks. No elevations are in G. (G: "No elevations are stored.")
2. **No heights at all.** Freeboard, deck heights, canopy, wheelhouse, air draft are null (G, N). Mine are photo ratios.
3. **OSM outline is not a clean hull.** 14 corners, perimeter 119.4 m, edges from 2.7 to 33.8 m. Only the long axis is trusted. I cannot tell which corners are stern platform, gangway or bow. Footprint width is not recoverable from it with confidence.
4. **Length conflicts.** 51 m, 51.78 m, 51.79 m, 52 m, and the OSM span 53.5 m. Beam 12.00 or 12.01 m, no real conflict. I use 51.8 m x 12.0 m.
5. **Photos show a vent or funnel above the canopy at the aft end (stern-wheels.jpg, around the aft centre). N says no tall stack appears.** Both can be true if it is short. Check this before leaving it out.
6. **Gangway is unsized and its position is ambiguous.** The raised ramp (2008, 2012, 2018) versus the FAQ "incline up and then down". N says which ramp is the gangway is missing. In 2012 the ramp is raised, so the stern is also a bank-side ramp. Ramp may not match the 2026 state.
7. **Bow position is unsurveyed.** Orientation depends on photos and OSM agreeing. They do (all five photos put the bow west). Still not a survey.
8. **Piling material.** Wood or concrete. Visible posts are white in paddlewheel.jpg. Colour only.
9. **Draft 0.73 m vs auction 2.4 ft at a full load.** Same value, but it is not stated which load.
10. **Tonnage 611 vs 750.49 GT, speed 9 vs 10 kt, capacity 250/300/399/400.** None affects geometry.
11. **No photo shows the bow end head-on, or the port side from the bridge deck or from the air.** No aerial or high-angle view is in the folder. Roof layout (canopy plan, wheelhouse roof, vents) is unknown from above. This is the view the sim uses.
12. **All photos pre-date the 2020 puncture.** The 2026 wheelchair lift is not in any photo.
13. **No night, lighting or text-source paint colour.** Colours are photo-read only.

## Handoff requests

**Blocking**
1. Water-surface elevation at the pier and bank-top elevation at the gangway foot, in the same datum the sim terrain uses. Ask the researcher for the river level used by the neighbouring bridge models. Why: placement vertical.
2. Top-down or high-oblique imagery of the boat (satellite tile, drone image, or a Commons photo from the Low Level or Tawatinâ). Needed: canopy plan, wheelhouse roof, deck layout, hull plan width, gangway line. Why: the sim sees the roof.
3. One published or measurable height: freeboard, canopy height, or wheelhouse top above the water. A scaled photo with a known object (door height, railing height) is acceptable. Why: replaces my photo ratios.
4. Confirm that the OSM vessel polygon is the right placement envelope. Ask which corners are the stern platform and which is the bow. Compare with a satellite image. Why: footprint and rotation.

**Nice to have**
5. Bow-on and stern-on photos. Bow is missing entirely. Stern-on exists only in 2012.
6. Gangway length, width, and which ramp is current as of 2026. Why: close-up detail.
7. Pier and piling plan size, count, material. Why: small detail near the hull.
8. How a static boat should sit on sim water. Does the sim water plane sit at the river elevation, or does it need a flatten/water polygon? Why: avoids a boat hovering or buried.
9. Night lighting: are there navigation lights, deck lights, or a lit sign at night? Why: emissive materials. No source in the folder.
10. Collision: confirm none is wanted for the hull or ramp.
11. A text source for paint colours, and the wheel diameter read from a photo with a known scale. Why: colour sanity and wheel size check (16 ft is the Journal's figure only).
12. Whether the boat should be omitted in winter or when it sails. Folder says winter events are dockside, so a permanent docked model is fine.
