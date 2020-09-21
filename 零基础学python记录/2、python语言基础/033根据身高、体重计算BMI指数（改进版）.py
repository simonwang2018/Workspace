# !/usr/bin/python
# -*- coding:utf-8 -*-
# @File     : 033根据身高、体重计算BMI指数（改进版）.py
# @Author   : Simon
# @Time     : 2020/9/21 9:43
height = float(input('请输入您的身高（单位为米）：'))                          #保存身高的变量，单位：米
weight = float(input('请输入您的体重（单位为千克）：'))                          #保存体重的变量，单位：千克
bmi = weight/(height * height)         #用于计算BMI指数，公式：BMI=体重/身高的平方
print('您的BMI指数为：' + str(bmi))        #输出BMI指数
#判数身材是否合理
if bmi < 18.5:
    print('您的体重过轻 ~@_@~')
if bmi >= 18.5 and bmi < 24.9:
    print('正常范围，注意保持 （-_-）')
if bmi >= 24.9 and bmi <29.9:
    print('您的体重过重 ~@_@~')
if bmi >= 29.9:
    print('肥胖 ^@_@^')
