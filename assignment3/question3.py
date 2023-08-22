# Question3


class Square:
    side:str

    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2
        
    
    def perimeter(self):
        return 4*self.side
    
obj=Square(9)
print("Area of square:",obj.area())
print("Perimeter of square:",obj.perimeter())