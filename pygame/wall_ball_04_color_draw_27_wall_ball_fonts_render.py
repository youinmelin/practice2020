# https://www.bilibili.com/video/av19574503?p=27
# turn ball to text, use render
# when press mouse left key, the ball stop. 
# when press mouse left key and move mouse, the ball move with the mouse
# when release mouse left key, the ball continue to move 
import pygame,sys
import pygame.freetype

pygame.init()
WIN_X = 500
WIN_Y = 600
GOLD = 255,251,0
RED = pygame.Color('red')
WHITE = 255,255,255
GREEN = pygame.Color('green')
BLACK = 0,0,0
pos = [230, 160]
# 建立字体对象
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('WALL BALL')
screen = pygame.display.set_mode((WIN_X,WIN_Y),pygame.RESIZABLE)
# screen = pygame.display.set_mode((WIN_X,WIN_Y),pygame.NOFRAME)
# screen = pygame.display.set_mode((WIN_X,WIN_Y),pygame.FULLSCREEN)
# screen = pygame.display.set_mode((WIN_X,WIN_Y))
f1 = pygame.freetype.Font('C://Windows//Fonts//msyh.ttc',36)
f1surf, f1rect = f1.render('NASA',fgcolor=GOLD,size=50)
ball_img = 'PYG02-ball.gif'
speedx = speedfx = 1
speedy = speedfy = 1
# mark the ball's status
still = False
ball_surf = pygame.image.load(ball_img)
ball_rect = ball_surf.get_rect()
fps = 300
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            WIN_X= event.w
            WIN_Y= event.h
            screen = pygame.display.set_mode((WIN_X,WIN_Y),pygame.RESIZABLE)
        
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1: # left key of mouse
                still = True
        if event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1: # if release, move the ball to the mouse x y
                ball_rect = ball_rect.move(event.pos[0] - ball_rect.left, event.pos[1] - ball_rect.top)
        if event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                ball_rect = ball_rect.move(event.pos[0] - ball_rect.left, event.pos[1] - ball_rect.top)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

            # control speed by direction key
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
    # 如果窗口没有最小化，就移动小球
    if pygame.display.get_active() and not still:
        ball_rect = ball_rect.move(speedx,speedy)
    if ball_rect.left < 0 or ball_rect.right > WIN_X:
        speedx = - speedx
        if ball_rect.left < 0:
            ball_rect.left = 0
        if ball_rect.right > WIN_X:
            ball_rect.right = WIN_X
    if ball_rect.top < 0 or ball_rect.bottom > WIN_Y:
        speedy = - speedy
        if ball_rect.top < 0:
            ball_rect.top = 0
        if ball_rect.bottom > WIN_Y:
            ball_rect.bottom = WIN_Y
    # print (ball_rect)
    if pos[0]<0 or pos[0] > WIN_X:
        speedfx = -speedfx
    if pos[1]<0 or pos[1] > WIN_Y:
        speedfy = -speedfy
    pos[0] = pos[0] + speedfx
    pos[1] = pos[1] + speedfy

    screen.fill((0,0,0))
    # render must be after the fill
    f1surf, f1rect = f1.render('NASA',fgcolor=GOLD,size=50)
    screen.blit(f1surf,(pos[0],pos[1]))
    # screen.blit(ball_surf,(pos[0],pos[1]))
    screen.blit(ball_surf,ball_rect)
    pygame.display.update()
    fclock.tick(fps)
