
def wrap_on(line,width):
    if len(line) <= width:
        return line.strip(),''
    else:
        return line[:width],line[width:]
 
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
        
def wordwrap(switch,line,width):
    if switch == 'on':
        line1,line2= wordwrap_on(line,width)
        return line1,line2
    else:
        return line,''
        
def center_align(line,width):
    line = line.strip()
    align = width -len(line)
    if align >= 0:
        return ' '*(align/2)+ line
    else:
        return line
                
def right_align(line,width):
    line = line.strip()
    align = width - len(line)
    if align >= 0:
        return ' '*align+line
    else:
        return line

def align(align_type,line,width):
    if align_type == 'center':
        return center_align(line,width)
       
    if align_type == 'right':
        return right_align(line,width)
        
    if align_type == 'left':
        print line
