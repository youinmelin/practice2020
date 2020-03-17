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
        # self.clock2 = Clock(self.screen,(300,300))
        self.angle = 1
        self.size = [89,50]
        self.grow = 9

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
            self.stretch()
            self.rotate()
            pygame.display.update()

    def stretch(self):
        clock2 = Clock(self.screen,(300,300))
        if self.size[0] > 120 or self.size[0] < 80: 
            self.grow *= -1
        self.size[0] += self.grow
        print(self.size)
        clock2.flower_stretch(self.size)
        clock2.draw_flower()

    def rotate(self):
        self.angle += 6
        self.clock.flower_rotate(self.angle)
        self.clock.draw_flower()



class Clock():
    def __init__(self,screen, topright = (200,130)):
        self.screen = screen
        self.topright = topright
        image_name = 'images\\clock\\clock_flower.jpg'
        # type(self.image) --> pygame.Surface
        self.image = pygame.image.load(image_name)
        self.image_rect = self.image.get_rect()
        self.image_rect.topright= topright
        self.flower_rotate(0)
        self.flower_stretch(self.image_rect.size)
        # self.image_rect.move(self.topright)
    def draw_flower(self):
        self.screen.blit(self.image_changed,self.image_changed_rect)
        pygame.draw.circle(self.screen,(0,255,0),self.image_changed_rect.topright,5)
        pygame.draw.rect(self.screen,(0,255,0),self.image_changed_rect,2)

    def flower_rotate(self,angle):
        # anticlockwise ( not clockwise )
        # create a new variable to save image rotated
        self.image_changed = pygame.transform.rotate(self.image, angle)
        self.image_changed_rect = self.image_changed.get_rect(center = self.topright)

    def flower_stretch(self,size):
        self.image_changed = pygame.transform.scale(self.image,size)
        self.image_changed_rect = self.image_changed.get_rect(topright = self.topright)
        
if __name__ == '__main__':
    game = MainWindow()
    game.start_game()
