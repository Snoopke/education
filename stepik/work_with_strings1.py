s = str(input().lower())
a = str(input().lower())
b = str(input().lower())

counter = 0
while a in s:
    s = s.replace(a, b)
    counter += 1
    if counter > 1000:
        print("Impossible")
        break
if counter <= 1000:
    print(counter)



