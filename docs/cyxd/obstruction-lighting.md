# CYXD: obstruction lighting on downtown buildings

Researched 2026-11-26. Covers open-questions item 13 (flashing red beacons on downtown buildings). Written so a later session can pick it up without repeating the research.

## Short answer

Whether a building needs lights is set by CARs 601.23(1) and 601.24. The lights themselves are set by Standard 621. A building is an obstacle, and must be marked and lit, if any of these is true:

- (a) it penetrates an airport obstacle limitation surface (OLS), calculated per Chapter 4 of TP 312E;
- (b) it is higher than 90 m AGL and within 6 km of the geographical centre of an aerodrome;
- (c) it is higher than 90 m AGL and within 3.7 km of the centreline of a recognized VFR route;
- (d) it is higher than 150 m AGL;
- (e) for catenary wires crossing a river, any part is higher than 90 m AGL.

Downtown is about 3 km from CYXD, so test (b) covers it: a downtown building over 90 m is an obstacle. Test (a) can catch buildings well under 90 m near the runway ends, which is one possible reason for the 10 to 15 storey buildings that have lights.

Sources (read 2026-11-26):
- [CARs 601.23 to 601.24](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/page-55.html)
- [CARs 601.25 to 601.29](https://laws-lois.justice.gc.ca/eng/regulations/SOR-96-433/page-56.html)
- [Transport Canada: marking and lighting of obstacles](https://tc.canada.ca/en/aviation/general-operating-flight-rules/marking-lighting-obstacles-air-navigation)
- [Standard 621](https://tc.canada.ca/en/corporate-services/acts-regulations/list-regulations/canadian-aviation-regulations-sor-96-433/standards/standard-621-obstacle-marking-lighting-canadian-aviation-regulations-cars)

## Other rules that matter

- **601.24:** the owner of a new or modified obstacle must notify the Minister and mark and light it to Standard 621, or to an equivalent the Minister approves (601.27). Transport Canada's guidance says this is done with an Aeronautical Assessment Form (AAF).
- **601.25:** the Minister can require marking and lighting of a structure that is hazardous because of its height or location, even if it fails the 601.23 tests. The owner then has six months.
- **601.26:** an existing obstacle must be upgraded to the current Standard 621 if its location relative to other obstacles or its surroundings change. Installations made before the current Standard's effective date don't otherwise have to be upgraded.
- **601.28 and 601.29:** failures must be reported to air traffic services, and nobody may deface or damage a required light.

## Have the rules changed?

Yes, in two ways, though the thresholds may not have.

- Before the 2011 amendment (SOR/2011-285, [Canada Gazette, 21 Dec 2011](https://gazette.gc.ca/rp-pr/p2/2011/2011-12-21/html/sor-dors285-eng.html)), marking and lighting was largely guidance. The amendment made it mandatory. Lights on older buildings may be voluntary or from earlier rules, and they are not necessarily grandfathered in the way a current installation is.
- Standard 621 has been revised. The 1st edition (31 Dec 2011) was cancelled by the 2nd edition. The Transport Canada page shows a last amendment of 2026/08/13.

**Not verified:** whether the 90 m and 150 m thresholds existed before 2011, and what the pre-1995 rules were. The pre-1995 rules are the ones the user asked about, and I have not found their text.

## Lights by height (Standard 621, unverified)

A subagent read Standard 621's lighting chapters from the summary, not the full text. Treat these as leads to check against the current PDF:

- up to about 45 m: steady red double-unit lights at the highest point, one per 45 m, with flashing red beacons (CL-864) allowed as an alternative;
- up to about 150 m: medium-intensity white (CL-865), flashing in sync, with red at night on dual-lit installations;
- above 150 m: high-intensity white (CL-856) on the highest point.

If that is right, most downtown towers over 90 m get white lights, not flashing red. The open question assumed flashing red beacons on all of them, which may need revising. Check the current Standard 621 before choosing a light for any building.

Shielding (Standard 621 section 2.2): a dominant lit building can make nearby unlit obstacles unnecessary to light, if the regional office judges its lighting gives sufficient warning. Clusters are assessed one by one.

## The obstacle-surface script

`tools/obstacle_surfaces.py` lays out the OLS for CYXD from `airport-cyxd/PackageSources/Scenery/airport-cyxd/CYXD.xml` and applies the 601.23 height tests.

- Command line: `python -I tools/obstacle_surfaces.py [--buildings buildings.csv] [--rules rules.json] [--radius 8000] [--cell 50] [--grid-csv out.csv]`. It prints the area each surface covers and the area where it is the lowest limit, then reports any buildings above a cutoff.
- Import: `from obstacle_surfaces import ObstacleModel`, then `ObstacleModel().clearance(lat, lon, top_amsl_m, ground_amsl_m)`. It returns `obstacle`, `margin_m` (positive means above the cutoff), `cutoff_amsl_m` and `cutoff`. Ground elevation enables the 90 m and 150 m tests.
- The surface dimensions are placeholders in the shape of ICAO Annex 14 / TP 312 surfaces for a non-precision runway. They are not checked against TP 312E Chapter 4 and are not the pre-1995 rules. Replace them with `--rules FILE` (JSON with the keys in `RULES`) once the real values are known.
- Runway data: all three runways are used (04/22, 12/30, 16/34), as if all were open.

With the placeholders, the inner horizontal surface sits at about 712 m AMSL downtown (45 m above the field at 667.3 m). If downtown ground is near 670 m, buildings above roughly 40 m would penetrate. That result depends on the placeholder dimensions and on an assumed ground height, so it is not a finding yet.

## The 1995 premise

The user said CYXD closed to scheduled service in 1995, so lights would date from before 1995. The repo's notes do not confirm that date:

- `runway-04-22-closure.md` says the 04/22 pavement was still operating in 1978, was out of the operating inventory when Edmonton Airports wrote its 1995 plan, and closed sometime between 1979 and 1994. The 1995 plan budgeted overlays for "the two runways."
- The airport closed completely on 30 November 2013.

Neither source gives the date scheduled service ended. Check that before using 1995 as the cutoff for the rules.

## Open items

1. Get the pre-1995 OLS and obstruction-lighting text, and put the dimensions into a `--rules` file.
2. Get downtown building heights (LiDAR or OSM) into a `buildings.csv` with `ground_amsl_m`, and run the script. A reference list of completed towers 100 m and taller, with partly unverified heights and coordinates, is in `edmonton-tall-buildings.md`.
3. Check the current Standard 621 PDF for the lighting-by-height rules and the shielding table before choosing lights.
4. Confirm the date scheduled service ended at CYXD.
5. Decide whether the flashing-red plan in open-questions item 13 still holds once the heights and the light types are known.
