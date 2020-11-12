# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 045 字典的创建和删除.py
# Author      : Simon
# Time        : 2020/11/12 15:44
# Description :
'''
定义字典时，每个元素都包含两个部分“键”和“值”。以水果名称和价格的字典为例，键为水果名称，值为水果价格。如下：
                 值 --->  6.5        4      3        11.8     5
                 键 --->  apple   orange  banana    peach    pear
创建字典时，在“键”和“值”之间使用冒号分隔，相邻两个元素使用逗号分隔，所有元素放在一对“｛｝”中。语法格式如下：
dictionary = {'key1':'value1','key2':'value2', ...,'keyn':'valuen',}
参数说明：
dictionary：表示字典名称。
key1、key2...keyn：表示元素的键，必须是唯一的，并且不可变，例如，可以是字符串、数字或者元组。
value1、value2...valuen:表示元素的值，可以是任何数据类型，不是必须唯一的。
例如，创建一个保存通迅录信息的字典，可以使用下面的代码：
'''
dictionary = {'qq':'81223311','深圳':'88988212','无语':'83223392'}
print(dictionary)
# 同列表和元组一样，也可以创建空字典。在python中，可以使用下面两种方法创建空字典：
dictionary = {}
print(dictionary)
# 或者
dictionary = dict()

# dict()方法除了可以创建一个空字典外，还可以通过已有数据快速创建字典。
