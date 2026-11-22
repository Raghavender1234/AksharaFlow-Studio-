@echo off
title Build AksharaFlow_Studio.exe
cd /d "%~dp0"
python build_assets.py
python -m PyInstaller --noconfirm --clean --onefile --windowed --name "AksharaFlow_Studio" --icon "assets\aksharaflow.ico" --version-file "version_info.txt" --add-data "frontend;frontend" --add-data "backend;backend" --paths "backend" --hidden-import database --hidden-import curriculum_en --hidden-import curriculum_inscript --hidden-import adaptive_engine "backend\app.py"
echo.
echo Build complete! Output: dist\AksharaFlow_Studio.exe
pause
