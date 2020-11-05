import requests

# remove the '-'
# url = 'https://api.github.com/datarepresentationstudent/Hello'
# apiKey = 'b4ddb9e5603dallcd857b83bad6ea6eb1819b92-d'
url = 'https://api.github.com/markcot/aPrivateOne'
apiKey = '0c514b26b9551d8265b44c89b583b45a41e3009-e'


# Create text file for upload to Github
filename = "Lab06-02-08-text.txt"
filetext = "hello text content"

# Create/override text file and write text content to the file
with open(filename, 'w') as f:
   f.write(filetext)

# Read the text content of the file
with open(filename, 'r') as f:
   print(f.read())

response = requests.post(url, data='.\Lab06-02-08-text.txt', auth=('token',apiKey))

print(response.text)
