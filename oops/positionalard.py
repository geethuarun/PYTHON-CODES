# def create_person(*args):# *args=("hari",35} tuple format
#     print(args)

# create_person("hari",35)



# def create_person(**kwargs):# **kwargs={"name":"hari","age":35} dictionary format
#     print(kwargs)

# create_person(name="hari",age=35)



class Student:
    rolno:int
    name:str
    course:str

    def __init__(self,**kwargs):#kwargs={"rolno"="1000","name"="vijay"}
        self.rolno=kwargs.get("rolno")
        self.name=kwargs.get("name")


    def __str__(self):#otherwise o/p will not be understandable
        return self.name

    def get(self):
        print(self.rolno,self.name)


obj=Student(rolno=1000,name="vijay")
print(obj)#__str__
        