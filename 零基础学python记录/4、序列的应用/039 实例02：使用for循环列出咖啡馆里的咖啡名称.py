# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 039 实例02：使用for循环列出咖啡馆里的咖啡名称.py
# Author      : Simon
# Time        : 2020/11/12 9:40
# Description : 应用for循环语句输出每个元组元素的值，并且在后面加上“咖啡”二字。
coffeename = ('蓝山','卡布奇诺','曼特宁','摩卡','麝香猫','哥伦比亚')            # 定义元组
print("您好，欢迎光临 ~ 伊米咖啡馆 ~ \n\n我店有: \n")
for name in coffeename:                                                    # 遍历元组
    print(name + '咖啡',end = ' ')

'''
另外，元组还可以使用for循环和enumerate（）函数结合进行遍历。
enumerate（）函数用于将一个可遍历的数据对象（如列表或元组）组合一个索引序列，同时列出数据和数据下标，一般在for循环中使用。
'''