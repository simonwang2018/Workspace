print('Enter your name:')
somename = input()
# 在python 2中使用的是raw_input，而在python3中整合到input了。
# 表示的用户任意输入一个字符串，并把它赋值给somename。
print ('Hi',somename,'how are you today')
#上边的语句可以使用下边的方法输入，不需要用到第一条打印
somename = input('Enter your name:')
print ('hi',somename,'how are you today')

