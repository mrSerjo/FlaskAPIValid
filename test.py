import requests


BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + '/check_inn/1234567890')
print(response.json())
response = requests.get(BASE + '/check_inn/1234567891231230')
print(response.json())