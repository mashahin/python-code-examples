# import libraries
import requests
from bs4 import BeautifulSoup as bs

# load the web page content
url1 = "https://keithgalli.github.io/web-scraping/example.html"
url2 = "https://www.pararius.com/apartments/amsterdam?ac=1"
url3 = "https://www.rentcanada.com/winnipeg-mb"

page = requests.get(url=url3)
print("\nResponse: \n", page)

# conver the url content to a beautiful soup object
soup = bs(page.content, 'html.parser')
print("\nSoup object: \n", soup.prettify())

lists = soup.find_all('div', class_="listing-container")
print(lists)

""" for list in lists:
    title = list.find('a', class_="listing-search-item__link--title")
    location = list.find('div', class_="listing-search-item__sub-title")
    price = list.find('div', class_="listing-search-item__price")
    area = list.find('li', class_="illustrated-features__item--surface-area")
    info = [title, location, price, area]
    print(title) """

# print the web content
# print(soup.prettify())
