from abc import ABC,abstractmethod
class Employee(ABC):
    designation:str
    salary:str
    def __init__(self,desi,sal):
        self.designation=desi
        self.salary=sal
    

    @abstractmethod
    def calculate_salary(self):
        pass

class Manager(Employee):
     def __init__(self,desi,sal):
         super().__init__(desi,sal)

     def calculate_salary(self):
        
         print(f"{self.designation} salary is {self.salary+25000}")

class Developer(Employee):
    def __init__(self,desi,sal):
        super().__init__(desi,sal)

    def calculate_salary(self,amount):
        self.salary+=amount
        
        print(f"{self.designation} salary is {self.salary}")

obj=Manager("manager",25000)
obj.calculate_salary()
obj1=Developer("developer",20000)
obj1.calculate_salary(1000)
