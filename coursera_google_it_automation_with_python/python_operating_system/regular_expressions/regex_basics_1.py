log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# Goal: Extract process identifier

index = log.index("[")
print(log[index+1:index+6])

import re

regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])