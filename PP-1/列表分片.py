#列表分片(切片),索引使用冒号隔开
letters = ['a','b','c','d','e']
print (letters[1:4]) #打印出来是‘b’,'c','d'，这里从第一个索引开始，在达到最后一个之前停止。
print (letters[1]) #此处列表索引取回来的值是b，取回来的是一个元素。
print (letters[1:2])#列表分片取回来的是更小的值‘b’，这个分片是原列表的部分副本。
print (type(letters[1])) #查看索引列表1的类型是字符串
print (type(letters[1:2])) #查看列表分片1的类型是列表
#分片简写,简写方法是使用冒号
print(letters[:2])#冒号前面没有数字，这样就会得到从列表起始位置开始一直到指定索引之间的所有元素
print(letters[2:])#冒号后面没有数字，就会得到从指定索引到列表末尾的所有元素。
print(letters[:])#没有放入任何数，只有冒号，就可以得到整个列表。
#修改元素，可以使用索引来修改某个列表元素
print(letters)
letters[2] = 'z' #使用索引列表修改第3个元素
#letters[5] = 'f' 这条是错误的，不能使用索引之引列表增加新的元素
letters.append('f') #利用append来增加元素，增加的是在列表最末尾
print(letters)
