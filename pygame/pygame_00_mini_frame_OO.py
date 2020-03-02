# A pygame minimum frame, help to build a new pygame program 
import pygame
import sys

class MainWindow():
    def __init__(self):
        self.WIN_X = 800
        self.WIN_Y = 600

        BLACK = 0, 0, 0
        WHITE = 255, 255, 255
        GOLD = 255, 251, 0
        RED = pygame.Color('red')
        GREEN = 0, 255, 0
        BLUE = 0, 0, 255
        YELLOW = pygame.Color('yellow')
        self.color_list = [BLACK, WHITE, GOLD, RED, GREEN, BLUE, YELLOW]
        self.fps = 300
        self.fclock = pygame.time.Clock()

        title_name = 'new pygame'
        init_result = pygame.init()

        # Create a window
        self.screen = pygame.display.set_mode((self.WIN_X, self.WIN_Y))
        self.screen.fill(self.color_list[0])
        pygame.display.update()
        # Set title
        pygame.display.set_caption(title_name)

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print ('BYE-BYE')
                    pygame.quit()
                    sys.exit()
            self.fclock.tick(self.fps)

if __name__ == '__main__':
    game = MainWindow()
    game.start_game()
