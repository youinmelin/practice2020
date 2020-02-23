## pygame note

- ball = pygame.image.load("xxx.gif")
- ballrect = ball.get_rect()
- rect对象的属性包括top,bottom,left,right,width,heigh
-
- ballrect = ballrect.move(x,y)
- screen.blit(ball,ballrect)  # 将图像(ball)绘制在另一个图像(ballrect)上
-
- fclock = pygame.time.Clock()
- fclock.tick(30) # 刷新率是30
