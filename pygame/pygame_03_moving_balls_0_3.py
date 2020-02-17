from pygame_00_base_class import *
import random


def main():
    screen = Screen(window_x=200,window_y=200)
    screen.background()
    
    circle = Circle(screen.myscreen,x = 50 , y = 50,width=0)
    circle.draw()
    circle2 = Circle(screen.myscreen,x = 80 , y = 50,width=0)
    circle2.draw()
    pygame.display.update()
    movex = 3
    movey = 2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.background()
        # circle.move(2)
        circle.radius += 0
        circle.x += movex
        circle.y += movey
        circle2.x += movex
        circle2.y += movey

        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        if circle.x > screen.window_x - circle.radius \
            or circle.x < 0 + circle.radius:
            movex = -movex
            circle.color = red,green,blue
            circle2.color = red,green,blue
        if circle.y > screen.window_y - circle.radius \
            or circle.y < 0 + circle.radius:
            movey = -movey
            circle.color = red,green,blue
            circle2.color = red,green,blue
        circle.draw()
#        if circle2.x > screen.window_x - circle2.radius \
#            or circle2.x < 0 + circle2.radius:
#            movex = -movex
#            circle2.color = red,green,blue
#        if circle2.y > screen.window_y - circle2.radius \
#            or circle2.y < 0 + circle2.radius:
#            movey = -movey
#            circle2.color = red,green,blue
        circle2.draw()
        pygame.display.update()
        time.sleep(0.05)
        print(circle.x,circle.y)

if __name__ == '__main__':
    main()

