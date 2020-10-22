# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 033 使用赋值运算符直接创建元组.py
# Author      : Simon
# Time        : 2020/10/22 14:58
# Description :
'''
1、同其他类型的python变量一样，创建元组时，也可以使用赋值运算符“=”直接将一个元组赋值给变量。语法格式如下：
tuplename = (element 1,element 2,element 3,...,element n)
其中，tuplename表示元组的名称，可以是任何符合Python命名规则的标识符；element 1、element 2、element 3、element n表示元组中的元素，
个数没有限制，并且只要为python支持的数据类型就可以。
注意：创建元组的语法与创建列表的语法类似，只是创建列表时使用的是“[]”，而创建元组时使用的是“（）”。
'''
'''例如，下面定义的都是合法的元组：'''
num = (7,14,34,32,53,24,89,12)
ukguzheng = ('渔舟唱晚','高山流水','出水莲')
untitle = ('python',28,('人生苦短，学python'),['爬虫','自动化运维'])

# 在python中，元组使用一对小括号将所有的元素括起来，但是小括号并不是必须的，只要将一组值用逗号分隔开来，python就可以视其为元组。如下：
ukguzhen = '渔舟唱晚','高山流水','出水莲'

'''如果要创建的元组只包括一个元素，则需要在定义元组时，在元素的后面加一个逗号","例如下面的代码定义的就是包括一个元素的元组：'''
verse1 = ('一片冰心在玉壶',)                                    # 加了逗号是元组
print('verse1的类型为：',type(verse1))                         # 输出verse1变量的类型
verse2 = ('一片冰心在玉壶')                                    # 不加逗号输出的是字符串
print('verse2的类型为:',type(verse2))
