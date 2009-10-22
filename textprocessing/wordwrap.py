import sys
from textprocessing import *

def wordwrap():     
    if len( sys.argv ) == 3:
        file = open(sys.argv[2],'r')

    if len( sys.argv ) == 2:
        file = sys.stdin

    width = int(sys.argv[1])
    line = file.readline()
    while line:
        line=line.strip()
        line1,line = wordwrap_on(line,width)
        print line1
        if line == '':
            line = file.readline()
wordwrap()
