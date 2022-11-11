@echo off
echo Installing required modules...
py -3 -m pip install -r requirements.txt
echo:
echo Launching Achievements Reader...
py -3 main.py
pause
