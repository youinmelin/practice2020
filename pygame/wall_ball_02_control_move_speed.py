# https://www.bilibili.com/video/av19574503?p=7

import pygame,sys

pygame.init()
WIN_X = 500
WIN_Y = 600
screen = pygame.display.set_mode((WIN_X,WIN_Y))
ball_img = 'PYG02-ball.gif'
speedx = 1
speedy = 1
ball = pygame.image.load(ball_img)
ball_rect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
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
    if ball_rect.left < 0 or ball_rect.right > WIN_X:
        speedx = - speedx
    if ball_rect.top < 0 or ball_rect.bottom > WIN_Y:
        speedy = - speedy
    print (ball_rect)
    screen.fill((0,0,0))
    screen.blit(ball,ball_rect)
    pygame.display.update()
    fclock.tick(fps)
