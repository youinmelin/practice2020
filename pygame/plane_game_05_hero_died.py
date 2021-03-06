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
        self.enemy = Enemy()
        self.enemy_group = pygame.sprite.Group()
        self.enemy_group.add(self.enemy)


    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ('BYE-BYE')
                pygame.quit()
                sys.exit()
            if event.type == HERO_FIRE_EVENT and self.hero.live == True:
                self.hero.fire()
            if event.type == CREATE_ENEMY_EVENT  and self.hero.live == True:
                self.enemy = Enemy()
                self.enemy_group.add(self.enemy)
              
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.hero.speed = -2
                if event.key == pygame.K_RIGHT:
                    self.hero.speed = 2
                # after hero died, press 'r', will restart the game
                if self.hero.live == False and event.unicode == 'r':
                    self.__init__()
            elif event.type == pygame.KEYUP:
                self.hero.speed = 0

    def __update_sprite(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    def __check_collide(self):

        for enemy_plane in self.enemy_group:
            for current_bullet in self.hero.bullet_group:
                if pygame.Rect.colliderect(current_bullet.rect, enemy_plane.rect):
                    current_bullet.kill()
                    enemy_plane.collide = True
            if not enemy_plane.collide :
                if pygame.Rect.colliderect(self.hero.rect, enemy_plane.rect):
                    self.hero.live = False
                    # self.enemy_group.empty()
                    self.hero.died()

    def __gameover(self):
        pass

    def start_game(self):
        while True:
            self.fclock.tick(self.fps)
            self.__event_handler()
            self.__update_sprite()
            self.__check_collide()
            pygame.display.update()
            
            # print(f'enemies:{len(self.enemy_group)}')

if __name__ == '__main__':
    game = MainWindow()
    game.start_game()

