# !/usr/bin/python
# -*- coding:utf-8 -*-
# @File     : 016字符串类型.py
# @Author   : Simon
# @Time     : 2020/9/17 10:57
'''字符串就是连续的字符序列，可以是计算机所能表示的一切字符的集合。在python中，字符串属于不可变序列，通常使用单引号，双引号或者三引号括
起来。这三种引号形式在语义上没有差别，只是在形式上有些差别。其中单引号和双引号中的字符序列必须在一行上，而三引号内的字符序列可以分部在连
续的多行上。'''
title = '我喜欢的名言警句'                            #使用单引号，字符串内容必须在一行
mot_cn = '命运给予我们的不是失望之酒，而是机会之杯。'    #使用双引号，字符串内容必须在一行。
#使用三引号，字符串内容可以分布在多行
mot_en = '''Our destiny offers not the cup of despair,
but the chance of opportunity.'''
print(title)
print(mot_cn)
print(mot_en)
