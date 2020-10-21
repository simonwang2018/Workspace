# !/usr/bin/python
# -*- coding:utf-8 -*-
# File        : 023 获取指定元素首次出现的索引位置.py
# Author      : Simon
# Time        : 2020/10/21 11:31
# Description :
'''
使用列表对象的index()方法可以获取指定元素在列表中首次出现的位置（即索引）。基本语法格式如下：
listname.index(obj)
参数说明：
listname:表示列表的名称。
obj：表示要查找的对象，这里只能精确匹配。
返回值：首次出现的索引值。
例如下面的代码：
'''
song = ['云在飞','我在诛仙','送你一匹马','半壶纱','云在飞','遇见你','等了那么久']
position = song.index('半壶纱')
print(position)

'''上面的代码运行后，将显示3，表示“半壶纱”在列表song中首次出现的索引位置是3。'''
