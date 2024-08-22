import pyautogui


# ㅡㅡㅡㅡㅡㅡㅡ 마우스 이동 , menu 이미지 클릭 

# ㅡ 1 해당 이미지 잇는곳 위치 정보

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)

# ㅡ 2 해당 이미지 위치정보 = 마우스 클릭해 
# pyautogui.click(file_menu)


# ㅡㅡㅡㅡㅡㅡㅡ 마우스 이동, Trash 이미지 

# ㅡ 1 해당 이미지 잇는곳 위치 정보

trash = pyautogui.locateOnScreen("trash.png")
print(trash)

# ㅡ 2 해당 이미지로 마우스 이동
pyautogui.moveTo(trash) # 절대좌표로 / 위부터 한줄씩 이동하며 스캔 찾아서 -> 마우스 이동 

# ㅡㅡㅡㅡㅡㅡㅡㅡ 만약 이미지가 화면상에 없다면 


# ㅡ 1 해당 이미지 잇는곳 위치 정보

screen = pyautogui.locateAllOnScreen("screenshot.png") #지금 화면에 없는 이미지
print(screen) # 에러 발생 - None 결과 
'''
이미지 기반이라
해상도가 조금만 바뀌어도 실패확률 높다

자동화 스크립트 작성시 = 작업환경과 똑같이 만들어줘야 

'''

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡ 아이콘 똑같은게 2개 이상잇을 때?

'''
구글 검색 - ws3schools checkbox
ㄴ
첫 사이트 - 첫 exmaple - try yourself 
ㄴ
checkbox 이미지 마련하고..

'''

# 이미지가 여러개인 상태에서 ..

# ㅡㅡㅡ 1 여러개 위치 다 탐색 ver.


'''
locateAllOnScreen ?
: 화면내 해당 이미지 여러개 - 모든 정보 다가져

'''

for i in pyautogui.locateAllOnScreen("checkbox.png"):
    print(i)
    pyautogui.click(i, duration= 0.25) # 해당 위치마다 클릭하는거 ㅋㅋ
    
    
# ㅡㅡㅡ 2 한개 위치 탐색 ver.


checkbox = pyautogui.locateOnScreen("checkbox.png")
pyautogui.click(checkbox)
# 결과는 : 여러개중 = 제일 첫번째 이미지만 클릭하고 종료!! 


# ㅡㅡㅡㅡㅡㅡㅡ 마우스 이동, Trash 이미지 => 속도 개선 하기 !! 

# ㅡㅡㅡ 1. GrayScale : 여러색 이미지를 -> 흑백으로 전환후 비교
'''
정확도는 떨어질수잇음
'''

# 1 해당 이미지 잇는곳 위치 정보
trash = pyautogui.locateOnScreen("trash.png",grayscale=True)
print(trash)

# 2 해당 이미지로 마우스 이동
pyautogui.moveTo(trash) # 절대좌표로 / 위부터 한줄씩 이동하며 스캔 찾아서 -> 마우스 이동 
 

# ㅡㅡㅡ 2. 범위지정 가능 - 꼭 전체화면 대상 x 특정 범위에서만 o (범위를 좁혀주기)

# 0 해당 이미지 위치정보 부근의 범위정보 파악
pyautogui.mouseInfo()

'''
좌측 상단 1488,623 시작
우측 하단 1881,760 끝
ㄴ
width = 1881 - 1488 = 393
height = 760 - 623 = 137
'''


# 1 해당 이미지 잇는곳 위치 정보 - 지정 범위내에서 찾아라 
trash = pyautogui.locateOnScreen("trash.png",region=(1488, 623, 393, 137)) # 시작x, 시작y, width, height 값 
print(trash)

# 2 해당 이미지로 마우스 이동
pyautogui.moveTo(trash) # 절대좌표로 / 위부터 한줄씩 이동하며 스캔 찾아서 -> 마우스 이동 
 
 
# ㅡㅡㅡ 3 정확도 조정 - 몇 % 이상 일치하면 해당이미지라고 인식하게 

run1 = pyautogui.locateOnScreen("run1.png", confidence=0.9) #90% 이상 일치하면 = 해당이미지로 인식 
pyautogui.moveTo(run1)

'''
터미널에 설치
pip3 install opencv-python

'''

# ㅡㅡㅡㅡㅡㅡㅡ 자동화 대상이 바로 보여지지 않는 경우 


# ㅡㅡ <게속 기다리기>

# 방법1 

cake = pyautogui.locateOnScreen("cake.png")

if cake :
    pyautogui.click(cake)
else:
    print("발견 실패")
    
    
# 방법 2 
while cake is None: # 발견될떄까지 게속 돌려 
    cake = pyautogui.locateOnScreen("file_menu.png")   
    print("발견 실패")
    
# 뒤늦게 cake 이미지 열면 
pyautogui.click(cake)
    
    
    
# ㅡㅡ <일정시간동안 기다리기> Timeout 

# 방법 1

import time
import sys

timeout = 10 # 10초 대기

start = time.time() # 시작시간 설정
cake = None
while cake is None:
    cake = pyautogui.locateOnScreen("cake.png")
    end = time.time()
    
    if end - start > timeout: # 지정 10초 초과하면
        print("시간종료")
        sys.exit()
        

pyautogui.click(cake) # 기한 내에 성공햇으면 클릭하고 끝 



# 방법 2


def find_target(img_file, timeout=30):
    start = time.time()
    target = None # 없는걸로 시작햇으나 
    while target is None:
        target = pyautogui.locateOnScreen(img_file) # 찾앗을지도 
        end = time.time()
        if end - start > timeout:
            break
    return target # 1 찾앗을수도 / 없을수도 

def my_click(img_file, timeout=30):
    
    target = find_target(img_file, timeout) # 2 위에 작성한 타깃 함수 !! 
    
    if target: # 타깃 찾은경우 
        pyautogui.click(target)
        
    else : # 타깃 None 경우 
        print(f"[Timeout {timeout}s] Target not found ({img_file}).... Terminate program !!! ")
        sys.exit()

my_click("cake.png", 10) # 10초동안 발견 못하면 - 끝내고 / 발견하면 - 동작하고 넘어가 