#改变变量为全局。如果使用global关键字，Python不会建立名为my_price的局部变量，而是会使用名
#为my_price的全局变量。另外，如果还没有名为my_price的全局变量，python就会创建一个。
def calculatetax (price,tax_rate): #函数计算税额，并返回总价格
    global my_price   # 告诉python你想使用全局版本的my_price
