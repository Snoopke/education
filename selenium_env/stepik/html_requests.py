import requests
import re
import sys

reg_expression = r"[\"|'].*[\"|']" #замена a* yf
html_list = requests.get('http://pastebin.com/raw/7543p0ns')
print(html_list.content)
