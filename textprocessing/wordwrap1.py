import sys

def wordwrap_on(line,width):
    if len(line) <= width:
        return line,''
    else:
        char_list = list(line)
        length,length1 = 0,len(line)

        while length1 > width and line[:length1].find(' ')!= -1:
            length = char_list[::-1].index(' ',length)+1
            length1 = len(line)-length
        
        length = len(line)-length  
        return line[:length],line[length+1:]
    
def wordwrap():
    """ This function aklja slfjala;sklf
    asjdlkfjask lasdfkl"""
    file = open(sys.argv[2])
    width = int(sys.argv[1]) 
    line = file.readline()
    while line:
        line = line.strip()
        line1,line = wordwrap_on(line,width)
        print line1
        if line=='' :
            line = file.readline()
wordwrap()
