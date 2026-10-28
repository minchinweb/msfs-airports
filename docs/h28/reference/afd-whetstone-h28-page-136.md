# AFD page 136: Whetstone Intl (H28), Port of Del Bonita

Source: https://xcfind.com/static/afd/NW_136_29OCT2026.pdf (Northwest U.S. Airport/Facility Directory, Montana, page 136, effective 29 Oct 2026 to 24 Dec 2026, chart L-13D Great Falls). Saved here as a transcription; the PDF itself is not in the repo.

## Entry (as printed)

- **WHETSTONE INTL (H28)**, 32 NW of Great Falls, UTC-7 (-6 DT), N49°00.00' W112°47.55'. Elevation 4336 ft. NOTAM file GTF.
- **RWY 07-25: 4440 x 65 ft (turf)**. RWY 07: P-line.
- **Airport remarks:** Unattended. No snow removal. Gopher holes on Rwy 07-25. Rwy 07 P-line marked with red balls. Rwy 07-25 threshold marked by double cones; edge marked by white cones spaced 200 ft.
- **Airport manager:** 406-444-2506.
- **Communications:** CTAF/UNICOM 122.8.
- **Clearance delivery:** call Salt Lake ARTCC at 801-320-2568.

## Notes for the sim project

- 4440 ft x 65 ft = 1353 m x 20 m, which matches the current runway (`airport-H28`, 1,353 m x 20 m).
- Double cones at the thresholds and white cones every 200 ft (about 61 m) on the edges match SPEC and the cone plan.
- The red balls on the P-line match the power-line marker balls.
- The AFD coordinate (N49°00.00' W112°47.55' = 49.00000, -112.79250) is about 0.13' north and 0.0154° (about 1.1 km) west of the marker in the XML (48.99868, -112.77713). Check whether the AFD point is a reference point for the strip, or whether the marker is off. Not changed here.
- Rwy 07 is the only published runway end on this page. The sim's 08/26 naming is not used here.
