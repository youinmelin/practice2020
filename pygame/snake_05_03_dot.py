# 
import pygame
import sys

SCREEN_RECT = pygame.Rect(0, 0, 500, 500)

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
        self.fps = 1
        self.fclock = pygame.time.Clock()

        title_name = 'new pygame'
        init_result = pygame.init()

        # Create a window
        self.screen = pygame.display.set_mode((SCREEN_RECT.width, SCREEN_RECT.height))
        self.screen.fill(self.color_list[0])
        pygame.display.update()
        # Set title
        pygame.display.set_caption(title_name)
        self.direction = 'right'
        self.snake_size = 10
        # build a list, every block of the snake is in the list
        self.snake_list = []
        self.__creat_snake()

    def __creat_snake(self, speed = 10):
        if not self.snake_list :
            self.head = Head(self.screen, [0,0,self.snake_size,self.snake_size],speed)
            self.snake_list.append(self.head)
        elif len(self.snake_list) >= 1:
            # print(self.snake_list[-1].rect)
            self.snake_body = Snake(self.screen,self.snake_list[-1].rect) 
            self.snake_list.append(self.snake_body)

    def __update_snake(self):

        # print(len(self.snake_list))
        for e, rect in enumerate(self.snake_list):
            if e == 0:
                print('move head')
                rect.update(self.direction,0)
            else:
                # print('move body',e)
                rect_pre = self.snake_list[e-1].rect
                print(rect_pre)
                rect.update(self.direction,rect_pre)
                

    def __add_snake(self):
        print('add')
        self.__creat_snake()

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
                # get the direction, from the key event
                elif event.key == pygame.K_LEFT:
                    self.direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    self.direction = 'right'
                elif event.key == pygame.K_UP:
                    self.direction = 'up'
                elif event.key == pygame.K_DOWN:
                    self.direction = 'down'
                elif event.unicode:
                    if event.unicode == 'a':
                        self.__add_snake()


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

    def update(self,direction,rect):
        # print(x,y)
        print('move body')
        self.rect = rect
        snake_rect = pygame.draw.rect(self.screen, self.color, self.rect)
        self.rect = snake_rect
        # print (snake_rect, self.rect)
        return snake_rect 

class Head(Snake):
    def __init__(self, screen, rect, speed ):
        super().__init__(screen, rect)
        self.speed = speed
        self.color = 255,0,0

    def update(self,direction,recti):
        # print(direction)
        if direction == 'left':
            self.rect[0] -= self.speed
        elif direction == 'right':
            self.rect[0] += self.speed
        elif direction == 'up':
            self.rect[1] -= self.speed
        elif direction == 'down':
            self.rect[1] += self.speed
        snake_rect = pygame.draw.rect(self.screen, self.color, self.rect)
        self.rect = snake_rect
        # print (snake_rect, self.rect)
        return snake_rect 


if __name__ == '__main__':
    game = MainWindow()
    game.start_game()
