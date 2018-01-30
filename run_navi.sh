#!/bin/sh
export DISPLAY=:0
export LD_LIBRARY_PATH=${PWD}:/usr/lib:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=/home/vagrant/Qt5.8.0/5.8/gcc_64/lib/:$LD_LIBRARY_PATH

echo "export LD_LIBRARY_PATH=${PWD}:/usr/lib:${LD_LIBRARY_PATH}"

while ADDRESS='' read -r line; do
    echo "Text read from file: $line"
    export DBUS_SESSION_BUS_ADDRESS="$line"
    echo "export DBUS_SESSION_BUS_ADDRESS=${DBUS_SESSION_BUS_ADDRESS}"
done < "/tmp/sa_dbus_session.dat"

./NaviC300App
