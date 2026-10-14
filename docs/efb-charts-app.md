# Showing our own charts in-game: EFB app research

Status: **research only (2026-10-14). Nothing built or tested.** Written so a later session can pick it up without redoing the search.

## Question

Can we embed approach plates (e.g. the 2010 CYXD CAP 3 plates in `docs/cyxd/charts/procedures-2010/`) so they can be viewed in-game?

## Findings

### The built-in chart viewer can't be extended
- The sim's chart service is read-only for add-ons. The SDK Charts API (WASM, `MSFS_Charts.h`) has `fsChartsGetIndex(icao, provider, cb)`, `fsChartsGetPages`, `fsChartsGetPageImage` and the two `Free` functions.
- The provider is only `"LIDO"` or `"FAA"` (online). Docs: <https://docs.flightsimulator.com/msfs2024/html/6_Programming_APIs/WASM/Charts_API/Charts_API.htm>
- Not found anywhere: a chart element or file type in the scenery schemas, a custom or local chart provider, or any developer thread about airport add-ons supplying charts. Searched the SDK `Schemas` folder, the samples, and the web.
- CYXD (closed in real life) and its 2010 plates will not appear in LIDO or FAA, so the built-in viewer shows nothing for it.
- Asobo notes charts are not guaranteed for every airport: <https://flightsimulator.zendesk.com/hc/en-us/articles/16959472213916-Electronic-Flight-Bag-EFB-introduction>

### A custom EFB app is the viable route
- MSFS 2024 has an official EFB app API (JavaScript/TypeScript, JSX). Docs: <https://docs.flightsimulator.com/msfs2024/retail/programming-apis/efb/electronic-flight-bag-api/> and the template sample <https://docs.flightsimulator.com/msfs2024/html/7_Samples_Tutorials/Samples/EFB/EFB_Template_Sample.htm>
- The docs say a built app, once in a package, appears in the EFB for every aircraft. It is independent of any one airport or aircraft. **Unverified in the sim.**
- Third-party precedent exists: Navigraph's EFB charts app and the SimBrief EFB app (PC only). One Navigraph forum thread reports an EFB app hiding airport markers in the 2024 EFB, so test the default map after installing.
- Tablets modelled by an aircraft developer are separate from the universal EFB, so an app may not show in those.

### The SDK template (on disk)
`D:\MSFS\MSFS 2024 SDK\Samples\DevmodeProjects\EFB\`
- `EFBTemplateAppProject.xml`: the project (`Packages`/`PackagesMetadata` folders, one package).
- `PackageDefinitions\mycompany-efb-templateapp.xml`: package definition. Content type `MISC`. Two asset groups:
  - `ContentInfo` (thumbnail).
  - A `Copy` group: `PackageSources\TemplateApp\dist\` is copied to `.\html_ui\efb_ui\efb_apps\TemplateApp\`. This is where the sim finds the app.
- `PackageSources\efb_api\`: the EFB API typings and runtime. Keep it unchanged apart from `npm install`.
- `PackageSources\vendor\microsoft-msfs-sdk-2.1.1.tgz`: the Microsoft avionics SDK, which supplies `FSComponent`.
- `PackageSources\TemplateApp\`: the app to copy and rename.
  - `src\TemplateApp.tsx`: an `App` and an `AppView`. `registerViews()` registers pages and popups (`appViewService.registerPage/registerPopup`). `defaultView` picks the first page.
  - `src\Components\SamplePage.tsx`, `SamplePopup.tsx`: example pages.
  - `src\Assets\app-icon.svg`: the app icon.
  - `build.js`: esbuild. Entry `src/TemplateApp.tsx`, output `dist`. `src/Assets` is copied to `dist/Assets`. SASS selectors are prefixed with the folder name, so renaming the folder matters.
  - The global `BASE_URL` is `coui://html_ui/efb_ui/efb_apps/TemplateApp`. This is the way to load our own images (`<img src={BASE_URL + "/Assets/xxx.png"}>`, **unverified**). Change the folder name here when renaming.
  - `.env`: `TYPECHECKING`, `SOURCE_MAPS`, `MINIFY`.
- The sample README says Node >= 18, npm >= 5. Run `npm install` in both `efb_api\` and `TemplateApp\`. Then `npm run build` (once) or `npm run watch`.

### Building and testing (from the docs)
- Needs Node.js 18.12 LTS or later and npm.
- Developer Mode on. Open the project in the Project Editor and run "Build All In Project" (this packages `dist`). This is a separate project from the airport ones, so `build.bat` would need to learn about it, or use the Project Editor.
- Start a flight in an aircraft with an EFB (docs suggest the DA62).
- Docs inconsistency: one page names the main file `TemplateApp.tsx`, another `TemplateApp.js`. The SDK on disk has `.tsx`.

## Proposed design (not started)
A small package, e.g. "Historic Charts", separate from the airport packages:
- One EFB app with a page listing airports, then a chart list, then an image viewer (zoom and pan matter for plates).
- Plates are PNGs in `src/Assets/`, copied to `dist/Assets/` by the build. CYXD's 2010 set first.
- Plates are large screenshots, so downscale and check the package size.
- Existing plate source: `docs/cyxd/charts/procedures-2010/*.png`.

## Open questions to test first
1. Can the app load PNGs from its own package via `BASE_URL`? (The key risk.)
2. Does the EFB image view support zoom and pan, or do we need our own? Does the gamepad or pointer input work on it?
3. Does the app show up for every aircraft, including the ones in the FSE aircraft projects?
4. Does the app work on the MS Store sim? (Unknown. The Navigraph and SimBrief apps are PC-only.)
5. Are there copyright concerns about redistributing Canada Air Pilot plates in a package? Check before publishing, if ever.

## Alternative if the EFB route fails
A poster or briefing-board object in the airport scenery with the plate as a texture. Viewable only in the world, and no code.
