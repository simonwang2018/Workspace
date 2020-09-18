import  pygame,sys
from pygame.locals import *
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
        self.rect = self.rect.move(self.speed)
        if self.rect.left <= 0 or self.rect.right >= screen.get_width():
            self.speed[0] = - self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = - self.speed[1]
#--------------球拍类定义---------------------------
class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self,location = [0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,20])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
#-----------------初始化Pygame、时钟、球和球拍---------------------
pygame.init()
screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
ball_speed = [10,5]
myBall = MyBallClass('wackyball.bmp',ball_speed,[50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270,400])
#----------------主循环开始---------------------
while 1:
    clock.tick(30)
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:#如果鼠标移动就移动球拍
            paddle.rect.centerx = event.pos[0]
#---------------检查球是否碰到球拍--------------------
    if pygame.sprite.spritecollide(paddle,ballGroup,False):
        myBall.speed[1] = - myBall.speed[1]
    myBall.move()#移动球
#-----------------------完全重绘--------------------
    screen.blit(myBall.image,myBall.rect)
    screen.blit(paddle.image,paddle.rect)
    pygame.display.flip()
