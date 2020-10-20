# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 020 修改元素.py
# Author      : Simon
# Time        : 2020/10/20 16:39
# Description :
'''
修改列表中的元素只需要通过索引获取该元素，然后再为其重新赋值即可。例如，定义一个保存3个元素的列表，然后修改索引值为2的元素，代码如下：
'''
verse = ['长亭外','古道边','芳草碧连天']
print(verse)
verse[2] = '一行白鹭上青天'                      # 修改列表的第3个元素
print(verse)
