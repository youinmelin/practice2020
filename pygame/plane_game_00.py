import pygame
import sys
from plane_sprites import *

class MainWindow():
    def __init__(self):
        self.WIN_X = 480
        self.WIN_Y = 700

        BLACK = 0, 0, 0
        WHITE = 255, 255, 255
        GOLD = 255, 251, 0
        RED = pygame.Color('red')
        GREEN = 0, 255, 0
        BLUE = 0, 0, 255
        YELLOW = pygame.Color('yellow')
        self.color_list = [BLACK, WHITE, GOLD, RED, GREEN, BLUE, YELLOW]
        self.fps = 300
        self.fclock = pygame.time.Clock()

        title_name = 'plane game'
        init_result = pygame.init()

        # Create a window
        self.screen = pygame.display.set_mode((self.WIN_X,self.WIN_Y))
        self.screen.fill(self.color_list[0])
        pygame.display.update()
        # Set title
        pygame.display.set_caption(title_name)

    def start_game(self):
        bg = BackGround()
        bg_surf = bg.bg_move()
        hero = Hero('images\\plane_images\\life.png')
        hero2 = GameSprite('images\\plane_images\\life.png',2)
        hero_group = pygame.sprite.Group(hero,hero2)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print ('BYE-BYE')
                    pygame.quit()
                    sys.exit()
            self.screen.blit(bg_surf, (0,0))
            hero_group.update()
            hero_group.draw(self.screen)
            pygame.display.update()
            self.fclock.tick(self.fps)

class BackGround:
    def bg_move(self):
        pic_name = 'images\\plane_images\\background.png'
        bg_surf = pygame.image.load(pic_name)
        return bg_surf

if __name__ == '__main__':
    game = MainWindow()
    game.start_game()

