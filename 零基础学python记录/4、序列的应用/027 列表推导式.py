# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 027 列表推导式.py
# Author      : Simon
# Time        : 2020/10/21 15:32
# Description :
'''
使用列表推导式可以快速生成一个列表，或者根据某个列表生成满足指定需求的列表。列表推导式通常有以下几常用的语法格式。
（1）生成指定范围的数值列表，语法格式如下：
list = [Expression for var in range]
参数说明：
list:表示生成的列表名称。
Expression:表达式，用于计算新列表的元素。
var:循环变量。
range:采用range()函数生成的range对象。
例如，要生成一个包括10个随机数的列表，要求数的范围在10~100（包括）之间，具体代码如下：
'''
import random                    # 导入random标准库
randomnumber = [random.randint(10,100) for i in range(10)]
print("生成的随机数为:",randomnumber)

'''
(2)根据列表生成指定需求的列表，语法格式如下：
newlist = [Expression for var in list]
参数说明：
newlist:表示新生成的列表名称。
Expression:表达式，用于计算新列表的元素。
var:变量，值为后面列表的每个元素值。
list:用于生成新列表的原列表。
例如，定义一个记录商品价格的列表，然后应用列表推导式生成一个将全部商品价格打五折的列表，具体代码如下：
'''
price = [1200,5330,2988,6200,1998,8888]
sale = [int(x*0.5) for x in price]
print("原价格：",price)
print("打五折的价格：",sale)

'''
(3)从列表中选择符合条件的元素组成新的列表，语法格式如下：
newlist = [Expression for var in list if condition]
参数说明：
newlist:表示新生成的列表名称。
Expression：表达式，用于计算新列表的元素。
var：变量，值为后面列表的每个元素值。
list：用于生成新列表的原列表。
condition：条件表达式，用于指定筛选条件。
例如，定义一个记录商品价格的列表，然后应用列表推导式生成一个商品价格高于5000元的列表，具体代码如下：
'''
price = [1200,5330,2988,6200,1998,8888]
sale = [x for x in price if x > 5000]
print("原列表：",price)
print("价格高于5000的:",sale)
