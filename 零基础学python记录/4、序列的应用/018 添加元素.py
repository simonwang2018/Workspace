# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 018 添加元素.py
# Author      : Simon
# Time        : 2020/10/20 11:27
# Description :
'''
使用列表对象的append()方法实现添加元素，用于在列表的末尾追加元素，语法格式如下：
listname.append(obj)
其中，listname为要添加元素的列表名称，obj为要添加到列表末尾的对象。
'''
# 例如，定义一个包括4个元素的列表，应用append()向该列表的末尾添加一个元素，可以使用下面的代码：
phone = ['摩托罗拉','诺基亚','三星','OPPO']
len(phone)
phone.append('IPhone')
len(phone)
print(phone)

''' 列表对象除了提供append()方法可以向列表中添加元素，还提供了Insert()方法也可以向列表中添加元素。该方法用于向列表的指定位置插入元素。
但是由于该方法的执行效率没有append()方法高，所以不推荐这种方法。'''

'''上面介绍的是向列表中添加一个元素，如果想要将一个列表中的全部元素添加到另一个列表中，可以使用列表对象的extend()方法实现。
extend()方法的语法如下：
listname.extend(seq)
其中，listname为原列表，seq为要添加的列表。语句执行后，seq的内容将追加到listname的后面。
'''
