#处理声音的模块pygame.mixer
import pygame,sys
pygame.init()
pygame.mixer.init() #要播放声音，需先初始化
screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000) #等待1秒钟，让mixer完成初始化

pygame.mixer.music.load('001.mp3')
pygame.mixer.music.set_volume(0.30) #调节音乐的音量
pygame.mixer.music.play()
splat = pygame.mixer.Sound('splat.wav')
splat.set_volume(0.50) #调节音效的音量
splat.play()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()