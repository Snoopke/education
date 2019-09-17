import sys
import re

reg_expression = r"(\b\w)(\w)" #замена a* yf
for line in sys.stdin:
    line = line.rstrip()
    # process line
    print(re.sub(reg_expression,r"\2\1", line, flags=re.IGNORECASE))
