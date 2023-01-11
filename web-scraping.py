# import libraries
import requests
from bs4 import BeautifulSoup as bs

# load the web page content
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

# conver the url content to a beautiful soup object
soup = bs(r.content)

# print the web content
print(soup.prettify())

