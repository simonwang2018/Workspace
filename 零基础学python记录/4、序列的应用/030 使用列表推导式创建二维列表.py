# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 030 使用列表推导式创建二维列表.py
# Author      : Simon
# Time        : 2020/10/22 14:26
# Description :
'''
使用列表推导式也可以创建二维列表，因为这种方法比较简洁，所以建议使用这种方法创建二维列表。例如，使用列表推导式创建一个包含4行5列的二维列
表可以使用下面的代码：
'''
arr = [[j for j in range(5)] for i in range(4)]
print(arr)
'''
创建二维数组后，可以通过以下语法格式访问列表中的元素：
listname[下标1][下标2]
参数说明：
listname:列表名称。
下标1：表示列表中第几行，下标值从0开始，即第一行的下标为0。
下标2：表示列表中第几列，下标值从0开始，即第一列的下标为0.
例如，要访问二维列表中的第2行，第4列，可以使用下面的代码：
verse[1][3]
'''
