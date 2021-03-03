import urllib.request
from bs4 import BeautifulSoup
from datetime import date
from collections import Counter
import re

hds = {"User-Agent": "Mozilla/5.0"}
url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&listType=title&date=20210302"

baseUrl = urllib.request.Request(url, headers=hds)
# date = "".join(date.isoformat(date.today()).split("-"))
# url = baseUrl + urllib.parse.quote_plus(date)
html = urllib.request.urlopen(baseUrl)

soup = BeautifulSoup(html, "html.parser")
search_list = []
for i in soup.find_all(class_="nclicks(fls.list)"):
    tmp = i.text.split(" ")
    for j in tmp:
        tmp1 = re.sub('[^a-z0-9가-힣]', '', j)
        if tmp1 != ("" or "Virus" or "Outbreak" or "Chicago" or "Schools" or "Baseball"):
            search_list.append(tmp1)

print(Counter(search_list).most_common(10))
