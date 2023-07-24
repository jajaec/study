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


# 이벤트 루프
running = True  # 게임이 진행중?

while running:
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False
    
    screen.blit(background, (0, 0)) #배경 그리기
    #screen.fill((0, 0, 255))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()