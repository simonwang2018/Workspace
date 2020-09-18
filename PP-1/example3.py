#寻找10至12岁之间的女孩加入球队，询问年龄和性别。合理建立程序，不是女孩就不必询问年龄。
gender = input('Enter your gender:')
if gender != 'female':
    print ("You can't join this team! ")
else:
    age = int(input('Enter your age:'))
    if 10 <= age <= 12:
        print ('You can join this team!')
    else:
        print("You can't join this team!")