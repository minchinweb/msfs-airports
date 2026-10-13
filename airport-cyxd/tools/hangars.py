"""CYXD hangars on the east line (4-8, 11), Hangar 14 (museum), Hangar 18 (Flying Club) and the west-side hangars 38 / 39.

Imported by gen_buildings.py (main() calls place()).  Footprints, centres and headings come from the OSM outlines as they were
mapped in 2016 (Overpass `date:` query) cross-checked against Esri World Imagery Wayback 2014-02 tiles; see
docs/cyxd/hangar-footprints.md.  Hangar 9 has no confirmed footprint yet: the model is built but NOT placed (see HANGAR9_*).

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
    """Pale-yellow ribbed gable-end hangar with a wide arched door opening (front, +Z).  Heading 0 (front faces north).
    Brick block on the east side (viewer-left of the front), orange-panelled neighbour on the west.  OSM 325273554: 33.5 x 71 m."""
    m = Mesh(textured=True)
    W, D, wh, rise = 33.5, 71.0, 7.2, 3.4
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, wh, z0, z1, YELLOWR, top=False)
    m.gable(x0, x1, wh, rise, z0, z1, along_z=True, sw_roof=METAL, sw_wall=YELLOWR)
    for x in (x0 - 0.12, x1):
        m.box(x, x + 0.12, wh - 0.5, wh + 0.05, z0, z1, RWHITE)
    a, hd, top, n = 14.0, 6.2, 8.4, 10
    pts = [(-a, 0, z1 + 0.06), (a, 0, z1 + 0.06)] + [(a * u, hd + (top - hd) * (1 - u * u), z1 + 0.06)
                                                    for u in [1 - 2 * k / n for k in range(n + 1)]]
    m.poly(pts, DARK, (0, 3, z1 - 4))
    for sx in (-a - 0.45, a):
        m.box(sx, sx + 0.45, 0, hd, z1, z1 + 0.14, RWHITE)
    m.box(-15.9, -14.8, 4.5, 6.7, z1, z1 + 0.12, RWHITE)  # white board behind the roundel
    number_disc(m, -15.35, 5.6, z1 + 0.12, (0, 1), 0.9, "4")
    m.box(2.0, 6.6, 8.55, 9.0, z1, z1 + 0.1, RWHITE)  # Government of Alberta sign, over the arch's shoulder
    m.box(2.2, 3.0, 8.65, 8.9, z1 + 0.1, z1 + 0.13, BLUE)
    m.box(x1, x1 + 10.0, 0, 4.6, z1 - 16.0, z1, BRICKD)
    m.box(x0 - 12.0, x0, 0, 9.0, z1 - 22.0, z1 - 2.0, SALMON)
    rows_x(m, -1, x0 - 12.0, z1 - 21.0, z1 - 3.0, 4.2, 4, 2.0, 1.6)
    roof_vents(m, [(0, -10), (0, 6), (0, 22)], wh + rise)
    m.mirror_x()
    return m


# Hangar 5 -----------------------------------------------------------------------------------
def hangar5():
    """Tan ribbed hangar, cream upper band, white sliding doors on the west gable end (+Z, heading 270), two-storey bronze
    curtain-wall office at the east (landside) end, "5" roundel high on the south wall.  OSM 325270299: 53.1 x 43.3 m."""
    m = Mesh(textured=True)
    W, D, wh, rise = 53.1, 43.3, 8.6, 3.2
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, wh - 2.4, z0, z1, TAN, top=False)
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


# Hangar 9 (placement not confirmed) -------------------------------------------------------------
def hangar9():
    """Hangar 9: pale hall with a full-width glazed sliding-door wall under a grey canopy on the front (+Z), a plain two-storey block at
    the left end (+X) and a taller ribbed annex at the right end (-X).  Dimensions are estimates; NOT placed until the footprint is known."""
    m = Mesh(textured=True)
    W, D, wh, rise = 52.0, 48.0, 9.4, 3.0
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    hx0, hx1 = -19.0, 18.0
    m.box(hx0, hx1, 0, wh, z0, z1, RWHITE, top=False)
    m.gable(hx0, hx1, wh, rise, z0, z1, along_z=True, sw_roof=METAL, sw_wall=RWHITE)
    xs = [-17.0 + 6.8 * i for i in range(6)]
    m.box(-17.4, 17.4, 0, 8.6, z1, z1 + 0.05, DARK)
    leaves(m, z1, xs, 0, 8.4, DOORG, post=DGREY)
    for y in (1.3, 3.1, 4.9, 6.7):
        for a, b in zip(xs[:-1], xs[1:]):
            rows_z(m, 1, z1 + 0.25, a + 0.4, b - 0.4, y, 3, 1.5, 1.5)
    m.box(-17.9, 17.9, 8.6, 9.0, z1, z1 + 2.6, GREY)  # canopy
    m.box(hx1, x1, 0, 6.8, z0, z1, RWHITE)  # plain two-storey block, left end
    rows_z(m, 1, z1, hx1 + 1.5, x1 - 1.5, 1.2, 2, 1.6, 1.8)
    rows_z(m, 1, z1, hx1 + 1.5, x1 - 1.5, 4.0, 2, 1.6, 1.8)
    m.box(x0, hx0, 0, 12.4, z0, z0 + 22.0, RWHITE)  # taller ribbed annex, right end
    m.box(x0 - 0.2, hx0, 12.4, 12.7, z0 - 0.2, z0 + 22.2, DGREY)
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
    W, D, wh, rise = 68.8, 64.0, 8.4, 3.0
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, wh, z0, z1, MUSTARD, top=False)
    m.gable(x0, x1, wh, rise, z0, z1, along_z=True, sw_roof=DGREY, sw_wall=MUSTARD)
    for x in (x0 - 0.12, x1):
        m.box(x, x + 0.12, wh - 0.4, wh + 0.05, z0, z1, DGREY)
    # door panels with cream edge trim
    for a, b in ((-26.0, -4.0), (-2.0, 20.0)):
        m.box(a, b, 0, 7.4, z1, z1 + 0.12, MUSTARD)
        m.box(a, b, 7.3, 7.5, z1 + 0.1, z1 + 0.2, CREAM)
        m.box(a, a + 0.18, 0, 7.4, z1 + 0.1, z1 + 0.2, CREAM)
        m.box(b - 0.18, b, 0, 7.4, z1 + 0.1, z1 + 0.2, CREAM)
    # viewer-left (+x) end: tall narrow windows, personnel doors
    for xw in (30.5, 32.8):
        m.window((0, 0, 1), (xw, 2.0, z1), (1, 0, 0), 1.1, 4.4)
    m.box(26.0, 27.6, 0, 2.2, z1, z1 + 0.1, DGREY)
    m.box(29.0, 30.0, 0, 2.2, z1, z1 + 0.1, DGREY)
    number_disc(m, 6.5, 7.6, z1, (0, 1), 0.95, "38")
    m.box(2.5, 10.5, 5.6, 5.8, z1, z1 + 1.8, DGREY)  # canopy under the roundel
    # long walls: plain, with a couple of doors
    for z in (-8.0, 14.0):
        m.box(x1, x1 + 0.1, 0, 2.2, z, z + 1.1, DGREY)
        m.box(x0 - 0.1, x0, 0, 2.2, z, z + 1.1, DGREY)
    roof_vents(m, [(0, -14), (0, 0), (0, 14)], wh + rise)
    m.mirror_x()
    return m


def hangar39():
    """Old PWA hangar (Hangar 39; later Spar Aerospace): pale-blue ribbed hangar, heading 138 (doors face SE), a tall main door bay and a
    lower second bay of white sliding leaves with louvre panels and green guide posts, white and mid-blue panelling, the "39" roundel on the
    corner wall, a two-storey wing on the rear (NW) side.  OSM 230718900: 56.0 x 79.0 m."""
    m = Mesh(textured=True)
    W, D = 56.0, 79.0
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    bx = -8.0  # boundary between the main bay (+x side, viewer-left) and the low bay (-x side)
    m.box(bx, x1, 0, 11.4, z0, z1, PBLUE, top=False)
    m.gable(bx, x1, 11.4, 3.2, z0, z1, along_z=True, sw_roof=METAL, sw_wall=PBLUE)
    m.box(x0, bx, 0, 8.4, z0, z1, PBLUE, top=False)
    m.gable(x0, bx, 8.4, 2.0, z0, z1, along_z=True, sw_roof=METAL, sw_wall=PBLUE)
    m.box(bx - 0.04, x1, 7.2, 11.4, z1, z1 + 0.1, RWHITE, top=False)  # white panel above the main door
    m.box(x0, bx, 0, 1.4, z1, z1 + 0.1, STEEL)  # mid-blue base band on the low bay
    # main bay: 36 m of tall leaves
    xs = [bx + 2.0 + 8.0 * i for i in range(5)]
    m.box(xs[0], xs[-1], 0, 10.0, z1, z1 + 0.05, DARK)
    leaves(m, z1, xs, 0, 9.7, RWHITE, post=GREEN)
    louvres(m, z1, xs, [(2.2, 4.0), (5.6, 7.4)], sw=TAN)
    m.box(xs[0], xs[-1], 9.7, 10.2, z1, z1 + 0.5, DGREY)
    # low bay: 16 m of leaves
    xs2 = [x0 + 2.0 + 4.0 * i for i in range(5)]
    m.box(xs2[0], xs2[-1], 0, 7.6, z1, z1 + 0.05, DARK)
    leaves(m, z1, xs2, 0, 7.3, RWHITE, post=GREEN)
    louvres(m, z1, xs2, [(1.8, 3.4), (4.4, 6.0)], sw=TAN)
    m.box(xs2[0], xs2[-1], 7.3, 7.8, z1, z1 + 0.45, DGREY)
    # roundel on the low bay's side wall near the front corner, steel truss over the bay gap
    number_disc(m, x0, 6.2, z1 - 5.0, (-1, 0), 0.95, "39")
    m.box(bx - 0.6, bx + 0.6, 8.4, 11.4, z1 + 0.2, z1 + 0.5, DGREY)
    # rear (NW) two-storey wing
    m.box(-22.0, 22.0, 0, 7.4, z0 - 10.0, z0, PBLUE, top=True)
    for y in (1.6, 4.6):
        rows_z(m, -1, z0 - 10.0, -22.0, 22.0, y, 14, 1.4, 1.3)
    m.box(-22.3, 22.3, 7.4, 7.8, z0 - 10.3, z0, DGREY)
    roof_vents(m, [(12, -20), (12, -5), (12, 10), (-18, -10), (-18, 8)], 14.4)
    m.mirror_x()
    return m


# placement ----------------------------------------------------------------------------------
# name -> (title, builder, lat, lon, heading, footprint W (across front), D (depth), extra exclusion margin)
HANGARS = [
    ("cyxd_hangar4", "Hangar 4 (yellow, arched door, OSM 325273554)", hangar4, 53.573457, -113.508430, 0, 33.5, 71.1),
    ("cyxd_hangar5", "Hangar 5 (tan, bronze office, OSM 325270299)", hangar5, 53.572793, -113.508364, 270, 53.1, 43.3),
    ("cyxd_hangar6", "Hangar 6 (white and green, OSM 325267780)", hangar6, 53.572135, -113.508405, 270, 41.9, 46.2),
    ("cyxd_hangar7", "Hangar 7 (steel blue, OSM 325271251)", hangar7, 53.571617, -113.508378, 270, 36.4, 39.3),
    ("cyxd_hangar8", "Hangar 8 (pale blue-grey with end block, OSM 325268698)", hangar8, 53.570358, -113.508293, 270, 66.3, 52.9),
    ("cyxd_hangar11", "Hangar 11 (USAAF T3 barrel vault with annexes, OSM 325268748)", hangar11, 53.569251, -113.508228, 0, 86.3, 64.0),
    ("cyxd_hangar14", "Hangar 14 (Alberta Aviation Museum, OSM 230718920)", hangar14, 53.565714, -113.517130, 90, 100.0, 90.8),
    ("cyxd_hangar18", "Hangar 18 (Edmonton Flying Club complex, traced from 2014 imagery)", hangar18, 53.568740, -113.519699, 48, 60.0, 43.0),
    ("cyxd_hangar38", "Hangar 38 (mustard yellow, OSM 230718902)", hangar38, 53.573308, -113.529714, 138, 68.8, 64.0),
    ("cyxd_hangar39", "Hangar 39 (old PWA hangar, OSM 230718900)", hangar39, 53.574982, -113.529363, 138, 56.0, 79.0),
]
# Hangar 9 has no confirmed position: the model is written to modelLib but not placed.  Fill in lat/lon/heading to place it.
HANGAR9_PLACEMENT = None  # e.g. (lat, lon, heading)
MARGIN = 6.0


def place(out, excl, modellib, footprint):
    """Write the hangar models and append their placements / build exclusions to the generator's lists."""
    for name, title, fn, lat, lon, hdg, W, D in HANGARS:
        guid = fn().save(modellib / name, name)
        out.append((title, "%.8f" % lat, "%.8f" % lon, "%g" % hdg, guid))
        excl.append((title, footprint("%.8f" % lat, "%.8f" % lon, "%g" % hdg, -W / 2 - MARGIN, W / 2 + MARGIN, -D / 2 - MARGIN, D / 2 + MARGIN)))
    guid9 = hangar9().save(modellib / "cyxd_hangar9", "cyxd_hangar9")
    if HANGAR9_PLACEMENT:
        lat, lon, hdg = HANGAR9_PLACEMENT
        out.append(("Hangar 9", "%.8f" % lat, "%.8f" % lon, "%g" % hdg, guid9))
        excl.append(("Hangar 9", footprint("%.8f" % lat, "%.8f" % lon, "%g" % hdg, -32.0, 32.0, -30.0, 30.0)))
