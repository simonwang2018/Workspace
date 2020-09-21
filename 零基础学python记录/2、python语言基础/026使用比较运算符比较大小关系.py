# !/usr/bin/python
# -*- coding:utf-8 -*-
# @File     : 026使用比较运算符比较大小关系.py
# @Author   : Simon
# @Time     : 2020/9/18 15:45
python = 95                                #定义变量，存储python课程的分数
english = 92                               #定义变量，存储english课程的分数
c = 89                                     #定义变量，存储C语言课程的分数
#输出3个变量的值
print('python = ' + str(python) + ' english = ' + str(english) + ' c = ' + str(c) + '\n')
print('python < english的结果:' + str(python < english))                 #小于操作
print('python > english的结果:' + str(python > english))                 #大于操作
print('python == english的结果:' + str(python == english))               #等于操作
print('python != english的结果:' + str(python != english))               #不等于操作
print('python <= english的结果:' + str(python <= english))               #小于或等于操作
print('english >= c的结果:' + str(python > c))                           #大于或等于操作
