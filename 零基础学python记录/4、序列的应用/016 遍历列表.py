# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 016 遍历列表.py
# Author      : Simon
# Time        : 2020/10/20 10:55
# Description :
'''
1、直接使用for循环实现
直接使用for循环遍历列表，只能输出元素的值，语法格式如下：
for item in listname:
    # 输出item
其中，item用于保存获取到的元素值，要输出元素内容时，直接输出该变量即可；listname为列表名称。
'''
# 通过for循环遍历该列表，并输出各个球队的名称，代码如下：
print('2017~2018赛季NBA西部联盟前八名：')
team = ['休斯顿 火箭','勇士','波特兰','犹他','新奥尔良','马刺','马成','森林狼']
for item in team:
    print(item)

'''
2、使用for循环和enumerate()函数可以实现同时输出索引值和元素内容，语法格式如下：
for index,item in enumerate(listname):
    # 输出index和item
参数说明：
index:用于保存元素的索引。
item：用于保存获取到的元素值，要输出元素内容时，直接输出该变量即可。
listname:列表名称。
'''
# 通过for循环和enumerate()函数扁历列表，并输出索引和球队名称，代码如下：
print('2017~2018赛季NBA西部联盟前八名：')
team = ['休斯顿 火箭','勇士','波特兰','犹他','新奥尔良','马刺','马成','森林狼']
for index,item in enumerate(team):
    print(index + 1,item)


