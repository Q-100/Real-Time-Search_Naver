import urllib.request
from bs4 import BeautifulSoup
from datetime import date
from collections import Counter

hds = {"User-Agent": "Mozilla/5.0"}
url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&listType=title&date=20210302"

baseUrl = urllib.request.Request(url,headers=hds)
# date = "".join(date.isoformat(date.today()).split("-"))
# url = baseUrl + urllib.parse.quote_plus(date)
html = urllib.request.urlopen(baseUrl)

soup = BeautifulSoup(html, "html.parser")
tmp = []
for i in soup.find_all(class_="nclicks(fls.list)"):
    tmp += i.text.split(" ")

tmp1 = Counter(tmp).most_common(5)
print(tmp1)