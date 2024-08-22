import pygame


pygame.init() #초기화 - 반드시필요


#========== 1 화면

# 화면 크기 설정

screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()

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

# 이동 '속도'
character_speed = 0.6


# 적 enemy 캐릭터

enemy =  pygame.image.load("/Users/mzc01-sarahy/Documents/Study/Dev/projects/nado-coding/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # 적군 이미지의 크기 
enemy_width = enemy_size[0] # 적군 가로크기 
enemy_height = enemy_size[1] # 적군 세로크기
enemy_x_pos = screen_width/2 - enemy_width/2 
enemy_y_pos = screen_height/2 - enemy_height/2 #적군은 위치 가운데로



#========== 3 텍스트

# 폰트정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)



# 총 시간
total_time = 10

# 시작시간 계산
start_ticks = pygame.time.get_ticks() #시작 tick 을 받아옴


#========== 3 키 이동

# 이벤트 루프 
running = True # 게임이 진행중인가? 
while running :
    
    
    dt = clock.tick(60) # 게임화면의 초당 프레임 수(fps) 설정 / 값 높을수록 = '부드러움'
    
    # 근데 프레임이랑, 속도는 관련 없어야!!! 프레임 높다고 속도 빨라지면 안됌
    # 보정법 = 40줄 '속도값' + 50줄 'fps숫자값' 보정해주면서 조절가능!!!
    
    
# 캐릭터가 1초동안 100만큼 이동을 하려면,,
# 10 fps : 1초 동안에 10번 동작(이동) -> 1번에 몇만큼 이동? 10만큼 (10속도 * 10fps = 100)
# 20 fps : 1초 동안에 20번 동작(이동) -> 1번에 몇만큼 이동? 5만큼 (5속도 * 20fps = 100)
    
    print('fps : ' + str(clock.get_fps()))
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 - 파이썬 게임 실행위해 필수 
        
        if event.type == pygame.QUIT: # x버튼 창 끄는 이벤트 발생시 
            running = False # 게임 진행중이 아님 
            
        if event.type == pygame.KEYDOWN: # 키 눌럿을때
            if event.key == pygame.K_LEFT : #왼쪽 키를
                to_x -= character_speed
            if event.key == pygame.K_RIGHT : #오른쪽 키를
                to_x += character_speed
            if event.key == pygame.K_UP : #위쪽 키를
                to_y -= character_speed
            if event.key == pygame.K_DOWN : #아래쪽 키를
                to_y += character_speed
                
        if event.type == pygame.KEYUP : # 키 뗏을때 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                to_y = 0
            
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
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
        
    # 충돌 처리를 위한 rect 정보 업데이트
    
    character_rect = character.get_rect() #rectangle정보 = x좌표, y좌표 / width, height
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect() #rectangle정보 = x좌표, y좌표 / width, height
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos  
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect): #충돌 했니
        print('충돌했다.')
        running = False
     
            
            
    #===== 실제 그려주기 
            
    screen.blit(background, (0,0)) # 배경 그리기 in 위치 
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 in 위치 
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적군 그리기 in 위치 
    
    #ㅡㅡㅡ 타이머 텍스트 집어 넣기 
    
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   
    # (현재 더 커진 지나온 찍힌 시간 - 최초 짧앗던 시작 시간) = 경과 시간 
    # 경과시간(ms) / 1000으로 나누어서 = 초(s) 단위로 표시 
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    # render : 실제 그리는 행위
    # 남은시간, 그냥 무조건 true ,글자 색상
     
    #ㅡㅡㅡ
    
    screen.blit(timer, (10, 10)) # 타이머 텍스트 in 위치 
    
    timedd = 'timeout!!'
    
    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0 :
        print('TimeOut')
        
        running = False
    
    
    pygame.display.update() # 화면 수시로 다시 그려줘야, 계속 호출 - 필수
    
# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기 (ms)
       


# pygame 종료
pygame.quit()

