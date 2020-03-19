import pygame
import sys
from math import sin,cos,pi
import random

SCREEN_RECT = pygame.Rect(0, 0, 850, 850)

class MainWindow():
    def __init__(self):

        BLACK = 0, 0, 0
        WHITE = 255, 255, 255
        GOLD = 255, 251, 0
        RED = pygame.Color('red')
        GREEN = 0, 255, 0
        BLUE = 0, 0, 255
        YELLOW = pygame.Color('yellow')
        self.color_list = [BLACK, WHITE, GOLD, RED, GREEN, BLUE, YELLOW]
        self.fps = 1
        self.fclock = pygame.time.Clock()

        title_name = 'clock'
        init_result = pygame.init()

        # Create a window
        self.screen = pygame.display.set_mode((SCREEN_RECT.width, SCREEN_RECT.height))
        self.screen.fill(self.color_list[0])
        pygame.display.update()
        # Set title
        pygame.display.set_caption(title_name)
        self.angle = 0
        # size[0]:width, size[1]:height
        self.size = [89, 30]
        self.flist = []
        self.start_point_x = 135
        self.start_point_y = 430
        self.flowers_num = 60
        self.create_sprites()
        self.count = 0

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ('BYE-BYE')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print ('BYE-BYE')
                    pygame.quit()
                    sys.exit()

    def start_game(self):
        while True:
            self.__event_handler()
            self.fclock.tick(self.fps)
            self.screen.fill(self.color_list[1])
            self.stretch()
            self.flower_group.update()
            pygame.display.update()

    def create_sprites(self):
        self.flower_group = pygame.sprite.Group()
        # create_dial_plate
        for i in range(self.flowers_num):
            self.angle += 360/self.flowers_num
            # self.angle = 0 if self.angle>=360 else self.angle
            flower_sprite =  Clock(self.screen,(self.start_point_x,self.start_point_y),self.size,self.angle)
            # draw lines to guide the pictures
            self.start_point_x,self.start_point_y = self.line(self.size[1],self.start_point_x,self.start_point_y,self.angle)
            self.flower_group.add(flower_sprite)
            self.flist.append(flower_sprite)
        # print(dir(self.flower_group))


    def line(self,length,x=0,y=0,angle_a = 270,color=(255,255,255)):
        x2 = x + length*(sin(angle_a * pi/180))
        y2 = y + length*(sin((90-angle_a) * pi/180))
        pygame.draw.line(self.screen,color,(x,y),(x2,y2),7)
        return x2,y2

    def stretch(self):
        for f in self.flist:
            if f.is_stretch:
                pass
            else:
                self.count += 1
                self.count = 0 if self.count >= 60 else self.count
        #self.flist[self.count].is_stretch = True if i == 0 else False
        self.flist[self.count].is_stretch = True

class Clock(pygame.sprite.Sprite):
    def __init__(self,screen,pointA, image_size,angle,is_stretch = False):
        super().__init__()
        self.screen = screen
        self.angle_degree = angle
        self.pointAx = pointA[0]
        self.pointAy = pointA[1]
        self.is_stretch = is_stretch
        image_name = 'images\\clock\\clock_flower1.jpg'
        # type(self.image) --> pygame.Surface
        self.size = image_size
        self.image = pygame.image.load(image_name)
        self.rect_new = self.count_rect(100,100,self.angle_degree)
        self.i = 0

    def update(self):

        # anticlockwise ( not clockwise )
        # create a new variable to save image rotated
        self.image_changed = pygame.transform.rotozoom(self.image, self.angle_degree,1)
        self.image_changed_rect = self.image_changed.get_rect(topleft= self.rect_new.topleft)
        self.screen.blit(self.image_changed,self.image_changed_rect)
        # print('rotate',self.angle_degree,'rect',self.image_changed_rect )
        self.i += 1
        if self.is_stretch:
            self.flower_stretch()

    def count_rect(self,pointAx,pointAy,angle_degree,w = 89, h = 30):
        ''' give pointA(image's topright point) and angle, count the rect of the surface '''
        if self.angle_degree in range(0,90):
            self.angle = self.angle_degree * pi/180
            x1 = self.pointAx - w * cos(self.angle)
            y1 = self.pointAy
        elif self.angle_degree in range(90,180):
            self.angle = (self.angle_degree - 90) * pi/180
            x1 = self.pointAx
            y1 = self.pointAy - h * sin(self.angle)
        elif self.angle_degree in range(180,270):
            self.angle = self.angle_degree * pi/180
            x1 = self.pointAx + h * sin(self.angle)
            y1 = self.pointAy + h * cos(self.angle) + w * sin(self.angle)
        elif self.angle_degree in range(270,361):
            self.angle = self.angle_degree * pi/180
            x1 = self.pointAx + h * sin(self.angle) - w * cos(self.angle)
            y1 = self.pointAy + w * sin(self.angle)
        rect = pygame.Rect(x1, y1, w, h)
        return rect
        
    def flower_stretch(self):
        action_num = 4
        print(self.i)
        def change(image_name):
            self.image = pygame.image.load(image_name)
            w,h = self.image.get_rect().width,self.image.get_rect().height
            self.rect_new = self.count_rect(self.pointAx,self.pointAy,self.angle_degree,w,h)
        if self.i%action_num == 0:
            image_name = 'images\\clock\\clock_flower1.jpg'
            change(image_name)
        elif self.i%action_num == 1:
            image_name = 'images\\clock\\clock_flower2.jpg'
            change(image_name)
        elif self.i%action_num == 2:
            image_name = 'images\\clock\\clock_flower3.jpg'
            change(image_name)
        elif self.i%action_num == 3:
            image_name = 'images\\clock\\clock_flower2.jpg'
            change(image_name)
            self.is_stretch = False

if __name__ == '__main__':
    game = MainWindow()
    game.start_game()
