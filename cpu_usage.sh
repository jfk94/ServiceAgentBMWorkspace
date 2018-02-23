#!/bin/sh

me=`basename "$0"`
_now=$(date +"%m_%d_%Y")

if test "$#" -eq 0; then
    echo "USAGE: ./${me} process [process]"
    exit 1
fi

REPORT_FILE="CPU_Usage_$_now"

echo "  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND" >> $REPORT_FILE

while :
do
    for i in "$@"
    do
        top -p $(pgrep -d',' $i) -n 1 | sed "/$i/!d"  >> $REPORT_FILE
    done
    sleep 1;
done
