# Question1


class Student:
    name:str
    age:int
    grade:str

    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def get_student(self):
        print(f"Student name {self.name} has age {self.age} got {self.grade} grade")

obj=Student("Gowri",3,"A")
obj.get_student()