import sys
from textprocessing import *

def text_process():     
    if len( sys.argv ) == 2:
        file = open(sys.argv[1])

    if len( sys.argv ) == 1:
        file = sys.stdin

    dir1 = {'#linewidth':'80','#align': 'left','#wrap':'off'}
    line = file.readline() 
    while line:
        if line[0] == '#':
            list_of_words = line.split()
            if dir1.has_key(list_of_words[0]):
                dir1[list_of_words[0]] = list_of_words[1]
        else:
            width = int(dir1['#linewidth'])
            align_type = dir1['#align']
            wrap_switch = dir1['#wrap']
            while len(line)>0:
                line1,line = wordwrap(wrap_switch,line,width)
                print align(align_type,line1,width)
        line = file.readline()
        
text_process()
