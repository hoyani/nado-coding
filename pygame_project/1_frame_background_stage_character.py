import pygame
import os


#################################################################### 무조건 필수부분


#초기화 - 반드시필요
pygame.init() 


#========== 1 화면

# 화면 크기 설정

screen_width = 640 # 가로크기
screen_height = 480 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang")


# FPS
clock = pygame.time.Clock()



##################################  1> 사용자 게임 초기화 : 배경화면, 게임이미지, 좌표, 좌표, 속도, 폰트등)



# 상대경로 설정 
current_path = os.path.dirname(__file__) # 현재 파일 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환


#-------- 배경 

# 배경 불러오기 (상대경로)
background = pygame.image.load(os.path.join(image_path, "background2.png"))
# 배경 불러오기 (절대경로)
# background = pygame.image.load("/Users/mzc01-sarahy/Documents/Study/Dev/projects/nado-coding/pygame_basic/background.png")


#-------- 스테이지 

# 스테이지 불러오기 (상대경로)
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터 두기위해 사용 
 

#-------- 캐릭터 

# 캐릭터 불러오기 (상대경로)
character = pygame.image.load(os.path.join(image_path, "character2.png"))
character_size = character.get_rect().size
character_width = character_size[0] # 스테이지의 높이 위에 캐릭터 두기위해 사용 
character_height = character_size[1] # 스테이지의 높이 위에 캐릭터 두기위해 사용 

character_x_pos = screen_width/2 - character_width/2#화면 가로 절반 크기 해당 지점에 위치 
character_y_pos = screen_height - stage_height - character_height #화면 세로 크기 가장 아래 지점에 위치 
 

 
##################################  2> 이벤트 처리 (키보드, 마우스등)


# 이벤트 루프 
running = True # 게임이 진행중인가? 
while running :
    
    
    dt = clock.tick(60) # 게임화면의 초당 프레임 수(fps) 설정 / 값 높을수록 = '부드러움'
    
    
    # ======== 키 이동 (위치 정의)
    
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 - 파이썬 게임 실행위해 필수 
        
        if event.type == pygame.QUIT: # x버튼 창 끄는 이벤트 발생시 
            running = False # 게임 진행중이 아님 
            
            
    #===== 실제 그려주기 
            
    screen.blit(background, (0,0)) # 배경 그리기 in 위치 
    screen.blit(stage, (0,screen_height - stage_height)) # 배경 그리기 in 위치 
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 in 위치
            
            
    # ㅡㅡㅡㅡㅡㅡ 업데이트 필수 !!! 
    pygame.display.update() # 화면 수시로 다시 그려줘야, 계속 호출
    
    
    
 
# pygame 종료
pygame.quit()

