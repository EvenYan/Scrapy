from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = bsObj.body.h1.read()
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
