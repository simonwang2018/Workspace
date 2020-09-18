#如果想完全跳出循环，不再完成计数，或者放弃等待结束条件。可以使用break。下面是在(i==3)时就跳
#出循环。
for i in range (1,6):
    print()
    print('i = ',i,end = '')
    print(' hello,how',end = '')
    if i == 3:
        break
    print(' are you today?')