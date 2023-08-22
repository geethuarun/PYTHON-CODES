# from abc import ABC,abstractmethod

# class Bike(ABC):
#     name:str
#     model:str
#     fuel_type:str
#     def __init__(self,name,model,fuel_type):
#          self.name=name
#          self.model=model
#          self.fuel_type=fuel_type

#     @abstractmethod
#     def start(self):
#          pass

# class Hunter(Bike):
#     def __init__(self, name, model, fuel_type):
#           super().__init__(name, model, fuel_type)

#     def start(self):
#          print(f"{self.name} starting model {self.model} fuel {self.fuel_type}")

# obj=Hunter("ather","2023","petrol")
# obj.start()


from abc import ABC,abstractmethod
class Createview(ABC):
    model:str
    template_name=str
    form_class=str
    def __init__(self,model,template_name,form_class):
        self.model=model
        self.template_name=template_name
        self.form_class=form_class

    @abstractmethod
    def create(self):
        pass

class Employee_create(Createview):
    def __init__(self, model, template_name, form_class):
        super().__init__(model, template_name, form_class)

    def create(self):
        print("functionality for creating object")

obj=Employee_create("employee","html","empform")
obj.create()