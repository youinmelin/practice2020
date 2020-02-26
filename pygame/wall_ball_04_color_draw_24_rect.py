# https://www.bilibili.com/video/av19574503?p=24
import pygame
import sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

init_result = pygame.init()
print(init_result)

# Create a window
screen = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
screen.fill((255,255,255))
GOLD = 255,251,0
RED = pygame.Color('red')
r1rect = pygame.draw.rect(screen,GOLD,(100, 100, 200, 100),5)
r2rect = pygame.draw.rect(screen,RED,(210, 210, 200, 100), 0)

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
