import requests
import json


# remove the minus sign
apiKey = 'b4ddb9e5603dallcd857b83bad6ea6eb1819b92-d'
url = 'https://api.github.com/datarepresentationstudent/aPrivateOne'
filename = "repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
#print(response.json())

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)
