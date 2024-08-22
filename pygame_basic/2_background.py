import pygame


pygame.init() #초기화 - 반드시필요

# 화면 크기 설정

screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경이미지 불러오기
background = pygame.image.load("/Users/mzc01-sarahy/Documents/Study/Dev/projects/nado-coding/pygame_basic/background.png")

# 이벤트 루프 
running = True # 게임이 진행중인가?
while running :
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 - 파이썬 게임 실행위해 필수 
        if event.type == pygame.QUIT: # x버튼 창 끄는 이벤트 발생시 
            running = False # 게임 진행중이 아님 
            
            
    #screen.fill((0, 0, 255)) # 이미지 말고, 바로 색 채울수도 RGB 값
    screen.blit(background, (0,0)) # background 그리기 in 위치 
    
    pygame.display.update() # 화면 수시로 다시 그려줘야, 계속 호출 - 필수
        


# pygame 종료
pygame.quit()


