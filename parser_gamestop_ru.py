import requests
from bs4 import BeautifulSoup as BS

page = 1

r = requests.get("https://stopgame.ru/review/new/izumitelno/p1")
html = BS(r.content, 'html.parser')

for el in html.select(".items > .article-summary"):
    title = el.select('.caption > a')
    print( title[0].text)
