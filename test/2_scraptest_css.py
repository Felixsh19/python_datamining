from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html)
namelist = bs0bj.findAll("span",{"class":"red"})
for name in namelist:
    print(name.get_text())
