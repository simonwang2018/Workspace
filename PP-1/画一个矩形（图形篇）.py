'''pygame.draw.rect(screen,[255,0,0],[250,150,300,200],0),其中的[250，150，300，200]对
应的是[left,top,width,height],因为矩形要使用左上角坐标、宽和高来定义'''
import pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480]) #这里是定义screen窗口
screen.fill([255,255,255]) #用白色背景填充窗口
pygame.draw.rect(screen,[255,0,0],[250,150,300,200],0)#这行代码可以用下边两行代码替代
#my_list = [250,150,300,200]
#pygame.draw.rect(screen,[250,0,0],my_list,0) 或者是下边两行
#my_rect = pygame.rect(250,150,300,200)
#pygame.draw.rect(screen,[255,0,0],my_rect,0)
pygame.display.flip() #翻转
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
