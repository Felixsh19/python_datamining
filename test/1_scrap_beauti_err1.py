#网页可能不存在及服务器错误的情况
from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getTitle(url):  #捕捉异常
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    try:
        bs0bj = BeautifulSoup(html.read())
        title = bs0bj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("page failed")
else:
    print(title)