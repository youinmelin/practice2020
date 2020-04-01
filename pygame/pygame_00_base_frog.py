# from pygame_00_base_frog import *
import pygame
import math
import time

class Draw:
    def __init__(self,surface):
        self.surface = surface
    
    def line(self,length,x=0,y=0,angle_a = 0,color=(255,0,0),width = 0, st = 0):
        '''right:angle_a=0,top:angle_a=90,left:angle_a=180,bottom:angle_a=270 or -90
            :return x2,y2 is the end of point
        '''
        angle_a += 90
        x2 = x + length*(math.sin(angle_a*math.pi/180))
        y2 = y + length*(math.sin((90-angle_a)*math.pi/180))
        pygame.draw.line(self.surface,color,(x,y),(x2,y2), width )
        # pygame.display.update()
        time.sleep(st)
        return x2,y2

    def aaline(self,length,x=0,y=0,angle_a = 0,color=(255,0,0),st = 0):
        '''right:angle_a=0,top:angle_a=90,left:angle_a=180,bottom:angle_a=270 or -90
            :return x2,y2 is the end of point
        '''
        angle_a += 90
        x2 = x + length*(math.sin(angle_a*math.pi/180))
        y2 = y + length*(math.sin((90-angle_a)*math.pi/180))
        pygame.draw.aaline(self.surface,color,(x,y),(x2,y2), 90)
        pygame.display.update()
        time.sleep(st)
        return x2,y2

    def circle(self,r,x,y,angle_a = 0,width =1,color=(0,0,0),st = 0,center = False):
        ''' draw a circle'''
        angle_a += 90
        r = int(r)
        if r < width:
            print ('ERROR: width can not greater than radius')
            r = width
        # center is False: x,y are the rightmost point.
        # center is True: x,y are the center point.
        if center == False:
            center_x = int(x + r*(math.cos(angle_a*math.pi/180)))
            center_y = int(y + r*(math.sin(angle_a*math.pi/180)))
        else:
            center_x = x
            center_y = y
        pygame.draw.circle(self.surface,color,(center_x,center_y),r,width)
        pygame.display.update()
        time.sleep(st)

    def arc_e(self,r1,r2,x,y,angle_a,angle_b,width=1,color=(0,0,0),st = 0):
        ''' 
            draw an ellipse
            r1:an ellipse's long side
            r2:an ellipse's short side
            x,y:ellipse's rightmost point
            angle_a:arc's start angle,right->0,top->90,left->180,bottom->270
        '''
        rect = x-2*r1,y-r2,2*r1,2*r2
        start_angle = angle_a*math.pi/180
        stop_angle = angle_b*math.pi/180
        pygame.draw.arc(self.surface,color,rect,start_angle,stop_angle,width)
        pygame.display.update()
        time.sleep(st)
        center_x = x - r1
        center_y = y 
        x2 = r1 * math.cos(angle_b*math.pi/180) + center_x
        y2 = -r2 * math.sin(angle_b*math.pi/180) + center_y
        return x2,y2

    def arc(self,r,x,y,angle_a,angle_b,width=1,color=(0,0,0),st = 0,center = False):
        ''' r:radius
            if center is False: x,y are the rightmost point
            angle_a:circle's start angle
            right->0,top->90,left->180,bottom->270
        '''
        if r < width:
            print ('ERROR: width can not greater than radius')
            r = width
        if center == False:
            rect = x-2*r,y-r,2*r,2*r
            center_x = x - r
            center_y = y
        else:
            rect = x-r,y-r,2*r,2*r
            center_x = x 
            center_y = y
        start_angle = angle_a*math.pi/180
        stop_angle = angle_b*math.pi/180
        pygame.draw.arc(self.surface,color,rect,start_angle,stop_angle,width)
        pygame.display.update()
        time.sleep(st)
        # print(center_x,center_y)
        x2 = r * math.cos(stop_angle) + center_x -r
        y2 = -r * math.sin(stop_angle) + center_y
        return x2,y2

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    screen.fill((255,255,255))

    x = 300
    y = 300
    color = 255,0,0
    length = 50
    length2 = 10
    angle_a = 90
    sleep_time = 2
    tt = Draw(screen)
    x,y = tt.line(length,x,y,angle_a,st=sleep_time)
    print(x,y)
    tt.circle(3,x,y,width = 3)
    x,y = tt.arc(length,x,y,0,45,color=color,st=sleep_time,center=True)
    tt.circle(3,x,y,width = 3)
    x,y = tt.arc(length,x,y,0,30,color=color,st=sleep_time,center=True)
    tt.circle(3,x,y,width = 3)
    x,y = tt.arc(length,x,y,0,90,color=color,st=sleep_time,center=True)
    print(x,y)
    # x,y = tt.arc_e(length,length2,x,y,0,180,color=color,st=sleep_time)
    # tt.circle(3,x,y,width = 3)
    # x,y = tt.arc_e(length,length2,x,y,0,145,color=color,st=sleep_time)
    # tt.circle(3,x,y,width = 3)
    # x, y = tt.arc_e(length, length2, x, y, 0, 90, color=color, st=sleep_time)
    # tt.circle(3, x, y, width=3)
#    print(x,y)
    # angle_a = angle_a + 90
    # x2 = x + length*(math.sin(angle_a*math.pi/180))
    # y2 = y + length*(math.sin((90-angle_a)*math.pi/180))
    # print(x,y,x2,y2)
    # pygame.draw.aaline(screen,color,(x,y),(x2,y2), 90)
    # pygame.draw.circle(screen,color,(x,y),2,0)
    # pygame.draw.aaline(screen,(255,0,0),(300,300),(500,400), 90)
    # pygame.draw.line(screen,(0,0,0),(400,300),(600,400),9)
    # pygame.display.update()
    time.sleep(2)
if __name__ == "__main__":
    main()
