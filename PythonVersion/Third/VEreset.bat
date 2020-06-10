@ECHO OFF
FOR /F %%j IN (userPath.txt) DO SET AUX=%%j
SETX PATH "%AUX%"

ECHO Variable de entorno PATH restaurada
