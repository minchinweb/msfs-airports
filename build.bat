@echo off
setlocal EnableExtensions DisableDelayedExpansion

rem --------------------------------------------------------------------------
rem build.bat - build an MSFS 2024 project in this repo from the command line.
rem Run "build.bat -h" for usage. Notes for Claude are in CLAUDE.md.
rem
rem Written for the MS Store version of MSFS 2024. The build is judged from
rem files, not exit codes: it is finished when the project's
rem _PackageInt\_RPTErrors.xml is rewritten, and errors are read from it.
rem --------------------------------------------------------------------------

rem SDK location. The MSFS 2024 SDK installer sets MSFS2024_SDK; edit the
rem fallback below if yours is installed somewhere else.
set "SDK_DIR=C:\MSFS 2024 SDK"
if defined MSFS2024_SDK set "SDK_DIR=%MSFS2024_SDK%"
set "TOOL=%SDK_DIR%\Tools\bin\fspackagetool.exe"
set "SIM_IMAGE=FlightSimulator2024.exe"

set "ROOT=%~dp0"
set "ROOT=%ROOT:~0,-1%"
set "SUMMARY=%ROOT%\_build\last-build.txt"
set "ERRTXT=%ROOT%\_build\last-build-errors.txt"

set "PROJECT_ARG="
set "REBUILD="
set "MODE=auto"
set "WINDOW="
set "PAUSE_AT_END="
set "WAIT=300"
set "EXITCODE=3"

rem ---- arguments -----------------------------------------------------------
:parse
if "%~1"=="" goto parsed
set "ARG=%~1"
if /i "%ARG%"=="-h" goto usage
if /i "%ARG%"=="--help" goto usage
if "%ARG%"=="/?" goto usage
if /i "%ARG%"=="-rebuild" (set "REBUILD=1" & shift & goto parse)
if /i "%ARG%"=="-tool" (set "MODE=tool" & shift & goto parse)
if /i "%ARG%"=="-direct" (set "MODE=direct" & shift & goto parse)
if /i "%ARG%"=="-window" (set "WINDOW=1" & shift & goto parse)
if /i "%ARG%"=="-pause" (set "PAUSE_AT_END=1" & shift & goto parse)
if /i "%ARG%"=="-wait" (set "WAIT=%~2" & shift & shift & goto parse)
if "%ARG:~0,1%"=="-" (echo Unknown option: "%ARG%" & goto usage_error)
if defined PROJECT_ARG (echo Only one project can be given. & goto usage_error)
set "PROJECT_ARG=%ARG%"
shift
goto parse

:parsed
if not defined PROJECT_ARG (echo No project given. & goto usage_error)
set "WAIT_N=0"
set /a "WAIT_N=WAIT" >nul 2>&1
if %WAIT_N% LEQ 0 (echo -wait needs a positive number of seconds. & goto usage_error)

mkdir "%ROOT%\_build" 2>nul
> "%SUMMARY%" echo MSFS 2024 build, %DATE% %TIME%

rem ---- find the project XML ------------------------------------------------
rem Accepts a project .xml, a folder holding one, or a short name: "cyxd"
rem finds the folder airport-cyxd, "cev7" finds airport-CEV7-tofield-ab.xml.
set "PROJ="
set "SEARCH_DIR="
if exist "%PROJECT_ARG%\*" set "SEARCH_DIR=%PROJECT_ARG%"
if not defined SEARCH_DIR if exist "%ROOT%\%PROJECT_ARG%\*" set "SEARCH_DIR=%ROOT%\%PROJECT_ARG%"
if not defined SEARCH_DIR if exist "%PROJECT_ARG%" set "PROJ=%PROJECT_ARG%"
if not defined SEARCH_DIR if not defined PROJ if exist "%ROOT%\%PROJECT_ARG%" set "PROJ=%ROOT%\%PROJECT_ARG%"
if defined SEARCH_DIR goto have_dir
if defined PROJ goto have_proj

for /d %%D in ("%ROOT%\*-%PROJECT_ARG%") do if not defined SEARCH_DIR set "SEARCH_DIR=%%~fD"
if defined SEARCH_DIR goto have_dir

set "COUNT=0"
for %%F in ("%ROOT%\*%PROJECT_ARG%*.xml") do call :is_project "%%~fF" && (set "PROJ=%%~fF" & set /a COUNT+=1)
if %COUNT% GTR 1 (call :log "More than one project file in the repo root matches '%PROJECT_ARG%'; give the file name." & goto setup_error)
if defined PROJ goto have_proj
call :log "Could not find a project for '%PROJECT_ARG%'."
goto setup_error

:have_dir
set "COUNT=0"
for %%F in ("%SEARCH_DIR%\*.xml") do call :is_project "%%~fF" && (set "PROJ=%%~fF" & set /a COUNT+=1)
if %COUNT% EQU 0 (call :log "No project XML found in '%SEARCH_DIR%'." & goto setup_error)
if %COUNT% EQU 1 goto have_proj
call :log "More than one project XML in '%SEARCH_DIR%'; give one of these instead:"
for %%F in ("%SEARCH_DIR%\*.xml") do call :is_project "%%~fF" && call :log "  %%~nxF"
goto setup_error

:have_proj
for %%F in ("%PROJ%") do (set "PROJ=%%~fF" & set "PDIR=%%~dpF" & set "PNAME=%%~nF")
set "PDIR=%PDIR:~0,-1%"
call :log "Project:     %PROJ%"
if not "%PROJ: =%"=="%PROJ%" call :log "Warning:     the project path contains spaces; fspackagetool has had trouble with that."

set "SIM_RUNNING="
tasklist /fi "imagename eq %SIM_IMAGE%" /nh 2>nul | find /i "%SIM_IMAGE%" >nul && set "SIM_RUNNING=1"
if defined SIM_RUNNING call :log "Sim running: yes"
if not defined SIM_RUNNING call :log "Sim running: no"

set "REBUILD_TOOL="
set "REBUILD_SIM="
if defined REBUILD set "REBUILD_TOOL=-rebuild"
if defined REBUILD set "REBUILD_SIM=Force"
set "HAVE_TOOL="
if exist "%TOOL%" set "HAVE_TOOL=1"
if /i "%MODE%"=="direct" goto try_direct
if defined HAVE_TOOL goto try_tool
call :log "fspackagetool.exe not found at %TOOL%"
call :log "             Install the MSFS 2024 SDK, or set MSFS2024_SDK to its folder."
if /i "%MODE%"=="tool" goto setup_error
if not defined SIM_RUNNING goto setup_error
goto try_direct

rem ---- method 1: the SDK's fspackagetool (documented) -----------------------
:try_tool
call :log "Method:      fspackagetool"
call :stamp
echo.
echo Running: "%TOOL%" "%PROJ%" -nopause %REBUILD_TOOL%
echo.
rem Start the tool in its own console and return at once. The tool's exit code
rem is a nonzero value even after a good build, and Windows Terminal then
rem leaves the tab open. Run it under cmd /c so that console exits 0. The
rem tool also stays running after the package is written; the script stops
rem it once the build report is on disk, and the wrapper then exits.
rem -window leaves the console visible; otherwise it is minimized.
set "WINFLAG=/MIN"
if defined WINDOW set "WINFLAG="
start "MSFS build - %PNAME%" %WINFLAG% cmd.exe /c ""%TOOL%" "%PROJ%" -nopause %REBUILD_TOOL% & exit /b 0"
rem With the sim closed the report usually appears quickly, so only a short
rem grace period is needed. With the sim open the tool may hand the job to
rem the running sim and produce nothing itself, so allow longer for work to start.
set "IDLE=15"
if defined SIM_RUNNING set "IDLE=45"
call :wait_for_build
call :close_packagetool
if "%WAIT_RC%"=="0" goto finished
if "%WAIT_RC%"=="1" goto unconfirmed
call :log "             fspackagetool produced no build activity."
if /i not "%MODE%"=="auto" goto nothing
if not defined SIM_RUNNING goto nothing
call :log "             Falling back to calling %SIM_IMAGE% directly."

rem ---- method 2: call the sim exe directly (undocumented) --------------------
rem Syntax copied from MSFS 2020: exe -I ; BuildAssetPackages, then the
rem project xml, temp parent folder, output parent folder, optional Force
rem (rebuild) and Console. Unverified on 2024.
:try_direct
call :find_sim_exe
if not defined SIM_EXE (call :log "Could not find %SIM_IMAGE%. Set MSFS2024_EXE to its full path." & goto setup_error)
call :log "Method:      direct call of %SIM_EXE%"
call :stamp
echo.
echo Running: "%SIM_EXE%" -I ";" BuildAssetPackages "%PROJ%" "%PDIR%" "%PDIR%" %REBUILD_SIM% Console
echo.
start "MSFS build - %PNAME%" /wait "%SIM_EXE%" -I ";" BuildAssetPackages "%PROJ%" "%PDIR%" "%PDIR%" %REBUILD_SIM% Console
call :log "             %SIM_IMAGE% exit code %ERRORLEVEL%"
set "IDLE=45"
if not defined SIM_RUNNING set "IDLE=20"
call :wait_for_build
if "%WAIT_RC%"=="0" goto finished
if "%WAIT_RC%"=="1" goto unconfirmed
call :log "             The direct call produced no build activity."
goto nothing

rem ---- results -------------------------------------------------------------
:finished
powershell -NoProfile -NonInteractive -Command "[xml]$x=Get-Content -LiteralPath '%PDIR%\_PackageInt\_RPTErrors.xml' -Raw; $m=@($x.SelectNodes('//Location') | ForEach-Object { $t=$_.Message; if($_.Source -and $_.Source -ne ':0'){ $t=$t+'  ('+$_.Source+')' }; $t } | Select-Object -Unique); $m | ForEach-Object { '  '+$_ }; exit $m.Count" > "%ERRTXT%" 2>&1
set "NERR=%ERRORLEVEL%"
if "%NERR%"=="0" goto built_ok
call :log "Result:      BUILT WITH ERRORS, %NERR% unique message(s) from _PackageInt\_RPTErrors.xml:"
type "%ERRTXT%"
type "%ERRTXT%" >> "%SUMMARY%"
set "EXITCODE=1"
goto restart_note
:built_ok
call :log "Result:      OK, no errors in _PackageInt\_RPTErrors.xml"
set "EXITCODE=0"
:restart_note
if defined SIM_RUNNING call :log "Note:        the sim is running. Restart it to load the rebuilt package; a rebuild does not reload scenery in a running sim."
goto end

:unconfirmed
call :log "Result:      NOT CONFIRMED. Build activity was seen, but _RPTErrors.xml was not rewritten within %WAIT_N% s."
call :log "             Check the DevMode console in the sim, or rerun with a longer -wait."
set "EXITCODE=2"
goto end

:nothing
call :log "Result:      NO BUILD. Nothing was written to _PackageInt or Packages."
if defined SIM_RUNNING call :log "Hint:        build from DevMode, Project Editor in the sim, or close the sim and rerun this script."
if not defined SIM_RUNNING call :log "Hint:        check the builder output above. If it closed at once, try again with -window."
set "EXITCODE=2"
goto end

:setup_error
set "EXITCODE=3"
goto end

:usage_error
echo.
call :usage
exit /b 3

:end
call :log "Summary:     %SUMMARY%"
call :log "Exit code:   %EXITCODE%"
if defined PAUSE_AT_END pause
endlocal & exit /b %EXITCODE%

rem ---- subroutines ---------------------------------------------------------
:log
echo(%~1
>> "%SUMMARY%" echo(%~1
exit /b 0

:is_project
findstr /l /m /c:"<Project " "%~1" >nul 2>&1
exit /b %ERRORLEVEL%

:stamp
set "START="
for /f "usebackq delims=" %%T in (`powershell -NoProfile -NonInteractive -Command "[DateTime]::UtcNow.Ticks"`) do set "START=%%T"
if not defined START (call :log "PowerShell is needed to check the result and could not be run." & set "START=0")
exit /b 0

:wait_for_build
rem Exit codes: 0 finished (_RPTErrors.xml rewritten), 1 activity seen but
rem not finished in time, 2 no activity for IDLE seconds. Activity means a
rem file written under _PackageInt or Packages, or a newly started sim process.
echo Waiting for the build to finish, up to %WAIT_N% s...
powershell -NoProfile -NonInteractive -Command "$s=[long]'%START%'; $done='%PDIR%\_PackageInt\_RPTErrors.xml'; $watch=@('%PDIR%\_PackageInt','%PDIR%\Packages'); $t0=Get-Date; $active=$false; while($true){ if((Test-Path -LiteralPath $done) -and ((Get-Item -LiteralPath $done).LastWriteTimeUtc.Ticks -gt $s)){ exit 0 }; $el=((Get-Date)-$t0).TotalSeconds; if($el -ge %WAIT_N%){ if($active){ exit 1 } else { exit 2 } }; if(-not $active){ $hit=Get-ChildItem -LiteralPath $watch -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $_.LastWriteTimeUtc.Ticks -gt $s } | Select-Object -First 1; if(-not $hit){ $hit=Get-Process -Name FlightSimulator2024 -ErrorAction SilentlyContinue | Where-Object { try { $_.StartTime.ToUniversalTime().Ticks -gt $s } catch { $false } } | Select-Object -First 1 }; if($hit){ $active=$true } elseif($el -ge %IDLE%){ exit 2 } }; Start-Sleep -Seconds 1 }"
set "WAIT_RC=%ERRORLEVEL%"
exit /b 0

:close_packagetool
rem fspackagetool does not exit when the build is finished, so its console
rem stays until someone closes it. Stop the process. Do not touch the sim.
tasklist /fi "imagename eq fspackagetool.exe" /nh 2>nul | find /i "fspackagetool.exe" >nul
if errorlevel 1 exit /b 0
if "%WAIT_RC%"=="0" (
  powershell -NoProfile -NonInteractive -Command "$s=[long]'%START%'; $layout='%PDIR%\Packages'; $deadline=(Get-Date).AddSeconds(12); while((Get-Date) -lt $deadline){ $hit=Get-ChildItem -LiteralPath $layout -Recurse -Filter layout.json -ErrorAction SilentlyContinue | Where-Object { $_.LastWriteTimeUtc.Ticks -gt $s } | Select-Object -First 1; if($hit){ break }; Start-Sleep -Seconds 1 }"
)
call :log "             Closing fspackagetool so its console can exit."
taskkill /IM fspackagetool.exe /F >nul 2>&1
exit /b 0

:find_sim_exe
rem The running sim's own exe if it is open, else the installed Store
rem package that contains FlightSimulator2024.exe.
set "SIM_EXE="
if defined MSFS2024_EXE set "SIM_EXE=%MSFS2024_EXE%"
if defined SIM_EXE exit /b 0
for /f "usebackq delims=" %%P in (`powershell -NoProfile -NonInteractive -Command "$p=Get-Process -Name FlightSimulator2024 -ErrorAction SilentlyContinue | Select-Object -First 1 -ExpandProperty Path; if(-not $p){ $p=Get-AppxPackage | Where-Object { $_.InstallLocation } | ForEach-Object { Join-Path $_.InstallLocation 'FlightSimulator2024.exe' } | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1 }; $p"`) do set "SIM_EXE=%%P"
exit /b 0

:usage
echo Build an MSFS 2024 project in this repo from the command line.
echo.
echo   build.bat ^<project^> [-rebuild] [-tool or -direct] [-window] [-wait N] [-pause]
echo.
echo   ^<project^>  a project .xml, a project folder, or a short name, e.g.
echo                cyxd   airport-cyxd\airport-CYXD-edmonton-blatchford-field.xml
echo                es30   aircraft-es30\airplane-es30-fse.xml
echo                cev7   airport-CEV7-tofield-ab.xml in the repo root
echo                bridges scenery-edmonton-bridges\scenery-edmonton-bridges.xml
echo   -rebuild   redo all conversions (full rebuild)
echo   -tool      only use the SDK's fspackagetool.exe
echo   -direct    only call FlightSimulator2024.exe -I ; BuildAssetPackages ...
echo              (syntax from MSFS 2020, unverified on 2024)
echo   -window    show the builder console. It is closed when the build is written
echo   -wait N    seconds to wait for the build to finish (default 300)
echo   -pause     wait for a key press before closing
echo.
echo   Default: fspackagetool; if the sim is running and that did nothing,
echo   fall back to the direct call. The result is read from the project's
echo   _PackageInt\_RPTErrors.xml and summarised in _build\last-build.txt.
echo.
echo   Exit codes: 0 built OK, 1 built with errors, 2 nothing built or not
echo   confirmed, 3 setup problem.
exit /b 0
