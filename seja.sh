#!/bin/sh

./sa-ctl.sh -t

systemctl start obigo-af
./run_cicagent.sh 2>/dev/null &
./run_sauid.sh 2>/dev/null &
./run_saui_test.sh 2>/dev/null &
./run_sad.sh
