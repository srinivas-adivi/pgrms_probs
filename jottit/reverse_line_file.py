import sys

def reverse_each_line():
	return '\n'.join(line.strip()[::-1] for line in open(sys.argv[1]).readlines()).strip()
print reverse_each_line()
