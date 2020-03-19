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
        self.str_size = self.size[0] 
        self.fdict = {}
        self.create_sprites()

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
            # self.stretch(self.fdict[f'flower{r}'])
#            self.run_dial_plate()
            self.flower_group.update()
            pygame.display.update()

    def create_sprites(self):
        self.flower_group = pygame.sprite.Group()
        # create_dial_plate
        for i in range(60):
            self.angle += 6
            self.angle = 0 if self.angle>=360 else self.angle
            self.fdict[f'flower{i}'] =  Clock(self.screen,(self.start_point_x,self.start_point_y),self.size,self.angle)
            # draw lines to guide the pictures
            self.start_point_x,self.start_point_y = self.line(self.size[1],self.start_point_x,self.start_point_y,self.angle)
            self.flower_group.add(self.fdict[f'flower{i}'])

#    def run_dial_plate(self):
#        for f in self.fdict:
#            self.fdict[f].update()
        

    def line(self,length,x=0,y=0,angle_a = 270,color=(255,255,255)):
        x2 = x + length*(sin(angle_a * pi/180))
        y2 = y + length*(sin((90-angle_a) * pi/180))
        pygame.draw.line(self.screen,color,(x,y),(x2,y2),7)
        return x2,y2

    def stretch(self,clock_object):
        clock_object.flower_stretch(self.str_size)

class Clock(pygame.sprite.Sprite):
    def __init__(self,screen,pointA, image_size,angle,topright = (200,130)):
        super().__init__()
        self.screen = screen
        self.topright = topright
        self.angle_degree = angle
        self.pointAx = pointA[0]
        self.pointAy = pointA[1]
        image_name = 'images\\clock\\clock_flower2.jpg'
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

    def count_rect(self,pointAx,pointAy,angle_degree,w = 89, h = 30):
        ''' give pointA(image's topright point) and angle, count the rect of the surface '''
        # w = self.size[0]
        # h = self.size[1]
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
        
    def flower_stretch(self,str_size):

        if self.i%2 == 1:
            image_name = 'images\\clock\\clock_flower2.jpg'
            self.image = pygame.image.load(image_name)
            self.rect_new = self.count_rect(self.pointAx,self.pointAy,self.angle_degree)
            print(self.i)

        elif self.i%2 == 0:
            image_name = 'images\\clock\\clock_flower3.jpg'
            self.image = pygame.image.load(image_name)
            w,h = self.image.get_rect().width,self.image.get_rect().height
            self.rect_new = self.count_rect(self.pointAx,self.pointAy,self.angle_degree,w,h)
            print(self.i)

        
if __name__ == '__main__':
    game = MainWindow()
    game.start_game()
