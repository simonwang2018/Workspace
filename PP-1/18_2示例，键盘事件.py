#----------------初始化--------------------------------------
import  pygame,sys
pygame.init()
screen = pygame.display.set_mode([640,480])
background = pygame.Surface(screen.get_size())
background.fill([255,255,255])
clock = pygame.time.Clock()
#--------------Ball类定义，包括move（）方法----------------------
class Ball(pygame.sprite.Sprite):
    def __init__(self,image_file,speed,location):
        pygame.sprite.Sprite.__init__(self) #初始化动画精灵
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = speed
    def move(self):
        if self.rect.left <= screen.get_rect().left or self.rect.right >= screen.get_rect().right:
            self.speed[0] = - self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos
my_ball = Ball('beach_ball.png',[10,0],[20,20])#建立球的实例，[10,0]是速度，[20,20]是位置
#下边3条代码是生成一个重复事件，即我们一件按住向上或向下时，沙滩球可以一直移动，如果没有下边3条代码
#按住向上或向下按键，沙滩球也只是移动一步。
delay = 100
interval = 50
pygame.key.set_repeat(delay,interval)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
#------------------检查按键，让球上移或下移---------------------
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                my_ball.rect.top = my_ball.rect.top - 20
            elif event.key == pygame.K_DOWN:
                my_ball.rect.top = my_ball.rect.top + 20
# -------------------完全重绘----------------------------
    clock.tick(30) #这是时钟
    screen.blit(background,(0,0))
    my_ball.move()
    screen.blit(my_ball.image,my_ball.rect)
    pygame.display.flip()
