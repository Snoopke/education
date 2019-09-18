import sys
import re

reg_expression = r"\ba+\b" #замена a* yf
for line in sys.stdin:
    line = line.rstrip()
    # process line
    print(re.sub(reg_expression,"argh", line, count=1, flags=re.IGNORECASE))
