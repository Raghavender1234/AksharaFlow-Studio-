@echo off
title TypeMaster Pro - Standalone Desktop Typing Tutor
cd /d "c:\Users\brred\Desktop\TypingMaster_Pro\backend"
python "c:\Users\brred\Desktop\TypingMaster_Pro\backend\app.py"
if errorlevel 1 (
    echo.
    echo Failed to launch TypeMaster Pro. Please ensure Python is installed.
    pause
)
