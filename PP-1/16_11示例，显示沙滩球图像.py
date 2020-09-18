#在pygame中，使用图像最简单的方法就是利用函数image函数，图像要与代码在同一文件夹下
import  pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
#pygame.image.load()加载一个图像，并创建名为my_ball的对象。
my_ball = pygame.image.load('beach_ball.png')
screen.blit(my_ball,[50,50])
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
