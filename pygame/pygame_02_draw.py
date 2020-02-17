# https://www.cnblogs.com/xiaowuyi/archive/2012/06/06/2538921.html
import pygame,sys
import time
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))

pygame.display.update()

# draw a circle,args:1,surface;2,color;3,position of the center;4,radius;5,width
pygame.draw.circle(screen,(255,0,0),(200,200),30,9)
pygame.display.update()
# rectangle,args:1,surface;2,color;3,(left,top,width,height);4,width
pygame.draw.rect(screen,(0,255,0),(250,250,100,30),3)
pygame.display.update()

pygame.draw.lines(screen,(0,255,255),False,((100,190),(300,300),(10,10)),1)
pygame.display.update()
time.sleep(2)
