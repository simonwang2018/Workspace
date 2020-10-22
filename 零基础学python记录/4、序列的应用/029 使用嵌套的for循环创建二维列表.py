# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 029 使用嵌套的for循环创建二维列表.py
# Author      : Simon
# Time        : 2020/10/22 14:18
# Description :
'''
2、例如，创建一个包含4行5列的二维列表，可以使用下面的代码：
'''
arr = []                            # 创建一个空列表
for i in range(4):
    arr.append([])                  # 在空列表中再添加一个空列表
    for j in range(5):
        arr[i].append(j)               # 为内层列表添加元素
print(arr)

