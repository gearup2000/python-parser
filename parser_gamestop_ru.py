import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://stopgame.ru/review/new/izumitelno/p1") # fetch the content of the page
html = BS(r.content, 'html.parser') # result of previous stroke goes to the BeautifulSoup

for el in html.select(".items > .article-summary"): # select the tags items and article-summary
    title = el.select('.caption > a')
    print( title[0].text)
