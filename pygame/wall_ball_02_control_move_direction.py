
import pygame,sys

pygame.init()
WIN_X = 500
WIN_Y = 600
screen = pygame.display.set_mode((WIN_X,WIN_Y))
ball_img = 'PYG02-ball.gif'
ball = pygame.image.load(ball_img)
ball_rect = ball.get_rect()
print(dir(ball_rect))
ball_rect.centerx = 100
ball_rect.centery = 100
fps = 300
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        speedx = 0
        speedy = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                speedy += 5
            if event.key == pygame.K_UP:
                speedy -= 5
            if event.key == pygame.K_LEFT:
                speedx -= 5
            if event.key == pygame.K_RIGHT:
                speedx += 5
    # ball_rect = rect(100,200,50,50)
        ball_rect = ball_rect.move(speedx,speedy)
    # appear on the opposite side of the window
    if ball_rect.centerx < 0:
        ball_rect.centerx = WIN_X
    if ball_rect.centery < 0:
        ball_rect.centery = WIN_Y
    if ball_rect.centerx > WIN_X:
        ball_rect.centerx = 0
    if ball_rect.centery > WIN_Y:
        ball_rect.centery = 0
    # print (ball_rect)
    screen.fill((0,0,0))
    screen.blit(ball,ball_rect)
    pygame.display.update()
    fclock.tick(fps)
