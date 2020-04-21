import requests
import logging
from pprint import pprint
logging.basicConfig(level=logging.DEBUG)

url = 'https://www.iotype.com/api/recognize/file'

myobj = {'token':"RWUDHoP6F1CNM7pC"}
files = {'audio':open('salam.mp3', 'rb')}
headers = {'Content-Type':'multipart/form-data'}
payload = {'token':"RWUDHoP6F1CNM7pC", 'audio':open('salam.mp3', 'rb')}
r = requests.post(url, data=payload, headers=headers, files=files)
print(r.headers)
print(r.text)

x = requests.post(url, params=myobj, files=files)
print(x.text)

payloads = {'token':'RWUDHoP6F1CNM7pC', 'audio':open('salam.mp3', 'rb')}
z = requests.post(url, files=payloads, headers=headers)
print(z.text)
