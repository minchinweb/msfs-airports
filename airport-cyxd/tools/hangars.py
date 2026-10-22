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
    arched door opening, "4" roundel and Government of Alberta sign from the Wikimedia photo are on that front (+Z) wall; that wall is the gable end
    (user, 2026-10-21): the ridge runs E-W back from the door wall.  Brick block at the north end (viewer-left of
    the front), orange-panelled neighbour at the south end.  OSM 325273554: 71 (N-S) x 33.5 m."""
    m = Mesh(textured=True)
    W, D, wh, rise = 71.1, 33.5, 9.0, 4.4
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, wh, z0, z1, YELLOWR, top=False)
    m.gable(x0, x1, wh, rise, z0, z1, along_z=True, sw_roof=METAL, sw_wall=YELLOWR)  # gable end = the west (door) wall (user, 2026-10-21)
    for x in (x0 - 0.12, x1):
        m.box(x, x + 0.12, wh - 0.5, wh + 0.05, z0, z1, RWHITE)
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
    roof_vents(m, [(0, -10), (0, 0), (0, 10)], wh + rise)
    m.mirror_x()
    return m


# Hangar 5 -----------------------------------------------------------------------------------
def hangar5():
    """Tan ribbed hangar, cream upper band, white sliding doors on the west gable end (+Z, heading 270), two-storey bronze
    curtain-wall office block on the south side (user), "5" roundel high on the south wall above it.  OSM 325270299: 53.1 x 43.3 m."""
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
    # office block on the SOUTH side (-X; user, 2026-10-21), 30 x 12 m, two storeys of bronze glazing
    m.box(x0 - 12.0, x0, 0, 6.4, -15.0, 15.0, BRONZE)
    for y in (0.9, 4.0):
        rows_x(m, -1, x0 - 12.0, -15.0, 15.0, y, 8, 2.5, 2.2)
    m.box(x0 - 12.4, x0, 6.4, 6.7, -15.4, 15.4, DGREY)
    m.box(x0 - 13.8, x0 - 12.0, 3.1, 3.4, -3.5, 3.5, DGREY)  # entrance canopy
    number_disc(m, x0, 7.7, 0.0, (-1, 0), 0.85, "5")  # high on the south wall, above the offices
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
    # landside (-Z, east, 109 St) office windows (Street View 2012, 109 St NW): a ground row and a ribbon of upper windows across the low wing,
    # end block and hall, two doors, the LAW OFFICE / AVIATION signs on the end block
    rows_z(m, -1, z0, wx0 + 1.5, hx1 - 1.5, 1.0, 16, 2.0, 1.6)
    rows_z(m, -1, z0, wx0 + 1.5, hx1 - 1.5, 3.9, 14, 3.2, 1.7)
    for dx in (-26.0, 12.0):
        m.box(dx, dx + 1.2, 0, 2.2, z0 - 0.08, z0, DGREY)
    rect_sign(m, -7.6, 8.3, z0 - 0.12, (0, -1), 7.6, 1.1, "lawoffice", 0.0, 0.5)
    rect_sign(m, 2.4, 7.0, z0 - 0.12, (0, -1), 5.6, 0.8, "lawoffice", 0.5, 1.0)
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
    oval_sign(m, ox, oy, oz + 0.12, (0, 1), 4.6, 2.0, "esso")  # texture from tools/make_signs.py: blue-rimmed white oval, red "Esso"
    number_disc(m, 10.5, 9.0, -a, (0, -1), 1.0, "20")  # airside roundel above the big door (user, 2026-10-21)
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
    W, D = 38.0, 46.0  # white part 38 wide; the hole in the aerial is 72 x 46 m (user, 2026-10-21), the blue-grey hall fills the rest
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
    # blue-grey gabled hall at the SE end of OSM 230718900, x -53..-19 (together 72 m)
    m.box(-53.0, -19.0, 0, 9.0, z0, z1, STEEL, top=False)
    m.gable(-53.0, -19.0, 9.0, 3.0, z0, z1, along_z=True, sw_roof=METAL, sw_wall=STEEL)
    m.pos = [(x + 17.0, y, z) for x, y, z in m.pos]  # centre the 72 m footprint on the origin
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
    # roof sign board and control cab stand on the annex roof (y 11.3); the roof vents and the cab were floating 0.3-0.9 m above it
    m.box(-26.0, 4.0, 11.3, 14.4, az0 + 0.4, az0 + 0.6, WHITE)
    rect_sign(m, -11.0, 12.85, az0 + 0.38, (0, -1), 28.0, 2.8, "nwi", 0.0, 0.5)  # NORTHWEST INDUSTRIES LTD. (1956 photo)
    rect_sign(m, -11.0, 3.8, az0 - 0.1, (0, -1), 26.0, 1.5, "nwi", 0.5, 1.0)  # COMMERCIAL AIRCRAFT SERVICE on the second-floor band
    m.box(-9.0, -4.0, 11.3, 14.6, az0 + 6.0, az0 + 11.0, DGREY)  # control cab
    m.box(-9.1, -3.9, 12.4, 13.9, az0 + 5.9, az0 + 11.1, GLASS)
    m.box(-9.4, -3.6, 14.6, 14.9, az0 + 5.6, az0 + 11.4, DGREY)
    # landside (east, 109 St) fire escape on the annex (11094273884): two white landings with green doors, a steel ladder and handrails
    fz0 = az0 + 4.0
    for ly in (3.9, 7.2):
        m.box(ax1, ax1 + 1.7, ly, ly + 0.15, fz0, fz0 + 2.2, WHITE)
        m.box(ax1 + 1.6, ax1 + 1.7, ly + 0.15, ly + 1.1, fz0, fz0 + 2.2, WHITE)  # rail along the outer edge
        m.box(ax1, ax1 + 0.06, ly + 0.15, ly + 2.3, fz0 + 0.5, fz0 + 1.5, GREEN)  # door onto the landing
    for rz in (fz0 + 0.3, fz0 + 0.9):
        m.box(ax1 + 1.45, ax1 + 1.55, 0, 7.4, rz, rz + 0.06, DGREY)  # ladder rails
    for k in range(24):
        m.box(ax1 + 1.45, ax1 + 1.55, 0.3 + k * 0.3, 0.34 + k * 0.3, fz0 + 0.3, fz0 + 0.96, DGREY)  # rungs
    m.box(ax1, ax1 + 0.06, 0, 2.2, az0 + 9.0, az0 + 10.0, GREEN)  # ground-floor door
    # east wing: two storeys, ribbon windows, taller stair tower at its south end
    m.box(26.0, 43.15, 0, 8.6, -20.0, z1, WHITE, top=True)
    m.box(25.8, 43.35, 8.6, 8.9, -20.2, z1 + 0.2, GREEN)
    for y in (1.4, 5.0):
        rows_x(m, 1, 43.15, -18.0, z1 - 2.0, y, 10, 1.5, 1.8)
    m.box(36.0, 43.15, 8.9, 13.5, -20.0, -9.0, WHITE)
    # west annex
    m.box(-43.15, bx0, 0, 6.0, -30.0, -4.0, WHITE)
    rows_x(m, -1, -43.15, -28.0, -6.0, 2.4, 5, 1.2, 1.5)
    for vx, vz in ((-12, -10), (-12, 6), (10, -10), (10, 6)):  # sit on the barrel roof (was a flat 13.8 m, up to 0.9 m above it)
        roof_vents(m, [(vx, vz)], arch(vx) - 0.15)
    m.mirror_x()
    return m


# Hangar 14 (Alberta Aviation Museum) ----------------------------------------------------------
def hangar14():
    """Hangar 14 (BCATP 1941, Alberta Aviation Museum): white horizontal-siding upper band over a dark teal-green lower wall with
    glazed panes.  The three big apron door bays are on the SOUTH gable end (+Z, heading 180, toward the road; user 2026-10-21), the
    museum entrance with its teal canopy and glazed band on the east wall (-X).  OSM 230718920: 90.8 (E-W) x 100 (N-S) m."""
    m = Mesh(textured=True)
    W, D, H = 90.8, 100.0, 8.8
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, 4.4, z0, z1, TEAL, top=False)
    m.box(x0, x1, 4.4, H, z0, z1, WHITE, top=True)
    m.box(x0 - 0.2, x1 + 0.2, H, H + 0.5, z0 - 0.2, z1 + 0.2, TEAL)
    m.gable(x0, x1, H + 0.5, 2.6, z0, z1, along_z=True, sw_roof=LROOF, sw_wall=WHITE)
    # south gable end: three door bays
    xs = [x0 + 4.9 + 27.0 * i for i in range(4)]
    m.box(xs[0], xs[-1], 0, 7.6, z1, z1 + 0.05, DARK)
    leaves(m, z1, xs, 0, 7.4, TEAL, front=1, post=DGREY)
    for a, b in zip(xs[:-1], xs[1:]):
        rows_z(m, 1, z1 + 0.25, a + 2, b - 2, 4.6, 6, 3.4, 1.8)
    # east wall (-X): glazed band, sign bars, canopy, entrance (was the "front" at heading 90; z = old x)
    rows_x(m, -1, x0, z0 + 3, z1 - 3, 1.0, 14, 4.2, 2.9)
    for a, b in ((-24, -8), (-4, 8), (12, 26)):
        m.box(x0 - 0.12, x0, 5.9, 7.1, a, b, TEAL)
    m.box(x0 - 3.2, x0, 3.5, 3.8, -26.0, -14.0, TEAL)  # entrance canopy
    m.box(x0 - 3.2, x0 - 3.0, 3.8, 4.1, -25.5, -14.5, WHITE)
    m.box(x0 - 0.15, x0, 0, 3.0, 14.0, 26.0, DGREY)
    for y in (0.9, 2.1):
        rows_x(m, -1, x0 - 0.15, 14.5, 25.5, y, 4, 2.0, 0.9)
    # west wall (+X) and north end: plain glazed bands
    rows_x(m, 1, x1, z0 + 3, z1 - 3, 1.0, 14, 4.2, 2.9)
    rows_z(m, -1, z0, x0 + 3, x1 - 3, 1.0, 12, 4.2, 2.9)
    roof_vents(m, [(-20, -30), (-20, 0), (-20, 30), (20, -30), (20, 0), (20, 30)], H + 2.6)
    m.mirror_x()
    return m


# Hangar 18 (Edmonton Flying Club) -----------------------------------------------------------
def hangar18():
    """Edmonton Flying Club complex, rebuilt (user, 2026-10-21) as THREE BLOCKS stacked from the road to the apron, like wings stuck together.
    Frame (before the shift and mirror): +Z = bearing 48 (NE, away from Airport Rd), +X = bearing 138 (SE, toward the tower); the shift at
    the end puts the origin at the centre of the whole 70 x 84 m footprint.  Footprints are from the 2014 Wayback aerial (about 0.7 m / px,
    docs/cyxd/footprints/hangar18-three-blocks.png): shadows and lit wall edges give A and B well, C is the least certain.
      C  landside club block, x -20..44, z -62..-49 (13 m deep, the narrowest): long white pilastered wall on Airport Rd with dark window
         slots, the FLYING CLUB entrance, a taller glazed club room at the SE end with a roof overhang and a viewing deck over the
         lower ground floor, looking toward the tower; the "18" roundel on the landside wall (Flickr 11094398653, Street View 31 / 50 Airport Rd).
      B  middle block, x -12..40, z -49..-17: teal base with small windows under a striped (cream / mauve / tan / grey) upper wall, a cream
         block pier with a door at its NE end (Flickr 11094307134).
      A  airside block, x -26..27, z -17..22: the olive-green hangar (two white leaves on the SE face, black band above) then a cream
         pier with a door and the long white wing with the swoosh and the "18" at its NE corner (airside video, 11165054745)."""
    m = Mesh(textured=True)
    # ---- A: airside block -------------------------------------------------------------------
    ax0, ax1, az0, az1, zp = -26.0, 27.0, -17.0, 22.0, 1.5
    m.box(ax0, ax1, 0, 8.6, az0, zp - 1.5, GREEN, top=False)  # olive hangar z -17..0
    m.box(ax0 - 0.1, ax1 + 0.1, 8.6, 8.9, az0, zp - 1.5, DGREY)
    m.box(ax0, ax1 + 0.1, 0, 8.6, zp - 1.5, zp, CREAM)  # block pier between the hangar and the wing (z 0..1.5)
    m.box(ax0, ax1, 0, 9.6, zp, az1, RWHITE, top=False)  # white wing z 1.5..22
    m.box(ax0 - 0.1, ax1 + 0.1, 9.6, 9.9, zp, az1 + 0.1, DGREY)
    xd = ax1 + 0.04
    m.box(xd, xd + 0.08, 0, 6.4, -14.5, -2.5, DARK)  # door opening
    for z0_ in (-14.5, -8.5):
        m.box(xd + 0.08, xd + 0.28, 0, 6.2, z0_ + 0.05, z0_ + 5.95, RWHITE)  # two sliding leaves
        for k in range(3):
            m.window((1, 0, 0), (xd + 0.28, 4.7, z0_ + 0.5 + k * 1.8), (0, 0, 1), 1.3, 0.5)  # small windows near the top of each leaf
    m.box(xd + 0.08, xd + 0.4, 6.2, 6.8, -15.0, -2.0, DARK)  # black band over the doors
    m.window((1, 0, 0), (ax1 + 0.1, 0.0, -1.1), (0, 0, 1), 0.9, 2.1)  # pier personnel door
    # swoosh on the white wing's SE face: grey-blue band with a thin red line, curving up toward the SW end
    for y0, y1, sw in ((5.6, 6.2, STEEL), (5.2, 5.4, RED)):
        m.box(ax1, ax1 + 0.05, y0, y1, 6.0, 20.0, sw)
        m.poly([(ax1 + 0.05, y0, 6.0), (ax1 + 0.05, y1, 6.0), (ax1 + 0.05, y1 + 2.4, 3.2), (ax1 + 0.05, y0 + 2.4, 3.2)], sw, (ax1 - 5, y0, 5.0))
    number_disc(m, ax1, 8.0, 20.4, (1, 0), 0.95, "18")  # NE corner of the SE face
    # ---- B: middle block --------------------------------------------------------------------
    bx0, bx1, bz0, bz1 = -12.0, 40.0, -49.0, -17.0
    m.box(bx0, bx1, 0, 4.6, bz0, bz1, TEAL, top=False)
    m.box(bx0, bx1, 4.6, 9.6, bz0, bz1, CREAM, top=True)
    cols = [CREAM, MAUVE, TAN, GREY]
    stripes(m, bz0, bz1 - 6.0, 4.6, 9.6, bx1, 1, cols, axis="z")
    stripes(m, bz0, bz1, 4.6, 9.6, bx0, -1, cols, axis="z")
    m.box(bx0 - 0.1, bx1 + 0.1, 9.6, 9.9, bz0 - 0.1, bz1 + 0.1, DGREY)
    rows_x(m, 1, bx1, bz0 + 1.0, bz1 - 8.0, 1.6, 7, 1.6, 0.9)  # small windows along the teal base
    rows_x(m, -1, bx0, bz0 + 3.0, bz1 - 3.0, 1.6, 7, 1.6, 0.9)
    m.box(bx1, bx1 + 0.12, 4.0, 4.2, bz0, bz1 - 6.0, DGREY)  # eave line between base and stripes
    m.box(bx1 - 12.0, bx1 + 0.1, 0, 8.4, bz1 - 6.0, bz1, CREAM)  # cream block pier at the NE end, x 28..40
    m.window((1, 0, 0), (bx1 + 0.1, 0.0, bz1 - 4.5), (0, 0, 1), 0.9, 2.1)  # its personnel door
    m.box(bx1 + 0.1, bx1 + 0.16, 3.5, 4.8, bz1 - 3.5, bz1 - 1.3, BLUE)  # small blue sign
    roof_vents(m, [(0, -40), (15, -30), (28, -44)], 9.9)
    # ---- C: landside club block -------------------------------------------------------------
    n_c = len(m.pos)
    cx0, cx1, cz0, cz1 = -20.0, 44.0, -62.0, -49.0
    wing1 = 28.0  # long wing x -20..28 (two storeys, 6.8 m); club room x 28..40 (8.0 m); ground-floor block to x 44 under the deck
    m.box(cx0, wing1, 0, 6.8, cz0, cz1, RWHITE, top=False)
    m.box(cx0 - 0.1, wing1, 6.8, 7.6, cz0 - 0.1, cz1, BEIGE)  # tan corrugated fascia
    m.box(wing1, 40.0, 0, 8.0, cz0, cz1, RWHITE, top=False)
    m.box(wing1 - 0.1, 43.0, 8.0, 8.9, cz0 - 1.5, cz1 + 0.1, BEIGE)  # roof overhang over the deck, beige fascia
    # landside (SW, -Z) wall: pilasters with dark window slots (two storeys), entrance with canopy
    for k in range(13):
        xk = -17.0 + k * 3.7
        if 8.0 < xk < 20.0 or xk > 25.0:
            continue
        m.window((0, 0, -1), (xk, 0.9, cz0), (1, 0, 0), 1.1, 5.4)
    m.box(13.0, 17.4, 0, 2.3, cz0 - 0.05, cz0, DGREY)  # entrance doors
    m.box(12.4, 18.0, 2.5, 2.75, cz0 - 1.6, cz0, WHITE)  # canopy
    m.box(18.2, 20.2, 0, 3.0, cz0 - 0.08, cz0, BLUE)  # mural panels beside the door
    m.box(10.2, 12.2, 0, 3.0, cz0 - 0.08, cz0, PANEL)
    rect_sign(m, 15.2, 4.6, cz0 - 0.1, (0, -1), 4.4, 1.7, "efc", 0.5, 1.0)  # EDMONTON FLYING CLUB board over the entrance
    m.box(-9.6, -7.8, 0, 2.2, cz0 - 0.1, cz0, DGREY)  # CAFETERIA door, far end of the wall
    m.box(-9.9, -7.5, 2.4, 3.0, cz0 - 0.1, cz0, RED)
    number_disc(m, 28.7, 6.6, cz0, (0, -1), 0.95, "18")  # landside roundel above the yellow louvre panel
    m.box(28.0, 30.2, 2.2, 5.0, cz0 - 0.1, cz0, YELLOW)
    # club room (x 28..40): glazed upper floor on the SE face and the SW face
    rows_x(m, 1, 40.0, cz0 + 1.0, cz1 - 1.0, 4.4, 6, 1.7, 2.8)
    rows_z(m, -1, cz0, wing1 + 3.0, 39.0, 4.4, 3, 2.6, 2.8)
    m.box(40.0, 44.0, 0, 3.4, cz0, cz1, RWHITE)  # lower ground-floor block under the deck
    rows_x(m, 1, 44.0, cz0 + 1.5, cz1 - 1.5, 1.2, 3, 2.2, 1.4)
    # viewing deck: slab, white railing, over the lower block, facing the tower
    m.box(40.0, 44.0, 3.4, 3.8, cz0, cz1, GREY)
    for z in [cz0 + 0.2 + 0.8 * k for k in range(int((cz1 - cz0) / 0.8))]:
        m.box(43.8, 43.9, 3.8, 4.8, z, z + 0.06, CREAM)
    m.box(43.75, 43.95, 4.75, 4.85, cz0, cz1, CREAM)
    for x in (41.0, 42.5):
        m.box(x, x + 0.06, 3.8, 4.8, cz0, cz0 + 0.06, CREAM)
        m.box(x, x + 0.06, 3.8, 4.8, cz1 - 0.06, cz1, CREAM)
    m.box(40.0, 40.12, 7.0, 7.7, cz0, cz1, DGREY)  # fascia the lettering sits on
    rect_sign(m, 40.14, 7.35, -55.5, (1, 0), 12.0, 0.7, "efc", 0.0, 0.5)  # EDMONTON FLYING CLUB on the club-room fascia, facing the tower
    roof_vents(m, [(-5, -55), (10, -55)], 7.6)
    # user, 2026-10-21: the club block lies 18 m further toward the tower (SE) than first traced (x -2..62)
    m.pos[n_c:] = [(x + 18.0, y, z) for x, y, z in m.pos[n_c:]]
    # shift the origin to the middle of the whole footprint (x -26..44, z -62..22)
    m.pos = [(x - 18.0, y, z + 20.0) for x, y, z in m.pos]
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
    number_disc(m, 0.0, 10.7, z0, (0, -1), 1.4, "38")  # landside roundel on the back wall (user, 2026-10-21)
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
    number_disc(m, 0.0, 8.6, zm + 0.12, (0, 1), 1.4, "39")  # airside roundel on the set-back middle block above the roller door (user, 2026-10-21)
    number_disc(m, x0 + bw / 2, 12.3, zb, (0, -1), 1.3, "39")  # landside roundel high on the back wall above the low wing
    roof_vents(m, [(-30, -10), (-30, 10), (-30, 28), (30, -10), (30, 10), (30, 28)], wh + rise)
    m.mirror_x()
    return m


# Old terminal (Building 21) and its parking garage -------------------------------------------
def hangar21():
    """Old terminal, "Hangar 21" (OSM way 230718907, later Amiskwaciy Academy), traced from the 2017 Wayback zoom-19 imagery
    (docs/cyxd/footprints/terminal21-2017-overlay.png).  Frame: +Z = bearing 51 (apron side, NE), +X = bearing 141 (SE) along the building.
    North wing (tall dark-brick block with the "21" roundel on its landside face), a two-storey spine along the apron with a glazed ground
    floor and a canopy, a lower cream landside wing with a glazed entrance, the taller SE block, and a covered walkway to the garage
    (Street View 13, 14, 17, 18)."""
    m = Mesh(textured=True)
    # north wing x -86..-51.5, z -8..17
    m.box(-86.0, -51.5, 0, 9.5, -8.0, 17.0, BRICKD, top=False)
    m.box(-86.2, -51.3, 9.5, 10.0, -8.2, 17.2, DGREY)
    rows_z(m, -1, -8.0, -84.0, -53.5, 2.4, 6, 2.2, 1.6)
    rows_z(m, -1, -8.0, -84.0, -53.5, 6.2, 6, 2.2, 1.6)
    rows_z(m, 1, 17.0, -84.0, -53.5, 2.4, 6, 2.2, 1.6)
    rows_z(m, 1, 17.0, -84.0, -53.5, 6.2, 6, 2.2, 1.6)
    rows_x(m, -1, -86.0, -6.0, 15.0, 4.0, 4, 2.2, 1.8)
    for x in (-82.0, -77.0, -72.0, -67.0, -62.0, -57.0):  # red-brown vertical fins on the landside face (Street View 13)
        m.box(x, x + 0.6, 0, 9.5, -8.5, -8.0, RED)
    number_disc(m, -60.0, 7.4, -8.5, (0, -1), 1.3, "21")
    m.box(-78.0, -58.0, 0, 3.2, -8.6, -8.0, GLASS)  # entrance glazing
    # spine along the apron x -52..72, z -4..13, two storeys; glazed ground floor behind columns
    m.box(-52.0, 72.0, 0, 7.6, -4.0, 13.0, BRICKD, top=False)
    m.box(-52.2, 72.2, 7.6, 8.1, -4.2, 13.2, DGREY)
    for x in range(-48, 71, 6):
        rows_z(m, 1, 13.0, x, x + 5.0, 1.0, 1, 4.0, 2.6)
        rows_z(m, 1, 13.0, x, x + 5.0, 4.6, 1, 4.0, 1.6)
    m.box(-48.0, 70.0, 3.9, 4.3, 13.0, 16.0, CREAM)  # apron-side canopy
    for x in range(-46, 70, 12):
        m.box(x, x + 0.5, 0, 3.9, 15.4, 15.9, CREAM)
    # lower cream landside wing x -50..25, z -21..-4 with a glazed entrance bay
    m.box(-50.0, 25.0, 0, 4.6, -21.0, -4.0, CREAM, top=False)
    m.box(-50.2, 25.2, 4.6, 5.0, -21.2, -3.8, DGREY)
    rows_z(m, -1, -21.0, -48.0, 6.0, 1.2, 12, 2.4, 1.8)
    m.box(-12.0, 4.0, 0, 3.6, -21.1, -21.0, GLASS)
    m.box(-14.0, 6.0, 3.6, 3.9, -24.0, -21.0, CREAM)  # entrance canopy
    # inner courtyard roof between the wings
    m.box(-40.0, 20.0, 5.0, 5.2, -21.0, -4.0, DGREY)
    # SE block x 25..76, z -19..13, taller
    m.box(25.0, 76.0, 0, 9.5, -19.0, 13.0, BRICKD, top=False)
    m.box(24.8, 76.2, 9.5, 10.0, -19.2, 13.2, DGREY)
    for y in (2.0, 6.0):
        rows_z(m, -1, -19.0, 27.0, 74.0, y, 8, 3.0, 1.6)
        rows_x(m, 1, 76.0, -17.0, 11.0, y, 5, 3.0, 1.6)
    m.box(24.0, 30.0, 0, 8.0, 13.0, 13.1, DARK)
    roof_vents(m, [(-70, 4), (-65, 10), (0, 5), (10, 8), (50, 0), (60, 6)], 10.0)
    # covered walkway from the spine's SW side toward the garage, on piers
    m.box(-41.0, -34.0, 5.5, 8.5, -52.0, -21.0, BRICKD)
    m.box(-41.2, -33.8, 8.5, 8.8, -52.2, -20.8, DGREY)
    for z in (-46.0, -36.0):
        for x in (-40.6, -34.6):
            m.box(x, x + 0.6, 0, 5.5, z, z + 0.6, CREAM)
    # centre the whole footprint (x -86..76, z -52..17) on the origin
    m.pos = [(x + 5.0, y, z + 17.5) for x, y, z in m.pos]
    m.mirror_x()
    return m


def garage22():
    """Terminal parking garage ("22" roundel), three decks stepping down toward the SE end, brown horizontal cladding on an open ground floor
    of precast piers, stair tower at the NW end (Street View 14-18).  Footprint from the 2017 Wayback zoom-19 imagery:
    about 100 x 72 m, +Z = bearing 58 (NE, toward the terminal), +X = bearing 148."""
    m = Mesh(textured=True)
    x0, x1, z0, z1 = -50.0, 50.0, -36.0, 36.0
    m.box(x0 + 0.6, x1 - 0.6, 0, 3.0, z0 + 0.6, z1 - 0.6, DARK, top=False)  # open ground floor
    for i in range(12):  # precast piers on both long faces and the ends
        x = x0 + 0.5 + i * (x1 - x0 - 1.4) / 11
        for z in (z0, z1 - 0.8):
            m.box(x, x + 0.9, 0, 3.0, z, z + 0.8, CREAM)
    for k in range(1, 8):
        z = z0 + k * (z1 - z0) / 8
        for x in (x0, x1 - 0.8):
            m.box(x, x + 0.8, 0, 3.0, z - 0.4, z + 0.4, CREAM)
    # tiers: (x_start, x_end, top height)
    for xa, xb, h in ((x0, 30.0, 10.4), (30.0, 40.0, 7.2), (40.0, x1, 4.0)):
        m.box(xa, xb, 3.0, h, z0, z1, BRONZE, top=True)
        m.box(xa - 0.1, xb + 0.1, h, h + 0.35, z0 - 0.1, z1 + 0.1, TAN)  # concrete cap
        y = 3.0
        while y + 3.3 <= h + 0.01:
            m.box(xa - 0.15, xb + 0.15, y + 2.55, y + 3.0, z0 - 0.15, z1 + 0.15, TAN)  # slab edge beam
            y += 3.3
        for yy in [3.0 + 3.3 * j + 0.9 for j in range(int((h - 3.0) / 3.3 + 0.01))]:
            n = max(1, int((xb - xa) / 9))
            rows_z(m, -1, z0, xa + 0.5, xb - 0.5, yy, n, 6.0 if xb - xa > 30 else 4.0, 1.0)
            rows_z(m, 1, z1, xa + 0.5, xb - 0.5, yy, n, 6.0 if xb - xa > 30 else 4.0, 1.0)
    for yy in (3.9, 7.2):
        rows_x(m, -1, x0, z0 + 3.0, z1 - 3.0, yy, 6, 7.0, 1.0)
    # stair tower at the NW end (angled wall in the photos) and the "22" roundel at the roof corner
    m.box(-30.0, -22.0, 10.4, 14.5, 10.0, 18.0, TAN)
    m.box(-30.2, -21.8, 14.5, 14.8, 9.8, 18.2, DGREY)
    m.box(-52.0, -50.0, 10.4, 12.0, 20.0, 27.0, CREAM)
    number_disc(m, -40.0, 8.0, z1 + 0.2, (0, 1), 1.4, "22")
    m.box(0.0, 3.0, 10.75, 12.0, -3.0, 3.0, DGREY)  # roof lift housing
    m.mirror_x()
    return m


# Second hangar by Kingsway ("orange", 1930s-1982) --------------------------------------------
# Proper position: centre 53.56945, -113.52610 (about +-50 m, placed on the 1944 aerial from the 118 Ave / Kingsway junction; docs/cyxd/open-questions.md),
# heading 57.78 (front to the NE apron), footprint 70 x 44 m.  At that spot the exclusion polygon (footprint + 6 m) also removes the Chateau Nova Hotel
# (OSM way 230718905, 109 x 88 m, its NE corner reaches into the footprint).  To keep the hotel the whole model is moved ORANGE_SHIFT_NE_M metres toward
# the apron, which also puts the exclusion 3 m short of Blue (the 1938 hangar).  To bring it back to its proper position set ORANGE_SHIFT_NE_M = 0.0
# (and accept losing the hotel, or rebuild the hotel as a model).  The size itself is the proper 70 x 44 m; for the larger 1944-aerial reading
# (about 70 x 55 m) raise D in the HANGARS row and the z extents in hangar_second(), and move the shift up by half the difference.
ORANGE_LAT, ORANGE_LON, ORANGE_HDG = 53.56945, -113.52610, 57.78
ORANGE_SHIFT_NE_M = 14.0


def _orange_pos():
    a = math.radians(ORANGE_HDG)
    return (ORANGE_LAT + ORANGE_SHIFT_NE_M * math.cos(a) / 111200.0, ORANGE_LON + ORANGE_SHIFT_NE_M * math.sin(a) / 66170.0)


def hangar_second():
    """The second barrel-vault hangar beside Kingsway, still standing in 1982 (user's "orange"; postcard PC013987 far hangar, City Archives ET-28-900 of 1982,
    the 1944 aerial).  Massing only: a pale two-storey flat-roofed wing with ribbon windows and a red band at the left, brick towers flush with the front at
    the ends of the barrel-vault hall, the hall with a dark roof and a big door opening under its arched front, a low service block behind the wing.
    Frame: +Z = front (NE, apron), +X = right of the front; footprint x -35..35, z -22..22.  Details of the wing and the towers are guesses."""
    m = Mesh(textured=True)
    zf, zb = 22.0, -22.0
    # wing x -35..-15: pale cream, two storeys, flat roof, red band under the parapet
    m.box(-35.0, -15.0, 0, 7.4, -4.0, zf, CREAM, top=False)
    m.box(-35.2, -14.8, 7.4, 7.8, -4.2, zf + 0.2, DGREY)
    m.box(-35.0, -15.0, 6.2, 6.7, zf, zf + 0.1, RED)
    for y in (1.4, 4.0):
        rows_z(m, 1, zf, -35.0, -15.0, y, 5, 2.4, 1.5)
        rows_x(m, -1, -35.0, -2.0, zf - 1.0, y, 4, 2.4, 1.5)
    m.box(-28.0, -26.0, 0, 2.3, zf, zf + 0.1, DARK)  # entrance
    m.box(-35.0, -15.0, 0, 4.4, zb, -4.0, CREAM, top=True)  # low service block behind the wing
    # barrel-vault hall x -9..29 (span 38), z -22..22
    xh0, xh1, wall, rise = -9.0, 29.0, 7.0, 5.5
    m.box(xh0, xh1, 0, wall, zb, zf, CREAM, top=False)
    n = 16
    prof = [(-math.cos(math.pi * i / n) * (xh1 - xh0) / 2 + (xh0 + xh1) / 2, wall + math.sin(math.pi * i / n) * rise) for i in range(n + 1)]
    for i in range(n):
        (xa, ya), (xb, yb) = prof[i], prof[i + 1]
        m.poly([(xa, ya, zb), (xb, yb, zb), (xb, yb, zf), (xa, ya, zf)], METAL, (0, wall - 3, 0))
    for z in (zf, zb):
        m.poly([(xh0, wall, z)] + [(x, y, z) for x, y in prof] + [(xh1, wall, z)], CREAM, (0, wall, 0))
    m.box(-6.0, 26.0, 0, 6.6, zf, zf + 0.1, DARK)  # door opening
    for k in range(4):
        m.box(-5.9 + k * 8.0, 1.9 + k * 8.0, 0, 6.4, zf + 0.1, zf + 0.3, DOORG)
    window_row(m, xh0 + 0.5, xh1 - 0.5, 7.4, zf, 9, 1.4, 1.2, (0, 0, 1), "x")
    for sgn in (-1, 1):
        for i in range(6):
            m.window((sgn, 0, 0), (xh0 if sgn < 0 else xh1, 3.2, zb + 4 + i * 6.5), (0, 0, 1), 3.0, 1.6)

    def brick_tower(x0, x1, h, floors):
        z0 = zf - (x1 - x0)
        m.box(x0, x1, 0, h, z0, zf, BRICKD, top=False)
        m.box(x0 - 0.2, x1 + 0.2, h, h + 0.5, z0 - 0.2, zf + 0.2, CREAM)
        for f in range(floors):
            y = 1.6 + f * (h - 3.0) / floors
            m.window((0, 0, 1), (x0 + 1.0, y, zf), (1, 0, 0), x1 - x0 - 2.0, 1.8)
            m.window((0, 0, -1), (x0 + 1.0, y, z0), (1, 0, 0), x1 - x0 - 2.0, 1.8)
    brick_tower(-15.0, -9.0, 13.0, 3)
    brick_tower(29.0, 35.0, 15.0, 4)
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
    ("cyxd_hangar14", "Hangar 14 (Alberta Aviation Museum, OSM 230718920)", hangar14, 53.565714, -113.517130, 180, 90.8, 100.0),
    ("cyxd_hangar18", "Hangar 18 (Edmonton Flying Club complex, traced from 2014 imagery)", hangar18, 53.568498, -113.519742, 48, 88.0, 84.0),
    ("cyxd_hangar38", "Hangar 38 (mustard yellow, OSM 230718902)", hangar38, 53.573308, -113.529714, 138, 68.8, 64.0),
    ("cyxd_hangar39", "Hangar 39 (pale-blue double hall, OSM 230718901, beside Hangar 38)", hangar39, 53.574052, -113.528731, 138, 107.0, 90.5),
    ("cyxd_hangar40", "Hangar 40 (Canadian Helicopters, white roof of OSM 230718900)", hangar40, 53.575004, -113.529385, 228, 72.0, 46.0),
    ("cyxd_hangar21", "Hangar 21 (old terminal, OSM 230718907; traced from the 2017 imagery)", hangar21, 53.570940, -113.523178, 51, 162.0, 70.0),
    ("cyxd_garage22", "Terminal parking garage (22; traced from the 2017 imagery)", garage22, 53.570567, -113.524067, 58, 100.0, 72.0),
    ("cyxd_hangar_second", "Second hangar by Kingsway (1930s-1982; barrel vault, pale wing, brick towers)", hangar_second, *_orange_pos(), ORANGE_HDG, 70.0, 44.0),
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
