import sys
import re

reg_expression = r"\b\w\b" #ищет слово, в котором две повторяющиеся части
for line in sys.stdin:
    line = line.rstrip()
    # process line
    if re.search(reg_expression, line):
        print(line)