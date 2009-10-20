import sys

def tail():
	sys.stdout.write(''.join(open(sys.argv[1]).readlines()[-10:]))
tail()
