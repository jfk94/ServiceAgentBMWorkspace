#!/usr/bin/env python

import os
import sys
import subprocess
import shutil
from pylib.print_color import *

PAPYRUSRT = "obigo-sdk/Papyrus-RT/papyrusrt"
SA_FOLDER = "sa"
CDT_PROJECT = "ServiceAgent_CDTProject"
BINARY_NAME = "ServiceAgent_CDTProject"

INSTALL_FOLDER = "ServiceAgentBM"
CLONE_FOLDER = "sa-bm"
CLONE_FOLDER_SA = "src"

BUILD_FOLDER = "build"
PACKAGE_FOLDER = "package"

CONFIGURATION = ''
PLATFORM = ''

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

if len(sys.argv) < 2:
	message = __file__ + " <Configuration Name>"
	printfail(message)
	sys.exit()

CONFIGURATION = sys.argv[1]

binaryfile = os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, CLONE_FOLDER_SA,
	SA_FOLDER, CDT_PROJECT, CONFIGURATION, BINARY_NAME)
printheader("##########################################################")
printheader("### Looking for the binary file : ")
printheader("### " + binaryfile)
printheader("##########################################################")
checkPath(binaryfile, True)

targetfile = ''

if CONFIGURATION == 'Debug':
	targetfile = os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER, PACKAGE_FOLDER, 'x86_64', 'bin/sa-service')
else:
	targetfile = os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER, PACKAGE_FOLDER, 'armv8-a', 'bin/sa-service')

printheader("##########################################################")
printheader("### Copying the binary file to ")
printheader("### " + targetfile)
printheader("##########################################################")
checkPath(targetfile, True)
shutil.copyfile(binaryfile, targetfile)
