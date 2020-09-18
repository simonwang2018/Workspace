#做个海报，用数字显示如何订购热狗，小面包，番茄酱，芥末酱和洋葱的所有可能的组合。
#外循环（热狗）运行两次。
#对热狗循环的每一次迭代，小面包循环运行两次，所以它会运行2X2=4次。
#对小面包循环的每一次迭代，番茄酱循环运行两次，所以它会运行2X2X2=8次。
#依此类推。
#使用了制表符，也就是\t.
dog_cal = 140 #计算卡路里
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40
print('\tDog\tBun\tKetchup\tMustard\tOnions\tCalories')
count = 1
for dog in [0,1]: #热狗循环是外循环
    for bun in [0,1]:
        for ketchup in [0,1]:
            for mustard in [0,1]:
                for onion in [0,1]:
                    total_cal = (bun * bun_cal)+(dog * dog_cal)+(ketchup * ket_cal)+\
                                (mustard * mus_cal)+(onion * onion_cal)
                    # 这里反斜线\的意思是，长语句在一行里放不下，就可以使用反斜线\
                    print('#',count,'\t ',end = '')
                    print(dog,'\t',bun,'\t',ketchup,'\t',end = '')
                    print(mustard,'\t',onion,end ='')
                    print('\t',total_cal)
                    count = count + 1


