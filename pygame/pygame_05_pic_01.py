from pygame_00_base_frog import *
import sys

pygame.init()
screen = pygame.display.set_mode((800,800))
screen.fill((255,255,255))
fog = Draw(screen)
length = 130
color = 255,255,255
x = 400
y = 400
angle = 0
st = 0.5
png = pygame.image.load(r'D:\我的文件夹\桌面\pictures\1234567890.png').convert()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    x, y = pygame.mouse.get_pos()
    screen.blit(png,(x,y))
    pygame.display.update()
