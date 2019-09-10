import sys
import re

reg_expression = r"human" #замена слова копутер на хумана
for line in sys.stdin:
    line = line.rstrip()
    # process line
    if "human" in line:
        x = re.sub(reg_expression,"computer", line)
        print(x)
    else:
        print(line)