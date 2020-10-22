# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 031 实例：使用二维列表输出不同版式的古诗.py
# Author      : Simon
# Time        : 2020/10/22 14:35
# Description :
'''在该文件中首先定义4个字符串，并定义一个二维列表，然后应用嵌套的for循环将古诗以横版方式输出，再将二维列表进行逆序排列，最后应用嵌套
的for循环将古诗以竖版方式输出，代码如下：'''
str1 = '千山鸟飞绝'
str2 = '万径人踪灭'
str3 = '孤舟蓑苙翁'
str4 = '独钓寒江雪'
verse = [list(str1),list(str2),list(str3),list(str4)]                # 定义一个二维列表
print('\n-- 横版 --\n')
for i in range(4):                                                   # 循环古诗的每一行
    for j in range(5):                                               # 循环每一行的每个字（列）
        if j == 4:                                                   # 如果是一行中的最后一个字
            print(verse[i][j])                                       # 换行输出
        else:
            print(verse[i][j],end='')                                # 不换行输出
verse.reverse()                                                      # 对列表进行逆序排列
print('\n-- 竖版 --\n')
for i in range(5):                                                   # 循环每一行的每个字（列）
    for j in range(4):                                               # 循环新逆序排列后的第一行
        if j == 3:                                                   # 如果是最后一行
            print(verse[j][i])                                       # 换行输出
        else:
            print(verse[j][i],end='')                                # 不换行输出

'''
说明：在上面的代码中，list()函数用于将字符串转换为列表；列表对象的reverse()方法用于对列表进行逆序排列，即将列表的最后一个元素移到第
一个，倒数第二个元素移到第二个，以此类推。
'''