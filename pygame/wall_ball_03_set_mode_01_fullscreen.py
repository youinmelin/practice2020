# https://www.bilibili.com/video/av19574503?p=11
# pygame.display
# fullscreen if press ESC , exit the game

import pygame,sys

pygame.init()
# get screen x and y position,before set mode
cur_x = pygame.display.Info().current_w
cur_y = pygame.display.Info().current_h
screen = pygame.display.set_mode((cur_x,cur_y),pygame.FULLSCREEN)
# screen = pygame.display.set_mode((WIN_X,WIN_Y),pygame.NOFRAME)
# screen = pygame.display.set_mode((WIN_X,WIN_Y),pygame.FULLSCREEN)
# screen = pygame.display.set_mode((WIN_X,WIN_Y))
ball_img = 'PYG02-ball.gif'
speedx = 1
speedy = 1
ball = pygame.image.load(ball_img)
ball_rect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()
print(cur_x,cur_y)

while True:
    for event in pygame.event.get():
        cur_x = pygame.display.Info().current_w
        cur_y = pygame.display.Info().current_h
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            if speedy > 0:
                if event.key == pygame.K_DOWN:
                    speedy -= 1
                if event.key == pygame.K_UP:
                    speedy += 1
            if speedy <= 0:
                if event.key == pygame.K_DOWN:
                    speedy += 1
                if event.key == pygame.K_UP:
                    speedy -= 1
            if speedx > 0:
                if event.key == pygame.K_LEFT:
                    speedx -= 1
                if event.key == pygame.K_RIGHT:
                    speedx += 1
            if speedx <= 0:
                if event.key == pygame.K_LEFT:
                    speedx += 1
                if event.key == pygame.K_RIGHT:
                    speedx -= 1
    # ball_rect = rect(100,200,50,50)
    ball_rect = ball_rect.move(speedx,speedy)
    if ball_rect.left < 0 or ball_rect.right > cur_x:
        speedx = - speedx
    if ball_rect.top < 0 or ball_rect.bottom > cur_y:
        speedy = - speedy
    # print (ball_rect)
    screen.fill((0,0,0))
    screen.blit(ball,ball_rect)
    pygame.display.update()
    fclock.tick(fps)
