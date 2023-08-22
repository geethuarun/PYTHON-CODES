# from abc import ABC,abstractmethod
# class Ide(ABC):
#     @abstractmethod
#     def debug(self):
#         pass

# class Pycharm(Ide):
#     def debug(self):
#         print("phycharm debug method")

# class Eclipse(Ide):
#     def debug(self):
#         print("Eclipse debugging")

# phy=Pycharm()
# phy.debug()


from abc import ABC,abstractmethod
@abstractmethod
class Shape(ABC):
    def draw(self):
        pass

class rectangle(Shape):
    def draw(self):
        print("Draw rectangle")

class triangle(Shape):
    def draw(self):
        print("Draw triangle")

dr=rectangle()
dr.draw()


