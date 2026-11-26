"""Add lower LODs to a saved flat-colour glTF model (any of this repo's model writers), so MSFS 2024 keeps drawing it far out.

    from model_lods import add_lods
    add_lods(folder, name)          # after <folder>/<name>.gltf, .bin and .xml are written

MSFS 2024 holds an LOD back until the model's bounding sphere fills a share of the screen height set by the LOD's vertex count (SDK,
"LOD Selection System"; on High: 1 % at 2,500 vertices, 2 % at 5,000, 12 % at 30,000; no floor under 1,000).  A model with one dense
LOD pops in late.  This writes <name>_lod1.gltf ... beside the model: its largest polygons (undersides dropped first, as they are not
seen from the air), down to 10,000, 2,500 and 950 vertices (a budget is used only when it is under 60 % of the model's count), and
rewrites the <LODS> block of <name>.xml with each LOD's minSize set to that floor (0 for the last).  A model of 1,000 vertices or
fewer is left as it is.  Materials, primitives, nodes and lights are kept; only the geometry is thinned.  The same method is
bridgelib.save_chunks' in scenery-edmonton-bridges (docs/edmonton-bridges/MODEL-NOTES.md, "Standard practice: LODs and draw
distance").

The writers give every polygon its own vertices (flat shading), so a polygon is a set of triangles joined by shared vertices.
"""
import json
import math
import re
import struct

VERTEX_FLOOR = [(1000, 0.0), (2500, 1.0), (5000, 2.0), (30000, 12.0), (60000, 24.0), (150000, 60.0)]
LOD_BUDGETS = (10000, 2500, 950)


def min_size_for(n):
    """The High-settings vertex floor for an LOD of n vertices, % of screen height, rounded down to 0.1."""
    if n <= VERTEX_FLOOR[0][0]:
        return 0.0
    for (n0, f0), (n1, f1) in zip(VERTEX_FLOOR, VERTEX_FLOOR[1:]):
        if n <= n1:
            return math.floor((f0 + (f1 - f0) * (n - n0) / (n1 - n0)) * 10) / 10
    return VERTEX_FLOOR[-1][1]


def _read(g, blob, a, fmt, size):
    acc = g["accessors"][a]
    v = g["bufferViews"][acc["bufferView"]]
    off = v.get("byteOffset", 0) + acc.get("byteOffset", 0)
    return [struct.unpack_from(fmt, blob, off + i * size) for i in range(acc["count"])]


def _load(folder, name):
    g = json.loads((folder / f"{name}.gltf").read_text())
    blob = (folder / g["buffers"][0]["uri"]).read_bytes()
    prim0 = g["meshes"][0]["primitives"][0]["attributes"]
    for p in g["meshes"][0]["primitives"]:
        assert p["attributes"] == prim0, "primitives must share one vertex set"
    pos = [p for p in _read(g, blob, prim0["POSITION"], "<3f", 12)]
    nrm = [p for p in _read(g, blob, prim0["NORMAL"], "<3f", 12)]
    uv = [p for p in _read(g, blob, prim0["TEXCOORD_0"], "<2f", 8)]
    tris = []                                            # (primitive, i, j, k)
    for pi, p in enumerate(g["meshes"][0]["primitives"]):
        acc = g["accessors"][p["indices"]]
        fmt, size = {5123: ("<H", 2), 5125: ("<I", 4)}[acc["componentType"]]
        ix = [i[0] for i in _read(g, blob, p["indices"], fmt, size)]
        tris += [(pi, ix[t], ix[t + 1], ix[t + 2]) for t in range(0, len(ix), 3)]
    return g, pos, nrm, uv, tris


def _polygons(n, tris):
    """Group triangles into polygons: triangles that share a vertex (union-find on vertices)."""
    parent = list(range(n))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for _p, i, j, k in tris:
        for b in (j, k):
            ra, rb = find(i), find(b)
            if ra != rb:
                parent[rb] = ra
    groups = {}
    for t, (_p, i, _j, _k) in enumerate(tris):
        groups.setdefault(find(i), []).append(t)
    return list(groups.values())


def _thin(pos, nrm, tris, polys, budget):
    """Indices of the polygons kept for a vertex budget: undersides last, then largest area first."""
    def info(ts):
        vs = {v for t in ts for v in tris[t][1:]}
        a = 0.0
        for t in ts:
            P, Q, R = (pos[v] for v in tris[t][1:])
            u = [Q[i] - P[i] for i in range(3)]
            w = [R[i] - P[i] for i in range(3)]
            c = (u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0])
            a += 0.5 * math.sqrt(sum(x * x for x in c))
        return len(vs), a, nrm[next(iter(vs))][1] < -0.5
    meta = [info(ts) for ts in polys]
    order = sorted(range(len(polys)), key=lambda q: (meta[q][2], -meta[q][1]))
    keep, n = [], 0
    for q in order:
        if n + meta[q][0] <= budget:
            keep.append(q)
            n += meta[q][0]
    return sorted(keep)


def _write(folder, g, pos, nrm, uv, tris, polys, keep, stem):
    remap, P, N, U = {}, [], [], []
    by_prim = {}
    for q in keep:
        for t in polys[q]:
            p, *vs = tris[t]
            out = []
            for v in vs:
                if v not in remap:
                    remap[v] = len(P)
                    P.append(pos[v]); N.append(nrm[v]); U.append(uv[v])
                out.append(remap[v])
            by_prim.setdefault(p, []).extend(out)
    assert len(P) < 65535
    pb = b"".join(struct.pack("<3f", *p) for p in P)
    nb = b"".join(struct.pack("<3f", *p) for p in N)
    ub = b"".join(struct.pack("<2f", *p) for p in U)
    blob = pb + nb + ub
    views = [{"buffer": 0, "byteOffset": 0, "byteLength": len(pb)},
             {"buffer": 0, "byteOffset": len(pb), "byteLength": len(nb)},
             {"buffer": 0, "byteOffset": len(pb) + len(nb), "byteLength": len(ub)}]
    accs = [{"bufferView": 0, "componentType": 5126, "count": len(P), "type": "VEC3",
             "min": [min(p[i] for p in P) for i in range(3)], "max": [max(p[i] for p in P) for i in range(3)]},
            {"bufferView": 1, "componentType": 5126, "count": len(P), "type": "VEC3"},
            {"bufferView": 2, "componentType": 5126, "count": len(P), "type": "VEC2"}]
    prims = []
    for pi, p in enumerate(g["meshes"][0]["primitives"]):
        ix = by_prim.get(pi)
        if not ix:
            continue
        ib = b"".join(struct.pack("<H", i) for i in ix)
        views.append({"buffer": 0, "byteOffset": len(blob), "byteLength": len(ib)})
        blob += ib + b"\x00" * ((-len(ib)) % 4)
        accs.append({"bufferView": len(views) - 1, "componentType": 5123, "count": len(ix), "type": "SCALAR"})
        prims.append({**p, "attributes": {"POSITION": 0, "NORMAL": 1, "TEXCOORD_0": 2}, "indices": len(accs) - 1})
    h = dict(g)
    h["meshes"] = [{**g["meshes"][0], "primitives": prims}]
    h["accessors"], h["bufferViews"] = accs, views
    h["buffers"] = [{"uri": f"{stem}.bin", "byteLength": len(blob)}]
    (folder / f"{stem}.bin").write_bytes(blob)
    (folder / f"{stem}.gltf").write_text(json.dumps(h, indent=1))
    return len(P)


def add_lods(folder, name):
    """Write the lower LODs of <folder>/<name> and list them in its XML.  Returns the vertex counts, LOD 0 first."""
    for old in folder.glob(f"{name}_lod*.*"):
        old.unlink()
    g, pos, nrm, uv, tris = _load(folder, name)
    n = len(pos)
    counts = [n]
    budgets = [b for b in LOD_BUDGETS if b < 0.6 * n]
    if budgets:
        polys = _polygons(n, tris)
        for j, b in enumerate(budgets, 1):
            counts.append(_write(folder, g, pos, nrm, uv, tris, polys, _thin(pos, nrm, tris, polys, b), f"{name}_lod{j}"))
    files = [name] + [f"{name}_lod{j}" for j in range(1, len(counts))]
    sizes = [min_size_for(c) for c in counts[:-1]] + [0.0]
    lods = "<LODS>\n" + "".join(f'\t\t<LOD minSize="{s:g}" ModelFile="{f}.gltf"/>\n' for s, f in zip(sizes, files)) + "\t</LODS>"
    x = folder / f"{name}.xml"
    xml = x.read_text(encoding="utf-8")
    new, k = re.subn(r"<LODS>.*?</LODS>", lambda _m: lods, xml, count=1, flags=re.S | re.I)
    assert k == 1, f"no <LODS> block in {x}"
    x.write_text(new, encoding="utf-8")
    return counts
