
def cat():
    """ concatenate files and print standard input on the standard output
    """
    argv = sys.argv
    len(argv)<=1 and read_input() or read_files(argv)

def read_input():
    """ reads form stdinput to write in stdoutput
    """
    try:
        line = sys.stdin.readline()
        while(line):
            sys.stdout.write(line)
            line = sys.stdin.readline()
    except KeyboardInterrupt:
        sys.stdout.write('\n')
        sys.exit(130)

def read_files(list):
    """ read each file in given list and write to stdout
    """
    failures = []
    for file in list[1:]:
        try:
            sys.stdout.write(open(file).read())

        except IOError, (errno, strerror):
            sys.stdout.write("%s: %s: %s\n" %(list[0], file, strerror))
            failures.append(errno)

    value = not failures and 1 or 0
    sys.exit(value)

if __name__ == "__main__":
    import sys
    cat()
