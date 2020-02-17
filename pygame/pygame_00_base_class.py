import pygame
import sys
import time

class Screen():
    def __init__(self,window_x=300,window_y=300,bg_color=(255,255,255)):
        self.window_x = window_x
        self.window_y = window_y
        self.bg_color = bg_color
    def background(self):
        pygame.init()
        self.myscreen = pygame.display.set_mode((self.window_x,self.window_y))
        self.myscreen.fill(self.bg_color)
        # pygame.display.update()

class OneObject():
    pass

class Circle(OneObject):
    def __init__(self,screen,color =(0,255,0), x = 100 , y = 200  , sidey = 20, sidex = 15, r = 20, width = 6):
        self.color = color
        self.x = x
        self.y = y
        self.sidey = sidey
        self.sidex = sidex
        self.radius = r
        self.width = width
        self.screen = screen
    def draw(self):
        self.center= self.x,self.y
        pygame.draw.circle(self.screen,self.color,self.center,self.radius,self.width)
        # pygame.display.update()
    def move(self,speed):
        self.move_x = self.move_y = speed
        self.x += self.move_x
        self.y += self.move_y
        

class Text():
    def __init__(self,screen):
        self.text_font = None
        self.text_size = 30
        self.text_color = 0,0,0
        self.text_content = ''
        self.text_x = 0
        self.text_y = 0
        self.screen = screen
    def draw_text(self):
        my_font = pygame.font.Font(self.text_font,self.text_size)
        text_image = my_font.render(self.text_content,self.text_font,self.text_color)
        self.screen.blit(text_image,(self.text_x,self.text_y))

def main():
    screen = Screen()
    screen.background()
    circle = Circle(screen.myscreen)
    circle.draw()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        time.sleep(0.1)

#        text_content = str(self.x) +', '+ str(self.y)
#
#        if self.x > window_x-self.sidey or self.x < 0:
#            self.move_x = -self.move_x
#        if self.y > window_y-self.sidex or self.y < 0:
#            self.move_y = -self.move_y

if __name__ == '__main__':
    main()

