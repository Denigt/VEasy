
@ECHO OFF

SET prog="B:\Mis_documentos\Programacion\Programas_en_Python\Programas\VEasy\VEasyBeta v3\VEasyBetav3.py"
SET icono="B:\Mis_documentos\Programacion\Programas_en_Python\Programas\VEasy\VEasyBeta v3\Images\VEasy.ico"
SET carp1="B:\Mis_documentos\Programacion\Programas_en_Python\Programas\VEasy\VEasyBeta v3\Images;Images"
SET carp2="B:\Mis_documentos\Programacion\Programas_en_Python\Programas\VEasy\VEasyBeta v3\Third;Third"

pyinstaller ^
--uac-admin ^
--icon %icono% ^
--onefile ^
%prog%

MOVE /Y "B:\Mis_documentos\Programacion\Programas_en_Python\Programas\VEasy\VEasyBeta v3\dist\VEasyBetav3.exe" "B:\Mis_documentos\Programacion\Programas_en_Python\Programas\VEasy\VEasyBeta v3\VEasyBetav3.exe"
RMDIR /S /Q "B:\Mis_documentos\Programacion\Programas_en_Python\Programas\VEasy\VEasyBeta v3\__pycache__"
RMDIR /S /Q "B:\Mis_documentos\Programacion\Programas_en_Python\Programas\VEasy\VEasyBeta v3\dist\"
RMDIR /S /Q "B:\Mis_documentos\Programacion\Programas_en_Python\Programas\VEasy\VEasyBeta v3\build\"
DEL /Q "B:\Mis_documentos\Programacion\Programas_en_Python\Programas\VEasy\VEasyBeta v3\VEasyBetav3.spec"

REM --add-data %carp1% 
REM --add-data %carp2%
REM --noconsole
REM --runtime-tmpdir C:\Users\raulp\Desktop

PAUSE

