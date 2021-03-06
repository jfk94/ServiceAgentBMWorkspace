#!/usr/bin/env python

import os
import sys
import commands
import subprocess
import shutil
from pylib.print_color import *

INSTALL_FOLDER = "ServiceAgentBM"
CLONE_FOLDER = "serviceagent-bm"
CLONE_FOLDER_SA = "serviceagent"
BUILD_FOLDER = "build"
PACKAGE_FOLDER = "package"
BUILD_SCRIPT = "sa_build.sh"
HOST_OPTION = "-bh"
TARGET_OPTION = "-bt"
BRANCH = ''
PLATFORM = ''

UICCID_PATH = '/etc/sa/'
UICCID_FILE = 'uiccid.txt'

CWD = os.path.dirname(os.path.realpath(__file__))
os.chdir(CWD)

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

if len(sys.argv) < 3:
	message = __file__ + " <branch name to check out> <host or target>"
	printfail(message)
	sys.exit()

BRANCH = sys.argv[1]
PLATFORM = sys.argv[2]

printheader("##########################################################")
printheader("### ServiceAgentBM Folder ")
printheader("##########################################################")
if os.path.exists(os.path.join(CWD, INSTALL_FOLDER)) == False:
	os.makedirs(os.path.join(CWD, INSTALL_FOLDER))
checkPath(os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER), False)

printheader("##########################################################")
printheader("### Initializing Repository")
printheader("##########################################################")
os.chdir(os.path.join(CWD, INSTALL_FOLDER))
os.popen("repo init -u git@github.com:OBIGOGIT/ServiceAgentBM-Build.git -b develop")
os.popen("repo sync | repo forall -c git checkout develop")
checkPath(os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, CLONE_FOLDER_SA), True)
os.chdir(os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, CLONE_FOLDER_SA))
subprocess.call(['git', 'checkout', BRANCH]);
if commands.getoutput('git status').find('Not currently on any branch') >= 0:
	printfail("Unknow branch : " + BRANCH)
	sys.exit()

printheader("##########################################################")
printheader("### Compiling")
printheader("##########################################################")
os.chdir(os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER))

if PLATFORM == 'host':
	subprocess.call(['./' + BUILD_SCRIPT, 'all', HOST_OPTION]);
	checkPath(os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER, PACKAGE_FOLDER, 'x86_64'), True)
elif PLATFORM == 'target':
	subprocess.call(['./' + BUILD_SCRIPT, 'all', TARGET_OPTION]);
	checkPath(os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER, PACKAGE_FOLDER, 'armv7-a'), True)
else:
	printfail("Unknow Platform : " + PLATFORM)
	sys.exit()

printheader("##########################################################")
printheader("### Copying %s to %s" % (os.path.join(CWD, UICCID_FILE), os.path.join(UICCID_PATH, UICCID_FILE)))
printheader("##########################################################")
checkPath(os.path.join(CWD, UICCID_FILE), True)
if (os.path.exists(UICCID_PATH)):
	subprocess.call(['sudo', 'rm', '-rf', UICCID_PATH]);
subprocess.call(['sudo', 'mkdir', UICCID_PATH]);
subprocess.call(['sudo', 'cp', os.path.join(CWD, UICCID_FILE), os.path.join(UICCID_PATH, UICCID_FILE)]);
