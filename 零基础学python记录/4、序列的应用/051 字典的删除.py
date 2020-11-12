# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 051 字典的删除.py
# Author      : Simon
# Time        : 2020/11/12 16:36
# Description :
a=1
'''
同列表和元组一样，不现需要的字典也可以命名用del命令删除整个字典。例如，通过下面的代码即可将已经定义的字典删除。
'''
name = ['绮梦','冷一','香香','兰兰']               # 作为键的列表
sign = ['水瓶座','射手座','双子座','双鱼座']        # 作为值的列表
dictionary = dict(zip(name,sign))                # 转换为字典
del dictionary

'''
另外，如果只想删除字典的全部元素，可以使用字典对象的clear()方法实现。执行clear()方法后，原字典将变为空字典。如下：
'''
name = ['绮梦','冷一','香香','兰兰']               # 作为键的列表
sign = ['水瓶座','射手座','双子座','双鱼座']        # 作为值的列表
dictionary = dict(zip(name,sign))                # 转换为字典
dictionary.clear()
print(dictionary)
'''除了上面介绍的方法可以删除字典元素，还可以使用字典对象的pop()方法删除并返回指定“键”的元素，以及使用字典对象的popitem（）方法
删除并返回字典中的一个元素。'''
