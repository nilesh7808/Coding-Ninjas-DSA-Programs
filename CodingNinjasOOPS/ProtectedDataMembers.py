# Protected Data Members

class vehicle:
    def __init__(self,color,speed):
        self._color = color
        self.speed = speed

    def getColor(self):
        return self._color

    def setColor(self,color):
        self._color = color

    def print(self):
        print("Now Car is :",self._color)
        print("Speed :",self.speed)

class Car(vehicle):
    def __init__(self,color,speed):
        super().__init__(color,speed)

    def print(self):
        print("Car is:",self._color)
        print("This is sensible coding what Python thinks ")

c = Car("Black",45)
c.print()
v = vehicle("Red", 45)
print()
v._color = "Green"
v.print()