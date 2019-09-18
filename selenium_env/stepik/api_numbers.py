import requests
import json
import sys


with open('dataset_24476_3.txt', "r") as file_inc:
    for line in file_inc:
        number = line.rstrip()
        default = 'default=Boring'
        type = '/math?'
        url = "http://numbersapi.com/" + str(number) + type + 'json'
        res = requests.get(url)
        x = res.json()
        with open("answer2.txt", "a") as ans:
            if x['found'] == True:
                ans.write('Interesting' + "\n")
            else:
                ans.write("Boring"+"\n")





