# 1. 모든 공을 없애면 게임 종료 (성공)
# 2. 캐릭터는 공에 닿으면 게임 종료 (실패)
# 3. 시간 제한 99초 초과시 게임종료 (실패)


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
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터 두기 위한 용도 / get_rect 함수 => 기본 0 idx 가로, 1 idx 세로
 



#-------- 캐릭터 

# 캐릭터 불러오기 (상대경로)
character = pygame.image.load(os.path.join(image_path, "character2.png"))
character_size = character.get_rect().size
character_width = character_size[0] # 스테이지의 높이 위에 캐릭터 두기위해 사용 
character_height = character_size[1] # 스테이지의 높이 위에 캐릭터 두기위해 사용 

character_x_pos = screen_width/2 - character_width/2 # 화면 가로 절반 크기 해당 지점에 위치 
character_y_pos = screen_height - stage_height - character_height # 화면 세로 크기 가장 아래 지점에 위치 

 
# 캐릭터 이동방향 
character_to_x = 0
 

# 캐릭터 이동 '속도' 
character_speed = 5



#-------- 무기  

# 무기 만들기 
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0] 


# 무기는 한번에 여러발 발사 가능 - 무기여러개 list 관리
weapons = [] # 위치값들


# 무기 이동 속도 
weapon_speed = 10



#-------- 공 (각 4개 따로처리)

# 공 만들기 
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png")),
]

# 공 크기에 따른 최초 속도들 
ball_speed_y = [ -18, -15, -12, -9 ] # index 0,1,2,3 에 해당하는것 (마이너스는 y값 위로 올라가야 되니)


# 공 정보
balls = []

# 최초 발생하는 큰 공0 추가 
balls.append({
    "pos_x" : 50, # 공의 x좌표
    "pos_y" : 50, # 공의 y좌표
    "img_idx" : 0, # 공의 이미지 인덱스 
    "to_x" : 3, # x축 이동방향 
    "to_y" : -6, # y축 이동방향 
    "init_speed_y" : ball_speed_y[0] # y 최초 속도    
})

# 사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1


# ㅡㅡㅡㅡㅡㅡㅡㅡ Font 정의
game_font = pygame.font.Font(None, 40)
total_time = 10
start_ticks = pygame.time.get_ticks() # 시작시간 정이ㅡ 


# ㅡㅡ 게임 종료 메시지 ㅡㅡ
# Time-Over 시간 초과 실패 
# Mission Complete 성공
# Gameover (캐릭터 공에 맞음, 실패)
game_result = "game over"


##################################  2> 이벤트 처리 (키보드, 마우스등)


# 이벤트 루프 
running = True # 게임이 진행중인가? 
while running :
    
    
    dt = clock.tick(30) # 게임화면의 초당 프레임 수(fps) 설정 / 값 높을수록 = '부드러움'
    
    
    # ================ 키 이동 (위치 정의)
    
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가 - 파이썬 게임 실행위해 필수 
        
        if event.type == pygame.QUIT: # x버튼 창 끄는 이벤트 발생시 
            running = False # 게임 진행중이 아님 
        
        if event.type == pygame.KEYDOWN: # 키 눌럿을때
            if event.key == pygame.K_LEFT : #왼쪽 키를
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT : #오른쪽 키를
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE : #스페이스바 키를
                weapon_x_pos = character_x_pos + character_width/2 - weapon_width/2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
                
                
        if event.type == pygame.KEYUP : # 키 뗏을때 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                character_to_x = 0
    
    # 게임 캐릭터 위치 최종 정의 
    character_x_pos += character_to_x 
            

    #================ 화면 밖에 안 벗어나게 (위치조정))
            
    #ㅡㅡㅡㅡㅡ 캐릭터 
    
    # 가로 경계값 처리 
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width : 
        character_x_pos = screen_width - character_width
            
    #ㅡㅡㅡㅡㅡ 무기
    
    # 무기 위치조정
    # 100, 200 -> 180, 160, 140 ... (y값만 speed 만큼 위로 올라가)
    # 500, 200 -> 180, 160, 140 ...
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로 올려 
    
    '''
    w[0]는 x_pos
    w[1]는 y_pos
    
    w[1] - weapon_speed 를 빼는건 : y값이 위로 올라가는거 !!! miss
    
    '''
    
    # 천장에 닿은 무기 증발
    
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0] #y좌표가 천장 0 보다크다? 그림상 천장 아래다!! 아래일 경우만 그려라
    
    #ㅡㅡㅡㅡㅡ 공 
    
    # 위치 정의
    for ball_idx, ball_val in enumerate(balls) : 
        ball_pos_x = ball_val['pos_x']    
        ball_pos_y = ball_val['pos_y'] 
        ball_img_idx = ball_val['img_idx']
        
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        
        # 가로벽에 닿았을때 공 이동 위치변경 (튕겨나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width : # 화면값 벗어나면 닿으면 -> 튕기게 만들기 
            ball_val['to_x'] = ball_val['to_x'] * -1 #x증감값 부호를 바꿔, 방향 전환!!
            
        
        # 세로 위치 
        # 1> 스테이지에 튕겨서 올라가는 처리 
        if ball_pos_y >= screen_height - stage_height - ball_height : # y좌표가 화면보다 커지려 한다? (아래쪽)
            ball_val['to_y'] = ball_val['init_speed_y'] # y 방향 초기값인 마이너스로 다시 위로 올라가게 셋팅
        else : # 2> 그외 모든 경우는 (위쪽으로 잘가는)
            ball_val['to_y'] += 0.5 # 반씩 속도 증가 
            
        ball_val['pos_x'] += ball_val['to_x']
        ball_val['pos_y'] += ball_val['to_y']
        
    
    
    #================ 충돌 처리 
        '''

        충돌처리 = 쪼개기 
        
        1. 공-캐릭터 : 게임 종료
        2. 공-무기 : 작아지거나 사라지는

        '''
    
    # ㅡㅡㅡㅡ 1. 공-캐릭터 충돌 
        
    # 캐릭터 rect 정보 업데이트 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    

    for ball_idx, ball_val in enumerate(balls) : 
        ball_pos_x = ball_val['pos_x']
        ball_pos_y = ball_val['pos_y'] 
        ball_img_idx = ball_val['img_idx'] 
        
        
        
        # 공 rect 정보 업데이트 
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        
        
        # 공 - 캐릭터 충돌 처리 
        if character_rect.colliderect(ball_rect): # 공-캐릭터 충돌햇나?
            running = False
            break # 게임 종료
        
        
        
    # ㅡㅡㅡㅡ 2. 공- 무기들 충돌 
        
        for weapon_idx, weapon_val in enumerate(weapons) : 
            weapon_x_pos = weapon_val[0]
            weapon_y_pos = weapon_val[1]
            
            # 무기 rect 정보 업데이트 
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_pos
            weapon_rect.top = weapon_y_pos
            
            # 공 - 무기들 충돌 처리 
            if weapon_rect.colliderect(ball_rect) :
                weapon_to_remove = weapon_idx # 해당 무기 없애기 위한 값 설정
                ball_to_remove = ball_idx # 해당 공 없애기 위한 값 설정
                
                
                # 가장 작은크기 공 아니면 = 다음 단계 공으로 나눠주기  
                if ball_img_idx < 3:
                    
                    # 현재 공 크기정보 가지고옴
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]
                    
                    # 나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx +1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]
                    
                    
                    # 왼쪽으로 튕겨나가는 작은 공 
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x좌표
                        "pos_y" : ball_pos_x + (ball_height / 2) - (small_ball_height / 2), # 공의 y좌표
                        "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스 
                        "to_x" : -3, # x축 이동방향 
                        "to_y" : -6, # y축 이동방향 
                        "init_speed_y" : ball_speed_y[ball_img_idx + 1] # y 최초 속도    
                    })
                    
                    # 오른쪽으로 튕겨나가는 작은 공 
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x좌표
                        "pos_y" : ball_pos_x + (ball_height / 2) - (small_ball_height / 2), # 공의 y좌표
                        "img_idx" : ball_img_idx + 1, # 공의 이미지 인덱스 
                        "to_x" : +3, # x축 이동방향 
                        "to_y" : -6, # y축 이동방향 
                        "init_speed_y" : ball_speed_y[ball_img_idx + 1] # y 최초 속도    
                    })
                    
                break
    # 충돌된 공 or 무기 -> 없애기
    if ball_to_remove > -1 :
        del balls[ball_to_remove]
        ball_to_remove = -1
        
    if weapon_to_remove > -1 :
        del weapon[weapon_to_remove]
        weapon_to_remove = -1
            
            
            
            
    
    #================ 실제 그려주기 
            
    screen.blit(background, (0,0)) # 배경 그리기 in 위치 
    
    for weapon_x_pos, weapon_y_pos in weapons :
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos)) # 무기 그리기 in 위치 
        
    for idx, val in enumerate(balls) :
        ball_pos_x = val['pos_x']
        ball_pos_y = val['pos_y']
        ball_img_idx = val['img_idx']
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y)) # 튀는 공 그리기 in 위치 
        
        
    
    screen.blit(stage, (0,screen_height - stage_height)) # 바닥 그리기 in 위치 
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 in 위치 
    
    # 경과 시간 게산 
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)))
    screen.blit(timer, (10, 10))
    
    # 시간 초과 햇다면?
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False
     
            
    # ㅡㅡㅡㅡㅡㅡ 업데이트 필수 !!! 
    pygame.display.update() # 화면 수시로 다시 그려줘야, 계속 호출
    
    
# 게임오버 메시지 
msg = game_font.render(game_result, True, (255,255,0)) #노란색 
msg_rect = msg.get_rect(cemter =( int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect) 
pygame.display.update()

# 2초 대기 후 종료 
pygame.time.delay(2000)
 
 
 
# pygame 종료
pygame.quit()

