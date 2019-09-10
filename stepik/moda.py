import re
import sys

with open("dataset_3363_3.txt", 'r') as question:
    read = question.read().lower().split()
    regex = r'\w*'
    for i in read:
        x = read.count(i)
        print(i + " " + str(x))