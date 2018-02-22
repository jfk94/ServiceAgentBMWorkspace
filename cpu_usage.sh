#!/bin/sh

REPORT_FILE="CPU_Usage_$1"
rm -rf $REPORT_FILE

echo "  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND" >> $REPORT_FILE
while :; do top -p $(pgrep -d',' $1) -n 1 | sed "/$1/!d"  >> $REPORT_FILE; sleep 1; done
