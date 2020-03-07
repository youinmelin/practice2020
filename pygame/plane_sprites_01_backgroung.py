import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

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
    def __init__(self):
        # 调用父类的初始化方法
        super().__init__('images\\plane_images\\life.png')
        self.speed = 0
        self.rect.y = 600

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


if __name__ == '__main__':
    pass

