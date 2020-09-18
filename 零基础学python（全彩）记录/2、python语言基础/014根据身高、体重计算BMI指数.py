# !/usr/bin/python
# -*- coding:utf-8 -*-
# @File     : 014根据身高、体重计算BMI指数.py
# @Author   : Simon
# @Time     : 2020/9/17 10:35
#在下面的代码中，str()函数用于将数值转换为字符串，if语句用于进行条件判断。
height = 1.70                          #保存身高的变量，单位：米
print('您的身高：' + str(height))
weight = 60.5                          #保存体重的变量，单位：千克
print('您的体重：' + str(weight))
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
