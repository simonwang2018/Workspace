#提前跳转，如果希望停止执行循环的当前迭代，提前跳到下一次迭代，需要的就是一条continue语句。
#注意第3次循环（i==3）时，循环体没有完成，它是提前跳转到(i==4)了，就这个continue语句。
#在while循环中，continue的作用也是一样的。
for i in range (1,6):
    print()
    print('i = ',i,end = '')
    print(' hello,how',end = '')
    if i == 3:
        continue
    print(' are you today?')
