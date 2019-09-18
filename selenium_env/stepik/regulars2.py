import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    # process line
    if re.findall(r"\bcat\b", line):
        print(line)
