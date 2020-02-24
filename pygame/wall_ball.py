# https://www.bilibili.com/video/av19574503?p=19
# mouse event
# when press mouse left key, the ball stop. 
# when press mouse left key and move mouse, the ball move with the mouse
# when release mouse left key, the ball continue to move 
import pygame,sys

pygame.init()
WIN_X = 500
WIN_Y = 600
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('WALL BALL')
screen = pygame.display.set_mode((WIN_X,WIN_Y),pygame.RESIZABLE)
# screen = pygame.display.set_mode((WIN_X,WIN_Y),pygame.NOFRAME)
# screen = pygame.display.set_mode((WIN_X,WIN_Y),pygame.FULLSCREEN)
# screen = pygame.display.set_mode((WIN_X,WIN_Y))
ball_img = 'PYG02-ball.gif'
speedx = 1
speedy = 1
# mark the ball's status
still = False
ball = pygame.image.load(ball_img)
ball_rect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()

while True:
    r = int(( ball_rect.right/WIN_X)*255)
    g = int((ball_rect.bottom/WIN_Y)*255)
    b = abs(speedx -speedy)
    print ( 'r,g,b',r,g,b)
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
    screen.fill((0,0,0))
    screen.blit(ball,ball_rect)
    pygame.display.update()
    fclock.tick(fps)
