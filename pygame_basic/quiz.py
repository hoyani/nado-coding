import pygame
import random

pygame.init()


###################### < 퀴즈 : 똥 피하기 게임 > ###########################

#========== 1 화면

# 화면 크기 설정

screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Hoyeon Game")



# FPS
clock = pygame.time.Clock()



##################################  1> 사용자 게임 초기화 : 배경화면, 게임이미지, 좌표, 좌표, 속도, 폰트등)

# 배경이미지 불러오기
background = pygame.image.load("/Users/mzc01-sarahy/Documents/Study/Dev/projects/nado-coding/pygame_basic/background1.jpeg")


#========== 2 캐릭터

# ㅡㅡㅡㅡ 스프라이트 캐릭터 불러오기
character =  pygame.image.load("/Users/mzc01-sarahy/Documents/Study/Dev/projects/nado-coding/pygame_basic/dog.jpeg")
character_size = character.get_rect().size # 캐릭터 이미지의 크기 
character_width = character_size[0] # 캐릭터 가로크기 
character_height = character_size[1] # 캐릭터 세로크기

# 시작 위치 (초기)
character_x_pos = screen_width/2 - character_width/2 # 처음엔 가운데 위치 
character_y_pos = screen_height - character_height # 첨엔 젤 아래 위치

# 이동할 좌표 
to_x = 0 

# 이동 '속도'
character_speed = 10

 

# ㅡㅡㅡㅡ 똥 캐릭터

ddong =  pygame.image.load("/Users/mzc01-sarahy/Documents/Study/Dev/projects/nado-coding/pygame_basic/ddong.png")
ddong_size = ddong.get_rect().size # 적군 이미지의 크기 
ddong_width = ddong_size[0] # 적군 가로크기 
ddong_height = ddong_size[1] # 적군 세로크기

# 똥 처음 위치 
ddong_x_pos = random.randint(0, screen_height - ddong_width)
ddong_y_pos = 0

# 이동 '속도'
ddong_speed = 10



#========== 3 텍스트

# # 폰트정의
# game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)



# # 총 시간
# total_time = 10

# # 시작시간 계산
# start_ticks = pygame.time.get_ticks() #시작 tick 을 받아옴




##################################  2> 이벤트 처리 (키보드, 마우스등)


# 이벤트 루프 
running = True # 게임이 진행중인가? 
while running :
    
    
    dt = clock.tick(60) # 게임화면의 초당 프레임 수(fps) 설정 / 값 높을수록 = '부드러움'
    
    # ======== 키 이동 (위치 정의)
    
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 - 파이썬 게임 실행위해 필수 
        
        if event.type == pygame.QUIT: # x버튼 창 끄는 이벤트 발생 시 
            running = False # 게임 진행중이 아님 
            
        if event.type == pygame.KEYDOWN: # 키 눌럿을때
            if event.key == pygame.K_LEFT : #왼쪽 키를
                to_x -= character_speed
            if event.key == pygame.K_RIGHT : #오른쪽 키를
                to_x += character_speed
                
        if event.type == pygame.KEYUP : # 키 뗏을때 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
                
    # 게임 캐릭터, 똥 위치 최종 정의     
    character_x_pos += to_x * dt
    ddong_y_pos += ddong_speed
    
    
    #======= 화면 밖에 안 벗어나게 
            
    # 게임 캐릭터는 - 가로 경계값 처리 
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width : 
        character_x_pos = screen_width - character_width
        
        
    # 렌덤으로 떨어지는 똥 반복 if문
    if ddong_y_pos > screen_height : 
        ddong_y_pos = 0 # 다시 위에서부터 올려놓고 
        ddong_x_pos = random.randint(0, screen_height - ddong_width) # 가로는 랜덤 왓다갓다 
            
            

    #========== 충돌 처리 
    
    # 충돌 처리를 위한 rect 정보 업데이트
    
    character_rect = character.get_rect() #rectangle정보 = x좌표, y좌표 / width, height
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    ddong_rect = ddong.get_rect() #rectangle정보 = x좌표, y좌표 / width, height
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos
    
     # 충돌 체크
    if character_rect.colliderect(ddong_rect): #충돌 했니
        print('충돌했다.')
        running = False
    
    #===== 실제 그려주기 
            
    screen.blit(background, (0,0)) # 배경 그리기 in 위치 
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 in 위치 
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos)) # 똥 그리기 in 위치 
    
    
    # ㅡㅡㅡㅡㅡㅡ 업데이트 필수 !!! 
    pygame.display.update() # 화면 수시로 다시 그려줘야, 계속 호출
    
    
# pygame 종료
pygame.quit()