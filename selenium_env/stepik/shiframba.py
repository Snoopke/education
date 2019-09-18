sample = input()
shifr = input()
encryption = input()
decryption = input()

answer1 = ''
answer2 = ''
for i in encryption:
        index = sample.find(i)
        x = shifr[index]
        answer1 += x
print(answer1)

for i in decryption:
    index = shifr.find(i)
    x = sample[index]
    answer2 += x
print(answer2)