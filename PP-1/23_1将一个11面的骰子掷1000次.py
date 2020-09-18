import random
totals = [0,0,0,0,0,0,0,0,0,0,0,0,0]#列表包含13项，索引从0到12
for i in range (1000):
    dice_total = random.randint(2,12)
    totals[dice_total] += 1 #将这个总数自增1

for i in range (2,13):
    print('total', i, 'cqme up', totals[i], 'times')
