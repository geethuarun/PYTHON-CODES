from datetime import date

class Operations:

    num1:str
    num2:str

    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2

    def add(self):
        return self.num1+self.num2
    
    @staticmethod
    def get_date():
        return date.today()
    
op=Operations(1,2)
print(op.add())
print(Operations.get_date())#while using static method class is called instead of object



class Parent:

    
    def vehicles(self):
        self.context=["passion","swift"]
        return self.context
class child(Parent):
    def vehicles(self):
        self.context=super().vehicles()
        self.context.append("hunter")
        return self.context
obj=child()
print(obj.vehicles())
