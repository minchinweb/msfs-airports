"""CYXD hangars on the east line (3-8, 11), Hangar 14 (museum), Hangar 18 (Flying Club), Hangar 20 (Esso) and the west-side hangars 38 / 39 / 40.

Imported by gen_buildings.py (main() calls place()).  Footprints, centres and headings come from the OSM outlines as they were
mapped in 2016 (Overpass `date:` query) cross-checked against Esri World Imagery Wayback 2014-02 tiles; see
docs/cyxd/hangar-footprints.md.  Hangar 9 has no footprint and no photo (the old "Hangar 9" photos are Hangar 8).

Model frame (same as the tower / Hangar 15 models): origin on the ground at the footprint centre, +Z = front = object heading,
+X = bearing heading + 90 (to the right looking along +Z; to the LEFT when you stand in front and face the building).  Models are
mirrored once at the end (Mesh.mirror_x) because the sim places model +X to the west.
"""
import math
from gen_buildings import *  # noqa: F401,F403  (Mesh, number_disc, palette constants, MODELLIB helpers)


# helpers ------------------------------------------------------------------------------------
def rows_z(m, sgn, zplane, x0, x1, y, n, w, h):
    """n windows between x0..x1 on a wall whose outward normal is (0, 0, sgn), wall plane z = zplane."""
    gap = (x1 - x0 - n * w) / (n + 1)
    for i in range(n):
        m.window((0, 0, sgn), (x0 + gap + i * (w + gap), y, zplane), (1, 0, 0), w, h)


def rows_x(m, sgn, xplane, z0, z1, y, n, w, h):
    """n windows between z0..z1 on a wall whose outward normal is (sgn, 0, 0), wall plane x = xplane."""
    gap = (z1 - z0 - n * w) / (n + 1)
    for i in range(n):
        m.window((sgn, 0, 0), (xplane, y, z0 + gap + i * (w + gap)), (0, 0, 1), w, h)


def leaves(m, zplane, xs, y0, y1, sw, front=1, depth=0.25, post=None, post_w=0.18):
    """Sliding-door leaves between the x edges `xs` proud of the wall at zplane (front=+1 for the +Z face, -1 for -Z)."""
    for a, b in zip(xs[:-1], xs[1:]):
        if front > 0:
            m.box(a + 0.05, b - 0.05, y0, y1, zplane, zplane + depth, sw)
        else:
            m.box(a + 0.05, b - 0.05, y0, y1, zplane - depth, zplane, sw)
    if post is not None:
        for x in xs:
            if front > 0:
                m.box(x - post_w / 2, x + post_w / 2, y0, y1 + 0.1, zplane, zplane + depth + 0.07, post)
            else:
                m.box(x - post_w / 2, x + post_w / 2, y0, y1 + 0.1, zplane - depth - 0.07, zplane, post)


def louvres(m, zplane, xs, rows, front=1, sw=DGREY, off=0.3):
    """Window / louvre panels (flat quads) on door leaves: rows = [(y0, y1), ...] for every leaf between consecutive `xs`."""
    for a, b in zip(xs[:-1], xs[1:]):
        for y0, y1 in rows:
            z = zplane + (off if front > 0 else -off)
            n = (0, 0, front)
            m.poly([(a + 0.7, y0, z), (b - 0.7, y0, z), (b - 0.7, y1, z), (a + 0.7, y1, z)], sw, (a, y0, z - front))


def barrel(m, x0, x1, z0, z1, spring, rise, wall_sw, roof_sw, n=14):
    """Barrel-vault hall along Z: straight walls to `spring`, circular-arc roof, arched end caps.  Returns the arch height function."""
    W = x1 - x0
    xm = (x0 + x1) / 2
    R = (W * W / 4 + rise * rise) / (2 * rise)
    cy = spring + rise - R

    def arch(x):
        return cy + math.sqrt(max(R * R - (x - xm) ** 2, 0.0))
    prof = [(x0 + W * i / n, arch(x0 + W * i / n)) for i in range(n + 1)]
    prof[0] = (x0, spring)
    prof[-1] = (x1, spring)
    m.box(x0, x1, 0, spring, z0, z1, wall_sw, top=False)
    zc = (z0 + z1) / 2
    for i in range(n):
        (xa, ya), (xb, yb) = prof[i], prof[i + 1]
        m.poly([(xa, ya, z0), (xb, yb, z0), (xb, yb, z1), (xa, ya, z1)], roof_sw, (xm, spring - 8, zc))
    for z, sgn in ((z1, 1), (z0, -1)):
        m.poly([(x, y, z) for x, y in prof], wall_sw, (xm, spring - 1, z - sgn * 5))
    return arch


def stripes(m, x0, x1, y0, y1, plane, front, cols, w=1.7, axis="x", depth=0.08):
    """Vertical colour stripes on a wall (plane = z for axis 'x', = x for axis 'z')."""
    a = x0
    i = 0
    while a < x1 - 1e-6:
        b = min(a + w, x1)
        sw = cols[i % len(cols)]
        if axis == "x":
            z0, z1 = (plane, plane + depth) if front > 0 else (plane - depth, plane)
            m.box(a, b, y0, y1, z0, z1, sw, top=False)
        else:
            xa, xb = (plane, plane + depth) if front > 0 else (plane - depth, plane)
            m.box(xa, xb, y0, y1, a, b, sw, top=False)
        a = b
        i += 1


def roof_vents(m, pts, y, sw=DGREY):
    for x, z in pts:
        m.box(x - 0.4, x + 0.4, y, y + 0.9, z - 0.4, z + 0.4, sw)


# Hangar 4 -----------------------------------------------------------------------------------
def hangar4():
    """Pale-yellow ribbed hangar whose long wall faces the runway (west, heading 270; the user's call: it must not face north).  The wide
    arched door opening, "4" roundel and Government of Alberta sign from the Wikimedia photo are on that front (+Z) wall; the roof ridge runs
    along the footprint's long axis (N-S), so the gable ends are the north and south ends.  Brick block at the north end (viewer-left of
    the front), orange-panelled neighbour at the south end.  OSM 325273554: 71 (N-S) x 33.5 m."""
    m = Mesh(textured=True)
    W, D, wh, rise = 71.1, 33.5, 9.0, 3.4
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, wh, z0, z1, YELLOWR, top=False)
    m.gable(x0, x1, wh, rise, z0, z1, along_z=False, sw_roof=METAL, sw_wall=YELLOWR)
    for z in (z0 - 0.12, z1):
        m.box(x0, x1, wh - 0.5, wh + 0.05, z, z + 0.12, RWHITE)
    a, hd, top, n = 14.0, 6.2, 8.4, 10
    cx = 6.0  # the opening is not centred: it sits towards the north (viewer-left) half of the wall
    pts = [(cx - a, 0, z1 + 0.06), (cx + a, 0, z1 + 0.06)] + [(cx + a * u, hd + (top - hd) * (1 - u * u), z1 + 0.06)
                                                              for u in [1 - 2 * k / n for k in range(n + 1)]]
    m.poly(pts, DARK, (cx, 3, z1 - 4))
    for sx in (cx - a - 0.45, cx + a):
        m.box(sx, sx + 0.45, 0, hd, z1, z1 + 0.14, RWHITE)
    rx = cx - a - 4.0
    m.box(rx - 1.1, rx + 1.1, 5.5, 7.8, z1, z1 + 0.12, RWHITE)  # white board behind the roundel, right of the opening
    number_disc(m, rx, 6.65, z1 + 0.12, (0, 1), 0.9, "4")
    m.box(cx + 2.0, cx + 6.6, 8.5, 8.95, z1, z1 + 0.1, RWHITE)  # Government of Alberta sign, over the arch's shoulder
    m.box(cx + 2.2, cx + 3.0, 8.6, 8.85, z1 + 0.1, z1 + 0.13, BLUE)
    m.box(x1, x1 + 10.0, 0, 4.6, z1 - 16.0, z1, BRICKD)
    m.box(x0 - 8.0, x0, 0, 9.0, z1 - 22.0, z1 - 2.0, SALMON)
    rows_x(m, -1, x0 - 8.0, z1 - 21.0, z1 - 3.0, 4.2, 4, 2.0, 1.6)
    roof_vents(m, [(-20, 0), (0, 0), (20, 0)], wh + rise)
    m.mirror_x()
    return m


# Hangar 5 -----------------------------------------------------------------------------------
def hangar5():
    """Tan ribbed hangar, cream upper band, white sliding doors on the west gable end (+Z, heading 270), two-storey bronze
    curtain-wall office at the east (landside) end, "5" roundel high on the south wall.  OSM 325270299: 53.1 x 43.3 m."""
    m = Mesh(textured=True)
    W, D, wh, rise = 53.1, 43.3, 8.6, 3.2
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, wh - 2.4, z0, z1, BRONZE, top=False)  # charcoal-brown ribbed lower wall, cream band above (Street View)
    m.box(x0, x1, wh - 2.4, wh, z0, z1, CREAM, top=False)
    m.gable(x0, x1, wh, rise, z0, z1, along_z=True, sw_roof=METAL, sw_wall=CREAM)
    for x in (x0 - 0.12, x1):
        m.box(x, x + 0.12, wh - 0.4, wh + 0.05, z0, z1, DGREY)
    xs = [-22.0 + 11.0 * i for i in range(5)]
    m.box(-22.4, 22.4, 0, 8.0, z1, z1 + 0.05, DARK)
    leaves(m, z1, xs, 0, 7.5, RWHITE, post=GREEN)
    louvres(m, z1, xs, [(1.8, 3.4), (4.4, 6.0)])
    m.box(-22.4, 22.4, 7.5, 7.9, z1, z1 + 0.35, DGREY)
    # landside office block, 30 x 12 m, two storeys of bronze glazing
    m.box(-15.0, 15.0, 0, 7.8, z0 - 12.0, z0, BRONZE)
    for y in (1.0, 4.4):
        rows_z(m, -1, z0 - 12.0, -15.0, 15.0, y, 8, 2.5, 2.3)
    m.box(-15.4, 15.4, 7.8, 8.2, z0 - 12.4, z0, DGREY)
    m.box(-3.5, 3.5, 3.1, 3.4, z0 - 13.8, z0 - 12.0, DGREY)  # entrance canopy
    m.box(15.0, 27.0, 0, 4.5, z0 - 8.0, z0, GREY)  # lower grey block towards the hangar's south side
    number_disc(m, x0, 7.3, z0 + 7.0, (-1, 0), 0.95, "5")
    roof_vents(m, [(0, -8), (0, 8), (10, 0)], wh + rise)
    m.mirror_x()
    return m


# Hangar 6 -----------------------------------------------------------------------------------
def hangar6():
    """White hangar with green side walls (west gable end = apron side with sliding doors, heading 270), low white annex at the
    east end with a blue door, "6" roundel high on the east gable.  OSM 325267780: 41.9 x 46.2 m."""
    m = Mesh(textured=True)
    W, D, wh, rise = 41.9, 46.2, 8.0, 3.0
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, wh, z0, z1, GREEN, top=False)
    for z, f in ((z1, 1), (z0, -1)):
        if f > 0:
            m.box(x0, x1, 0, wh, z, z + 0.06, RWHITE, top=False)
        else:
            m.box(x0, x1, 0, wh, z - 0.06, z, RWHITE, top=False)
    m.gable(x0, x1, wh, rise, z0 - 0.06, z1 + 0.06, along_z=True, sw_roof=METAL, sw_wall=RWHITE)
    for x in (x0 - 0.12, x1):
        m.box(x, x + 0.12, wh - 0.4, wh + 0.05, z0, z1, NAVY)
    xs = [-15.0 + 7.5 * i for i in range(5)]
    m.box(-15.4, 15.4, 0, 7.2, z1 + 0.06, z1 + 0.1, DARK)
    leaves(m, z1 + 0.06, xs, 0, 6.9, RWHITE, post=DGREY)
    m.box(-15.4, 15.4, 6.9, 7.3, z1 + 0.06, z1 + 0.4, DGREY)
    m.box(-12.0, 12.0, 0, 5.2, z0 - 9.0, z0, RWHITE)  # low annex, east end
    m.box(-12.3, 12.3, 5.2, 5.5, z0 - 9.3, z0, DGREY)
    m.box(4.4, 5.8, 0, 2.3, z0 - 9.12, z0 - 9.0, BLUE)
    m.box(-6.0, -1.0, 2.4, 3.6, z0 - 9.12, z0 - 9.0, NAVY)  # company sign
    number_disc(m, 9.0, 6.9, z0 - 0.06, (0, -1), 0.95, "6")
    roof_vents(m, [(0, -10), (0, 10)], wh + rise)
    m.mirror_x()
    return m


# Hangar 7 -----------------------------------------------------------------------------------
def hangar7():
    """Steel-blue ribbed hangar; west gable end (heading 270) has a wide white two-tier sliding door with the "7" roundel on the
    blue wall beside it; darker slate-blue annex with awning at the east end.  OSM 325271251: 36.4 x 39.3 m."""
    m = Mesh(textured=True)
    W, D, wh, rise = 36.4, 39.3, 8.4, 2.4
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, wh, z0, z1, STEEL, top=False)
    m.gable(x0, x1, wh, rise, z0, z1, along_z=True, sw_roof=METAL, sw_wall=STEEL)
    for x in (x0 - 0.12, x1):
        m.box(x, x + 0.12, wh - 0.4, wh + 0.05, z0, z1, RWHITE)
    xs = [-8.0 + 6.0 * i for i in range(5)]
    m.box(-8.4, 16.4, 0, 8.0, z1, z1 + 0.05, DARK)
    leaves(m, z1, xs, 0, 7.8, RWHITE, post=DGREY)
    m.box(-8.4, 16.4, 7.8, 8.2, z1, z1 + 0.3, DGREY)
    m.box(-8.4, 16.4, 4.0, 4.15, z1 + 0.25, z1 + 0.3, DGREY)  # leaf joint between the two tiers
    number_disc(m, -13.2, 6.3, z1, (0, 1), 0.95, "7")
    m.box(-10.0, 10.0, 0, 5.4, z0 - 8.0, z0, SLATE)  # annex, east end
    m.box(-10.3, 10.3, 5.4, 5.7, z0 - 8.3, z0, DGREY)
    m.box(-4.0, 4.0, 3.0, 3.25, z0 - 9.4, z0 - 8.0, NAVY)  # awning
    rows_z(m, -1, z0 - 8.0, -9.0, 9.0, 1.2, 2, 1.4, 2.0)
    m.box(x0, x1, 5.8, 6.6, z0 - 0.02, z0 + 0.02, DGREY)
    roof_vents(m, [(0, -8), (0, 0), (0, 8)], wh + rise)
    m.mirror_x()
    return m


# Hangar 8 -----------------------------------------------------------------------------------
def hangar8():
    """Pale blue-grey hall with a full-width glazed sliding-door wall on the west gable end (heading 270), a taller flat-topped end
    block carrying the "8" roundel, and a long low wing with a roof clerestory.  OSM 325268698: 66.3 x 52.9 m."""
    m = Mesh(textured=True)
    W, D = 66.3, 52.9
    z0, z1 = -D / 2, D / 2
    # hall (viewer-left, +x) 35 m, end block 10 m, low wing 21 m
    hx0, hx1 = -2.0, 33.15
    m.box(hx0, hx1, 0, 9.0, z0, z1, STEEL, top=False)
    m.gable(hx0, hx1, 9.0, 3.4, z0, z1, along_z=True, sw_roof=METAL, sw_wall=STEEL)
    xs = [0.0 + 6.2 * i for i in range(6)]
    m.box(-0.4, 31.4, 0, 8.6, z1, z1 + 0.05, DARK)
    leaves(m, z1, xs, 0, 8.3, RWHITE, post=GREEN)
    louvres(m, z1, xs, [(1.6, 3.2), (4.2, 5.8)])
    m.box(-0.4, 31.4, 8.3, 8.6, z1, z1 + 0.45, GREEN)  # canopy / header with its green trim line
    m.box(-12.0, hx0, 0, 12.6, z0, z1, RWHITE)  # taller end block
    m.box(-12.3, hx0, 12.6, 12.9, z0 - 0.3, z1 + 0.3, DGREY)
    number_disc(m, -7.0, 10.6, z1, (0, 1), 0.95, "8")
    m.box(-12.0 - 0.0, -11.3, 0, 12.9, z1 - 0.1, z1 + 0.3, DGREY)  # downpipe / stack beside the roundel
    wx0, wx1 = -W / 2, -12.0
    m.box(wx0, wx1, 0, 6.2, z0, z1, STEEL, top=False)
    m.box(wx0 - 0.15, wx1, 6.2, 6.5, z0 - 0.15, z1 + 0.15, DGREY)
    m.box(wx0 + 2, wx1 - 2, 6.5, 7.9, z0 + 4, z1 - 4, RWHITE, top=True)
    rows_x(m, 1, wx1 - 2, z0 + 4.5, z1 - 4.5, 6.8, 8, 2.2, 0.9)
    rows_x(m, -1, wx0 + 2, z0 + 4.5, z1 - 4.5, 6.8, 8, 2.2, 0.9)
    rows_z(m, 1, z1, wx0 + 4, wx1 - 4, 1.6, 4, 2.2, 2.6)
    m.box(wx0 + 6.0, wx0 + 9.0, 0, 2.5, z1, z1 + 0.08, DGREY)
    roof_vents(m, [(15, -12), (15, 0), (15, 12)], 12.4)
    m.mirror_x()
    return m


# Hangar 3, the dark-blue hangar, Hangar 20 (Esso), Hangar 40 (Canadian Helicopters) ----------------
def parapet(m, x0, x1, z0, z1, y0, y1, t, sw):
    """Four thin boxes round a rectangle (flat-roof parapet / fascia band), outer size x0..x1, z0..z1."""
    m.box(x0, x1, y0, y1, z0, z0 + t, sw)
    m.box(x0, x1, y0, y1, z1 - t, z1, sw)
    m.box(x0, x0 + t, y0, y1, z0 + t, z1 - t, sw)
    m.box(x1 - t, x1, y0, y1, z0 + t, z1 - t, sw)


def hangar3():
    """Hangar 3: long flat-roofed pale-blue hangar (heading 90, landside long wall faces east / 109 St).  Smooth pale-blue walls under a dark
    blue fascia with a red line below it, a tall south part (8.2 m) stepping down to the north end, big cream roller doors, green-teal window
    columns, a glazed entrance bump, the blue "3" roundel beside the main door (Street View 2007-2014, 3 109 St NW).  Footprint 81.6 x 25.7 m
    measured on the 2014 Wayback imagery (OSM way 325273617 is a short trace of it).  Model x = south (viewer-left from the landside)."""
    m = Mesh(textured=True)
    L, D = 81.6, 25.7
    x0, x1, z0, z1 = -L / 2, L / 2, -D / 2, D / 2
    xs, hs, hn = -28.0, 8.2, 6.4
    m.box(xs, x1, 0, hs, z0, z1, PBFLAT)
    m.box(x0, xs, 0, hn, z0, z1, PBFLAT)
    parapet(m, xs, x1, z0 - 0.1, z1 + 0.1, hs - 0.6, hs + 0.45, 0.5, NAVY)
    parapet(m, x0, xs, z0 - 0.1, z1 + 0.1, hn - 0.6, hn + 0.45, 0.5, NAVY)
    m.box(xs - 0.1, xs + 0.1, hn + 0.4, hs + 0.4, z0 - 0.1, z1 + 0.1, NAVY)
    m.box(xs, x1, hs - 1.1, hs - 0.9, z1, z1 + 0.1, RED)  # red line under the fascia on the landside wall
    m.box(x0, xs, hn - 1.1, hn - 0.9, z1, z1 + 0.1, RED)
    m.box(x1, x1 + 0.1, hs - 1.1, hs - 0.9, z0, z1, RED)
    # landside (+Z, east) wall, south to north
    m.box(21.0, 33.0, 0, 6.0, z1, z1 + 0.1, GREY)  # main roller door frame
    m.box(21.4, 32.6, 0, 5.7, z1 + 0.1, z1 + 0.2, CREAM)
    rows_z(m, 1, z1 + 0.2, 21.8, 32.2, 1.3, 4, 1.8, 0.9)  # window band across the lower door
    number_disc(m, 18.2, 5.3, z1, (0, 1), 0.95, "3")
    for xw in (13.2, 15.4):  # green-teal tall window columns
        m.window((0, 0, 1), (xw, 0.9, z1), (1, 0, 0), 1.3, 6.2)
    m.box(-21.2, -5.3, 0, 9.0, z1, z1 + 7.0, PBFLAT)  # entrance bump on the north half
    parapet(m, -21.3, -5.2, z1 - 0.1, z1 + 7.1, 8.4, 9.45, 0.5, NAVY)
    rows_z(m, 1, z1 + 7.0, -20.2, -6.3, 1.2, 4, 1.9, 6.4)
    m.box(-3.4, -1.8, 0, 2.3, z1, z1 + 0.1, DGREY)  # personnel door
    m.box(-12.8, -8.6, 0, 4.4, z1, z1 + 0.1, GREY)  # smaller roller door (north half)
    m.box(-12.6, -8.8, 0, 4.2, z1 + 0.1, z1 + 0.2, CREAM)
    m.box(-12.9, -12.7, 0, 4.4, z1 + 0.1, z1 + 0.25, RED)
    m.box(-37.4, -33.4, 0, 4.4, z1, z1 + 0.1, GREY)  # roller door at the low north end
    m.box(-37.2, -33.6, 0, 4.2, z1 + 0.1, z1 + 0.2, CREAM)
    # airside (-Z, west) wall: no photo, doors and windows kept generic
    for xd in (-22.0, 6.0):
        m.box(xd, xd + 1.4, 0, 2.3, z0 - 0.1, z0, DGREY)
    rows_z(m, -1, z0, -36.0, 36.0, 4.0, 9, 1.8, 1.3)
    roof_vents(m, [(30, 0), (8, 0), (-12, 0)], hs + 0.45)
    roof_vents(m, [(-34, 0)], hn + 0.45)
    m.mirror_x()
    return m


def hangar3_annex():
    """Tan concrete-block annex at the south end of Hangar 3 (heading 90; the brown double gate and the flat parapet roof of Street View 2012)."""
    m = Mesh(textured=True)
    L, D, h = 15.9, 13.2, 5.6
    m.box(-L / 2, L / 2, 0, h, -D / 2, D / 2, TANBLK)
    parapet(m, -L / 2 - 0.1, L / 2 + 0.1, -D / 2 - 0.1, D / 2 + 0.1, h - 0.3, h + 0.4, 0.4, BEIGE)
    m.box(L / 2 - 6.0, L / 2 - 1.0, 0, 2.6, D / 2, D / 2 + 0.1, BRICKD)  # brown gate on the east face
    m.box(-L / 2 + 2.0, -L / 2 + 5.0, 0.8, 1.8, D / 2, D / 2 + 0.2, GREY)  # electrical cabinet
    m.mirror_x()
    return m


def bluehangar():
    """Small dark-blue gabled hangar north of Hangar 3 (5 109 St NW; Street View 2007-2014), not numbered in the photos: dark-blue ribbed side
    walls, grey roof, white gable end with a big roller door (assumed to face south), a blue air-handler box on the east wall and two vent
    pipes.  OSM way 325272095: 24.6 x 20.7 m.  Model frame: +Z = the white door end."""
    m = Mesh(textured=True)
    W, D, wh, rise = 20.7, 24.6, 6.5, 3.0
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, wh, z0, z1, NAVYB, top=False)
    m.gable(x0, x1, wh, rise, z0, z1, along_z=True, sw_roof=DGREY, sw_wall=NAVYB)
    m.box(x0, x1, 0, wh, z1, z1 + 0.06, RWHITE, top=False)
    m.poly([(x0, wh, z1 + 0.06), (x1, wh, z1 + 0.06), (0.0, wh + rise, z1 + 0.06)], RWHITE, (0.0, wh - 1, z1 - 2))
    m.box(-5.6, 5.6, 0, 5.2, z1 + 0.06, z1 + 0.16, CREAM)
    m.box(x1, x1 + 0.7, 3.0, 4.6, 1.0, 4.4, BLUE)  # air-handler box
    m.box(x1 - 0.1, x1, 3.4, 4.2, 1.2, 4.2, DARK)
    for zz in (-3.0, -1.5):
        m.box(1.0, 1.3, wh + 1.0, wh + 3.8, zz, zz + 0.3, DGREY)
    m.mirror_x()
    return m


def hangar19():
    """Hangar 19 (user, 2026-10-21: the low brown/tan building beside the Esso building, Street View photos 06-09 and 62-69 Airport Rd NW; possibly the
    General Aviation Centre): two low tan/cream wings with glazed shop fronts either side of a taller two-storey brick centre with a stair
    tower.  Footprint about 65 x 29 m, long axis along bearing 142, measured on the 2014 imagery (not in OSM).  Heading 232 (front faces SW to
    Airport Rd); +x is the NW wing."""
    m = Mesh(textured=True)
    L, D = 65.0, 29.0
    x0, x1, z0, z1 = -L / 2, L / 2, -D / 2, D / 2
    cx0, cx1 = -8.0, 8.0
    for wx0, wx1 in ((x0, cx0), (cx1, x1)):  # low wings
        m.box(wx0, wx1, 0, 4.4, z0, z1, BEIGE)
        parapet(m, wx0 - 0.1, wx1 + 0.1, z0 - 0.1, z1 + 0.1, 4.0, 4.8, 0.4, TANBLK)
        n = int((wx1 - wx0) // 6.0)
        gap = ((wx1 - wx0) - 2.0 - n * 4.0) / n
        for i in range(n):  # glazed shop-front bays
            m.window((0, 0, 1), (wx0 + 1.0 + gap / 2 + i * (4.0 + gap), 0.5, z1), (1, 0, 0), 4.0, 2.8)
        m.window((0, 0, -1), (wx0 + 2.0, 1.6, z0), (1, 0, 0), wx1 - wx0 - 4.0, 1.4)
    m.box(cx0, cx1, 0, 8.6, z0, z1, BRICKD)  # brick centre
    parapet(m, cx0 - 0.1, cx1 + 0.1, z0 - 0.1, z1 + 0.1, 8.2, 9.0, 0.4, TANBLK)
    rows_z(m, 1, z1, cx0 + 1.5, cx1 - 1.5, 5.2, 3, 3.0, 2.0)
    m.window((0, 0, 1), (-1.4, 0.0, z1), (1, 0, 0), 2.8, 2.6)  # entrance
    m.box(-2.2, 2.2, 3.0, 3.4, z1, z1 + 1.6, TANBLK)  # entrance canopy
    m.box(-3.0, 3.0, 8.8, 11.0, z1 - 8.0, z1 - 2.0, BRICKD)  # taller stair tower
    m.box(-3.2, 3.2, 11.0, 11.35, z1 - 8.2, z1 - 1.8, TANBLK)
    m.mirror_x()
    return m


def gs_hut():
    """ILS glideslope shelter in the infield beside the old runway 16/34 (west-lineup photo, 2014 aerial): a small flat-roofed hut painted
    in red and white checks on all four walls, a door on the east face, and a mast with a small antenna box 5.7 m north.  Heading 0."""
    m = Mesh(textured=True)
    hx, hz, h = 2.75, 2.25, 3.0
    m.box(-hx, hx, 0, h, -hz, hz, WHITE)
    m.box(-hx - 0.1, hx + 0.1, h, h + 0.2, -hz - 0.1, hz + 0.1, LROOF)
    for row in range(2):
        y0 = row * 1.5
        for i in range(5):  # N and S walls
            if (i + row) % 2 == 0:
                xa = -hx + i * 2 * hx / 5
                m.box(xa, xa + 2 * hx / 5, y0, y0 + 1.5, hz, hz + 0.04, RED)
                m.box(xa, xa + 2 * hx / 5, y0, y0 + 1.5, -hz - 0.04, -hz, RED)
        for i in range(4):  # E and W walls
            if (i + row) % 2 == 0:
                za = -hz + i * 2 * hz / 4
                m.box(hx, hx + 0.04, y0, y0 + 1.5, za, za + 2 * hz / 4, RED)
                m.box(-hx - 0.04, -hx, y0, y0 + 1.5, za, za + 2 * hz / 4, RED)
    m.box(hx, hx + 0.1, 0, 2.1, -0.5, 0.5, DGREY)  # door
    m.box(-1.6, -1.45, 0, 9.0, 5.6, 5.75, DGREY)  # mast
    m.box(-2.0, -1.05, 8.0, 8.9, 5.5, 5.85, WHITE)  # antenna box
    m.mirror_x()
    return m


def hangar20():
    """Hangar 20 = the Esso / Imperial Oil building (user, 2026-10-21; Street View 2012, 83 Airport Rd NW).  Two tiers of tan horizontal-ribbed
    cladding: a 45 x 45 m two-storey upper tier with a ribbon window and rounded front corners, wrapped on the SW (front, Airport Rd) and SE
    sides by a lower one-storey tier with a long dark glazed band and the Esso oval.  Blue "20" roundel on the upper tier's NW end wall.
    Measured on the 2014 imagery (not in OSM).  Heading 228 (front faces SW); origin at the upper tier's centre."""
    m = Mesh(textured=True)
    U, hu, hl, r = 45.0, 10.5, 4.6, 4.5
    a = U / 2
    pts = [(-a, -a), (a, -a), (a, a - r)] + [(a - r + r * math.cos(math.radians(15 * k)), a - r + r * math.sin(math.radians(15 * k))) for k in range(1, 7)] \
        + [(-a + r + r * math.cos(math.radians(90 + 15 * k)), a - r + r * math.sin(math.radians(90 + 15 * k))) for k in range(0, 7)] + [(-a, a - r)]
    prism(m, pts, 0, hu, BEIGE)
    m.box(-a - 0.2, a + 0.2, hu, hu + 0.35, -a - 0.2, a + 0.2, DGREY)  # roof edge
    # lower tier wrapping the SE (-X) and SW (+Z) sides
    m.box(-a - 10.0, -a, 0, hl, -a, a + 8.0, BEIGE)
    m.box(-a, a, 0, hl, a, a + 8.0, BEIGE)
    m.box(-a - 10.2, a, hl, hl + 0.3, -a - 0.2, a + 8.2, DGREY)
    # glazing: upper ribbon on the long walls, lower tier dark band
    rows_z(m, 1, a, -a + 5.0, a - 5.0, 6.4, 4, 8.0, 2.0)
    rows_x(m, 1, a, -a + 5.0, a - 5.0, 6.4, 3, 8.0, 2.0)
    rows_x(m, -1, -a, -a + 5.0, a - 5.0, 6.4, 3, 8.0, 2.0)
    m.window((0, 0, 1), (-a, 1.0, a + 8.0), (1, 0, 0), 2 * a, 2.0)  # lower tier, front band
    m.window((-1, 0, 0), (-a - 10.0, 1.0, -a), (0, 0, 1), 2 * a + 8.0, 2.0)  # lower tier, SE band
    # NE (airside) wall, west-lineup photo: long ribbon window over the SE half, big dark hangar-type door in the NW half
    m.window((0, 0, -1), (-20.0, 6.0, -a), (1, 0, 0), 22.0, 2.2)
    m.box(3.0, 18.0, 0, 7.6, -a - 0.12, -a, DGREY)
    # Esso oval (white, blue rim, red lettering bar) on the lower tier's front wall
    ox, oy, oz = -6.0, 3.4, a + 8.0
    ring = [(2.0 * math.cos(math.radians(20 * k)), 0.7 * math.sin(math.radians(20 * k))) for k in range(18)]
    m.poly([(ox + u, oy + v, oz + 0.12) for u, v in ring], BLUE, (ox, oy, oz - 2))
    m.poly([(ox + 0.85 * u, oy + 0.8 * v, oz + 0.15) for u, v in ring], WHITE, (ox, oy, oz - 2))
    m.box(ox - 1.2, ox + 1.2, oy - 0.12, oy + 0.12, oz + 0.15, oz + 0.2, RED)
    number_disc(m, a, 8.6, a - 6.0, (1, 0), 1.2, "20")  # NW end wall of the upper tier (Street View photo 11)
    m.box(-4.0, 4.0, hu + 0.35, hu + 1.5, -6.0, 6.0, DGREY)  # plant on the roof
    m.mirror_x()
    return m


def hangar40():
    """Hangar 40 = Canadian Helicopters (user, 2026-10-21; Street View 2010-2012, 12043 121 St NW; Flickr woodhead 13207130405).  Faces NW to the
    car park: a white ribbed hall (left, with the big door), a two-storey red-brick office with red fascia, red awnings, glass-block
    entrance and a white gabled canopy (middle), and a taller white block carrying the blue "40" roundel (right).  Footprint is the white
    roof of OSM way 230718900 (about 38 x 25 m); the blue-grey gabled hall beside it is not part of this model.  Heading 318."""
    m = Mesh(textured=True)
    W, D = 38.0, 25.0
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    hx0 = 3.0
    m.box(hx0, x1, 0, 8.0, z0, z1, RWHITE, top=False)
    m.gable(hx0, x1, 8.0, 1.4, z0, z1, along_z=True, sw_roof=METAL, sw_wall=RWHITE)
    m.box(hx0 + 2.0, hx0 + 14.0, 0, 6.0, z0 - 0.12, z0, DGREY)  # big hangar door on the gable wall opposite the landside (user, 2026-10-21)
    m.box(-7.0, hx0, 0, 7.6, z0, z1, BRICKD)  # two-storey brick office
    m.box(-7.2, hx0 + 0.2, 7.6, 8.1, z0 - 0.2, z1 + 0.2, RED)
    m.window((0, 0, 1), (-3.2, 0.0, z1), (1, 0, 0), 1.4, 2.2)  # entrance door
    m.box(-4.7, -0.3, 2.7, 3.2, z1, z1 + 1.5, RWHITE)  # white canopy with gable
    m.gable(-4.7, -0.3, 3.2, 0.9, z1, z1 + 1.5, along_z=True, sw_roof=RWHITE, sw_wall=RWHITE)
    for xg in (-6.6, 0.6):  # glass-block panels
        m.window((0, 0, 1), (xg, 0.5, z1), (1, 0, 0), 1.6, 2.0)
    m.box(-7.1, -4.5, 2.6, 3.3, z1, z1 + 1.0, RED)  # red awning
    m.box(0.9, 3.0, 2.6, 3.3, z1, z1 + 1.0, RED)
    for xw in (-6.0, -1.6):  # first-floor windows
        m.window((0, 0, 1), (xw, 4.0, z1), (1, 0, 0), 2.6, 2.2)
    m.box(-19.0, -7.0, 0, 11.0, z0, z1, RWHITE)  # tall white block
    m.box(-19.1, -6.9, 11.0, 11.3, z0 - 0.1, z1 + 0.1, DGREY)
    number_disc(m, -9.4, 8.7, z1, (0, 1), 1.15, "40")
    m.box(-1.0, 1.6, 7.6, 8.9, -6.0, -2.0, DGREY)  # roof unit on the office
    m.mirror_x()
    return m


# Hangar 11 ----------------------------------------------------------------------------------
def hangar11():
    """USAAF T3 (1942-43) as it looked in the 1950s-60s: white barrel-vault hall with seven peach sliding-door leaves on the north end
    (+Z, heading 0), a three-storey white-clapboard annex across the south end carrying the "11" roundel, a control cab and the big
    roof sign, a two-storey east wing and a low west annex.  OSM 325268748: 86 x 64 m footprint."""
    m = Mesh(textured=True)
    z0, z1 = -32.0, 32.0
    bx0, bx1 = -29.0, 26.0
    arch = barrel(m, bx0, bx1, z0, z1, 7.6, 6.4, RWHITE, RWHITE)
    xs = [-24.0 + 48.0 / 7 * i for i in range(8)]
    m.box(-24.4, 24.4, 0, 8.2, z1, z1 + 0.05, DARK)
    leaves(m, z1, xs, 0, 8.0, PEACH, post=DGREY)
    for i in range(5):
        x = bx0 + 8 + i * 9.5
        if 9.8 + 1.3 < arch(x) - 0.4:
            m.window((0, 0, 1), (x - 0.7, 9.8, z1), (1, 0, 0), 1.4, 1.3)
    m.box(-24.4, 24.4, 8.0, 8.35, z1, z1 + 0.3, DGREY)
    # south annex: three storeys
    ax0, ax1, az0, az1 = -29.0, 7.0, -46.0, z0
    m.box(ax0, ax1, 0, 11.2, az0, az1, WHITE, top=False)
    m.box(ax0 - 0.2, ax1 + 0.2, 11.2, 11.6, az0 - 0.2, az1, GREEN)
    m.box(ax0, ax1, 11.2, 11.3, az0, az1, DGREY)
    for y in (1.4, 4.7, 8.0):
        rows_z(m, -1, az0, ax0 + 1.5, ax1 - 1.5, y, 9, 1.6, 1.5)
        rows_x(m, -1, ax0, az0 + 1.5, az1 - 1.5, y, 3, 1.6, 1.5)
        rows_x(m, 1, ax1, az0 + 1.5, az1 - 1.5, y, 3, 1.6, 1.5)
    number_disc(m, -22.0, 8.6, az0, (0, -1), 1.0, "11")
    m.box(-26.0, 4.0, 11.6, 14.4, az0 + 0.4, az0 + 0.6, WHITE)  # roof sign board
    m.box(-25.0, 3.0, 12.9, 13.4, az0 + 0.2, az0 + 0.4, DARK)
    m.box(-25.0, 3.0, 11.9, 12.4, az0 + 0.2, az0 + 0.4, DARK)
    m.box(-9.0, -4.0, 11.6, 14.6, az0 + 6.0, az0 + 11.0, DGREY)  # control cab
    m.box(-9.1, -3.9, 12.4, 13.9, az0 + 5.9, az0 + 11.1, GLASS)
    m.box(-9.4, -3.6, 14.6, 14.9, az0 + 5.6, az0 + 11.4, DGREY)
    # fire escape on the west side: two landings and a ladder
    m.box(ax0 - 1.6, ax0, 7.2, 7.35, az0 + 3.0, az0 + 5.0, DGREY)
    m.box(ax0 - 1.6, ax0, 3.9, 4.05, az0 + 3.0, az0 + 5.0, DGREY)
    m.box(ax0 - 0.12, ax0 - 0.05, 0, 11.0, az0 + 7.2, az0 + 7.3, DGREY)
    m.box(ax0 - 0.12, ax0 - 0.05, 0, 11.0, az0 + 8.4, az0 + 8.5, DGREY)
    # east wing: two storeys, ribbon windows, taller stair tower at its south end
    m.box(26.0, 43.15, 0, 8.6, -20.0, z1, WHITE, top=True)
    m.box(25.8, 43.35, 8.6, 8.9, -20.2, z1 + 0.2, GREEN)
    for y in (1.4, 5.0):
        rows_x(m, 1, 43.15, -18.0, z1 - 2.0, y, 10, 1.5, 1.8)
    m.box(36.0, 43.15, 8.9, 13.5, -20.0, -9.0, WHITE)
    # west annex
    m.box(-43.15, bx0, 0, 6.0, -30.0, -4.0, WHITE)
    rows_x(m, -1, -43.15, -28.0, -6.0, 2.4, 5, 1.2, 1.5)
    roof_vents(m, [(-12, -10), (-12, 6), (10, -10), (10, 6)], 13.8)
    m.mirror_x()
    return m


# Hangar 14 (Alberta Aviation Museum) ----------------------------------------------------------
def hangar14():
    """Hangar 14 (BCATP 1941, Alberta Aviation Museum): white horizontal-siding upper band over a dark teal-green lower wall with
    glazed panes, museum entrance with a teal canopy on the east front (+Z, heading 90), three apron door bays on the west side.
    OSM 230718920: 100 (N-S) x 90.8 m."""
    m = Mesh(textured=True)
    W, D, H = 100.0, 90.8, 8.8
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, 4.4, z0, z1, TEAL, top=False)
    m.box(x0, x1, 4.4, H, z0, z1, WHITE, top=True)
    m.box(x0 - 0.2, x1 + 0.2, H, H + 0.5, z0 - 0.2, z1 + 0.2, TEAL)
    m.gable(x0, x1, H + 0.5, 2.6, z0, z1, along_z=True, sw_roof=LROOF, sw_wall=WHITE)
    # east front: glazed band, sign bars, canopy, entrance
    rows_z(m, 1, z1, x0 + 3, x1 - 3, 1.0, 14, 4.2, 2.9)
    for a, b in ((-24, -8), (-4, 8), (12, 26)):
        m.box(a, b, 5.9, 7.1, z1, z1 + 0.12, TEAL)
    m.box(-26.0, -14.0, 3.5, 3.8, z1, z1 + 3.2, TEAL)  # entrance canopy
    m.box(-25.5, -14.5, 3.8, 4.1, z1 + 3.0, z1 + 3.2, WHITE)
    m.box(14.0, 26.0, 0, 3.0, z1, z1 + 0.15, DGREY)
    for y in (0.9, 2.1):
        rows_z(m, 1, z1 + 0.15, 14.5, 25.5, y, 4, 2.0, 0.9)
    # west apron side: three door bays
    xs = [x0 + 5 + 30.0 * i for i in range(4)]
    m.box(xs[0], xs[-1], 0, 7.6, z0 - 0.05, z0, DARK)
    leaves(m, z0, xs, 0, 7.4, TEAL, front=-1, post=DGREY)
    for a, b in zip(xs[:-1], xs[1:]):
        rows_z(m, -1, z0 - 0.25, a + 2, b - 2, 4.6, 6, 3.4, 1.8)
    roof_vents(m, [(-30, -20), (0, -20), (30, -20), (-30, 20), (0, 20), (30, 20)], H + 2.6)
    m.mirror_x()
    return m


# Hangar 18 (Edmonton Flying Club) -----------------------------------------------------------
def hangar18():
    """Edmonton Flying Club complex, heading 48 (front = NE / airside): two-storey club building with a glazed upper floor and
    balcony at the SE end (+X, next to the tower), the green hangar with two white sliding leaves, a white wing with the "18" roundel and
    a green / red-orange swoosh at the NW end, and a lower rear wing with a green base and a striped upper wall."""
    m = Mesh(textured=True)
    z0, z1 = -21.5, 21.5
    # club building: x 10..30
    m.box(10.0, 30.0, 0, 3.8, z0, z1, PANEL, top=False)
    rows_z(m, 1, z1, 11.5, 28.5, 0.9, 5, 2.4, 2.4)
    m.box(11.0, 29.0, 3.8, 7.4, z0 + 1.0, z1 - 2.0, DGREY)
    rows_z(m, 1, z1 - 2.0, 12.0, 28.0, 4.5, 6, 2.4, 2.0)
    m.box(9.0, 31.0, 7.4, 8.3, z0 - 0.5, z1 + 2.6, NAVY)  # deep roof fascia
    m.box(13.0, 27.0, 7.5, 8.15, z1 + 2.6, z1 + 2.68, RWHITE)  # EDMONTON FLYING CLUB sign strip
    for i in range(7):
        m.box(11.5 + i * 2.6, 11.7 + i * 2.6, 3.8, 5.0, z1 - 0.1, z1 + 2.5, CREAM)  # balcony posts
    m.box(11.0, 29.0, 4.9, 5.1, z1 + 2.4, z1 + 2.55, CREAM)
    m.box(11.0, 29.0, 3.7, 3.9, z1, z1 + 2.6, GREY)  # balcony slab
    # landside (-Z) face, Street View 31 Airport Rd (2012): white pilasters, club sign, blue "18" roundel upper right
    for i in range(8):
        m.box(10.5 + i * 2.6, 11.1 + i * 2.6, 0, 7.4, z0 - 0.25, z0, RWHITE)
    m.box(13.0, 23.0, 5.0, 6.0, z0 - 0.3, z0 - 0.25, RWHITE)
    m.box(13.5, 22.5, 5.35, 5.65, z0 - 0.33, z0 - 0.3, RED)
    number_disc(m, 27.0, 6.2, z0 - 0.25, (0, -1), 0.95, "18")
    # green hangar: x -15..10
    m.box(-15.0, 10.0, 0, 7.6, z0, z1, GREEN, top=False)
    m.gable(-15.0, 10.0, 7.6, 2.0, z0, z1, along_z=True, sw_roof=METAL, sw_wall=GREEN)
    m.box(-12.0, 8.0, 0, 6.6, z1, z1 + 0.05, DARK)
    xs = [-11.0, -1.0, 9.0 - 0.0]
    leaves(m, z1, xs, 0, 6.2, RWHITE, post=DGREY)
    louvres(m, z1, xs, [(4.6, 5.4)], sw=DGREY)
    m.box(-12.0, 9.0, 6.2, 6.6, z1, z1 + 0.28, DARK)
    # white wing with swoosh: x -30..-17
    m.box(-30.0, -17.0, 0, 9.6, z0, z1, RWHITE, top=True)
    m.box(-30.0, -17.0, 3.0, 3.5, z1, z1 + 0.06, GREEN)
    m.box(-30.0, -17.0, 3.7, 4.1, z1, z1 + 0.06, SALMON)
    number_disc(m, -20.0, 8.2, z1, (0, 1), 0.95, "18")
    m.box(-17.0, -15.0, 0, 8.4, z0, z1, CREAM)  # block pier between wing and hangar
    m.box(-17.0, -15.0, 0, 2.2, z1, z1 + 0.06, DARK)
    # rear wing: x 2..37, z -52..-21.5; green base with windows, striped upper wall
    m.box(2.0, 37.0, 0, 4.4, -52.0, z0, GREEN, top=False)
    cols = [CREAM, MAUVE, TAN, GREY]
    m.box(2.0, 37.0, 4.4, 9.6, -52.0, z0, CREAM, top=True)
    stripes(m, 2.0, 37.0, 4.4, 9.6, z0, 1, cols, axis="x")
    stripes(m, 2.0, 37.0, 4.4, 9.6, -52.0, -1, cols, axis="x")
    stripes(m, -52.0, z0, 4.4, 9.6, 37.0, 1, cols, axis="z")
    stripes(m, -52.0, z0, 4.4, 9.6, 2.0, -1, cols, axis="z")
    rows_x(m, 1, 37.0, -50.0, z0 - 2.0, 1.4, 7, 1.7, 1.4)
    rows_x(m, -1, 2.0, -50.0, z0 - 2.0, 1.4, 7, 1.7, 1.4)
    m.mirror_x()
    return m


# Hangar 38 / 39 (west side, doors face SE) ------------------------------------------------------
def hangar38():
    """Building 38: mustard-yellow ribbed hangar (heading 138, doors face SE) with a low-pitch gable roof, two big door panels with cream
    edge lines, tall narrow windows at one end, a canopy and the "38" roundel high on the front.  OSM 230718902: 68.8 x 64.0 m."""
    m = Mesh(textured=True)
    W, D, wh, rise = 68.8, 64.0, 12.5, 3.2
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, wh, z0, z1, MUSTARD, top=False)
    m.gable(x0, x1, wh, rise, z0, z1, along_z=True, sw_roof=DGREY, sw_wall=MUSTARD)
    for x in (x0 - 0.12, x1):
        m.box(x, x + 0.12, wh - 0.4, wh + 0.05, z0, z1, DGREY)
    # door panels with cream edge trim
    for a, b in ((-26.0, -4.0), (-2.0, 20.0)):
        m.box(a, b, 0, 10.4, z1, z1 + 0.12, MUSTARD)
        m.box(a, b, 10.3, 10.5, z1 + 0.1, z1 + 0.2, CREAM)
        m.box(a, a + 0.18, 0, 10.4, z1 + 0.1, z1 + 0.2, CREAM)
        m.box(b - 0.18, b, 0, 10.4, z1 + 0.1, z1 + 0.2, CREAM)
    # viewer-left (+x) end: tall narrow windows, personnel doors
    for xw in (30.5, 32.8):
        m.window((0, 0, 1), (xw, 2.0, z1), (1, 0, 0), 1.1, 4.4)
    m.box(26.0, 27.6, 0, 2.2, z1, z1 + 0.1, DGREY)
    m.box(29.0, 30.0, 0, 2.2, z1, z1 + 0.1, DGREY)
    number_disc(m, 6.5, 11.2, z1 + 0.12, (0, 1), 1.4, "38")  # big roundel high on the corner wall (Street View 2010)
    for sgn, xp in ((1, x1), (-1, x0)):  # tall narrow window banks along both long walls
        rows_x(m, sgn, xp, z0 + 4.0, z1 - 16.0, 3.5, 13, 0.9, 6.5)
    # long walls: plain, with a couple of doors
    for z in (-8.0, 14.0):
        m.box(x1, x1 + 0.1, 0, 2.2, z, z + 1.1, DGREY)
        m.box(x0 - 0.1, x0, 0, 2.2, z, z + 1.1, DGREY)
    roof_vents(m, [(0, -14), (0, 0), (0, 14)], wh + rise)
    m.mirror_x()
    return m


def hangar39():
    """Hangar 39 (user, 2026-10-21; photos 13207255803 and 13207268493 and Street View 26-28): OSM way 230718901 (107 x 90.5 m, heading 138,
    doors face SE).  Two tall pale-blue gabled hangars side by side with a 13 m gap, joined by a lower set-back middle block (roller door and
    two personnel doors, steel truss frame across the gap at the front) and a lower wing across the back.  Each bay's front is a recessed
    wall of white sliding leaves with two tiers of tan louvre panels, flanked by blue piers that project forward (the outer ones carry the
    door track).  Walls 14 m, ridge 17 m; "39" roundel position assumed."""
    m = Mesh(textured=True)
    W, D, wh, rise = 107.0, 90.5, 14.0, 3.0
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    bw, wing = 47.0, 12.0
    zb = z0 + wing  # bays run from the back wing to the front
    gx0, gx1 = x0 + bw, x1 - bw
    for bx0, bx1 in ((x0, x0 + bw), (x1 - bw, x1)):
        m.box(bx0, bx1, 0, wh, zb, z1, PBLUE, top=False)
        m.gable(bx0, bx1, wh, rise, zb, z1, along_z=True, sw_roof=METAL, sw_wall=PBLUE)
        xs = [bx0 + 4.0 + 6.5 * i for i in range(7)]
        m.box(xs[0], xs[-1], 0, 12.6, z1, z1 + 0.05, DARK)
        leaves(m, z1, xs, 0, 12.3, RWHITE, post=DGREY)
        louvres(m, z1, xs, [(3.6, 6.0), (8.6, 11.2)], sw=TAN)
        m.box(xs[0], xs[-1], 12.3, 12.8, z1, z1 + 0.5, DGREY)
        for px0, px1 in ((bx0, bx0 + 3.6), (bx1 - 3.0, bx1)):  # piers projecting past the door wall
            m.box(px0, px1, 0, wh + 0.4, z1, z1 + 1.1, PBLUE)
    # set-back middle block between the bays
    zm = z1 - 14.0
    m.box(gx0, gx1, 0, 11.0, zb, zm, PBLUE)
    m.box(gx0, gx1, 11.0, 11.3, zb, zm + 0.1, DGREY)
    m.box(gx0 + 2.0, gx0 + 7.0, 0, 4.2, zm, zm + 0.12, RWHITE)  # roller door
    for dx in (gx0 + 9.0, gx1 - 1.6):
        m.box(dx, dx + 1.1, 0, 2.2, zm, zm + 0.1, DGREY)
    # steel truss frame across the gap at the front
    for y in (13.2, 15.2, 17.0):
        m.box(gx0, gx1, y, y + 0.35, z1 + 0.5, z1 + 0.9, DGREY)
    for k in range(5):
        m.box(gx0 + 1.0 + k * 2.8, gx0 + 1.3 + k * 2.8, 13.2, 17.0, z1 + 0.5, z1 + 0.9, DGREY)
    # back wing across the full width
    m.box(x0, x1, 0, 10.0, z0, zb, PBLUE)
    m.box(x0, x1, 10.0, 10.4, z0 - 0.1, zb + 0.1, DGREY)
    rows_z(m, -1, z0, x0 + 3.0, x1 - 3.0, 6.0, 20, 2.4, 1.6)
    rows_z(m, -1, z0, x0 + 3.0, x1 - 3.0, 2.0, 12, 2.4, 1.6)
    for sgn, xp in ((1, x1), (-1, x0)):  # end walls
        rows_x(m, sgn, xp, zb + 4.0, z1 - 6.0, 9.0, 8, 1.6, 1.1)
        rows_x(m, sgn, xp, z0 + 2.0, zb - 2.0, 5.0, 3, 1.6, 1.2)
    number_disc(m, x1, 11.2, z1 - 14.0, (1, 0), 1.4, "39")
    roof_vents(m, [(-30, -10), (-30, 10), (-30, 28), (30, -10), (30, 10), (30, 28)], wh + rise)
    m.mirror_x()
    return m


# placement ----------------------------------------------------------------------------------
# name -> (title, builder, lat, lon, heading, footprint W (across front), D (depth), extra exclusion margin)
HANGARS = [
    ("cyxd_hangar4", "Hangar 4 (yellow, arched door, faces the runway, OSM 325273554)", hangar4, 53.573457, -113.508430, 270, 71.1, 33.5),
    ("cyxd_hangar5", "Hangar 5 (tan, bronze office, OSM 325270299)", hangar5, 53.572793, -113.508364, 270, 53.1, 43.3),
    ("cyxd_hangar6", "Hangar 6 (white and green, OSM 325267780)", hangar6, 53.572135, -113.508405, 270, 41.9, 46.2),
    ("cyxd_hangar7", "Hangar 7 (steel blue, OSM 325271251)", hangar7, 53.571617, -113.508378, 270, 36.4, 39.3),
    ("cyxd_hangar8", "Hangar 8 (pale blue-grey with end block, OSM 325268698)", hangar8, 53.570358, -113.508293, 270, 66.3, 52.9),
    ("cyxd_hangar11", "Hangar 11 (USAAF T3 barrel vault with annexes, OSM 325268748)", hangar11, 53.569251, -113.508228, 0, 86.3, 64.0),
    ("cyxd_hangar14", "Hangar 14 (Alberta Aviation Museum, OSM 230718920)", hangar14, 53.565714, -113.517130, 90, 100.0, 90.8),
    ("cyxd_hangar18", "Hangar 18 (Edmonton Flying Club complex, traced from 2014 imagery)", hangar18, 53.568740, -113.519699, 48, 60.0, 43.0),
    ("cyxd_hangar38", "Hangar 38 (mustard yellow, OSM 230718902)", hangar38, 53.573308, -113.529714, 138, 68.8, 64.0),
    ("cyxd_hangar39", "Hangar 39 (pale-blue double hall, OSM 230718901, beside Hangar 38)", hangar39, 53.574052, -113.528731, 138, 107.0, 90.5),
    ("cyxd_hangar40", "Hangar 40 (Canadian Helicopters, white roof of OSM 230718900)", hangar40, 53.575205, -113.529565, 318, 38.0, 25.0),
    ("cyxd_hangar3", "Hangar 3 (pale-blue flat-roofed hangar, traced from the 2014 imagery)", hangar3, 53.574710, -113.508533, 90, 81.6, 25.7),
    ("cyxd_hangar3_annex", "Hangar 3 tan block annex (south end)", hangar3_annex, 53.574273, -113.508547, 90, 15.9, 13.2),
    ("cyxd_bluehangar", "Dark-blue gabled hangar north of Hangar 3 (5 109 St NW, OSM 325272095)", bluehangar, 53.575629, -113.508404, 180, 20.7, 24.6),
    ("cyxd_hangar19", "Hangar 19 (low tan wings with a brick centre, 62-69 Airport Rd; traced from the 2014 imagery)", hangar19, 53.569158, -113.520582, 232, 65.0, 29.0),
    ("cyxd_gs_hut", "ILS glideslope hut with checkerboard paint (infield, 16/34 runway side; west-lineup photo)", gs_hut, 53.568983, -113.511000, 0, 8.0, 14.0),
    ("cyxd_hangar20", "Hangar 20 (Esso building, 83 Airport Rd NW; traced from the 2014 imagery)", hangar20, 53.569788, -113.521578, 228, 62.0, 58.0),
]
MARGIN = 6.0


def place(out, excl, modellib, footprint):
    """Write the hangar models and append their placements / build exclusions to the generator's lists."""
    for name, title, fn, lat, lon, hdg, W, D in HANGARS:
        guid = fn().save(modellib / name, name)
        out.append((title, "%.8f" % lat, "%.8f" % lon, "%g" % hdg, guid))
        excl.append((title, footprint("%.8f" % lat, "%.8f" % lon, "%g" % hdg, -W / 2 - MARGIN, W / 2 + MARGIN, -D / 2 - MARGIN, D / 2 + MARGIN)))
