import  pygame,sys
#--------------Ball类定义，包括move()方法----------------------
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,image_file,speed,location):
        pygame.sprite.Sprite.__init__(self) #初始化动画精灵
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = speed
#--------------移动球（在顶边和左右两边反弹）---------------
    def move(self):
        global points,score_text
        self.rect = self.rect.move(self.speed)
        if self.rect.left <= 0 or self.rect.right >= screen.get_width():
            self.speed[0] = - self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = - self.speed[1]
            points = points + 1
            score_text = font.render(str(points),1,(0,0,0))
#--------------球拍类定义---------------------------
class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self,location = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,20])
        image_surface.fill([78,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
#-----------------初始化Pygame、时钟、球和球拍---------------------
pygame.init()
screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
myBall = MyBallClass('wackyball.bmp',[10,5],[50,50])
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
    pygame.mixer.init()
    hit = pygame.mixer.Sound('hit_paddle.wav') #创建球碰到球拍时的音效
    hit.set_volume(0.4)
    if pygame.sprite.spritecollide(paddle,ballGroup,False):
        myBall.speed[1] = - myBall.speed[1]
        hit.play() #播放音效
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
        lives = lives - 1
#------------------创建和绘制最终的分数文本-----------------------
        if lives == 0:
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
#----------------2秒之后，获得新的一条命，重新开始---------------------
        else:
            pygame.time.delay(2000)
            myBall.rect.topleft = [50,50]
