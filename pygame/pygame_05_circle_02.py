from pygame_00_base_frog import *

pygame.init()
screen = pygame.display.set_mode((800,800))
# screen.fill((255,255,255))
# pygame.display.update()
frog = Draw(screen)
length = 300
x = 400
y = 400
angle = 0
st = 0.01
num = 99 
color = (255,0,0)
for i in range(1,num):
    angle += 8
    color_list = [(255,0,0),(255,255,0),(0,255,0)]
    j = i % (len(color_list))
    # screen.fill((0,0,0))
    # pygame.display.update()
    # x,y = fog.line(length,x,y,angle,st = st)
    frog.circle(i,x,y,angle,1,color,st = st)
    frog.circle(3 * i, x, y, angle, 1, color, st=st, center=True)

time.sleep(10)
