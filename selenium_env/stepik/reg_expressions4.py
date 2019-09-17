import sys
import re

reg_expression = r"\\" #строка содержащая бекслэш
for line in sys.stdin:
    line = line.rstrip()
    # process line
    if re.search(reg_expression, line):
        print(line)