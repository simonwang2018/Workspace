num1 = float (input('Enter the first number:'))
num2 = float (input('Enter the second number:'))
if num1 < num2: #判断num1与num2的关系
    print (num1,'is less than',num2)
if num1 > num2:
    print (num1,'is greater than',num2)
if num1 == num2:
    print (num1,'is equal to',num2)
if num1 != num2:
   print (num1,'is not equal to',num2)
 #测试为假的情况下可以使用elif函数
answer = float(input('Enter a number from 1 to 15:'))
if answer >= 10:
    print ('you got at least 10!')
elif answer >= 5:
    print ('you got at least 5!')
elif answer >= 3:
    print ('you got at least 3!')
else:
    print ('You got less than 3!')
