# A pygame minimum frame, help to build a new pygame program 
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
        self.fps = 30
        self.fclock = pygame.time.Clock()

        title_name = 'new pygame'
        init_result = pygame.init()

        # Create a window
        self.screen = pygame.display.set_mode((SCREEN_RECT.width, SCREEN_RECT.height))
        self.screen.fill(self.color_list[0])
        pygame.display.update()
        # Set title
        pygame.display.set_caption(title_name)
        self.__creat_sprite()

    def __creat_sprite(self):
#        self.head = Head(self.screen, (0, 0, 50, 50))
        self.head = Head()
        self.head_group = pygame.sprite.Group(self.head)
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ('BYE-BYE')
                pygame.quit()
                sys.exit()
    def __update_sprite(self):
        self.head_group.update()
        self.head_group.draw(self.screen)

    def start_game(self):
        while True:
            self.fclock.tick(self.fps)
            self.__event_handler()
            self.screen.fill(self.color_list[0])
            self.__update_sprite()
            pygame.display.update()

class Snake(pygame.sprite.Sprite):
    def __init__(self,image_name):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
#        self.color = 255, 255, 255
#        self.rect = rect
#        self.screen = screen

    def update(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.rect.x += 1

class Head(Snake):
    def __init__(self ):
        super().__init__('images\\snake\\snake.png')


if __name__ == '__main__':
    game = MainWindow()
    game.start_game()
