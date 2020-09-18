#使用and 就是必须所有条件都为真，才能执行if语句为真。
# 假设你要为8岁以上的人创建一个游戏，另外你希望玩家至少上三年级。这就要满足两个条件。下面测试。
#或者再加一个条件，就是要所有条件都为真，这个if语句才能为真
age = float(input('Enter your age:'))
grade = int(input('Enter your grade:'))
color = input('Enter you favorite color:')
if age >= 8:
    if grade >= 3:  # 每一个if都需要自己的代码块,所以print所都要缩进4个空格。
        if color == 'green':
#if age >= 8 and grade >= 3:#上边两行的代码可以写成这样。
#if age >= 8 and grade >= 3 and color == 'green':#上边三条可以写成这样。
            print('You can play this game!')
else:
    print('Sorry,you can not play this game!')
