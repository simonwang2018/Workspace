#处理声音的模块pygame.mixer
import pygame,sys
pygame.init()
pygame.mixer.init() #要播放声音，需先初始化
screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000) #等待1秒钟，让mixer完成初始化

pygame.mixer.music.load('001.mp3')
pygame.mixer.music.play()

#pygame.mixer.music.play(3) 播放音乐3次
#pygame.mixer.music.play(-1) 让音乐永远重复下去

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
