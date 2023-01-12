# import libraries
import requests
from bs4 import BeautifulSoup as bs

# load the web page content
url = "https://keithgalli.github.io/web-scraping/example.html"

page = requests.get(url=url)

# conver the url content to a beautiful soup object
soup = bs(page.content)

# print the web content
print(soup.prettify())
