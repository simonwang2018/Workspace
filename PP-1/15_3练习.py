#编写一个程序，生成1到20之间的5个随机整数的列表，并打印出来
#方法一
import random
print(random.randint(1,20))
print(random.randint(1,20))
print(random.randint(1,20))
print(random.randint(1,20))
print(random.randint(1,20))
#方法二
import random
def randomprint():
    print (random.randint(1,20))
for i in range(5):
    randomprint()
#方法三
import random
for i in range(5):
    print (random.randint(1,20))