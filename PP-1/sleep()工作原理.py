#要注意，调用sleep()函数时，必须在前面加上time。这是因为，尽管我们已经用import导入了time，
#但是并没有让它成为主程序命名空间的一部分。每次想要用sleep()函数时，都必须调用time.sleep()
'''
import time
print ('How')
time.sleep(2)
print ('are')
time.sleep(2)
print ('you')
time.sleep(2)
print ('today?') '''
#使用from time import sleep可以不必要在sleep前边再加time，因为这句是告诉python，
#在time模块中寻找名为sleep的变量（函数或对象）
from time import sleep
print ('Hello,talk to you again in 5 seconds...')
sleep(5)
print ('Hi again')
#from time import *是从模块导入所有可用的名字，但这种做为不是最佳做法，最好导入真正需要的部分。