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
def fmesh():
    """A textured mesh whose windows get a projecting grey surround and sill (user, 2026-10-21: the windows looked painted flat on the wall)."""
    m = Mesh(textured=True)
    m.frame = GREY
    return m


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


def pane_x(m, sgn, xplane, zc, y0, w, h, cols=2, rows=2, fw=0.08, sw=TEAL, depth=0.1):
    """Framed window on a wall with outward normal (sgn, 0, 0): dark glass, a frame of width fw and cols x rows panes (zc = centre along z)."""
    xa, xb = (xplane - 0.05, xplane + depth) if sgn > 0 else (xplane - depth, xplane + 0.05)
    za, zb = zc - w / 2, zc + w / 2
    if m.blocked(xplane - 0.5, xplane + 0.5, y0 - 0.2, y0 + h + 0.2, za - 0.2, zb + 0.2):
        return
    m.window((sgn, 0, 0), (xplane, y0, za), (0, 0, 1), w, h)
    for z in (za, zb - fw):
        m.box(xa, xb, y0, y0 + h, z, z + fw, sw)
    for y in (y0, y0 + h - fw):
        m.box(xa, xb, y, y + fw, za, zb, sw)
    for i in range(1, cols):
        z = za + w * i / cols
        m.box(xa, xb, y0, y0 + h, z - fw / 2, z + fw / 2, sw)
    for j in range(1, rows):
        y = y0 + h * j / rows
        m.box(xa, xb, y - fw / 2, y + fw / 2, za, zb, sw)


def pane_z(m, sgn, zplane, xc, y0, w, h, cols=2, rows=2, fw=0.08, sw=TEAL, depth=0.1):
    """Same as pane_x on a wall with outward normal (0, 0, sgn); xc = centre along x."""
    za, zb = (zplane - 0.05, zplane + depth) if sgn > 0 else (zplane - depth, zplane + 0.05)
    xa, xb = xc - w / 2, xc + w / 2
    if m.blocked(xa - 0.2, xb + 0.2, y0 - 0.2, y0 + h + 0.2, zplane - 0.5, zplane + 0.5):
        return
    m.window((0, 0, sgn), (xa, y0, zplane), (1, 0, 0), w, h)
    for x in (xa, xb - fw):
        m.box(x, x + fw, y0, y0 + h, za, zb, sw)
    for y in (y0, y0 + h - fw):
        m.box(xa, xb, y, y + fw, za, zb, sw)
    for i in range(1, cols):
        x = xa + w * i / cols
        m.box(x - fw / 2, x + fw / 2, y0, y0 + h, za, zb, sw)
    for j in range(1, rows):
        y = y0 + h * j / rows
        m.box(xa, xb, y - fw / 2, y + fw / 2, za, zb, sw)


def door_x(m, sgn, xplane, zc, w, h, leaf=TEAL, frame=WHITE, y0=0.0):
    """Door on a wall with outward normal (sgn, 0, 0): white frame, leaf with two rails and a small glazed light."""
    xa, xb = (xplane, xplane + 0.12) if sgn > 0 else (xplane - 0.12, xplane)
    xo = (xplane + 0.1, xplane + 0.16) if sgn > 0 else (xplane - 0.16, xplane - 0.1)
    za, zb = zc - w / 2, zc + w / 2
    m.box(xa, xb, y0, y0 + h + 0.15, za - 0.1, zb + 0.1, frame)
    m.box(xo[0], xo[1], y0, y0 + h, za, zb, leaf)
    for y in (y0 + 0.3, y0 + h * 0.55):
        m.box(xo[0], xo[1] + 0.03, y, y + 0.07, za, zb, DGREY)
    m.window((sgn, 0, 0), (xo[1] if sgn > 0 else xo[0], y0 + h * 0.62, za + w * 0.2), (0, 0, 1), w * 0.6, h * 0.28, off=0.0)


def door_z(m, sgn, zplane, xc, w, h, leaf=TEAL, frame=WHITE):
    """Door on a wall with outward normal (0, 0, sgn); see door_x."""
    za, zb = (zplane, zplane + 0.12) if sgn > 0 else (zplane - 0.12, zplane)
    zo = (zplane + 0.1, zplane + 0.16) if sgn > 0 else (zplane - 0.16, zplane - 0.1)
    xa, xb = xc - w / 2, xc + w / 2
    m.box(xa - 0.1, xb + 0.1, 0, h + 0.15, za, zb, frame)
    m.box(xa, xb, 0, h, zo[0], zo[1], leaf)
    for y in (0.3, h * 0.55):
        m.box(xa, xb, y, y + 0.07, zo[0], zo[1] + 0.03, DGREY)
    m.window((0, 0, sgn), (xa + w * 0.2, h * 0.62, zo[1] if sgn > 0 else zo[0]), (1, 0, 0), w * 0.6, h * 0.28, off=0.0)


def win_x(m, sgn, xplane, zc, y0, w, h):
    """Double-hung window on a clapboard wall with outward normal (sgn, 0, 0): white frame, dark glass, meeting rail and a projecting sill."""
    pane_x(m, sgn, xplane, zc, y0, w, h, cols=1, rows=2, fw=0.1, sw=WHITE)
    xa, xb = sorted((xplane, xplane + 0.22 * sgn))
    m.box(xa, xb, y0 - 0.1, y0, zc - w / 2 - 0.1, zc + w / 2 + 0.1, WHITE)


def win_z(m, sgn, zplane, xc, y0, w, h):
    """Same as win_x on a wall with outward normal (0, 0, sgn); xc = centre along x."""
    pane_z(m, sgn, zplane, xc, y0, w, h, cols=2, rows=2, fw=0.1, sw=WHITE)
    za, zb = sorted((zplane, zplane + 0.22 * sgn))
    m.box(xc - w / 2 - 0.1, xc + w / 2 + 0.1, y0 - 0.1, y0, za, zb, WHITE)


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


def rod(m, x, y0, z0, y1, z1, w, sw):
    """Square rod of side w leaning from (x, y0, z0) to (x, y1, z1) (a canopy strut); built from four side quads."""
    b = [(x, y0, z0), (x + w, y0, z0), (x + w, y0, z0 + w), (x, y0, z0 + w)]
    t = [(px, y1, pz + (z1 - z0)) for px, _, pz in b]
    c = (x + w / 2, (y0 + y1) / 2, (z0 + z1) / 2 + w / 2)
    for i in range(4):
        j = (i + 1) % 4
        m.poly([b[i], b[j], t[j], t[i]], sw, c)


def curtain(m, axis, nrm, plane, a0, a1, y0, row_h, ncol, glass=GLASSB, top_sw=DARK, frame=DARK):
    """Curtain wall (user, 2026-10-21: Hangar 5's office is mostly glass with thin framing): panes in a grid of ncol columns between a0..a1 and rows
    of heights row_h from y0, each pane a quad 5 cm off the wall, the top row a dark spandrel; thin mullions stand 18 cm proud of the glass so the
    glazing reads as set back.  axis "x": wall runs along x at z = plane (normal (0, 0, nrm)); axis "z": runs along z at x = plane (normal (nrm, 0, 0))."""
    ys = [y0]
    for h in row_h:
        ys.append(ys[-1] + h)
    cs = [a0 + (a1 - a0) * i / ncol for i in range(ncol + 1)]
    mw, md = 0.07, 0.18

    def P(a, y, d):
        return (a, y, plane + nrm * d) if axis == "x" else (plane + nrm * d, y, a)

    def bar(a_lo, a_hi, y_lo, y_hi):
        p0, p1 = P(a_lo, y_lo, 0.0), P(a_hi, y_hi, md)
        m.box(min(p0[0], p1[0]), max(p0[0], p1[0]), y_lo, y_hi, min(p0[2], p1[2]), max(p0[2], p1[2]), frame)
    centre = P((a0 + a1) / 2, (ys[0] + ys[-1]) / 2, -3.0)
    for r in range(len(row_h)):
        sw = top_sw if r == len(row_h) - 1 else glass
        for c in range(ncol):
            m.poly([P(cs[c], ys[r], 0.05), P(cs[c + 1], ys[r], 0.05), P(cs[c + 1], ys[r + 1], 0.05), P(cs[c], ys[r + 1], 0.05)], sw, centre)
    for a in cs:
        bar(a - mw, a + mw, ys[0], ys[-1])
    for y in ys:
        bar(a0, a1, y - mw, y + mw)


def roof_vents(m, pts, y, sw=DGREY):
    for x, z in pts:
        yy = y(x, z) if callable(y) else y  # a function of (x, z) for vents on a sloped roof (the Hangar 14 units floated above the pitch)
        m.box(x - 0.4, x + 0.4, yy, yy + 0.9, z - 0.4, z + 0.4, sw)


# Hangar 4 -----------------------------------------------------------------------------------
def hangar4():
    """Pale-yellow ribbed hangar whose long wall faces the runway (west, heading 270; the user's call: it must not face north).  The wide
    arched door opening, "4" roundel and Government of Alberta sign from the Wikimedia photo are on that front (+Z) wall, which has two doors
    (dark open one north, white closed one south, orange bay between; 1989 archive photo EA-207-425); that wall is the gable end
    (user, 2026-10-21): the ridge runs E-W back from the door wall.  Brick block at the north end (viewer-left of
    the front).  OSM 325273554: 71 (N-S) x 33.5 m."""
    m = fmesh()
    W, D, wh, rise = 71.1, 33.5, 9.0, 4.4
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    t = 1.3  # depth of the door-wall frontage: the openings are real recesses with the dark hall behind them (user, 2026-10-21: flat and cartoony)
    zi = z1 - t
    m.box(x0, x1, 0, wh, z0, zi, YELLOWR, top=False)
    m.gable(x0, x1, wh, rise, z0, z1, along_z=True, sw_roof=METAL, sw_wall=YELLOWR)  # gable end = the west (door) wall (user, 2026-10-21)
    for x in (x0 - 0.12, x1):
        m.box(x, x + 0.12, wh - 0.5, wh + 0.05, z0, z1, RWHITE)
    a, hd, top, n = 14.5, 6.2, 8.4, 28
    zf = z1 + 0.06
    cn, an = 18.5, 13.5  # north door, x 5..32 (a 1.5 m yellow strip, as in the 2010 photo, separates it from the orange bay)
    cs, as_ = -17.25, 12.75  # south door, x -30..-4.5

    def arch_h(cx, a, x):
        u = (x - cx) / a
        return hd + (top - hd) * (1 - u * u)

    def frontage(cx, a, hall=True):
        """The wall above one arched opening, built as slices so the arch is cut through the full thickness; dark hall behind."""
        for k in range(n):
            xa, xb = cx - a + 2 * a * k / n, cx - a + 2 * a * (k + 1) / n
            yl = max(arch_h(cx, a, xa), arch_h(cx, a, xb))
            m.box(xa, xb, yl, wh, zi, z1, YELLOWR, top=False)
            m.poly([(xa, yl, zi), (xb, yl, zi), (xb, yl, z1), (xa, yl, z1)], DGREY, ((xa + xb) / 2, yl + 5, (zi + z1) / 2))  # soffit
            m.box(xa, xb, yl - 0.05, yl + 0.5, z1, z1 + 0.2, RWHITE, top=False)  # raised arch surround
        if not hall:
            return
        # the dark hall behind the opening (x cx-a..cx+a, up to the crown) with maroon roof columns
        m.poly([(cx - a, 0, zi + 0.02), (cx + a, 0, zi + 0.02), (cx + a, top, zi + 0.02), (cx - a, top, zi + 0.02)], DARK, (cx, 3, zi - 5))
        for fx in (-0.62, -0.3, 0.3, 0.62):
            m.box(cx + fx * a - 0.3, cx + fx * a + 0.3, 0, hd + 0.8, zi + 0.02, zi + 0.5, BRICK)
        m.box(cx - a, cx + a, hd, hd + 0.5, zi + 0.02, zi + 0.4, BRICK)  # first roof truss across the opening

    def wall_piece(xa, xb):
        m.box(xa, xb, 0, wh, zi, z1, YELLOWR, top=False)

    # solid wall between and beside the doors, then the two recessed openings
    wall_piece(x0, cs - as_)
    wall_piece(cs + as_, cn - an)
    wall_piece(cn + an, x1)
    # two doors on the runway wall (1989 City of Edmonton archive photo EA-207-425): a dark open one at the north (viewer-left) end,
    # a white closed one at the south end, with a two-storey orange-panelled bay between them
    frontage(cn, an)
    frontage(cs, as_, hall=False)
    zc = z1 - 0.7  # the closed door's white leaves stand inside the reveal
    pts = [(cs - as_, 0, zc), (cs + as_, 0, zc)] + [(cs + as_ * u, hd + (top - hd) * (1 - u * u), zc) for u in [1 - 2 * k / 20 for k in range(21)]]
    m.poly(pts, RWHITE, (cs, 3, zi - 4))
    for k in range(1, 5):  # panel joints on the closed door
        jx = cs - as_ + 2 * as_ * k / 5
        m.box(jx - 0.06, jx + 0.06, 0.2, 7.0, zc, zc + 0.04, DGREY)
    for sx in (cn - an - 0.5, cn + an):  # door-track posts proud of the wall, a pale post and a dark one
        m.box(sx, sx + 0.5, 0, hd + 0.4, z1, z1 + 0.28, RWHITE)
    for sx in (cs - as_ - 0.5, cs + as_):
        m.box(sx, sx + 0.5, 0, hd + 0.4, z1, z1 + 0.28, DGREY)
    # eave trim along the top of the door wall, in two lengths that stop at the orange bay (the bay's front face and the trim's were coplanar and
    # z-fought; the roundel used to overlap the trim too, user 2026-10-21)
    m.box(x0 - 0.1, -4.5, wh - 0.2, wh + 0.1, z1, z1 + 0.24, RWHITE)
    m.box(3.0, x1 + 0.1, wh - 0.2, wh + 0.1, z1, z1 + 0.24, RWHITE)
    m.box(-4.5, 3.0, 0, wh + 0.1, z1, z1 + 0.3, SALMON)  # orange bay between the doors
    for y in (1.2, 5.0):
        m.window((0, 0, 1), (-1.75, y, z1 + 0.3), (1, 0, 0), 2.0, 1.6)
    rx = 5.8  # the "4" roundel sits on the yellow wall above the door's south shoulder, next to the orange bay (2010 photo)
    m.box(rx - 1.05, rx + 1.05, 6.75, 8.65, z1, z1 + 0.12, RWHITE)
    number_disc(m, rx, 7.7, z1 + 0.12, (0, 1), 0.85, "4")
    # Government of Alberta sign over the north shoulder (viewer-left): white board with the blue Alberta box and the name
    rect_sign(m, cn + an - 3.3, 8.2, z1 + 0.1, (0, 1), 4.6, 0.55, "goa")
    m.box(x1, x1 + 10.0, 0, 4.6, z1 - 16.0, z1, BRICKD)
    # landside (east, -Z), Street View 47 (2012): the "4" roundel high on the wall near the south end (next to Hangar 5) with a grey man door under it
    number_disc(m, x0 + 4.5, 7.4, z0 - 0.0, (0, -1), 0.9, "4")
    m.box(x0 + 3.9, x0 + 5.1, 0, 2.1, z0 - 0.08, z0, GREY)
    m.box(x0 + 3.8, x0 + 5.2, 2.1, 2.25, z0 - 0.12, z0, DGREY)
    m.box(x1 - 6.0, x1 - 4.8, 0, 2.1, z0 - 0.08, z0, GREY)  # second man door toward the brick block
    m.box(x1 - 6.1, x1 - 4.7, 2.1, 2.25, z0 - 0.12, z0, DGREY)
    roof_vents(m, [(0, -10), (0, 0), (0, 10)], wh + rise)
    m.mirror_x()
    return m


# Hangar 5 -----------------------------------------------------------------------------------
def hangar5():
    """Tan ribbed hangar, cream upper band, white sliding doors on the west gable end (+Z, heading 270), two-storey bronze
    curtain-wall office wing on the south side (11 m wide, full depth), "5" roundels airside and landside.  OSM 325270299: 53.1 x 43.3 m."""
    m = fmesh()
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
    # office wing on the SOUTH side (-X), 11 m wide (half the earlier 22 m) and the FULL depth of the hangar, flush with both the west (runway)
    # and the east (landside) walls (user, 2026-10-21).  Two storeys of bronze glazing on the west face, the south end and round the landside.
    ox = x0 - 11.0
    m.box(ox, x0, 0, 7.6, z0, z1, DARK)
    rh = [2.4, 2.4, 1.7, 0.9]  # three bronze panes high and a dark spandrel under the roof (Wikimedia 11094269004, Street View 50)
    curtain(m, "z", -1, ox, z0 + 0.15, z1 - 0.15, 0.2, rh, 18)  # south end
    curtain(m, "x", 1, z1, ox + 0.15, x0 - 0.15, 0.2, rh, 5)  # west (airside) face
    curtain(m, "x", -1, z0, ox + 0.15, x0 - 0.15, 0.2, rh, 5)  # east (landside) face: the glazing goes round to the back
    m.box(ox - 0.4, x0, 7.6, 7.9, z0 - 0.4, z1 + 0.4, DGREY)
    m.box(ox - 1.8, ox, 3.1, 3.4, -(D / 2) + 14.0, -(D / 2) + 22.0, DGREY)  # entrance canopy on the south end
    # "5" roundels (user, 2026-10-21): airside on the cream band beside the door header at the south corner; landside high at the south end
    # of the east wall next to the offices, as in Street View 2010 (h5-office-50 / 51)
    number_disc(m, x0 + 2.2, 7.4, z1, (0, 1), 0.85, "5")
    number_disc(m, x0 + 3.2, 7.4, z0, (0, -1), 0.85, "5")
    # landside (east, -Z), Street View 48 / 49 (2012): plain ribbed wall with a few small wall packs, and a low dark-grey annex at the north end
    # (+X) with a grey man door and two round vents; a second man door near the south end beside the office
    m.box(x1 - 12.0, x1, 0, 4.2, z0 - 4.5, z0, DGREY)
    m.box(x1 - 12.2, x1, 4.2, 4.45, z0 - 4.7, z0, DARK)
    m.box(x1 - 7.2, x1 - 6.0, 0, 2.1, z0 - 4.58, z0 - 4.5, GREY)
    m.box(x1 - 7.4, x1 - 5.8, 2.1, 2.3, z0 - 4.7, z0 - 4.5, DARK)
    for vx in (x1 - 10.0, x1 - 8.4):
        m.box(vx - 0.4, vx + 0.4, 4.45, 5.15, z0 - 3.4, z0 - 2.6, GREY)
    m.box(x0 + 5.0, x0 + 6.2, 0, 2.1, z0 - 0.08, z0, GREY)
    m.box(x0 + 4.9, x0 + 6.3, 2.1, 2.25, z0 - 0.12, z0, DARK)
    roof_vents(m, [(0, -8), (0, 8), (0, 0)], wh + rise)
    m.mirror_x()
    return m


# Hangar 6 -----------------------------------------------------------------------------------
def hangar6():
    """White hangar with green side walls (west gable end = apron side with sliding doors, heading 270), low white annex at the
    east end with a blue door, "6" roundel high on the east gable.  OSM 325267780: 41.9 x 46.2 m."""
    m = fmesh()
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
    number_disc(m, 18.2, 6.9, z1 + 0.06, (0, 1), 0.95, "6")  # airside roundel beside the door header (user, 2026-10-21)
    roof_vents(m, [(0, -10), (0, 10)], wh + rise)
    m.mirror_x()
    return m


# Hangar 7 -----------------------------------------------------------------------------------
def hangar7():
    """Steel-blue ribbed hangar; west gable end (heading 270) has a wide white two-tier sliding door with the "7" roundel on the
    blue wall beside it; darker slate-blue annex with awning at the east end.  OSM 325271251: 36.4 x 39.3 m."""
    m = fmesh()
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
    number_disc(m, 14.0, 3.5, z0, (0, -1), 0.95, "7")  # landside roundel on the east gable beside the annex (user, 2026-10-21)
    roof_vents(m, [(0, -8), (0, 0), (0, 8)], wh + rise)
    m.mirror_x()
    return m


# Hangar 8 -----------------------------------------------------------------------------------
def hangar8():
    """Hangar 8, turned (user, 2026-10-21): the big glazed sliding-door wall and the main gable face NORTH, not onto the runway.  Pale
    grey-blue hall at the north end (+X, 35 m) with the door wall on its north end wall (wide, 52.9 m: eight leaves between two projecting
    sidebars like Hangar 39's, a lean-to canopy with a green fascia, ridge running N-S so the gable faces north), a taller flat-topped end
    block (10 m) carrying the "8" roundel, and a long two-storey wing with a roof clerestory to the south.  Landside (east, 109 St) from
    Street View 59 / 61: tall roundel block, two-storey window ribbon, a tall narrow window and glazing on the hall.  OSM 325268698:
    66.3 (N-S) x 52.9 m (E-W)."""
    m = fmesh()
    W, D = 66.3, 52.9
    z0, z1 = -D / 2, D / 2
    hx0, hx1 = -2.0, 33.15
    wh, rise = 9.0, 3.4
    m.box(hx0, hx1, 0, wh, z0, z1, STEEL, top=False)
    m.gable(hx0, hx1, wh, rise, z0, z1, along_z=False, sw_roof=METAL, sw_wall=STEEL)  # gable end on the north wall (x = hx1)
    # north door wall: dark opening, eight leaves with wire-glass panels, sidebars, canopy
    dz0, dz1 = -22.0, 22.0
    zs = [dz0 + (dz1 - dz0) * i / 8 for i in range(9)]
    m.box(hx1, hx1 + 0.05, 0, 8.6, dz0 - 0.4, dz1 + 0.4, DARK)
    for a_, b_ in zip(zs[:-1], zs[1:]):
        m.box(hx1, hx1 + 0.25, 0, 8.3, a_ + 0.05, b_ - 0.05, RWHITE)
        for y0, y1 in ((1.6, 3.2), (4.2, 5.8), (6.4, 7.8)):
            m.poly([(hx1 + 0.3, y0, a_ + 0.7), (hx1 + 0.3, y0, b_ - 0.7), (hx1 + 0.3, y1, b_ - 0.7), (hx1 + 0.3, y1, a_ + 0.7)], DGREY,
                   (hx1 - 1, y0, a_))
    for z in zs:  # dark guide posts
        m.box(hx1, hx1 + 0.32, 0, 8.4, z - 0.09, z + 0.09, DGREY)
    for pz0, pz1 in ((z0, dz0 - 0.4), (dz1 + 0.4, z1)):  # sidebars that carry the door track, projecting past the wall
        m.box(hx1, hx1 + 1.1, 0, wh + 0.3, pz0, pz1, GREY)
    number_disc(m, hx1 + 1.1, 5.6, (dz1 + 0.4 + z1) / 2, (1, 0), 0.95, "8")  # roundel on the sidebar beside the big door (user, 2026-10-21)
    m.box(hx1, hx1 + 0.9, 8.3, 8.8, dz0 - 0.4, dz1 + 0.4, GREEN)  # header / canopy fascia with its green trim line
    m.poly([(hx1, 9.6, dz0 - 0.4), (hx1, 9.6, dz1 + 0.4), (hx1 + 2.6, 8.8, dz1 + 0.4), (hx1 + 2.6, 8.8, dz0 - 0.4)], METAL, (hx1, 3, 0))  # lean-to
    m.box(hx1 + 2.55, hx1 + 2.65, 8.5, 8.9, dz0 - 0.4, dz1 + 0.4, GREEN)
    # Street View 59 (recounted 2026-10-21): the roundel slab next to the hall, then the wing, whose first-floor ribbon starts under a taller
    # tower set back a little from the slab; roof clerestory above the wing; a one-storey skirt projects at the far end
    xb, hA, hB = -26.0, 6.9, 5.4
    hs, ht = 11.0, 13.0
    wx0 = -W / 2
    m.frame = NAVY  # the window surrounds are navy in the photo
    m.box(-7.0, hx0, 0, hs, z0, z1, RWHITE)  # roundel slab
    m.box(-7.1, hx0, hs, hs + 0.25, z0 - 0.15, z1 + 0.15, DGREY)
    m.box(-12.0, -7.0, hA, ht, z0 + 0.5, z1, RWHITE)  # tower over the start of the wing, landside face set back 0.5 m
    m.box(-12.1, -6.9, ht, ht + 0.25, z0 + 0.4, z1 + 0.1, DGREY)
    number_disc(m, -4.5, 9.4, z1, (0, 1), 0.95, "8")  # airside
    m.box(-12.0, -11.3, 0, ht + 0.25, z1 - 0.1, z1 + 0.3, DGREY)  # downpipe / stack beside the tower
    m.box(xb, -7.0, 0, hA, z0, z1, STEEL, top=False)
    m.box(wx0, xb, 0, hB, z0, z1, STEEL, top=False)
    m.box(xb, -7.0, hA, hA + 0.05, z0, z1, METAL)  # roofs (the wall boxes are open at the top)
    m.box(wx0, xb, hB, hB + 0.05, z0, z1, METAL)
    m.box(xb - 0.15, -7.0, hA, hA + 0.25, z0 - 0.15, z1 + 0.15, DGREY)  # eaves cornice
    m.box(wx0 - 0.15, xb - 0.15, hB, hB + 0.25, z0 - 0.15, z1 + 0.15, DGREY)  # ends short of the step so the two trims do not overlap
    cx0, cx1 = -25.0, -13.5
    m.box(cx0, cx1, hA + 0.25, 9.5, z0 + 2.5, z1 - 4, RWHITE, top=True)  # roof clerestory
    m.box(cx0 - 0.1, cx1 + 0.1, 9.5, 9.7, z0 + 2.4, z1 - 3.9, DGREY)
    rows_x(m, -1, cx0, z0 + 4.5, z1 - 6.0, 7.55, 8, 2.2, 1.7)
    rows_z(m, -1, z0 + 2.5, cx0 + 0.5, cx1 - 0.5, 7.55, 8, 1.1, 1.7)  # the clerestory glazing seen from the street: eight panes
    rows_z(m, 1, z1 - 4, cx0 + 0.5, cx1 - 0.5, 7.55, 8, 1.1, 1.7)
    rows_z(m, 1, z1, wx0 + 4, -14.0, 1.6, 4, 2.2, 2.6)
    m.box(wx0 + 6.0, wx0 + 9.0, 0, 2.5, z1, z1 + 0.08, DGREY)
    # landside (-Z, east, 109 St): per the photo, from the hall: tall narrow window under the roundel (1); ground tier: window, window, door,
    # long strip window, glass door, window (6); first-floor ribbon of eight panes; clerestory of eight panes; at the far end the skirt
    # with a window and a door and three small windows above it
    number_disc(m, -4.5, 9.4, z0, (0, -1), 0.95, "8")
    m.window((0, 0, -1), (-5.0, 3.3, z0), (1, 0, 0), 1.1, 2.1)
    for wxx, ww, wh_, wy in ((-9.2, 2.2, 1.9, 1.1), (-12.2, 1.9, 1.9, 1.1), (-19.4, 3.6, 1.7, 1.3), (-21.2, 1.1, 2.0, 0.1), (-24.2, 1.9, 1.9, 1.1)):
        m.window((0, 0, -1), (wxx, wy, z0), (1, 0, 0), ww, wh_)
    m.box(-14.4, -13.2, 0, 2.2, z0 - 0.08, z0, DGREY)
    rows_z(m, -1, z0, -25.8, -7.4, 4.2, 8, 2.0, 2.2)
    # wall profile: plinth, navy band under the ribbon, downpipes, a corner pilaster on the slab, a skirt at the far end
    m.box(-26.0, hx0, 0, 0.45, z0 - 0.06, z0, DGREY)
    m.box(-25.8, -7.0, 3.95, 4.07, z0 - 0.06, z0, NAVY)
    for dpx in (-25.95, -7.45, -2.6):
        m.box(dpx, dpx + 0.16, 0, hA if dpx < -7.0 else hs, z0 - 0.12, z0, GREY)
    m.box(-7.0, -6.8, 0, hs, z0 - 0.1, z0, GREY)  # slab edge pilaster
    m.box(wx0, -26.0, 0, 3.6, z0 - 1.6, z0, STEEL)  # one-storey skirt
    m.box(wx0 - 0.1, -25.9, 3.6, 3.9, z0 - 1.7, z0, DGREY)
    m.window((0, 0, -1), (-29.0, 1.1, z0 - 1.6), (1, 0, 0), 2.2, 1.5)
    m.box(-32.2, -31.0, 0, 2.2, z0 - 1.68, z0 - 1.6, DGREY)
    rows_z(m, -1, z0, wx0 + 0.5, -26.5, 4.2, 3, 1.2, 1.0)
    # LAW OFFICE across the tower base, AVIATION a little lower beyond it, standing on the eaves cornice
    for sx, sy, sw_, sh_, v0, v1, dep in ((-10.8, 7.63, 5.0, 0.85, 0.0, 0.5, 0.55), (-15.9, 7.51, 4.4, 0.6, 0.5, 1.0, 2.55)):
        m.box(sx - sw_ / 2 - 0.06, sx + sw_ / 2 + 0.06, sy - sh_ / 2 - 0.06, sy + sh_ / 2 + 0.06, z0 - 0.1, z0 + dep, GREY)
        rect_sign(m, sx, sy, z0 - 0.12, (0, -1), sw_, sh_, "lawoffice", v0, v1)
    m.box(hx0, hx1, 0, 3.0, z0 - 0.05, z0, WHITE)  # hall landside: pale lower wall, glazed bays above
    rows_z(m, -1, z0, hx0 + 4.0, hx1 - 4.0, 3.2, 8, 2.6, 4.6)
    m.box(hx1 - 3.0, hx1 - 1.8, 0, 2.2, z0 - 0.08, z0, DGREY)
    roof_vents(m, [(-30, -12), (-30, 0), (-30, 12)], hB + 0.25)
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
    m = fmesh()
    L, D = 81.6, 25.7
    x0, x1, z0, z1 = -L / 2, L / 2, -D / 2, D / 2
    xs, hs, hn = -28.0, 8.2, 6.4
    m.box(xs, x1, 0, hs, z0, z1, PBFLAT)
    m.box(x0, xs, 0, hn, z0, z1, PBFLAT)
    parapet(m, xs, x1, z0 - 0.1, z1 + 0.1, hs - 0.6, hs + 0.45, 0.5, NAVY)
    parapet(m, x0, xs, z0 - 0.1, z1 + 0.1, hn - 0.6, hn + 0.45, 0.5, NAVY)
    m.box(xs - 0.1, xs + 0.1, hn + 0.4, hs + 0.4, z0 - 0.05, z1 + 0.05, NAVY)  # was flush with the parapets' outer faces and z-fought
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
    m = fmesh()
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
    m = fmesh()
    W, D, wh, rise = 20.7, 24.6, 6.5, 3.0
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    m.box(x0, x1, 0, wh, z0, z1, NAVYB, top=False)
    m.gable(x0, x1, wh, rise, z0, z1, along_z=True, sw_roof=DGREY, sw_wall=NAVYB)
    m.box(x0, x1, 0, wh, z1, z1 + 0.06, RWHITE, top=False)
    m.poly([(x0, wh, z1 + 0.06), (x1, wh, z1 + 0.06), (0.0, wh + rise, z1 + 0.06)], RWHITE, (0.0, wh - 1, z1 - 2))
    # roller door with depth (user, 2026-10-21): the leaf sits behind projecting jambs and a header beam, with ribs and a bottom rail
    m.box(-5.4, 5.4, 0, 5.0, z1 + 0.06, z1 + 0.2, CREAM)
    for k in range(1, 5):
        m.box(-5.4, 5.4, k * 1.0 - 0.05, k * 1.0 + 0.05, z1 + 0.2, z1 + 0.27, GREY)
    m.box(-5.4, 5.4, 0, 0.18, z1 + 0.2, z1 + 0.3, DGREY)
    for jx0, jx1 in ((-5.95, -5.4), (5.4, 5.95)):
        m.box(jx0, jx1, 0, 5.7, z1 + 0.06, z1 + 0.42, DGREY)
    m.box(-5.95, 5.95, 5.0, 5.7, z1 + 0.06, z1 + 0.55, DGREY)
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
    m = fmesh()
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
    number_disc(m, 0.0, 5.9, z0, (0, -1), 0.95, "19")  # airside roundel on the brick centre (user, 2026-10-21)
    m.box(-3.0, 3.0, 8.8, 11.0, z1 - 8.0, z1 - 2.0, BRICKD)  # taller stair tower
    m.box(-3.2, 3.2, 11.0, 11.35, z1 - 8.2, z1 - 1.8, TANBLK)
    m.mirror_x()
    return m


def gs_hut():
    """ILS glideslope shelter in the infield beside the old runway 16/34 (west-lineup photo, 2014 aerial): a small flat-roofed hut painted
    in red and white checks on all four walls, a door on the east face, and a mast with a small antenna box 5.7 m north.  Heading 0."""
    m = fmesh()
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
    m = fmesh()
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
    """Hangar 40 = Canadian Helicopters (user, 2026-10-21; Street View 29-32, 2010-2012, 12039 / 12043 121 St NW; Flickr woodhead 13207130405).
    Faces NW to the car park.  Exactly three masses (user, 2026-10-21): the brick office with the landside entrance in the middle and a gabled
    hangar of the same size on each side of it.  The left one (+X) has its end plate flush with the office; the right one (-X, the SE one) comes
    about 3.5 m forward of the office door and carries the blue "40" roundel (Street View 29).  Heading 228."""
    m = fmesh()
    W, D = 72.0, 46.0
    z0, z1 = -D / 2, D / 2
    wh, rise = 8.0, 2.4
    # left hall (+X) x 3..34, end plate flush with the office
    m.box(3.0, 34.0, 0, wh, z0, z1, RWHITE, top=False)
    m.gable(3.0, 34.0, wh, rise, z0, z1, along_z=True, sw_roof=METAL, sw_wall=RWHITE)
    for xw in (8.0, 14.0, 20.0):
        m.window((0, 0, 1), (xw, 4.2, z1), (1, 0, 0), 2.4, 1.6)  # window pairs seen on the left hall's end plate in Street View 29
    m.box(25.0, 28.0, 0, 2.2, z1, z1 + 0.1, DGREY)  # personnel door
    # big hangar doors on the gable wall opposite the landside, one per hall (user, 2026-10-21: both halls need an airside door), four leaves each
    for dx0, dx1 in ((5.0, 32.0), (-36.0, -9.0)):
        m.box(dx0, dx1, 0, 6.0, z0 - 0.05, z0, DARK)
        leaves(m, z0, [dx0 + (dx1 - dx0) * i / 4 for i in range(5)], 0, 5.8, GREY, front=-1, post=DGREY)
        m.box(dx0 - 0.3, dx1 + 0.3, 5.8, 6.3, z0 - 0.5, z0, DGREY)  # header
    number_disc(m, 18.5, 7.1, z0 - 0.0, (0, -1), 0.8, "40")  # airside roundels above the doors (user: "there should be a rondelle somewhere")
    number_disc(m, -22.5, 7.1, z0 - 0.0, (0, -1), 0.8, "40")
    # brick office between the halls
    m.box(-7.0, 3.0, 0, 7.6, z0, z1, BRICKD)
    parapet(m, -7.2, 3.2, z0 - 0.2, z1 + 0.2, 7.5, 8.1, 0.4, RED)  # red fascia round a flat grey roof, not a red roof
    m.box(-7.0, 3.0, 7.5, 7.7, z0, z1, DGREY)
    m.window((0, 0, 1), (-3.2, 0.0, z1), (1, 0, 0), 1.4, 2.2)  # entrance door
    m.box(-4.7, -0.3, 2.7, 3.2, z1, z1 + 1.5, RWHITE)  # white canopy with gable
    m.gable(-4.7, -0.3, 3.2, 0.9, z1, z1 + 1.5, along_z=True, sw_roof=RWHITE, sw_wall=RWHITE)
    for xg in (-6.6, 0.6):  # glass-block panels
        m.window((0, 0, 1), (xg, 0.5, z1), (1, 0, 0), 1.6, 2.0)
    m.box(-7.1, -4.5, 2.6, 3.3, z1, z1 + 1.0, RED)  # red awning
    m.box(0.9, 3.0, 2.6, 3.3, z1, z1 + 1.0, RED)
    for xw in (-6.0, -1.6):  # first-floor windows
        m.window((0, 0, 1), (xw, 4.0, z1), (1, 0, 0), 2.6, 2.2)
    m.box(-1.0, 1.6, 7.6, 8.9, -6.0, -2.0, DGREY)  # roof unit on the office
    # right hall (-X) x -38..-7: same size, end plate 3.5 m forward of the office, the "40" roundel on it
    zf = z1 + 3.5
    m.box(-38.0, -7.0, 0, wh, z0, zf, RWHITE, top=False)
    m.gable(-38.0, -7.0, wh, rise, z0, zf, along_z=True, sw_roof=METAL, sw_wall=RWHITE)
    number_disc(m, -14.0, 6.4, zf, (0, 1), 1.15, "40")
    m.box(-9.0, -7.4, 0, 2.2, zf, zf + 0.1, DGREY)
    m.pos = [(x + 2.0, y, z) for x, y, z in m.pos]  # centre the 72 m footprint on the origin
    m.mirror_x()
    return m


# Hangar 11 ----------------------------------------------------------------------------------
def hangar11():
    """USAAF T3 (1942-43) as it looked in the 1950s-60s: white barrel-vault hall with seven peach sliding-door leaves on the north end
    (+Z, heading 0), a three-storey white-clapboard annex across the south end carrying the "11" roundel, a control cab and the big
    roof sign, a two-storey east wing and a low west annex.  OSM 325268748: 86 x 64 m footprint."""
    m = fmesh()
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
    # south annex: three storeys across the whole south end, flush with the landside (+X) wall so the long wing's wall runs on from its corner
    # (photos 11094273884, h11-annex-63..66).  Wall relief: corner boards, belt courses at the floor lines, framed double-hung windows with sills.
    ax0, ax1, az0, az1 = -29.0, 43.15, -46.0, z0
    m.box(ax0, ax1, 0, 11.2, az0, az1, WHITE, top=False)
    m.box(ax0 - 0.2, ax1 + 0.2, 11.2, 11.6, az0 - 0.2, az1, GREEN)
    m.box(ax0, ax1, 11.2, 11.3, az0, az1, DGREY)
    for y in (4.7, 8.0):
        m.box(ax0, ax1 + 0.1, y - 1.5, y - 1.3, az0 - 0.1, az1, WHITE)  # belt course
        m.box(ax0 - 0.1, ax1, y - 1.5, y - 1.3, az0 - 0.1, az1, WHITE)
    for x in (ax0 - 0.1, ax1 - 0.1):                                     # corner boards
        m.box(x, x + 0.25, 0, 11.2, az0 - 0.1, az0 + 0.2, WHITE)
    for y in (1.4, 4.7, 8.0):
        for x in [ax0 + 2.5 + 3.4 * k for k in range(20)]:
            if x < ax1 - 4.0 and not (y > 7.0 and abs(x - 37.0) < 2.8):
                win_z(m, -1, az0, x, y, 1.6, 1.5)
        for i in range(5):                                               # landside face of the annex (beside the fire escape)
            win_x(m, 1, ax1, az0 + 4.2 + 1.9 * i, y, 1.0, 1.5)
        for i in range(3):
            win_x(m, -1, ax0, az0 + 3.0 + 4.0 * i, y, 1.6, 1.5)
    number_disc(m, 37.0, 8.6, az0, (0, -1), 1.0, "11")
    # roof sign board and control cab stand on the annex roof (y 11.3); the roof vents and the cab were floating 0.3-0.9 m above it
    m.box(-26.0, 4.0, 11.3, 14.4, az0 + 0.4, az0 + 0.6, WHITE)
    rect_sign(m, -11.0, 12.85, az0 + 0.38, (0, -1), 28.0, 2.8, "nwi", 0.0, 0.5)  # NORTHWEST INDUSTRIES LTD. (1956 photo)
    rect_sign(m, -11.0, 3.8, az0 - 0.1, (0, -1), 26.0, 1.5, "nwi", 0.5, 1.0)  # COMMERCIAL AIRCRAFT SERVICE on the second-floor band
    m.box(-9.0, -4.0, 11.3, 14.6, az0 + 6.0, az0 + 11.0, DGREY)  # control cab
    m.box(-9.1, -3.9, 12.4, 13.9, az0 + 5.9, az0 + 11.1, GLASS)
    m.box(-9.4, -3.6, 14.6, 14.9, az0 + 5.6, az0 + 11.4, DGREY)
    # landside (109 St) fire escape, one only (11094273884): a steel ladder up the south face beside the corner, two white landings with
    # green doors on the landside face next to it, stringers down from each landing, and the ladder carried 1 m above the roof
    lx = ax1 - 1.0
    for rx in (lx - 0.27, lx + 0.27):
        m.box(rx - 0.03, rx + 0.03, 0, 12.6, az0 - 0.32, az0 - 0.26, DGREY)  # ladder rails
    for k in range(40):
        m.box(lx - 0.27, lx + 0.27, 0.3 + k * 0.3, 0.34 + k * 0.3, az0 - 0.3, az0 - 0.27, DGREY)  # rungs
    for y in (0.5, 4.0, 7.5, 11.0):
        for rx in (lx - 0.27, lx + 0.27):
            m.box(rx - 0.04, rx + 0.04, y, y + 0.1, az0 - 0.3, az0 - 0.03, DGREY)  # wall brackets
    for ly in (3.5, 6.8):
        m.box(ax1, ax1 + 1.7, ly, ly + 0.15, az0 + 0.1, az0 + 2.3, WHITE)           # landing deck
        m.box(ax1 + 1.6, ax1 + 1.7, ly + 0.15, ly + 1.1, az0 + 0.1, az0 + 2.3, WHITE)  # rails
        m.box(ax1, ax1 + 1.7, ly + 0.15, ly + 1.1, az0 + 2.2, az0 + 2.3, WHITE)
        m.box(ax1, ax1 + 1.7, ly + 0.95, ly + 1.1, az0 + 0.1, az0 + 0.2, WHITE)     # top rail toward the ladder
        door_x(m, 1, ax1, az0 + 1.2, 0.9, 2.1, leaf=GREEN, y0=ly + 0.15)
        m.box(ax1 + 0.05, ax1 + 0.15, ly - 0.7, ly, az0 + 0.3, az0 + 2.1, WHITE)    # underside bracket
    door_x(m, 1, ax1, az0 + 3.0, 0.9, 2.1, leaf=WHITE)                              # ground door under the escape
    for zc in (az0 + 11.2, az0 + 12.0):                                              # U-HAUL double doors
        door_x(m, 1, ax1, zc, 0.8, 2.2, leaf=GREEN)
    # low one-storey block in front of the long wall (h11-annex-65/66): ten big windows and a door under a green-trimmed roof
    bz0, bz1 = z0 + 1.0, -8.0
    m.box(ax1, ax1 + 3.5, 0, 4.0, bz0, bz1, WHITE, top=True)
    m.box(ax1 - 0.1, ax1 + 3.7, 4.0, 4.25, bz0 - 0.2, bz1 + 0.2, GREEN)
    m.box(ax1, ax1 + 3.55, 3.55, 3.65, bz0 - 0.05, bz1 + 0.05, WHITE)                 # belt course
    for k in range(10):
        win_x(m, 1, ax1 + 3.5, bz0 + 2.6 + 2.0 * k, 1.2, 1.4, 1.9)
    door_x(m, 1, ax1 + 3.5, bz0 + 1.2, 0.9, 2.1, leaf=WHITE)
    # east (landside) wing: two storeys, 27 framed double-hung windows per floor on the 2.3 m pitch counted from photos 63/64, belt course,
    # corner boards, the ground row under the low block left out
    m.box(26.0, 43.15, 0, 8.6, z0, z1, WHITE, top=True)
    m.box(25.8, 43.35, 8.6, 8.9, z0 - 0.2, z1 + 0.2, GREEN)
    m.box(26.0, 43.25, 3.3, 3.5, z0, z1, WHITE)                                      # belt course between the floors
    for k in range(27):
        zc = z0 + 2.2 + 2.3 * k
        win_x(m, 1, 43.15, zc, 5.0, 1.0, 1.7)
        if zc > bz1 + 1.0:
            win_x(m, 1, 43.15, zc, 1.4, 1.0, 1.7)
    for z in (z0, z1 - 0.25):
        m.box(43.0, 43.25, 0, 8.6, z, z + 0.25, WHITE)
    # west annex
    m.box(-43.15, bx0, 0, 6.0, -30.0, -4.0, WHITE)
    rows_x(m, -1, -43.15, -28.0, -6.0, 2.4, 5, 1.2, 1.5)
    for vx, vz in ((-12, -10), (-12, 6), (10, -10), (10, 6)):  # sit on the barrel roof (was a flat 13.8 m, up to 0.9 m above it)
        roof_vents(m, [(vx, vz)], arch(vx) - 0.15)
    m.mirror_x()
    return m


# Hangar 14 (Alberta Aviation Museum) ----------------------------------------------------------
def hangar14():
    """Hangar 14 (BCATP 1941, Alberta Aviation Museum), reworked from the 2011 Commons photo (Alberta_Aviation_Museum.jpg), the 2012-2024
    Street View frames, the 2026-10-21 frontage set and the 2014 aerial (tower-photos/EDMONTON_MUNI_AIRPORT__15439598181_.jpg).
    OSM 230718920: 90.8 (E-W) x 100 (N-S) m; front = the SOUTH gable (+Z, heading 180, facing Kingsway and the Bomarc).
    Windows counted from photos.  A perspective fit of the 2012 Street View frame (h14-kingsway-81) puts the west wall's 18 upper windows on an
    even 5.1 m pitch, the first 7.8 m north of the south corner (fit residual under 0.1 %).  The aerial gives the east wall the same 18 bays
    from 7.2 m; its porch block covers the three at 59-78 m, so 15 show.  Both long walls: tall four-pane upper windows over a row of small
    ones (2.85 m pitch west, 2.55 m east).
    South face from the west end (viewer-left, +X): the end of the two-storey white clapboard west wing (10 m wide, 7.2 m); then the hall
    front under a white band with the dark-green ALBERTA AVIATION MUSEUM lettering and a V wing mark either side (aerial crop): glazed door
    bay (10-23.5 m), solid green bay with four small windows, glazed bay with the teal awning, white pilaster (48-50), glazed lobby with the
    entrance doors and small canopy (70 m), a second pilaster (78-79.5), glazed bay, white corner post.  West wall: lean-to ledge, doors at 14
    and 45 m, a one-storey block at 47-67 m with two doors.  East wall: low lean-to (3.4 m high, 3.5 m deep) and a porch block at 59-78 m."""
    m = Mesh(textured=True)
    W, D, H = 90.8, 100.0, 8.8
    WING, WH = 10.0, 7.2
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    xm = x1 - WING                       # west edge of the hall
    U = lambda u: x1 - u                 # x of a point u metres in from the west end
    Z = lambda t: z1 - t                 # z of a point t metres north of the south corner
    m.box(x0, xm, 0, 4.4, z0, z1, TEAL, top=False)
    m.box(x0, xm, 4.4, H, z0, z1, WHITE, top=True)
    m.box(x0 - 0.2, xm, H, H + 0.5, z0 - 0.2, z1 + 0.3, TEAL)
    m.gable(x0, xm, H + 0.5, 2.6, z0, z1, along_z=True, sw_roof=LROOF, sw_wall=WHITE)
    # west wing: white clapboard, flat roof, projects 0.6 m beyond the door face
    zw = z1 + 0.6
    m.box(xm, x1, 0, WH, z0, zw, WHITE, top=True)
    m.box(xm, x1 + 0.2, WH, WH + 0.3, z0 - 0.2, zw + 0.2, TEAL)
    for k in range(18):                                              # 18 tall upper windows, 2 x 2 panes (photos 79-81)
        pane_x(m, 1, x1, Z(7.8 + 5.1 * k), 3.9, 1.7, 2.8)
    LOW = [t for t in (7.9 + 2.85 * j for j in range(33)) if t < 98 and not (12.2 < t < 16.0 or 43.3 < t < 46.2 or 46.0 < t < 68.5)]
    for t in LOW:                                                    # small lower windows
        pane_x(m, 1, x1, Z(t), 1.1, 1.0, 1.1)
    m.box(x1, x1 + 0.9, 3.4, 3.55, z0, Z(68.5), WHITE)               # lean-to ledge between the storeys
    m.box(x1, x1 + 0.9, 3.4, 3.55, Z(46.0), z1, WHITE)
    door_x(m, 1, x1, Z(14.1), 1.0, 2.1)
    door_x(m, 1, x1, Z(44.7), 1.0, 2.1, leaf=DGREY)
    m.box(x1, x1 + 3.0, 0, 3.7, Z(67.0), Z(47.0), WHITE)             # one-storey block against the wall (photo 81)
    m.box(x1 - 0.1, x1 + 3.2, 3.7, 3.95, Z(67.2), Z(46.8), TEAL)
    door_x(m, 1, x1 + 3.0, Z(52.8), 1.0, 2.1)
    door_x(m, 1, x1 + 3.0, Z(61.1), 1.0, 2.1)
    pane_x(m, 1, x1 + 3.0, Z(57.0), 1.1, 1.0, 1.1)
    # wing end (south face): two tall upper windows, door and small window below
    for xc in (x1 - 2.8, x1 - 7.2):
        pane_z(m, 1, zw, xc, 3.9, 1.7, 2.8)
    door_z(m, 1, zw, x1 - 2.2, 1.0, 2.1)
    pane_z(m, 1, zw, x1 - 6.2, 1.1, 1.0, 1.1)

    # south face of the hall
    def solid(ua, ub, wins=False):
        xa, xb = U(ub), U(ua)
        m.box(xa, xb, 0, 5.5, z1, z1 + 0.12, TEAL)
        n = max(1, int(round((xb - xa) / 3.4)))
        for k in range(1, n):
            m.box(xa + (xb - xa) * k / n - 0.04, xa + (xb - xa) * k / n + 0.04, 0, 5.5, z1 + 0.12, z1 + 0.15, DGREY)
        if wins:
            for k in range(4):
                pane_z(m, 1, z1 + 0.12, xa + (xb - xa) * (k + 1) / 5, 1.4, 1.1, 0.55, cols=2, rows=1, fw=0.06)

    def glazed(ua, ub, sill=2.2, pitch=1.15):
        xa, xb = U(ub), U(ua)
        m.box(xa, xb, 0, sill, z1, z1 + 0.12, TEAL)
        m.box(xa, xb, sill, 5.5, z1, z1 + 0.05, DARK)
        n = max(2, int(round((xb - xa) / pitch)))
        for i in range(n + 1):
            x = xa + (xb - xa) * i / n
            m.box(x - 0.05, x + 0.05, sill, 5.5, z1, z1 + 0.14, TEAL)
        y = sill
        while y < 5.5:
            m.box(xa, xb, y - 0.04, y + 0.04, z1, z1 + 0.14, TEAL)
            y += 0.8
        m.box(xa, xb, 5.42, 5.55, z1, z1 + 0.16, TEAL)

    glazed(10.0, 23.5)
    solid(23.5, 37.0, wins=True)
    glazed(37.0, 48.0)
    m.box(U(50.0), U(48.0), 0, H, z1, z1 + 0.25, WHITE)             # pilaster under the lettering
    glazed(50.0, 78.0, sill=1.1, pitch=2.5)                         # lobby glazing (2014 aerial)
    m.box(U(79.5), U(78.0), 0, H, z1, z1 + 0.25, WHITE)             # second pilaster
    glazed(79.5, 88.4, sill=1.1, pitch=2.5)
    xa, xb = U(71.8), U(68.6)                                       # glass entrance doors in the lobby: frame, centre post, push bars
    m.box(xa, xb, 0.0, 2.6, z1 + 0.04, z1 + 0.2, DARK)
    for x in (xa, (xa + xb) / 2 - 0.05, xb - 0.1):
        m.box(x, x + 0.1, 0.0, 2.7, z1 + 0.04, z1 + 0.24, WHITE)
    for y in (0.0, 2.6):
        m.box(xa, xb, y, y + 0.1, z1 + 0.04, z1 + 0.24, WHITE)
    for x in ((xa + xb) / 2 - 0.35, (xa + xb) / 2 + 0.25):
        m.box(x, x + 0.1, 0.9, 1.1, z1 + 0.2, z1 + 0.3, DGREY)
    m.box(U(72.6), U(67.8), 2.85, 3.0, z1, z1 + 1.3, TEAL)          # small canopy over them
    m.box(x0, x0 + 1.2, 0, H, z1, z1 + 0.2, WHITE)                  # corner post
    m.box(x0, xm, 5.5, 5.6, z1, z1 + 0.3, TEAL)                     # door header
    # teal awning over the door in the third glazed bay (Commons photo; aerial)
    ac, aw, ad = U(40.0), 3.6, 1.9
    q = lambda x, y, z: (x, y, z)
    m.poly([q(ac - aw, 3.9, z1), q(ac + aw, 3.9, z1), q(ac + aw, 3.15, z1 + ad), q(ac - aw, 3.15, z1 + ad)], TEAL, (ac, 0, z1 + 1))
    m.poly([q(ac - aw, 3.5, z1 + 0.1), q(ac + aw, 3.5, z1 + 0.1), q(ac + aw, 3.0, z1 + ad - 0.1), q(ac - aw, 3.0, z1 + ad - 0.1)], DARK, (ac, 6, z1 + 1))
    m.poly([q(ac - aw, 3.9, z1), q(ac - aw, 3.15, z1 + ad), q(ac - aw, 3.0, z1 + ad)], TEAL, (ac, 3, z1 + 1))
    m.poly([q(ac + aw, 3.9, z1), q(ac + aw, 3.0, z1 + ad), q(ac + aw, 3.15, z1 + ad)], TEAL, (ac, 3, z1 + 1))
    rect_sign(m, U(48.8), 7.1, z1 + 0.06, (0, 1), 36.0, 1.4, "museum", 0.0, 0.5)   # ALBERTA AVIATION MUSEUM with the two V marks
    # east wall (-X): 15 tall upper windows (18 bays from 7.2 m at 5.1 m; the porch block hides k = 11-13), a low lean-to with small windows
    for k in list(range(0, 11)) + list(range(14, 18)):
        pane_x(m, -1, x0, Z(7.2 + 5.1 * k), 4.6, 1.7, 2.8)
    m.box(x0 - 3.5, x0, 0, 3.4, z0, z1, WHITE, top=True)             # lean-to, full length from the south face
    m.box(x0 - 3.7, x0, 3.4, 3.65, z0 - 0.2, z1 + 0.2, TEAL)
    LOWE = [t for t in (6.0 + 2.55 * j for j in range(38)) if t < 98 and not (56.0 < t < 80.0)]
    for t in LOWE:
        pane_x(m, -1, x0 - 3.5, Z(t), 1.3, 1.0, 1.1)
    door_z(m, 1, z1, x0 - 1.0, 1.0, 2.1)                              # lean-to south end: door and window
    pane_z(m, 1, z1, x0 - 2.6, 1.3, 1.0, 1.1)
    m.box(x0 - 3.5, x0, 3.65, 7.2, Z(78.0), Z(59.0), WHITE)          # porch block at 59-78 m
    m.box(x0 - 3.7, x0, 7.2, 7.45, Z(78.2), Z(58.8), TEAL)
    door_x(m, -1, x0 - 3.5, Z(68.5), 1.0, 2.1)
    for t in (62.5, 74.0):
        pane_x(m, -1, x0 - 3.5, Z(t), 1.3, 1.0, 1.1)
    for xc in [x0 + 3 + 6.7 * i for i in range(11)]:                  # north end: tall upper windows
        pane_z(m, -1, z0, xc, 4.6, 1.7, 2.8)
    cx, hw = (x0 + xm) / 2, (xm - x0) / 2                              # vents sit on the gable pitch
    roof_vents(m, [(cx + dx, dz) for dx in (-20, 20) for dz in (-30, 0, 30)], lambda x, z: H + 0.5 + 2.6 * (1 - abs(x - cx) / hw) - 0.1)
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
    m = fmesh()
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
    m.box(bx1 - 12.0, bx1 + 0.1, 0, 8.4, bz1 - 6.0, bz1 + 0.12, CREAM)  # cream block pier at the NE end, x 28..40; stands 12 cm proud of B's airside face (it z-fought: teal / tan vs cream)
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
    number_disc(m, cx0 + 4.0, 6.2, cz0, (0, -1), 0.95, "18")  # landside roundel high at the NW end of the office wing (Street View 5, 52 Airport Rd)
    number_disc(m, cx0, 6.2, (cz0 + cz1) / 2, (-1, 0), 0.95, "18")  # and on the wing's north (NW end) wall
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
    m = fmesh()
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
    door track).  Walls 16.7 m (a third above Hangar 38), ridge 19.7 m; "39" roundel position assumed."""
    m = fmesh()
    W, D, wh, rise = 107.0, 90.5, 16.7, 3.0  # side wall a third taller than Hangar 38's 12.5 m (user, 2026-10-21; photo 13207457714)
    x0, x1, z0, z1 = -W / 2, W / 2, -D / 2, D / 2
    bw, wing = 47.0, 12.0
    zb = z0 + wing  # bays run from the back wing to the front
    gx0, gx1 = x0 + bw, x1 - bw
    for bx0, bx1 in ((x0, x0 + bw), (x1 - bw, x1)):
        m.box(bx0, bx1, 0, wh, zb, z1, PBLUE, top=False)
        m.gable(bx0, bx1, wh, rise, zb, z1, along_z=True, sw_roof=METAL, sw_wall=PBLUE)
        xs = [bx0 + 4.0 + 6.5 * i for i in range(7)]
        m.box(xs[0], xs[-1], 0, 15.3, z1, z1 + 0.05, DARK)
        leaves(m, z1, xs, 0, 15.0, RWHITE, post=DGREY)
        louvres(m, z1, xs, [(4.4, 7.2), (10.4, 13.6)], sw=TAN)
        m.box(xs[0], xs[-1], 15.0, 15.5, z1, z1 + 0.5, DGREY)
        for px0, px1 in ((bx0, bx0 + 3.6), (bx1 - 3.0, bx1)):  # piers projecting past the door wall
            m.box(px0, px1, 0, wh + 0.4, z1, z1 + 1.1, PBLUE)
    # set-back middle block between the bays
    zm = z1 - 14.0
    m.box(gx0, gx1, 0, 12.5, zb, zm, PBLUE)
    m.box(gx0, gx1, 12.5, 12.8, zb, zm + 0.1, DGREY)
    m.box(gx0 + 2.0, gx0 + 7.0, 0, 4.2, zm, zm + 0.12, RWHITE)  # roller door
    for dx in (gx0 + 9.0, gx1 - 1.6):
        m.box(dx, dx + 1.1, 0, 2.2, zm, zm + 0.1, DGREY)
    # steel truss frame across the gap at the front
    for y in (15.8, 17.8, 19.6):
        m.box(gx0, gx1, y, y + 0.35, z1 + 0.5, z1 + 0.9, DGREY)
    for k in range(5):
        m.box(gx0 + 1.0 + k * 2.8, gx0 + 1.3 + k * 2.8, 15.8, 19.6, z1 + 0.5, z1 + 0.9, DGREY)
    # back wing across the full width
    m.box(x0, x1, 0, 10.0, z0, zb, PBLUE)
    m.box(x0, x1, 10.0, 10.4, z0 - 0.1, zb + 0.1, DGREY)
    rows_z(m, -1, z0, x0 + 3.0, x1 - 3.0, 6.0, 20, 2.4, 1.6)
    rows_z(m, -1, z0, x0 + 3.0, x1 - 3.0, 2.0, 12, 2.4, 1.6)
    for sgn, xp in ((1, x1), (-1, x0)):  # end walls
        rows_x(m, sgn, xp, zb + 4.0, z1 - 6.0, 11.5, 8, 1.6, 1.1)
        rows_x(m, sgn, xp, z0 + 2.0, zb - 2.0, 5.0, 3, 1.6, 1.2)
    number_disc(m, x1, 14.2, z1 - 14.0, (1, 0), 1.4, "39")
    number_disc(m, 0.0, 10.0, zm + 0.12, (0, 1), 1.4, "39")  # airside roundel on the set-back middle block above the roller door (user, 2026-10-21)
    number_disc(m, x0 + bw / 2, 14.6, zb, (0, -1), 1.3, "39")  # landside roundel high on the back wall above the low wing
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
    m = fmesh()
    # north wing x -86..-51.5, z -8..17
    m.box(-86.0, -51.5, 0, 9.5, -8.0, 17.0, BRICKD, top=False)
    m.box(-86.2, -51.3, 9.5, 10.0, -8.2, 17.2, DGREY)
    rows_z(m, -1, -8.0, -84.0, -53.5, 2.4, 6, 2.2, 1.6)
    rows_z(m, -1, -8.0, -84.0, -53.5, 6.2, 6, 2.2, 1.6)
    rows_z(m, 1, 17.0, -84.0, -53.5, 2.4, 6, 2.2, 1.6)
    rows_z(m, 1, 17.0, -84.0, -53.5, 6.2, 6, 2.2, 1.6)
    rows_x(m, -1, -86.0, -6.0, 15.0, 4.0, 4, 2.2, 1.8)
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
    # lower cream landside wing x -50..8, z -21..-4 with a glazed entrance bay
    m.box(-50.0, 8.0, 0, 4.6, -21.0, -4.0, CREAM, top=False)
    m.box(-50.2, 8.2, 4.6, 5.0, -21.2, -3.8, DGREY)
    rows_z(m, -1, -21.0, -48.0, 6.0, 1.2, 12, 2.4, 1.8)
    m.box(-12.0, 4.0, 0, 3.6, -21.1, -21.0, GLASS)
    m.box(-14.0, 6.0, 3.6, 3.9, -24.0, -21.0, CREAM)  # entrance canopy
    # inner courtyard roof between the wings
    m.box(-40.0, 8.0, 5.0, 5.2, -21.0, -4.0, DGREY)
    # SE end (archive photos MS-1270.213.1 and .3, 2013): a two-storey brick wall set back at z -13 (x 8..40) behind a deep landside canopy with
    # red struts, then the block (x 40..76, z -19) with two "21" roundels (one on the set-back wall, one on the block), and the glazed viewing
    # lounge cantilevered from the upper floor at the SE corner.
    m.box(8.0, 40.0, 0, 9.5, -13.0, 13.0, BRICKD, top=False)
    m.box(7.8, 40.2, 9.5, 10.0, -13.2, 13.2, DGREY)
    m.box(40.0, 76.0, 0, 9.5, -19.0, 13.0, BRICKD, top=False)
    m.box(39.8, 76.2, 9.5, 10.0, -19.2, 13.2, DGREY)
    m.box(9.0, 39.0, 0.3, 3.1, -13.15, -13.0, GLASS)  # glazed doors under the canopy
    m.box(8.0, 40.0, 4.1, 4.6, -23.0, -13.0, CREAM)  # canopy slab with a pale ribbed fascia
    for x in (10.0, 18.0, 26.0, 34.0, 39.0):
        m.box(x, x + 0.6, 0, 4.1, -23.0, -22.4, RED)
    for x in range(9, 40, 5):  # red struts rising from the canopy edge to the roof edge
        rod(m, x, 4.6, -22.8, 10.0, -13.3, 0.3, RED)
    rows_z(m, -1, -13.0, 10.0, 28.0, 6.0, 3, 2.2, 1.6)
    number_disc(m, 32.0, 7.8, -13.1, (0, -1), 1.2, "21")
    number_disc(m, 45.0, 6.6, -19.1, (0, -1), 1.4, "21")
    rows_z(m, -1, -19.0, 48.0, 58.0, 5.3, 2, 2.2, 1.6)
    m.box(41.0, 43.5, 0, 2.4, -19.1, -19.0, DARK)  # service door
    m.box(48.0, 58.0, 3.5, 4.0, -19.9, -19.0, CREAM)  # small canopy over the entrance
    rows_z(m, -1, -19.0, 62.0, 74.0, 1.0, 3, 2.6, 1.4)
    # viewing lounge x 56..76, upper floor, on the APRON (NE) face at the SE end so it looks east toward the runways (user, 2026-10-21: it had
    # been put on the landside); glazed on the apron face and the SE end under a sloping glass roof
    lz0, lz1 = 13.0, 16.6
    m.box(56.0, 76.0, 4.2, 4.8, lz0, lz1, DGREY)
    m.box(56.0, 76.0, 4.8, 8.6, lz0, lz1, GLASS, top=False)
    for x in [56.0 + 4.0 * i for i in range(6)]:
        m.box(x, x + 0.15, 4.8, 8.6, lz1, lz1 + 0.15, DGREY)
    m.poly([(56.0, 8.6, lz1), (76.0, 8.6, lz1), (76.0, 9.6, lz0), (56.0, 9.6, lz0)], GLASS, (66.0, 4.0, (lz0 + lz1) / 2))
    for x in (56.0, 76.0):  # triangular glass sides under the sloping roof
        m.poly([(x, 8.6, lz0), (x, 8.6, lz1), (x, 9.6, lz0)], GLASS, (66.0 if x > 60 else 66.0, 6.0, (lz0 + lz1) / 2))
    for x in (60.0, 72.0):  # two slim columns carrying the cantilever
        m.box(x, x + 0.5, 0, 4.2, lz1 - 0.6, lz1 - 0.1, DGREY)
    rows_x(m, 1, 76.0, -17.0, 11.0, 2.0, 5, 3.0, 1.6)
    rows_x(m, 1, 76.0, -17.0, 11.0, 6.0, 5, 3.0, 1.6)
    roof_vents(m, [(-70, 4), (-65, 10), (0, 5), (10, 8), (50, 0), (60, 6)], 10.0)
    # covered walkway from the garage straight into the spine's landside wall (user, 2026-10-21: it used to stop on the low wing's roof, hanging).
    # It runs on piers, passes over the low cream wing at a floor height just above that roof, and ends flush in the spine wall (7.6 m).
    m.box(-41.0, -34.0, 5.2, 7.4, -52.0, -4.0, BRICKD)
    m.box(-41.2, -33.8, 7.4, 7.7, -52.2, -3.8, DGREY)
    for z in (-46.0, -36.0, -28.0):
        for x in (-40.6, -34.6):
            m.box(x, x + 0.6, 0, 5.2, z, z + 0.6, CREAM)
    for z in (-40.0, -31.0, -24.0, -12.0):  # window slots along both sides
        m.window((1, 0, 0), (-34.0, 5.8, z), (0, 0, 1), 3.5, 1.1)
        m.window((-1, 0, 0), (-41.0, 5.8, z), (0, 0, 1), 3.5, 1.1)
    # gate annexes: the jetway roots stand at the face of the building (see CYXD.xml, gates 7, 10, 11, 12); each gets a small boarding bay with a
    # door where the bridge docks (user, 2026-10-21: the jetways did not attach to the building).  Authored x = footprint x - 5, z = footprint z - 17.5.
    for xc in (-39.7, -7.0, 25.0):
        m.box(xc - 2.6, xc + 2.6, 0, 4.6, 13.0, 17.4, CREAM, top=False)
        m.box(xc - 2.8, xc + 2.8, 4.6, 4.9, 12.9, 17.5, DGREY)
        m.window((0, 0, 1), (xc - 1.0, 0.0, 17.4), (1, 0, 0), 2.0, 2.7)
    m.box(-88.4, -86.0, 0, 4.6, 2.0, 7.0, CREAM, top=False)  # gate 7, on the north wing's NW end wall
    m.box(-88.6, -85.9, 4.6, 4.9, 1.9, 7.1, DGREY)
    m.window((-1, 0, 0), (-88.4, 0.0, 3.0), (0, 0, 1), 2.0, 2.7)
    # centre the whole footprint (x -86..76, z -52..17) on the origin
    m.pos = [(x + 5.0, y, z + 17.5) for x, y, z in m.pos]
    m.mirror_x()
    return m


def garage22():
    """Terminal parking garage ("22" roundel), an OPEN parkade (user, 2026-10-21: it is open in real life, give it a ground deck and leave the sides open).
    Levels stepping down toward the SE end (decks at 10.4 / 7.2 / 4.0 m, reaching x 30 / 40 / 50); every deck is a concrete slab with a 1.1 m brown
    cladding band on its rim, and between the band and the slab above is an open slot with the precast columns standing in it (Street View 15-18).
    Mk 5 (user, 2026-10-21): (1) only perimeter columns (clear spans inside); (2) the decks are not flat: the aerial (terminal21-2017-overlay.png)
    shows a central bay starting about 45 % of the way along from the NW end that dips toward the SE, so every deck is a U (flat sides and NW end)
    round a ramp slab that descends at about 7 % to the level below (the lowest to the ground, where it is the vehicle entrance with a gate, island
    and yellow bollards as in Street View 16/17); (3) a second "22" board on the stair tower's long (SE) side.
    Footprint from the 2017 Wayback zoom-19 imagery: about 100 x 72 m, +Z = bearing 58 (NE, toward the terminal), +X = bearing 148."""
    m = fmesh()
    x0, x1, z0, z1 = -50.0, 50.0, -36.0, 36.0
    GH, SL, GC = 3.2, 0.5, 3.5  # level height, slab thickness, ground-floor clearance under the lowest slab
    BW, XA = 15.0, -14.0  # half width of the dipping bay, x where the dip starts (same for every deck, so the ramps are parallel)
    SLOPE = GH / 44.0
    YG = 0.08  # ramp foot at the ground
    decks = [(4.0, x1), (7.2, 40.0), (10.4, 30.0)]

    def ramp_y(yd, x):
        return yd - SLOPE * (x - XA)

    def columns(xa, xb, ya, yb):
        """Perimeter columns only (clear spans inside); none in the dipping bay's mouth."""
        nx, nz = max(1, round((xb - xa) / 8.3)), 8
        for i in range(nx + 1):
            x = xa + 0.4 + i * (xb - xa - 0.8) / nx
            for j in range(nz + 1):
                if not (j in (0, nz) or i in (0, nx)):
                    continue
                z = z0 + 0.4 + j * (z1 - z0 - 0.8) / nz
                if abs(z) < BW + 0.5 and x > XA:
                    continue
                m.box(x - 0.4, x + 0.4, ya, yb, z - 0.4, z + 0.4, CREAM)
                if j in (0, nz) and yb - ya > 2.0:  # the corbelled column heads on the outer faces
                    m.box(x - 0.6, x + 0.6, yb - 0.5, yb, z - 0.5 if j == 0 else z - 0.4, z + 0.4 if j == 0 else z + 0.5, TAN)

    def prism_z(prof, za, zb, sw):
        """Convex xy profile extruded between z = za and zb."""
        c = (sum(p[0] for p in prof) / len(prof), sum(p[1] for p in prof) / len(prof), (za + zb) / 2)
        m.poly([(x, y, za) for x, y in prof], sw, c)
        m.poly([(x, y, zb) for x, y in prof], sw, c)
        for i in range(len(prof)):
            (xa, ya), (xb, yb) = prof[i], prof[(i + 1) % len(prof)]
            m.poly([(xa, ya, za), (xb, yb, za), (xb, yb, zb), (xa, ya, zb)], sw, c)

    def flat_slab(xa, xb, za, zb, yd):
        m.box(xa, xb, yd - SL, yd, za, zb, TAN, top=False)
        m.poly([(xa, yd, za), (xb, yd, za), (xb, yd, zb), (xa, yd, zb)], DGREY, (0.0, yd - 5.0, 0.0))  # deck surface
        m.poly([(xa, yd - SL, za), (xb, yd - SL, za), (xb, yd - SL, zb), (xa, yd - SL, zb)], DGREY, (0.0, yd + 5.0, 0.0))  # underside

    m.poly([(x0, 0.03, z0), (x1, 0.03, z0), (x1, 0.03, z1), (x0, 0.03, z1)], DGREY, (0.0, -5.0, 0.0))  # the ground deck
    columns(x0, x1, 0.03, GC)
    for k, (yd, X) in enumerate(decks):
        # U-shaped deck: flat slabs along both sides and across the NW end, the centre bay is a ramp down to the level below
        flat_slab(x0, X, z0, -BW, yd)
        flat_slab(x0, X, BW, z1, yd)
        flat_slab(x0, XA, -BW, BW, yd)
        xe = min(X, XA + (yd - YG) / SLOPE) if k == 0 else X  # the lowest ramp ends where it meets the ground
        ye = max(ramp_y(yd, xe), YG)
        te = SL if k else 0.04
        m.poly([(XA, yd, -BW), (xe, ye, -BW), (xe, ye, BW), (XA, yd, BW)], DGREY, (XA, yd - 5.0, 0.0))  # ramp surface
        m.poly([(XA, yd - SL, -BW), (xe, ye - te, -BW), (xe, ye - te, BW), (XA, yd - SL, BW)], DGREY, (XA, yd + 5.0, 0.0))  # ramp underside
        m.poly([(xe, ye, -BW), (xe, ye, BW), (xe, ye - te, BW), (xe, ye - te, -BW)], TAN, (xe - 1.0, ye, 0.0))  # ramp end
        # deep edge beams under the side slabs, down to the ramp (the dark walls along the bay in the aerial)
        xs = XA + SL / SLOPE
        prof = [(xs, yd - SL), (X, yd - SL)]
        if k == 0:
            prof += [(X, YG), (xe, YG)]
        else:
            prof += [(X, ye)]
        for za, zb in ((BW, BW + 0.3), (-BW - 0.3, -BW)):
            prism_z(prof, za, zb, TAN)
        # brown cladding band on the rim (open at the SE end of the bay) and a rail along the bay's top edge
        m.box(x0 - 0.1, X + 0.1, yd, yd + 1.1, z0 - 0.1, z0 + 0.2, BRONZE)
        m.box(x0 - 0.1, X + 0.1, yd, yd + 1.1, z1 - 0.2, z1 + 0.1, BRONZE)
        m.box(x0 - 0.1, x0 + 0.2, yd, yd + 1.1, z0 + 0.2, z1 - 0.2, BRONZE)
        m.box(X - 0.2, X + 0.1, yd, yd + 1.1, z0 + 0.2, -BW, BRONZE)
        m.box(X - 0.2, X + 0.1, yd, yd + 1.1, BW, z1 - 0.2, BRONZE)
        m.box(XA, X, yd, yd + 0.9, BW, BW + 0.25, TAN)
        m.box(XA, X, yd, yd + 0.9, -BW - 0.25, -BW, TAN)
        if k + 1 < len(decks):
            columns(x0, min(X, decks[k + 1][1]), yd, yd + GH - SL)
    # entrance at the SE end (Street View 16/17): the lowest ramp meets the ground between the edge beams; a gate island with two ticket posts,
    # a short barrier boom over each lane and yellow bollards, just outside the mouth
    m.box(50.5, 56.0, 0, 0.2, -0.9, 0.9, TAN)
    for xp in (52.0, 54.0):
        m.box(xp - 0.2, xp + 0.2, 0.2, 1.5, -0.35, 0.35, DGREY)
    for zb0, zb1 in ((0.9, 3.0), (3.0, 5.0), (5.0, 7.0), (-3.0, -0.9), (-5.0, -3.0), (-7.0, -5.0)):
        stripe = RED if (int(abs(zb0)) // 2) % 2 == 0 else WHITE
        m.box(52.0, 52.12, 1.1, 1.22, zb0, zb1, stripe)
    for xb_, zb_ in ((50.8, -0.7), (50.8, 0.7), (55.6, -0.7), (55.6, 0.7), (52.0, -7.4), (52.0, 7.4)):
        m.box(xb_ - 0.2, xb_ + 0.2, 0, 1.0, zb_ - 0.2, zb_ + 0.2, YELLOW)
    # stair tower at the NW end (angled wall in the photos) with the "22" roundel on its NE face and a second one on its SE (long-side) face,
    # and the lift housing on the roof
    m.box(-49.5, -41.5, 10.4, 15.0, 22.0, 30.0, TAN)
    m.box(-49.7, -41.3, 15.0, 15.3, 21.8, 30.2, DGREY)
    m.box(-52.0, -50.0, 11.4, 13.0, 20.0, 27.0, CREAM)
    number_disc(m, -45.5, 12.7, 30.0, (0, 1), 1.4, "22")
    number_disc(m, -41.5, 12.7, 26.0, (1, 0), 1.4, "22")
    m.box(-24.0, -21.0, 10.4, 13.4, -3.0, 3.0, DGREY)  # roof lift housing (in the aerial it stands on the flat part, before the dip)
    m.mirror_x()
    return m


# Second hangar by Kingsway ("orange", 1930s-1982) --------------------------------------------
# Proper position: centre 53.56945, -113.52610 (about +-50 m, placed on the 1944 aerial from the 118 Ave / Kingsway junction; docs/cyxd/open-questions.md),
# heading 57.78 (front to the NE apron), footprint now 76 x 52 m (was 70 x 44; EA-207-440, 1990).  At that spot the exclusion polygon (footprint + 6 m) also removes the Chateau Nova Hotel
# (OSM way 230718905, 109 x 88 m, its NE corner reaches into the footprint).  To keep the hotel the whole model is moved ORANGE_SHIFT_NE_M metres toward
# the apron (18 m since the 2026-10-21 enlargement: the back edge stays where it was, the front grows), which also puts the exclusion 3 m short of Blue (the 1938 hangar).  To bring it back to its proper position set ORANGE_SHIFT_NE_M = 0.0
# (and accept losing the hotel, or rebuild the hotel as a model).  The size is now 76 x 52 m (photo EA-207-440); at shift 0 the back edge would
# be 8 m further SW, so lower the shift to 10 if the hotel is gone.
ORANGE_LAT, ORANGE_LON, ORANGE_HDG = 53.56945, -113.52610, 57.78
ORANGE_SHIFT_NE_M = 18.0


def _orange_pos():
    a = math.radians(ORANGE_HDG)
    return (ORANGE_LAT + ORANGE_SHIFT_NE_M * math.cos(a) / 111200.0, ORANGE_LON + ORANGE_SHIFT_NE_M * math.sin(a) / 66170.0)


def hangar_second():
    """The second barrel-vault hangar beside Kingsway, still standing in 1990 (user's "orange"; postcard PC013987 far hangar, City Archives ET-28-900 of 1982,
    EA-207-440 of 1990 = Hudson General, the 1944 aerial).  Massing only: a pale two-storey flat-roofed wing with ribbon windows and a red band at the left,
    brick towers flush with the front at the ends of the barrel-vault hall, the hall with a dark roof and a big door opening under its arched front, a low
    service block behind the wing.
    Frame: +Z = front (NE, apron), +X = right of the front; footprint x -38..38, z -26..26.  Details of the wing and the towers are guesses.
    Size from EA-207-440 (2026-10-21): the blue front wall of the 1990 hall is about 12 window bays wide and the pickups and sedan on the road give a ground-plane
    scale of 14-25 px/m at the wall, so the hall front is 50-75 m wide, its eaves 7-12 m and its apex 13-24 m.  Taken: span 53 m, eaves 10 m, apex 18.5 m
    (the first model was 38 m, 7 m and 12.5 m and read as small beside the photo)."""
    m = fmesh()
    zf, zb = 26.0, -26.0
    # wing x -38..-26: pale cream, two storeys, flat roof, red band under the parapet
    wx0, wx1, wh = -38.0, -26.0, 8.8
    m.box(wx0, wx1, 0, wh, -4.0, zf, CREAM, top=False)
    m.box(wx0 - 0.2, wx1 + 0.2, wh, wh + 0.4, -4.2, zf + 0.2, DGREY)
    m.box(wx0, wx1, wh - 1.4, wh - 0.9, zf, zf + 0.1, RED)
    for y in (1.6, 4.9):
        rows_z(m, 1, zf, wx0, wx1, y, 3, 2.4, 1.8)
        rows_x(m, -1, wx0, -2.0, zf - 1.0, y, 4, 2.4, 1.8)
    m.box(-33.0, -31.0, 0, 2.4, zf, zf + 0.1, DARK)  # entrance
    m.box(wx0, wx1, 0, 5.0, zb, -4.0, CREAM, top=True)  # low service block behind the wing
    # barrel-vault hall x -21..32 (span 53), z -26..26: eaves 10 m, apex 18.5 m
    xh0, xh1, wall, rise = -21.0, 32.0, 10.0, 8.5
    m.box(xh0, xh1, 0, wall, zb, zf, CREAM, top=False)
    n = 20
    prof = [(-math.cos(math.pi * i / n) * (xh1 - xh0) / 2 + (xh0 + xh1) / 2, wall + math.sin(math.pi * i / n) * rise) for i in range(n + 1)]
    for i in range(n):
        (xa, ya), (xb, yb) = prof[i], prof[i + 1]
        m.poly([(xa, ya, zb), (xb, yb, zb), (xb, yb, zf), (xa, ya, zf)], METAL, (0, wall - 3, 0))
    for z in (zf, zb):
        m.poly([(xh0, wall, z)] + [(x, y, z) for x, y in prof] + [(xh1, wall, z)], CREAM, (0, wall, 0))
    m.box(xh0 + 3.0, xh1 - 3.0, 0, 9.0, zf, zf + 0.1, DARK)  # door opening
    nl = 6
    dw = (xh1 - xh0 - 6.0) / nl
    for k in range(nl):
        m.box(xh0 + 3.1 + k * dw, xh0 + 3.0 + (k + 1) * dw - 0.1, 0, 8.8, zf + 0.1, zf + 0.3, DOORG)
    window_row(m, xh0 + 8.0, xh1 - 8.0, wall + 1.0, zf, 7, 1.4, 1.2, (0, 0, 1), "x")
    for sgn in (-1, 1):
        for i in range(8):
            m.window((sgn, 0, 0), (xh0 if sgn < 0 else xh1, 3.0, zb + 4 + i * 6.0), (0, 0, 1), 3.0, 4.5)

    def brick_tower(x0, x1, h, floors):
        z0 = zf - (x1 - x0)
        m.box(x0, x1, 0, h, z0, zf, BRICKD, top=False)
        m.box(x0 - 0.2, x1 + 0.2, h, h + 0.5, z0 - 0.2, zf + 0.2, CREAM)
        for f in range(floors):
            y = 1.6 + f * (h - 3.0) / floors
            m.window((0, 0, 1), (x0 + 1.0, y, zf), (1, 0, 0), x1 - x0 - 2.0, 1.8)
            m.window((0, 0, -1), (x0 + 1.0, y, z0), (1, 0, 0), x1 - x0 - 2.0, 1.8)
    brick_tower(-26.0, -21.0, 14.5, 3)
    brick_tower(32.0, 38.0, 17.0, 4)
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
    ("cyxd_hangar_second", "Second hangar by Kingsway (1930s-1982; barrel vault, pale wing, brick towers)", hangar_second, *_orange_pos(), ORANGE_HDG, 76.0, 52.0),
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
    # Alberta Aviation Museum frontage (Bomarc, Norseman, memorial, Voodoo): origins are the OSM nodes, no exclusions needed
    import display_aircraft
    for name, title, fn, lat, lon in display_aircraft.DISPLAY:
        out.append((title, "%.8f" % lat, "%.8f" % lon, "0", fn().save(modellib / name, name)))
    # a generated building stood off the SE end of the old terminal (user, 2026-10-21, sim screenshot): clear the surroundings of the SE end and the
    # landside beside it (terminal frame, +Z = bearing 51, +X = bearing 141)
    excl.append(("Old terminal: SE end and landside surroundings", footprint("53.57094000", "-113.52317800", "51", -20.0, 150.0, -95.0, -18.0)))
    # the building between the garage and the terminal survived that (user, 2026-10-21): clear the whole block with polygons AND with an object
    # rectangle (a base-scenery object is not covered by the building polygons), terminal frame x -100..100, z -130..45 (garage and terminal plus walkway)
    block = footprint("53.57094000", "-113.52317800", "51", -100.0, 100.0, -130.0, 45.0)
    excl.append(("Old terminal and parking garage: whole block", block))
    OBJECT_RECTS.append(("old terminal and garage: remove sim-placed objects between them", block))
    # trees pushing through Hangars 38 / 39 / 40 and between 38 and 39 (user, 2026-10-21): vegetation-free hull round all three plus a margin
    pts = []
    for name, title, fn, lat, lon, hdg, W, D in HANGARS:
        if name in ("cyxd_hangar38", "cyxd_hangar39", "cyxd_hangar40"):
            pts += footprint("%.8f" % lat, "%.8f" % lon, "%g" % hdg, -W / 2 - 14.0, W / 2 + 14.0, -D / 2 - 14.0, D / 2 + 14.0)
    VEG_EXCL.append(("Hangars 38, 39 and 40 and the ground between them", _hull(pts)))
    # trees in the strip between the garage and the terminal's landside (user, 2026-10-21; the conifer rows in the 2017 aerial), terminal frame
    VEG_EXCL.append(("Between the parking garage and the old terminal", footprint("53.57094000", "-113.52317800", "51", -60.0, 100.0, -62.0, -22.0)))


OBJECT_RECTS = []  # (title, corners): ExclusionRectangle for base-scenery objects, written by gen_buildings.main()
VEG_EXCL = []  # (title, corners): polygons that also remove trees


def _hull(pts):
    """Convex hull of (lat, lon) points (monotone chain), counter-clockwise."""
    p = sorted(set(pts))
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for q in p:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], q) <= 0:
            lo.pop()
        lo.append(q)
    for q in reversed(p):
        while len(up) >= 2 and cross(up[-2], up[-1], q) <= 0:
            up.pop()
        up.append(q)
    return lo[:-1] + up[:-1]
