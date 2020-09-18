#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
print('I\'m \"ok\"!') 
print('I\'m ok.')
print('I\'m learning\nPython.')
print('\\\n\\')
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')
#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容pygame.examples.aliens.main()
#'''...'''是在交互式命令行下使用才有效，...是提示符，不是自己输入的，而是换行后自动提示的。
print('''line1
... line2
... line3''')
#如果将上边的写成程序存成Py就如下格式
print('''line1
line2
line3''')
