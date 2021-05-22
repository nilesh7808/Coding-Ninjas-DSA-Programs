
class vehicle:
    def __init__(self,color):
        self.__color = color
    def getColor(self):
        return self.__color
    def setColor(self,color):
        return self.__color

class Car(vehicle):
    def print_Car(self):
        print("Color is :",self.getColor())

c = Car("Red")
c.print_Car()