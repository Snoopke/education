import csv
import collections

ans = []
with open("dataset_3380_5.txt") as classmates:
    reader = csv.reader(classmates, delimiter='\t')
    for row in reader:
        print(row)

