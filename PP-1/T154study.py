#题，编写一个程序，要求它工作30秒，每3秒打印一个随机小数。
#方法一，需要154调用T154study方法一中代码来运行才可以起作用。
import random
def randomprint():
    print (random.random())
#方法二
import time,random
for i in range(10):
    time.sleep(3)
    print (random.random())
