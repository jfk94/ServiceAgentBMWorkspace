#!/usr/bin/env python

import os
import sys
import subprocess
from pylib.print_color import *

INSTALL_FOLDER = "ServiceAgentBM"
CLONE_FOLDER = "sa-bm"
CLONE_FOLDER_SA = "src"

BUILD_FOLDER = "build"
PACKAGE_FOLDER = "package"

KILL_SCRIPT = "kill_sad.sh"

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

targetfile = os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER, PACKAGE_FOLDER, 'x86_64', KILL_SCRIPT)
printheader("##########################################################")
printheader("### Looking for the script ")
printheader("### " + targetfile)
printheader("##########################################################")
checkPath(targetfile, True)
os.chdir(os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER, PACKAGE_FOLDER, 'x86_64'))
subprocess.call(['./' + KILL_SCRIPT]);
