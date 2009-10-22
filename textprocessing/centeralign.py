import sys
from textprocessing import *

def center_align():     
    if len( sys.argv ) == 3:
        file = open(sys.argv[2],'r')

    if len( sys.argv ) == 2:
        file = sys.stdin

    width = int(sys.argv[1])
    line = file.readline()
    while line:
        print align('center',line,width)
        line = file.readline()
        
center_align()
