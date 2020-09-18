#使用for语句，询问喜欢的数，然后希望乘到多大的乘法表。
number = int(input('Which multiplication table would you like?'))
i = int(input('How high do you want to go?'))
print("Here's your table:")
for i in range (1,i+1):
    print(number,'x',i,'=',i*number)
#使用while语句完成上边的例子
number = int(input('Which multiplication table would you like?'))
i = int(input('How high do you want to go?'))
print("Here's your table:")
j = 1 #引用j，当j小于或等于i时，则打印这个表。
while j <= i:
    print(number,'x',j,'=',j*number)
    j += 1


