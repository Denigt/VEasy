@ECHO OFF

FOR /F "tokens=3*" %%i IN ('REG QUERY HKCU\Environment /v PATH') DO SET AUX=%%i
ECHO %AUX%>userPath.txt
SETX PATH "%AUX%;%CD%\Converter\bin"

ECHO Variable de entorno PATH modificada
