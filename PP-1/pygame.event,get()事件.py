'''打开的窗口右上角的X是关闭，但是想要关闭，在一个pygame程序中，X应该连接到一个
名为sys.exit()的内置函数。'''
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
#下边4条是关闭窗口所需的代码,pygame.event.get()方法从事件队列得到所有事件的一个列表。for循环迭
#代处理这个列表中的每一个事件，如果看到一个QUIT事件，它会运行一个名为sys.exit()的函数，这会关闭
#pygame窗口，并结束程序。了解到这一点后，现在你应该已经完全清楚“点击X结束程序”代码是如何工作的。
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
