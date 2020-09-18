#使用not把比较倒过来，表示相反的逻辑
age = float(input('Enter your age:'))
if not (age < 8):#与if age >= 8的含义是一样的。
    print ('You are allowed to play this game.')
else:
    print ("Sorry,you can't play this game.")
