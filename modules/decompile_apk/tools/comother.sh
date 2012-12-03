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
rm -rf out
mkdir out
java -jar tools/apktoolhc.jar b Working
mv Working/dist/*.apk ../../Output
echo "----------"
echo "Working unsigned Other apk placed into 'Output' directory"
echo "----------"
END=$(date +%s)
ELAPSED=$((END - START))
E_MIN=$((ELAPSED / 60))
E_SEC=$((ELAPSED - E_MIN * 60))
printf "Elapsed: "
[ $E_MIN != 0 ] && printf "%d min(s) " $E_MIN
printf "%d sec(s)\n" $E_SEC
echo "Finished."
