#创建5个名字，将他们包含在一个列表中，然后打印出来。
namelist = []#创建一个空列表
print('Enter 5 names(press the Enter key after each name):')
for i in range (5):#此处的索引5表示上边输入5个名字
    name = input()
    namelist.append(name) #向列表添加元素
print ('The names are',namelist)
del namelist[3] #删除列表中索引3的元素
int(input("Replace one name.Which one?(1-5):"))
namelist.insert(3, 'Peter') #在索引3的位置插入一个元素
print ('New name:',end = '')
print (namelist[3])
print (namelist)
