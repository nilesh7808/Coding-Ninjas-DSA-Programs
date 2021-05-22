
# Accessing the private members in python Inheritance
class vehicle:
    def __init__(self, color, maxSpeed):
        self.color = color
        self.__maxSpeed = maxSpeed  # this is a private inheritance member

    def getMaxSpeed(self):
        return self.__maxSpeed
    def setMaxSpeed(self,maxSpeed):
        return self.__maxSpeed

    def Print(self):
        print("Color :", self.color)
        print("Max Speed :",self.__maxSpeed)

class Car(vehicle):
    def __init__(self, color, __maxSpeed, numGears, isConvertible):
        super().__init__(color,__maxSpeed)
        self.numGears = numGears
        self.isConvertible = isConvertible

    def printCar(self):
        #super().Print() #1st Way
        self.Print()  #2nd Way
        # print("Color :",self.color)
        # print("Max Speed :",self.getMaxSpeed())
        print("Number of Gears",self.numGears)
        print("Is Convertible :",self.isConvertible)

c = Car("Red",245,4,True)
c.printCar()