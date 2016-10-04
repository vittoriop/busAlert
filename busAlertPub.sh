#!/usr/bin/env bash

user=whoami
PID=$(pgrep gnome-session)
dbus=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)
export DBUS_SESSION_BUS_ADDRESS=$dbus
XAUTHORITY=/home/$user/.Xauthority
export XAUTHORITY
DISPLAY=:0
export DISPLAY
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $DIR
python $DIR/busAlert.py
