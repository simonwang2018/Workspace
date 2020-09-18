class ball:
    def  __init__(self,color,size,direction): #这里是_init_()方法
        self.color = color
        self.size = size
        self.direction = direction
    def __str__(self):#这里是_str_方法
        msg = "Hi, I'm a " + self.size +' ' + self.color + ' ball!'
        return msg
myball = ball ('red','small','down') #属性作为_init_（）的参数传入
print (myball)
