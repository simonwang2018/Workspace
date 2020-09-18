#这里要求my_price变成全局变量后，打印出来的都是一样的值
def calculatetax (price,tax_rate): #函数计算税额，并返回总价格
    total = price + (price * tax_rate)
    global my_price 
    my_price = 10000 #在函数内部修改变量
    print ('my_price(局部变量) = ',my_price)#从函数内打印
    return total #将结果发回给主程序
my_price = float(input('Enter a Price:'))
totalprice = calculatetax(my_price,0.06) #调用函数并把结果保存在totalprice
print ('price = ',my_price,'total price = ',totalprice )
print ('my_price (全局变量)= ',my_price) #从函数外打印
