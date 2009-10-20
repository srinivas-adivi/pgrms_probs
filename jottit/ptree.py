
def make_dict(file):
    ppid_and_pid_cmd = {}
    lines = file.readlines()
    frist_ppid = lines[1].split()[1]
    for line in lines[1:]:
        pid, ppid, cmd = line.split()
        ppid_and_pid_cmd.setdefault(ppid, []).append((pid, cmd))

    return frist_ppid, ppid_and_pid_cmd

def trace_allprocess(ppid, dic, count=0):
    for (pid,cmd) in dic[ppid]:
        print '| '*count + '|-- '+ ' '.join((pid, cmd))
        if dic.has_key(pid):
            count += 1
            trace_allprocess(pid, dic, count)
            count -= 1

def execute_command(command):
    return os.popen(command)

if __name__ == "__main__":
    import os
    import sys
    
    output_file = execute_command('ps -axo pid,ppid,comm')
    first_ppid, ppid_and_pid_cmd = make_dict(output_file)
    trace_allprocess(first_ppid, ppid_and_pid_cmd)
