import requests

params = {'id': '4'}
#response = requests.get("https://jsonplaceholder.typicode.com/users/1")
response = requests.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(f"Status code: {response.status_code}")
#print(f"Headers: {response.headers}")
print(f"Json: {response.json()}")