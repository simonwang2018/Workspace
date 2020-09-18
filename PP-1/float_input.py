temp_string = input('Enter your number:')
fahrenheit = float(temp_string)
# 以上两条是用户输入字符串，然后由这个字符串创建一个数。
#fahrenheit = float(input('Enter your nember:')) #这一条可以代替上边的两条。
print(fahrenheit)
# 下边是测试例子
print('This program converts fahrenheit go celsius')
print('Type in a temperature in fahrenheit:')
fahrenheit = float(input())
celsius = (fahrenheit - 32) * 5.0 / 9
print('that is',celsius,'degrees celsius')
