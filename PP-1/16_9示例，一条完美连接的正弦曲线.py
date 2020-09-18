'''pygame有一个画线的方法，另外还有一种方法可以在一系列点之间画线（类似于‘连接多个点’）。
这个方法是pygame.draw.lines()，它需要5个参数：
●画线的表面（surface）
●颜色（color）
●是否要画一条线将最后一个点与第一个点相连接，使形状闭合（closed）
●要连接的点的列表（list）
●线宽（width）'''
import pygame,sys
import math #导入数学函数，包括sin()
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
plotPoints = [] #给标绘点赋值
for x in range(0,640): #从左到右循环（X=0到639）
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240) #计算每个点的Y坐标（垂直坐标）
    plotPoints.append([x,y]) #将各个点添加到列表
pygame.draw.lines(screen,[0,0,0],False,plotPoints,2) #用draw.lines()函数画出整条曲线
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
