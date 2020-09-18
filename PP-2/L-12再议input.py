'''birth = input('birth:')
if birth < 2000:
    print('00前')
else:
    print('00后')
#这里在输入数字1890后，结果报错。这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。python提供了int()函数来
#完成这件事情。'''
s = input('birth:')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

