class GameObject:

    def __init__(self, name):
        self.name = name

    def pickUp(self, player):
        # put code here to add the object
        # to the player's collection


class Coin(GameObject):

	    def __init__(self, value):
        GameObject.__init__(self, "coin")  # 在__init__()中，继承GameObject的初始化方法
        self.value = value                 # 并补充新内容

    def spend(self, buyer, seller):
        # put code here to remove the coin
        # from the buyer's money and
        # add it to the seller's money
