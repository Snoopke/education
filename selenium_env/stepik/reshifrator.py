import re


with open('dataset_3363_2.txt', "r") as case:
    line = case.readline()

    regex = r".\d+"
    jojo = re.findall(regex, line)
    answer = ''
for i in jojo:
    answer += i[0] * int(i[1:])
with open("reshifrator_answer.txt", 'w') as ans:
    write = ans.writelines(answer)
    print(write)