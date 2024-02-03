from inputs import getIP
import requests

ip = getIP()

api = requests.get(f'http://ip-api.com/json/{ip}')

response = api.json()

for key, value in response.items():
    k = key.upper()
    print(f'{k}: {value}')