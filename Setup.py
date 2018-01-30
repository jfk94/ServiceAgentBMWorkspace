#!/usr/bin/env python

import os
import subprocess
import shutil
from pylib.print_color import *

UICCID_PATH = '/etc/sa/'
UICCID_FILE = 'uiccid.txt'
NAVI_RUN_SCRIPT = 'run_navi.sh'
NAVI_PATH = '/home/telecons/work/SYMC_C300'

def checkPath(path, exist):
	if exist == True:
		if os.path.exists(path) == False:
			printfail(path + " doesn't exist")
			sys.exit()
		else:
			return
	if exist == False:
		if os.path.exists(path) == True:
			printfail(path + " already exist")
			sys.exit()
		else:
			return

CWD = os.path.dirname(os.path.realpath(__file__))
os.chdir(CWD)

printheader("##########################################################")
printheader("### Copying %s to %s" % (os.path.join(CWD, UICCID_FILE), os.path.join(UICCID_PATH, UICCID_FILE)))
printheader("##########################################################")
checkPath(os.path.join(CWD, UICCID_FILE), True)
if (os.path.exists(UICCID_PATH)):
	subprocess.call(['sudo', 'rm', '-rf', UICCID_PATH]);
subprocess.call(['sudo', 'mkdir', UICCID_PATH]);
subprocess.call(['sudo', 'cp', os.path.join(CWD, UICCID_FILE), os.path.join(UICCID_PATH, UICCID_FILE)]);

printheader("##########################################################")
printheader("### Copying %s to %s" % (os.path.join(CWD, NAVI_RUN_SCRIPT), os.path.join(NAVI_PATH, NAVI_RUN_SCRIPT)))
printheader("##########################################################")
checkPath(os.path.join(CWD, NAVI_RUN_SCRIPT), True)
checkPath(NAVI_PATH, True)
subprocess.call(['sudo', 'cp', os.path.join(CWD, NAVI_RUN_SCRIPT), os.path.join(NAVI_PATH, NAVI_RUN_SCRIPT)]);
