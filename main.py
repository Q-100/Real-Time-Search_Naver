import urllib.request
from bs4 import BeautifulSoup
from datetime import date
from collections import Counter
import re

hds = {"User-Agent": "Mozilla/5.0"}
url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&listType=title&date=20210309"
url2 = "https://news.naver.com/main/list.nhn?mode=LPOD&sid2=140&sid1=001&mid=sec&oid=001&isYeonhapFlash=Y&date=20210309"
urls = ["https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&listType=title&date=20210309",
        "https://news.naver.com/main/list.nhn?mode=LPOD&sid2=140&sid1=001&mid=sec&oid=001&isYeonhapFlash=Y&date=20210309",
        ]
banned = ['',
          "Virus", "Outbreak", "Chicago", "Schools", "Baseball", "utbreak", "emen", "ong", "FRANCE",
          'INTERNATIONAL', 'DAY', 'POLAND', 'ABORTION', 'LAW', 'PROTEST', 'WOMENS', 'ITALY', 'EQUATORIAL', 'GUINEA',
          'EXPLOSION', 'MACRON', 'ECONOMY', 'EU', 'START', 'UP', 'epaselect', 'BELGIUM', 'PARLIAMENT',
          ]

baseUrl = urllib.request.Request(url2, headers=hds)
# date = "".join(date.isoformat(date.today()).split("-"))
# url = baseUrl + urllib.parse.quote_plus(date)
html = urllib.request.urlopen(baseUrl)

soup = BeautifulSoup(html, "html.parser")
search_list = []
for i in soup.find_all(class_="nclicks(fls.list)"):
    tmp = [word for word in re.sub('[^a-zA-Z0-9가-힣]', " ", i.text).split(" ") if word not in banned]
    search_list += tmp
print(Counter(search_list).most_common(10))
