"""Exclusion polygons for the bridge models.

Each site's footprint is the plan-view union of every triangle of its meshes, grown by MARGIN metres and simplified, so the sim's own
buildings, photogrammetry (TIN) and OSM/MS building footprints are removed under and around the model but nowhere else.  A footprint that
falls into separate pieces gives one polygon per piece; holes are filled (the inside of a cloverleaf loop is excluded too).  The polygon
element and attribute set are the ones airport-cyxd/tools/gen_buildings.py writes (they work in the sim there).

footprints() must run before bridgelib.save_chunks, which mirrors the mesh in place.  Needs shapely.
"""
import uuid

NS = uuid.UUID("5d0c6c7e-0c1d-4a53-9b6e-0c7d00000003")
MARGIN = 4.0       # m, grown around the model
SIMPLIFY = 2.0     # m
MAX_VERTS = 120    # per polygon; the tolerance is raised until it fits
MIN_AREA = 150.0   # m2, drops slivers (isolated lamps, a stray rail) left after the union
GROUP = '\t<Group displayName="Ground Cover" groupID="6" groupGenerated="FALSE"/>\n'


def _no_holes(pieces):
    """A Polygon element has one ring, so a footprint with holes (the inside of a loop ramp) is cut in two along an east-west line
    through the first hole's centre, which opens the hole into a notch; repeat until no piece has a hole."""
    from shapely.geometry import box
    out, todo = [], list(pieces)
    while todo:
        g = todo.pop()
        if not g.interiors:
            out.append(g)
            continue
        minx, miny, maxx, maxy = g.bounds
        cy = g.interiors[0].centroid.y
        for half in (box(minx - 1, cy, maxx + 1, maxy + 1), box(minx - 1, miny - 1, maxx + 1, cy)):
            r = g.intersection(half)
            todo.extend(r.geoms if hasattr(r, "geoms") else [r])
            todo = [t for t in todo if t.geom_type == "Polygon" and not t.is_empty]
    return out


def footprints(res):
    """[[(lat, lon), ...], ...] for a build() result; coordinates are the mesh's (e, n) turned into lat/lon with the site frame."""
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    tris = []
    for _name, m in res["parts"]:
        P, I = m.pos, m.idx
        for k in range(0, len(I), 3):
            a, b, c = P[I[k]], P[I[k + 1]], P[I[k + 2]]
            area2 = (b[0] - a[0]) * (c[2] - a[2]) - (c[0] - a[0]) * (b[2] - a[2])
            if abs(area2) > 1e-4:
                tris.append(Polygon([(a[0], a[2]), (b[0], b[2]), (c[0], c[2])]))
    if not tris:
        return []
    # grow each triangle a little before the union so edge-sharing triangles fuse without needles from float noise
    geom = unary_union([t.buffer(0.05) for t in tris]).buffer(MARGIN, join_style=2)
    pieces = _no_holes(list(geom.geoms) if geom.geom_type == "MultiPolygon" else [geom])
    out = []
    for g in pieces:
        if g.area < MIN_AREA:
            continue
        ring = Polygon(g.exterior)
        tol = SIMPLIFY
        s = ring.simplify(tol)
        while len(s.exterior.coords) - 1 > MAX_VERTS:
            tol *= 1.5
            s = ring.simplify(tol)
        pts = list(s.exterior.coords)[:-1]
        if not s.exterior.is_ccw:    # counter-clockwise, like the CYXD polygons
            pts.reverse()
        out.append([res["frame"].ll(e, n) for e, n in pts])
    return out


def polygon_xml(title, alt, verts, key):
    guid = "{" + str(uuid.uuid5(NS, key)).upper() + "}"
    a = '\t\t<Attribute name="%s" guid="{%s}" type="%s" value="%s"/>'
    lines = ['\t<Polygon version="0.4.0" displayName="%s" parentGroupID="6" altitude="%.3f">' % (title.replace('"', "'")[:70], alt),
             a % ("UniqueGUID", "359C73E8-06BE-4FB2-ABCB-EC942F7761D0", "GUID", guid),
             a % ("ExcludeDetectedBuildings", "5C1A2387-1F07-47DF-A569-962CF6258E55", "UINT8", "1"),
             a % ("ExcludeOSMBuildings", "F3C2635D-9F2F-458F-8663-90B3837BED09", "UINT8", "1"),
             a % ("ExcludeMSBuildings", "F78A3074-8AD5-4B8B-92C4-C1C948BB7AA5", "UINT8", "1"),
             a % ("ExcludeTIN", "18B58CBF-AE02-4A19-8AA9-3809E8E73400", "UINT8", "1"),
             a % ("ExclusionFlags", "4CACC252-E6DC-419A-B20C-16EC601DF70E", "UINT32", "3")]
    lines += ['\t\t<Vertex lat="%.8f" lon="%.8f"/>' % v for v in verts]
    lines.append("\t</Polygon>")
    return "\n".join(lines)
