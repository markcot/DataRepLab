import requests

url = 'https://github.com/markcot/jupyter-example/blob/master/README.md'

response = requests.get(url)

print(response.text)
