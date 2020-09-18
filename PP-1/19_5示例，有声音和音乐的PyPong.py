import  pygame,sys
#--------------Ball类定义，包括move()方法----------------------
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,image_file,speed,location = [0,0] ):
        pygame.sprite.Sprite.__init__(self) #初始化动画精灵
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = speed
#--------------移动球（在顶边和左右两边反弹）---------------
    def move(self):
        global points,score_text
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = - self.speed[0]
            hit_wall.play() #球碰到两边时的声音

        if self.rect.top <= 0 :
            self.speed[1] = - self.speed[1]
            points = points + 1
            score_text = font.render(str(points),1,(0,0,0))
            get_point.play() #球碰到顶边（玩家得分）时播放的声音
#--------------球拍类定义---------------------------
class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self,location = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,20])
        image_surface.fill([78,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
#-----------------初始化Pygame的sound模块、时钟、球和球拍---------------------
pygame.init()
pygame.mixer.init()
#---------------创建声音对象，加载声音，并设置每个声音的音量------------
pygame.mixer.music.load('001.mp3') #加载音乐文件
pygame.mixer.music.set_volume(0.3) #设置音乐的音量
pygame.mixer.music.play(-1) #开始播放音乐，一直重复
hit = pygame.mixer.Sound('hit_paddle.wav')
hit.set_volume(0.4)
new_life = pygame.mixer.Sound('new_life.wav')
new_life.set_volume(0.5)
splat = pygame.mixer.Sound('splat.wav')
splat.set_volume(0.1)
hit_wall = pygame.mixer.Sound('hit_wall.wav')
hit_wall.set_volume(0.2)

get_point = pygame.mixer.Sound('get_point.wav')
get_point.set_volume(0.4)
bye = pygame.mixer.Sound('game_over.wav')
bye.set_volume(0.6)

screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
myBall = MyBallClass('wackyball.bmp',[12,6],[50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270,400])
lives = 3
points = 0
#------------------创建font对象-----------------------
font = pygame.font.Font(None,50)
score_text = font.render(str(points),1,(0,0,0))
textpos = [10,10]
done = False
#----------------主循环开始---------------------
while 1:
    clock.tick(30)
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:#如果鼠标移动就移动球拍
            paddle.rect.centerx = event.pos[0]
#------------------检查球是否碰到球拍--------------------
    if pygame.sprite.spritecollide(paddle,ballGroup,False):
        hit.play() #球碰到球拍时播放声音
        myBall.speed[1] = - myBall.speed[1]
    myBall.move()#移动球
#--------------------完全重绘----------------------------------
    if not done:
        screen.blit(myBall.image,myBall.rect)
        screen.blit(paddle.image,paddle.rect)
        screen.blit(score_text,textpos)
        for i in range(lives):
            width = screen.get_width()
            screen.blit(myBall.image,[width - 40 * i,20])
        pygame.display.flip()
#------------------如果球碰到底边就减一条命-----------------------
    if myBall.rect.top >= screen.get_rect().bottom:
        if not done:
            splat.play() #玩家丢一条命时播放声音
        lives = lives - 1
#------------------创建和绘制最终的分数文本-----------------------
        if lives <= 0:
            if not done:
                pygame.time.delay(1000) #等待1秒，然后播放结束声音
                bye.play()

            final_text1 = "Game Over "
            final_text2 = "Your final score is: " + str(points)
            ft1_font = pygame.font.Font(None,70)
            ft1_surf = font.render(final_text1,1,(0,0,0))
            ft2_font = pygame.font.Font(None,50)
            ft2_surf = font.render(final_text2,1,(0,0,0))
            screen.blit(ft1_surf,[screen.get_width() / 2 - ft1_surf.get_width() / 2,200])
            screen.blit(ft2_surf,[screen.get_width() / 2 - ft2_surf.get_width() / 2,200])
            pygame.display.flip()
            done = True
            pygame.mixer.music.fadeout(2000) #音乐淡出
#----------------2秒之后，获得新的一条命，重新开始---------------------
        else:
            pygame.time.delay(1000)
            new_life.play() #开始新的一条命时播放音乐
            myBall.rect.topleft = [50,50]
            screen.blit(myBall.image , myBall.rect)
            pygame.display.flip()
            pygame.time.delay(1000)
