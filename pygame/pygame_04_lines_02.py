from pygame_00_base_fog import *

pygame.init()
screen = pygame.display.set_mode((800,800))
# screen.fill((255,255,255))
# pygame.display.update()
fog = Draw(screen)
length = 300
x = 400
y = 400
angle = 0
st = 0.01
num = 900
for i in range(1,num):
    angle += 89
    color_list = [(255,0,0),(255,255,0),(0,255,0),(0,255,255)]
    j = i % (len(color_list))
    # screen.fill((0,0,0))
    # pygame.display.update()
    # x,y = fog.line(length,x,y,angle,st = st)
    x,y = fog.line(i,x,y,angle,color_list[j],st = st)

time.sleep(10)
