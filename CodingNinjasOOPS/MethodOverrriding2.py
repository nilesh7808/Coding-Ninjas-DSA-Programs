
class vehicle:

    def __init__(self,color):
        self.color = color

    def print(self):
        print("The color of Car is:",self.color)

class Car(vehicle):

    def print(self):
        super().print()         # Now it will look to the parent class
        print("This is Pretty Good ")

c = Car("Black")
c.print()