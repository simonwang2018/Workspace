n = 0
while n < 10:
    n = n + 1
    print(n)
#上面的程序可以打印出1~10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  #如果n是偶数，执行continue语句
        continue    #continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
