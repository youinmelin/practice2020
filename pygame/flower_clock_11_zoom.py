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
        self.fps = 30
        self.fclock = pygame.time.Clock()

        title_name = 'clock'
        init_result = pygame.init()
        print('init_result',init_result)

        # Create a window
        self.screen = pygame.display.set_mode((SCREEN_RECT.width, SCREEN_RECT.height))
        self.screen.fill(self.color_list[1])
        pygame.display.update()
        # Set title
        pygame.display.set_caption(title_name)
        # set parameters
        self.initial_set(60)

    def initial_set(self,num = 60):
        ''' set initial parameters '''
        self.angle = 0
        # size[0]:width, size[1]:height
        self.size = [89, 30]
        self.flist = []
        self.start_point_x = 135
        self.start_point_y = 430
        self.flowers_num = num
        # number of flowers must be divisible by 360 and less than 60
        while 360 % self.flowers_num or self.flowers_num > 60:
            self.flowers_num -= 1
        # c = circumference
        c = self.flowers_num * self.size[1]
        # give center point 421 415, then count start_point
        self.start_point_x = int(421 - c/(2 * pi))
        print(self.start_point_x)
        print(self.flowers_num)
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
                if event.key == pygame.K_DOWN:
                    if  self.flowers_num > 15:
                        self.flowers_num -=1
                    self.initial_set(self.flowers_num)
                if event.key == pygame.K_UP:
                    self.flowers_num += 1
                    while 360 % self.flowers_num:
                        self.flowers_num += 1
                    self.initial_set(self.flowers_num)

    def start_game(self):
        while True:
            self.__event_handler()
            self.fclock.tick(self.fps)
            self.screen.fill(self.color_list[1])
            self.create_dial_plate()
            self.stretch()
            self.flower_group.update()
            pygame.display.update()


    def create_sprites(self):
        self.flower_group = pygame.sprite.Group()
        # create_dial_plate
        for i in range(self.flowers_num):
            self.angle = 0 if self.angle>=360 else self.angle
            self.angle += int(360/self.flowers_num)
            flower_sprite =  Clock(self.screen,(self.start_point_x,self.start_point_y),self.size,self.angle)
            # draw lines to guide the pictures
            self.start_point_x,self.start_point_y = self.line(self.size[1],self.start_point_x,self.start_point_y,self.angle)
            self.flower_group.add(flower_sprite) 
            self.flist.append(flower_sprite)
        # print(flower_sprite.rect_new.x,flower_sprite.rect_new.y)
        # print(dir(self.flower_group))
        print(self.flist[0].rect_new.topright,self.flist[int(self.flowers_num/2)-1].rect_new.bottomleft)
        # count center point
        self.diameter = self.flist[int(self.flowers_num/2)-1].rect_new.bottomleft[0] - self.flist[0].rect_new.topright[0]
        self.centerx = self.diameter / 2 + self.flist[0].rect_new.topright[0]
        self.centery = self.flist[0].rect_new.top - self.size[1]/2
        print('center point',self.centerx,self.centery)

    def line(self,length,x=0,y=0,angle_a = 270,color=(255,0,255)):
        ''' draw a polygon to guide the circle, x2,y2 are the last point in every line '''
        x2 = x + length*(sin(angle_a * pi/180))
        y2 = y + length*(sin((90-angle_a) * pi/180))
        pygame.draw.line(self.screen,color,(x,y),(x2,y2),7)
        return x2,y2

    def create_dial_plate(self):
        dial_pic = 'images/clock/dial_plate.png'
        self.dial_image = pygame.image.load(dial_pic)
        rate = self.diameter / 600
        self.dial_image = pygame.transform.rotozoom(self.dial_image, 0 , rate)
        self.dial_rect = self.dial_image.get_rect()
        self.dial_rect.centerx = self.centerx 
        self.dial_rect.centery = self.centery
        self.screen.blit(self.dial_image,self.dial_rect)
        pygame.draw.circle(self.screen,self.color_list[3],self.dial_rect.center,7)

    def stretch(self):
        ''' stretch the flower to let it change width '''
        self.count = 0 if self.count >= self.flowers_num else self.count
        self.flist[self.count].is_stretch = 2
        pre = self.count - 1 if self.count >= 0 else self.flowers_num - 1
        self.flist[pre].is_stretch = 1
        aft = self.count + 1 if self.count < self.flowers_num-1 else 0
        self.flist[aft].is_stretch = 3
        pre2 = self.count - 2 if self.count > 1 else self.flowers_num + self.count-2
        self.flist[pre2].is_stretch = 0
        self.count += 1

class Clock(pygame.sprite.Sprite):
    def __init__(self,screen,pointA, image_size,angle,is_stretch = 0):
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
        self.flower_stretch()
        self.image_changed = pygame.transform.rotozoom(self.image, self.angle_degree,1)
        self.image_changed_rect = self.image_changed.get_rect(topleft= self.rect_new.topleft)
        self.screen.blit(self.image_changed,self.image_changed_rect)
        # print('rotate',self.angle_degree,'rect',self.image_changed_rect )

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
        def change(image_name):
            self.image = pygame.image.load(image_name)
            w,h = self.image.get_rect().width,self.image.get_rect().height
            self.rect_new = self.count_rect(self.pointAx,self.pointAy,self.angle_degree,w,h)
        if self.is_stretch == 0:
            image_name = 'images\\clock\\clock_flower1.jpg'
            change(image_name)
        elif self.is_stretch  == 1:
            image_name = 'images\\clock\\clock_flower2.jpg'
            change(image_name)
        elif self.is_stretch  == 2:
            image_name = 'images\\clock\\clock_flower3.jpg'
            change(image_name)
        elif self.is_stretch  == 3:
            image_name = 'images\\clock\\clock_flower2.jpg'
            change(image_name)

if __name__ == '__main__':
    game = MainWindow()
    game.start_game()
