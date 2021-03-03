import pyautogui
while True:
    a = pyautogui.locateOnScreen("a.PNG")
    try:
        center = pyautogui.center(a)
        print(center)
    except:
        print("NONE")
