#将打开一个目前硬盘上还没有的文件。写完后，将会在硬盘中多出一个新的文件。并包含下列内容。
new_file = open ('my_new_notes.txt','w')
new_file.write('Eat supper\n')
new_file.write('Play soccer\n')
new_file.write('Go to bed')
new_file.close()
