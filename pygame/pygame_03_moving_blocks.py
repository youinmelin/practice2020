from pygame_00_base_class import *
import random


def main():
    screen = Screen()
    screen.background()
    
    circle = Circle(screen.myscreen,width=0)
    circle.draw()
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

        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        if circle.x > screen.window_x - circle.radius \
            or circle.x < 0 + circle.radius:
            movex = -movex
            circle.color = red,green,blue
        if circle.y > screen.window_y - circle.radius \
            or circle.y < 0 + circle.radius:
            movey = -movey
            circle.color = red,green,blue
        circle.draw()
        pygame.display.update()
        time.sleep(0.01)
        print(circle.x,circle.y)

if __name__ == '__main__':
    main()

