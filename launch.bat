#!/bin/sh > nul 2> nul
@ECHO OFF

python main.py > nul 2> nul
if  errorlevel 9009 goto TRY_1

:TRY_1
py3 main.py > nul 2> nul
if  errorlevel 9009 goto TRY_2

:TRY_2
python3 main.py > nul 2> nul
if  errorlevel 9009 goto TRY_3

:TRY_3
py main.py > nul 2> nul
if  errorlevel 9009 goto ERROR
echo SUCCESSFUL
cmd \k
goto EOF 

:ERROR
echo Failed
cmd /k
exit /b 1

:EOF 

