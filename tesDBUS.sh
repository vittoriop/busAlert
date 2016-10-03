#!/usr/bin/env bash

user="$(whoami)"
pids=`pgrep -u $user`

for pid in $pids; do
    dbus=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$pid/environ|cut -d= -f2-)
    if [ -n $dbus ]; then
        IFS="," read -ra array <<< "$dbus"
        dbus_value="${array[0]}"
        if [[ $dbus_value != "" ]]; then
            echo $dbus_value
            break
        fi
    fi
done
