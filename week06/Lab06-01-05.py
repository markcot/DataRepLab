import requests, json
from xlwt import *

#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)
data = response.json()
#print(data)

# Get the file name for the new file to write
filename = 'githubusers.json'
with open(filename, 'w') as f:
   json.dump(data, f, indent=4)


#write to excel file
w = Workbook()
ws = w.add_sheet('githubusers')
row = 0
ws.write(row, 0, "login")
ws.write(row, 1, "id")
ws.write(row, 2, "url")
ws.write(row, 3, "site_admin")
row += 1
for user in data:
   ws.write(row, 0, user["login"])
   ws.write(row, 1, user["id"])
   ws.write(row, 2, user["url"])
   ws.write(row, 3, user["site_admin"])
   row += 1
w.save('githubusers.xls')
