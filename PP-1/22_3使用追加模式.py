#写文件完成时一定要使用close()。这是因为，只有使用close关闭文件，所作的修改才会真正保存到文件。
todo_list = open ('notes.txt','a') #以追加模式打开文件
todo_list.write ('\nSpend allowance')#以追加模式打开文件
todo_list.close() #关闭文件