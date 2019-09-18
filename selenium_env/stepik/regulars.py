import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    # process line
    jojo = re.findall("cat", line)
    if len(jojo) >= 2:
        print(line)
    else:
        continue
