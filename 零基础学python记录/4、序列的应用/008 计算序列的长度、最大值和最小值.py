# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 008 计算序列的长度、最大值和最小值.py
# Author      : Simon
# Time        : 2020/10/10 15:42
# Description :
'''
1、使用len()函数计算序列的长度，即返回序列包含多少个元素；
2、使用max()函数返回序列中的最大元素；
3、使用min()函数返回序列中的最小元素。
'''
num = [7,14,21,28,35,42,49,56,63]
print("序列num的长度为",len(num))                     # 计算列表的长度
print("序列",num,"中的最大值为",max(num))             # 计算列表中的最大元素
print("序列",num,"中的最小值为",min(num))             # 计算列表中的最小元素

# 除了上面介绍的3个内置函数外，python还提供了如下内置函数。
'''
list()                      将序列转换为列表
str()                       将序列转换为字符串
sum()                       计算元素和
sorted()                    对元素进行排序
reversed()                  反向序列中的元素
enumerate()                 将序列组合为一个索引序列，多用在for循环中    
'''
