s = str(input().lower())
t = str(input().lower())
counter = 0
index = 0

for i in range(len(s)):
    if t in s:
        if s.startswith(t, index):
            counter += 1
            index += 1
        else:
            index += 1
    else:
        break

print(counter)