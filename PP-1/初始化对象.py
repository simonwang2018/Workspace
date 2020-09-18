class ball: #创建一个类
    def  __init__(self,color,size,direction): #这里是_init_()方法,创建一个实例并设置属性
        self.color = color
        self.size = size
        self.direction = direction
    def bounce(self):
        if self.direction == 'down':
            self.direction = 'up'
myball = ball ('red','small','down') #属性作为_init_（）的参数传入
#打印对象的属性
print ('I just created a ball.')
print ('My ball is ',myball.size)
print ('My ball is ',myball.color)
print ("My ball's direction is ",myball.direction )
print ("Now I'm going to bounce the ball")
print ()
myball.bounce() #使用一个分法
print ("Now the ball's direction is ",myball.direction)
print (myball)