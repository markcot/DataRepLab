import requests
import json


# remove the minus sign
apiKey = '71b89bdc0378f2330931041ef2f2fc573043336-5'
url = 'https://api.github.com/user/repos'
filename = "repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print(response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)
