# A pygame minimum frame, help to build a new pygame program 
import pygame
import sys

WIN_X = 800
WIN_Y = 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
GOLD = 255, 251, 0
RED = pygame.Color('red')
GREEN = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = pygame.Color('yellow')
fps = 300
fclock = pygame.time.Clock()

title_name = 'new pygame'
init_result = pygame.init()

# Create a window
screen = pygame.display.set_mode((WIN_X,WIN_Y))
screen.fill(BLACK)
pygame.display.update()
# Set title
pygame.display.set_caption(title_name)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print ('BYE-BYE')
            pygame.quit()
            sys.exit()

    fclock.tick(fps)
