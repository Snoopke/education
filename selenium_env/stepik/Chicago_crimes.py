import csv
import collections

ans = []
with open("Crimes.csv") as crimes:
    reader = csv.reader(crimes)
    for row in reader:
        print(row)
        ans.append(row[5])

print(collections.Counter(ans).most_common())