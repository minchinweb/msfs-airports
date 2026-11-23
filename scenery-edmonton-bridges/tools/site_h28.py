"""H28 Blackmud Creek arches (Anthony Henday Drive over Blackmud Creek, west of 111 Street... east of it: 53.4348, -113.5134).

Three cast-in-place concrete, deck-stiffened, open-spandrel arch bridges, completed September 2005 (CCE 2008, "Three Crossings On
Henday"): one per Henday carriageway and one for the ramp from the Calgary Trail interchange.  Each 76 m long: a 40 m arch span with
about 18 m of deck cantilevered on past each springing; two ribs per structure, 40 m span, 7.5 m rise, 7.0 m wide, 0.4 m thick; a
1.5 m deep cellular deck slab; 15 degree structure skew (roadway 45 degrees to the creek); roadway 17 m above the creek bed on 16 m
embankments.  Reference: docs/edmonton-bridges/reference/H27-calgary-trail-gateway (one task with H27).

Where: the reference brief first placed H28 at -113.496.  Those OSM ways are H27's trellis flyovers.  Blackmud Creek (OSM stream
490629227) passes under the Henday 1.5 km further west, under OSM bridge ways 25477513 (westbound, three lanes), 25477514
(eastbound, three lanes) and the ramp pair 25477544 (the collector from Calgary Trail, two lanes) and 115754686 (one lane), each about
76-78 m long, which the 2018 LiDAR shows as three raised decks: ramp, westbound, eastbound.  The two ramp ways share one deck.
Sourced: plan from OSM, deck levels from the 2018 LiDAR (henday.py), structure dimensions from CCE 2008.  The arch is centred on the
creek crossing; the springing skew is turned towards the creek.
Assumed (flagged): deck widths from the lane count (the ramp deck carries both ramp ways: three lanes' width), rib positions under
the deck (the ramp deck centred 3.9 m left of way 25477544, half way to 115754686; ribs centred at a quarter of the deck width each side), spandrel cross walls every 5 m, footing sizes, approaches and slopes.
"""
import sys
from bridgelib import *
import henday

CODE, TITLE = "H28", "Blackmud Creek arches"
F = "H27-calgary-trail-gateway"
LAT0, LON0 = 53.4349, -113.5134
DATUM = 660.00

DECKS = [
    dict(seed=25477513, lanes=3, kind="arch"),           # Henday westbound
    dict(seed=25477514, lanes=3, kind="arch"),           # Henday eastbound
    dict(seed=25477544, lanes=3, kind="arch", t_off=3.9),  # ramp structure: collector 25477544 (2 lanes) + 115754686 (1 lane)
]


def sample():
    henday.sample(F, "h28", LAT0, LON0, DECKS)


def build():
    r = henday.build_site(F, "h28", LAT0, LON0, DATUM, DECKS, "br_h28_blackmud")
    return dict(code=CODE, title=TITLE, lat0=LAT0, lon0=LON0, alt=DATUM, parts=[("br_h28_blackmud_arches", r["m"])], frame=r["fr"],
                views=[("a", 160.0, 12.0), ("b", 20.0, 25.0), ("c", 300.0, 45.0)], preview=dict(span=420.0, water=False))


if __name__ == "__main__":
    if "--sample" in sys.argv:
        sample()
