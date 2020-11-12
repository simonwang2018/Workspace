# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 040 实例03：使用for循环和enumerate函数遍历元组.py
# Author      : Simon
# Time        : 2020/11/12 9:54
# Description :
print('2017~2018赛季NBA西部联盟前八名\n')
team = ('火箭','勇士','波特兰','犹他','新奥尔良','马刺','马成','森林狼')
for index,item in enumerate(team):
    if index%2 == 0:                        # 判断是否为偶数，为偶数时不换行
        print(item + '\t\t', end='')
    else:
        print(item + '\n')                  # 换行输出
