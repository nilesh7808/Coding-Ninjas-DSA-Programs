# abstract classes and abstract methods
from abc import ABC,abstractmethod
class Automobile(ABC):
    def __init__(self,no_of_Wheels):
        self.no_of_Wheels = no_of_Wheels
        print("Abstract class "+"(Automobile)"+" has been created.")

    @abstractmethod
    def start(self):
        print("Start of Automobile has been called")
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def drive(self):
        pass
    @abstractmethod
    def get_no_of_wheels(self):
        return self.no_of_Wheels

class Truck(Automobile):
    # def __init__(self,name):
    #     super().__init__()
    #     super().start()
    #     self.name = name
    #     print("Truck has been created.")

    def start(self):
        print("Start of Truck has been called")
    def stop(self):
        pass
    def drive(self):
        pass
    def get_no_of_wheels(self):
        return super().get_no_of_wheels()

class Bus(Automobile):
    # def __init__(self,name):
    #     super().__init__()
    #     print("Bus has been created.")
    #     self.name = name

    def start(self):
        pass
    def stop(self):
        pass
    def drive(self):
        pass
    def get_no_of_wheels(self):
        return super().get_no_of_wheels()
T = Truck(8)
B = Bus(4)
print(T.get_no_of_wheels())
print(B.get_no_of_wheels())
#T.start()
#A = Automobile()   :- Give error = TypeError: Can't instantiate abstract class Automobile with abstract methods drive, start, stop
#b = Bus("BSRCTC")