numblocks = int(input('How many blocks of stars do you want?'))
for block in range (1,numblocks + 1):
    print('block =',block)#打印block的数值，分辩是执行到哪一个block。
    for line in range (1,block * 2):
        for star in range (1,(block + line) * 2):
            print('*',end = '')
        print('line =',line,'star = ', star) #打印line与star，这样更加好分辩它们之间的数值。
    print()