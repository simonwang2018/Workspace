#为BankAccount建立一个类定义。它应该有一些属性，包括账户名（一个字符串）、账号（一个字符串或整数）
#和余额（一个浮点数），另外还要有一些方法显示余额、存钱和取钱。
class BankAccount:
    def __init__(self,account_name,account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.account_overage = 0.0
    def ShowOverage(self):
        print ('The account balance is ',self.account_overage)
    def Save(self,money):
        self.account_overage = self.account_overage + money
        print ('You save',money)
        print ('The new overage is ',self.account_overage)
    def Withdrawal(self,money):
        if self.account_overage >= money:
            self.account_overage = self.account_overage - money
            print ('You withdrawal',money)
            print ('The new overage is ',self.account_overage)
        else:
            print ('You tried to withdrawal ',money)
            print ('Your balance is ',self.account_overage)
            print ('No enough funds')
myAccount = BankAccount('mumu',12345678)
print ('Account name',myAccount.account_name)
print ('Account number',myAccount.account_number)
myAccount.ShowOverage()
myAccount.Save(100)
myAccount.Withdrawal(20.5)
myAccount.Withdrawal(50)
