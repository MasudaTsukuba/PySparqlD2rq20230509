import requests


response = requests.get('http://localhost:5001/?str2uri=John')

if response.status_code == 200:
    data = response.json()
    print(data['uri'])
else:
    print('Error: ', response.status_code)
