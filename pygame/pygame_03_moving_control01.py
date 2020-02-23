from pygame_00_base_frog import *
import random
import sys

pygame.init()
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
r = 30
x = 300
y = 300
color = 255,0,0
length = 50
length2 = 10
angle_a = 90
sleep_time = 2
tt = Draw(screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left')
                x -= 3
        # x, y = pygame.mouse.get_pos()

        screen.fill((0,0,0))
        tt.circle(r,x,y,width = 0,color = color, center = True)
