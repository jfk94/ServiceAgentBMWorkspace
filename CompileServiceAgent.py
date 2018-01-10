#!/usr/bin/env python

import os
import sys
import commands
import subprocess
import getpass
from pylib.print_color import *

PAPYRUSRT = "obigo-sdk/Papyrus-RT/papyrusrt"
SA_FOLDER = "SA"
CDT_PROJECT = "ServiceAgent_CDTProject"
BINARY_NAME = "ServiceAgent_CDTProject"

INSTALL_FOLDER = "ServiceAgentBM"
CLONE_FOLDER = "serviceagent-bm"
CLONE_FOLDER_SA = "serviceagent"

BUILD_FOLDER = "build"
BUILD_SCRIPT = "sa_build.sh"
BUILD_TARGET = "-bt"

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

def CompileHost():
	printheader("##########################################################")
	printheader("### Looking for PapyrusRT ")
	printheader("### " + os.path.join('/home', getpass.getuser(), PAPYRUSRT))
	printheader("##########################################################")
	checkPath(os.path.join('/home', getpass.getuser(), PAPYRUSRT), True)

	printheader("##########################################################")
	printheader("### Looking for CDT Project ")
	printheader("### " + os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, CLONE_FOLDER_SA,SA_FOLDER, CDT_PROJECT))
	printheader("##########################################################")
	checkPath(os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, CLONE_FOLDER_SA,
		SA_FOLDER, CDT_PROJECT), True)

	printheader("##########################################################")
	printheader("### Compiling CDT Project ")
	printheader("##########################################################")
	subprocess.call([os.path.join('/home', getpass.getuser(), PAPYRUSRT),
		'--launcher.suppressErrors', '-nosplash', '-application',
		'org.eclipse.cdt.managedbuilder.core.headlessbuild',
		'-import',
		os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, CLONE_FOLDER_SA,
			SA_FOLDER, CDT_PROJECT),
		'-cleanBuild',
		CDT_PROJECT + '/' + CONFIGURATION]);

def CompileTarget():
	printheader("##########################################################")
	printheader("### There is not CDT Project for Target Compile ")
	printheader("##########################################################")

	printheader("##########################################################")
	printheader("### Looking for Build Script ")
	printheader("### " + os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER, BUILD_SCRIPT))
	printheader("##########################################################")
	checkPath(os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER, BUILD_SCRIPT), True)
	os.chdir(os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER))

	if CONFIGURATION == 'Debug':
		subprocess.call(['./'+ BUILD_SCRIPT, 'sad', '-d', BUILD_TARGET]);
	else:
		subprocess.call(['./'+ BUILD_SCRIPT, 'sad', '-r', BUILD_TARGET]);

if len(sys.argv) < 3:
	message = __file__ + " <Debug or Release> <host or target>"
	printfail(message)
	sys.exit()

CONFIGURATION = sys.argv[1]
PLATFORM = sys.argv[2]

if PLATFORM == 'target':
	CompileTarget()
else:
	CompileHost()
