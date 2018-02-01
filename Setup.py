#!/usr/bin/env python

import os
import subprocess
import shutil
from pylib.print_color import *
from pylib.copytree import *

UICCID_PATH = '/etc/sa/'
UICCID_FILE = 'uiccid.txt'
NAVI_RUN_SCRIPT = 'run_navi.sh'
NAVI_PATH = '/home/telecons/work/SYMC_C300'
AF_TARGET_PATH = '/home/vagrant/Release/Obigo/OAF'
AF_SOURCE_PATH = '/home/vagrant/work/Release/Obigo/OAF'
AF_W20 = 'w20'
SA_TARGET_PATH = '/home/vagrant/Release/Obigo/SA'
SA_SOURCE_PATH = '/home/vagrant/work/Release/Obigo/SA'
SA_SERVICE = 'bin/sa-service'
RUN_SCRIPT_C300_TARGET_PATH = '/home/vagrant/Release/Obigo'
RUN_SCRIPT_C300_SOURCE_PATH = '/home/vagrant/work/Release/Obigo'
RUN_SCRIPT_C300 = 'run_c300_bm.sh'

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

printheader("##########################################################")
printheader("### Copying AF from %s to %s" % (AF_SOURCE_PATH, AF_TARGET_PATH))
printheader("##########################################################")
checkPath(AF_SOURCE_PATH, True)
if os.path.exists(AF_TARGET_PATH) == False:
	copytree(AF_SOURCE_PATH, AF_TARGET_PATH)
else:
	SOURCE_TIME = os.path.getmtime(os.path.join(AF_SOURCE_PATH, AF_W20))
	TARGET_TIME = os.path.getmtime(os.path.join(AF_TARGET_PATH, AF_W20))
	printwarning("Source Time : %s , Target Time : %s" % (SOURCE_TIME, TARGET_TIME))
	if SOURCE_TIME != TARGET_TIME:
		printheader("Remove Target : " + AF_TARGET_PATH)
		shutil.rmtree(AF_TARGET_PATH)
		printheader("Copying AF from %s to %s" % (AF_SOURCE_PATH, AF_TARGET_PATH))
		copytree(AF_SOURCE_PATH, AF_TARGET_PATH)

printheader("##########################################################")
printheader("### Copying SA from %s to %s" % (SA_SOURCE_PATH, SA_TARGET_PATH))
printheader("##########################################################")
checkPath(SA_SOURCE_PATH, True)
if os.path.exists(SA_TARGET_PATH) == False:
	copytree(SA_SOURCE_PATH, SA_TARGET_PATH)
else:
	SOURCE_TIME = os.path.getmtime(os.path.join(SA_SOURCE_PATH, SA_SERVICE))
	TARGET_TIME = os.path.getmtime(os.path.join(SA_TARGET_PATH, SA_SERVICE))
	printwarning("Source Time : %s , Target Time : %s" % (SOURCE_TIME, TARGET_TIME))
	if SOURCE_TIME != TARGET_TIME:
		printheader("Remove Target : " + SA_TARGET_PATH)
		shutil.rmtree(SA_TARGET_PATH)
		printheader("Copying SA from %s to %s" % (SA_SOURCE_PATH, SA_TARGET_PATH))
		copytree(SA_SOURCE_PATH, SA_TARGET_PATH)

printheader("##########################################################")
printheader("### Copying %s from %s to %s" % (RUN_SCRIPT_C300, SA_SOURCE_PATH, SA_TARGET_PATH))
printheader("##########################################################")
checkPath(os.path.join(RUN_SCRIPT_C300_SOURCE_PATH, RUN_SCRIPT_C300), True)
if os.path.exists(os.path.join(RUN_SCRIPT_C300_TARGET_PATH, RUN_SCRIPT_C300)) == False:
	shutil.copyfile(os.path.join(RUN_SCRIPT_C300_SOURCE_PATH, RUN_SCRIPT_C300), os.path.join(RUN_SCRIPT_C300_TARGET_PATH, RUN_SCRIPT_C300))
else:
	SOURCE_TIME = os.path.getmtime(os.path.join(RUN_SCRIPT_C300_SOURCE_PATH, RUN_SCRIPT_C300))
	TARGET_TIME = os.path.getmtime(os.path.join(RUN_SCRIPT_C300_TARGET_PATH, RUN_SCRIPT_C300))
	printwarning("Source Time : %s , Target Time : %s" % (SOURCE_TIME, TARGET_TIME))
	if SOURCE_TIME != TARGET_TIME:
		printheader("Remove Target : " + os.path.join(RUN_SCRIPT_C300_TARGET_PATH, RUN_SCRIPT_C300))
		os.remove(os.path.join(RUN_SCRIPT_C300_TARGET_PATH, RUN_SCRIPT_C300))
		printheader("Copying %s from %s to %s" % (RUN_SCRIPT_C300, SA_SOURCE_PATH, SA_TARGET_PATH))
		shutil.copyfile(os.path.join(RUN_SCRIPT_C300_SOURCE_PATH, RUN_SCRIPT_C300), os.path.join(RUN_SCRIPT_C300_TARGET_PATH, RUN_SCRIPT_C300))
