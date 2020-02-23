from pygame_00_base_frog import *

pygame.init()
screen = pygame.display.set_mode((800,800))
screen.fill((255,255,255))
pygame.display.update()
frog = Draw(screen)
length = 300
x = 400
y = 400
r = 2
angle_a = 10
angle_b = 35
st = 0.01
num = 3
color = (255,0,0)
# loop number
for j in range(60):
    r += 7
    # cut number
    for i in range(num):
        # frog.arc(r,x,y,angle_a,angle_b,5,st=st)
        frog.arc(r,x,y,angle_a,angle_b,8,color=color,st=st,center=True)
        # twisting
        twisting = 3
        angle_a += 360/num + twisting
        angle_b += 360/num + twisting

time.sleep(1)
