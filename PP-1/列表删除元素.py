#remove不需知道元素在列表中的哪个位置，只需确认它在列表中
letters = ['a','b','c','d','e']
letters.remove('c')
print(letters)
#del允许利用素引从列表中删除元素
del letters[3] #这里删除了第4个元素（素引3），也就是字母e。
print(letters)
#用pop删除元素,POP从列表取出最后一个元素交给你，删除列表末尾的元素。
letters = ['a','b','c','d','e']
lastletter = letters.pop()
print(['a','b','c','d'])
print(lastletter)
#使用pop还可以提供一个索引。弹出了第2个字母,即b.弹出的元素赋给second，而且会从letters删除。
#使用pop(i)方法删除指定位置的元素，其中i是素引位置。
letters = ['a','b','c','d','e']
second = letters.pop(1) #如果在pop()括后里没有提供参数时，pop会返回最后一个元素。
print(second)
print(letters)
