#using constructor

class Student:
    rollno:int
    name:str
    course:str

    def __init__(self,rol,name,course):
        self.rolno=rol
        self.name=name
        self.course=course

    def get_student(self):
        print(self.rolno,self.name,self.course)

stu=Student(12,"Arun","phython")
stu.get_student()