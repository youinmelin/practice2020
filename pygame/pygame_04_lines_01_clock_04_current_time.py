from pygame_00_base_frog import *
import sys
import datetime

pygame.init()
screen = pygame.display.set_mode((800,800))
fog = Draw(screen)
length_s = 300
length_m = 250 
length_h = 200
x = 400
y = 400
# angle = 90
# st: sleep time
st = 0
width = 5
# fog.line(length,x,y,angle,st = st)
while True:
    cur = datetime.datetime.now()
    angle_s = cur.second * -6
    angle_m = cur.minute * -6
    angle_h = cur.hour * -6
    screen.fill((0,0,0))
    fog.line(length_s,x,y,angle_s,st = st,width = width)
    fog.line(length_m,x,y,angle_m,st = st,width = width)
    fog.line(length_h,x,y,angle_h,st = st,width = width)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print ('BYE-BYE')
            pygame.quit()
            sys.exit()

