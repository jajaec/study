# 1. 모든 공을 없애면 게임 종료 (성공)
# 2. 캐릭터는 공에 닿으면 게임 종료 (실패)
# 3. 시간 제한 99초 초과 시 게임 종료 (실패)

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
# 무기 기동 속도
weapon_speed = 10

# 공만들기 (4개 크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9]

# 공 정보들
balls = []

# 최초 발생 큰공 추가
balls.append({
    "pos_x" : 50,   # 공의 X 좌표
    "pos_y" : 50,   # 공의 Y 좌표
    "img_idx" : 0,  # 공의 이미지 인덱스
    "to_x" : 3, # 공의 X 이동방향
    "to_y" : -6, # 공의 Y 이동방향
    "init_spd_y" : ball_speed_y[0]}) # Y 최초 속도

# 사라질 무기와 공정보
weapon_to_remove = -1
ball_to_remove = -1

# 이벤트 루프
running = True  # 게임이 진행중?

# Font 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks()   # 시작 시간 정의

# 게임 종료 메시지  / Timeout, Mission Complete, Game Over
game_result = "Game Over!"

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

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을때 공 이동 위치 변경 (튕김 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1
        
        # 세로 위치
        # 스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:   # 그외의 모든 경우에 속도 증가
            ball_val["to_y"] += 0.5
        
        ball_val["pos_x"] +=  ball_val["to_x"]
        ball_val["pos_y"] +=  ball_val["to_y"]

    # 충돌 처리

    # 캐릭터 rect 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # 공 rect 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # 공과 캐릭터 충돌 처리
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # 공과 무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 rect 정보 업데이트 
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # 충돌 채크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx

                # 가장 작은 공이 아니면 둘로 나누워짐.
                if ball_img_idx < 3:
                    # 현재 공크기 정보
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # 나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # 왼쪽으로가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),   # 공의 X 좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),   # 공의 Y 좌표
                        "img_idx" : ball_img_idx + 1,  # 공의 이미지 인덱스
                        "to_x" : -3, # 공의 X 이동방향
                        "to_y" : -6, # 공의 Y 이동방향
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]}) # Y 최초 속도

                    # 왼쪽으로가는 작은 공
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),   # 공의 X 좌표
                        "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),   # 공의 Y 좌표
                        "img_idx" : ball_img_idx + 1,  # 공의 이미지 인덱스
                        "to_x" : 3, # 공의 X 이동방향
                        "to_y" : -6, # 공의 Y 이동방향
                        "init_spd_y" : ball_speed_y[ball_img_idx + 1]}) # Y 최초 속도

                break
        else:
            continue
        break

        #for 바깥조건:
        #    바깥동작
        #    for 안쪽조건:
        #        안쪽동작
        #        if 충돌하면:
        #            break
        #    else:
        #        continue
        #    break

    # 충돌되 무기 or 공 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 모든 공 없으면 게임 종료
    if len(balls) == 0:
        game_result = "Mission Complete!"
        running = False

    # 5. 화면에 그리기
    # 아래 순서데로 그림.
    screen.blit(background, (0, 0))

    # 무기 이미지 그리기
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    # 공 이미지 그리기
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]

        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
   
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("Time : {}".format(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10, 10))

    # 시간 초과
    if total_time - elapsed_time <= 0:
        game_result = "Time Over!"
        running = False


    pygame.display.update() # 게임화면을 다시 그리기!

# 게임오버 메시지
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(2000)

# pygame 종료
pygame.quit()