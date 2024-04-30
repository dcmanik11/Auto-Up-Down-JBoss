@echo off

echo Pemeriksaan Serial Number Laptop
echo ================================

wmic bios get serialnumber
pause >nul
