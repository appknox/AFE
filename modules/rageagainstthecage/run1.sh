#!/bin/bash
#----------------------------------------------------------------------------------------------#
#Android Framework for Exploitation v-1                                                        #
# (C)opyright 2010 - XYS3C                                                                     #
#---Important----------------------------------------------------------------------------------#
#                     *** Do NOT use this for illegal or malicious use ***                     #
#              The programs are provided as is without any guarantees or warranty.             #
#---Defaults-----------------------------------------------------------------------------------#

clear
headr(){
echo "
---The Android Exploitation Framework ---
 _______  _______  _______    _               _______     __   
(  ___  )(  ____ \(  ____ \  ( )  |\     /|  (  __   )   /  \  
| (   ) || (    \/| (    \/  | |  | )   ( |  | (  )  |   \/) ) 
| (___) || (__    | (__      (_)  | |   | |  | | /   |     | | 
|  ___  ||  __)   |  __)      _   ( (   ) )  | (/ /) |     | | 
| (   ) || (      | (        ( )   \ \_/ /   |   / | |     | | 
| )   ( || )      | (____/\  | |    \   /    |  (__) | _ __) (_
|/     \||/       (_______/  (_)     \_/     (_______)(_)\____/
                                                               
Copyright Reserved : XYS3C (Visit us at http://xysec.com)                                                       
"
}
headr
echo "RageAgainstTheCage Exploit & CWM 3.1.0.1"
echo
echo "Updated and tweaked by Rodderik and DRockstar 6/24/2011"
echo "Original one click by joeykrim and one click installer by noobnl and firon"
echo "busybox by skeeterslint"
echo "Huge credits go out to:"
echo "koush - dual fs recovery binary"
echo "DRockstar - recovery kernel build"
echo "### Plugin by Subho Halder for AFE #####"
echo
read -n1 -s -p "Press any key to continue..."

echo -e "Starting adb server"

if [ -z $(which sudo 2>/dev/null) ]; then
	adb kill-server
else
	sudo adb kill-server
fi
if [ -z $(which sudo 2>/dev/null) ]; then
	adb start-server
else
	sudo adb start-server
fi
state=$(adb get-state | tr -d '\r\n[:blank:]')
while [ "$state" != device ]; do
	state=$($adb get-state | tr -d '\r\n[:blank:]')
	read -n1 -s -p "Phone is not connected. Press any key to continue."
	exit
done
root=$(adb shell id | grep uid=0)
if [ -z "$root" ]; then
	echo -e "Copy and run the exploit (may take up to two minutes)"
	adb push rageagainstthecage-arm5.bin /data/local/tmp/rageagainstthecage-arm5.bin
	adb push root.sh /data/local/tmp/root.sh
	adb shell chmod 755 /data/local/tmp/rageagainstthecage-arm5.bin
	adb shell chmod 755 /data/local/tmp/root.sh
	adb shell /data/local/tmp/root.sh
	
	
	echo Wait for phone to reconnect...
	sleep 20;
	i=0;
	state=$(adb get-state | tr -d '\r\n[:blank:]')
	while [[ "$state" != device && $i -lt 30 ]]; do
		state=$(adbadb get-state | tr -d '\r\n[:blank:]')
		let i=i+1;
		sleep 1;
	done
	
	if [ "$state" != "device" ]; then
		echo "Phone did not reconnect after 30 seconds."
		read -n1 -s -p "Pausing script. Unplug and replug USB cable and check the connection (verify with adb shell)."
	fi
	
	
	state=$(adb get-state | tr -d '\r\n[:blank:]')
	if [ "$state" != "device" ]; then
		echo "Aborting script. Phone is still not connected. Reboot the phone and try again.";
		exit 1;
	fi
	
	root=$(adb shell id | grep uid=0)
	if [ -z "$root" ]; then
		echo "Root was not obtained. Please re-run the script."
		exit 1;
	fi

fi

echo "Mount system as r/w, cleanup old files, do some basic configuration"
adb shell mount -t rfs -o remount,rw /dev/block/stl9 /system
oldroot=$(adb shell "if [ -f /system/bin/joeykrim-root.sh ]; then echo -n 'exists'; fi");
if [ -z "$oldroot" ]; then
	adb shell rm /system/bin/playlogo
	adb shell mv /system/bin/playlogo-orig /system/bin/playlogo
	adb shell chmod 755 /system/bin/playlogo
fi
adb push rootsetup /data/local/tmp/rootsetup
adb shell chmod 755 /data/local/tmp/rootsetup
adb shell /data/local/tmp/rootsetup
adb shell rm /data/local/tmp/rootsetup
adb shell rm /system/app/Asphalt5_DEMO_ANMP_Samsung_D700_Sprint_ML.apk
adb shell rm /system/app/FreeHDGameDemos.apk
adb shell sync
sleep 2;

echo "Copying files onto phone..."
adb push su /system/xbin/su
adb push Superuser.apk /system/app/Superuser.apk
adb push busybox /system/xbin/busybox
adb push remount /system/xbin/remount

echo "Setting permissions..."
adb shell chmod 755 /system/xbin/busybox
adb shell chmod 755 /system/xbin/remount
adb shell chown root.shell /system/xbin/su
adb shell chmod 4755 /system/xbin/su
adb shell ln -s /system/xbin/su /system/bin/su

echo "Installing busybox..."
adb shell /system/xbin/busybox --install -s /system/xbin

osversion=$(./adb shell getprop ro.build.id | tr -d '\r\n[:blank:]')
if [ "$osversion" == "FROYO" ]; then
	echo Installing clockworkmod redirector
	adb push recovery /system/bin/recovery
	adb push recoveryfiles /system/bin/recoveryfiles/
	adb push recoveryfiles/etc /system/bin/recoveryfiles/etc/
	adb push recoveryres /system/bin/recoveryres/
	adb shell busybox chmod -R 0755 /system/bin/recoveryfiles/*
	adb shell busybox chmod -R 0755 /system/bin/recoveryres/*
	adb shell chmod 0755 /system/bin/recovery
	adb shell sync
fi

echo "Installing clockworkmod recovery..."
adb push bmlwrite /data/local
adb shell chmod 755 /data/local/bmlwrite
adb push zImage /data/local/tmp/zImage
adb shell /data/local/bmlwrite /data/local/tmp/zImage /dev/block/bml8

echo "Cleaning up files..."
sleep 5;
adb shell rm /data/local/bmlwrite
adb shell rm /data/local/tmp/zImage
adb shell rm /data/local/tmp/rageagainstthecage-arm5.bin
adb shell rm /data/local/tmp/root.sh
adb shell toolbox reboot

if [ -z $(which sudo 2>/dev/null) ]; then
	adb kill-server
else
	sudo adb kill-server
fi
echo "All done!"
echo
echo "If your phone did not reboot or root does not"
echo "work correctly. Please rerun the script."
read -n1 -s -p "Press any key to exit the plugin."
echo
menu