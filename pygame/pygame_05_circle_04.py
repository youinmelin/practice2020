from pygame_00_base_frog import *

pygame.init()
screen = pygame.display.set_mode((800,800))
screen.fill((255,255,255))
pygame.display.update()
frog = Draw(screen)
length = 300
x = 400
y = 300
r = 5
angle_a = 5
angle_b = 40
st = 0.1
num = 8
color = (255,0,0)
for j in range(num*2):
    r += 15
    for i in range(num):
        # frog.arc(r,x,y,angle_a,angle_b,5,st=st)
        frog.arc(r,x,y,angle_a,angle_b,5,color=color,st=st,center=True)
        angle_a += 360/num +5
        angle_b += 360/num +5

time.sleep(10)
