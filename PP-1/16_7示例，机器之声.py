'''color_name = random.choice(THECOLORS.keys())在python2中运行正常，在python2中，
key()方法返回的是一个列表，而在python3中，其返回的是一dict_keys对象，所以我们使用
random.choice来随机取一个列表元素的时候，在python3中，就不能直接使用，
要使用list方法将dict_keys对象转换为列表'''
import pygame,sys,random
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for i in range(100):
    width = random.randint(0,255)
    height = random.randint(0,100)
    top = random.randint(0,400)
    left = random.randint(0,500)
    color_name = random.choice(list(THECOLORS.keys()))
    color = THECOLORS[color_name]
    line_width = random.randint(1,3)
    pygame.draw.rect(screen,color,[left,top,width,height],line_width)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
