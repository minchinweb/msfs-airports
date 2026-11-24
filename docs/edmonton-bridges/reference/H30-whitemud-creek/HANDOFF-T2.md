# H30 Whitemud Creek arch: Tier 2 handoff

Modelled 2026-11-23 by `scenery-edmonton-bridges/tools/site_h30.py`. Model `br_h30_whitemud_arch`: about 3,900 polys in one chunk, placed at 53.4286, -113.5630 at a datum of 650.00 m. The package builds (exit 0, `_RPTErrors.xml` empty) after a restart of Gaming Services; the first try said NO BUILD. **Not seen in the sim.**

## What it is

The Henday is **not** on a deck here. The highway runs on a grass embankment about 20 m high, and the creek and a path pass under it through an arch tunnel. The Commons photo (`photos/`) shows this, and the user confirmed it. The sources give a "semi-circular arch spanning 20 metres" on "7 metre high walls", the path "raised within the arch", and "a giant oculus" (CCE; discoverAPEGA).

The 2019 aerial (0.57 m) shows the following. The coordinates are traced as east/north metres in the module:

- **Tunnel**: runs at 352° true under both carriageways, 83 m between the outer faces of the two portals.
- **Portals**: each one is the arch shell cut back by a sloping plane. From above it is a D:
  - 20 m across the outer face;
  - 12.75 m (south) or 13.5 m (north) from the face to the crown of the cut;
  - rimmed in white and open to the sky;
  - transverse beams at path level show through it.
- **Oculus**: a 14 m ring in the median, on the tunnel axis, with the same beams below.
- **Retaining walls**: stepped walls flare out from both portals.
- **Path**: a girder bridge on crosshead piers runs from the northeast into the north portal, curves through the tunnel, and leaves the south portal to the southeast.

## Heights (2018 LiDAR, `elevation/h30-samples.json`, 1 m grid)

- Creek bed: 658.1 to 658.3 m.
- Highway on the fill: 678.3 to 679.7 m.
- Path deck: level at 667.1 to 667.6 m on both approach bridges. This is 9 m above the bed, not the published 7 m. The springing is put at the path level, 667.0 m, so the walls are 8.8 m from the bed.
- Through the oculus: a median of 665.3 m, which is the beams and the path.
- Wall tops at the portal corners: 669 to 671 m, stepping down outward to about 666 m.
- The bare-earth model removes the fill over the tunnel: the DTM has a trench along the creek line.

## In the model

- **Arch shell**: 10 m inner radius, 0.6 m thick, from 667.0 m to a crown of 677.0 m (677.6 m outside), so 1 to 2 m under the road. It is cut to the D at each portal and holed for the oculus.
- **Walls, floor and beams**: side walls from the creek bed to the springing, and a floor at the creek bed. Beams 0.6 x 0.9 m every 3.4 m run wall to wall under the path.
- **Rims and collars**: a white collar on each D's cut edge, rising to the 2018 first-return level beside it. The oculus collar rises from the shell to the median level, with a 3 m grass apron round it.
- **Retaining walls**: stepped walls with tops from the first return.
- **Path**: on the OSM line (ways 493371666, 493371668 and 493371667), 3.4 m wide, with steel railings. It sits on the beams inside the tunnel and on single-column crosshead piers every 11.5 m outside, with an abutment at each end.
- **Terrain**: three flatten polygons at 657.9 m, one over the oculus and one over each D. The sim's ground would otherwise fill the openings. The exclusion polygon comes from the model footprint, as usual.
- **Not modelled**: the highway over the tunnel. It is left to the sim's own terrain and road.

## Assumed (flagged in the module docstring)

- The arch is a true semicircle, and the shell, wall, collar and rim thicknesses are assumed.
- The floor is flat at the creek bed. No creek water is modelled.
- The beam size and spacing are assumed. The beams span the full width.
- The path width and pier spacing are assumed. The pier spacing is read from the photo.

## Sim checks for William

1. **Do the openings show?** Look for the two D's and the oculus from above. If the terrain still covers them, the flatten polygons are not taking. If there is a dark ring round the oculus or the D's, the terrain step is showing past the aprons. Widen the aprons in `site_h30.py`.
2. **Does the sim's terrain carry the fill?** If it does not (the 2018 bare earth has a trench here), the white tube of the shell will show and the road will dip. The fix is to model the road surface over the tunnel. That is not done.
3. **The view from the creek**: the portal hoods, the path bridges and the walls against the embankment.

## Rebuilding

- Regenerate: `python -I scenery-edmonton-bridges/tools/gen_bridges.py h30`. It needs numpy, Pillow and shapely. For example: `uv run --no-project --python 3.13 --with numpy --with pillow --with shapely python -I ...`.
- Resample the LiDAR (needs the gitignored clips, which come from `fetch-site-data.py H30-whitemud-creek`): `python -I -c "import sys; sys.path.insert(0, 'scenery-edmonton-bridges/tools'); import site_h30; site_h30.sample()"`.
