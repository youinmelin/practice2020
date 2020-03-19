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
        self.fps = 10
        self.fclock = pygame.time.Clock()

        title_name = 'new pygame'
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
        self.grow = 9
        self.start_point_x = 135
        self.start_point_y = 430
        self.flist = []
        self.fdict = {}
        self.create_dial_plate()

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
        r = 0
        while True:
            self.__event_handler()
            self.fclock.tick(self.fps)
            self.screen.fill(self.color_list[1])
            # self.stretch()
            # self.rotate()
            self.run_dial_plate()
            r += 1
            r = 0 if r>=60 else r
            # self.stretch(self.fdict[f'flower{r}'])
            pygame.display.update()

    def create_dial_plate(self):
        for i in range(60):
            self.angle += 6
            self.angle = 0 if self.angle>=360 else self.angle
            self.fdict[f'flower{i}'] =  Clock(self.screen,(self.start_point_x,self.start_point_y),self.size,self.angle)
            # draw lines to guide the pictures
            self.start_point_x,self.start_point_y = self.line(self.size[1],self.start_point_x,self.start_point_y,self.angle)
            # print(f'flower{i}',self.fdict[f'flower{i}'])

    def run_dial_plate(self):
        for i in range(60):
            self.fdict[f'flower{i}'].draw_flower()
        

    def line(self,length,x=0,y=0,angle_a = 270,color=(255,255,255)):
        x2 = x + length*(sin(angle_a * pi/180))
        y2 = y + length*(sin((90-angle_a) * pi/180))
        pygame.draw.line(self.screen,color,(x,y),(x2,y2),7)
        return x2,y2

    def stretch(self,clock_object):
        if self.size[0] > 120 or self.size[0] < 80: 
            self.grow *= -1
        self.size[0] += self.grow
        print(clock_object)
        clock_object.flower_stretch()
        clock_object.draw_flower()

class Clock():
    def __init__(self,screen,pointA, image_size,angle,topright = (200,130)):
        self.screen = screen
        self.topright = topright
        self.angle_degree = angle
        self.pointAx = pointA[0]
        self.pointAy = pointA[1]
        image_name = 'images\\clock\\clock_flower2.jpg'
        # type(self.image) --> pygame.Surface
        self.size = image_size
        self.image = pygame.image.load(image_name)

    def draw_flower(self):

        # anticlockwise ( not clockwise )
        # create a new variable to save image rotated
        rect_new = self.count_rect(100,100,self.angle_degree)
        self.image_changed = pygame.transform.rotozoom(self.image, self.angle_degree,1)
        self.image_changed_rect = self.image_changed.get_rect(topleft= rect_new.topleft)
        self.screen.blit(self.image_changed,self.image_changed_rect)
        # print('rotate',self.angle_degree,'rect',self.image_changed_rect )

    def count_rect(self,pointAx,pointAy,angle_degree):
        ''' give pointA(image's topright point) and angle, count the rect of the surface '''
        w = self.size[0]
        h = self.size[1]
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
        self.image_changed = pygame.transform.scale(self.image,self.size)
        self.image_changed_rect = self.image_changed.get_rect(topright = self.topright)
        
if __name__ == '__main__':
    game = MainWindow()
    game.start_game()
