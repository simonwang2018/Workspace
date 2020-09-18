#append()向列表末尾增加一个元素
#extend()向列表末尾增加多个元素
#insert()在列表中的某个位置增加一个元素，不一定是在列表末尾。可以在列表任何地方。
letters = ['a','b','c','d','e']
letters.append('n')
letters.append('g')
print (letters)
#extend如果是向列表只加一个元素，可以不使用中括号，如果是增加多个元素，必须使用中括号。
letters.extend(['p','q','r'])
print (letters)
#将字母z增加到索引为2的位置，它后面的每一个元素都会向后移一个位置。
letters.insert(2,'z')
print(letters)
