import sys
from textprocessing import *

def wrap():     
    if len( sys.argv ) == 3:
        file = open(sys.argv[2],'r')

    if len( sys.argv ) == 2:
        file = sys.stdin

    width = int(sys.argv[1])
    line = file.readline()
    while line:
        line1,line = wrap_on(line,width)
        print line1
        if len(line) == 0:
            line = file.readline()
if __name__ == '__main__':
	wrap()
