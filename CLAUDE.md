# msfs-airports

MSFS 2024 add-on projects: airports and FSE aircraft variants. The sim is the **MS Store** version. Each project folder has its own project XML, e.g. `airport-cyxd/airport-CYXD-edmonton-blatchford-field.xml` or `aircraft-es30/airplane-es30-fse.xml`. Two older projects sit in the repo root (`airport-2FA2-Monroe-Airpark.xml`, `airport-CEV7-tofield-ab.xml`). Each project's handoff notes are in `docs/<project>/STATUS.md` (or `status.md`). Read the relevant one before resuming work.

## Commits

Prefix commit messages with 🤖.

## Building

Use `build.bat` in the repo root. From the bash tool, run it through cmd. The `//c` stops Git Bash from rewriting `/c` as a path:

    cmd.exe //c build.bat cyxd             # airport-cyxd
    cmd.exe //c build.bat es30 -rebuild    # full rebuild of aircraft-es30
    cmd.exe //c build.bat cev7             # airport-CEV7-tofield-ab.xml in the root
    cmd.exe //c build.bat bridges          # scenery-edmonton-bridges

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
- After a successful build `fspackagetool.exe` can stay alive (the build is already complete: `_RPTErrors.xml` is empty and `Packages/.../layout.json` is fresh) and keep `build.bat` from returning. Check those two files, then kill the process (`Stop-Process -Name fspackagetool`). Seen 2026-10-12.
- Seen 2026-10-14 (sim closed, fresh worktree): `cmd /c "cd /d <repo> && .\build.bat cyxd -window"` built OK (exit 0) and takes about 30 s. A leftover "Microsoft Flight Simulator 2024" launch dialog from a previous build (processes `gamingservicesui`, `gamelaunchhelper`) makes the next run report "NO BUILD" until it is closed. Run one build at a time, and kill `fspackagetool` when done. `_RPTErrors.xml` showing only `CompileMemory failed` is a real compile failure (it was a bad `<Departure>`).
- `fspackagetool.exe` stays running after the package is written, and it exits with a nonzero code (`-2015035325`) even when the build is good. Windows Terminal is the default console host and leaves that tab open (seen 2026-10-14; the user had to close it). `build.bat` starts the tool under `cmd /c "... & exit /b 0"`, waits until `_RPTErrors.xml` is rewritten, allows up to 12 s for `layout.json`, then `taskkill /IM fspackagetool.exe /F`. The wrapper exits 0 and the tab closes. Do not leave a build window for the user to close.
- 2026-10-14: the MS Store sim has a pending update. `fspackagetool` still compiled `scenery-edmonton-bridges` with the sim closed (`_RPTErrors.xml` empty). Do not launch the sim from a build until William has updated it in the Xbox app. The packager may still pop the "Custom arguments were used" / update dialog; dismiss it. The build does not need the sim.
- 2026-10-14, `scenery-edmonton-bridges` with a `ModelLib` group (sim closed, PowerShell, `.uild.bat bridges -window`, `MSFS2024_SDK` overridden): builds OK (exit 0), but every second run says "NO BUILD" until the leftover launch-dialog processes are killed (`Stop-Process -Name gamingservicesui,gamelaunchhelper,fspackagetool -Force`). Do that before each build. `fspackagetool` had not written `Packages/.../layout.json` when `build.bat` closed it, so run `python -I scenery-edmonton-bridges/tools/make_layout.py` afterwards.
- 2026-10-17, `scenery-edmonton-bridges-poi` (sim closed, PowerShell, `.\build.bat scenery-edmonton-bridges-poi -window`, SDK overridden): built OK (`_RPTErrors.xml` empty, BGL and `layout.json` written) but the builder's Windows Terminal tab stayed open because `fspackagetool` was still alive. Do not use `-window` from the agent; if the tab is left, `Stop-Process -Name fspackagetool,gamingservicesui,gamelaunchhelper -Force` closes it.
- 2026-10-21, sim RUNNING: `.\build.bat cyxd` (PowerShell, SDK overridden) gave "NO BUILD" (exit 2): `fspackagetool` produced no activity and the direct `FlightSimulator2024.exe -I ... BuildAssetPackages` call exited 0 with nothing written. Building with the sim open does not work; close the sim first.
