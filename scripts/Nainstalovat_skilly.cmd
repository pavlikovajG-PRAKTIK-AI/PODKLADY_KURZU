@echo off
REM Dvojklik spusti instalaci skillu PRAKTIK-AI - funguje v Pruzkumniku
REM i v jinych spravcich souboru (Total Commander apod.), kde
REM "Spustit v PowerShellu" v kontextovem menu chybi.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install_skills.ps1"
echo.
pause
