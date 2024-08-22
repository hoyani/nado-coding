import pygame


pygame.init() #초기화 - 반드시필요


#========== 1 화면

# 화면 크기 설정

screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경이미지 불러오기
background = pygame.image.load("/Users/mzc01-sarahy/Documents/Study/Dev/projects/nado-coding/pygame_basic/background.png")


#========== 2 캐릭터

# 스프라이트 캐릭터 불러오기
character =  pygame.image.load("/Users/mzc01-sarahy/Documents/Study/Dev/projects/nado-coding/pygame_basic/character.png")
character_size = character.get_rect().size # 캐릭터 이미지의 크기 
character_width = character_size[0] # 캐릭터 가로크기 
character_height = character_size[1] # 캐릭터 세로크기
character_x_pos = screen_width/2 - character_width/2#화면 가로 절반 크기 해당 지점에 위치 
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래 지점에 위치 

# 이동할 좌표 
to_x = 0
to_y = 0


#========== 3 키 이동

# 이벤트 루프 
running = True # 게임이 진행중인가? 
while running :
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 - 파이썬 게임 실행위해 필수 
        if event.type == pygame.QUIT: # x버튼 창 끄는 이벤트 발생시 
            running = False # 게임 진행중이 아님 
            
        if event.type == pygame.KEYDOWN: # 키 눌럿을때
            if event.key == pygame.K_LEFT : #왼쪽 키를
                to_x -= 2
            if event.key == pygame.K_RIGHT : #오른쪽 키를
                to_x += 2
            if event.key == pygame.K_UP : #위쪽 키를
                to_y -= 2
            if event.key == pygame.K_DOWN : #아래쪽 키를
                to_y += 2
                
        if event.type == pygame.KEYUP : # 키 뗏을때 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0
            
    character_x_pos += to_x
    character_y_pos += to_y
    
    #======= 화면 밖에 안 벗어나게 
            
    # 가로 경계값 처리 
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width : 
        character_x_pos = screen_width - character_width
        
    # 세로 경계값 처리 
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height : 
        character_y_pos = screen_height - character_height
            
            
            
    #===== 실제 그려주기 
            
    screen.blit(background, (0,0)) # 배경 그리기 in 위치 
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 in 위치 

    pygame.display.update() # 화면 수시로 다시 그려줘야, 계속 호출 - 필수
        


# pygame 종료
pygame.quit()

