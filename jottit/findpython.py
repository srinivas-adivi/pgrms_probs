
def findpython(path):
    try:
        for file in os.listdir(path):
            actual_path = path.strip('/') +'/'
            if os.path.isdir(actual_path+file):
                findpython(actual_path+file)
            elif 'py' in file.split('.', 1):
                sys.stdout.write(actual_path+file+'\n')

    except OSError, (error, strerror):
        print "path is not a PATH for directory"

if __name__ == "__main__":
    import os
    import sys
    
    try:
        path = sys.argv[1]
        if os.path.exists(path):
            findpython(path)
        else:
            print "given path does not exist"

    except IndexError, (strerror):
        print "IndexError :" + "%s" %strerror
        print "USAGE: 'python findpython.py directory_path'"
    
