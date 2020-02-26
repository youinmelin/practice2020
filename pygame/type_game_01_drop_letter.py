# A pygame minimum frame, help to build a new pygame program 
import pygame
import sys
import random
import pygame.freetype

WIN_X = 800
WIN_Y = 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
GOLD = 255, 251, 0
RED = pygame.Color('red')
GREEN = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = pygame.Color('yellow')
fps = 30
fclock = pygame.time.Clock()

title_name = 'new pygame'
init_result = pygame.init()

# Create a window
screen = pygame.display.set_mode((WIN_X,WIN_Y))
screen.fill(BLACK)
pygame.display.update()
# Set title
pygame.display.set_caption(title_name)
pos = [100,50]
alphabet_list = 'abcdefghijklmnopqrstuvwxyz'

# font = pygame.font.Font(None, 50)
font = pygame.freetype.Font(None, 50)
letter = alphabet_list[random.randint(0,25)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print ('BYE-BYE')
            pygame.quit()
            sys.exit()
    if pos[1] == WIN_Y:
        pos[1] = 50
        letter = alphabet_list[random.randint(0,25)]
    font_surf, font_rect = font.render(letter,WHITE)
    screen.fill(BLACK)
    pos[1] += 5
    screen.blit(font_surf,(pos[0],pos[1]))
    pygame.display.update()
        
    fclock.tick(fps)
