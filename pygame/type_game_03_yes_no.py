# A pygame minimum frame, help to build a new pygame program 
import pygame
import sys
import random
import pygame.freetype

WIN_X = 300
WIN_Y = 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
GOLD = 255, 251, 0
RED = pygame.Color('red')
GREEN = 0, 255, 0
BLUE = 0, 0, 255
YELLOW = pygame.Color('yellow')
color_list = [ WHITE, GOLD, RED, GREEN, BLUE, YELLOW]
color = color_list[random.randint(0,len(color_list)-1)]
fps = 200
fclock = pygame.time.Clock()

title_name = 'new pygame'
init_result = pygame.init()

# Create a window
screen = pygame.display.set_mode((WIN_X,WIN_Y))
screen.fill(BLACK)
pygame.display.update()
# Set title
pygame.display.set_caption(title_name)
pos = [100,50]
alphabet_list = 'abcdefghijklmnopqrstuvwxyz'

# font = pygame.font.Font(None, 50)
font_size = 50
font = pygame.freetype.Font(None, font_size)
letter = alphabet_list[random.randint(0,25)]
# status --> 'waiting' waiting for type; 'yes': right type; 'wrong': wrong type
status = 'waiting'
yes = 0
while True:
    if pos[1] >= WIN_Y:
        status = 'waiting'
        # pos y is random
        pos[0] = random.randint(0,WIN_X-font_size)
        pos[1] = 0
        letter = alphabet_list[random.randint(0,25)]
        color = color_list[random.randint(0,len(color_list)-1)]
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            print ('BYE-BYE')
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print ('BYE-BYE')
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode and status != 'yes':
                # type right
                if event.unicode == letter:
                    status = 'yes' 
                    print('yes')
                else:
                    status = 'wrong'
                    print('wrong',event.unicode)

    if status == 'yes':
        font_surf, font_rect = font.render('YES',color,size = 30)
        yes += 1
        if yes >= 100:
            pos[1] = WIN_Y
            yes = 0
    elif status == 'waiting':
        font_surf, font_rect = font.render(letter,color)
    elif status == 'wrong':
        font_surf, font_rect = font.render('NO-'+letter,color,size = 30)
    screen.fill(BLACK)
    pos[1] += 1
    screen.blit(font_surf,(pos[0],pos[1]))
    pygame.display.update()
        
    fclock.tick(fps)
