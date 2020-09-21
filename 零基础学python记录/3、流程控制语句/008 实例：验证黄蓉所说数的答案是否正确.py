# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 008 实例：验证黄蓉所说数的答案是否正确.py
# Author      : Simon
# Time        : 2020/9/21 14:37
# Description : 使用if...else语句判断用户输入的数字是不是黄蓉所说的除以三余二，除以五余三，除以七余二的数，并给予相应的提示。
print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
number = int(input("请输入瑛姑给出的数："))
if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
    print(number,"符合条件")
else:
    print(number,"不符合条件")

