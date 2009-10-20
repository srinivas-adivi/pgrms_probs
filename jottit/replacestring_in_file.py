
def replace(filename, search_string, replacement):
    """Replaces all occurrences of search string with replacement in the 
        specified file."""
    try:
        tmpfile = filename + '.tmp'
        fi = open(filename, 'r')
        fo = open(tmpfile, 'w')
        

        # read 1MB at a time
        chunk_size = 1024 * 1024

        while True:
            chunk = fi.read(chunk_size)
            if not chunk:
                break
            chunk = chunk.replace(search_string, replacement)
            fo.write(chunk)

        fi.close()
        fo.close()

        # mv tmpfile filename
        os.rename(tmpfile, filename)
        return 0

    except IOError, (errno, strerror):
        print "IOError :" + filename + " :%s" %strerror
        return errno

failures = lambda x: x != 0

def main(search_string, replacement, filenames):
    results = [replace(f, search_string, replacement) for f in filenames]
    if filter(failures, results):
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    import os
    import sys
    
    try: 
        main(sys.argv[1], sys.argv[2], sys.argv[3:])
    

    except IndexError, (strerror):
        error = "USAGE : python replacestring_in_file.py search_string replacestring filename"
        print "IndexError :" + "%s" %strerror
        print "%s" %error
        sys.exit(1)

