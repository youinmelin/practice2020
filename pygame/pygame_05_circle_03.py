from pygame_00_base_frog import *

pygame.init()
screen = pygame.display.set_mode((800,800))
screen.fill((255,255,255))
pygame.display.update()
frog = Draw(screen)
length = 300
x = 600
y = 300
r = 200
r2 = 100
angle_a = 0
angle_b = 45
st = 0.1
num = 6
color = (255,0,0)
for i in range(num):
    # frog.arc(r,x,y,angle_a,angle_b,5,st=st)
    frog.arc_e(r,r2,x,y,angle_a,angle_b,5,color=color,st=st)
    angle_a += 360/num
    angle_b += 360/num

time.sleep(10)
