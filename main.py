import urllib.request
from bs4 import BeautifulSoup
from datetime import date
from collections import Counter
import re

hds = {"User-Agent": "Mozilla/5.0"}
urls = ["https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&listType=title&date=20210321",  # 네이버 속보
        "https://news.naver.com/main/list.nhn?mode=LPOD&sid2=140&sid1=001&mid=sec&oid=001&isYeonhapFlash=Y&date=20210321",
        # 연합뉴스 속보
        "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105",  # IT/과학
        "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=100",  # 정치속보
        "https://news.naver.com/main/ranking/popularMemo.nhn"  # 랭킹뉴스 댓글 많은 순
        ]
banned = ['',
          "Virus", "Outbreak", "Chicago", "Schools", "Baseball", "utbreak", "emen", "ong", "FRANCE",
          'INTERNATIONAL', 'DAY', 'POLAND', 'ABORTION', 'LAW', 'PROTEST', 'WOMENS', 'ITALY', 'EQUATORIAL', 'GUINEA',
          'EXPLOSION', 'MACRON', 'ECONOMY', 'EU', 'START', 'UP', 'epaselect', 'BELGIUM', 'PARLIAMENT', 'Peru',
          'Belgium',
          'WOMEN',"GERMANY", "REGIONAL","ELECTIONS"
          ]
# https://news.nate.com/rank/updown 네이트 업다운
# https://news.zum.com/front?c=06 줌 뉴스
# date = "".join(date.isoformat(date.today()).split("-"))
# url = baseUrl + urllib.parse.quote_plus(date)
search_list = []
for link in urls:
    baseUrl = urllib.request.Request(link, headers=hds)
    html = urllib.request.urlopen(baseUrl)
    soup = BeautifulSoup(html, "html.parser")
    if link == "https://news.naver.com/main/ranking/popularMemo.nhn":
        for i in soup.find_all(class_="list_title nclicks('RBP.cmtnws')"):
            tmp = [word for word in re.sub('[^a-zA-Z0-9가-힣]', " ", i.text).split(" ") if word not in banned]
            search_list += tmp
    else:
        for i in soup.find_all(class_="nclicks(fls.list)"):
            tmp = [word for word in re.sub('[^a-zA-Z0-9가-힣]', " ", i.text).split(" ") if word not in banned]
            search_list += tmp

for i in range(10):
    print(i+1, "위 :", Counter(search_list).most_common(20)[i][0])


