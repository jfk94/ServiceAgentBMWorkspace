class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def printfail(msg):
	print bcolors.FAIL + msg + bcolors.ENDC

def printheader(msg):
	print bcolors.HEADER + msg + bcolors.ENDC

def printwarning(msg):
	print bcolors.WARNING + msg + bcolors.ENDC
