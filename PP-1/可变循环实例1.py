numstars = int(input('How many stars do you want?'))
#如果需要5个星号，这里加1就是5个，如果不加1就是4个星号。另一种方法是从0开始计数就不需要加1.
for i in range (1,numstars+1):
    print('*',end = '')
