# 建立一个可以挣利息的类，名为InterestAccount。这应当是BankAccount的一个子类
#（所以会继承BankAccount的属性和方法）。InternetAccount还应当有一个对应利息率的属性，另外有
# 一个方法来增加利息。为了力求简单，假设每年会调用一次addInternet()方法计算利息并更新余额
class BankAccount:
    def __init__(self,account_name,account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.account_overage = 0.0

    def ShowOverage(self):
        print ("The account balance is ",self.account_overage)

    def Save(self,money):
        self.account_overage = self.account_overage + money
        print ("You save ",money)
        print ("The new overage is ",self.account_overage)

    def Withdrawal(self,money):
        if self.account_overage >= money:
            self.account_overage = self.account_overage - money
            print ("You withdrawal ",money)
            print ("The new overage is ",self.account_overage)
        else:
            print ("You tried to withdrawal",money)
            print ("Your balance is",self.account_overage)
            print ("No enough funds")

class InterestAccount(BankAccount):
    def __init__(self, interest_rate):
        BankAccount.__init__(self, "muyu", 123456)#继承BankAccount类
        self.interest_rate = interest_rate

    def addInterest(self):
        interest = self.account_overage * self.interest_rate
        print ("Your interest is",interest)
        print ("Your overall funds is",interest+self.account_overage)

myAccount = InterestAccount(0.2)
myAccount.Save(100)
myAccount.Withdrawal(20.5)
myAccount.Withdrawal(50)
myAccount.addInterest()