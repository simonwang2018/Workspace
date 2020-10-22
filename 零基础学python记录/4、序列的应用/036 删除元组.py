# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 036 删除元组.py
# Author      : Simon
# Time        : 2020/10/22 17:27
# Description :
'''
对于已经创建的元组，不再使用时，可以使用del语句将其删除。语法格式如下：
del tuplename
其中，tuplename为要删除元组的名称。
说明：del语句在实际开发时，并不常用。因为Python自带的垃圾回收机制会自动销毁不用的元组，所以即使我们不手动将其删除，python也会自动将其
回收。
例如，定义一个名称为verse的元组，然后再应用del语句将其删除，可以使用下面的代码:
'''
verse = ('渔舟唱晚','高山流水','出水莲')
del verse
