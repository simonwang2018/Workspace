#使用写模式打开这个文件，并写入内容，原文件的内容会被删除。
the_file = open('notes.txt','w')
the_file.write('Wake up\n')
the_file.write('Watch cartoons')
the_file.close()