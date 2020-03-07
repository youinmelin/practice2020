from time import sleep
import pygame
import sys
from plane_sprites import *

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
class MainWindow():
    def __init__(self):

        self.fps = 60 
        self.fclock = pygame.time.Clock()

        title_name = 'plane game'
        init_result = pygame.init()

        # Create a window
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        pygame.display.update()
        # Set title
        pygame.display.set_caption(title_name)
        # create sprites and sprites group
        self.__create_sprites()
        # set timer event
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def __create_sprites(self):
        bg = BackGround( 0)
        bg2 = BackGround( -SCREEN_RECT.height)
        self.bg_group = pygame.sprite.Group(bg, bg2)

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        self.enemy_group = pygame.sprite.Group()


    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ('BYE-BYE')
                pygame.quit()
                sys.exit()
            if event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            if event.type == CREATE_ENEMY_EVENT:
                self.enemy = Enemy()
                self.enemy_group.add(self.enemy)
              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.hero.speed = -2
                if event.key == pygame.K_RIGHT:
                    self.hero.speed = 2
            elif event.type == pygame.KEYUP:
                self.hero.speed = 0

    def start_game(self):
        while True:
            self.__event_handler()


            self.bg_group.update()
            self.bg_group.draw(self.screen)
            self.hero_group.update()
            self.hero_group.draw(self.screen)
            self.enemy_group.update()
            self.enemy_group.draw(self.screen)
            self.hero.bullet_group.update()
            self.hero.bullet_group.draw(self.screen)
            pygame.display.update()
            self.fclock.tick(self.fps)

if __name__ == '__main__':
    game = MainWindow()
    game.start_game()

