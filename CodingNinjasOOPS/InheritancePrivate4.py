
class vehicle:
    def __init__(self,color):
        self.__color = color

    def getColor(self):
        return self.__color
    def setColor(self,color):
        return self.__color

    def printCar(self):
        print("Car is of Color :",self.__color)

class Car(vehicle):
    def print_Car(self):
        self.printCar()
        super().printCar()
        print("This is pretty Good")

c = Car("Blue")
c.print_Car()