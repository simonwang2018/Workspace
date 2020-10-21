# 打印9 * 9 乘法表
for i in range(1,10):
    for m in range (1,i+1):
        sum = i * m
        if m < i:
            print(m,'x',i,'=',sum ,end= '   ')
        else:
            print(m,'x',i,'=',sum)