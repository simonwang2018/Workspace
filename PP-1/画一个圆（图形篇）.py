import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480]) #这里是定义screen窗口
screen.fill([255,255,255]) #用白色背景填充窗口
pygame.draw.circle(screen,[255,0,0],[100,100],30,0)#用什么颜色来画，对应的值为[255,0,0]
#在什么位置画，在这里位于[100,100]，这表示从左上角向下100像素再向右100像素的位置。圆的大小，这里是30
#这是圆的半径，也就是圆心到外围边界的距离，单位是像素。线宽，即线的粗细，此处width=0，那么圆是完全填充的
pygame.display.flip() #翻转
#下边4条代码，是因为打开窗口后，为了能够点击窗口右上角的红X关闭窗口所需的代码
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
