#!/usr/bin/env python

import os
import sys
import subprocess
import shutil
from pylib.print_color import *

PAPYRUSRT = "obigo-sdk/Papyrus-RT/papyrusrt"
SA_FOLDER = "SA"
CDT_PROJECT = "ServiceAgent_CDTProject"
BINARY_NAME = "ServiceAgent_CDTProject"

INSTALL_FOLDER = "ServiceAgentBM"
CLONE_FOLDER = "serviceagent-bm"
CLONE_FOLDER_SA = "serviceagent"

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

if len(sys.argv) < 3:
	message = __file__ + " <Debug or Release> <host or target>"
	printfail(message)
	sys.exit()

CONFIGURATION = sys.argv[1]
PLATFORM = sys.argv[2]

def CopyHost():
	binaryfile = os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, CLONE_FOLDER_SA,
		SA_FOLDER, CDT_PROJECT, CONFIGURATION, BINARY_NAME)
	printheader("##########################################################")
	printheader("### Looking for the binary file : ")
	printheader("### " + binaryfile)
	printheader("##########################################################")
	checkPath(binaryfile, True)

	targetfile = os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER, PACKAGE_FOLDER, 'x86_64', 'bin/sa-service')
	printheader("##########################################################")
	printheader("### Copying the binary file to ")
	printheader("### " + targetfile)
	printheader("##########################################################")
	checkPath(targetfile, True)
	shutil.copyfile(binaryfile, targetfile)

def CopyTarget():
	printheader("##########################################################")
	printheader("### There is no action for copying the target binary file")
	printheader("##########################################################")

if PLATFORM == 'target':
	CopyTarget()
else:
	CopyHost()
