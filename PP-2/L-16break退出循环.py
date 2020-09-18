n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
#上面的代码可以打印出1~100.如果要提前结束循环，可以用break语句：
n = 1
while n <= 100:
    if n > 10:  #当n=11时，条件满足，执行break语句
        break   #break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
#执行上面的代码可以看到，打印出1~10后，紧接着打印END，程序结束。可见break的作用是提前结束循环。
