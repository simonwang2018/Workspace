# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 025 对列表进行排序：1.1使用列表对象的sort()方法.py
# Author      : Simon
# Time        : 2020/10/21 15:04
# Description :
'''
列表对象提供了sort()方法用于对原列表中的元素进行排序。排序后原列表中的元素顺序将发生改变。语法格式如下：
listname.sort(key=None,reverse=False)
参数说明：
lisatname:表示要进行排序的列表。
key:表示指定从每个元素中提取一个用于比较的键（例如，设置“key=str.lower”表示在排序时不区分字母大小）。
reverse:可选参数，如果将其值指定为True,则表示降序排列；如果为False，则表示为升序排列，默认为升序排列。
如下代码：
'''
grade = [98,99,97,100,100,96,94,89,95,100]            # 10名学生的语文成绩列表
print('原列表：',grade)
grade.sort()                                          # 进行升序排列
print('升序：',grade)
grade.sort(reverse=True)                              # 进行降序排列
print('降序:',grade)

'''
使用sort()方法进行数值列表的排序比较简单，但是使用sort()方法对字符串列表进行排序时，采用的规则是先对大写字母排序，然后再对小写字母排序。
如果想要对字符串列表进行排序（不区分大小写时），需要指定其key参数。例如，定义一个保存英文字符串的列表，然后应用sort()方法对其进行升序排
列，可以使用下面的代码：
'''
char = ['cat','Tom','Angela','pet']
char.sort()                                           # 默认区分字母大小写
print('区分字母大小写：',char)
char.sort(key=str.lower)                              # 不区分字母大小写
print('不区分字母大小写：',char)

# 说明：使用sort()方法对列表进行排序时，对中文支持不好，不能直接使用这个。
