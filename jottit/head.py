import sys

def shead():
	sys.stdout.write(''.join(open(sys.argv[1]).readlines()[:10]))
shead()
