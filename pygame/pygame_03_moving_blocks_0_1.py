import pygame
import sys
import time

window_x = 300
window_y = 300
pygame.init()
screen = pygame.display.set_mode((window_x,window_y))
screen.fill((255,255,255))
pygame.display.update()

rect_color = 0,255,0
rect_x = 100
rect_y = 200
rect_sidey = 20
rect_sidex = 15
rect_width = 0
rect_move_x = 3
rect_move_y = -3
my_font = pygame.font.Font(None,30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255,255,255))
    time.sleep(0.1)

    rect_x += rect_move_x
    rect_y += rect_move_y

    text_content = str(rect_x) +', '+ str(rect_y)
    text_color = 0,0,0
    text_image = my_font.render(text_content,True,text_color)
    screen.blit(text_image,(0,0))

    if rect_x > window_x-rect_sidey or rect_x < 0:
        rect_move_x = -rect_move_x
    if rect_y > window_y-rect_sidex or rect_y < 0:
        rect_move_y = -rect_move_y

    rect_arg = rect_x,rect_y,rect_sidey,rect_sidex
    print(rect_x,rect_y)
    pygame.draw.rect(screen,rect_color,rect_arg,rect_width)
    pygame.display.update()
