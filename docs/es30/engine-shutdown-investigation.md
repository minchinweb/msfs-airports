# ES-30 FSE variant: electric engine shuts down at start

Status: **unresolved** (investigation notes, no code changes made).
Worktree: `fix-es30-engine-shutdown` (branch `worktree-fix-es30-engine-shutdown`).

## Problem

The user's ES-30 variant (Dash 8 100/200 FSE tanks, in `aircraft-es30/`) has its electric engine shut down every time the flight starts in MSFS 2024. Otherwise it flies normally.

## What the variant overrides

All paths below are under
`aircraft-es30/PackageSources/SimObjects/Airplanes/cardboardgt-aircraft-es30-fse/presets/cardboardgt/es30_fse_dh8a/config/`.
Everything else comes from Asobo's base ES-30 through `[MODULAR_MERGE] auto = 1`.

- `systems.cfg`: replaces `consumer.1` with
  `Name:ConsumerHeavyBattery#CType:Battery#Capacity:30000#Amperage:1850#Voltage:800`.
  The user's comment says the base capacity was 3000 Ah (10x increase, to reach FSEconomy range).
- `flight_model.cfg`: redefines `Tank.1` / `Tank.2` (LeftTank / RightTank) at 420 gal each.
- `engines.cfg`: empty (merge only).

The installed Community package was diffed against source and matches, so this is not a stale build.

## What the extracted base files show

Source: `C:\tmp\msfs\asobo_es30` (partial, unencrypted extract supplied by the user).

- Base batteries are named `LowBattery1`, `LowBattery2`, `HeavyBattery3` to `HeavyBattery8` (from `common/flt/*.flt`, `common/panel/panel.xml`, `es30mfdplugin.js`).
  None is named `ConsumerHeavyBattery`.
- Base has two fuel tanks (left/right) and fuel pumps/valves (`LeftPump`, `LeftEngineValve`, `CrossfeedValve`, etc. in the `.flt` files).
- `engines.cfg`, `systems.cfg` and `flight_model.cfg` in the extract are stubs (`[MODULAR_MERGE]` only).
  **The real base `[ELECTRICAL]` section is not available.** The `.fsarchive` files in
  `%LOCALAPPDATA%\Packages\Microsoft.Limitless_8wekyb3d8bbwe\LocalCache\Packages\StreamedPackages\fs24-asobo-aircraft-es30` are compressed and not greppable.
- `panel.xml` has `MaxZeroFuel` 26800 lb.

## Hypotheses (unverified, most likely first)

1. The `consumer.1` override is a partial or wrong replacement.
   `consumer.1` in the base may not be the heavy-battery consumer (it could be the low-voltage battery's), or the base line has extra parameters that were dropped.
   Replacing it could leave the motors without correct power or control at start.
2. `Amperage:1850` is now too low for the 10x capacity, or the Voltage/Amperage/Capacity combination differs from the base.
3. The tank override (least likely; mostly a weight and balance concern, which the release notes already flag).

## Next steps

Needs one of the following from the user (not obtainable by me):

- The base ES-30 `[ELECTRICAL]` lines (`consumer.*`, `battery.*`, `supplier.*`) from `systems.cfg`.
  The SDK Aircraft Editor in Dev Mode can open the base aircraft.
- Results of these tests:
  1. Delete the `consumer.1` line from `systems.cfg`. If the engine stays running, that line is the cause.
  2. If it still shuts down, restore the line and remove the `Tank.1` / `Tank.2` overrides from `flight_model.cfg`.

Once the base lines are known:

1. Find which `consumer.N` the heavy batteries (`HeavyBattery3` to `HeavyBattery8`) actually reference.
2. Override only that index, copying every base parameter and changing only `Capacity` (and `Amperage` if needed).
3. Update `ReleaseNotes.xml` and the changelog, then rebuild.

## Instructions for Claude picking this up later

- Re-enter the worktree with `EnterWorktree` using `path` = `D:\Code\msfs-airports\.claude\worktrees\fix-es30-engine-shutdown`.
- Read this file first. Do not redo the search of `C:\tmp\msfs\asobo_es30` or the streamed packages; they have no base electrical config.
- The user wrote "EC-30", but the aircraft is the ES-30 (Heart Aerospace).
- The sim cannot be run from here, so a fix cannot be verified by me. State this plainly and ask the user to test in-game.
- Do not edit `systems.cfg` speculatively. Wait for the base `[ELECTRICAL]` lines or the user's test result.
