#在Python中，有两种除法，一种除法是/：
>>> 10 / 3
3.3333333333333335
#/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
>>> 9 / 3
3.0
#还有一种除法是//，称为地板除，两个整数的除法仍然是整数：

>>> 10 // 3
3
#你没有看错，整数的地板除//永远是整数，即使除不尽。要做精确的除法，使用/就可以。
#因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：

>>> 10 % 3
1
#无论整数做//除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的。