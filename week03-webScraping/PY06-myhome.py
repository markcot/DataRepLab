import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")

soup = BeautifulSoup(page.content, 'html.parser')

listings = soup.find("div", class_="PropertyListingCard")

price = listings.find(class_="PropertyListingCard__Price").text
print(price)

address = listings.find(class_="PropertyListingCard__Address").text
print(address)
