# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 006 实例：判断输入的是不是黄蓉所说的数.py
# Author      : Simon
# Time        : 2020/9/21 14:16
# Description :使用if语句判断用户输入的数字是不是黄蓉所说的除以三余二，除以五余三，除以七余二的数。符合条件的数为23.
print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
number = int(input("请输入您认为符合条件的数："))
if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
    print(number,"符合条件：三三数之剩二，五五数之剩三，七七数之剩二")

#说明：使用if语句时，如果只有一条语句，那么语句快可以直接写到冒号的右侧 ，如下：
#if a > b: max = a   但是为了程序代码的可读性，建议不要这么做。

