# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 026 实例：助力黄蓉3：for循环改进版解题法.py
# Author      : Simon
# Time        : 2020/9/23 10:08
# Description :
print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
for number in range(100):
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:     # 判断是否符条件
        print("答曰：这个数是",number)                                # 输出符合条件的数
        break                                                       # 跳出for循环
