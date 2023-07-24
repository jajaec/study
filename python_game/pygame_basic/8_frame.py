import pygame

###################################### 기본
pygame.init()   # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  #가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("나도 게임")

# FPS
clock = pygame.time.Clock()
######################################

# 1. 사용자 게임 초기화 (배경, 이미지, 좌표, 폰트, 속도 등)
# 배경이미지 불러오기
background = pygame.image.load("pygame_basic/background.png")

# 캐릭터 이미지 불러오기
character = pygame.image.load("pygame_basic/character.png")
character_size = character.get_rect().size    # 이미지 크기 GET
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 이미지
enemy = pygame.image.load("pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size    # 이미지 크기 GET
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작 시간정보
start_ticks = pygame.time.get_ticks()

# 이벤트 루프
running = True  # 게임이 진행중?

while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수 설정

    print("fps: " + str(clock.get_fps()))

    # 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 화면 경계 설정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 화면 경계 설정
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    # 4. 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) #배경 그리기
    #screen.fill((0, 0, 255))
    screen.blit(character, (character_x_pos, character_y_pos))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타이머
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))

    screen.blit(timer, (10, 10))

    if (total_time - elapsed_time) <= 0:
        print("타임아웃")
        running = False
    
    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()