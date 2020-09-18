#询问用户想要多少行，以及每行希望有多少个星号。
numlines = int(input('How many lines of stars do you want?'))
numstars = int(input('How many stars per line?'))
for line in range (0,numlines):
    for stars in range (0,numstars):
        print('*',end = '')#此处的end是让星号打在一行号上，在python2中是以逗号表示，python3不行。
    print()