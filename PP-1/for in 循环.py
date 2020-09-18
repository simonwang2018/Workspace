for looper in [1,2,3,4,5]: #表示looper的值从1开始（所以looper=1）。对应列表中的每一个值，
#这个循环会把下一个指令块中的所有工作完成一次（列表就是中括号中的那些数），每个循环时
#变量looper会赋为这个列表中的下一个值。
    print('hello')#此为python每次循环时要执行的代码块。for循环需要一个代码块来告诉程序每次
#循环时做什么。这个代码块称为特环体。每次循环称为一个迭代。
for looper in [1,2,3,4,5]:
    print(looper) #此处打印的是变量looper的值。即中括号中的值。
#打印一个8的乘法表
for loop in [1,2,3,4,5]:
    print(loop,'times 8 =',loop * 8)
