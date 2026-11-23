"""H27 Henday / Calgary Trail / Gateway Boulevard (Anthony Henday Drive, Highway 216, at Highway 2): the three-level interchange.

Sourced (docs/edmonton-bridges/reference/H27-calgary-trail-gateway NOTES.md, SOURCES.md):
  * plan: OSM ways (geometry.json `osm_added_2026_11_23`, read from the OSM API on 2026-11-23); the deck seeds are the OSM bridge ways
    listed in DECKS;
  * heights: 2018 LiDAR (henday.py: the raised run of each chain, a robust fit to the first returns lowered 0.12 m, the bare earth
    under each crossing road), sampled into elevation/h27-samples.json by `python -I site_h27.py --sample`;
  * the four trellis-beam structures (CCE 2008, "Three Crossings On Henday"): beams 8 m apart on 44 m spans between integral (MSE
    wall) abutments, 600 mm wide at the bottom and 1,300 mm top flange, no piers next to the roadway.  Which four: the striped
    beam shadows in the 2019 aerial (both Henday carriageways over the West Edmonton Mall ramp, the West Edmonton Mall ramp and the
    2 South ramp over Calgary Trail SW); the beam layout matches the shadows.  Mapillary frames in street/ show the beams on the MSE
    walls and the curved 2 South flyover on single-column hammerhead piers.
Assumed (flagged): deck widths from the OSM lane count (henday.width), 1.8 m girder depth and 2.0 m trellis beam depth, pier sizes
and stations (henday.place_piers), the trellis beam top following the deck, approach widths and 4:1 slopes.  Concrete barriers both
sides (Mapillary).  No lamps, signs or gantries.  The CCE "Alberta's first three-level interchange" is the 2 South flyover (OSM layer 2)
over the Henday, over the West Edmonton Mall ramp.
"""
import sys
from bridgelib import *
import henday

CODE, TITLE = "H27", "Henday / Calgary Trail / Gateway"
F = "H27-calgary-trail-gateway"
LAT0, LON0 = 53.4365, -113.4910
DATUM = 680.00

DECKS = [
    # Henday and its links over Calgary Trail / Gateway Boulevard
    dict(seed=22924969, lanes=2, kind="girder"),          # westbound link to 2 South
    dict(seed=22924966, lanes=2, kind="girder"),          # Henday westbound
    dict(seed=22924964, lanes=2, kind="girder"),          # Henday eastbound
    dict(seed=22916449, lanes=1, kind="girder"),          # eastbound link, beside the eastbound deck
    # west side
    dict(seed=41985530, lanes=2, kind="trellis"),         # Henday westbound over the West Edmonton Mall ramp
    dict(seed=41985559, lanes=2, kind="trellis"),         # Henday eastbound over the West Edmonton Mall ramp
    dict(seed=41985706, lanes=2, kind="girder"),          # Henday westbound, east of the flyover
    dict(seed=41986110, lanes=1, kind="girder"),          # westbound exit beside it
    dict(seed=41985746, lanes=2, kind="girder"),          # Henday eastbound, east of the flyover
    dict(seed=22915670, lanes=2, kind="girder", order=3),  # 2 South flyover, the third level
    # south side
    dict(seed=22916446, lanes=1, kind="girder"),          # loop ramp over Calgary Trail / Gateway
    dict(seed=22949436, lanes=2, kind="trellis"),         # West Edmonton Mall ramp over Calgary Trail SW
    dict(seed=22924959, lanes=4, kind="trellis"),         # 2 South ramp over the West Edmonton Mall ramp
    dict(seed=22927649, lanes=2, kind="girder"),          # link from Calgary Trail SW to the east ramps
    # east side, over the railway (Leduc Subdivision) and Gateway's ramps
    dict(seed=60093990, lanes=2, kind="girder"),
    dict(seed=22916432, lanes=2, kind="girder"),
    dict(seed=22916426, lanes=2, kind="girder"),
    dict(seed=115758014, lanes=1, kind="girder"),
    dict(seed=22916422, lanes=2, kind="girder"),
]


def sample():
    henday.sample(F, "h27", LAT0, LON0, DECKS)


def build():
    r = henday.build_site(F, "h27", LAT0, LON0, DATUM, DECKS, "br_h27_calgary_trail")
    return dict(code=CODE, title=TITLE, lat0=LAT0, lon0=LON0, alt=DATUM, parts=[("br_h27_calgary_trail", r["m"])], frame=r["fr"],
                views=[("a", 205.0, 35.0), ("b", 120.0, 30.0), ("c", 20.0, 60.0)], preview=dict(span=1500.0, water=False))


if __name__ == "__main__":
    if "--sample" in sys.argv:
        sample()
