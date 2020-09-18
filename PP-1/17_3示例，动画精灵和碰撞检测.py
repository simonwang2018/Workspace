import sys,pygame
from random import *
#----------------------球的类定义---------------------------------
class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,image_file,location,speed):
        pygame.sprite.Sprite.__init__(self)#初始化动画精灵
        self.image = pygame.image.load(image_file)#向其中加载图像文件
        self.rect = self.image.get_rect()#得到定义图像边界的矩形
        self.rect.left, self.rect.top = location#设置球的初始位置
        self.speed = speed #增加这行代码，为球创建一个speed属性
#----------------------增加这个方法来移动球-----------------------
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:#检查是否碰到窗口左右两边，如果是，让X-speed反向
            self.speed[0] = - self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:#检查是否碰到窗口上下两边，如果是，让y-speed反向
            self.speed[1] = - self.speed[1]
#----------------新的animate()函数-----------------------
def animate(group):
    screen.fill([255,255,255])
    for ball in group:
        ball.move()
    for ball in group:
        group.remove(ball)
        if pygame.sprite.spritecollide(ball,group,False):#检查精灵与组之间的碰撞
            ball.speed[0] = - ball.speed[0]
            ball.speed[1] = - ball.speed[1]
        group.add(ball)#将球再添加回原来的组中
        ball.move()
        screen.blit(ball.image,ball.rect)
    pygame.display.flip()
    pygame.time.delay(20)
#----------------主程序-----------------------------------
size = width, height = 640 , 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = 'beach_ball.png'
group = pygame.sprite.Group()#创建精灵组
for row in range (0,2): #------------创建4个球--------
    for column in range (0,2):#-----------
        location = [column * 180 + 10,row * 180 + 10]#每次循环时都有一个不同位置
        speed = [choice([-2,2]),choice([-2,2])]
        ball = MyBallClass(img_file,location,speed)#在这个位置创建一个球
        group.add(ball)#把球收集到一个列表中
#----------------------重绘屏幕----------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    animate(group) #调用animate（）函数并传入group
