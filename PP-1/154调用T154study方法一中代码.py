#调用T154study模块的文件
import time
import T154study
for i in range(1,11):
    time.sleep(3)
    print ("第",i,"次","第",i * 3,"秒","随机打印一个小数:", end = ' ')
    T154study.randomprint()
