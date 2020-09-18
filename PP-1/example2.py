#计算如果购买金额低于或等于10元，会给10%的折扣。大于等于10元，会给20%的折扣，再显示最终价格。
sum = float(input('Enter your buy sum:'))
if sum <= 10:
    print ('You have 10% discount!')
    buysum = sum - sum * 0.1
    print (buysum)
if sum >= 10:
    print ('You have 20% discount!')
    buysum = sum - sum * 0.1
    print (buysum)
