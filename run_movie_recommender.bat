@echo off
title Movie Recommendation System

echo =========================================
echo        Movie Recommendation System
echo =========================================
echo.

REM Navigate to src folder
cd /d "%~dp0src"

REM Run the Python script
python movie_recommender_cli.py

echo.
echo =========================================
echo Press any key to exit...
pause > nul
