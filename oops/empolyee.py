# class Employee:
#     id:int
#     name:str
#     desig:str
#     salary:int
#     def set_emp(self,id,nam,desi,sal):
#         self.id=id
#         self.name=nam
#         self.desig=desi
#         self.salary=sal

#     def get_emp(self):
#         print(self.id,self.name,self.desig,self.salary)

# emp=Employee()
# emp.set_emp(12,"geethu","hr",50000)
# emp.get_emp()
    

#using constructor
class Employee:
    id:int
    name:str
    desig:str
    salary:int
    def __init__(self,id,nam,desi,sal):
        self.id=id
        self.name=nam
        self.desig=desi
        self.salary=sal

    def get_emp(self):
        print(self.id,self.name,self.desig,self.salary)


emp=Employee(12,"geethu","hr",50000)
emp.get_emp()