import pygame
import random

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """ plane game sprites"""
    def __init__(self,image_name,speed=1):
        # 调用父类的初始化方法
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

class Hero(GameSprite):
    def __init__(self,speed = 0, live = True):
        # 调用父类的初始化方法
        super().__init__('images\\plane_images\\me1.png')
        self.speed = speed
        self.live = live
        self.rect.y = SCREEN_RECT.bottom - self.rect.height
        self.bullet_group = pygame.sprite.Group()
        self.bullet = Bullet(0,0)
        self.i = 1
        self.j = 1
        self.max = 50

    def update(self):
        if self.rect.right > SCREEN_RECT.width:
            self.rect.x = SCREEN_RECT.width- self.rect.width
        elif self.rect.left < 0:
            self.rect.x = 0
        else:
            self.rect.x += self.speed

        if self.i % 20 in range(10):
            self.image = pygame.image.load('images\\plane_images\\me1.png')
        else:
            self.image = pygame.image.load('images\\plane_images\\me2.png')
        self.i += 1
        if self.live == False:
            self.died()

    def change(self):
        if self.i > 500:
            self.image = pygame.image.load('images\\plane_images\\me_destroy_3.png')
    def fire(self):
        for i in range(0,3):
            self.bullet = Bullet(self.rect.centerx,self.rect.y-i*15)
            self.bullet_group.add(self.bullet)

    def died(self):
        if self.j < self.max / 4:
            self.image = pygame.image.load('images\\plane_images\\me_destroy_1.png')
        elif self.j < self.max*2 / 4:
            self.image = pygame.image.load('images\\plane_images\\me_destroy_2.png')
        elif self.j < self.max*3 / 4:
            self.image = pygame.image.load('images\\plane_images\\me_destroy_3.png')
        else:
            self.image = pygame.image.load('images\\plane_images\\me_destroy_4.png')
        self.j += 1
        if self.j > self.max:
            self.kill()
            print('hero killed')


class BackGround(GameSprite):
    def __init__(self,pos_y = 0):
        # 调用父类的初始化方法
        super().__init__('images\\plane_images\\background.png')
        self.pos_y = pos_y
        self.rect.y = self.pos_y

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

class Bullet(GameSprite):
    def __init__(self,pos_x, pos_y):
        # 调用父类的初始化方法
        super().__init__('images\\plane_images\\bullet1.png')
        self.speed = -2
        self.pos_x = pos_x - self.rect.centerx
        self.pos_y = pos_y
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
    def update(self):
        super().update()
        # if bullets are out of the screem, delete them from group
        if self.rect.bottom < 0:
            self.kill()

class Enemy(GameSprite):
    def __init__(self, collide = False):
        super().__init__('images\\plane_images\\enemy1.png')
        self.collide = collide
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = 0
        self.i = 0
        self.max = 20
    def update(self):
        super().update()
        self.speed = 2
        if self.rect.top > SCREEN_RECT.height:
            self.kill()
        if self.collide == True:
            self.delenemy()

    def delenemy(self):
        # print("enemy died %s" % self.rect)
        if self.i < self.max / 4:
            self.image = pygame.image.load('images\\plane_images\\enemy1_down1.png')
        elif self.i < self.max*2 / 4:
            self.image = pygame.image.load('images\\plane_images\\enemy1_down2.png')
        elif self.i < self.max*3 / 4:
            self.image = pygame.image.load('images\\plane_images\\enemy1_down3.png')
        else:
            self.image = pygame.image.load('images\\plane_images\\enemy1_down4.png')
        self.i += 1
        if self.i > self.max:
            self.kill()
            print('kill')



if __name__ == '__main__':
    pass

