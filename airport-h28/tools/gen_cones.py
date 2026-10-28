"""Generate the H28 cone models (flat-colour palette, like CYXD's gen_buildings.py) into
airport-h28/PackageSources/modelLib/:
  h28_cone_white/   white cone with a black top (the strip's edge cones)
  h28_cone_red/     all-red cone (placed next to a white one at the red-white pairs)
  h28_cones_edge/   the two edge cones across the runway as one model (white, at +-EDGE, CONE_SCALE built in)
  h28_cones_07/     the threshold set: a white and a red cone on each edge, the red one 2 m outboard (west at heading 0)
  texture/h28_palette.png(.xml)
The sets exist because the sim drops a lone 1.2 m cone a few hundred metres out (it culls by on-screen size); a 20 m
wide model stays drawn as far as the fence segments do. Placements are written by gen_field.py.
    python -I airport-h28/tools/gen_cones.py
Prints the two model GUIDs (stable: uuid5 of the model name). Safe to re-run."""
import json
import math
import struct
import uuid
import zlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_field as gf  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
MODELLIB = ROOT / "airport-h28/PackageSources/modelLib"
NS = uuid.UUID("5d0c6c7e-0c1d-4a53-9b6e-0c7d00000028")
PALETTE = [(236, 234, 230), (196, 40, 36), (24, 24, 26)]  # white, red, black
WHITE, RED, BLACK = range(3)
SW = 16
SIDES = 16


def write_palette(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    w, h = SW * len(PALETTE), SW
    raw = b"".join(b"\x00" + b"".join(bytes(PALETTE[x // SW]) for x in range(w)) for _ in range(h))

    def chunk(t, d):
        c = struct.pack(">I", len(d)) + t + d
        return c + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)

    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)) \
        + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
    path.write_bytes(png)
    path.with_name(path.name + ".xml").write_text(
        '<BitmapConfiguration>\n\t<BitmapSlot>MTL_BITMAP_DECAL0</BitmapSlot>\n</BitmapConfiguration>\n')


class Mesh:
    def __init__(self):
        self.pos, self.nrm, self.uv, self.idx = [], [], [], []
        self.at(0.0, 0.0, 1.0)

    def at(self, ox, oz, s):
        """Place the next cone at (ox, oz) with scale s (glTF frame: +X is west once placed, see h28_cones_07)."""
        self.ox, self.oz, self.s = ox, oz, s

    def p(self, x, y, z):
        return (self.ox + self.s * x, self.s * y, self.oz + self.s * z)

    def uvof(self, sw):
        return ((sw + 0.5) / len(PALETTE), 0.5)

    def band(self, r0, y0, r1, y1, sw):
        """Cone-frustum side (counter-clockwise seen from outside), outward normals."""
        slope = (r0 - r1) / (y1 - y0) if y1 != y0 else 0.0
        base = len(self.pos)
        for i in range(SIDES + 1):
            a = 2 * math.pi * i / SIDES
            c, s = math.cos(a), math.sin(a)
            n = (c, slope, s)
            ln = math.sqrt(sum(v * v for v in n))
            n = tuple(v / ln for v in n)
            for r, y in ((r0, y0), (r1, y1)):
                self.pos.append(self.p(r * c, y, r * s))
                self.nrm.append(n)
                self.uv.append(self.uvof(sw))
        for i in range(SIDES):
            a, b, c2, d = base + 2 * i, base + 2 * i + 1, base + 2 * i + 2, base + 2 * i + 3
            self.idx += [a, b, c2, b, d, c2]  # counter-clockwise seen from outside (glTF front face)

    def cap(self, r, y, sw):
        base = len(self.pos)
        self.pos.append(self.p(0, y, 0))
        self.nrm.append((0, 1, 0))
        self.uv.append(self.uvof(sw))
        for i in range(SIDES + 1):
            a = 2 * math.pi * i / SIDES
            self.pos.append(self.p(r * math.cos(a), y, r * math.sin(a)))
            self.nrm.append((0, 1, 0))
            self.uv.append(self.uvof(sw))
        for i in range(SIDES):
            self.idx += [base, base + 2 + i, base + 1 + i]

    def save(self, folder, name):
        folder.mkdir(parents=True, exist_ok=True)
        pos = b"".join(struct.pack("<3f", *p) for p in self.pos)
        nrm = b"".join(struct.pack("<3f", *p) for p in self.nrm)
        uv = b"".join(struct.pack("<2f", *p) for p in self.uv)
        ib = b"".join(struct.pack("<H", i) for i in self.idx)
        blob = pos + nrm + uv + ib
        if len(blob) % 4:
            blob += b"\x00" * (4 - len(blob) % 4)
        n = len(self.pos)
        mn = [min(p[i] for p in self.pos) for i in range(3)]
        mx = [max(p[i] for p in self.pos) for i in range(3)]
        g = {
            "asset": {"version": "2.0", "generator": "airport-h28/tools/gen_cones.py",
                      "extensions": {"ASOBO_normal_map_convention": {"tangent_space_convention": "DirectX"}}},
            "extensionsUsed": ["ASOBO_normal_map_convention"],
            "scene": 0, "scenes": [{"nodes": [0]}],
            "nodes": [{"mesh": 0, "name": name}],
            "meshes": [{"name": name, "primitives": [{"attributes": {"POSITION": 0, "NORMAL": 1, "TEXCOORD_0": 2},
                                                      "indices": 3, "mode": 4, "material": 0}]}],
            "materials": [{"name": "h28_flat", "pbrMetallicRoughness": {
                "baseColorTexture": {"index": 0}, "metallicFactor": 0.0, "roughnessFactor": 0.9}}],
            "textures": [{"sampler": 0, "source": 0}],
            "samplers": [{"magFilter": 9728, "minFilter": 9728}],
            "images": [{"uri": "h28_palette.png"}],
            "accessors": [
                {"bufferView": 0, "componentType": 5126, "count": n, "type": "VEC3", "min": mn, "max": mx},
                {"bufferView": 1, "componentType": 5126, "count": n, "type": "VEC3"},
                {"bufferView": 2, "componentType": 5126, "count": n, "type": "VEC2"},
                {"bufferView": 3, "componentType": 5123, "count": len(self.idx), "type": "SCALAR"}],
            "bufferViews": [
                {"buffer": 0, "byteOffset": 0, "byteLength": len(pos)},
                {"buffer": 0, "byteOffset": len(pos), "byteLength": len(nrm)},
                {"buffer": 0, "byteOffset": len(pos) + len(nrm), "byteLength": len(uv)},
                {"buffer": 0, "byteOffset": len(pos) + len(nrm) + len(uv), "byteLength": len(ib)}],
            "buffers": [{"uri": f"{name}.bin", "byteLength": len(blob)}],
        }
        (folder / f"{name}.bin").write_bytes(blob)
        (folder / f"{name}.gltf").write_text(json.dumps(g, indent=1))
        guid = "{" + str(uuid.uuid5(NS, name)).upper() + "}"
        (folder / f"{name}.xml").write_text(
            '<?xml version="1.0" encoding="utf-8"?>\n'
            f'<ModelInfo guid="{guid}" version="1.1">\n\t<LODS>\n\t\t<LOD minSize="0" ModelFile="{name}.gltf"/>\n\t</LODS>\n</ModelInfo>\n')
        return guid


H, R0, R1 = 0.60, 0.45, 0.07  # cone height, base radius, top radius (metres): squat, as in the 2025 photos
TOP = 0.14  # black-top band height


def lerp_r(y):
    return R0 + (R1 - R0) * y / H


def white_cone(m=None):
    m = m or Mesh()
    m.band(R0, 0.0, lerp_r(H - TOP), H - TOP, WHITE)
    m.band(lerp_r(H - TOP), H - TOP, R1, H, BLACK)
    m.cap(R1, H, BLACK)
    return m


def red_cone(m=None):
    m = m or Mesh()
    m.band(R0, 0.0, R1, H, RED)
    m.cap(R1, H, RED)
    return m


def main():
    write_palette(MODELLIB / "texture" / "h28_palette.png")
    white = white_cone().save(MODELLIB / "h28_cone_white", "h28_cone_white")
    red = red_cone().save(MODELLIB / "h28_cone_red", "h28_cone_red")
    edge = Mesh()
    thr = Mesh()
    for z in (-gf.EDGE, gf.EDGE):
        edge.at(0.0, z, gf.CONE_SCALE)
        white_cone(edge)
        thr.at(0.0, z, gf.CONE_SCALE)
        white_cone(thr)
        thr.at(gf.RED_GAP, z, gf.CONE_SCALE)
        red_cone(thr)
    g_edge = edge.save(MODELLIB / "h28_cones_edge", "h28_cones_edge")
    g_thr = thr.save(MODELLIB / "h28_cones_07", "h28_cones_07")
    print("white", white, "red", red, "edge set", g_edge, "threshold set", g_thr)


if __name__ == "__main__":
    main()
