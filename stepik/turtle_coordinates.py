n = int(input())
coord = (x, y)
d = {'север':0,'запад':0,'юг':0,'восток':0}
for i in range(n):
    key = input().split()
    if key[0] in d:
        d.update({key[0]: key[1]})

print(d)