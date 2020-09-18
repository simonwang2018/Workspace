#readlin()方法一次只读取一行，所以它不会把结果放入一个列表。每次使用时，都只得到一个字符串。
my_file = open ('notes.txt','r')
first_line = my_file.readline()
second_line = my_file.readline()
my_file.seek(0) #找到文件中你指示的位置。括号中的数字就是从文件起始位置算起的字节数。设置
#为0，就会回到文件的起始位置。
first_line_again = my_file.readline()
print ('first line = ', first_line)
print ('second line = ', second_line)
my_file.close()