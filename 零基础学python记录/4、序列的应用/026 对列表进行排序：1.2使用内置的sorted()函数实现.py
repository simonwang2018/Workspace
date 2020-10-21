# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 026 对列表进行排序：1.2使用内置的sorted()函数实现.py
# Author      : Simon
# Time        : 2020/10/21 15:19
# Description :
'''
使用内置的sorted()函数对列表进行排序，原列表的元素顺序不变。语法格式如下：
sorted(iterable,key=None,reverse=False)
参数说明：
iterable:表示要进行排序的列表名称。
key:表示指定从每个元素中提取一个用于比较的键（例如，设置“key=str.lower”表示在排序时不区分字母大小）。
reverse:可选参数，如果将其值指定为True,则表示降序排列；如果为False，则表示为升序排列，默认为升序排列。
如下面的代码：
'''
grade = [98,99,97,100,100,96,94,89,95,100]            # 10名学生的语文成绩列表
grade_as = sorted(grade)                              # 进行升序排列
print("升序：",grade_as)
grade_des = sorted(grade,reverse=True)                # 进行降序排列
print('降序:',grade_des)
print('原序列：',grade)

'''
说明：列表对象的sort()方法和内置sorted（）函数的作用基本相同；不同点是在使用sort()方法时，会改变原列表的元素排列顺序，而使用sorted()
函数时，会建立一个原列表的副本，该副本为排序后的列表。
'''
