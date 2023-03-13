import re

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    return "" if result is None else result[1]

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
log2 = "99 elephants in a [cage]"
print(extract_pid(log))
print(extract_pid(log2))