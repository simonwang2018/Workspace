#询问用户从第几秒开始循环倒计时。
#再加上让它除了打印各个数之外还要打印一行星号，使用了嵌套循环。
sec = int(input('How many seconds?'))
import time
for i in range (sec,0,-1):
    print(i,end = '')
    for star in range(i):
        print('*',end = '')
    print()
    time.sleep(1)
print('Blast Off')