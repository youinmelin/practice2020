from pygame_00_base_frog import *
import sys

pygame.init()
screen = pygame.display.set_mode((800,800))
fog = Draw(screen)
length = 300
x = 400
y = 400
angle = 90
# st: sleep time
st = 0.5
fog.line(length,x,y,angle,st = st)
while True:
    for i in range(0,60):
        angle = i * 6
        screen.fill((0,0,0))
        # pygame.display.update()
        fog.line(length,x,y,angle,st = st)
        print(angle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ('BYE-BYE')
                pygame.quit()
                sys.exit()

