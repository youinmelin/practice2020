import pygame

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
    def __init__(self,speed = 0):
        # 调用父类的初始化方法
        super().__init__('images\\plane_images\\life.png')
        self.speed = speed
        self.rect.y = SCREEN_RECT.bottom - self.rect.height

    def update(self):
        if self.rect.right > SCREEN_RECT.width:
            self.rect.x = SCREEN_RECT.width- self.rect.width
        elif self.rect.left < 0:
            self.rect.x = 0
        else:
            self.rect.x += self.speed

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
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

if __name__ == '__main__':
    pass

