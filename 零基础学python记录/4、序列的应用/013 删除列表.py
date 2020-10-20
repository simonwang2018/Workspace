# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 013 删除列表.py
# Author      : Simon
# Time        : 2020/10/20 10:27
# Description :
'''
对于已经创建的列表，不再使用时，可以使用del语句将其删除。语法格式如下：
del listname
其中，listname为要删除列表的名称。
说明：del语句在实际开发时，并不常用。因为python自带的垃圾回收机制会自动销毁不用的列表，所以即使不手动将其删除，python也会自动将其回收。
'''
# 例如，定义一个名称为team的列表，然后再应用del语句将其删除，可以使用下面的代码：
team = ['皇马','罗马','拜仁']
del team
