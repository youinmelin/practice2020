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
        self.fps = 10
        self.fclock = pygame.time.Clock()

        title_name = 'new pygame'
        init_result = pygame.init()

        # Create a window
        self.screen = pygame.display.set_mode((SCREEN_RECT.width, SCREEN_RECT.height))
        self.screen.fill(self.color_list[0])
        pygame.display.update()
        # Set title
        pygame.display.set_caption(title_name)
        self.clock = Clock(self.screen)
        self.angle = 1

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
            self.__event_handler()
            self.fclock.tick(self.fps)
            self.screen.fill(self.color_list[1])
            self.angle += 7
            self.clock.flower_rotate(self.angle)
            self.clock.draw_flower()
            pygame.display.update()

class Clock():
    def __init__(self,screen, topright = (200,130)):
        self.screen = screen
        self.topright = topright
        image_name = 'images\\clock\\clock_flower.jpg'
        # type(self.image) --> pygame.Surface
        self.image = pygame.image.load(image_name)
        self.image_rect = self.image.get_rect()
        self.image_rect.topright= topright
        # self.image_rect.move(self.topright)
    def draw_flower(self):
        self.screen.blit(self.image_rotated,self.image_rotated_rect)
        #pygame.draw.circle(self.screen,(255,0,0),self.image_rotated.get_rect().topright,5)
        #pygame.draw.rect(self.screen,(255,0,0),self.image_rotated.get_rect(),2)
        pygame.draw.circle(self.screen,(0,255,0),self.image_rotated_rect.topright,5)
        pygame.draw.rect(self.screen,(0,255,0),self.image_rotated_rect,2)

    def flower_rotate(self,angle):
        # anticlockwise ( not clockwise )
        # create a new variable to save image rotated
        self.image_rotated = pygame.transform.rotate(self.image, angle)
        self.image_rotated_rect = self.image_rotated.get_rect(center = self.topright)


if __name__ == '__main__':
    game = MainWindow()
    game.start_game()
