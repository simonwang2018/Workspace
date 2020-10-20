# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 017 实例：分两列显示NBA西部联盟前八名的球队.py
# Author      : Simon
# Time        : 2020/10/20 11:13
# Description : 应用for循环和enumerate()函数遍历列表，在循环体中通过if...else语句判断是否为偶数，如果为偶数则不换行输出，否则换行输出。
print('2017~2018赛季NBA西部联盟前八名：')
team = ['火箭','勇士','波特兰','犹他','新奥尔良','马刺','马成','森林狼']
for index,item in enumerate(team):
    if index % 2 == 0:                              # 判断是否为偶数，为偶数时不换行
        print(item + '\t\t', end='')
    else:
        print(item + '\n')                         # 换行输出

# 说明：在上面的代码中，在第11行的print（）函数中使用end=''表示不换行输出，即下一条print()函数的输出内容会和这一内容在同一行输出。