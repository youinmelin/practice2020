from pygame_00_base_fog import *

pygame.init()
screen = pygame.display.set_mode((800,800))
fog = Draw(screen)
length = 130
color = 255,255,255
x = 400
y = 400
angle = 0
st = 0.5
# fog.circle(length,x,y,angle,st = st)
for i in range(1,31):
    angle += 12
    length = int (length)
    # screen.fill((0,0,0))
    pygame.draw.circle(screen,color,(x,y),5,0)
    # pygame.display.update()
    fog.circle(length-5*i,x,y,angle,st = st)

