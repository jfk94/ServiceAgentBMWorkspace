#!/usr/bin/env python

import os
import sys
import subprocess
import shutil
import pexpect
from pylib.print_color import *

INSTALL_FOLDER = "ServiceAgentBM"
CLONE_FOLDER = "sa-bm"
CLONE_FOLDER_SA = "src"

BUILD_FOLDER = "build"
PACKAGE_FOLDER = "package"

SSH_NEWKEY = r'Are you sure you want to continue connecting \(yes/no\)\?'

TARGET_ADDRESS = ''
TARGET_FOLDER = ''
TARGET_PASSWORD = 'root'

SED_SCRIPT = 'replace_workingfolder.sh'
RUN_SCRIPT_SAD = 'run_sad.sh'
RUN_SCRIPT_SAUI = 'run_sauid.sh'
RUN_SCRIPT_CICAGENT = 'run_cicagent.sh'
SA_SERVICE = 'obigo-sa'
SA_PROCESS_NAME = 'sa-service'
SAUI_PROCESS_NAME = 'saui-service'

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

def setpassword():
	child.logfile = sys.stdout

	i = child.expect([pexpect.TIMEOUT, SSH_NEWKEY, '[P|p]assword: '])
	if i == 0: # Timeout
	    print('ERROR!')
	    print('SSH could not login. Here is what SSH said:')
	    print(child.before, child.after)
	    sys.exit (1)
	if i == 1: # SSH does not have the public key. Just accept it.
		child.sendline('yes')
		child.expect('[P|p]assword: ')
		child.sendline(TARGET_PASSWORD)
	if i == 2: # Target requests password
		child.sendline(TARGET_PASSWORD)
	child.expect(pexpect.EOF)

if len(sys.argv) < 3:
	message = __file__ + " <Target Address> <Target Folder>"
	printfail(message)
	sys.exit()

TARGET_ADDRESS = sys.argv[1]
TARGET_FOLDER = sys.argv[2]

targetfile = os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER, PACKAGE_FOLDER, 'armv8-a', 'bin/sa-service')
printheader("##########################################################")
printheader("### Looking for the target file : ")
printheader("### " + targetfile)
printheader("##########################################################")
checkPath(targetfile, True)

printheader("##########################################################")
printheader("### Stopping SA Service : " + SA_SERVICE)
printheader("##########################################################")
child = pexpect.spawn('ssh root@%s systemctl -a | grep obigo; systemctl stop %s'%(TARGET_ADDRESS, SA_SERVICE))
setpassword()
child = pexpect.spawn('ssh root@%s systemctl -a | grep obigo; systemctl stop %s'%(TARGET_ADDRESS, 'obigo-saui'))
setpassword()
child = pexpect.spawn('ssh root@%s systemctl -a | grep obigo; systemctl stop %s'%(TARGET_ADDRESS, 'cicagent'))
setpassword()
child = pexpect.spawn('ssh root@%s systemctl -a | grep obigo; systemctl stop %s'%(TARGET_ADDRESS, 'obigo-af'))
setpassword()
child = pexpect.spawn('ssh root@%s systemctl -a | grep obigo'%(TARGET_ADDRESS))
setpassword()
child = pexpect.spawn('ssh root@%s pkill %s'%(TARGET_ADDRESS, SA_PROCESS_NAME))
setpassword()
child = pexpect.spawn('ssh root@%s pkill %s'%(TARGET_ADDRESS, SAUI_PROCESS_NAME))
setpassword()
child = pexpect.spawn('ssh root@%s pkill %s'%(TARGET_ADDRESS, 'cicagent'))
setpassword()

printheader("##########################################################")
printheader("### Deleting Target Folder")
printheader("### " + TARGET_ADDRESS + ':' + TARGET_FOLDER)
printheader("##########################################################")
child = pexpect.spawn('ssh root@%s rm -rf %s'%(TARGET_ADDRESS, TARGET_FOLDER))
setpassword()

printheader("##########################################################")
printheader("### Installing binary files to Target")
printheader("### " + TARGET_ADDRESS + ':' + TARGET_FOLDER)
printheader("##########################################################")
child = pexpect.spawn('scp -r %s root@%s:%s'
	%(os.path.join(CWD, INSTALL_FOLDER, CLONE_FOLDER, BUILD_FOLDER, PACKAGE_FOLDER, 'armv8-a'),
	TARGET_ADDRESS,
	TARGET_FOLDER))
setpassword()

checkPath(os.path.join(CWD, 'seja.sh'), True)
child = pexpect.spawn('scp -r %s root@%s:%s'
	%(os.path.join(CWD, 'seja.sh'),
	TARGET_ADDRESS,
	TARGET_FOLDER))
setpassword()

printheader("##########################################################")
printheader("### Changing working folder path of " + RUN_SCRIPT_SAD)
printheader("##########################################################")
checkPath(os.path.join(CWD, SED_SCRIPT), True)
child = pexpect.spawn('scp -r %s root@%s:%s'
	%(os.path.join(CWD, SED_SCRIPT),
	TARGET_ADDRESS,
	TARGET_FOLDER))
setpassword()
child = pexpect.spawn("ssh root@%s %s %s"
	%(TARGET_ADDRESS,
	os.path.join(TARGET_FOLDER, SED_SCRIPT),
	os.path.join(TARGET_FOLDER, RUN_SCRIPT_SAD)))
setpassword()

printheader("##########################################################")
printheader("### Changing working folder path of " + RUN_SCRIPT_SAUI)
printheader("##########################################################")
checkPath(os.path.join(CWD, SED_SCRIPT), True)
child = pexpect.spawn('scp -r %s root@%s:%s'
	%(os.path.join(CWD, SED_SCRIPT),
	TARGET_ADDRESS,
	TARGET_FOLDER))
setpassword()
child = pexpect.spawn("ssh root@%s %s %s"
	%(TARGET_ADDRESS,
	os.path.join(TARGET_FOLDER, SED_SCRIPT),
	os.path.join(TARGET_FOLDER, RUN_SCRIPT_SAUI)))
setpassword()

printheader("##########################################################")
printheader("### Changing working folder path of " + RUN_SCRIPT_CICAGENT)
printheader("##########################################################")
checkPath(os.path.join(CWD, SED_SCRIPT), True)
child = pexpect.spawn('scp -r %s root@%s:%s'
	%(os.path.join(CWD, SED_SCRIPT),
	TARGET_ADDRESS,
	TARGET_FOLDER))
setpassword()
child = pexpect.spawn("ssh root@%s %s %s"
	%(TARGET_ADDRESS,
	os.path.join(TARGET_FOLDER, SED_SCRIPT),
	os.path.join(TARGET_FOLDER, RUN_SCRIPT_CICAGENT)))
setpassword()

printheader("##########################################################")
printheader("### Copying %s to %s" % (os.path.join(CWD, UICCID_FILE), os.path.join(TARGET_FOLDER, UICCID_FILE)))
printheader("##########################################################")
checkPath(os.path.join(CWD, UICCID_FILE), True)
child = pexpect.spawn('scp %s root@%s:%s'%(UICCID_FILE, TARGET_ADDRESS, os.path.join(TARGET_FOLDER, UICCID_FILE)))
setpassword()
