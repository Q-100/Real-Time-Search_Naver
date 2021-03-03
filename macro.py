import pyautogui as pag
import time
import winsound as sd
import random
from datetime import datetime

# (269 452) = 장바구니 조회
# (244 415) = 장바구니 조회
# (346 327) = 네트워크 신청
# (347 351) = 웹프로그래밍 신청
while True:
    # x,y = pag.position()
    # a = "X: " + str(x) + " Y: " + str(y)
    # print(a)
    pag.click(269, 452)
    network = pag.locateCenterOnScreen("network.PNG")
    web = pag.locateCenterOnScreen("web.PNG")
    test = pag.locateCenterOnScreen("7.PNG")
    if network is not None or web is not None:
        print(datetime.now(), "찾았어요!!!!!!!!!!!!!!!찾았어요!!!!!!!!!!!!!!!찾았어요!!!!!!!!!!!!!!!찾았어요!!!!!!!!!!!!!!!찾았어요!!!!!!!!!!!!!!!")
        while True:
            sd.Beep(2000, 1000)
            time.sleep(2)
    print(datetime.now(),"못찾음")
    sec = random.randint(60, 100)
    time.sleep(sec)
