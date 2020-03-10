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
        self.__creat_snake()

    def __creat_snake(self):
        snake_size = 25
        speed = snake_size
        self.head = Head(self.screen, [0,0,snake_size,snake_size],speed)

    def __update_snake(self):

        self.head_rect = self.head.update()
        print (self.head_rect)

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ('BYE-BYE')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print ('BYE-BYE')
                    pygame.quit()
                    sys.exit()


    def start_game(self):
        while True:
            self.fclock.tick(self.fps)
            self.__event_handler()
            self.screen.fill(self.color_list[0])
            self.__update_snake()
            pygame.display.update()

class Snake():
    def __init__(self, screen, rect):
        self.color = 255, 255, 255
        self.rect = rect
        self.screen = screen

    def update(self):
        snake_rect = pygame.draw.rect(self.screen, self.color, self.rect)
        return  snake_rect

class Head(Snake):
    def __init__(self, screen, rect,speed):
        super().__init__(screen, rect)
        self.speed = speed
    def update(self):
        super().update()
        self.rect[0] += self.speed
        if self.rect[0] + self.rect[2] >= SCREEN_RECT.width:
            self.speed = -self.speed
            print (self.rect)


if __name__ == '__main__':
    game = MainWindow()
    game.start_game()
