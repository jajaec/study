import os
import pygame

###################################### 기본
pygame.init()   # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 640  #가로크기
screen_height = 480 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("나도 팡")

# FPS
clock = pygame.time.Clock()
######################################

# 1. 사용자 게임 초기화 (배경, 이미지, 좌표, 폰트, 속도 등)
current_path = os.path.dirname(__file__)    # 현재 파일의 위치
image_path = os.path.join(current_path, "images")

# 배경만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

character_to_x = 0

character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기 여러발
weapons = []

weapon_speed = 10

# 이벤트 루프
running = True  # 게임이 진행중?

while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수 설정

    # 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트가 발생하였는가?
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            if event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        
        if event.type == pygame.KEYUP:
            if  event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                character_to_x = 0

    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 무기 위치 조정
    # 100, 200 -> 180, 160, 140, ...
    # 500, 200 -> 180, 160, 140, ...
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons ]

    # 무기가 천장에 닿으면 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0 ]

    # 5. 화면에 그리기
    # 아래 순서데로 그림.
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
   

    pygame.display.update() # 게임화면을 다시 그리기!

# pygame 종료
pygame.quit()