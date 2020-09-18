#输入一个数从1到10的乘法表。
m = int(input('Which multiplication table would you like:'))
print('Here is your table:')
for i in range (1,11):
    print(m,'x', i,'=', i*m)
#使用while循环上面实例的乘法表
number = int(input('Which multiplication table would you like:'))
print("Here's your table:")
i = 1 #指定i的列表
while i <= 10:#设定i到哪个值结束
    print(number,'x',i,'=',number * i)
    i=i+1

