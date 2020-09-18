from my_module import c_to_f #替代import my_module
celsius = float(input('Enter temperature in Celsius:'))
fahrenheit = c_to_f(celsius) #这里其中c_to_f替代了my_module.c_to_f，使得前边不用加模块名。
print ("That's",fahrenheit,"degrees Fahrenheit")