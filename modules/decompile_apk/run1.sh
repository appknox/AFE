#!/bin/sh

version=1.0

chmod -R +x tools
PATH=tools:$PATH

while :
do

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
  echo "================================================="
  echo "*                FJ APKTools v2.0               *"
  echo "================================================="  
  echo "  1 - Install Framework Files"
  echo "  2 - Decompile GB apk"
  echo "  3 - Decompile ICS apk"
  echo "  4 - Decompile Other apk"
  echo "  5 - Compile GB apk"
  echo "  6 - Compile ICS apk"
  echo "  7 - Compile Other apk"
  echo "  8 - Unarchive original signed apk"
  echo "  9 - Unarchive unsigned working apk"
  echo "  10 - Compress final"
  echo "  CU - Clean up previous projects"
  echo "  --------------------"
  echo "  0 - More Options"
  echo "  --------------------"
  echo "  x - Exit"
  echo 
  echo -n "Enter option: "
  read opt
  
  if [ "$?" != "1" ]
  then
    case $opt in
     1) sh tools/fwmenu; echo "Done.";;
      2) sh tools/decgb.sh; echo "Done.";;     
      3) sh tools/decics.sh; echo "Done.";;
      4) sh tools/decother.sh; echo "Done.";;
      5) sh tools/comgb.sh; echo "Done.";;
      6) sh tools/comics.sh; echo "Done.";;
      7) sh tools/comother.sh; echo "Done.";;
      8) sh tools/unziporig.sh; echo "Done.";;
      9) sh tools/unzipworking.sh; echo "Done.";;
      10) sh tools/zipfinal.sh; echo "Done.";;
      CU) sh tools/cleanup.sh; echo "Done.";;
      0) sh tools/othermenu; echo "Done.";;
      x) clear; echo; echo "Goodbye."; echo; exit 1;;
      *) echo "Invalid option"; continue;;
    esac
  fi

  tools/press_enter

done

