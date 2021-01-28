import requests

url = 'http://127.0.0.1:8000/client/3/books'
headers = {'Authorization': 'Token 8f00183f0d702f969d3388a9f8cf7f1297103563'}
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.json())