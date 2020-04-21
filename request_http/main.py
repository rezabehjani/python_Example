import requests

for i in range(0, 200):
    response = requests.get('http://api.iotkaran.ir/hello')
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')

    print(response)