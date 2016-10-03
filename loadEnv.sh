#!/usr/bin/env bash

# user="$(whoami)"
# pids=`pgrep -u $user`
# 
# for pid in $pids; do
#     dbus=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$pid/environ|cut -d= -f2-)
#     if [ -n $dbus ]; then
#         export DBUS_SESSION_BUS_ADDRESS=$dbus
#         break
#         # IFS="," read -ra array <<< "$dbus"
#         # dbus_value="${array[0]}"
#         # if [[ $dbus_value != "" ]]; then
#         #     export DBUS_SESSION_BUS_ADDRESS=$dbus_value
#         #     break
#         # fi
#     fi
# done
# use this on gnome
PID=$(pgrep gnome-session)
dbus=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)
export DBUS_SESSION_BUS_ADDRESS=$dbus
XAUTHORITY=/home/vittorio/.Xauthority
export XAUTHORITY
DISPLAY=:0
export DISPLAY
# echo $DBUS_SESSION_BUS_ADDRESS >> /home/vittorio/Desktop/cronLog.txt
# echo $XAUTHORITY >> /home/vittorio/Desktop/cronLog.txt
# echo $DISPLAY >> /home/vittorio/Desktop/cronLog.txt
python /home/vittorio/Code/myRepo/Python/busAlert/busAlert.py
