import pyautogui

# ㅡㅡㅡㅡ 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장


# ㅡㅡㅡ 마우스 위치/색 정보 


# pyautogui.mouseInfo()
# # 132,64 34,167,242 #22A7F2

pixel = pyautogui.pixel(132,64)
print(pixel) # => 이 좌표의 RGB 색상값 출력 34,167,242


# ㅡㅡㅡ 현재 마우스 정보랑 = 값 맞는지 판별하기 

print(pyautogui.pixelMatchesColor(132,64, (34,167,242))) # 좌표 = 해당 좌표 색상값 일치하는지 
print(pyautogui.pixelMatchesColor(132,64, pixel)) # 좌표 = 해당 좌표 색상값 일치하는지 



''' 
활용) 

네이버 홈페 로그인 색 저장 후, 
ㄴ 초록이면 작업
ㄴ 빨강이면 에러 출력 등

'''