# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 019 实例：向NBA名人堂列表中追加新进球星.py
# Author      : Simon
# Time        : 2020/10/20 15:48
# Description : 先定义一个保存NBA名人堂原有球星名字的列表，然后创建一个保存2018新进球星名字列表，再调用列表对象extend（）追加元素。
oldlist = ['乔丹','阿布','奥拉','巴克','姚明']
newlist = ['基德','纳什','希尔']
oldlist.extend(newlist)
print(oldlist)
