#inheritance
class Parent:
    


    def mobile(self):
        print("iphone")

    def car(self):
        print("swift")

    def bike(self):
        print("passionpro")

class child(Parent):

    pass

obj=child()
# obj.mobile()
# obj.bike()

#method overriding
class Mobile(object):#is A
    name:str
    price:int
    display:str

    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.price=kwargs.get("price")
        self.display=kwargs.get("display")

    def __str__(self):
        return self.name
    
    @property#decorators
    def get_price(self):
        return self.price
    
    @property
    def get_dis_price(self):
        return self.price-1000
    
obj=Mobile(name="oneplus",price=30000,dislpay="amoled")
# print(obj)

#decorators
print(obj.get_price)
print(obj.get_dis_price)




