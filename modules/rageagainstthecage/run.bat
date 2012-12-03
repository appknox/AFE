@echo off
cls
echo One Click Root ^& CWM 3.1.0.1 for the Epic 4G
echo.
echo Updated and tweaked by Rodderik and DRockstar 6/24/2011
echo.
echo Original one click by joeykrim and one click installer by noobnl and firon
echo busybox by skeeterslint
echo Huge credits go out to:
echo koush - dual fs recovery binary
echo DRockstar - recovery kernel build
echo.
pause
cd "%~dp0"
IF NOT EXIST rageagainstthecage-arm5.bin goto :Missing
adb kill-server
adb start-server
goto:Connect
:Connect
FOR /F "tokens=*" %%i in ('adb get-state') do SET STATE=%%i
IF "%STATE%"=="device" goto :CheckRoot
echo Phone is not connected.
pause
goto:Connect

:CheckRoot
FOR /F "tokens=*" %%i in ('adb shell id ^| find "uid=0"') do SET ROOT=%%i
IF "%ROOT%."=="." GOTO :Exploit
goto :Root

:Exploit
echo Copy and run the exploit (may take up to two minutes). Ignore messages about re-logging in.
echo If more than five minutes pass, reboot the phone and try again.


adb push rageagainstthecage-arm5.bin /data/local/tmp/rageagainstthecage-arm5.bin
adb push root.sh /data/local/tmp/root.sh
adb shell chmod 755 /data/local/tmp/rageagainstthecage-arm5.bin
adb shell chmod 755 /data/local/tmp/root.sh
adb shell /data/local/tmp/root.sh

echo Wait for phone to reconnect...
@ping 127.0.0.1 -n 21 -w 1000 > nul
set i=0
:CheckStateLoop
@ping 127.0.0.1 -n 2 -w 1000 > nul
set /A i=i+1
IF %i%==30 GOTO :Failed
FOR /F "tokens=*" %%i in ('adb get-state') do SET STATE=%%i
IF "%STATE%" NEQ "device" goto :CheckStateLoop

FOR /F "tokens=*" %%i in ('adb shell id ^| find "uid=0"') do SET ROOT=%%i
IF "%ROOT%." NEQ "." GOTO :Root
goto:Failed


:Failed
echo Root was not obtained after 60 seconds. Make sure the phone is connected and that adb is working. If adb shell isn't root, reboot the phone and try the script again.
pause

:Root
FOR /F "tokens=*" %%i in ('adb get-state') do SET STATE=%%i
IF "%STATE%"=="unknown" GOTO:Abort
echo Mount system as r/w, cleanup old files, do some basic configuration
adb shell mount -t rfs -o remount,rw /dev/block/stl9 /system
FOR /F "tokens=*" %%i in ('adb shell "if [ -f /system/bin/joeykrim-root.sh ]; then echo -n "exists"; fi"') do SET OLDROOT=%%i
IF "%OLDROOT%" EQU "exists" GOTO :Playlogo
goto:Rootsetup
:Playlogo
adb shell rm /system/bin/playlogo
adb shell mv /system/bin/playlogo-orig /system/bin/playlogo
adb shell chmod 755 /system/bin/playlogo
goto:Rootsetup

:Rootsetup
adb push rootsetup /data/local/tmp/rootsetup
adb shell chmod 755 /data/local/tmp/rootsetup
adb shell /data/local/tmp/rootsetup
adb shell rm /data/local/tmp/rootsetup
adb shell rm /system/app/Asphalt5_DEMO_ANMP_Samsung_D700_Sprint_ML.apk
adb shell rm /system/app/FreeHDGameDemos.apk
adb shell sync
@ping 127.0.0.1 -n 5 -w 1000 > nul

echo Copying files onto phone...
adb push su /system/xbin/su
adb push Superuser.apk /system/app/Superuser.apk
adb push busybox /system/xbin/busybox
adb push remount /system/xbin/remount

echo Setting permissions...
adb shell chmod 755 /system/xbin/busybox
adb shell chmod 755 /system/xbin/remount
adb shell chown root.shell /system/xbin/su
adb shell chmod 6755 /system/xbin/su
adb shell ln -s /system/xbin/su /system/bin/su

echo Installing busybox...
adb shell /system/xbin/busybox --install -s /system/xbin

FOR /F "tokens=*" %%i in ('adb shell getprop ro.build.id') do SET OSVERSION=%%i
IF "%OSVERSION%" EQU "FROYO" GOTO :Redirector
goto:Clockwork

:Redirector
echo Installing clockworkmod redirector
adb push recovery /system/bin/recovery
adb push recoveryfiles /system/bin/recoveryfiles/
adb push recoveryfiles/etc /system/bin/recoveryfiles/etc/
adb push recoveryres /system/bin/recoveryres/
adb shell busybox chmod -R 0755 /system/bin/recoveryfiles/*
adb shell busybox chmod -R 0755 /system/bin/recoveryres/*
adb shell chmod 0755 /system/bin/recovery
adb shell sync
goto:Clockwork

:Clockwork
echo Installing clockworkmod recovery...
adb push bmlwrite /data/local
adb shell chmod 755 /data/local/bmlwrite
adb push zImage /data/local/tmp/zImage
adb shell /data/local/bmlwrite /data/local/tmp/zImage /dev/block/bml8
goto:CheckRebootLoop

:CheckRebootLoop
REM @ping 127.0.0.1 -n 6 -w 1000 > nul
REM set /A i=i+1
REM IF %i%==45 GOTO :CleanupFailed
REM FOR /F "tokens=*" %%i in ('"adb" get-state') do SET STATE=%%i
REM IF "%STATE%" NEQ "device" goto :CheckRebootLoop

echo Cleaning up files...
@ping 127.0.0.1 -n 6 -w 1000 > nul
adb shell rm /data/local/bmlwrite
adb shell rm /data/local/tmp/zImage
adb shell rm /data/local/tmp/rageagainstthecage-arm5.bin
adb shell rm /data/local/tmp/root.sh
adb shell toolbox reboot

echo.
echo All done!
echo.
echo If your phone did not reboot or root does not
echo work correctly. Please rerun the script.
echo Press any key to exit the script.
pause
adb kill-server
goto:eof

:Abort
echo Aborting script. Phone is still not connected. Reboot the phone and try again.
adb kill-server
pause
goto:eof
:Missing
echo rageagainstthecage-arm5.bin is missing. Make sure you extracted the zip archive correctly.
pause
:CleanupFailed
echo Root succeeded, but cleanup failed. Manually remove files in /data/local/tmp/.
pause
goto:eof