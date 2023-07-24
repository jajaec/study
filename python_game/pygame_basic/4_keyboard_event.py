import pygame

pygame.init()   # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  #가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("나도 게임")

# 배경이미지 불러오기
background = pygame.image.load("D:/Workspaces/python_game/pygame_basic/background.png")

# 캐릭터 이미지 불러오기
character = pygame.image.load("D:/Workspaces/python_game/pygame_basic/character.png")
character_size = character.get_rect().size    # 이미지 크기 GET
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True  # 게임이 진행중?

while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 3
            elif event.key == pygame.K_RIGHT:
                to_x += 3
            elif event.key == pygame.K_UP:
                to_y -= 3
            elif event.key == pygame.K_DOWN:
                to_y += 3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x
    character_y_pos += to_y

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

    screen.blit(background, (0, 0)) #배경 그리기
    #screen.fill((0, 0, 255))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()