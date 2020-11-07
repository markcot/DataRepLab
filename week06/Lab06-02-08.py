import requests
import json

# remove the minus sign
apiKey = '71b89bdc0378f2330931041ef2f2fc573043336-5'
url = 'https://api.github.com/user/repos'


# Test content of Hello file
tempfilename = "repo2.json"
response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()
print("Github repo name:", repoJSON[1]["full_name"])

# Update description of Hello repository
repoJSON[1]["description"] = "MC test"
# Test output of changes to file
file = open(tempfilename, 'w')
json.dump(repoJSON[1], file, indent=4)

# Upload changed data to Github
# data = {'json': repoJSON[1]["description": "MC test"], 'apiKey': apiKey}
# response = requests.put(url, json=data)
# print(response.status_code)

# Test of post to git url
git_url = 'git://github.com/datarepresentationstudent/Hello.git'
html = {"test":1234}
data = {'html': html, 'apiKey': apiKey}
response = requests.post(url, json=data)
print(response.status_code)

