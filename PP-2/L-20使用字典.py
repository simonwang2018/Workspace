#给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，列表越长，耗时越长。
names = ['Michael','Bob','Tracy']
scores = [95,75,85]
#如果用字典实现，只需要一个名字-成绩的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用python写一个字典如下：
d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])
