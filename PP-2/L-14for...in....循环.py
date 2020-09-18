names = ['Michael','Bob','Tracy']
for name in names:
    print(name)
#for x in...循环就是把每个元素代入变量X，然后执行缩进块的语句。
# 再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum) 
#如果要计算1-100的整数之和，从1写到100有点困难，幸好python提供一个range()函数，可以生成一个
# 整数序列，再通过list()函数可以转换为list.如range(5)生成的序列是从0开始小于5的整数：
'''list(range(5))
   [0, 1, 2, 3, 4]'''
#range(101)就可以生成0-100的整数序列，计算如下：
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
