#while循环也称为条件循环，条件循环会在满足某个条件时一直保持循环。
print('Type 3 to continue,anything else to quit.')
someinput = input()
while someinput == '3':
    print('Thank you for the 3.Very kind of you.')
    print('Type 3 to continue,anything else to quit.')
    someinput = input()
print("That's not 3,so I'm quitting now.")
