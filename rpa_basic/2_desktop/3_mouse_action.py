import pyautogui




# ================= 마우스 액션

# ㅡㅡㅡㅡ 목적지 위치 좌표 먼저 알아내기 

# pyautogui.sleep(3) # 3초 대기 -> file 목적지 위치로 마우스 이동할 시간 벌기 ㅋㅋ 
# print(pyautogui.position())


# ㅡㅡㅡㅡ 1 클릭
# pyautogui.click(124, 21, duration=1) # 1초동안 이 좌표로 이동 후/ (124, 21) 좌표를 마우스 클릭 

# ㅡ 클릭 = 다음 Down + Up 합친거와 동일 (이는 반 반 위치다르게 사용할때 = 드래그앤드랍 시)
# pyautogui.mouseDown()
# pyautogui.mouseUp()


# ㅡㅡㅡㅡ 2 더블클릭 
# pyautogui.doubleClick()
# pyautogui.click(clicks=2)
# pyautogui.click(clicks=500)


# ㅡ 실습1 - 그림판에서 : 사선 일직선 그리기 

# pyautogui.sleep(3) # 3초 대기 ->  목적지 위치로 마우스 이동할 시간 벌기 ㅋㅋ 

# pyautogui.moveTo(200,200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300,300)
# pyautogui.mouseUp()


# ㅡ 실습2 - 그림판에서 : 사선 일직선 그리기 

# pyautogui.sleep(3) # 3초 대기 ->  목적지 위치로 마우스 이동할 시간 벌기 ㅋㅋ 

# pyautogui.moveTo(200,200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300,300)
# pyautogui.mouseUp()


# ㅡㅡㅡㅡ 마우스 클릭 스팟

# pyautogui.rightClick() # 마우스 우클릭 
# pyautogui.middleClick() # 마우스 휠부분 - 위아래 스크롤 효과



# ㅡㅡㅡㅡ 창 하나를 클릭해서 옆으로 이동할때 



# ㅡ 현재위치 먼저 


pyautogui.sleep(3) # 3초 대기 ->  목적지 위치로 마우스 이동할 시간 벌기 ㅋㅋ 
# print(pyautogui.position())
pyautogui.moveTo(578, 286)  

# ㅡ 1 상대이동 
# pyautogui.drag(100,0, duration=0.25) # 현재위치 기준 + x 100, y 0 만큼 드래그 / 너무 빠른동작으로 drag 수행이 안될때는 드래그 duration 설정
# ㅡ 2 절대 이동 
# pyautogui.dragTo(700, 286, duration=0.25) # 걍 바로 x 800, y 320 좌표로 이동 ㅋㅋ

# ㅡㅡㅡㅡ 스크롤하기

pyautogui.scroll(300) # 위 방향으로 300만큼 스크롤
# pyautogui.scroll(-300) # 아래 방향으로 300만큼 스크롤
