# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 030 pass空语句.py
# Author      : Simon
# Time        : 2020/9/23 10:58
# Description : 在python中还有一个pass语句，表示空语句。它不做任何事情，一般起到占位作用。例如，在应用for循环输出1~10之间（不包括10）
# 的偶数时，在不是偶数时，应用pass语句占个位置，方便以后对不是偶数的数进行处理。代码如下：
for i in range(1,10):
    if i % 2 == 0:                  # 判断是否为偶数
        print(i,end= ' ')
    else:                           # 不是偶数
        pass                        # 占位符，不做任何事情

