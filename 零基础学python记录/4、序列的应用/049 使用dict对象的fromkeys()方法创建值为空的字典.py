# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 049 使用dict对象的fromkeys()方法创建值为空的字典.py
# Author      : Simon
# Time        : 2020/11/12 16:22
# Description :
a =1
'''
通过dict对象的fromkeys()方法创建值为空的字典，语法如下：
dictionary = dict.fromkeys(list1)
参数说明：
dictionary：表示字典名称。
list1:作为字典的键的列表。
例如，创建一个只包括名字的字典，可以使用下面的代码：
'''
namelist = ['绮梦','冷一','香香','兰兰']                  # 作为键的列表
dictionary = dict.fromkeys(namelist)
print(dictionary)
