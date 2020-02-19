from pygame_00_base_frog import *

pygame.init()
screen = pygame.display.set_mode((800,800))
fog = Draw(screen)
length = 300
x = 400
y = 400
angle = 0
st = 0.5
fog.line(length,x,y,angle,st = st)
for i in range(0,90):
    angle += 4
    screen.fill((0,0,0))
    pygame.display.update()
    fog.line(length,x,y,angle,st = st)

