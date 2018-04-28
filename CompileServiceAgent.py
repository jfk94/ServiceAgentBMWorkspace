#!/usr/bin/env python

import os
import sys
import commands
import subprocess
import getpass
from pylib.print_color import *

PAPYRUSRT = "obigo-sdk/Papyrus-RT/papyrusrt"
SA_FOLDER = "sa"
CDT_PROJECT = "ServiceAgent_CDTProject"
BINARY_NAME = "ServiceAgent_CDTProject"

INSTALL_FOLDER = "ServiceAgentBM"
CLONE_FOLDER = "sa-bm"
CLONE_FOLDER_SA = "src"

BUILD_FOLDER = "build"
BUILD_SCRIPT = "sa_build.sh"
BUILD_TARGET = "-bt"

CONFIGURATION = ''
CONFIGURATION_DEBUG = 'Debug'
CLEANBUILD = '-build'

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
	message = __file__ + " <Configuration Name> [clean]"
	printfail(message)
	sys.exit()
if len(sys.argv) > 2:
	if sys.argv[2] == 'clean':
		CLEANBUILD = '-cleanBuild'
	else:
		message = __file__ + " <Configuration Name> [clean]"
		printfail(message)
		sys.exit()

CONFIGURATION = sys.argv[1]

printheader("##########################################################")
printheader("### Looking for PapyrusRT ")
printheader("### " + os.path.join('/home', getpass.getuser(), PAPYRUSRT))
printheader("##########################################################")
checkPath(os.path.join('/home', getpass.getuser(), PAPYRUSRT), True)

DEPENDECY_LIBRARY = os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, CLONE_FOLDER_SA,SA_FOLDER, 'external/armv7-a/lib/libsvchttp.a')
if CONFIGURATION != CONFIGURATION_DEBUG:
	printheader("##########################################################")
	printheader("### Looking for dependecy library ")
	printheader("### " + DEPENDECY_LIBRARY)
	printheader("##########################################################")
	checkPath(DEPENDECY_LIBRARY, True)

SOURCE_CODE_GENERATED = os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, CLONE_FOLDER_SA, SA_FOLDER, CDT_PROJECT, 'src')
printheader("##########################################################")
printheader("### Looking for source code generated ")
printheader("### " + SOURCE_CODE_GENERATED)
printheader("##########################################################")
checkPath(SOURCE_CODE_GENERATED, True)

printheader("##########################################################")
printheader("### Compiling CDT Project ")
printheader("##########################################################")
subprocess.call([os.path.join('/home', getpass.getuser(), PAPYRUSRT),
	'--launcher.suppressErrors', '-nosplash', '-application',
	'org.eclipse.cdt.managedbuilder.core.headlessbuild',
	'-import',
	os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, CLONE_FOLDER_SA,
		SA_FOLDER, CDT_PROJECT),
	CLEANBUILD,
	CDT_PROJECT + '/' + CONFIGURATION]);
