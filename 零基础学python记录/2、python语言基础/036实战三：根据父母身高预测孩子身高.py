# !/usr/bin/python
# -*- coding:utf-8 -*-
# @File     : 036实战三：根据父母身高预测孩子身高.py
# @Author   : Simon
# @Time     : 2020/9/21 10:07
father_height = float(input("请输入父亲的身高："))
mother_height = float(input("请输入母亲的身高："))
child_height = (father_height + mother_height) * 0.54
print("预测儿子身高为：",child_height)

