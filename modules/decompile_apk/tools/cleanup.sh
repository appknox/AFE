#!/bin/sh
START=$(date +%s)
clear
rm -rf Working
rm -rf original_apk
rm -rf out
rm -rf final
rm -rf signing
mkdir original_apk
mkdir out
mkdir final
mkdir signing
echo "----------"
echo "All project files and folders cleaned"
echo "----------"
END=$(date +%s)
ELAPSED=$((END - START))
E_MIN=$((ELAPSED / 60))
E_SEC=$((ELAPSED - E_MIN * 60))
printf "Elapsed: "
[ $E_MIN != 0 ] && printf "%d min(s) " $E_MIN
printf "%d sec(s)\n" $E_SEC
echo "Finished."
