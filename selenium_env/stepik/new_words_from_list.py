n = int(input())
words = []
new_words = []

for i in range(n):
    x = input().lower()
    words.append(x)

n2 = int(input())

for i in range(n2):
    stroke = input().lower().split()
    new_words += stroke

x = set(words)

y = set(new_words)
difer = []

for i in new_words:
    if i in words:
        continue
    elif i in difer:
        continue
    else:
        difer.append(i)

for i in difer:
    print(i)