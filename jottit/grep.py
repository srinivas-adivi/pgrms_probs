def grep(filename, word):
    '''It takes file and searching word as arguments.and return all lines in given file which contains given word.'''
    return ''.join(line for line in open(filename).readlines() if word in line)

if __name__ == "__main__":
    import sys
    import doctest
    doctest.testmod()
    try:
	sys.stdout.write(grep(sys.argv[1], sys.argv[2]))
    except IOError, (strerror):
        print "Please give existing file as first argument"
    except IndexError, (strerror):
	print "USAGE: python grep.py she.txt sure"
