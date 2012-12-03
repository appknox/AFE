#!/bin/sh
START=$(date +%s)
clear
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
     Modified FJ APKTools v2.0 PLUGIN by AFE Team"
rm -rf ~/apktool/framework
rm -rf tools/icsfw
mkdir -p tools/icsfw
cd tools/icsfw
wget http://fj-apktools.googlecode.com/files/icsfw.tgz
tar -xzf icsfw.tgz
cd ../..
java -jar tools/apktool.jar if tools/icsfw/framework-res.apk
java -jar tools/apktool.jar if tools/icsfw/twframework-res.apk
java -jar tools/apktool.jar if tools/icsfw/SystemUI.apk
echo "----------"
echo "ICS framework files installed to ~/apktool/framework"
echo "----------"
END=$(date +%s)
ELAPSED=$((END - START))
E_MIN=$((ELAPSED / 60))
E_SEC=$((ELAPSED - E_MIN * 60))
printf "Elapsed: "
[ $E_MIN != 0 ] && printf "%d min(s) " $E_MIN
printf "%d sec(s)\n" $E_SEC
echo "Finished."
