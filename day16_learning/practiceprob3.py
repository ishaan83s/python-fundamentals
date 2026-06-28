#Create a class Order which stores item & its price.
#Use dunder function __gt__() to convey that:
#Order1 > order 2,  if the price of order 1 > price of order 2

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,order2): #GREATER THAN DUNDER FUNCTION (>) 
        return self.price > order2.price



ord1 = Order(1,150)
ord2 = Order(1,250)

print(ord1>ord2)