import requests
import json

url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

#output to console
print(data)

for car in data["cars"]:
   print(car)

# save this to file
filename = 'cars.json'
if filename:
   # Writing JSON data
   with open(filename, 'w') as f:
      json.dump(data, f, indent=4)