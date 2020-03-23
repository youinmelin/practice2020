from pygame_00_base_frog import *
import pygame
import sys

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

class MainWindow():
    def __init__(self):

        BLACK = 0, 0, 0
        WHITE = 255, 255, 255
        GOLD = 255, 251, 0
        RED = pygame.Color('red')
        GREEN = 0, 255, 0
        BLUE = 0, 0, 255
        YELLOW = pygame.Color('yellow')
        self.color_list = [BLACK, WHITE, GOLD, RED, GREEN, BLUE, YELLOW]
        self.fps = 10
        self.fclock = pygame.time.Clock()

        title_name = 'new pygame'
        init_result = pygame.init()

        # Create a window
        self.screen = pygame.display.set_mode((SCREEN_RECT.width, SCREEN_RECT.height))
        self.screen.fill(self.color_list[1])
        pygame.display.update()
        # Set title
        pygame.display.set_caption(title_name)
        self.r = 150

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ('BYE-BYE')
                pygame.quit()
                sys.exit()

    def start_game(self):
        while True:
            self.__event_handler()
            self.fclock.tick(self.fps)
            self.draw()
            self.r += 10
            time.sleep(0.1)
            # self.screen.fill(self.color_list[1])
            pygame.display.update()

    def draw(self):
        tu = Draw(self.screen)
        x = 10
        y = 350
        num = 3
        angle1 = 0
        for i in range(3):
            angle = i * (180-180/num) 
            tu.arc(self.r,x,y,angle ,angle+(180/num)+1,5,(255,0,0),st = 0,center = True)
            x,y = tu.line(self.r,x,y,angle,color=(255,255,255),st=0)



if __name__ == '__main__':
    game = MainWindow()
    game.start_game()
