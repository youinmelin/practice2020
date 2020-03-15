# snake_06 completed the snake body function basically. 1.become longer 2.turn direction controlled by keys 3.body's blocks follow the previous block. Use the function of shallow copy
# snake_07 expected: edge control
# snake_08 expected: collide detect
# snake_09 expected: eat and grow

import pygame
import sys
import copy
import random

SCREEN_RECT = pygame.Rect(0, 0, 300, 300)

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
        self.fps = 3
        self.fclock = pygame.time.Clock()

        title_name = 'SNAKE'
        init_result = pygame.init()

        # Create a window
        self.screen = pygame.display.set_mode((SCREEN_RECT.width, SCREEN_RECT.height))
        self.screen.fill(self.color_list[0])
        pygame.display.update()
        # Set title
        pygame.display.set_caption(title_name)
        self.direction = 'right'
        self.snake_size = 9
        # build a list, every block of the snake is in the list. In this list,each item will be [ the object of the snake head or body, the rect object].
        self.snake_list = []
        self.collide = False
        self.__create_snake(self.snake_size+1)
        self.score = 0
        self.eaten = False
        self.food_x = random.randint(0,SCREEN_RECT.width/10-1)*(self.snake_size+1)
        self.food_y = random.randint(0,SCREEN_RECT.width/10-1)*(self.snake_size+1)

    def __create_snake(self, speed = 11):
        # create head
        if not self.snake_list :
            head_rect = pygame.Rect(0,0,self.snake_size,self.snake_size)
            self.head = Head(self.screen, head_rect, speed)
            self.snake_list.append((self.head, self.head.rect))
        # create body
        else:
            # print(self.snake_list[-1].rect)
            self.snake_body = Snake(self.screen,self.snake_list[-1][1]) 
            self.snake_list.append((self.snake_body, self.snake_body.rect))

    def __update_snake(self):

        for e, (snake,rect) in enumerate(self.snake_list):
            if e == 0:
                print('move head')
                # this snake is a head object
                snake.update(self.direction,'useless rect')
            else:
                print('move body',e)
                rect_pre = self.snake_list[e-1][0].rect_pre
                # print('---------------',rect_pre,self.collide)
                # this snake is a body object
                snake.update(self.direction,rect_pre)

    def __collide(self):
        if len(self.snake_list) > 1: 
            for e,(snake,rect) in enumerate(self.snake_list):
                # print(self.collide)
                if pygame.Rect.colliderect(self.head.rect, snake.rect) and e > 1:
                    self.collide = True
                    break    

    def __edge_detect(self):
        self.__collide()
        if self.head.rect.right > SCREEN_RECT.width:
            print('over')
            self.collide = True
        if self.head.rect.left < 0 :
            print('over')
            self.collide = True
        if self.head.rect.top < 0 :
            print('over')
            self.collide = True
        if self.head.rect.bottom > SCREEN_RECT.height:
            print('over')
            self.collide = True

    def __add_snake(self):
        print('add')
        self.score += 1
        self.__create_snake()

    def __food(self):
        if self.eaten:
            self.food_x = random.randint(0,SCREEN_RECT.width/10-1)*(self.snake_size+1)
            self.food_y = random.randint(0,SCREEN_RECT.width/10-1)*(self.snake_size+1)
            self.eaten = False
        # food_rect = pygame.draw.rect(self.screen,self.color_list[2],(self.food_x,self.food_y,self.snake_size,self.snake_size))
        food_rect = pygame.draw.circle(self.screen,self.color_list[2],pygame.Rect(self.food_x,self.food_y,self.snake_size,self.snake_size).center,int(self.snake_size/2))
        food_collide = pygame.Rect.colliderect(self.head.rect, food_rect)
        if food_collide:
            self.__add_snake()
            self.eaten = True

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
                # get the direction from the key event, cann't turn back directly.
                elif event.key == pygame.K_LEFT and self.direction != 'right':
                    self.direction = 'left'
                elif event.key == pygame.K_RIGHT and self.direction != 'left':
                    self.direction = 'right'
                elif event.key == pygame.K_UP and self.direction != 'down':
                    self.direction = 'up'
                elif event.key == pygame.K_DOWN and self.direction != 'up':
                    self.direction = 'down'
                elif event.unicode:
                    # some shortcut keys. a:longer, f:fast, s:slow
                    if event.unicode == 'a':
                        self.__add_snake()
                    if event.unicode == 'f' and self.fps < 30:
                        self.fps += 2
                    if event.unicode == 's' and self.fps > 2:
                        self.fps -= 2
                    if event.unicode == 'r':
                        self.__init__()

    def show_score(self):
        score_str = f'score {self.score}'
        scorefont = pygame.font.Font(None, 25)
        scorefont_surf = scorefont.render(score_str,True, (0,255,0))
        self.screen.blit(scorefont_surf, (0,0))

    def __gameover(self):
        gameover_str = 'GAME OVER'
        tip_str = 'ESC to quit. r to restart.'
        # tip_str = f'score {self.score}'
        
        bigfont = pygame.font.Font(None, 30)
        bigfont_surf = bigfont.render(gameover_str,True, (255,0,0))
        bigfont_rect = bigfont_surf.get_rect()
        bigfont_rect.centerx = SCREEN_RECT.centerx
        bigfont_rect.centery = SCREEN_RECT.height * 1 / 3

        smallfont = pygame.font.Font(None, 30)
        smallfont_surf = smallfont.render(tip_str,True, (255,0,0))
        smallfont_rect = smallfont_surf.get_rect()
        smallfont_rect.centerx = SCREEN_RECT.centerx
        smallfont_rect.centery = SCREEN_RECT.height * 2 / 3

        self.screen.blit(bigfont_surf, (bigfont_rect.x,bigfont_rect.y))
        self.screen.blit(smallfont_surf, (smallfont_rect.x,smallfont_rect.y))

    def start_game(self):
        while True:
            self.fclock.tick(self.fps)
            self.__event_handler()
            self.screen.fill(self.color_list[0])
            self.__food()
            if not self.collide:
                self.__update_snake()
            elif self.collide:
                self.__gameover()
            self.__edge_detect()
            self.show_score()
            pygame.display.update()

class Snake():
    def __init__(self, screen, rect):
        self.color = 255, 255, 255
        self.rect = rect
        self.rect_pre = rect 
        self.screen = screen

    def update(self,direction,rect): # direction is useless
        # Use the function of shallow copy to make sure self.rect_pre don't change with self.rect
        self.rect_pre = copy.copy(self.rect)
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

    def update(self,direction,rect): # rect is useless
        # Use the function of shallow copy to make sure self.rect_pre don't change with self.rect.(deep copy is OK too in here)
        self.rect_pre = copy.copy(self.rect)
        # print (id(self.rect_pre),id( self.rect))
        if direction == 'left':
            print('left')
            self.rect.x -= self.speed
        elif direction == 'right':
            print('right')
            self.rect.x += self.speed
        elif direction == 'up':
            print('up')
            self.rect.y = self.rect.y - self.speed
            print(f'{self.rect.y} - {self.speed}')
            print(f'{self.rect.y} ')
        elif direction == 'down':
            print('down')
            self.rect.y += self.speed
        snake_rect = pygame.draw.rect(self.screen, self.color, self.rect)
        # print (snake_rect)


if __name__ == '__main__':
    game = MainWindow()
    game.start_game()
