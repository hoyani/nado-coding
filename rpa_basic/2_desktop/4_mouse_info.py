import pyautogui


pyautogui.FAILSAFE = False # 그 ESC 기능 끄려면 / 근데 비추 
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용

# ㅡㅡㅡㅡ 마우스 정보 확인하기 

pyautogui.mouseInfo()
# 이렇게 하고 실행하면 = 팝업창 뜬다 !!

'''
마우스 위치 커서 올리고 - f1 누르면 = 마우스 위치 복사 
붙여넣기 결과 -> 마우스 위치 좌표값 (610,190)

맥에서는 = 마우스 위치의 색깔정보는 지원 x 
'''

# ㅡㅡㅡㅡㅡ 마우스 ver. ESC 기능 - ctrl c 취소 하려면 


'''
자동화 하다보면 시간 많이 걸리는데
중간에 실패 ? = 작업 중지해야하는데 
파이썬은 esc 가 안된다 
ㄴ

그럴땐
실행중에 마우스를 = 화면의 네 모서리 귀퉁이에 위치하면 된다!!! 
'''

# 1 일단 테스트용 - 1 먼저 움직이는 sample 실행 시키고 

for i in range(10):
    pyautogui.move(100,100) #상대좌표라 추가됌 
    pyautogui.sleep(1) 
    
# 2 마우스를 귀퉁이에 옮겨봐라 ! 