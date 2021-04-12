import urllib.request
from bs4 import BeautifulSoup

# 접근할 페이지 번호
pageNum = 1

# 저장할 이미지 경로 및 이름 (data폴더에 face0.jpg 형식으로 저장)
imageNum = 0
imageStr = "이미지/data"
hds = {"User-Agent": "Mozilla/5.0"}
url = "https://www.google.co.kr/search?q=carrot&tbm=isch&ved=2ahUKEwi62-SVufjvAhW0yosBHZVhD08Q2-cCegQIABAA&oq=carrot&gs_lcp=CgNpbWcQAzIFCAAQsQMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6CAgAELEDEIMBOgcIIxDqAhAnOgQIIxAnOgQIABADUMoVWPolYNsmaANwAHgAgAGLAYgB_gaSAQMwLjiYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=EBp0YLqTKrSVr7wPlcO9-AQ&bih=937&biw=1920&safe=off"

baseUrl = urllib.request.Request(url, headers=hds)
source = urllib.request.urlopen(baseUrl)

soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("a", class_="F9PbJd IJRrpb xKddTc")
print(soup)
# 이미지 경로를 받아 로컬에 저장한다.
for i in soup:
    imageNum += 1
    imgURL = i.find("img")["src"]
    urllib.request.urlretrieve(imgURL, imageStr + str(imageNum) + ".jpg")
    print(imgURL)
    print(imageNum)
