# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 017 实例：助力黄蓉1：while循环版解题法.py
# Author      : Simon
# Time        : 2020/9/21 17:26
# Description : 使用while循环语句实现从1开始依次尝试符合条件的数，直到找到符合条件的数时，才退出循环。具体的实现方法是：首先定义一个用
#于计数的变量number和一个作为循环条件的变量none（默认值为真），然后编写while循环语句，在循环体中，将变量number的值加1，并且判断number
#的值是否符合条件，当符合条件时，将变量none设置为假，从而退出循环。具体代码如下：
print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
none = True                                  # 作为循环条件的变量
number = 0                                   # 计数的变量
while none:
    number += 1                              # 计数加1
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:     #判断是否符合条件
        print("答曰：这个数是",number)        # 输出符合条件的数
        none = False                        # 将循环条件的变量赋值为否

# 注意：在使用while循环语句时，一定不要忘记添加将循环条件改为False的代码（例如上边的代码第16行一定不能少），否则，将产生死循环。