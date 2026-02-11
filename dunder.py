class Order():
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,or2):
        return self.price>or2.price
or1=Order("ball",40)
or2=Order("stumper",30)
print(or1>or2)