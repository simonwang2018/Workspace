classmates = ['Michael','Bob','Tracy'] #列表，从0，1，2...开始，第一个字符串是0开始
len(classmates)  #len()函数可以获得list元素的个数；
print(classmates)
#列表是一个可变的有序表，可以往列表中追加元素到末尾；
classmates.append('Adam')
print(classmates)
#也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1,'Jack')
print(classmates)
#要删除list末尾的元素，用pop()方法：
classmates.pop()
print(classmates)
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
print(classmates)
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'
print(classmates)
#可变元组,这个元组定义的时候有3个元素，分别是a,b和一个列表。
t = ('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
