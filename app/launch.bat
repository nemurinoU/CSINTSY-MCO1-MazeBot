#!/bin/sh > nul 2> nul
@ECHO OFF

python ../source/main.py > nul 2> nul
if  errorlevel 9009 goto TRY_1
else goto SUCCESS

:TRY_1
py3 ../source/main.py > nul 2> nul
if  errorlevel 9009 goto TRY_2
else goto SUCCESS

:TRY_2
python3 ../source/main.py > nul 2> nul
if  errorlevel 9009 goto TRY_3
else goto SUCCESS

:TRY_3
py ../source/main.py > nul 2> nul
if  errorlevel 9009 goto ERROR
else goto SUCCESS

:SUCCESS
echo SUCCESSFUL
cmd \k
goto EOF 

:ERROR
echo Failed
cmd /k
exit /b 1

:EOF 

