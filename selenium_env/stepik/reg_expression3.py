import sys
import re

reg_expression = r"z\S{3}z" #поиск строки, в которой между двумя z стоит 3 любых символа
for line in sys.stdin:
    line = line.rstrip()
    # process line
    if re.search(reg_expression, line):
        print(line)