import pyautogui

# ㅡㅡㅡㅡ 절대 좌표로 마우스 이동
#pyautogui.moveTo(200,100) # 지정한 위치 (가로x, 세로y)로 마우스 이동 
#pyautogui.moveTo(100,200, duration=3) # 3 초 동안 100, 200 위치로 이동 

# pyautogui.moveTo(100,100, duration=0.25)
# pyautogui.moveTo(200,200, duration=0.25)
# pyautogui.moveTo(300,300, duration=0.25)


# ㅡㅡㅡㅡ 상대 좌표로 이동

pyautogui.moveTo(100,100, duration=0.25)
print(pyautogui.position()) #Point(x,y)

pyautogui.move(100,100, duration=0.25) # 100, 100 기준으로 +100, +100 -> 200, 200
print(pyautogui.position()) #Point(x,y)

pyautogui.move(100,100, duration=0.25) # 200, 200 기준으로 -> 300, 300
print(pyautogui.position()) #Point(x,y)


p = pyautogui.position() #Point(x,y)
print(p[0], p[1]) # x,y
print(p.x, p.y) # x,y 