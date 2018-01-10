#!/usr/bin/env python

import os
import sys
import subprocess
import shutil
import pexpect
from pylib.print_color import *

CLONE_FOLDER = "serviceagent-bm"
CLONE_FOLDER_SA = "serviceagent"

BUILD_FOLDER = "build"
PACKAGE_FOLDER = "package"

SSH_NEWKEY = r'Are you sure you want to continue connecting \(yes/no\)\?'

TARGET_ADDRESS = ''
TARGET_FOLDER = ''
TARGET_PASSWORD = 'root'

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

targetfile = os.path.join(CWD,  CLONE_FOLDER, BUILD_FOLDER, PACKAGE_FOLDER, 'armv7-a', 'bin/sa-service')
printheader("##########################################################")
printheader("### Looking for the target file : ")
printheader("### " + targetfile)
printheader("##########################################################")
checkPath(targetfile, True)

printheader("##########################################################")
printheader("### Deleting Target Folder")
printheader("### " + TARGET_ADDRESS + ':' + TARGET_FOLDER)
printheader("##########################################################")
child = pexpect.spawn('ssh root@%s rm -rf %s'
	%(TARGET_ADDRESS, TARGET_FOLDER))
setpassword()

printheader("##########################################################")
printheader("### Installing binary files to Target")
printheader("### " + TARGET_ADDRESS + ':' + TARGET_FOLDER)
printheader("##########################################################")
child = pexpect.spawn('scp -r %s root@%s:%s'
	%(os.path.join(CWD,  CLONE_FOLDER, BUILD_FOLDER, PACKAGE_FOLDER, 'armv7-a'),
	TARGET_ADDRESS,
	TARGET_FOLDER))
setpassword()
