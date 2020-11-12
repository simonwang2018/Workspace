# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 041 修改元组元素.py
# Author      : Simon
# Time        : 2020/11/12 10:05
# Description :
coffeename = ('蓝山','卡布奇诺','曼特宁','摩卡','麝香猫','哥伦比亚')            # 定义元组
#coffeename[4] = '拿铁'
print(coffeename)
'''
上面的运行结果会报错，因为元组是不可变序列，所以我们不能对它的单个元素值进行修改。但是元组也不是完全不能修改。我们可以对元组进行重新赋值。
如下代码：
'''
coffeename = ('蓝山','卡布奇诺','曼特宁','摩卡','麝香猫','哥伦比亚')            # 定义元组
print(coffeename)
coffeename = ('蓝山','卡布奇诺','曼特宁','摩卡','拿铁','哥伦比亚')              # 对元组进行重新赋值
print('新元组',coffeename)
'''
还可以对元组进行连接组合。在进行元组连接时，连接的内容必须都是元组。不能将元组和字符串或者列表进行连接。另外，在进行元组连接时，如果要连
接的元组只有一个元素时，一定不要忘记后面的逗号。
'''
ukguzheng = ('蓝山','卡布奇诺','曼特宁','摩卡')
print('原元组:',ukguzheng)
ukguzheng = ukguzheng + ('麝香猫','哥伦比亚')
print('组合后:',ukguzheng)
