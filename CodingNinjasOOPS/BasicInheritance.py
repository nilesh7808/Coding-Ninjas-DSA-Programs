class vehicle: # superclass or parent class or base class
    def __init__(self, color, maxSpeed):
        self.color = color
        self.maxSpeed = maxSpeed
class Car(vehicle): # sub-class or child class or derived class
    def __init__(self, color, maxSpeed, numGears, isConvertible):
        super().__init__(color, maxSpeed)
        self.numGears = numGears
        self.isConvertible = isConvertible

    def printCar(self):
        print("Color :",self.color)
        print("Max Speed :",self.maxSpeed)
        print("Number of Gears",self.numGears)
        print("Is Convertible :",self.isConvertible)

c = Car("Red",245,4,True)
c.printCar()