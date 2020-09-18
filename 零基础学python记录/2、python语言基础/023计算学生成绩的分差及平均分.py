# !/usr/bin/python
# -*- coding:utf-8 -*-
# @File     : 023计算学生成绩的分差及平均分.py
# @Author   : Simon
# @Time     : 2020/9/18 15:18
python = 95                                #定义变量，存储python课程的分数
english = 92                               #定义变量，存储english课程的分数
c = 89                                     #定义变量，存储C语言课程的分数
sub = python - c                           #计算python课程和english课程的分数差
avg = (python + english + c) /3            #计算平均成绩
print('python课程和c语言课程的分之差：' + str(sub) + '分\n')
print('3门课的平均分：' + str(avg) + '分')
