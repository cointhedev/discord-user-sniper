@echo off
cls
title Discord Username Sniper
color 0a

python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed! Please install Python 3.8 or higher.
    echo Download from: https://www.python.org/downloads/
    pause
    exit
)

echo Installing requirements - please wait...
pip install -r requirements.txt >nul

python main.py
pause 