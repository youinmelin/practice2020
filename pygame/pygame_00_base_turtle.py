import pygame
import math
import time

class Draw:
    def __init__(self,surface):
        self.surface = surface
    
    def line(self,length,x=0,y=0,angle_a = 0,color=(255,0,0),st = 0):
        angle_a += 90
        x2 = x + length*(math.sin(angle_a*math.pi/180))
        y2 = y + length*(math.sin((90-angle_a)*math.pi/180))
        pygame.draw.aaline(self.surface,color,(x,y),(x2,y2), 90)
        pygame.display.update()
        time.sleep(st)
        angle_a += 90
        return x2,y2,angle_a

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    screen.fill((255,255,255))

    x = 300
    y = 350
    color = 255,0,0
    length = 100
    angle_a = 0
    sleep_time = 1
    tt = Draw(screen)
    x,y,angle_a = tt.line(length,x,y,angle_a,st=1)
    x,y,angle_a = tt.line(length,x,y,angle_a+60,st=1)
    x,y,angle_a = tt.line(length,x,y,angle_a+60,st=1)

    # angle_a = angle_a + 90
    # x2 = x + length*(math.sin(angle_a*math.pi/180))
    # y2 = y + length*(math.sin((90-angle_a)*math.pi/180))
    # print(x,y,x2,y2)
    # pygame.draw.aaline(screen,color,(x,y),(x2,y2), 90)
    # pygame.draw.circle(screen,color,(x,y),2,0)
    # pygame.draw.aaline(screen,(255,0,0),(300,300),(500,400), 90)
    # pygame.draw.line(screen,(0,0,0),(400,300),(600,400),9)
    pygame.display.update()
    time.sleep(2)
if __name__ == "__main__":
    main()
