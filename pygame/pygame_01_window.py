# https://ukdevguy.com/how-to-create-a-game-window-in-pygame/

import pygame
import sys

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

init_result = pygame.init()
print(init_result)

# Create a game window
game_window = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
game_window.fill((255,255,255))
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