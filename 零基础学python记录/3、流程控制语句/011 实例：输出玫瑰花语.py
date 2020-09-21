# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 011 实例：输出玫瑰花语.py
# Author      : Simon
# Time        : 2020/9/21 15:41
# Description : 使用if...elif...else多分支语句实现根据用户输入的玫瑰花的朵数输出其代表的含义。
print("在古希腊神话中，玫瑰集爱情与美丽与一身，所以人们常用玫瑰来表达爱情。")
print("但是不同朵数的玫瑰花代表的含义是不同的。\n")
# 获取用户输入的朵数，并转换为整型
number = int(input("输入您想送几朵玫瑰花，小默会告诉你含义："))            # int（）函数用于将用户的输入强制转换成整型
if number == 1:                         # 判断输入的数是否为1，代表1朵
    # 如果等于1则输出提示信息
    print("1朵：你是我的唯一！")
elif number == 3:                       # 判断是否3朵
    print("3朵：I Love You!")
elif number == 10:                      # 判断是否10朵
    print("10朵：十全十美！")
elif number == 99:                      # 判断是否为99朵
    print("99朵：天长地久！")
elif number == 108:                     # 判断是否为108朵
    print("108朵：求婚！")
else:
    print("小默也不知道了！可以考虑送1朵、3朵、10朵、99朵或108朵哦！")
