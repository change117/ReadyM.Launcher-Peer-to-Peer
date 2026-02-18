@echo off
REM Quick start script for ReadyM.Launcher (Windows)

echo ReadyM.Launcher - Quick Start
echo ==============================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from python.org
    pause
    exit /b 1
)

REM Check if config exists
if not exist config.json (
    echo No configuration found. Creating default config...
    python launcher.py --setup
    echo.
    echo Please edit config.json to set your game path and player name
    echo Then run this script again
    pause
    exit /b 0
)

REM Display menu
echo Select an option:
echo 1) Host a game session (start server)
echo 2) Join a game session (discover peers)
echo 3) Launch game
echo 4) Show status
echo 5) Change player name
echo 6) Interactive mode
echo 7) Exit
echo.

set /p choice="Enter choice [1-7]: "

if "%choice%"=="1" goto host
if "%choice%"=="2" goto discover
if "%choice%"=="3" goto launch
if "%choice%"=="4" goto status
if "%choice%"=="5" goto setname
if "%choice%"=="6" goto interactive
if "%choice%"=="7" goto exit
goto invalid

:host
echo Starting discovery server...
echo Press Ctrl+C to stop
python launcher.py --server
goto end

:discover
echo Searching for peers...
python launcher.py --discover
pause
goto end

:launch
echo Launching game...
python launcher.py --launch
pause
goto end

:status
python launcher.py --status
pause
goto end

:setname
set /p name="Enter your player name: "
python launcher.py --player-name "%name%"
pause
goto end

:interactive
python launcher.py
goto end

:exit
echo Goodbye!
exit /b 0

:invalid
echo Invalid choice
pause
exit /b 1

:end
