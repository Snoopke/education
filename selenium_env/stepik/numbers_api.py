import requests
import json

api_url = 'http://numbersapi.com/'
params = {
    "number": '42'
}
res = requests.get(api_url, params=params)
print(res.headers['Content-Type'])
print(res.json())



