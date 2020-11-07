import requests

url = 'https://github.com/markcot/jupyter-example/blob/master/README.md'

response = requests.get(url)

print(response.status_code)
print(response.text[:1000])
