import requests, json

url = "https://api.github.com/users?since=100"

response = requests.get(url)
data = response.json()
print(data)