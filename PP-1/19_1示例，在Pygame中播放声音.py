#处理声音的模块pygame.mixer
import pygame,sys
pygame.init()
pygame.mixer.init() #要播放声音，需先初始化
screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000) #等待1秒钟，让mixer完成初始化
splat = pygame.mixer.sound('001.mp3') #创建声音对象
splat.play() #播放声音
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
