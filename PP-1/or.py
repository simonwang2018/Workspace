#or关键字也是用来把多个条件放在一起。如果使用or，只要任意一个条件为真，就会执行代码块。
color = input('Enter your favorite color:')
if color == 'red' or color == 'blue' or color == 'green':
    print ('You are allowed to play this game.')
else:
    print ("Sorry,you can't play the game.")
my_number = 7
if my_number < 20:
    print ('Under 20')
else:
    print ('20 or over')
