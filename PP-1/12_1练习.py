#创建5个名字，将他们包含在一个列表中，然后打印出来。
namelist = []#创建一个空列表
print ('Enter 5 names(press the Enter key after each name):')
for i in range (5):#此处的索引5表示上边输入5个名字
    name = input()
    namelist.append(name) #向列表添加元素
print ('The names are',namelist)
namelist.sort()
print (namelist)
print ('The third name you entered is:',end = '')
print (namelist[2])
