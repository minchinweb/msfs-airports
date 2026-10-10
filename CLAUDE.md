# msfs-airports

MSFS 2024 add-on projects: airports and FSE aircraft variants. The sim is the **MS Store** version. Each project folder has its own project XML, e.g. `airport-cyxd/airport-CYXD-edmonton-blatchford-field.xml` or `aircraft-es30/airplane-es30-fse.xml`. Two older projects sit in the repo root (`airport-2FA2-Monroe-Airpark.xml`, `airport-CEV7-tofield-ab.xml`). Each project's handoff notes are in `docs/<project>/STATUS.md` (or `status.md`). Read the relevant one before resuming work.

## Building

Use `build.bat` in the repo root. From the bash tool, run it through cmd. The `//c` stops Git Bash from rewriting `/c` as a path:

    cmd.exe //c build.bat cyxd             # airport-cyxd
    cmd.exe //c build.bat es30 -rebuild    # full rebuild of aircraft-es30
    cmd.exe //c build.bat cev7             # airport-CEV7-tofield-ab.xml in the root

- The project can be a short name (`cyxd`, `es30`, `navaids`), a project folder, or a project .xml. Run `build.bat -h` for all options.
- Exit codes: 0 built with no errors, 1 built with errors, 2 nothing built or not confirmed, 3 setup problem.
- The script judges the result from `<project>/_PackageInt/_RPTErrors.xml`, which is rewritten at the end of every build. It prints the error messages and saves them, with the rest of the run, to `_build/last-build.txt`. Read that file rather than asking the user to copy console output.
- With the sim closed, it uses the SDK's `fspackagetool.exe` (the documented route). The SDK path comes from `MSFS2024_SDK`, or else `C:\MSFS 2024 SDK`.
- With the sim running, it is unverified. The script tries `fspackagetool` first. If nothing happens, it calls `FlightSimulator2024.exe -I ";" BuildAssetPackages ...` directly (syntax from MSFS 2020). If both give exit code 2, ask the user to build from DevMode > Project Editor, or to close the sim and rerun.
- Running `fspackagetool` directly from the agent shell once exited immediately with "Attached to EXE". If `build.bat` reports no build, retry with `-window`, which runs the builder in its own console window.
- A rebuild does not reload scenery in a running sim. The user has to restart the sim to see changes.
- Once a method is confirmed to work or fail, note it here (sim open or closed, with or without `-window`) so the next session doesn't re-test it.

## Confirmed build notes (2026-10-10, sim closed)
- `MSFS2024_SDK` in the user's environment points to `D:\MSFS\MSFS 2024 SDK\`, which has no `Tools\bin\fspackagetool.exe`. The SDK is at `C:\MSFS 2024 SDK`. Override per run: `$env:MSFS2024_SDK='C:\MSFS 2024 SDK'`.
- Run it from PowerShell: `cmd /c ".\build.bat cyxd"`. From Git Bash the GNU `find` shadows Windows `find` and the sim-running check fails. `cmd /c build.bat` without `.\` also fails.
- With the sim closed, `fspackagetool` built CYXD (exit code 0, `_RPTErrors.xml` empty, BGL rewritten) without `-window`. It prints "Attached to EXE" and a odd exit code (-2015035325); ignore it, `build.bat` judges by `_RPTErrors.xml`. On the MS Store sim it may pop up "Something went wrong launching your game. Custom arguments were used." The build still completed; just dismiss it.
