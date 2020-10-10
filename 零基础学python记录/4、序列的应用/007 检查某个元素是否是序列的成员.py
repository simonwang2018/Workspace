# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 007 检查某个元素是否是序列的成员.py
# Author      : Simon
# Time        : 2020/10/10 15:35
# Description :
'''在Python中，可以使用in关键字检查某个元素是否为序列的成员，即检查某个元素是否包含在某个序列中。语法格式如下：
value in sequence
其中，value表示要检查的元素，sequence表示指定的序列。'''
# 如检查名称为num1的序列中，是否包含元素“3”，可以使用下面的代码：
num1 = ['1','2','3','4']
print('3' in num1)

# 运行上面的代码，将显示结果为True,表示在序列中存在指定的元素。
# 另外，在python中，也可以使用not in关键字实现检查某个元素是否不包含在指定的序列中。如下，将显示结果为Fale.
num1 = ['1','2','3','4']
print('3' not in num1)

