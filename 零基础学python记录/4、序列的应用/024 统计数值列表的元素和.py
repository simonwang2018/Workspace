# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 024 统计数值列表的元素和.py
# Author      : Simon
# Time        : 2020/10/21 11:36
# Description :
'''
在Python中，提供了sum()函数用于统计数值列表中各元素的和。语法格式如下：
sum(iterable[,start])
参数说明：
iteralbe:表示要统计的列表。
start:表示统计结果是从哪个数开始（即将统计结果加上start所指定的数），是可选参数，如果没有指定，默认值为0.
例如，定义一个保存10名学生语文成绩的列表，然后应用sum()函数统计列表中元素的和，即统计总成绩，然后输出，代码如下：
'''
grade = [98,99,97,100,100,96,94,89,95,100]            # 10名学生的语文成绩列表
total = sum(grade)
print("语文总成绩为：",total)
