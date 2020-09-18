#使用class创建一个对象
class Ball: #创建一个类
    def bounce(self):
        if self.direction == 'down':
            self.direction = 'up'
myball = Ball () #建立一个类的分类
myball.direction = 'down' #设置一些属性
myball.color = 'red'
myball.size = 'small'
#打印对象的属性
print ('I just created a ball.')
print ('My ball is ',myball.size)
print ('My ball is ',myball.color)
print ("My ball's direction is ",myball.direction )
print ("Now I'm going to bounce the ball")
print ()
myball.bounce() #使用一个分法
print ("Now the ball's direction is ",myball.direction)