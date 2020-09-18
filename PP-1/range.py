#使用range循环，从给定的第一个数开始，在给定的最后一个数之前结束。
for looper in range (1,5): #此条代码与fo looper in [1,2,3,4]是一样的意思。
    print (looper,'times 8 = ',looper * 8)
for looper in range (5):#这条代码与for looper in range (0,5)是一个意思，但是这里是从0开始
    #循环，与上边的不一样，上边是从1开始循环。
    print (looper,'times 8 = ',looper * 8)
#按步长计数实例如下
for i in range (1,10,2):#在10后边有个逗号2，即是以步长2开始循环。
    print (i)
#反向计数循环，第3个参数为负数时，循环会向下计数，而不是向上计数。
for i in range (10,1,-1):
    print(i)
#倒计时定时器实例
import time
for i in range (10,0,-1):
    print (i)
    time.sleep(1)
print('blast off')
