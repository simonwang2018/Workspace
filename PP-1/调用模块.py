#此处调用的是同文件夹的my_module.py文件。注意必须放在同一个文件夹下。
import my_module #my_module包含c_to_f()函数
celsius = float(input('Enter a temperature in Celsius:'))
fahreheit = my_module.c_to_f(celsius) #此条注意my_module.如果不加就会提示找不到函数。
print ("That's", fahreheit,"degrees Fahrenheit")
