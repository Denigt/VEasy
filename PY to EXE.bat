
@ECHO OFF

SET prog="C:\Users\raulp\Desktop\VEasyBeta v3\VEasyBetav3.py"
SET icono="C:\Users\raulp\Desktop\VEasyBeta v3\Images\VEasy.ico"
SET carp1="C:\Users\raulp\Desktop\VEasyBeta v3\Images;Images"
SET carp2="C:\Users\raulp\Desktop\VEasyBeta v3\Third;Third"

pyinstaller ^
--uac-admin ^
--icon %icono% ^
--onefile ^
%prog%

MOVE /Y "C:\\Users\raulp\Desktop\VEasyBeta v3\dist\VEasyBetav3.exe" "C:\\Users\raulp\Desktop\VEasyBeta v3\VEasyBetav3.exe"
RMDIR /S /Q "C:\Users\raulp\Desktop\VEasyBeta v3\__pycache__"
RMDIR /S /Q "C:\Users\raulp\Desktop\VEasyBeta v3\dist\"
RMDIR /S /Q "C:\Users\raulp\Desktop\VEasyBeta v3\build\"
DEL /Q "C:\Users\raulp\Desktop\VEasyBeta v3\VEasyBetav3.spec"

REM --add-data %carp1% 
REM --add-data %carp2%
REM --noconsole
REM --runtime-tmpdir C:\Users\raulp\Desktop

PAUSE

