#布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，在Python中，
# 可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来.
>>> True
True
>>> False
False
>>> 3 > 2
True
>>> 3 > 5
False
#布尔值可以用and、or和not运算。and运算是与运算，只有所有都为True，and运算结果才是True
>>> True and True
True
>>> True and False
False
>>> False and False
False
>>> 5 > 3 and 3 > 1
True
#or运算是或运算，只要其中有一个为True，or运算结果就是True
>>> True or True
True
>>> True or False
True
>>> False or False
False
>>> 5 > 3 or 1 > 3
True
#not运算是非运算，它是一个单目运算符，把True变成False，False变成True
>>> not True
False
>>> not False
True
>>> not 1 > 2
True
#布尔值经常用在条件判断中，比如：
if age >= 18:
    print('adult')
else:
    print('teenager')


