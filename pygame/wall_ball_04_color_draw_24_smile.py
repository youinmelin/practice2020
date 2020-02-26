# https://www.bilibili.com/video/av19574503?p=24
import pygame
import sys
from math import pi

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

init_result = pygame.init()
print(init_result)

# Create a window
screen = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
GOLD = 255,251,0
RED = pygame.Color('red')
WHITE = 255,255,255
GREEN = pygame.Color('green')

# r1rect = pygame.draw.rect(screen,GOLD,(100, 100, 200, 100),5)
# r2rect = pygame.draw.rect(screen,RED,(210, 210, 200, 100), 0)
e1rect = pygame.draw.ellipse(screen,GREEN,(50,50,500,300),3)
c1rect =  pygame.draw.circle(screen,GOLD,(200,180),30,5)
c2rect =  pygame.draw.circle(screen,GOLD,(400,180),30)
r1rect =  pygame.draw.rect(screen,RED,(170,130,60,10),3)
r2rect =  pygame.draw.rect(screen,RED,(370,130,60,10))
plist = [(295,170),(285,250),(260,280),(340,280),(315,250),(305,170)]
l1rect = pygame.draw.lines(screen,GREEN,True,plist,2)
a1rect = pygame.draw.arc(screen,RED,(200,220,200,100),1.4*pi,1.9*pi,3) 

pygame.display.update()
# Set title
pygame.display.set_caption('new pygame')

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print (event.type)
            game_running = False
pygame.quit()
sys.exit()
