from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pagees/page2.html")
bsObj = BeautifulSoup(html)
tages = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for tag in tags:
    print(tag)

