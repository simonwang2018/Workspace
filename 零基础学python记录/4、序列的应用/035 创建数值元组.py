# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 035 创建数值元组.py
# Author      : Simon
# Time        : 2020/10/22 17:19
# Description :
'''
在python中，可以使用tuple()函数直接将range（）函数循环出来的结果转换为数值元组。
tuple()函数的基本语法如下：
tuple(data)
其中，data表示可以转换为元组的数据，其类型可以是range对象、字符串、元组或者其他可迭代类型的数据。
例如，创建一个10~20（不包括20）所有偶数的元组，可以使用下面的代码：
'''
tuple(range(10,20,2))

'''运行上面的代码后，将得到下面的列表：
(10, 12, 14, 16, 18)
说明：使用tuple()函数不仅能通过range对象创建元组，还可以通过其他对象创建元组。
'''
