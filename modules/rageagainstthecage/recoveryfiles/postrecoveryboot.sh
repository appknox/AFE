#!/sbin/sh

# Restart with root hacked adbd
echo msc_adb > /dev/usb_device_mode
touch /tmp/recovery.log
sync

NEEDS_ADBD=$(ps | grep adbd | grep -v grep)
if [ -z "$NEEDS_ADBD" ]
then
    /sbin/adbd recovery &
fi
