class GameObject: #定义GameObject类
    def __init__(self,name):
        self.name = name
    def pickUp(self):
        pass
        # put code here to add the object
        # to the player's collection
class Coin(GameObject): #Coin是GameObject的子类
    def __init__(self,value):
        GameObject.__init__(self) #在_init_()中，继承GameObject的初始化并补充新内容
        self.value = value
    def spend(self,buyer,seller): #Coin类新的spend()方法
        pass
        # put code here to remove the coin
        # from the buyer's money and
        # add it to the seller's money