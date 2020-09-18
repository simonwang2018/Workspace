#计算零钱的总面值，包括五分币、二分币和一分币，函数应当返回这些硬币的总面值。然后编写一个程序
#调用这个函数。
def count (quarters,dimes,nickels,pennies):
    total = quarters * 5 + dimes * 2 + nickels * 1 + pennies
    return total
quarters = int(input('quarters:'))
dimes = int(input('dimes:'))
nickels = int(input('nickels:'))
pennies = int(input('pennies:'))
total = count(quarters,dimes,nickels,pennies)
print ('total is:',total)