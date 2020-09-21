# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 037根据总步数计算消耗的热量值.py
# Author      : Simon
# Time        : 2020/9/21 10:59
# Description : 由于行走速度不同，计算卡路里的消耗也不同，这里假设走一步消耗28卡路里。
step_number = int(input("请输入当天行走的步数!\n"))
calorie = int(step_number) * 28
print("今天共消耗卡路里：", calorie ,"(即",calorie/1000, "千卡)")
