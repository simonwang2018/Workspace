# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 042 元组推导式.py
# Author      : Simon
# Time        : 2020/11/12 10:20
# Description :
# 使用元组推导式可以快速生成一个元组，它的表现形式和列表推导式类似，只是将列表推导式中的[]修改为()。
# 例如，使用下面的代码生成一个包含10个随机数的元组。
import random                               # 导入random标准库
randomnumber = (random.randint(10,100) for i in range(10))
print('生成的元组为: ',randomnumber)
'''从上面的执行结果中，可以看出使用元组推导式生成的结果并不是一个元组或者列表，而是一个生成器对象，这一点和列表推导式是不同的。要使
用该生成器对象可以将其转换为元组或列表。其中，转换为元组使用tuple()函数，而转换为列表则使用list()函数。如下代码：'''
import random                               # 导入random标准库
randomnumber = (random.randint(10,100) for i in range(10))
randomnumber = tuple(randomnumber)          # 转换元组
print('转换后: ',randomnumber)

'''要使用通过元组推导器生成的生成器对象，还可以直接通过for循环遍历或者直接使用_next_()方法进行遍历。如下，通过生成器推导式生成一个
包含3个元素的生成器对象number，然后调用3次_next_()方法输出每个元素的值，再将生成器对象number转换为元组输出，代码如下：'''
number = (i for i in range(3))                    # 生成生成器对象
print(number.__next__())                          # 输出第1个元素
print(number.__next__())                          # 输出第2个元素
print(number.__next__())                          # 输出第3个元素
number = tuple(number)                            # 转换为元组
print('转换后：',number)

'''通过生成器推导式生成一个包括4个元素的生成器对象number，然后应用for循环遍历该生成器对象，并输出每一个元素的值，最后将其转换为元
组输出，代码如下：'''
number = (i for i in range(4))                    # 生成生成器对象
for i in number:                                  # 遍历生成器对象
    print(i,end=' ')                               # 输出每个元素的值
print(tuple(number))                              # 转换为元组输出

'''从上面的两个示例中可以看出，无论通过哪种方法遍历，如果再想使用该生成器对象，都必须重新创建一个生成器对象，因为遍历后原生成器对象
已经不丰在了。'''

