@echo off
set /p dir=Enter directory to delete:
del /f/s/q "%dir%" > nul
rmdir /s/q "%dir%"                  
pause                                                                                      