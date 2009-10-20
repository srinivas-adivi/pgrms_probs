import sys

def reverse():
	return ''.join(line for line in open(sys.argv[1]).readlines()[::-1]).strip()

print reverse()

