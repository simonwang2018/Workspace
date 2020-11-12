# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 047 实例04：使用dict创建一个保存星座的字典.py
# Author      : Simon
# Time        : 2020/11/12 16:09
# Description : 有4个人，将他们每个人的星座对应保存在另一个列表中。
name = ['绮梦','冷一','香香','兰兰']               # 作为键的列表
sign = ['水瓶座','射手座','双子座','双鱼座']        # 作为值的列表
dictionary = dict(zip(name,sign))                # 转换为字典
print(dictionary)                                # 输出转换后字典

