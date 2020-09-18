#循环嵌套，深度为3.
numblocks = int(input('How many blocks of stars do you want?'))
numlines = int(input('How many lines in each block?'))
numstars = int(input('How many stars per line?'))
for block in range (0,numblocks): #block循环
    for line in range (0,numlines):#line循环
        for star in range (0,numstars):#star循环
            print('*',end = '')
        print()
    print()