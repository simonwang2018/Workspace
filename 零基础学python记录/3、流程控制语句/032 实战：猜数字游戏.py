# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 032 实战：猜数字游戏.py
# Author      : Simon
# Time        : 2020/9/23 13:18
# Description : 编写一个猜数字的小游戏，随机生成一个1到10之间（包括1和10）的数字作为基准数，玩家每次通过键盘输入一个灵敏字，如果输入的
# 数字和基准数相同，则成功过关，否则重新输入。如果玩家输入-1，则表示退出游戏。
print("------------猜数字游戏------------\n")
print("请输入1~10之间的任意一个数：\n")
for total in range(1,11):
    if total == 9:
        print("恭喜你，你赢了，猜中的数字是：9")
    elif total < 9:
        print("太小，请重新输入：")
    elif total > 9:
        print("太大，请重新输入：")
        break


