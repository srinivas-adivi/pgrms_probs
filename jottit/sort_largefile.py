
def sortlargefile(filename):
    """sort lines in given file which is large enough that won't fit in the     memory of a process."""

    sortfile = filename + '.sort'
    fi = open(filename, 'r')
    fo = open(sortfile, 'w')
    
    # read 1MB at a time
    chunk_size = 1024 * 1024
    chunk = []    
    while True:
        chunk.extend(fi.readlines(chunk_size))
        if not chunk: break

    chunk.sort()
    fo.write(''.join(chunk))

    fi.close()
    fo.close()

if __name__ == "__main__":
    import os
    import sys

    try:
        sortlargefile(sys.argv[1])
        
    except IndexError, (strerror):
        error = "file name u have to give"
        print "IndexError:" + "%s" %error
        sys.exit(1)
    
    except IOError, (errno, strerror):
        print "IOError: " + "%s" %strerror
        sys.exit(errno)

