import requests
import json

f = open ("../week02/carviewer2.html", "r")
html = f.read()
#print(html)

apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c-4'
url = 'https://api.html2pdf.app/v1/generate'

data = {'html':html, 'apiKey': apiKey}
response = requests.post(url, json=data)
print(response.status_code)

# Write binary data to a file
newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
newFile.write(response.content)