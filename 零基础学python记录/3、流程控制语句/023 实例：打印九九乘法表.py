# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 023 实例：打印九九乘法表.py
# Author      : Simon
# Time        : 2020/9/22 16:04
# Description :
for i in range(1,10):                   # 输出9行
    for j in range(1,i + 1):            # 输出与行数相等的列
        print(str(j) + "x" + str(i) + "=" + str(i * j) + "\t",end = '')
    print('')                           # 换行

'''代码注解：本实例的代码使用了双层for循环，第一个循环可以看成是对乘法表行数的控制，同时也是每一个乘法公式的第二个因素；第二个循环控制乘
法表的列数，列数的最大值应该等于行数，因此第二个循环的条件应该是在第一个循环的基础上建立的。'''

