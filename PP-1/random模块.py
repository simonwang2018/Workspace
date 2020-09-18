#random模块用于生成随机数。这在游戏和仿真中非常有用。
#每次使用random.randint（）时，会得到一个新的随机整数。由于我们为它传递的参数是0和100，所以得
#到的整数会介于0到100之间。而random.random()总是会提代一个介于0到1之间的随机小数，不用在括
#号里放任何参数。
import random
print (random.randint(0,100))
print (random.randint(0,100))
print (random.random())
print (random.random())
#如果使用random.random()，你想得到其它范围内的一个随机数，比如说0到10之间，只需要将结果乘以10.
print (random.random() * 10)