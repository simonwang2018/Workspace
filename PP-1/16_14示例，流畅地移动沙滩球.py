#在pygame中，使用图像最简单的方法就是利用函数image函数，图像要与代码在同一文件夹下
import  pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
#pygame.image.load()加载一个图像，并创建名为my_ball的对象。
my_ball = pygame.image.load('beach_ball.png')
x = 50
y = 50
screen.blit(my_ball,[x,y])   #命名用x和y（）而不是数字
pygame.display.flip()
for looper in range(1,100):
    pygame.time.delay(20)
    #沙滩球图形大约90像素，所以下边白色矩形的大小就是90像素宽和高。
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)#这一条代码是擦除第一个球
    x = x + 5
    screen.blit(my_ball,[x,y])
    pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
