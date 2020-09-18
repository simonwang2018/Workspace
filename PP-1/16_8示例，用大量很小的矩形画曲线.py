import pygame,sys
import math #导入数学函数，包括sin()
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for x in range(0,640): #从左到右循环（X=0到639）
    y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240) #计算每个点的Y坐标（垂直坐标）
    pygame.draw.rect(screen,[0,0,0],[x,y,1,1],1)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
