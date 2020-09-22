# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 020 实例：助力黄蓉2：for循环版解题法.py
# Author      : Simon
# Time        : 2020/9/22 15:47
# Description : 使用for循环语句从1循环到100（不包含100），并且记录符合黄蓉要求的数。具体的实现方法是：应用for循环语句从1迭代到99，在
# 循环体中，判断迭代变量number是否符合要求，如果符合则应用print()函数输出，否则继续循环。具体代码如下：
print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
for number in range(100):
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:     # 判断是否符条件
        print("答曰：这个数是",number)                                # 输出符合条件的数
